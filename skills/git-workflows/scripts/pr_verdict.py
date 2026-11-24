#!/usr/bin/env python3
"""Say whether a commit's checks are green, and if not, exactly why.

A session driving a pull request runs this instead of reading checks off a page or a command's
printed output. It reads everything from GitHub's REST API:

- the checks the base branch requires: the `required_status_checks` rules from
  `GET /repos/{owner}/{repo}/rules/branches/{branch}`, with any classic branch protection's
  contexts from `GET /repos/{owner}/{repo}/branches/{branch}` (a branch without it adds none);
- every check run on the commit, 100 to a page, of which only the newest of each name counts,
  since a re-run supersedes the run before it;
- every workflow run for the commit, to tell a required check still to come from one that
  never will.

    pr_verdict.py --repo OWNER/NAME --pr 42
    pr_verdict.py --repo OWNER/NAME --sha <40 hex digits> [--branch main] [--logs]

It prints the verdict, then one line for each check that isn't a plain pass, saying what to do.
The worst verdict wins, in this order, and sets the exit status:

    1 FAILED     a check failed or timed out, required or not: a red optional check on the
                 default branch is still a red default branch
    3 BLOCKED    a required check hasn't reported and every workflow run has finished, so it
                 never will: the rules name a job that no longer runs, which only the owner
                 can change
    4 CANCELLED  the newest run of a required check was canceled, usually by a newer push:
                 judge the newest head instead
    2 PENDING    something is queued or running, required or not, or nothing has reported yet
    0 GREEN      every required check passed, and nothing else failed or runs
    5            no verdict: the API couldn't be read, or the arguments were wrong. Never
                 read this as green.

`--logs` prints, for each failed job, every line of its log that names a failure: pytest's
`FAILED` and `ERROR` lines, its summary line, and `##[error]` lines. One line from the end
of a log hides every other failing test.

Limits: a commit is judged against the rules as they are now, so a commit made before a
required job existed reads BLOCKED for it; judge the newest commit. Only check runs are
read, not commit statuses, so a required check reported only as a status reads as missing,
as does one from a service outside GitHub Actions while the commit's workflows have finished.

A token in GITHUB_TOKEN or GH_TOKEN raises the rate limit, and reads a private repository;
without one, a public repository is read unauthenticated. Standard library only, Python 3.10
or later.
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

API = "https://api.github.com"
PER_PAGE = 100
MAX_PAGES = 50
TIMEOUT_SECONDS = 30

GREEN, PENDING, CANCELLED, BLOCKED, FAILED = "GREEN", "PENDING", "CANCELLED", "BLOCKED", "FAILED"
UNREADABLE = "UNREADABLE"
# Worst first: the first verdict any check earns, in this order, is the commit's.
ORDER = (FAILED, BLOCKED, CANCELLED, PENDING)
EXIT = {GREEN: 0, FAILED: 1, PENDING: 2, BLOCKED: 3, CANCELLED: 4, UNREADABLE: 5}
NOTE = "NOTE"  # a line worth printing that changes no verdict

PASSED = {"success", "neutral", "skipped"}
CANCELED = {"cancelled", "stale"}  # GitHub's spelling; stale is a run GitHub gave up on

REPO = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
SHA = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
JOB = re.compile(r"/job/(\d+)")
ANSI = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
TIMESTAMP = re.compile(r"^\ufeff?\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z ?")
PYTEST_SUMMARY = re.compile(
    r"^=+ .*\b\d+ (?:failed|passed|errors?|skipped|deselected|xfailed|xpassed|warnings?)\b"
    r".* in \d[\d.]*s\b"
)
NAMES_FAILURE = re.compile(r"^(?:FAILED |ERROR |##\[error\])")

Fetch = Callable[[str], bytes]


class Unreadable(Exception):
    """GitHub's answer couldn't be read, or wasn't the shape its docs give: no verdict."""


@dataclass
class Commit:
    """What the verdict is judged from."""

    sha: str
    branch: str
    required: set[str]
    check_runs: list[dict[str, Any]]
    workflow_runs: list[dict[str, Any]]


@dataclass
class Verdict:
    name: str
    lines: list[str] = field(default_factory=list)

    @property
    def code(self) -> int:
        return EXIT[self.name]


def http_fetch(auth: str | None) -> Fetch:
    """A fetch that reads GitHub's API, sending the token to GitHub only.

    The token goes in an unredirected header, so a job log's redirect to its storage host
    doesn't carry it there.
    """

    def fetch(url: str) -> bytes:
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "pr-verdict",
            },
        )
        if auth:
            request.add_unredirected_header("Authorization", f"Bearer {auth}")
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                return response.read()
        except (OSError, http.client.HTTPException) as error:
            raise Unreadable(f"{url}: {error}") from error

    return fetch


class GitHub:
    """GitHub's REST API for one repository, read through a fetch the tests replace."""

    def __init__(self, repo: str, fetch: Fetch) -> None:
        self.repo = repo
        self.fetch = fetch

    def url(self, path: str, params: dict[str, Any] | None = None) -> str:
        query = f"?{urllib.parse.urlencode(params)}" if params else ""
        return f"{API}/repos/{self.repo}{path}{query}"

    def json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        url = self.url(path, params)
        try:
            return json.loads(self.fetch(url))
        except (ValueError, UnicodeDecodeError) as error:
            raise Unreadable(f"{url}: not JSON ({error})") from error

    def pages(self, path: str, key: str, params: dict[str, Any]) -> list[dict[str, Any]]:
        """Every item of a paginated list, reading pages until one comes back short."""
        items: list[dict[str, Any]] = []
        for page in range(1, MAX_PAGES + 1):
            body = self.json(path, {**params, "per_page": PER_PAGE, "page": page})
            batch = body.get(key) if isinstance(body, dict) else None
            if not isinstance(batch, list):
                raise Unreadable(f"{self.url(path)}: the answer has no list of {key}")
            items += batch
            if len(batch) < PER_PAGE:
                return items
        raise Unreadable(f"{self.url(path)}: more than {MAX_PAGES} pages of {key}")

    def text(self, path: str) -> str:
        return self.fetch(self.url(path)).decode("utf-8", errors="replace")


def required_checks(api: GitHub, branch: str) -> set[str]:
    """The check names the branch's rulesets and classic protection require."""
    where = f"/{urllib.parse.quote(branch, safe='/')}"
    rules = api.json(f"/rules/branches{where}")
    if not isinstance(rules, list):
        raise Unreadable(f"{api.url('/rules/branches' + where)}: not a list of rules")
    names = set()
    for rule in rules:
        if rule.get("type") == "required_status_checks":
            for check in rule.get("parameters", {}).get("required_status_checks", []):
                names.add(check["context"])
    protection = api.json(f"/branches{where}").get("protection") or {}
    classic = protection.get("required_status_checks") or {}
    names.update(classic.get("contexts") or [])
    names.update(check["context"] for check in classic.get("checks") or [])
    return names


def gather(api: GitHub, pr: int | None = None, sha: str = "", branch: str | None = None) -> Commit:
    """Everything the verdict needs, read from the API: a pull request's head, or `sha`."""
    try:
        if pr is not None:
            pull = api.json(f"/pulls/{pr}")
            sha = pull["head"]["sha"]
            branch = branch or pull["base"]["ref"]
        elif branch is None:
            branch = api.json("")["default_branch"]
        return Commit(
            sha=sha,
            branch=branch,
            required=required_checks(api, branch),
            check_runs=api.pages(f"/commits/{sha}/check-runs", "check_runs", {"filter": "all"}),
            workflow_runs=api.pages("/actions/runs", "workflow_runs", {"head_sha": sha}),
        )
    except (KeyError, TypeError, AttributeError) as error:
        raise Unreadable(f"an answer wasn't the shape GitHub documents ({error!r})") from error


def newest(check_runs: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """The newest run of each check name. GitHub numbers runs in the order it makes them."""
    latest: dict[str, dict[str, Any]] = {}
    for run in check_runs:
        name = run["name"]
        if name not in latest or run["id"] > latest[name]["id"]:
            latest[name] = run
    return latest


def judge(commit: Commit) -> Verdict:
    """The verdict and its lines, worst first. Pure: it reads only what `gather` returned."""
    try:
        latest = newest(commit.check_runs)
        workflows_done = all(run["status"] == "completed" for run in commit.workflow_runs)
        found = list(_check_lines(latest, commit.required))
        found += _missing_lines(latest, commit.required, workflows_done)
        found += _workflow_lines(commit.workflow_runs)
    except (KeyError, TypeError) as error:
        raise Unreadable(f"a run wasn't the shape GitHub documents ({error!r})") from error
    if not latest and not commit.workflow_runs:
        found.append((PENDING, "nothing has reported on this commit yet; run this again soon"))
    rank = {name: index for index, name in enumerate((*ORDER, NOTE))}
    found.sort(key=lambda item: (rank[item[0]], item[1]))
    name = next((kind for kind in ORDER if any(k == kind for k, _ in found)), GREEN)
    lines = [line for _, line in found]
    if name == BLOCKED:
        lines.append(
            "A commit is judged against the rules as they are now: one made before a required "
            "job existed reads BLOCKED for it. Judge the newest commit before asking the owner."
        )
    return Verdict(name, lines)


def _check_lines(latest: dict[str, dict[str, Any]], required: set[str]):
    for name, run in sorted(latest.items()):
        label = f"{name} (required)" if name in required else name
        status, conclusion = run["status"], run.get("conclusion")
        if status != "completed":
            yield PENDING, f"{label}: {status}. Wait for it to finish, then run this again."
        elif conclusion in PASSED:
            continue
        elif conclusion in CANCELED and name in required:
            yield (
                CANCELLED,
                f"{label}: its newest run was {conclusion}, usually by a newer push. Judge the "
                "newest head; if this is the newest, re-run it once.",
            )
        elif conclusion in CANCELED:
            yield NOTE, f"{label}: {conclusion}. Not required, so it doesn't block."
        else:
            yield (
                FAILED,
                f"{label}: {conclusion}. Read its log (--logs prints the failing lines), "
                f"fix the cause and push: {run.get('details_url') or run.get('html_url')}",
            )


def _missing_lines(latest: dict[str, dict[str, Any]], required: set[str], done: bool):
    for name in sorted(required - latest.keys()):
        if done:
            yield (
                BLOCKED,
                f"{name} (required): never reported, and every workflow run for this commit "
                "has finished. The rules name a job that no longer runs; only the owner can "
                "change the rules. Report it, and don't merge around it.",
            )
        else:
            yield PENDING, f"{name} (required): hasn't reported yet, and workflows still run."


def _workflow_lines(workflow_runs: list[dict[str, Any]]):
    for run in workflow_runs:
        conclusion = run.get("conclusion")
        if run["status"] != "completed":
            continue
        if conclusion == "startup_failure":
            yield (
                FAILED,
                f"workflow {run['name']}: failed to start, so none of its jobs ran. Fix the "
                f"workflow file: {run.get('html_url')}",
            )
        elif conclusion == "action_required":
            yield (
                PENDING,
                f"workflow {run['name']}: waits for someone with write access to approve it: "
                f"{run.get('html_url')}",
            )


def failure_lines(log: str) -> list[str]:
    """Every line of a job's log that names a failure, in order, without its timestamp."""
    found = []
    for raw in log.splitlines():
        line = TIMESTAMP.sub("", ANSI.sub("", raw)).rstrip()
        if NAMES_FAILURE.match(line) or PYTEST_SUMMARY.match(line):
            found.append(line)
    return found


def job_id(run: dict[str, Any]) -> int | None:
    """The Actions job behind a check run, or None for a check from anywhere else."""
    match = JOB.search(run.get("details_url") or "")
    if match:
        return int(match.group(1))
    if (run.get("app") or {}).get("slug") == "github-actions":
        return run["id"]
    return None


def log_lines(api: GitHub, commit: Commit) -> list[str]:
    """Each failed job's failing lines, under its name. A log that can't be read is said so."""
    out = []
    for name, run in sorted(newest(commit.check_runs).items()):
        if run["status"] != "completed" or run.get("conclusion") in PASSED | CANCELED:
            continue
        job = job_id(run)
        if job is None:
            out.append(f"{name}: not a GitHub Actions job; read it at {run.get('details_url')}")
            continue
        try:
            lines = failure_lines(api.text(f"/actions/jobs/{job}/logs"))
        except Unreadable as error:
            out.append(f"{name}: its log couldn't be read ({error}); a token may be needed")
            continue
        if not lines:
            out.append(f"{name}: no line of its log names a failure; read it whole")
            continue
        out.append(f"{name}, job {job}:")
        out += [f"    {line}" for line in lines]
    return out


class _Parser(argparse.ArgumentParser):
    """A usage error exits 5, no verdict, since argparse's own 2 would read as PENDING."""

    def error(self, message: str):  # type: ignore[override]
        self.print_usage(sys.stderr)
        print(f"{self.prog}: error: {message}", file=sys.stderr)
        raise SystemExit(EXIT[UNREADABLE])


def arguments(argv: list[str] | None) -> argparse.Namespace:
    parser = _Parser(description="Say whether a commit's checks are green, and if not, why.")
    parser.add_argument("--repo", required=True, help="OWNER/NAME")
    which = parser.add_mutually_exclusive_group(required=True)
    which.add_argument("--pr", type=int, help="judge this pull request's head commit")
    which.add_argument("--sha", help="judge this commit, by its full SHA")
    parser.add_argument("--branch", help="the base branch whose rules apply")
    parser.add_argument("--logs", action="store_true", help="print each failed job's failures")
    args = parser.parse_args(argv)
    if not REPO.fullmatch(args.repo):
        parser.error(f"--repo must be OWNER/NAME, not {args.repo!r}")
    if args.sha is not None and not SHA.fullmatch(args.sha):
        parser.error("--sha must be a full commit SHA, in lowercase hex")
    return args


def main(argv: list[str] | None = None, fetch: Fetch | None = None) -> int:
    args = arguments(argv)
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    api = GitHub(args.repo, fetch or http_fetch(token))
    try:
        commit = gather(api, pr=args.pr, sha=args.sha or "", branch=args.branch)
        verdict = judge(commit)
    except Unreadable as error:
        print(f"{UNREADABLE}: {error}")
        print("No verdict. This is not green: read the checks again, or report it.")
        return EXIT[UNREADABLE]
    print(
        f"{verdict.name}: {args.repo} {commit.sha[:12]}, against {commit.branch}'s rules "
        f"({len(commit.required)} required, {len(newest(commit.check_runs))} reported)"
    )
    for line in verdict.lines:
        print(f"  {line}")
    if args.logs:
        for line in log_lines(api, commit):
            print(f"  {line}")
    return verdict.code


if __name__ == "__main__":
    sys.exit(main())

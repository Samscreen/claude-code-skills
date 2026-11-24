"""The git-workflows skill's pr_verdict.py reads a commit's checks as its module says.

Every test answers the script's API calls from canned JSON, so none reaches the network.
"""

import ast
import http.client
import importlib.util
import io
import json
import stat
import sys
import urllib.error
from pathlib import Path

import pytest

SCRIPT = (
    Path(__file__).resolve().parent.parent
    / "skills"
    / "git-workflows"
    / "scripts"
    / "pr_verdict.py"
)
REPO = "example/repo"
SHA = "a" * 40


def load():
    spec = importlib.util.spec_from_file_location("pr_verdict", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


pv = load()


def url(path: str, **params) -> str:
    return pv.GitHub(REPO, None).url(path, params or None)


def check(ident: int, name: str, conclusion: str | None = "success", status: str = "completed"):
    return {
        "id": ident,
        "name": name,
        "status": status,
        "conclusion": conclusion if status == "completed" else None,
        "details_url": f"https://github.com/{REPO}/actions/runs/9/job/{ident}",
        "app": {"slug": "github-actions"},
    }


def workflow(name: str = "CI", status: str = "completed", conclusion: str | None = "success"):
    return {"name": name, "status": status, "conclusion": conclusion, "html_url": "https://x"}


def commit(required=(), checks=(), workflows=None) -> object:
    workflows = [workflow()] if workflows is None else workflows
    return pv.Commit(SHA, "main", set(required), list(checks), list(workflows))


class Fake:
    """GitHub's API from a table of canned answers; a missing URL is a 404."""

    def __init__(self, answers: dict[str, object]):
        self.answers = answers
        self.asked: list[str] = []

    def __call__(self, address: str) -> bytes:
        self.asked.append(address)
        if address not in self.answers:
            raise pv.Unreadable(f"{address}: HTTP Error 404: Not Found")
        answer = self.answers[address]
        if isinstance(answer, Exception):
            raise answer
        if isinstance(answer, bytes):
            return answer
        return json.dumps(answer).encode("utf-8")


def answers(required=(), checks=(), workflows=None, protection=None, sha=SHA, base="main"):
    """A pull request, 42, whose head is `sha`, into `base`, with its checks and rules."""
    workflows = [workflow()] if workflows is None else workflows
    rules = [
        {
            "type": "required_status_checks",
            "parameters": {"required_status_checks": [{"context": name} for name in required]},
        },
        {"type": "deletion"},
    ]
    return {
        url("/pulls/42"): {"head": {"sha": sha}, "base": {"ref": base}},
        url(f"/rules/branches/{base}"): rules,
        url(f"/branches/{base}"): {"name": base, "protection": protection},
        url(f"/commits/{sha}/check-runs", filter="all", per_page=100, page=1): {
            "total_count": len(checks),
            "check_runs": list(checks),
        },
        url("/actions/runs", head_sha=sha, per_page=100, page=1): {
            "total_count": len(workflows),
            "workflow_runs": list(workflows),
        },
    }


def main(capsys, table, *argv):
    code = pv.main(["--repo", REPO, *(argv or ("--pr", "42"))], fetch=Fake(table))
    return code, capsys.readouterr().out


@pytest.mark.parametrize(
    ("required", "checks", "workflows", "verdict"),
    [
        (["test"], [check(1, "test"), check(2, "lint")], None, "GREEN"),
        (["test"], [check(1, "test", "skipped"), check(2, "docs", "neutral")], None, "GREEN"),
        (["test"], [check(1, "test", "failure")], None, "FAILED"),
        # A red optional check is still red.
        (["test"], [check(1, "test"), check(2, "lint", "failure")], None, "FAILED"),
        (["test"], [check(1, "test", "timed_out")], None, "FAILED"),
        (["test"], [check(1, "test", "action_required")], None, "FAILED"),
        (["test", "gone"], [check(1, "test")], None, "BLOCKED"),
        (["test"], [check(1, "test", "cancelled")], None, "CANCELLED"),
        (["test"], [check(1, "test", "stale")], None, "CANCELLED"),
        (["test"], [check(1, "test", status="in_progress")], None, "PENDING"),
        (["test"], [check(1, "test"), check(2, "slow", status="queued")], None, "PENDING"),
        # A required check not yet reported while a workflow runs is still to come.
        (["test"], [], [workflow(status="in_progress")], "PENDING"),
        ([], [], [], "PENDING"),
        (
            [],
            [check(1, "test")],
            [workflow("CI"), workflow("Bad", conclusion="startup_failure")],
            "FAILED",
        ),
        ([], [], [workflow(conclusion="action_required")], "PENDING"),
    ],
)
def test_each_verdict(required, checks, workflows, verdict):
    assert pv.judge(commit(required, checks, workflows)).name == verdict


@pytest.mark.parametrize(
    ("checks", "verdict"),
    [
        ([check(1, "a", "failure"), check(2, "b", "cancelled")], "FAILED"),
        ([check(1, "b", "cancelled"), check(2, "c", status="queued")], "BLOCKED"),
        (
            [check(1, "b", "cancelled"), check(2, "c", status="queued"), check(3, "gone")],
            "CANCELLED",
        ),
        ([check(1, "b"), check(2, "c", status="queued"), check(3, "gone")], "PENDING"),
    ],
)
def test_the_worst_verdict_wins(checks, verdict):
    assert pv.judge(commit(["b", "gone"], checks)).name == verdict


def test_lines_come_worst_first_and_each_says_what_to_do():
    checks = [check(1, "b", "cancelled"), check(2, "c", status="queued"), check(3, "a", "failure")]
    lines = pv.judge(commit(["b", "gone"], checks)).lines
    assert lines[0].startswith("a: failure. Read its log")
    assert lines[1].startswith("gone (required): never reported")
    assert lines[2].startswith("b (required): its newest run was cancelled")
    assert lines[3].startswith("c: queued. Wait")
    assert len(lines) == 4


def test_an_optional_cancelled_check_is_noted_but_does_not_block():
    verdict = pv.judge(commit(["test"], [check(1, "test"), check(2, "docs", "cancelled")]))
    assert verdict.name == "GREEN"
    assert verdict.lines == ["docs: cancelled. Not required, so it doesn't block."]


def test_blocked_says_the_commit_is_judged_against_todays_rules():
    verdict = pv.judge(commit(["gone"], [check(1, "test")]))
    assert verdict.code == 3
    assert "Judge the newest commit" in verdict.lines[-1]


@pytest.mark.parametrize(
    ("checks", "verdict"),
    [
        ([check(1, "test", "failure"), check(2, "test")], "GREEN"),
        ([check(2, "test"), check(1, "test", "failure")], "GREEN"),
        ([check(1, "test"), check(3, "test", "failure")], "FAILED"),
        ([check(4, "test", "cancelled"), check(5, "test", status="queued")], "PENDING"),
    ],
)
def test_only_the_newest_run_of_each_check_counts(checks, verdict):
    assert pv.judge(commit(["test"], checks)).name == verdict


@pytest.mark.parametrize("extra", [30, 0])
def test_every_page_of_check_runs_is_read(extra):
    checks = [check(n, f"job {n}") for n in range(1, 101 + extra)]
    table = answers(["job 1"], checks[:100])
    table[url(f"/commits/{SHA}/check-runs", filter="all", per_page=100, page=2)] = {
        "check_runs": checks[100:]
    }
    fake = Fake(table)
    found = pv.gather(pv.GitHub(REPO, fake), pr=42)
    assert len(found.check_runs) == 100 + extra
    assert sum("check-runs" in asked for asked in fake.asked) == 2


def test_a_list_longer_than_the_page_limit_is_unreadable(monkeypatch):
    monkeypatch.setattr(pv, "MAX_PAGES", 2)
    full = {"check_runs": [check(n, "x") for n in range(100)]}
    fake = Fake({url("/c", per_page=100, page=p): full for p in (1, 2)})
    with pytest.raises(pv.Unreadable, match="more than 2 pages"):
        pv.GitHub(REPO, fake).pages("/c", "check_runs", {})


def test_required_checks_join_every_ruleset_and_classic_protection():
    table = answers(["test"], protection={"required_status_checks": {"contexts": ["legacy"]}})
    rules = table[url("/rules/branches/main")]
    rules.append(
        {
            "type": "required_status_checks",
            "parameters": {"required_status_checks": [{"context": "org-wide"}]},
        }
    )
    table[url("/branches/main")]["protection"]["required_status_checks"]["checks"] = [
        {"context": "by-app", "app_id": 1}
    ]
    found = pv.required_checks(pv.GitHub(REPO, Fake(table)), "main")
    assert found == {"test", "org-wide", "legacy", "by-app"}


@pytest.mark.parametrize("protection", [None, {"enabled": False}, {"required_status_checks": None}])
def test_a_branch_without_classic_protection_adds_nothing(protection):
    table = answers(["test"])
    table[url("/branches/main")] = {"name": "main", "protection": protection}
    assert pv.required_checks(pv.GitHub(REPO, Fake(table)), "main") == {"test"}


def test_a_pull_request_is_judged_on_its_head_against_its_base(capsys):
    table = answers(["test"], [check(1, "test"), check(2, "lint", "failure")], base="release")
    code, out = main(capsys, table)
    assert code == 1
    first, *rest = out.splitlines()
    assert first == f"FAILED: {REPO} {SHA[:12]}, against release's rules (1 required, 2 reported)"
    assert rest == [
        f"  lint: failure. Read its log (--logs prints the failing lines), fix the cause and "
        f"push: https://github.com/{REPO}/actions/runs/9/job/2"
    ]


def test_a_green_commit_prints_only_its_verdict(capsys):
    code, out = main(capsys, answers(["test"], [check(1, "test")]))
    assert code == 0
    assert out.startswith("GREEN: ")
    assert len(out.splitlines()) == 1


@pytest.mark.parametrize(("branch", "expected"), [((), "main"), (("--branch", "next"), "next")])
def test_a_commit_takes_the_default_branch_unless_one_is_named(capsys, branch, expected):
    table = answers(["test"], [check(1, "test")], base=expected)
    table[url("")] = {"default_branch": "main"}
    code, out = main(capsys, table, "--sha", SHA, *branch)
    assert code == 0, out
    assert f"against {expected}'s rules" in out


@pytest.mark.parametrize(
    "break_it",
    [
        lambda table: table.pop(url("/pulls/42")),
        lambda table: table.update({url("/pulls/42"): b"<html>rate limited</html>"}),
        lambda table: table.update({url("/pulls/42"): {"message": "Not Found"}}),
        lambda table: table.update({url("/rules/branches/main"): {"message": "Bad"}}),
        lambda table: table.update({url("/branches/main"): ["not", "a", "branch"]}),
        lambda table: table.update(
            {url(f"/commits/{SHA}/check-runs", filter="all", per_page=100, page=1): {"x": 1}}
        ),
        lambda table: table.update(
            {url("/actions/runs", head_sha=SHA, per_page=100, page=1): {"workflow_runs": [{}]}}
        ),
        lambda table: table.update(
            {
                url(f"/commits/{SHA}/check-runs", filter="all", per_page=100, page=1): {
                    "check_runs": [{"name": "test"}]
                }
            }
        ),
    ],
)
def test_an_answer_it_cannot_read_gives_no_verdict(capsys, break_it):
    table = answers(["test"], [check(1, "test")])
    break_it(table)
    code, out = main(capsys, table)
    assert code == 5
    assert out.startswith("UNREADABLE: ")
    assert "GREEN" not in out
    assert "This is not green" in out


LOG = "\n".join(
    [
        "\ufeff2026-11-24T10:00:00.0000000Z ##[group]Run uv run pytest",
        "2026-11-24T10:00:01.1234567Z tests/test_a.py::test_one PASSED",
        "2026-11-24T10:00:01.2234567Z tests/test_a.py::test_two FAILED",
        "2026-11-24T10:00:02.0000000Z =========== short test summary info ============",
        "2026-11-24T10:00:02.1000000Z FAILED tests/test_a.py::test_two - assert 1 == 2",
        "2026-11-24T10:00:02.2000000Z \x1b[31mFAILED\x1b[0m tests/test_b.py::test_three - KeyError",
        "2026-11-24T10:00:02.3000000Z ERROR tests/test_c.py - ImportError: no module named x",
        "2026-11-24T10:00:02.4000000Z === 2 failed, 5 passed, 1 error in 3.21s ===",
        "2026-11-24T10:00:02.5000000Z ##[error]Process completed with exit code 1.",
        "2026-11-24T10:00:02.6000000Z Post job cleanup.",
    ]
)


def test_log_lines_name_every_failure_not_only_the_last():
    assert pv.failure_lines(LOG) == [
        "FAILED tests/test_a.py::test_two - assert 1 == 2",
        "FAILED tests/test_b.py::test_three - KeyError",
        "ERROR tests/test_c.py - ImportError: no module named x",
        "=== 2 failed, 5 passed, 1 error in 3.21s ===",
        "##[error]Process completed with exit code 1.",
    ]


def test_a_passing_log_names_only_its_summary():
    log = "tests/test_a.py::test_one PASSED\n===== 5 passed in 0.12s =====\nDone.\n"
    assert pv.failure_lines(log) == ["===== 5 passed in 0.12s ====="]


@pytest.mark.parametrize(
    ("run", "expected"),
    [
        ({"id": 7, "details_url": "https://github.com/o/r/actions/runs/1/job/99"}, 99),
        ({"id": 7, "details_url": None, "app": {"slug": "github-actions"}}, 7),
        ({"id": 7, "details_url": "https://ci.example.com/7", "app": {"slug": "other"}}, None),
    ],
)
def test_the_job_behind_a_check_run(run, expected):
    assert pv.job_id(run) == expected


def test_logs_print_each_failed_jobs_failing_lines(capsys):
    outside = {
        **check(3, "external", "failure"),
        "details_url": "https://ci.example.com/3",
        "app": {"slug": "other"},
    }
    checks = [
        check(1, "test", "failure"),
        check(2, "lint", "failure"),
        outside,
        check(4, "quiet", "failure"),
        check(5, "docs"),
    ]
    table = answers(["test"], checks)
    table[url("/actions/jobs/1/logs")] = LOG.encode("utf-8")
    table[url("/actions/jobs/2/logs")] = pv.Unreadable("HTTP Error 403: Forbidden")
    table[url("/actions/jobs/4/logs")] = b"all fine\n"
    fake = Fake(table)
    code = pv.main(["--repo", REPO, "--pr", "42", "--logs"], fetch=fake)
    out = capsys.readouterr().out
    assert code == 1  # a log that can't be read changes no verdict
    assert "  external: not a GitHub Actions job; read it at https://ci.example.com/3" in out
    assert "  lint: its log couldn't be read (HTTP Error 403: Forbidden)" in out
    assert "  quiet: no line of its log names a failure; read it whole" in out
    assert "  test, job 1:\n      FAILED tests/test_a.py::test_two - assert 1 == 2\n" in out
    assert "      ##[error]Process completed with exit code 1.\n" in out
    assert not any("/jobs/5/" in asked for asked in fake.asked)  # a passing job's log isn't read


@pytest.mark.parametrize(
    "argv",
    [
        ["--repo", "example", "--pr", "1"],
        ["--repo", REPO, "--sha", "abc1234"],
        ["--repo", REPO, "--sha", SHA.upper()],
        ["--repo", REPO, "--pr", "1", "--sha", SHA],
        ["--repo", REPO],
    ],
)
def test_a_usage_error_exits_five_not_pending(argv, capsys):
    with pytest.raises(SystemExit) as raised:
        pv.main(argv, fetch=Fake({}))
    assert raised.value.code == 5
    assert "error:" in capsys.readouterr().err


class Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


@pytest.mark.parametrize("token", ["CHANGEME", None])
def test_the_token_goes_to_github_only(monkeypatch, token):
    seen = []

    def urlopen(request, timeout):
        seen.append(request)
        return Response(b"{}")

    monkeypatch.setattr(pv.urllib.request, "urlopen", urlopen)
    assert pv.http_fetch(token)("https://api.github.com/repos/example/repo") == b"{}"
    [request] = seen
    # An unredirected header isn't carried to the host a job log redirects to.
    assert "Authorization" not in request.headers
    expected = {"Authorization": f"Bearer {token}"} if token else {}
    assert request.unredirected_hdrs == expected
    assert request.headers["Accept"] == "application/vnd.github+json"


@pytest.mark.parametrize(
    "error",
    [
        urllib.error.URLError("rate limit exceeded"),
        TimeoutError("timed out"),
        http.client.IncompleteRead(b"{"),
    ],
    ids=["refused", "timeout", "cut-short"],
)
def test_a_failed_request_is_unreadable(monkeypatch, error):
    def urlopen(request, timeout):
        raise error

    monkeypatch.setattr(pv.urllib.request, "urlopen", urlopen)
    with pytest.raises(pv.Unreadable, match="api.github.com"):
        pv.http_fetch(None)("https://api.github.com/repos/example/repo")


def test_the_main_reads_the_token_from_the_environment(monkeypatch):
    made = []
    monkeypatch.setenv("GH_TOKEN", "CHANGEME")
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.setattr(pv, "http_fetch", lambda auth: made.append(auth) or Fake({}))
    assert pv.main(["--repo", REPO, "--pr", "1"]) == 5
    assert made == ["CHANGEME"]


def test_the_script_is_executable_and_uses_the_standard_library_only():
    assert SCRIPT.stat().st_mode & stat.S_IXUSR
    assert SCRIPT.read_text(encoding="utf-8").startswith("#!/usr/bin/env python3\n")
    tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
    imported = {
        alias.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {node.module.split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    assert imported <= set(sys.stdlib_module_names) | {"__future__"}

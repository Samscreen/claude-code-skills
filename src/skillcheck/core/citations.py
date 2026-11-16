"""Cited commits: every commit the records cite stays reachable from HEAD.

Pull requests here merge with a merge commit, so each commit a pull request, a record or a report
cites stays in `main`'s history. A squash or rebase-merge writes new commits and leaves the
branch's own behind, unreachable, and a later garbage collection deletes them. The owner
approved this rule on 2026-11-16 to hold that.

What it reads: `docs/decisions.md`, `CHANGELOG.md` and `ROADMAP.md`, each line, fences and code
spans included. A citation is a run of 7 to 40 lowercase hexadecimal characters, standing alone
(no letter, digit, underscore or hyphen either side), that holds at least one digit and at least
one letter. A run of digits alone is a number, such as a workflow run's ID, and a run of letters
alone is a word, such as `defaced`. A commit whose short form is all digits or all letters is
cited by a longer prefix, which isn't. Longer runs, such as a SHA-256, aren't citations.

How each is judged:

- It resolves to a commit here (`git rev-parse --verify --quiet <hash>^{commit}`) that HEAD
  reaches (`git merge-base --is-ancestor`): it passes.
- It resolves to a commit HEAD doesn't reach: it fails, naming the file, line and hash.
- It names no commit here, or more than one: it fails, unless `.github/foreign-hashes.txt`
  lists it. That file holds each hash in the records that is something else, such as another
  repository's commit or a file's hash, one per line with what it is. Every run of that shape is
  taken as a commit citation unless listed, so a record that cites something else says so in a
  reviewed file, and a mistyped commit can't pass as a file's hash.

The rule needs the history. Where it has none it checks nothing and says why in the summary
line, with no finding: no `git`, a directory that isn't the root of a repository with a commit,
or a shallow clone, which is how CI checks out by default. A commit outside a shallow clone's
depth can't be told from one the history lost.
"""

import re
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path

Add = Callable[[str, str, str], None]

RECORDS = ("docs/decisions.md", "CHANGELOG.md", "ROADMAP.md")
FOREIGN = ".github/foreign-hashes.txt"
CITATION = re.compile(r"(?<![\w-])(?=[0-9a-f]*[0-9])(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}(?![\w-])")


def check(root: Path, add: Add) -> str:
    """Report each cited commit HEAD doesn't reach; return the summary line's part."""
    if shutil.which("git") is None:
        return "cited commits unchecked (no git)"
    state = _git(
        root, "rev-parse", "--show-toplevel", "--is-shallow-repository", "--verify", "HEAD"
    )
    if state.returncode != 0 or Path(state.stdout.split("\n")[0]).resolve() != root.resolve():
        return "cited commits unchecked (no git history)"
    if state.stdout.split("\n")[1] == "true":
        return "cited commits unchecked (shallow clone)"
    foreign = _foreign(root)
    judged: dict[str, str | None] = {}
    cited = 0
    for where in RECORDS:
        path = root / where
        if not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in CITATION.finditer(line):
                cited_hash = match.group()
                if cited_hash in foreign:
                    continue
                cited += 1
                if cited_hash not in judged:
                    judged[cited_hash] = _problem(root, cited_hash)
                if problem := judged[cited_hash]:
                    add(where, "citations", f"line {number}: {cited_hash} {problem}")
    return f"{cited} cited commit(s)"


def _problem(root: Path, cited_hash: str) -> str | None:
    commit = _git(root, "rev-parse", "--verify", "--quiet", f"{cited_hash}^{{commit}}")
    if commit.returncode != 0:
        return (
            f"names no single commit in this repository; if it's another repository's commit "
            f"or a file's hash, list it in {FOREIGN} with what it is"
        )
    if _git(root, "merge-base", "--is-ancestor", commit.stdout.strip(), "HEAD").returncode != 0:
        return (
            "is a commit HEAD doesn't reach, as a squash or rebase-merge leaves a branch's "
            "commits; cite the commit that reached main"
        )
    return None


def _foreign(root: Path) -> set[str]:
    path = root / FOREIGN
    if not path.is_file():
        return set()
    lines = path.read_text(encoding="utf-8").splitlines()
    return {line.split()[0] for line in lines if line.strip() and not line.startswith("#")}


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True, check=False
    )

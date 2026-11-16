"""Every commit the records cite stays reachable from HEAD (core/citations.py).

Each test builds its own git repository under tmp_path; none reads this repository's history.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

from skillcheck.core import citations
from skillcheck.core.checks import check_repository

NO_HISTORY = "cited commits unchecked (no git history)"


@pytest.fixture(autouse=True)
def isolated_git(monkeypatch):
    # The machine's own git settings, such as commit signing, stay out of the fixtures.
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", os.devnull)
    monkeypatch.setenv("GIT_CONFIG_NOSYSTEM", "1")
    for role in ("AUTHOR", "COMMITTER"):
        monkeypatch.setenv(f"GIT_{role}_NAME", "Fixture")
        monkeypatch.setenv(f"GIT_{role}_EMAIL", "fixture@example.com")


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args], check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def write(root: Path, path: str, text: str) -> None:
    (root / path).parent.mkdir(parents=True, exist_ok=True)
    (root / path).write_text(text, encoding="utf-8")


def commit(root: Path, message: str, path: str | None = "notes.txt") -> str:
    """Commit everything, first writing the message to `path` unless it's None."""
    if path is not None:
        write(root, path, message + "\n")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", message)
    return git(root, "rev-parse", "HEAD")


def short(sha: str, length: int = 7) -> str:
    """The shortest prefix from `length` on that holds a digit and a letter, as a citation does."""
    while not (re.search(r"[0-9]", sha[:length]) and re.search(r"[a-f]", sha[:length])):
        length += 1
    return sha[:length]


def new_repository(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    git(root, "init", "-q", "-b", "main")
    commit(root, "base")
    return root


def run(root: Path) -> tuple[str, list[tuple[str, str, str]]]:
    found: list[tuple[str, str, str]] = []
    summary = citations.check(root, lambda *finding: found.append(finding))
    return summary, found


def test_commits_main_reaches_pass_wherever_the_records_cite_them(tmp_path):
    root = new_repository(tmp_path / "repo")
    first = commit(root, "first")
    write(
        root, "docs/decisions.md", f"# Decisions\n\n- Applied in `{short(first)}`, then {first}.\n"
    )
    write(root, "CHANGELOG.md", f"- A change ({short(first, 9)}).\n")
    write(root, "ROADMAP.md", f"| Done in `{short(first)}` |\n")
    commit(root, "records", None)
    assert run(root) == ("4 cited commit(s)", [])


@pytest.mark.parametrize(
    ("merge", "stranded"),
    [
        (["merge", "-q", "--no-ff", "-m", "Merge feature", "feature"], False),
        (["merge", "-q", "--squash", "feature"], True),
    ],
    ids=["merge-commit", "squash"],
)
def test_a_branch_commit_cited_after_a_squash_merge_fails(tmp_path, merge, stranded):
    root = new_repository(tmp_path / "repo")
    git(root, "switch", "-q", "-c", "feature")
    cited = commit(root, "the feature", "feature.txt")
    git(root, "switch", "-q", "main")
    git(root, merge[0], *merge[1:])
    if stranded:
        git(root, "commit", "-q", "-m", "the feature, squashed")
    # The branch goes once merged; its commit stays in the object store, unreachable.
    git(root, "branch", "-q", "-D", "feature")
    write(root, "docs/decisions.md", f"# Decisions\n\n- Built in `{short(cited)}`.\n")
    commit(root, "records", None)
    summary, found = run(root)
    assert summary == "1 cited commit(s)"
    if not stranded:
        assert found == []
        return
    ((path, rule, message),) = found
    assert (path, rule) == ("docs/decisions.md", "citations")
    assert message == (
        f"line 3: {short(cited)} is a commit HEAD doesn't reach, as a squash or rebase-merge "
        "leaves a branch's commits; cite the commit that reached main"
    )


def test_a_hash_naming_no_commit_here_fails_until_listed_as_foreign(tmp_path):
    root = new_repository(tmp_path / "repo")
    write(root, "docs/decisions.md", "# Decisions\n\n- Pinned at abc1234def, a file's hash.\n")
    commit(root, "records", None)
    summary, found = run(root)
    assert summary == "1 cited commit(s)"
    ((path, rule, message),) = found
    assert (path, rule) == ("docs/decisions.md", "citations")
    assert message.startswith("line 3: abc1234def names no single commit in this repository")
    assert citations.FOREIGN in message
    write(root, citations.FOREIGN, "# What each hash is.\n\nabc1234def  a file's hash\n")
    assert run(root) == ("0 cited commit(s)", [])
    # A listed hash is passed over, and the citations after it are still read.
    first = commit(root, "first")
    write(root, "docs/decisions.md", f"- Pinned at abc1234def, built in `{short(first)}`.\n")
    assert run(root) == ("1 cited commit(s)", [])


@pytest.mark.parametrize(
    "text",
    [
        "a word of hex letters alone: defaced",
        "a number: run 37258285607",
        "too short: abc123",
        "upper case: ABC1234",
        "a UUID: 46cfbc1a-d1c5-5a09-bbbb-4b2444266d0f",
        f"a SHA-256: {'ab12' * 16}",
        "inside a word: gabc1234 or abc1234_x",
    ],
)
def test_runs_that_are_not_commit_citations_are_left_alone(tmp_path, text):
    root = new_repository(tmp_path / "repo")
    write(root, "CHANGELOG.md", f"- {text}\n")
    commit(root, "records", None)
    assert run(root) == ("0 cited commit(s)", [])


def test_a_shallow_clone_checks_nothing_and_says_so(tmp_path):
    source = new_repository(tmp_path / "source")
    first = commit(source, "first")
    write(source, "docs/decisions.md", f"- Built in `{short(first)}`.\n")
    commit(source, "records", None)
    # A space in the path, so the check reads git's answer by line, not by word.
    clone = tmp_path / "a clone"
    subprocess.run(
        ["git", "clone", "-q", "--depth", "1", source.as_uri(), str(clone)],
        check=True,
        capture_output=True,
    )
    assert run(clone) == ("cited commits unchecked (shallow clone)", [])


@pytest.mark.parametrize("where", ["plain", "subdirectory", "no-commit"])
def test_a_directory_without_its_own_history_checks_nothing(tmp_path, where):
    root = tmp_path / "plain"
    root.mkdir()
    if where == "subdirectory":
        root = new_repository(tmp_path / "repo") / "docs"
        root.mkdir()
    elif where == "no-commit":
        git(root, "init", "-q")
    write(root, "docs/decisions.md", "- Built in `abc1234def`.\n")
    assert run(root) == (NO_HISTORY, [])


def test_without_git_nothing_is_checked(tmp_path, monkeypatch):
    root = new_repository(tmp_path / "repo")
    monkeypatch.setattr(citations.shutil, "which", lambda _name: None)
    assert run(root) == ("cited commits unchecked (no git)", [])


def test_the_summary_line_says_what_was_checked(tmp_path):
    root = new_repository(tmp_path / "repo")
    first = commit(root, "first")
    write(root, "ROADMAP.md", f"Shipped in `{short(first)}`.\n")
    commit(root, "records", None)
    report = check_repository(root)
    assert "standard, 1 cited commit(s), " in report.summary()


def test_a_repository_whose_path_holds_a_space_is_checked(tmp_path):
    root = new_repository(tmp_path / "a repo")
    first = commit(root, "first")
    write(root, "ROADMAP.md", f"Shipped in `{short(first)}`.\n")
    assert run(root) == ("1 cited commit(s)", [])


def test_a_citation_s_finding_reaches_the_report(tmp_path):
    root = new_repository(tmp_path / "repo")
    write(root, "CHANGELOG.md", "- Built in abc1234def.\n")
    commit(root, "records", None)
    assert [(f.path, f.rule) for f in check_repository(root).findings] == [
        ("CHANGELOG.md", "citations")
    ]

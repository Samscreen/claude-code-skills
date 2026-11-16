#!/usr/bin/env python3
"""Check that this copy of the skill is whole: Step 0 of its SKILL.md.

SKILL.md's frontmatter records `files-sha256`, a hash over every other file in the skill. This
script hashes the files beside it and compares, so a run knows which bytes it is following
before it reads them. It prints one line and exits 0 when the hash matches, 1 when it differs,
and 2 when it couldn't check, so "couldn't check" never reads as a match:

    COPY OK standard=<version> files=<count> sha256=<hash> path=<skill folder>

    python3 verify_copy.py                 # the skill this script sits in
    python3 verify_copy.py <skill folder>  # another copy
    python3 verify_copy.py --print         # print the hash for SKILL.md, check nothing

The hash covers each file's path and bytes, with Windows line endings read as Unix ones, in
path order. It leaves out SKILL.md, which holds the hash, and anything under a folder or file
whose name starts with a dot or is `__pycache__`, which Python writes beside a script it runs.
Standard library only, Python 3.10 or later.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

SKILL = "SKILL.md"
SKIPPED = "__pycache__"
FIELD = re.compile(r'^\s+(standard-version|files-sha256):\s*"([^"]*)"\s*$')
HASH = re.compile(r"[0-9a-f]{64}")


class CannotCheck(Exception):
    """A file the check needs is missing or unreadable, so nothing can be said either way."""


def files(skill: Path) -> list[Path]:
    """Every file the hash covers, in the order it covers them."""
    found = []
    for path in skill.rglob("*"):
        parts = path.relative_to(skill).parts
        if not path.is_file() or parts == (SKILL,):
            continue
        if any(part.startswith(".") or part == SKIPPED for part in parts):
            continue
        found.append(path)
    return sorted(found, key=lambda path: path.relative_to(skill).as_posix())


def digest(skill: Path) -> tuple[str, int]:
    """The skill's files-sha256, and how many files it covers."""
    listing = []
    covered = files(skill)
    for path in covered:
        data = path.read_bytes().replace(b"\r\n", b"\n")
        listing.append(f"{hashlib.sha256(data).hexdigest()}  {path.relative_to(skill).as_posix()}")
    whole = hashlib.sha256(("\n".join(listing) + "\n").encode("utf-8")).hexdigest()
    return whole, len(covered)


def recorded(skill: Path) -> dict[str, str]:
    """The version and hash SKILL.md's frontmatter records."""
    try:
        lines = (skill / SKILL).read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        raise CannotCheck(f"can't read {SKILL}: {error}") from error
    if not lines or lines[0].strip() != "---" or "---" not in (line.strip() for line in lines[1:]):
        raise CannotCheck(f"{SKILL} has no frontmatter")
    end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    found = {m.group(1): m.group(2) for line in lines[1:end] if (m := FIELD.match(line))}
    if not HASH.fullmatch(found.get("files-sha256", "")):
        raise CannotCheck(f"{SKILL} records no files-sha256 of 64 hex digits")
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check this copy of the skill against SKILL.md.")
    parser.add_argument("skill", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--print", action="store_true", help="print the hash, check nothing")
    args = parser.parse_args(argv)
    skill = args.skill.resolve()
    if args.print:
        print(digest(skill)[0])
        return 0
    try:
        found = recorded(skill)
        actual, count = digest(skill)
    except CannotCheck as error:
        print(f"COPY MISSING path={skill} reason={error}")
        return 2
    version = found.get("standard-version", "unknown")
    expected = found["files-sha256"]
    if actual != expected:
        print(
            f"COPY MISMATCH standard={version} files={count} expected={expected} "
            f"actual={actual} path={skill}"
        )
        return 1
    print(f"COPY OK standard={version} files={count} sha256={actual} path={skill}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

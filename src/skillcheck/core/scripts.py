"""A skill's scripts and their tests: the script beside the skill, its tests in the suite.

A script a skill runs, such as a steward's, lives in the skill's ``scripts/``, and its tests live
in the repository's own test suite, which CI runs. A script no test names is a script CI never
runs, so ``skillcheck`` warns of each one. It warns rather than fails: a test can reach a script
in ways no search can see, and a repository may keep its tests outside ``tests/`` or ``test/``.

A script counts as tested when a file in the repository's ``tests/`` or ``test/`` names its file,
such as ``check_report.py``, or, for Python, imports it.
"""

import re
from collections.abc import Callable
from pathlib import Path

from skillcheck.core import paths

SUFFIXES = {".py", ".sh", ".ps1", ".js", ".mjs", ".ts"}
TEST_DIRS = ("tests", "test")

Add = Callable[[str, str, str], None]


def check(root: Path, skills: list[Path], repository: Path, warn: Add) -> None:
    """Warn of each script in a skill under ``root`` that no test in ``repository`` names."""
    tests = [
        path.read_text(encoding="utf-8", errors="replace")
        for directory in TEST_DIRS
        for path in paths.files_under(repository, directory, SUFFIXES)
    ]
    for skill_dir in skills:
        for script in paths.files_under(skill_dir, "scripts", SUFFIXES):
            if not any(names(text, script) for text in tests):
                warn(
                    script.relative_to(root).as_posix(),
                    "scripts",
                    "no file in the repository's tests/ or test/ names or imports it, so CI "
                    "never runs it",
                )


def names(text: str, script: Path) -> bool:
    """Whether a test's text names the script's file, or imports it as a Python module."""
    if script.name in text:
        return True
    imported = rf"\b(?:import|from)\s+(?:[\w.]+\.)?{re.escape(script.stem)}\b"
    return script.suffix == ".py" and re.search(imported, text) is not None

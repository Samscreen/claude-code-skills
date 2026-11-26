"""A draft skill: one its owner hasn't accepted yet, marked where claude.ai accepts the mark.

Other repositories' sessions wrote DRAFT into a skill's description or title. The description is
what a model reads to choose a skill, so the word spends the listing's room, and no check can
tell what it means or when it ends. The mark is ``metadata: {status: "draft"}`` instead:
``metadata`` is the Agent Skills spec's own map of strings, which claude.ai accepts, as it accepts
each skill's ``metadata.reviewed``.

A draft is checked like any other skill, and ``skillcheck`` names it in its summary without
failing. What ends a draft is in docs/authoring-a-skill.md and ``git-workflows``'
``pr-stewardship`` module.
"""

import re
from collections.abc import Callable

STATUS = "status"
DRAFT = "draft"
WORD = re.compile(r"\bDRAFT\b")
TITLE = re.compile(r"^# (.+)$", re.MULTILINE)

Add = Callable[[str, str, str], None]


def check(data: dict, body: str, where: str, add: Add) -> bool:
    """Report a draft marked any other way; return whether the skill is marked a draft."""
    title = TITLE.search(body)
    for part, text in (
        ("description", data.get("description")),
        ("title", title.group(1) if title else None),
    ):
        if isinstance(text, str) and WORD.search(text):
            add(where, "draft", f'its {part} says DRAFT; mark a draft with metadata status "draft"')
    metadata = data.get("metadata")
    status = metadata.get(STATUS) if isinstance(metadata, dict) else None
    if status is None:
        return False
    if status != DRAFT:
        add(
            where,
            "draft",
            f'metadata status is {status!r}; the one status is "draft", and a finished skill '
            "has none",
        )
        return False
    return True

"""The parts of the skill that carries the standard, while the standard moves into them.

Piece 1 of the rebuild moved the procedure into ``SKILL.md`` and the standing rules,
vocabularies, environment and self-check into references beside the standard file, with the
run report's skeleton and schema in ``assets/`` and two scripts in ``scripts/``. Once a skill
records ``files-sha256`` or carries the schema, these checks hold it to that shape:

- ``SKILL.md`` links every file in ``references/``, ``assets/`` and ``scripts/``, so none is
  orphaned, since a reference never links another;
- ``files-sha256`` is the hash ``scripts/verify_copy.py`` computes, so no release ships a copy
  whose own check stops every run;
- the report schema's fields are the templates' fields, and its statuses the vocabularies';
- each Markdown file passes the standard's structural checks: fences, ``<constraints>``,
  tables and whitespace.

Test G itself still runs on the standard file, in ``standard.py``.
"""

import hashlib
import json
import re
from collections.abc import Callable
from pathlib import Path

from skillcheck.core import frontmatter

COPY_FIELD = "files-sha256"
SCHEMA = "assets/report-schema.json"
SKELETON = "assets/report-skeleton.md"
SELF_CHECK = "references/self-check.md"
VOCABULARIES = "references/vocabularies.md"
PARTS = ("references", "assets", "scripts")
SKIPPED = "__pycache__"
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)\s]*)?\)")
FENCE = re.compile(r"^\s*```")
TOP = re.compile(r"^([A-Za-z_][\w-]*):")
NESTED = re.compile(r"^  ([A-Za-z_][\w-]*):")
STATUS_ROW = re.compile(r"^\| \d+ \| `([^`]+)` \|")

Add = Callable[[str, str, str], None]
Markdown = Callable[[Path, str, Add], None]


def files_sha256(skill_dir: Path) -> str:
    """The hash ``scripts/verify_copy.py`` computes. A test holds the two to the same value."""
    listing = []
    for path in _covered(skill_dir):
        data = path.read_bytes().replace(b"\r\n", b"\n")
        listing.append(f"{hashlib.sha256(data).hexdigest()}  {_rel(skill_dir, path)}")
    return hashlib.sha256(("\n".join(listing) + "\n").encode("utf-8")).hexdigest()


def _covered(skill_dir: Path) -> list[Path]:
    found = []
    for path in skill_dir.rglob("*"):
        parts = path.relative_to(skill_dir).parts
        if not path.is_file() or parts == ("SKILL.md",):
            continue
        if any(part.startswith(".") or part == SKIPPED for part in parts):
            continue
        found.append(path)
    return sorted(found, key=lambda path: _rel(skill_dir, path))


def _rel(base: Path, path: Path) -> str:
    return path.relative_to(base).as_posix()


def check(root: Path, skill_dir: Path, standard: Path, markdown: Markdown, add: Add) -> None:
    skill_md = skill_dir / "SKILL.md"
    where = _rel(root, skill_md)
    try:
        data, body = frontmatter.parse(skill_md.read_text(encoding="utf-8"))
    except OSError, frontmatter.FrontmatterError:
        return  # the skill checks already report an unreadable SKILL.md
    metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    recorded = metadata.get(COPY_FIELD)
    if recorded is None and not (skill_dir / SCHEMA).is_file():
        return  # the standard as one file, before piece 1
    if recorded is None:
        add(where, "standard", f"SKILL.md records no {COPY_FIELD}, which Step 0 checks")
    else:
        actual = files_sha256(skill_dir)
        if str(recorded) != actual:
            add(
                where,
                "standard",
                f"SKILL.md's {COPY_FIELD} is {recorded}; the skill's files hash to {actual}",
            )
    _check_linked(skill_dir, body, where, add)
    for path in [
        skill_md,
        *sorted(skill_dir.glob("references/*.md")),
        *sorted(skill_dir.glob("assets/*.md")),
    ]:
        if path != standard:
            markdown(path, _rel(root, path), add)
    _check_schema(root, skill_dir, standard, add)


def _check_linked(skill_dir: Path, body: str, where: str, add: Add) -> None:
    linked = {match.group(1) for match in LINK.finditer(body)}
    for part in PARTS:
        for path in sorted((skill_dir / part).rglob("*")):
            name = _rel(skill_dir, path)
            if path.is_file() and SKIPPED not in path.parts and name not in linked:
                add(where, "standard", f"SKILL.md doesn't link {name}")


def _check_schema(root: Path, skill_dir: Path, standard: Path, add: Add) -> None:
    where = _rel(root, skill_dir / SCHEMA)
    try:
        schema = json.loads((skill_dir / SCHEMA).read_text(encoding="utf-8"))
        blocks = schema["blocks"]
        statuses = schema["statuses"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        add(where, "standard", f"the report schema can't be read: {exc}")
        return
    templates = _templates(skill_dir, standard)
    for name in sorted(set(blocks) | set(templates), key=_order):
        if name not in blocks:
            add(where, "standard", f"the schema has no {name} block, which a template gives")
            continue
        if name not in templates:
            add(where, "standard", f"the schema's {name} block has no template")
            continue
        fields, beside = templates[name]
        spec = blocks[name]
        listed = spec.get("fields", [])
        for field in sorted(set(listed) - set(fields)):
            add(where, "standard", f"{name}: the schema lists {field}, which its template doesn't")
        for field in sorted(set(fields) - set(listed)):
            add(
                where,
                "standard",
                f"{name}: the template has {field}, which the schema doesn't list",
            )
        for field in sorted(set(spec.get("optional", [])) - set(listed)):
            add(where, "standard", f"{name}: optional {field} isn't one of its fields")
        if sorted(spec.get("beside", [])) != sorted(beside):
            add(where, "standard", f"{name}: the blocks beside it are {beside} in its template")
    vocabulary = _statuses(skill_dir / VOCABULARIES)
    if vocabulary != statuses:
        add(where, "standard", f"the schema's statuses aren't the vocabularies': {vocabulary}")


def _order(name: str) -> tuple[int, str]:
    return (int(name.split()[1]), name) if name.startswith("phase ") else (-1, name)


def _templates(skill_dir: Path, standard: Path) -> dict[str, tuple[list[str], list[str]]]:
    """Each block's template fields, and the blocks its template puts beside it."""
    found: dict[str, tuple[list[str], list[str]]] = {}
    for path in (standard, skill_dir / SKELETON, skill_dir / SELF_CHECK):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for body in _yaml_blocks(text):
            top = [m.group(1) for line in body if (m := TOP.match(line))]
            nested = [m.group(1) for line in body if (m := NESTED.match(line))]
            if top and (number := re.match(r"phase: (\d+)", body[0])):
                found[f"phase {int(number.group(1))}"] = (top[1:], [])
            elif top and top[0] in ("post_gate", "conformance"):
                found[top[0]] = (nested, top[1:])
            elif "standard" in top and "job" in top:
                found.setdefault("header", (top, []))
    return found


def _yaml_blocks(text: str) -> list[list[str]]:
    lines = text.split("\n")
    out, index = [], 0
    while index < len(lines):
        if lines[index].strip() == "```yaml":
            end = index + 1
            while end < len(lines) and not FENCE.match(lines[end]):
                end += 1
            out.append(lines[index + 1 : end])
            index = end
        index += 1
    return out


def _statuses(path: Path) -> list[str]:
    try:
        lines = path.read_text(encoding="utf-8").split("\n")
    except OSError:
        return []
    return [m.group(1) for line in lines if (m := STATUS_ROW.match(line))]

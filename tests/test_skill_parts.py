"""The skill around the standard: its parts linked, its copy hash current, its schema agreeing."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest
from conftest import add_standard

from skillcheck.core import skill_parts
from skillcheck.core.checks import check_repository

SCRIPT = (
    Path(__file__).resolve().parent.parent
    / "skills"
    / "project-bootstrap-and-audit"
    / "scripts"
    / "verify_copy.py"
)
# The block on the file's first line is read too.
SELF_CHECK = """\
```yaml
conformance:
  standard_version: "<version>"
  waits_observed: <int>          # a comment line is no field
validated:
  - {rule: "<quoted>", caught: "<what>"}
```
"""
VOCABULARIES = """\
# Vocabularies

| Precedence | Status | Meaning |
|---|---|---|
| 1 | `GAP` | Missing |
| 2 | `OK` | Fine |
"""
# A block naming a standard but no job isn't the header, and an empty block hides nothing.
SKELETON = """\
# Skeleton

```yaml
standard: <a standard's name in prose>
```

```yaml
```

```yaml
standard: <name>
job: <job>
```

```yaml
other: a block that is none of the report's
```
"""
SCHEMA = {
    "statuses": ["GAP", "OK"],
    "blocks": {
        "header": {"fields": ["standard", "job"], "optional": []},
        **{f"phase {n}": {"fields": ["notes"], "optional": []} for n in range(10)},
        "conformance": {
            "fields": ["standard_version", "waits_observed"],
            "optional": [],
            "beside": ["validated"],
        },
    },
}
LINKS = (
    "[s](references/self-check.md) [v](references/vocabularies.md) "
    "[k](assets/report-skeleton.md) [j](assets/report-schema.json) [c](scripts/check.py)\n"
)


def load_script():
    spec = importlib.util.spec_from_file_location("verify_copy", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def add_parts(repo, schema: dict | None = None) -> Path:
    """The synthetic standard's skill with piece 1's parts, every rule passing."""
    skill_dir = add_standard(repo).parent.parent
    for name, text in {
        "references/self-check.md": SELF_CHECK,
        "references/vocabularies.md": VOCABULARIES,
        "assets/report-skeleton.md": SKELETON,
        "assets/report-schema.json": json.dumps(SCHEMA if schema is None else schema),
        "scripts/check.py": "print('ok')\n",
    }.items():
        (skill_dir / name).parent.mkdir(parents=True, exist_ok=True)
        (skill_dir / name).write_text(text, encoding="utf-8")
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8").replace(
        "Read [the standard]", LINKS + "Read [the standard]"
    )
    skill_md.write_text(text, encoding="utf-8")
    rehash(skill_dir)
    return skill_dir


def rehash(skill_dir: Path, value: str | None = None) -> None:
    skill_md = skill_dir / "SKILL.md"
    lines = [
        line
        for line in skill_md.read_text(encoding="utf-8").split("\n")
        if "files-sha256" not in line
    ]
    index = lines.index("metadata:") + 1
    lines.insert(index, f'  files-sha256: "{value or skill_parts.files_sha256(skill_dir)}"')
    skill_md.write_text("\n".join(lines), encoding="utf-8")


SKILL = "skills/standard-skill"


def findings(repo) -> list[str]:
    return [f.message for f in check_repository(repo.root).findings if f.rule == "standard"]


def located(repo) -> list[tuple[str, str]]:
    return [(f.path, f.message) for f in check_repository(repo.root).findings]


def test_conforming_parts_pass(repo):
    add_parts(repo)
    assert findings(repo) == []


def test_the_standard_alone_needs_no_parts(repo):
    add_standard(repo)
    assert findings(repo) == []


def test_a_stale_copy_hash_is_reported(repo):
    skill_dir = add_parts(repo)
    (skill_dir / "scripts/check.py").write_text("print('changed')\n", encoding="utf-8")
    [(path, message)] = located(repo)
    assert path == f"{SKILL}/SKILL.md"
    assert message.startswith("SKILL.md's files-sha256 is ")
    assert message.endswith(f"; the skill's files hash to {skill_parts.files_sha256(skill_dir)}")


def test_a_schema_without_a_copy_hash_is_reported(repo):
    skill_dir = add_parts(repo)
    skill_md = skill_dir / "SKILL.md"
    text = "\n".join(
        line
        for line in skill_md.read_text(encoding="utf-8").split("\n")
        if "files-sha256" not in line
    )
    skill_md.write_text(text, encoding="utf-8")
    assert located(repo) == [
        (f"{SKILL}/SKILL.md", "SKILL.md records no files-sha256, which Step 0 checks")
    ]


def test_an_unlinked_part_is_reported(repo):
    skill_dir = add_parts(repo)
    (skill_dir / "scripts/__pycache__").mkdir()
    (skill_dir / "scripts/__pycache__/check.pyc").write_bytes(b"\0")
    (skill_dir / "scripts/extra.py").write_text("\n", encoding="utf-8")
    rehash(skill_dir)
    assert located(repo) == [(f"{SKILL}/SKILL.md", "SKILL.md doesn't link scripts/extra.py")]


def test_each_part_passes_the_structural_checks(repo):
    skill_dir = add_parts(repo)
    (skill_dir / "references/self-check.md").write_text(
        SELF_CHECK + "\nA line.  \n", encoding="utf-8"
    )
    (skill_dir / "assets/report-skeleton.md").write_text(SKELETON + "```\n", encoding="utf-8")
    (skill_dir / "references/vocabularies.md").write_text(
        VOCABULARIES
        + "<!-- a comment that splits the table -->\n| - | none | Unranked |\n\n"
        + "<constraints>\n<constraints>\n</constraints>\n\n```text\n```\nAfter a fence. \n",
        encoding="utf-8",
    )
    rehash(skill_dir)
    assert located(repo) == [
        (f"{SKILL}/references/self-check.md", "trailing whitespace on 1 line(s), first at line 9"),
        (f"{SKILL}/references/vocabularies.md", "<constraints> opens inside another at line 11"),
        (f"{SKILL}/references/vocabularies.md", "<constraints> opens 2 times and closes 1 times"),
        (f"{SKILL}/references/vocabularies.md", "HTML comment inside a table at line 7"),
        (
            f"{SKILL}/references/vocabularies.md",
            "trailing whitespace on 1 line(s), first at line 16",
        ),
        (f"{SKILL}/assets/report-skeleton.md", "code fences are unbalanced: 9 fence lines"),
    ]


def test_a_part_is_checked_from_its_first_line(repo):
    # Unlike the standard, a part has no frontmatter, so its first lines are prose.
    skill_dir = add_parts(repo)
    (skill_dir / "references/vocabularies.md").write_text(
        "| A |\n<!-- c -->\n| B |\n\n" + VOCABULARIES, encoding="utf-8"
    )
    (skill_dir / "assets/report-skeleton.md").write_text("\n\n" + SKELETON, encoding="utf-8")
    rehash(skill_dir)
    assert located(repo) == [
        (f"{SKILL}/references/vocabularies.md", "HTML comment inside a table at line 2")
    ]


@pytest.mark.parametrize(
    ("change", "expected"),
    [
        (
            lambda s: s["blocks"]["header"]["fields"].append("tier"),
            "header: the schema lists tier, which its template doesn't",
        ),
        (
            lambda s: s["blocks"]["phase 3"]["fields"].remove("notes"),
            "phase 3: the template has notes, which the schema doesn't list",
        ),
        (
            lambda s: s["blocks"]["phase 2"]["optional"].append("proposed"),
            "phase 2: optional proposed isn't one of its fields",
        ),
        (
            lambda s: s["blocks"]["conformance"].update(beside=[]),
            "conformance: the blocks beside it are ['validated'] in its template",
        ),
        (
            lambda s: s["blocks"].pop("phase 9"),
            "the schema has no phase 9 block, which a template gives",
        ),
        (
            lambda s: s["blocks"].update(post_gate={"fields": [], "optional": []}),
            "the schema's post_gate block has no template",
        ),
        (
            lambda s: s.update(statuses=["OK", "GAP"]),
            "the schema's statuses aren't the vocabularies': ['GAP', 'OK']",
        ),
        (lambda s: s.pop("blocks"), "the report schema can't be read: 'blocks'"),
    ],
)
def test_the_schema_agrees_with_the_templates(repo, change, expected):
    schema = json.loads(json.dumps(SCHEMA))
    change(schema)
    add_parts(repo, schema)
    assert located(repo) == [(f"{SKILL}/assets/report-schema.json", expected)]


def test_every_block_is_compared_with_the_others_first_then_the_phases_in_order(repo):
    schema = json.loads(json.dumps(SCHEMA))
    del schema["blocks"]["phase 0"]
    schema["blocks"]["phase 4"] = {}
    schema["blocks"]["post_gate"] = {"fields": [], "optional": []}
    add_parts(repo, schema)
    assert findings(repo) == [
        "the schema's post_gate block has no template",
        "the schema has no phase 0 block, which a template gives",
        "phase 4: the template has notes, which the schema doesn't list",
    ]


def test_a_missing_skeleton_leaves_the_other_templates_read(repo):
    skill_dir = add_parts(repo)
    (skill_dir / "assets/report-skeleton.md").unlink()
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    (skill_dir / "SKILL.md").write_text(
        text.replace("[k](assets/report-skeleton.md) ", ""), "utf-8"
    )
    rehash(skill_dir)
    assert findings(repo) == ["the schema's header block has no template"]


def test_a_yaml_block_left_open_at_the_end_is_read_to_the_end(repo):
    skill_dir = add_parts(repo)
    with (skill_dir / "assets/report-skeleton.md").open("a", encoding="utf-8") as file:
        file.write("```yaml\nnote: x\n")
    rehash(skill_dir)
    assert findings(repo) == ["code fences are unbalanced: 9 fence lines"]


def test_missing_templates_leave_the_schema_without_them(repo):
    skill_dir = add_parts(repo)
    (skill_dir / "references/self-check.md").unlink()
    (skill_dir / "references/vocabularies.md").unlink()
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    text = text.replace("[s](references/self-check.md) [v](references/vocabularies.md) ", "")
    (skill_dir / "SKILL.md").write_text(text, encoding="utf-8")
    rehash(skill_dir)
    assert findings(repo) == [
        "the schema's conformance block has no template",
        "the schema's statuses aren't the vocabularies': []",
    ]


def test_an_unreadable_skill_md_is_left_to_the_skill_checks(repo):
    skill_dir = add_parts(repo)
    (skill_dir / "SKILL.md").write_text("no frontmatter\n", encoding="utf-8")
    assert findings(repo) == []


def test_the_script_and_skillcheck_hash_alike(tmp_path):
    skill = tmp_path / "skill"
    for name, data in {
        "SKILL.md": b'---\nmetadata:\n  files-sha256: "x"\n---\n',
        "references/a.md": b"line one\r\nline two\n",
        "scripts/run.py": b"print(1)\n",
        "scripts/__pycache__/run.pyc": b"\0",
        # A file name that sorts before a folder's by its path, and after it by its parts.
        "assets/a-b.txt": b"1\n",
        "assets/a/b.txt": b"2\n",
        ".hidden/file": b"skipped\n",
    }.items():
        (skill / name).parent.mkdir(parents=True, exist_ok=True)
        (skill / name).write_bytes(data)
    expected = skill_parts.files_sha256(skill)
    assert load_script().digest(skill) == (expected, 4)
    (skill / "references/a.md").write_bytes(b"line one\nline two\n")
    assert skill_parts.files_sha256(skill) == expected  # Windows line endings read as Unix ones

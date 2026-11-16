"""Step 0's copy check matches a whole copy, and names a changed or unreadable one."""

from pathlib import Path

import pytest
from test_skill_parts import load_script

from skillcheck.core import skill_parts

SKILL = Path(__file__).resolve().parent.parent / "skills" / "project-bootstrap-and-audit"
verify_copy = load_script()


def copy(tmp_path: Path, recorded: str | None = None) -> Path:
    skill = tmp_path / "skill"
    (skill / "references").mkdir(parents=True)
    (skill / "references" / "rules.md").write_text("A rule.\n", encoding="utf-8")
    (skill / "SKILL.md").write_text("---\nname: skill\n---\n", encoding="utf-8")
    value = recorded or skill_parts.files_sha256(skill)
    (skill / "SKILL.md").write_text(
        f'---\nname: skill\nmetadata:\n  standard-version: "1.2.3"\n  files-sha256: "{value}"\n'
        "---\n\nBody.\n",
        encoding="utf-8",
    )
    return skill


def test_this_repository_s_copy_is_whole(capsys):
    assert verify_copy.main([str(SKILL)]) == 0
    assert capsys.readouterr().out.startswith("COPY OK standard=")


def test_a_whole_copy_passes(tmp_path, capsys):
    skill = copy(tmp_path)
    assert verify_copy.main([str(skill)]) == 0
    assert capsys.readouterr().out == (
        f"COPY OK standard=1.2.3 files=1 sha256={skill_parts.files_sha256(skill)} path={skill}\n"
    )


def test_a_changed_file_is_a_mismatch(tmp_path, capsys):
    skill = copy(tmp_path)
    (skill / "references" / "rules.md").write_text("Another rule.\n", encoding="utf-8")
    assert verify_copy.main([str(skill)]) == 1
    assert capsys.readouterr().out.startswith("COPY MISMATCH standard=1.2.3 files=1 expected=")


@pytest.mark.parametrize(
    ("text", "reason"),
    [
        (None, "can't read SKILL.md"),
        (b"no frontmatter\n", "SKILL.md has no frontmatter"),
        (b"---\nname: x\n", "SKILL.md has no frontmatter"),
        (b"\xff\xfe", "can't read SKILL.md"),
        (b'---\nmetadata:\n  files-sha256: "short"\n---\n', "records no files-sha256"),
    ],
)
def test_a_copy_it_cannot_check_is_missing(tmp_path, capsys, text, reason):
    skill = copy(tmp_path)
    if text is None:
        (skill / "SKILL.md").unlink()
    else:
        (skill / "SKILL.md").write_bytes(text)
    assert verify_copy.main([str(skill)]) == 2
    out = capsys.readouterr().out
    assert out.startswith("COPY MISSING path=") and reason in out


def test_print_gives_the_hash_to_record(tmp_path, capsys):
    skill = copy(tmp_path, recorded="0" * 64)
    assert verify_copy.main([str(skill), "--print"]) == 0
    assert capsys.readouterr().out == skill_parts.files_sha256(skill) + "\n"

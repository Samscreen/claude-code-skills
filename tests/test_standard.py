"""The standard's own mechanical checks (its "Test G"), each proven on a planted defect."""

import pytest
from conftest import add_standard, standard_text

from skillcheck.core.checks import check_repository

WHERE = "skills/standard-skill/references/PROJECT-BOOTSTRAP-AND-AUDIT-v0.2.0.md"


def standard_findings(report) -> list[str]:
    return [f.message for f in report.findings if f.rule == "standard"]


def test_a_conforming_standard_passes_and_is_reported(repo):
    add_standard(repo)
    report = check_repository(repo.root)
    assert report.findings == []
    assert report.standard_version == "0.2.0"
    assert "standard 0.2.0" in report.summary()


def test_no_standard_is_reported_as_such(repo):
    report = check_repository(repo.root)
    assert report.standard_version is None
    assert "no standard" in report.summary()


def replace_once(text: str, old: str, new: str) -> str:
    assert old in text, f"fixture no longer contains {old!r}"
    return text.replace(old, new, 1)


@pytest.mark.parametrize(
    ("defect", "expected"),
    [
        (
            lambda t: replace_once(t, "notes: none\n```", "notes: none\n"),
            "code fences are unbalanced: 19 fence lines",
        ),
        (
            lambda t: replace_once(t, "</constraints>\n\n", ""),
            "<constraints> opens 1 times and closes 0 times",
        ),
        (
            lambda t: replace_once(
                t,
                "<constraints>\n\nA rule.",
                "<constraints>\n\n<constraints>\n\nA rule.\n\n</constraints>",
            ),
            "<constraints> opens inside another at line 16",
        ),
        (
            lambda t: replace_once(t, "## Entries", "## Old entries"),
            "the version history (## Entries) holds no versions",
        ),
        (
            lambda t: replace_once(t, "|---|---|\n", "|---|---|\n<!-- WHY -->\n| `N/A` | No |\n"),
            "HTML comment inside a table at line 22",
        ),
        (
            lambda t: replace_once(t, "### 10. Dimension 10", "### 11. Dimension 11"),
            "dimensions are numbered [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]; expected 1 to 10",
        ),
        (
            lambda t: replace_once(
                t, "# Provenance", "## Phase 9 — Extra — **WAIT**\n\n# Provenance"
            ),
            "3 waits; the standard has exactly 2",
        ),
        (
            lambda t: replace_once(t, "phase: 4\nnotes: none", "phase: 4\nother: x"),
            "the phase 4 block has no notes field",
        ),
        (
            lambda t: replace_once(t, "phase: 7\n", "phase: 6\n"),
            "phase blocks are [0, 1, 2, 3, 4, 5, 6, 6, 8, 9]; expected one each for 0 to 9",
        ),
        (
            lambda t: replace_once(t, "# Provenance", "# Synthetic standard\n\n# Provenance"),
            "duplicate heading '# Synthetic standard', 2 times",
        ),
        (
            lambda t: replace_once(t, "**0.2.0** — second.", "**0.1.5** — second."),
            "the version history starts at 0.1.5; the frontmatter says 0.2.0",
        ),
        (
            lambda t: replace_once(
                t,
                "**0.2.0** — second.\n\n**0.1.0** — first.",
                "**0.2.0** — second.\n\n**0.3.0** — third.",
            ),
            "the version history is not newest-first: 0.2.0 comes before 0.3.0",
        ),
        (
            lambda t: replace_once(t, "A rule.", "A rule.  "),
            "trailing whitespace on 1 line(s), first at line 16",
        ),
        (
            lambda t: replace_once(t, "A rule.", "A rule.\n\n\n\nMore."),
            "1 run(s) of three or more blank lines, first at line 17",
        ),
        # A block closing inside another, then a third opening: each nested opening is reported.
        (
            lambda t: replace_once(
                t,
                "<constraints>\n\nA rule.\n\n</constraints>",
                "<constraints>\n<constraints>\n</constraints>\n<constraints>\n</constraints>\n"
                "</constraints>",
            ),
            [
                "<constraints> opens inside another at line 15",
                "<constraints> opens inside another at line 17",
            ],
        ),
        # A comment on the line before the last, and comments between indented rows.
        (
            lambda t: t + "| a |\n  <!-- WHY -->\n  | b |\n<!-- WHY -->\n| c |",
            [
                "HTML comment inside a table at line 126",
                "HTML comment inside a table at line 128",
            ],
        ),
        # A heading straight after a closing fence is prose.
        (
            lambda t: replace_once(
                t, "# Provenance", "```\nx\n```\n# Synthetic standard\n\n# Provenance"
            ),
            "duplicate heading '# Synthetic standard', 2 times",
        ),
        # Three blank lines after a fenced block are a run, though the block breaks the numbering.
        (
            lambda t: replace_once(t, "# Provenance", "```\nx\n```\n\n\n\n# Provenance"),
            "1 run(s) of three or more blank lines, first at line 117",
        ),
        # An empty yaml block doesn't hide the phase block after it.
        (
            lambda t: replace_once(
                t,
                "# Provenance",
                "```yaml\n```\n\n```yaml\nphase: 4\nnotes: none\n```\n\n# Provenance",
            ),
            "phase blocks are [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]; expected one each for 0 to 9",
        ),
        (
            lambda t: replace_once(
                t, "**0.2.0** — second.", "**0.2.0** — second.\n\n**0.2.0** — again."
            ),
            "the version history is not newest-first: 0.2.0 comes before 0.2.0",
        ),
        (
            lambda t: replace_once(t, 'metadata:\n  version: "0.2.0"\n', ""),
            [
                "frontmatter says none; the filename says 0.2.0",
                "the version history starts at 0.2.0; the frontmatter says none",
            ],
        ),
        (
            lambda t: replace_once(t, "---\nname:", "name:"),
            "frontmatter: file does not start with a '---' line",
        ),
    ],
)
def test_each_mechanical_check_fires_on_its_defect(repo, defect, expected):
    add_standard(repo, text=defect(standard_text()))
    expected = [expected] if isinstance(expected, str) else expected
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (WHERE, "standard", message) for message in expected
    ]


def test_filename_and_frontmatter_versions_must_agree(repo):
    add_standard(repo, text=standard_text("0.2.0").replace('version: "0.2.0"', 'version: "0.9.0"'))
    messages = standard_findings(check_repository(repo.root))
    assert any("frontmatter says 0.9.0" in m for m in messages), messages


def test_the_skill_must_name_the_version_it_ships(repo):
    reference = add_standard(repo)
    skill_md = reference.parent.parent / "SKILL.md"
    skill_md.write_text(
        skill_md.read_text(encoding="utf-8").replace('"0.2.0"', '"0.1.0"'), encoding="utf-8"
    )
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (
            "skills/standard-skill/SKILL.md",
            "standard",
            "SKILL.md says standard-version 0.1.0; the reference file is v0.2.0",
        )
    ]


def test_a_skill_whose_metadata_is_not_a_mapping_is_left_to_the_skill_checks(repo):
    reference = add_standard(repo)
    skill_md = reference.parent.parent / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    skill_md.write_text(
        text.replace('metadata:\n  standard-version: "0.2.0"', "metadata: x"), "utf-8"
    )
    assert [f.rule for f in check_repository(repo.root).findings] == ["metadata"]


@pytest.mark.parametrize(
    "addition",
    [
        # Rows and comments near each other that don't put a comment between two rows.
        "prose\n<!-- a -->\n| a |\n\n| a |\nprose\n<!-- b -->\n| b |\n\n"
        "| a |\n<!-- c -->\nprose\n\n| a |\n<!-- d -->\nprose\n| b |\n",
        # Two blank lines in a row are allowed.
        "A rule.\n\n\nMore.\n",
    ],
)
def test_lookalikes_after_the_standard_pass(repo, addition):
    add_standard(repo, text=standard_text() + "\n" + addition)
    assert check_repository(repo.root).findings == []


def test_a_top_level_heading_ends_the_version_history(repo):
    text = replace_once(
        standard_text(),
        "**0.1.0** — first.\n",
        "**0.1.0** — first.\n\n# Appendix\n\n**9.9.9** — x.\n",
    )
    add_standard(repo, text=text)
    assert check_repository(repo.root).findings == []


def test_a_version_history_out_of_order_still_gives_the_version(repo):
    text = replace_once(standard_text(), "**0.1.0** — first.", "**0.3.0** — third.")
    add_standard(repo, text=text)
    assert check_repository(repo.root).standard_version == "0.2.0"


def test_unreadable_frontmatter_in_the_standard_is_reported(repo):
    add_standard(repo, text=standard_text().replace("---\nname:", "name:", 1))
    messages = standard_findings(check_repository(repo.root))
    assert any("frontmatter" in m for m in messages), messages


def test_fenced_content_is_not_mistaken_for_structure(repo):
    fenced = "```markdown\n# Synthetic standard\n\n### 3. Not a dimension\n\nA rule.  \n```\n"
    add_standard(
        repo, text=replace_once(standard_text(), "# Provenance", fenced + "\n# Provenance")
    )
    assert standard_findings(check_repository(repo.root)) == []


def test_an_unreadable_skill_md_is_left_to_the_skill_checks(repo):
    reference = add_standard(repo)
    (reference.parent.parent / "SKILL.md").write_text("no frontmatter\n", encoding="utf-8")
    report = check_repository(repo.root)
    assert standard_findings(report) == []
    assert "frontmatter" in {f.rule for f in report.findings}


README_ROW = (
    "| Skill | Plugin | What it does |\n|---|---|---|\n| `standard-skill` | `standards` | {} |\n"
)
ROADMAP_ROW = "| Skill | Covers | Status |\n|---|---|---|\n| `standard-skill` | {} | shipped |\n"


@pytest.mark.parametrize(
    ("name", "table", "cell"),
    [
        ("README.md", README_ROW, "Runs the synthetic standard (v0.1.0)"),
        ("ROADMAP.md", ROADMAP_ROW, "the standard, v0.1.0"),
    ],
)
def test_a_stale_copy_of_the_version_fires(repo, name, table, cell):
    add_standard(repo)
    (repo.root / name).write_text(table.format(cell), encoding="utf-8")
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (name, "standard", "the `standard-skill` row says standard v0.1.0; the file is v0.2.0")
    ]


def test_a_version_in_the_cell_after_the_word_standard_is_compared(repo):
    add_standard(repo)
    table = "| Skill | Covers | Version | Status |\n|---|---|---|---|\n"
    # Another skill's row comes first, so the search goes on past it.
    row = "| `later-skill` | other | v9.9.9 | planned |\n"
    row += "| `standard-skill` | the standard | v0.1.0 | shipped |\n"
    (repo.root / "ROADMAP.md").write_text(table + row, encoding="utf-8")
    assert [(f.path, f.message) for f in check_repository(repo.root).findings] == [
        ("ROADMAP.md", "the `standard-skill` row says standard v0.1.0; the file is v0.2.0")
    ]


def test_copies_that_agree_pass_and_other_rows_are_not_compared(repo):
    add_standard(repo)
    repo.skill("other-skill")
    repo.catalog(
        repo.plugin("standards", "./skills/standard-skill"),
        repo.plugin("others", "./skills/other-skill"),
    )
    other = "| `other-skill` | `others` | Quotes the standard v9.9.9 |\n"
    readme = README_ROW.format("Runs the synthetic standard (v0.2.0)") + other
    (repo.root / "README.md").write_text(readme, encoding="utf-8")
    roadmap = (
        ROADMAP_ROW.format("the standard, v0.2.0")
        + "| `other-skill` | the standard v9.9.9 | shipped |\n"
    )
    (repo.root / "ROADMAP.md").write_text(roadmap, encoding="utf-8")
    assert check_repository(repo.root).findings == []

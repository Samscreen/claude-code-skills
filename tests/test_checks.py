"""Each rule fires on a planted defect, alone, and stays quiet on a clean repository."""

import pytest
from conftest import DEFAULT_DESCRIPTION, REPORTING

from skillcheck.core import frontmatter
from skillcheck.core.checks import (
    DESCRIPTION_CAP,
    LISTING_BUDGET,
    MAX_COMPATIBILITY_LENGTH,
    MAX_CONTEXT_BYTES,
    MAX_CONTEXT_LINES,
    MAX_DESCRIPTION_LENGTH,
    MAX_NAME_LENGTH,
    MAX_SKILL_CHARS,
    MAX_SKILL_LINES,
    Report,
    check_repository,
)

CATALOG = ".claude-plugin/marketplace.json"


def rules(report) -> set[str]:
    return {finding.rule for finding in report.findings}


def test_empty_repository_says_nothing_was_checked(repo):
    report = check_repository(repo.root)
    assert report.findings == []
    assert report.summary() == (
        "skillcheck: 0 skill(s), 0 module(s), 0 description characters, 0 fact(s), no catalog, "
        "no roadmap, "
        "no standard, cited commits unchecked (no git history), 0 finding(s)"
    )


def test_clean_repository_passes(repo):
    repo.skill("example-skill")
    repo.catalog(repo.plugin("example", "./skills/example-skill"))
    report = check_repository(repo.root)
    assert report.findings == []
    assert report.summary() == (
        "skillcheck: 1 skill(s), 0 module(s), "
        f"{len(DEFAULT_DESCRIPTION)} description characters, 0 fact(s), "
        "1 catalog plugin(s), no roadmap, no standard, "
        "cited commits unchecked (no git history), 0 finding(s)"
    )


def test_limits_are_inclusive(repo):
    name = "a" * MAX_NAME_LENGTH
    repo.skill(name, f"name: {name}\ndescription: {'d' * DESCRIPTION_CAP}\n")
    repo.catalog(repo.plugin("example", f"./skills/{name}"))
    assert check_repository(repo.root).findings == []


@pytest.mark.parametrize("length", [DESCRIPTION_CAP + 1, MAX_DESCRIPTION_LENGTH])
def test_a_description_over_the_cap_fails_the_listing_rule_alone(repo, length):
    repo.skill("wordy-skill", f"name: wordy-skill\ndescription: {'d' * length}\n")
    repo.catalog(repo.plugin("example", "./skills/wordy-skill"))
    (finding,) = check_repository(repo.root).findings
    assert (finding.path, finding.rule) == ("skills/wordy-skill/SKILL.md", "listing")
    assert finding.message.startswith(f"description is {length} characters;")


# Each skill-NNN entry is "- skill-NNN: " and a newline around its description: 264 characters
# at the cap, so 19 fit the budget and 20 don't.
@pytest.mark.parametrize(("count", "over"), [(19, False), (20, True)])
def test_the_whole_listing_is_held_to_its_budget(repo, count, over):
    for number in range(count):
        name = f"skill-{number:03}"
        repo.skill(name, f"name: {name}\ndescription: {'d' * DESCRIPTION_CAP}\n")
    repo.catalog(repo.plugin("everything", "./skills/"))
    report = check_repository(repo.root)
    assert report.listing_chars == count * 264
    if over:
        assert [(f.path, f.rule) for f in report.findings] == [("skills", "listing")]
        assert report.findings[0].message == (
            f"the skills' listing is {count * 264} characters; the budget is "
            f"{LISTING_BUDGET}, room for 20 skills at 240; grow by modules instead"
        )
    else:
        assert report.findings == []


def test_whole_folder_entry_lists_every_skill(repo):
    repo.skill("first-skill")
    repo.skill("second-skill")
    repo.catalog(repo.plugin("everything", "./skills/"))
    assert check_repository(repo.root).findings == []


NAME_RULE = f"must be 1-{MAX_NAME_LENGTH} lowercase letters, digits and single hyphens"


# Each finding names its file, its rule and its words, so a report says where to look and why.
@pytest.mark.parametrize(
    ("directory", "frontmatter", "expected"),
    [
        (
            "mismatched",
            "name: other-name\ndescription: d\n",
            [("name", "name 'other-name' does not match directory 'mismatched'")],
        ),
        (
            "Bad_Name",
            "name: Bad_Name\ndescription: d\n",
            [("name", f"name 'Bad_Name' {NAME_RULE}")],
        ),
        (
            "double--hyphen",
            "name: double--hyphen\ndescription: d\n",
            [("name", f"name 'double--hyphen' {NAME_RULE}")],
        ),
        (
            "a" * (MAX_NAME_LENGTH + 1),
            f"name: {'a' * (MAX_NAME_LENGTH + 1)}\ndescription: d\n",
            [("name", f"name {'a' * (MAX_NAME_LENGTH + 1)!r} {NAME_RULE}")],
        ),
        ("no-name", "description: d\n", [("name", "name is missing or not a string")]),
        # A name that isn't a string fails as one, however truthy it is.
        (
            "number-name",
            "name: 42\ndescription: d\n",
            [("name", "name is missing or not a string")],
        ),
        (
            "no-description",
            "name: no-description\n",
            [("description", "description is missing or empty")],
        ),
        (
            "blank-description",
            "name: blank-description\ndescription: '  '\n",
            [("description", "description is missing or empty")],
        ),
        (
            "long-description",
            f"name: long-description\ndescription: {'d' * (MAX_DESCRIPTION_LENGTH + 1)}\n",
            [
                (
                    "description",
                    f"description is {MAX_DESCRIPTION_LENGTH + 1} characters; the limit is "
                    f"{MAX_DESCRIPTION_LENGTH}",
                )
            ],
        ),
        (
            "extra-field",
            "name: extra-field\ndescription: d\nwhen_to_use: never\nmodel: any\n",
            [("frontmatter-keys", "fields outside the spec: model, when_to_use")],
        ),
        (
            "empty-license",
            "name: empty-license\ndescription: d\nlicense: ''\n",
            [("license", "license must name a license or a bundled license file")],
        ),
        (
            "list-license",
            "name: list-license\ndescription: d\nlicense: [MIT]\n",
            [("license", "license must name a license or a bundled license file")],
        ),
        (
            "long-compatibility",
            "name: long-compatibility\ndescription: d\n"
            f"compatibility: {'c' * (MAX_COMPATIBILITY_LENGTH + 1)}\n",
            [
                (
                    "compatibility",
                    f"compatibility is {MAX_COMPATIBILITY_LENGTH + 1} characters; the limit is "
                    f"{MAX_COMPATIBILITY_LENGTH}",
                )
            ],
        ),
        (
            "empty-compatibility",
            "name: empty-compatibility\ndescription: d\ncompatibility: ''\n",
            [("compatibility", "compatibility must be non-empty text")],
        ),
        (
            "unquoted-version",
            "name: unquoted-version\ndescription: d\nmetadata:\n  version: 1.0\n  build: 7\n",
            [("metadata", "metadata values must be quoted strings: build, version")],
        ),
        (
            "nested-metadata",
            "name: nested-metadata\ndescription: d\nmetadata:\n  owner:\n    team: x\n",
            [("metadata", "metadata values must be quoted strings: owner")],
        ),
        (
            "list-metadata",
            "name: list-metadata\ndescription: d\nmetadata: [a, b]\n",
            [("metadata", "metadata must map strings to strings")],
        ),
        (
            "listed-tools",
            "name: listed-tools\ndescription: d\nallowed-tools: [Read, Grep]\n",
            [("allowed-tools", "allowed-tools must be one space-separated string")],
        ),
    ],
)
def test_frontmatter_rule_fires_alone(repo, directory, frontmatter, expected):
    repo.skill(directory, frontmatter)
    repo.catalog(repo.plugin("example", f"./skills/{directory}"))
    where = f"skills/{directory}/SKILL.md"
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (where, rule, message) for rule, message in expected
    ]


@pytest.mark.parametrize(
    ("text", "message"),
    [
        ("name: no-delimiters\ndescription: d\n", "file does not start with a '---' line"),
        ("---\nname: unclosed\ndescription: d\n", "frontmatter has no closing '---' line"),
        ("---\n- a\n- list\n---\n", "frontmatter is not a YAML mapping"),
        # PyYAML's own words follow, on one line; only their start is held, as they're its.
        ("---\nname: [unclosed\n---\n", "frontmatter is not valid YAML: while parsing a flow"),
    ],
)
def test_unreadable_frontmatter_fires(repo, text, message):
    repo.skill_file("broken", text + REPORTING)
    repo.catalog(repo.plugin("example", "./skills/broken"))
    (finding,) = check_repository(repo.root).findings
    assert (finding.path, finding.rule) == ("skills/broken/SKILL.md", "frontmatter")
    assert finding.message.startswith(message)
    assert "\n" not in finding.message


def test_frontmatter_parse_returns_the_mapping_and_the_body_after_it():
    text = "---\nname: x\n---\nFirst line.\nSecond line.\n"
    assert frontmatter.parse(text) == ({"name": "x"}, "First line.\nSecond line.")


def test_skill_directory_without_skill_md_fires(repo):
    (repo.root / "skills" / "empty").mkdir(parents=True)
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        ("skills/empty", "layout", "skill directory has no SKILL.md")
    ]


def test_stray_file_in_skills_fires(repo):
    repo.skill("example-skill")
    (repo.root / "skills" / "notes.md").write_text("stray\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/example-skill"))
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        ("skills/notes.md", "layout", "skills/ holds only skill directories")
    ]


def test_skill_missing_from_catalog_fires(repo):
    repo.skill("listed-skill")
    repo.skill("unlisted-skill")
    repo.catalog(repo.plugin("example", "./skills/listed-skill"))
    report = check_repository(repo.root)
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        ("skills/unlisted-skill", "catalog", "no catalog plugin lists this skill")
    ]


def test_catalog_path_to_missing_skill_fires(repo):
    repo.skill("example-skill")
    repo.catalog(repo.plugin("example", "./skills/example-skill", "./skills/typo-skill"))
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (CATALOG, "catalog", "example: './skills/typo-skill' has no SKILL.md")
    ]


def test_catalog_path_outside_skills_fires(repo):
    repo.skill("example-skill")
    repo.catalog(repo.plugin("example", "./skills/example-skill", "./other/example-skill"))
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (CATALOG, "catalog", "example: './other/example-skill' is not ./skills/<name>")
    ]


def test_skill_in_two_plugins_fires(repo):
    repo.skill("shared-skill")
    repo.catalog(
        repo.plugin("first", "./skills/shared-skill"),
        repo.plugin("second", "./skills/shared-skill"),
    )
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        ("skills/shared-skill", "catalog", "listed by 2 plugins: first, second")
    ]


def test_a_plugin_with_no_name_is_reported_as_unnamed(repo):
    repo.skill("shared-skill")
    repo.catalog(
        {"source": "./", "skills": ["./skills/shared-skill"]},
        repo.plugin("named", "./skills/shared-skill"),
    )
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        ("skills/shared-skill", "catalog", "listed by 2 plugins: <unnamed>, named")
    ]


def test_paths_after_a_whole_folder_entry_are_still_read(repo):
    repo.skill("example-skill")
    repo.catalog(repo.plugin("everything", "./skills/", "./skills/typo-skill"))
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (CATALOG, "catalog", "everything: './skills/typo-skill' has no SKILL.md")
    ]


def test_a_report_made_before_the_citations_ran_leaves_them_out_of_its_summary():
    assert Report().summary() == (
        "skillcheck: 0 skill(s), 0 module(s), 0 description characters, 0 fact(s), no catalog, "
        "no roadmap, no standard, 0 finding(s)"
    )


def test_a_whole_folder_entry_counts_as_a_listing_for_every_skill(repo):
    repo.skill("example-skill")
    repo.catalog(
        repo.plugin("everything", "./skills/"), repo.plugin("one", "./skills/example-skill")
    )
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        ("skills/example-skill", "catalog", "listed by 2 plugins: everything, one")
    ]


def test_skills_without_catalog_fire(repo):
    repo.skill("example-skill")
    report = check_repository(repo.root)
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        (CATALOG, "catalog", "missing, so 1 skill(s) ship in no plugin")
    ]


@pytest.mark.parametrize(
    ("skills", "message"),
    [
        ({"not": "a list"}, "malformed: 'skills' is not a list of paths"),
        ([42], "malformed: 42 is not ./skills/<name>"),
    ],
)
def test_malformed_skills_field_fires(repo, skills, message):
    # The malformed entry comes first, so the entries after it are still read.
    repo.skill("example-skill")
    repo.catalog(
        {"name": "malformed", "source": "./", "skills": skills},
        repo.plugin("example", "./skills/example-skill"),
    )
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (CATALOG, "catalog", message)
    ]


def test_a_plugin_listing_no_skills_lists_none(repo):
    repo.skill("example-skill")
    repo.catalog(
        {"name": "commands-only", "source": "./"}, repo.plugin("example", "./skills/example-skill")
    )
    assert check_repository(repo.root).findings == []


def test_single_path_string_is_accepted(repo):
    repo.skill("example-skill")
    repo.catalog({"name": "example", "source": "./", "skills": "./skills/example-skill"})
    assert check_repository(repo.root).findings == []


@pytest.mark.parametrize(
    ("text", "message"),
    [
        (
            "{not json",
            "not valid JSON: Expecting property name enclosed in double quotes: "
            "line 1 column 2 (char 1)",
        ),
        ('{"name": "no-plugins"}', "has no 'plugins' list"),
        ("[]", "has no 'plugins' list"),
    ],
)
def test_unreadable_catalog_fires(repo, text, message):
    repo.catalog_text(text)
    assert [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings] == [
        (CATALOG, "catalog", message)
    ]


def test_entries_from_other_sources_are_not_ours_to_check(repo):
    repo.skill("example-skill")
    # Entries from elsewhere, and one that isn't an object, come first: the rest are still read.
    repo.catalog(
        {"name": "elsewhere", "source": {"source": "github", "repo": "someone/else"}},
        "not an object",
        repo.plugin("example", "./skills/example-skill"),
    )
    assert check_repository(repo.root).findings == []


def test_description_characters_are_summed_across_skills(repo):
    repo.skill("first-skill")
    repo.skill("second-skill", "name: second-skill\ndescription: twelve chars\n")
    repo.catalog(repo.plugin("example", "./skills/first-skill", "./skills/second-skill"))
    report = check_repository(repo.root)
    assert report.description_chars == len(DEFAULT_DESCRIPTION) + len("twelve chars")


def test_link_to_missing_bundled_file_fires(repo):
    repo.skill("example-skill", body="See [the guide](references/guide.md).\n")
    repo.catalog(repo.plugin("example", "./skills/example-skill"))
    report = check_repository(repo.root)
    assert [(f.rule, f.message) for f in report.findings] == [
        ("reference", "links to references/guide.md, which does not exist")
    ]


def test_links_that_resolve_or_point_elsewhere_pass(repo):
    body = (
        "[guide](references/guide.md) [part](references/guide.md#setup) [web](https://example.com/x)\n"
        "[odd anchor](references/guide.md#a#b)\n"
        "[here](#usage) [mail](mailto:someone@example.com) [absolute](/no/such/file.md)\n"
    )
    skill_dir = repo.skill("example-skill", body=body)
    (skill_dir / "references").mkdir(exist_ok=True)
    (skill_dir / "references" / "guide.md").write_text("guide\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/example-skill"))
    assert check_repository(repo.root).findings == []


def test_optional_fields_in_spec_form_pass(repo):
    frontmatter = (
        "name: full-skill\ndescription: d\nlicense: Apache-2.0\n"
        f"compatibility: {'c' * MAX_COMPATIBILITY_LENGTH}\n"
        'metadata:\n  author: example-org\n  version: "1.0"\n'
        "allowed-tools: Bash(git:*) Read\n"
    )
    repo.skill("full-skill", frontmatter)
    repo.catalog(repo.plugin("example", "./skills/full-skill"))
    assert check_repository(repo.root).findings == []


def skill_of_lines(repo, total: int) -> None:
    head = "---\nname: sized-skill\ndescription: d\n---\n[why](references/why.md)\n" + REPORTING
    skill_dir = repo.skill_file("sized-skill", head + "line\n" * (total - head.count("\n")))
    (skill_dir / "references").mkdir()
    (skill_dir / "references" / "why.md").write_text("# Why\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/sized-skill"))


def test_skill_md_under_the_line_limit_passes(repo):
    skill_of_lines(repo, MAX_SKILL_LINES - 1)
    assert check_repository(repo.root).findings == []


@pytest.mark.parametrize("over", [False, True])
def test_skill_md_is_held_to_its_character_budget(repo, over):
    head = "---\nname: sized-skill\ndescription: d\n---\n[why](references/why.md)\n" + REPORTING
    filler = "x" * (MAX_SKILL_CHARS - len(head) - 1 + over) + "\n"
    skill_dir = repo.skill_file("sized-skill", head + filler)
    (skill_dir / "references").mkdir()
    (skill_dir / "references" / "why.md").write_text("# Why\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/sized-skill"))
    found = [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings]
    if over:
        assert found == [
            (
                "skills/sized-skill/SKILL.md",
                "size",
                f"SKILL.md is {MAX_SKILL_CHARS + 1} characters, over about 5,000 tokens; keep it "
                f"within {MAX_SKILL_CHARS} and move detail into modules",
            )
        ]
    else:
        assert found == []


def test_skill_md_at_the_line_limit_fires(repo):
    skill_of_lines(repo, MAX_SKILL_LINES)
    report = check_repository(repo.root)
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        (
            "skills/sized-skill/SKILL.md",
            "size",
            f"SKILL.md is {MAX_SKILL_LINES} lines; keep it under {MAX_SKILL_LINES}",
        )
    ]


@pytest.mark.parametrize("name", ["AGENTS.md", "CLAUDE.md"])
def test_context_file_at_the_line_limit_passes(repo, name):
    (repo.root / name).write_text("line\n" * MAX_CONTEXT_LINES, encoding="utf-8")
    assert check_repository(repo.root).findings == []


@pytest.mark.parametrize("name", ["AGENTS.md", "CLAUDE.md"])
def test_context_file_past_the_line_limit_fires(repo, name):
    lines = MAX_CONTEXT_LINES + 1
    (repo.root / name).write_text("line\n" * lines, encoding="utf-8")
    report = check_repository(repo.root)
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        (
            name,
            "size",
            f"{name} is {lines} lines and {lines * 5} bytes; keep it within "
            f"{MAX_CONTEXT_LINES} lines and {MAX_CONTEXT_BYTES} bytes",
        )
    ]


def test_context_file_past_the_byte_limit_fires(repo):
    # Few lines, each a paragraph: a line count alone would pass it.
    (repo.root / "AGENTS.md").write_text(("x" * 1000 + "\n") * 33, encoding="utf-8")
    assert rules(check_repository(repo.root)) == {"size"}


def test_context_file_at_the_byte_limit_passes(repo):
    (repo.root / "AGENTS.md").write_text("x" * (MAX_CONTEXT_BYTES - 1) + "\n", encoding="utf-8")
    assert check_repository(repo.root).findings == []


def test_a_listing_at_its_budget_passes(repo):
    # Each skill-NNN entry is its name, its description and 5 characters: 260 each at 246.
    for number in range(20):
        name = f"skill-{number:03}"
        repo.skill(name, f"name: {name}\ndescription: {'d' * 246}\n")
    repo.catalog(repo.plugin("everything", "./skills/"))
    report = check_repository(repo.root)
    assert (report.listing_chars, report.findings) == (LISTING_BUDGET, [])


def test_reference_that_links_to_another_reference_fires(repo):
    skill_dir = repo.skill("chained-skill", body="See [a](references/a.md).\n")
    (skill_dir / "references").mkdir(exist_ok=True)
    (skill_dir / "references" / "a.md").write_text("Then [b](b.md).\n", encoding="utf-8")
    (skill_dir / "references" / "b.md").write_text("b\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/chained-skill"))
    report = check_repository(repo.root)
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        (
            "skills/chained-skill/references/a.md",
            "reference-depth",
            "links to references/b.md; keep references one level deep from SKILL.md",
        )
    ]


def test_reference_links_back_out_or_to_scripts_pass(repo):
    skill_dir = repo.skill("flat-skill", body="See [a](references/a.md).\n")
    (skill_dir / "references").mkdir(exist_ok=True)
    (skill_dir / "scripts").mkdir()
    (skill_dir / "scripts" / "run.py").write_text("print()\n", encoding="utf-8")
    (skill_dir / "references" / "a.md").write_text(
        "[back](../SKILL.md) [script](../scripts/run.py) [web](https://example.com/x.md)"
        " [missing](gone.md) [here](#top)\n",
        encoding="utf-8",
    )
    repo.catalog(repo.plugin("example", "./skills/flat-skill"))
    assert check_repository(repo.root).findings == []


def test_reference_naming_another_reference_fires_once_per_name(repo):
    skill_dir = repo.skill("named-skill", body="See [a](references/a.md).\n")
    (skill_dir / "references" / "a.md").write_text(
        "Read `b.md` next.\nThen b.md again, and [b as a link](b.md).\n", encoding="utf-8"
    )
    (skill_dir / "references" / "b.md").write_text("b\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/named-skill"))
    report = check_repository(repo.root)
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        (
            "skills/named-skill/references/a.md",
            "reference-depth",
            "links to references/b.md; keep references one level deep from SKILL.md",
        ),
        (
            "skills/named-skill/references/a.md",
            "reference-depth",
            "line 1 names b.md; keep references one level deep from SKILL.md",
        ),
    ]


def test_table_row_split_by_a_pipe_in_code_fires(repo):
    body = (
        "| Question | Command |\n|---|---|\n| Which? | `git branch -vv` |\n"
        "| Gone? | `git branch -vv | grep gone` |\n"
    )
    repo.skill("table-skill", body=body)
    repo.catalog(repo.plugin("example", "./skills/table-skill"))
    report = check_repository(repo.root)
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        (
            "skills/table-skill/SKILL.md",
            "table",
            "line 9 has 3 cells and its table 2; GitHub splits a row on every pipe, even inside "
            "code",
        )
    ]


def test_tables_pipes_in_fences_and_separate_tables_pass(repo):
    body = (
        "| A | B |\n|---|---|\n| x | `y \\| z` |\n\n| One |\n|---|\n| 1 |\n\n"
        "```sh\n| not | a | table |\n```\n"
    )
    repo.skill("table-skill", body=body)
    repo.catalog(repo.plugin("example", "./skills/table-skill"))
    assert check_repository(repo.root).findings == []


def test_a_reference_linking_into_another_skill_is_named_by_its_link(repo):
    skill_dir = repo.skill("first-skill", body="See [a](references/a.md).\n")
    (skill_dir / "references" / "a.md").write_text(
        "And [theirs](../../second-skill/references/b.md).\n", encoding="utf-8"
    )
    other = repo.skill("second-skill")
    (other / "references" / "b.md").write_text("b\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/first-skill", "./skills/second-skill"))
    assert [(f.path, f.message) for f in check_repository(repo.root).findings] == [
        (
            "skills/first-skill/references/a.md",
            "links to ../../second-skill/references/b.md; keep references one level deep from "
            "SKILL.md",
        )
    ]


def test_a_reference_named_further_down_gives_its_own_line(repo):
    skill_dir = repo.skill("named-skill", body="See [a](references/a.md).\n")
    (skill_dir / "references" / "a.md").write_text("\nOne.\nRead b.md next.\n", "utf-8")
    (skill_dir / "references" / "b.md").write_text("b\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/named-skill"))
    assert [f.message for f in check_repository(repo.root).findings] == [
        "line 3 names b.md; keep references one level deep from SKILL.md"
    ]


def test_tables_are_checked_in_every_file_after_the_facts_file(repo):
    skill_dir = repo.skill("table-skill")
    (skill_dir / "references" / "facts.md").write_text("# Facts\n", encoding="utf-8")
    # A table on a file's first line starts that table.
    (skill_dir / "references" / "rules.md").write_text(
        "| A | B |\n|---|---|\n| 1 | 2 |\n\n"
        "```text\n| a | b |\n| c |\n```\n\n"
        "| A |\n|---|\n| 1 | 2 |\n",
        encoding="utf-8",
    )
    repo.catalog(repo.plugin("example", "./skills/table-skill"))
    assert [(f.path, f.message) for f in check_repository(repo.root).findings] == [
        (
            "skills/table-skill/references/rules.md",
            "line 12 has 2 cells and its table 1; GitHub splits a row on every pipe, even "
            "inside code",
        )
    ]


def test_naming_facts_itself_or_other_files_passes(repo):
    skill_dir = repo.skill("named-skill", body="See [a](references/a.md).\n")
    (skill_dir / "references" / "a.md").write_text(
        "Facts are in `facts.md`. This is a.md. Your `README.md`, docs/setup.md, x.md.\n",
        encoding="utf-8",
    )
    (skill_dir / "references" / "facts.md").write_text("# Facts\n", encoding="utf-8")
    (skill_dir / "references" / "setup.md").write_text("setup\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/named-skill"))
    assert check_repository(repo.root).findings == []


@pytest.mark.parametrize("char", ["\u202e", "\u200b", "\u2066", "\ufeff", "\U000e0041"])
def test_hidden_character_in_skill_md_fires(repo, char):
    repo.skill("hidden-skill", body=f"Innocent{char} text.\n")
    repo.catalog(repo.plugin("example", "./skills/hidden-skill"))
    report = check_repository(repo.root)
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        (
            "skills/hidden-skill/SKILL.md",
            "unicode",
            f"line 6 holds U+{ord(char):04X}, which is invisible or reorders text",
        )
    ]


def test_two_hidden_characters_count_the_second_as_one_more(repo):
    repo.skill("hidden-skill", body="One\u200b two\u202e.\n")
    repo.catalog(repo.plugin("example", "./skills/hidden-skill"))
    assert [f.message for f in check_repository(repo.root).findings] == [
        "line 6 holds U+200B, which is invisible or reorders text, and 1 more in this file"
    ]


def test_hidden_characters_at_the_root_and_in_each_directory_are_all_found(repo):
    for relative in ("AGENTS.md", "README.md", "research/run.md", ".github/ci.yml"):
        path = repo.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("x\u200b\n", encoding="utf-8")
    assert [(f.path, f.rule) for f in check_repository(repo.root).findings] == [
        ("AGENTS.md", "unicode"),
        ("README.md", "unicode"),
        ("research/run.md", "unicode"),
        (".github/ci.yml", "unicode"),
    ]


def test_hidden_character_in_a_bundled_file_fires(repo):
    skill_dir = repo.skill("bundled-skill")
    (skill_dir / "scripts").mkdir()
    (skill_dir / "scripts" / "run.sh").write_text("echo ok\u202e\n", encoding="utf-8")
    (skill_dir / "assets.bin").write_bytes(b"\xff\xfe\x00binary")
    repo.catalog(repo.plugin("example", "./skills/bundled-skill"))
    report = check_repository(repo.root)
    assert [(f.path, f.rule) for f in report.findings] == [
        ("skills/bundled-skill/scripts/run.sh", "unicode")
    ]


def test_link_to_another_skill_is_not_a_reference_chain(repo):
    repo.skill("first-skill", body="Pairs with [second](../second-skill/SKILL.md).\n")
    repo.skill("second-skill", body="Back to [first](../first-skill/SKILL.md).\n")
    repo.catalog(repo.plugin("example", "./skills/first-skill", "./skills/second-skill"))
    assert check_repository(repo.root).findings == []


def test_several_hidden_characters_are_counted_once_per_file(repo):
    repo.skill("hidden-skill", body="One\u200b two\u200b three\u202e.\n")
    repo.catalog(repo.plugin("example", "./skills/hidden-skill"))
    report = check_repository(repo.root)
    assert [(f.rule, f.message) for f in report.findings] == [
        (
            "unicode",
            "line 6 holds U+200B, which is invisible or reorders text, and 2 more in this file",
        )
    ]


def test_link_to_a_bundled_script_is_checked_for_existence_only(repo):
    skill_dir = repo.skill("script-skill", body="Run [the build](scripts/build.sh).\n")
    (skill_dir / "scripts").mkdir()
    (skill_dir / "scripts" / "build.sh").write_text("echo [not](a-link.md)\n", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/script-skill"))
    assert check_repository(repo.root).findings == []

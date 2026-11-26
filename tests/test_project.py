"""A repository's own skills (`skillcheck --project`), draft skills, and scripts' tests.

Each rule fires on its planted defect alone, beside a clean pass. Every skill here is synthetic.
"""

from pathlib import Path

import pytest
from conftest import DEFAULT_FRONTMATTER, REPORTING, RepoBuilder

from skillcheck.cli import main
from skillcheck.core import reporting, scripts
from skillcheck.core.checks import check_repository

DRAFT = 'metadata:\n  status: "draft"\n'


@pytest.fixture
def project(tmp_path: Path) -> RepoBuilder:
    """A repository whose own skills live in .claude/skills/, with no catalog."""
    return RepoBuilder(tmp_path / ".claude")


def findings(root: Path, project: bool = True) -> list[tuple[str, str, str]]:
    report = check_repository(root, project=project)
    return [(f.path, f.rule, f.message) for f in report.findings]


def replace_section(skill_dir: Path, body: str) -> None:
    path = skill_dir / "SKILL.md"
    path.write_text(path.read_text(encoding="utf-8").replace(REPORTING, body), encoding="utf-8")


# Project mode


def test_a_clean_project_passes_with_no_catalog(project):
    project.skill("steward")
    report = check_repository(project.root, project=True)
    assert report.findings == []
    assert report.warnings == []
    assert report.summary().startswith("skillcheck: project skills in .claude, 1 skill(s), ")
    assert report.summary().endswith(", 0 finding(s)")


def test_the_same_skills_checked_as_a_catalog_miss_their_catalog(project):
    project.skill("steward")
    assert findings(project.root, project=False) == [
        (".claude-plugin/marketplace.json", "catalog", "missing, so 1 skill(s) ship in no plugin")
    ]


def test_a_project_skill_still_meets_the_other_rules(project):
    project.skill("steward", DEFAULT_FRONTMATTER.format(name="steward") + "author: someone\n")
    assert findings(project.root) == [
        ("skills/steward/SKILL.md", "frontmatter-keys", "fields outside the spec: author")
    ]


def test_a_project_modules_trigger_tests_live_under_claude(project):
    project.modular_skill("steward", "merging")
    assert findings(project.root) == []
    (project.root / "tests/fixtures/modules/merging.json").unlink()
    assert findings(project.root) == [
        ("tests/fixtures/modules/merging.json", "modules", "`merging` has no trigger tests")
    ]


def test_a_project_skill_needs_no_reporting_section(project):
    replace_section(project.skill("steward"), "\n")
    assert findings(project.root) == []


def test_a_project_skill_needs_no_rationale_file_where_a_catalogs_does(project):
    project.skill("steward", rationale=False)
    assert findings(project.root) == []
    assert [rule for _, rule, _ in findings(project.root, project=False)] == [
        "rationale",
        "catalog",
    ]


def test_a_project_skills_section_may_name_its_own_repository(project):
    replace_section(
        project.skill("steward"), "\n" + reporting.section("https://github.com/example/app/issues")
    )
    assert findings(project.root) == []


def test_a_project_skills_section_still_holding_the_placeholder_fires_alone(project):
    replace_section(project.skill("steward"), "\n" + reporting.section(None))
    assert findings(project.root) == [
        (
            "skills/steward/SKILL.md",
            "reporting",
            "the 'When something here is wrong' section reports to "
            f"{reporting.UNKNOWN}; name the repository's own issues page, or remove the section",
        )
    ]


# Drafts


def test_a_skill_marked_draft_passes_and_is_named_in_the_summary(repo):
    repo.skill("fresh", DEFAULT_FRONTMATTER.format(name="fresh") + DRAFT)
    repo.skill("settled")
    repo.catalog(repo.plugin("p", "./skills/fresh", "./skills/settled"))
    report = check_repository(repo.root)
    assert report.findings == []
    assert report.drafts == ["fresh"]
    assert ", 0 fact(s), 1 draft(s): fresh, 1 catalog plugin(s), " in report.summary()


def test_a_draft_project_skill_is_named_in_the_project_summary(project):
    project.skill("steward", DEFAULT_FRONTMATTER.format(name="steward") + DRAFT)
    assert ", 1 draft(s): steward, 0 finding(s)" in check_repository(project.root, True).summary()


def test_another_status_fires_alone(project):
    project.skill(
        "steward", DEFAULT_FRONTMATTER.format(name="steward") + "metadata:\n  status: wip\n"
    )
    report = check_repository(project.root, project=True)
    assert report.drafts == []
    assert [(f.path, f.rule, f.message) for f in report.findings] == [
        (
            "skills/steward/SKILL.md",
            "draft",
            "metadata status is 'wip'; the one status is \"draft\", and a finished skill has none",
        )
    ]


@pytest.mark.parametrize(
    ("frontmatter", "body", "part"),
    [
        (
            "name: steward\ndescription: DRAFT. Merges pull requests. Use when merging.\n",
            "",
            "description",
        ),
        (DEFAULT_FRONTMATTER.format(name="steward"), "# Steward (DRAFT)\n\n", "title"),
    ],
)
def test_the_word_draft_in_a_description_or_title_fires_alone(project, frontmatter, body, part):
    project.skill("steward", frontmatter, body=body + "Body.\n")
    assert findings(project.root) == [
        (
            "skills/steward/SKILL.md",
            "draft",
            f'its {part} says DRAFT; mark a draft with metadata status "draft"',
        )
    ]


def test_draft_as_an_ordinary_word_passes(project):
    project.skill(
        "steward",
        "name: steward\ndescription: Reviews a draft pull request. Use when one opens.\n",
        body="# Steward\n\nA draft is never merged.\n",
    )
    assert findings(project.root) == []


# Scripts and their tests


def script(skill_dir: Path, name: str) -> Path:
    path = skill_dir / "scripts" / name
    path.parent.mkdir(exist_ok=True)
    path.write_text("print('hello')\n", encoding="utf-8")
    return path


def test_an_untested_project_script_warns_alone_and_fails_nothing(project, capsys):
    script(project.skill("steward"), "check_holds.py")
    report = check_repository(project.root, project=True)
    assert report.findings == []
    assert [(w.path, w.rule) for w in report.warnings] == [
        ("skills/steward/scripts/check_holds.py", "scripts")
    ]
    assert report.summary().endswith(", 1 warning(s), 0 finding(s)")
    assert main([str(project.root.parent), "--project"]) == 0
    assert capsys.readouterr().out.splitlines()[0] == (
        "skills/steward/scripts/check_holds.py: scripts: warning: no file in the repository's "
        "tests/ or test/ names or imports it, so CI never runs it"
    )


@pytest.mark.parametrize("directory", ["tests", "test"])
def test_a_project_script_named_in_the_repositorys_tests_passes(project, directory):
    script(project.skill("steward"), "check_holds.py")
    tests = project.root.parent / directory
    tests.mkdir()
    (tests / "test_steward.py").write_text("from check_holds import main\n", encoding="utf-8")
    assert check_repository(project.root, project=True).warnings == []


def test_a_script_here_is_looked_for_in_this_repositorys_tests(repo):
    script(repo.skill("example-skill"), "wrap-check.sh")
    script(repo.skill("other-skill"), "notes.txt")
    repo.catalog(repo.plugin("p", "./skills/example-skill", "./skills/other-skill"))
    assert [w.path for w in check_repository(repo.root).warnings] == [
        "skills/example-skill/scripts/wrap-check.sh"
    ]
    (repo.root / "tests").mkdir()
    (repo.root / "tests/test_wrap.py").write_text('SCRIPT = "wrap-check.sh"\n', encoding="utf-8")
    assert check_repository(repo.root).warnings == []


@pytest.mark.parametrize(
    ("text", "named"),
    [
        ('SCRIPT = SKILL / "scripts" / "check_holds.py"', True),
        ("import check_holds", True),
        ("from scripts.check_holds import main", True),
        ("import scripts.check_holds as holds", True),
        ("import check_holds_v2", False),
        ("check_holds()", False),
    ],
)
def test_a_python_script_is_named_by_its_file_or_an_import(text, named):
    assert scripts.names(text, Path("check_holds.py")) is named


def test_a_shell_script_is_named_only_by_its_file():
    assert scripts.names("import wrap", Path("wrap.sh")) is False


# The command line


def test_project_mode_checks_claude_and_exits_on_findings(project, capsys):
    project.skill("steward", "name: other\ndescription: d\n")
    assert main([str(project.root.parent), "--project"]) == 1
    lines = capsys.readouterr().out.splitlines()
    assert (
        lines[0] == "skills/steward/SKILL.md: name: name 'other' does not match directory 'steward'"
    )
    assert lines[-1].startswith("skillcheck: project skills in .claude, 1 skill(s), ")


def test_project_mode_reads_the_project_skills_facts(project, capsys):
    project.modular_skill("steward", "merging")
    assert main([str(project.root.parent), "--project", "--due", "2026-01-01"]) == 0
    assert capsys.readouterr().out == "skillcheck: 1 fact(s), 0 due by 2026-01-01\n"


def test_project_mode_with_no_project_skills_fails(tmp_path, capsys):
    with pytest.raises(SystemExit) as exited:
        main([str(tmp_path), "--project"])
    assert exited.value.code == 2
    assert ".claude/skills is not a directory" in capsys.readouterr().err


def test_project_mode_refuses_a_whole_repository_mode(project, capsys):
    project.skill("steward")
    with pytest.raises(SystemExit) as exited:
        main([str(project.root.parent), "--project", "--bom-check"])
    assert exited.value.code == 2
    assert "--project works alone or with --due" in capsys.readouterr().err

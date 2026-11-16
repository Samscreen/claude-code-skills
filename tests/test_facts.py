import email.message
import http.client
import subprocess
from datetime import date

import pytest

from skillcheck.cli import main
from skillcheck.core import facts
from skillcheck.core.checks import check_repository

FACTS_MD = "skills/facts-skill/references/facts.md"
HEADER = "| ID | Fact | Source | Quote | Checked | Check by |\n|---|---|---|---|---|---|\n"
FIRST_ROW = 5  # after the title, a blank line, the header and its rule


def row(
    ident: str = "`one`",
    source: str = "[Docs](https://example.com/docs)",
    quote: str = '"a quote"',
    checked: str = "2026-01-01",
    check_by: str = "2026-06-30",
    text: str = "A fact",
) -> str:
    return f"| {ident} | {text} | {source} | {quote} | {checked} | {check_by} |\n"


def facts_skill(repo, table: str, body: str = "Body.\n"):
    skill_dir = repo.skill("facts-skill", body=body)
    (skill_dir / "references" / "facts.md").write_text(f"# Facts\n\n{table}", encoding="utf-8")
    repo.catalog(repo.plugin("example", "./skills/facts-skill"))
    return skill_dir


def findings(repo) -> list[tuple[str, str, str]]:
    return [(f.path, f.rule, f.message) for f in check_repository(repo.root).findings]


def test_well_formed_facts_pass_and_are_counted(repo):
    table = (
        HEADER
        + row()
        + row("`two-links`", "[A](https://example.com/a), [B](https://example.com/b)")
        + row("`escaped`", quote='"the \\"area: \\" prefix"')
        + row(
            "`tag-sha`",
            "`git ls-remote --tags https://example.com/repo`",
            "`0123abcd refs/tags/v1.0.0`",
        )
        + row("`by-hand`", quote="version 1.2.3, uploaded 2026-01-01")
        + "\nProse between two tables.\n\n"
        + HEADER
        + row("`later`")
    )
    facts_skill(repo, table, body="Named: fact `one`, and facts `two-links` and `later`.\n")
    report = check_repository(repo.root)
    assert report.findings == []
    assert report.facts == 6
    by_id = {fact.id: fact for fact in facts.collect(repo.root)}
    assert list(by_id) == ["one", "two-links", "escaped", "tag-sha", "by-hand", "later"]
    assert by_id["one"] == facts.Fact(
        FACTS_MD,
        FIRST_ROW,
        "one",
        ("https://example.com/docs",),
        ("a quote",),
        date(2026, 6, 30),
        date(2026, 1, 1),
        (),
    )
    assert by_id["two-links"].sources == ("https://example.com/a", "https://example.com/b")
    assert by_id["escaped"].quotes == ('the "area: " prefix',)
    assert by_id["tag-sha"].sources == ("git ls-remote --tags https://example.com/repo",)
    assert by_id["tag-sha"].quotes == ("0123abcd refs/tags/v1.0.0",)
    assert by_id["by-hand"].quotes == ()
    assert by_id["later"].line == 15


@pytest.mark.parametrize(
    ("bad_row", "message"),
    [
        (
            "| `one` | A fact | [Docs](https://example.com) |\n",
            "a fact row has 6 cells, not 3",
        ),
        (row(ident="One"), "the ID is not one lowercase, hyphenated name in backticks"),
        (row(ident="`one_two`"), "the ID is not one lowercase, hyphenated name in backticks"),
        (
            row(source="PyPI"),
            "the source is neither an https link nor `git ls-remote --tags <https URL>`",
        ),
        (
            row(source="[Docs](http://example.com)"),
            "the source is neither an https link nor `git ls-remote --tags <https URL>`",
        ),
        (row(quote=""), "the quote is empty"),
        (row(checked="30/09/2026"), "the dates are not both YYYY-MM-DD"),
        (row(check_by="20261231"), "the dates are not both YYYY-MM-DD"),
        (row(check_by="2026-02-30"), "the dates are not both YYYY-MM-DD"),
        (
            row(checked="2026-06-30", check_by="2026-06-30"),
            "the check-by date is not after the checked date",
        ),
        (
            row(ident="`Bad`", quote=""),
            "the ID is not one lowercase, hyphenated name in backticks; the quote is empty",
        ),
    ],
)
def test_malformed_row_fires_alone(repo, bad_row, message):
    facts_skill(repo, HEADER + bad_row)
    assert findings(repo) == [(FACTS_MD, "facts", f"line {FIRST_ROW}: {message}")]
    assert check_repository(repo.root).facts == 0


def test_an_id_defined_twice_fires(repo):
    facts_skill(repo, HEADER + row() + row(checked="2026-02-01") + row(ident="`two`"))
    assert findings(repo) == [
        (FACTS_MD, "facts", f"line {FIRST_ROW + 1}: `one` is already defined above")
    ]
    assert [fact.id for fact in facts.collect(repo.root)] == ["one", "two"]


def test_rows_after_a_malformed_row_are_still_read(repo):
    facts_skill(repo, HEADER + row(quote="") + row(ident="`two`"))
    assert [fact.id for fact in facts.collect(repo.root)] == ["two"]


def test_a_table_written_without_spaces_or_with_aligned_columns_is_read(repo):
    compact = "|ID|Fact|Source|Quote|Checked|Check by|\n| :-- | :-- | :-- | :-- | :-- | --: |\n"
    compact += '|`one`|A fact|[Docs](https://example.com/docs)|"a quote"|2026-01-01|2026-06-30|\n'
    facts_skill(repo, compact)
    assert findings(repo) == []
    assert [fact.id for fact in facts.collect(repo.root)] == ["one"]


def test_collect_gathers_every_skills_facts(repo):
    facts_skill(repo, HEADER + row())
    other = repo.skill("other-skill")
    (other / "references" / "facts.md").write_text(f"{HEADER}{row(ident='`two`')}", "utf-8")
    assert [fact.id for fact in facts.collect(repo.root)] == ["one", "two"]


def test_a_table_with_other_columns_fires_and_its_rows_are_skipped(repo):
    facts_skill(repo, "| Name | Value |\n|---|---|\n| `x` | y |\n")
    assert findings(repo) == [
        (
            FACTS_MD,
            "facts",
            "line 3: a table here has the columns Name, Value; a fact table has ID, Fact, "
            "Source, Quote, Checked, Check by",
        )
    ]


def test_a_named_fact_that_is_not_defined_fires(repo):
    skill_dir = facts_skill(repo, HEADER + row(), body="See fact `missing-one`.\n")
    (skill_dir / "references" / "other.md").write_text(
        "\nFacts `one` and `gone`, and a fact `NOT-AN-ID` in prose.\n", encoding="utf-8"
    )
    # The facts file itself isn't searched: its rows describe facts, they don't name them.
    (skill_dir / "references" / "facts.md").write_text(
        f"# Facts\n\nSee fact `nowhere`.\n\n{HEADER}{row()}", encoding="utf-8"
    )
    assert findings(repo) == [
        (
            "skills/facts-skill/SKILL.md",
            "facts",
            "line 6 names fact `missing-one`, which no fact table in the repository defines",
        ),
        (
            "skills/facts-skill/references/other.md",
            "facts",
            "line 2 names fact `gone`, which no fact table in the repository defines",
        ),
    ]


def test_a_named_fact_in_a_skill_with_no_facts_file_fires(repo):
    repo.skill("plain-skill", body="As fact `node20` says.\n")
    repo.catalog(repo.plugin("example", "./skills/plain-skill"))
    assert findings(repo) == [
        (
            "skills/plain-skill/SKILL.md",
            "facts",
            "line 6 names fact `node20`, which no fact table in the repository defines",
        )
    ]


def test_a_skill_without_its_rationale_fires_alone(repo):
    repo.skill("bare-skill", rationale=False)
    repo.catalog(repo.plugin("example", "./skills/bare-skill"))
    assert findings(repo) == [
        (
            "skills/bare-skill/SKILL.md",
            "rationale",
            "SKILL.md doesn't link references/why.md, which says why the skill advises what it "
            "does, what others do instead, and the trade-offs",
        )
    ]


def test_a_rationale_link_to_a_missing_file_is_a_broken_link(repo):
    repo.skill("bare-skill", body="[Why](references/why.md#the-merge-strategy)\n", rationale=False)
    repo.catalog(repo.plugin("example", "./skills/bare-skill"))
    assert findings(repo) == [
        (
            "skills/bare-skill/SKILL.md",
            "reference",
            "links to references/why.md, which does not exist",
        )
    ]


def fact(ident: str, *sources: str, quotes: tuple[str, ...] = ("a quote",)) -> facts.Fact:
    return facts.Fact(FACTS_MD, 1, ident, sources, quotes, date(2026, 6, 30), date(2026, 1, 1), ())


def test_verify_finds_quotes_however_the_page_sets_them():
    pages = {
        "https://example.com/a": "The  “Latest” release is `2.56.0`, as SHOWN here.",
        "https://example.com/b": "append a line that says (cherry picked from commit abc) to it",
    }
    calls = []

    def fetch(source: str) -> str:
        calls.append(source)
        return pages[source]

    checked = [
        fact("typography", "https://example.com/a", quotes=('the "latest" release is 2.56.0',)),
        fact("elided", "https://example.com/b", quotes=("says (cherry picked from commit …)",)),
        fact("same-page", "https://example.com/a", quotes=("as shown here",)),
        fact("by-hand", "https://example.com/unfetched", quotes=()),
    ]
    assert list(facts.verify(checked, fetch)) == []
    assert calls == ["https://example.com/a", "https://example.com/b"]


def test_verify_reports_a_missing_quote_and_an_unreadable_source():
    def fetch(source: str) -> str:
        if source.startswith("https://example.com/down"):
            raise OSError("HTTP Error 404: Not Found")
        return "the words that are there"

    checked = [
        fact("by-hand", "https://example.com/up", quotes=()),
        fact("unreadable-first", "https://example.com/down", "https://example.com/down-too"),
        fact("gone", "https://example.com/up", quotes=("the words that are there", "and gone")),
        fact("elided-gone", "https://example.com/up", quotes=("the words … never were",)),
        fact("unreadable", "https://example.com/down"),
        fact(
            "one-of-two",
            "https://example.com/down",
            "https://example.com/up",
            quotes=("words that are",),
        ),
    ]
    assert [(f.id, problem) for f, problem in facts.verify(checked, fetch)] == [
        (
            "unreadable-first",
            "https://example.com/down could not be read (HTTP Error 404: Not Found); "
            "https://example.com/down-too could not be read (HTTP Error 404: Not Found)",
        ),
        ("gone", 'the quote is no longer at its source: "and gone"'),
        ("elided-gone", 'the quote is no longer at its source: "the words … never were"'),
        ("unreadable", "https://example.com/down could not be read (HTTP Error 404: Not Found)"),
    ]


def test_a_quote_on_a_source_that_failed_is_not_called_gone():
    def fetch(source: str) -> str:
        if source.startswith("https://example.com/down"):
            raise OSError("HTTP Error 404: Not Found")
        return "the first package's version"

    checked = [
        fact(
            "two-pages",
            "https://example.com/up",
            "https://example.com/down",
            "https://example.com/down-too",
            quotes=("the first package's version", "the second package's version"),
        )
    ]
    assert [problem for _, problem in facts.verify(checked, fetch)] == [
        'the quote is not in the sources read: "the second package\'s version"; '
        "https://example.com/down could not be read (HTTP Error 404: Not Found); "
        "https://example.com/down-too could not be read (HTTP Error 404: Not Found)"
    ]


def test_a_source_that_fails_once_is_tried_again():
    calls: list[str] = []

    def fetch(source: str) -> str:
        calls.append(source)
        if len(calls) == 1:
            raise OSError("HTTP Error 404: Not Found")
        return "a quote"

    assert list(facts.verify([fact("flaky", "https://example.com/flaky")], fetch)) == []
    assert calls == ["https://example.com/flaky"] * 2


def test_a_server_s_words_are_escaped_before_they_reach_a_report_or_an_issue(monkeypatch):
    def fetch(source: str) -> str:
        raise OSError("HTTP Error 500: \x1b[2J\nforged line")

    [(_, problem)] = facts.verify([fact("down", "https://example.com/down")], fetch)
    assert problem.endswith("(HTTP Error 500: \\x1b[2J\\x0aforged line)")

    def failing(args, **kwargs):
        return subprocess.CompletedProcess(args, 128, stdout="", stderr="remote: \x1b[31mred\n")

    monkeypatch.setattr(facts.subprocess, "run", failing)
    with pytest.raises(OSError, match=r"exited 128: remote: \\x1b\[31mred$"):
        facts.fetch_text("git ls-remote --tags https://example.com/repo")


def test_a_transfer_cut_short_is_an_unreadable_source_not_a_crash():
    def fetch(source: str) -> str:
        raise http.client.IncompleteRead(b"partial", 540111)

    [(_, problem)] = facts.verify([fact("cut", "https://example.com/big")], fetch)
    assert problem.startswith("https://example.com/big could not be read (IncompleteRead(")


class FakeResponse:
    def __init__(self, body: bytes, content_type: str) -> None:
        self.body = body
        self.headers = email.message.Message()
        self.headers["Content-Type"] = content_type

    def read(self) -> bytes:
        return self.body

    def __enter__(self) -> FakeResponse:
        return self

    def __exit__(self, *exc: object) -> None:
        return None


def test_fetch_reads_a_page_as_its_visible_text(monkeypatch):
    html = (
        "<html><head><style>p { color: red }</style><script>var x = '<p>hidden</p>';</script>"
        "</head><body><h1>Title</h1><p>One <code>paths</code> and <b>more</b>.</p></script>"
        "<li>Item&nbsp;two</li></body></html>"
    )
    seen = {}

    def urlopen(request, timeout):
        seen["agent"], seen["timeout"] = request.get_header("User-agent"), timeout
        return FakeResponse(html.encode("latin-1"), "text/html; charset=latin-1")

    monkeypatch.setattr(facts.urllib.request, "urlopen", urlopen)
    assert facts.fetch_text("https://example.com/page") == (" Title One paths and more. Item two")
    assert seen == {"agent": facts.USER_AGENT, "timeout": facts.TIMEOUT_SECONDS}


def test_fetch_returns_other_content_as_it_came(monkeypatch):
    body = '{"version": "4.6.2", "note": "café"}'
    monkeypatch.setattr(
        facts.urllib.request,
        "urlopen",
        lambda request, timeout: FakeResponse(body.encode(), "application/json"),
    )
    assert facts.fetch_text("https://example.com/api") == body


@pytest.mark.parametrize(
    ("body", "content_type", "text"),
    [
        ("café".encode("latin-1"), "text/plain; charset=latin-1", "café"),
        # A byte that isn't UTF-8 becomes U+FFFD rather than ending the run.
        (b"caf\xe9", "text/plain", "caf\ufffd"),
    ],
)
def test_fetch_decodes_by_the_charset_the_server_names(monkeypatch, body, content_type, text):
    monkeypatch.setattr(
        facts.urllib.request,
        "urlopen",
        lambda request, timeout: FakeResponse(body, content_type),
    )
    assert facts.fetch_text("https://example.com/notes") == text


def test_fetch_refuses_a_pdf_rather_than_read_its_bytes_as_text(monkeypatch):
    monkeypatch.setattr(
        facts.urllib.request,
        "urlopen",
        lambda request, timeout: FakeResponse(b"%PDF-1.7 \x00\xff", "application/pdf"),
    )
    with pytest.raises(facts.NotText, match="application/pdf"):
        facts.fetch_text("https://example.com/paper.pdf")


def test_a_quote_whose_only_source_is_a_pdf_is_left_to_be_checked_by_hand():
    calls: list[str] = []

    def fetch(source: str) -> str:
        calls.append(source)
        raise facts.NotText("application/pdf")

    assert list(facts.verify([fact("paper", "https://example.com/paper.pdf")], fetch)) == []
    assert calls == ["https://example.com/paper.pdf"]


def test_a_pdf_beside_a_page_still_has_its_quote_looked_for_on_the_page():
    def fetch(source: str) -> str:
        if source.endswith(".pdf"):
            raise facts.NotText("application/pdf")
        return "nothing like it"

    checked = [fact("both", "https://example.com/paper.pdf", "https://example.com/page")]
    [(_, problem)] = facts.verify(checked, fetch)
    assert problem == 'the quote is no longer at its source: "a quote"'


def test_fetch_runs_ls_remote_for_a_tag_source(monkeypatch):
    runs = []

    def run(args, **kwargs):
        runs.append(args)
        return subprocess.CompletedProcess(args, 0, stdout="0123abcd\trefs/tags/v1.0.0\n")

    monkeypatch.setattr(facts.subprocess, "run", run)
    source = "git ls-remote --tags https://example.com/repo"
    assert facts.fetch_text(source) == "0123abcd\trefs/tags/v1.0.0\n"
    assert runs == [["git", "ls-remote", "--tags", "https://example.com/repo"]]


def test_a_failed_or_slow_ls_remote_is_an_unreadable_source(monkeypatch):
    def failing(args, **kwargs):
        return subprocess.CompletedProcess(args, 128, stdout="", stderr="fatal: not found\n")

    monkeypatch.setattr(facts.subprocess, "run", failing)
    with pytest.raises(OSError, match="git ls-remote exited 128: fatal: not found"):
        facts.fetch_text("git ls-remote --tags https://example.com/repo")

    def slow(args, **kwargs):
        assert kwargs["timeout"] == facts.TIMEOUT_SECONDS
        raise subprocess.TimeoutExpired(args, kwargs["timeout"])

    monkeypatch.setattr(facts.subprocess, "run", slow)
    with pytest.raises(OSError, match="git ls-remote took over 30 seconds"):
        facts.fetch_text("git ls-remote --tags https://example.com/repo")


def test_ls_remote_reads_a_real_repository_s_tags_and_reports_a_missing_one(tmp_path):
    def git(*args: str) -> None:
        subprocess.run(["git", "-C", str(tmp_path), *args], check=True, capture_output=True)

    git("init", "-q")
    git(
        "-c",
        "user.name=t",
        "-c",
        "user.email=t@example.com",
        "commit",
        "-q",
        "--allow-empty",
        "-m",
        "x",
    )
    git("tag", "v1.0.0")
    assert facts._ls_remote(str(tmp_path)).endswith("\trefs/tags/v1.0.0\n")
    with pytest.raises(OSError, match="git ls-remote exited 128"):
        facts._ls_remote(str(tmp_path / "missing"))


def dated_skill(repo):
    table = HEADER + row("`soon`", check_by="2026-06-30") + row("`later`", check_by="2027-06-30")
    table += row("`broken`", quote="")  # malformed, so neither mode counts it
    facts_skill(repo, table)


def test_due_lists_the_facts_to_check_again_by_a_date(repo, capsys):
    dated_skill(repo)
    assert main([str(repo.root), "--due", "2026-06-30"]) == 1
    assert capsys.readouterr().out == (
        f"{FACTS_MD}:{FIRST_ROW}: due: `soon` was to be checked again by 2026-06-30\n"
        "skillcheck: 2 fact(s), 1 due by 2026-06-30\n"
    )
    assert main([str(repo.root), "--due", "2026-06-29"]) == 0
    assert capsys.readouterr().out == "skillcheck: 2 fact(s), 0 due by 2026-06-29\n"


def test_due_without_a_date_counts_from_today(repo, capsys):
    facts_skill(repo, HEADER + row(checked="2000-01-01", check_by="2000-01-02"))
    assert main([str(repo.root), "--due"]) == 1
    assert capsys.readouterr().out.endswith(f"1 due by {date.today()}\n")


def test_due_refuses_a_date_it_cannot_read(repo, capsys):
    with pytest.raises(SystemExit) as exited:
        main([str(repo.root), "--due", "30/09/2026"])
    assert exited.value.code == 2
    assert "'30/09/2026' is not a YYYY-MM-DD date" in capsys.readouterr().err


@pytest.mark.parametrize(
    ("text", "ends"),
    [
        (".NET 8 and 9 ended on 2026-11-10, at 8.0.34", [("2026-11-10", date(2026, 11, 10))]),
        (".NET 10 is LTS, to 2028-11-14", [("2028-11-14", date(2028, 11, 14))]),
        ("3.11 gets security fixes until 2027-10", [("2027-10", date(2027, 10, 1))]),
        ("Reaches end of life on 2027-05-05", [("2027-05-05", date(2027, 5, 5))]),
        ("Version 9 is EOL 2026-08-06", [("2026-08-06", date(2026, 8, 6))]),
        (
            "Stable 2.6.5 (2026-11-02); 2.0 serviced to 2027-04-29; 1.8's ended 2026-09-24",
            [("2027-04-29", date(2027, 4, 29)), ("2026-09-24", date(2026, 9, 24))],
        ),
        ("Released 2026-11-02, from 2026-06-16", []),  # a release or a start, not an end
        ("Ends 2026-02-30, or ends 2027-13", []),  # no such day, no such month
        ("Ends early 2027", []),  # no date to count from
    ],
)
def test_a_fact_dates_an_end_of_support_after_a_word_that_ends_it(repo, text, ends):
    facts_skill(repo, HEADER + row(text=text))
    [found] = facts.collect(repo.root)
    assert list(found.ends) == ends


def ending(end: str, checked: str) -> facts.Fact:
    day = date.fromisoformat
    return facts.Fact(
        FACTS_MD, 1, "eol", (), (), day("2030-01-01"), day(checked), ((end, day(end)),)
    )


@pytest.mark.parametrize(
    ("end", "checked", "reasons"),
    [
        (
            "2026-11-10",
            "2026-10-26",
            [
                "names support ending 2026-11-10, which has passed since "
                "it was checked on 2026-10-26"
            ],
        ),
        ("2026-11-10", "2026-11-11", []),  # checked since it passed
        ("2026-11-10", "2026-11-10", []),  # checked on the day it passed
        (
            "2026-11-16",
            "2026-01-01",
            [
                "names support ending 2026-11-16, which has passed since "
                "it was checked on 2026-01-01"
            ],
        ),
        (
            "2027-05-18",
            "2026-01-01",
            ["names support ending 2027-05-18, within six months of 2026-11-16"],
        ),
        ("2027-05-17", "2026-11-15", []),  # checked inside the six months
        ("2027-05-19", "2026-01-01", []),  # 184 days away
    ],
)
def test_an_end_of_support_makes_its_fact_due_once_ahead_and_once_after(end, checked, reasons):
    assert facts.support_ending(ending(end, checked), date(2026, 11, 16)) == reasons


def test_due_counts_a_fact_due_both_ways_once(repo, capsys):
    table = HEADER + row(
        "`eol`", checked="2026-01-01", check_by="2026-06-30", text="Version 1 ends 2026-12-01"
    )
    table += row("`ended`", checked="2026-01-01", check_by="2027-01-01", text="Ended 2026-03-01")
    facts_skill(repo, table)
    assert main([str(repo.root), "--due", "2026-07-01"]) == 1
    assert capsys.readouterr().out == (
        f"{FACTS_MD}:{FIRST_ROW}: due: `eol` was to be checked again by 2026-06-30\n"
        f"{FACTS_MD}:{FIRST_ROW}: due: `eol` names support ending 2026-12-01, within six months "
        "of 2026-07-01\n"
        f"{FACTS_MD}:{FIRST_ROW + 1}: due: `ended` names support ending 2026-03-01, which has "
        "passed since it was checked on 2026-01-01\n"
        "skillcheck: 2 fact(s), 2 due by 2026-07-01\n"
    )


def test_verify_prints_each_fact_it_could_not_confirm(repo, capsys, monkeypatch):
    dated_skill(repo)
    monkeypatch.setattr(facts, "fetch_text", lambda source: "nothing like it")
    assert main([str(repo.root), "--verify"]) == 1
    assert capsys.readouterr().out == (
        f'{FACTS_MD}:{FIRST_ROW}: verify: `soon`: the quote is no longer at its source: "a quote"\n'
        f"{FACTS_MD}:{FIRST_ROW + 1}: verify: `later`: the quote is no longer at its source: "
        '"a quote"\n'
        "skillcheck: 2 fact(s), 2 with a quote to look for, 2 not confirmed\n"
    )
    monkeypatch.setattr(facts, "fetch_text", lambda source: "Here is a quote.")
    assert main([str(repo.root), "--verify"]) == 0
    assert capsys.readouterr().out == (
        "skillcheck: 2 fact(s), 2 with a quote to look for, 0 not confirmed\n"
    )

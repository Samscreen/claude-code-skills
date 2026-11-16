# Decisions

Append-only. Supersede by adding a new entry that points at the old one; never edit history.

From 2026-11-16, a release is one line in the entry of the change it ships, not an entry of its
own. Entries before 2026-10-16, and the release-only entries since, are on the `archive` branch;
the last section lists each that still stands or is cited.

## 2026-11-16 — This repository re-checked against standard v0.49.1, for release 0.1.30

- **Asked:** the owner's "do all" (2026-11-16), to a list that named the re-check the README's
  release steps promise after each release. The last one recorded was of 2026-09-30, against
  v0.40.0. A helper ran the standard's audit, read-only, to its first wait, on `main` at
  `c8c3a07`, tier T3. Result: six dimensions `OK`, two `DRIFT`, two `GAP`.
- **Fixed here, documentation and a test:**
  - The README's release steps and `docs/withdrawing-a-skill.md` said the release reaches
    Claude Code plugin installs. It's the merge that changes the catalog's `version`: an install
    takes `main` as it stands once the version string changes, released or not. Claude Code's
    documentation says so, read 2026-11-16 ([Release a new
    version](https://code.claude.com/docs/en/plugins/host-marketplace#release-a-new-version):
    "Bump `version` on each release: users stay on their cached copy until the string
    changes."). That answers the question the entry of 2026-10-26 left "not yet checked". Cloud
    sessions with the hook still take the release.
  - Both tracked shell scripts, `src/skillcheck/cloud-setup.sh` and `house-style`'s
    `wrap-check.sh`, are now linted by a test that runs ShellCheck on every tracked `*.sh`.
    Neither is a Markdown example, so nothing read them before. Both pass.
- **Recorded:**
  - A19's trigger fired. The inception entry declined mutation testing while branch coverage
    was 100%, until "a check is found letting through a defect its test says it catches". The
    mutation run of 2026-11-03 found 7 of 112 mutants and 27 of 51 hand-made ones surviving,
    which is that trigger, and the entry of that day didn't name A19. Whether mutation runs on
    `core/` become a step of each release, or stay one-off with a new trigger, is the owner's.
  - ShellCheck, which `shellcheck-py` (MIT) carries, is GPL-3.0, and `@anthropic-ai/claude-code`
    is under Anthropic's own terms. Both are development tools, run in CI and by hand, and never
    in a release asset or a skill. The allowlist takes GPL with a recorded internal-only
    decision, which this is for ShellCheck. Claude Code's terms need the owner's explicit yes,
    asked in the report.
- **Waiting on the owner:** a `skillcheck` rule that every commit the records cite stays
  reachable from `main` (all 17 do today, checked by hand); a pull request rule on `main`, asked
  on 2026-10-05; whether the `copier` template's and reusable workflows' triggers have fired,
  since the private companion runs `skillcheck` from here; and how often this re-check runs.
  The standard proposal S1, fewest dependencies and newest versions from R21, is drafted for the
  owner's approval. R01 and R04 don't support a rule on keeping one application's data from
  another, so nothing is proposed for it.

## 2026-11-16 — Finished records move to the `archive` branch

- **The owner's word:** "do all" (2026-11-16), given to a list that named moving `ROADMAP.md`'s
  finished findings and lessons, and decisions before 2026-10-16, to `archive`, which the
  documentation audit of that day proposed. It changes `docs/archive.md`'s answer that these
  files stay whole on `main`.
- **Moved, verbatim, to `archive:2026-11-16/`:** the standard's findings F1 to F167, less F165,
  still planned; the 52 lessons their modules took in (L23, L25 and L27 the same day); the front
  door's choices of 2026-10-13; every decision entry dated before 2026-10-16; and the eleven
  entries since that only record a release. Each archive file opens with the commit it came from.
- **Kept on `main`:** every open lesson as it stood, F165, the pieces table, whose rows now name
  the findings each piece places, and the front door's open items with a one-item summary of
  its choices. `docs/decisions.md` ends with a section listing each standing or cited decision
  from before 2026-10-16, the pointers in later entries that name a moved one, and each moved
  release, so the old entries stay as written.
- **Changed:** from 2026-11-16, a release is one line in the entry of the change it ships, not
  an entry of its own. Releases 0.1.19, 0.1.20 and 0.1.22 keep their entries, since each records
  more than its contents. The README's withdrawal runbook is now `docs/withdrawing-a-skill.md`,
  linked from the README's Operations section.
- **Measured:** `ROADMAP.md` from 1,452 lines to 487; `docs/decisions.md` from 3,837 to 1,927,
  counting the day's new entries.
- **Checked:** nothing in `src/skillcheck` reads a lesson, a finding, a decision entry or a README
  section; `skillcheck` reports 0 findings, and the suite's 652 tests pass.
- **Left to the owner:** the 0.1.25 entry's open item, the claude.ai tries of `ci-workflows` and
  `ci-speed`, which no later entry records. The steward now cites answer 4 through the end
  section.

## 2026-11-16 — `markdown-format` split from `writing-style`; L23, L25 and L27 taken in

- **Why now:** `writing-style` (15,925 characters) and `prose-check` (15,996) sat at the
  16,000-character limit, as the 2026-10-27 entry warned, and L25 and L27 waited for
  `writing-style`, which had no room.
- **The seam:** what prose says against how a Markdown file is laid out. `writing-style` keeps
  rules 1 to 7 and 11 to 13: voice, words to cut, plain words, American spelling, dates and
  records. The new `markdown-format` takes rules 8 to 10: headings, wrapping, lists, code
  blocks, tables, links and emphasis, file names and a README's sections, with their Why
  sections. Both stay in `house-style`, so no row in `docs/module-moves.md`. Every fact keeps
  its ID: `google-sentence-case` and `ms-sentence-case` move to `markdown-format`.
- **`prose-check` trimmed to 14,869 characters,** with no rule lost: the spelling rule's list of
  patterns moved to `writing-style`'s American spelling section, and the `heading-colon` fact,
  a style guides' fact, to `markdown-format`. `prose-check` names both.
- **Lessons taken in:**
  - L25, in `writing-style`'s *Claims and their evidence*: the strongest verb the evidence
    supports and no stronger, the artifact named, and what an absence means. Its Why cites L25,
    with L5 and L4 as the cases.
  - L27, in `writing-style`'s *Instructions for a reader who isn't a programmer*: no
    application name where it could be typed, the screen described, one command per block
    with its expected output. `markdown-format`'s code rule and Why carry its formatting half.
  - The rest of L23, in `coding`'s `c-build`: argument shape is a probe axis of its own (rule
    8, the Fuzzing section, an audit row and the Why, which now cites L23 three times). Room
    came from tighter wording and shorter quotes that stay exact substrings of the checked
    ones, with no rule, mistake, audit row or example cut: 15,970 characters, so its next
    addition splits it first.
- **One new fact,** `google-code-font`: Google keeps code font for text entered verbatim, and
  bold, not code font, for a named element on screen. Read at the source on 2026-11-16.
- **Pointers moved:** the router, `documentation`'s and `prose-check`'s openings, the
  `prose-check` trigger test's note, and `architecture`'s `repo-structure`, which sent Markdown
  file names to `writing-style`, now name `markdown-format`.
- **Reviewed against `docs/authoring-a-skill.md`, for `markdown-format`:**
  1. Whose work: the owner's own, moved from `writing-style`; nothing work-owned.
  2. Sources: three facts moved with their IDs and dates; one new, checked today.
  3. Licenses: Google's guide is CC BY 4.0 (fact `google-license`), Microsoft's short quotes
     for facts, as before.
  4. No secrets, company detail or audited repository: the L27 case is "one owner".
  5. Fits both surfaces: no tool names, no network.
  6. Frontmatter: `house-style`'s description already covers Markdown; unchanged.
  7. Shape: Rules, Mistakes, Audit, Why, Facts, Sources; 9,924 characters; other modules named
     in words.
  8. No code blocks added.
  9. Trigger evaluations: five should-trigger requests and three near misses
     (`writing-style`, `prose-check`, `documentation`). `writing-style`'s set gains a claims
     request and a non-programmer request, and its heading near miss now names
     `markdown-format`.
  10. Catalog unchanged, since the skill isn't new; a shipped `ROADMAP.md` row; the README's
      `house-style` row still fits.
  11. CHANGELOG lines below; `metadata.reviewed` was already 2026-11-16.
  12. No old copy on claude.ai covers this module, so nothing to delete.
- **Requests for the owner to try on claude.ai,** from `uv run skillcheck --tries
  markdown-format writing-style`: "Are headings in sentence case or title case here?" should
  read `markdown-format`, not `writing-style`; "Rewrite this README so it reads plainly and
  drops the marketing fluff." should read `writing-style`, not `markdown-format`.

## 2026-11-16 — `testing`'s `test-strategy`, from R06c

- **Asked, by the owner:** "do all" to the triage list (2026-11-16), which included the
  planned `test-strategy` row.
- **Built:** `test-strategy`: tests sorted by size and by scope, the mix set by what broad
  tests cost rather than by a shape, a command-line program's logic tested in process and its
  binary in a temporary directory, real dependencies kept where quick and hermetic, test data
  built per test from factories, an inventory of the program's commands and settings matched
  against tests, skipped tests counted, and metamorphic and differential testing where no
  oracle exists. 13 facts, prefix `ts-`, each quote read at its source on 2026-11-16.
- **Sources:** R06c's checked claims (Fowler's TestPyramid and test-shapes article, Dodds'
  trophy, *Software Engineering at Google* ch. 11, the Tetragon pull request, Testcontainers'
  versions, with Go at v0.45.0 as R06c's verification corrected). R06c doesn't cover
  metamorphic or differential testing, and R06b names them only as unchecked leads. Those were
  checked today against the primary sources, as `research/README.md` allows when a skill relies
  on a claim: Chen, Cheung and Yiu's 1998 report (arXiv 2002.12543), Segura and others' 2016
  survey (White Rose eprint), and Yang and others' Csmith paper (PLDI 2011). Test data adds
  pytest's `tmp_path`, Go's `t.TempDir()` and factory_boy 3.3.3, read today from their docs
  and PyPI. R06c's factory_boy and Bogus lines were unchecked; Bogus isn't used.
- **Moved:** `testing-patterns`' "Strategy, still being checked" paragraph is gone (15,960 to
  15,734 characters); it held no facts, so no ID moved. Its ROADMAP row drops "Strategy".
- **Neighbours:** `test-oracles` no longer says differential and metamorphic testing wait for
  R06c; `acceptance-runs`, `flaky-tests` and `test-gates` send test strategy to
  `test-strategy`. The router gains its row, the description gains "strategy, test data"
  (249 characters), and `metadata.reviewed` is 2026-11-16. The README's `testing` row names
  test data and metamorphic and differential testing.
- **The review in `docs/authoring-a-skill.md`:**
  1. Whose work: this repository's own; nothing work-owned.
  2. Sources: each fact from a primary source with its link, exact quote, checked 2026-11-16,
     and a check-by date (six months for guidance, three for versions). Three PDFs are checked
     by hand when due.
  3. Licenses: SWE at Google CC BY-NC-ND 4.0 and Fowler's pages quoted, never adapted; Dodds,
     the papers and Tetragon (Apache-2.0) as short quotes; pytest, Go and factory_boy docs as
     short quotes. Nothing adapted, so no notice file.
  4. No secrets, company detail or audited repository names; the one named project, Cilium
     Tetragon, is a research source.
  5. Fits Claude Code and claude.ai: no commands to run, no tool names.
  6. Frontmatter: spec fields only; description at 249 characters.
  7. Shape: Rules, Mistakes, Audit (status words only), Why, Facts, Sources; 15,511
     characters; names other modules in words.
  8. No code examples.
  9. Trigger evaluations: six requests that should reach it and two near misses (a mutation
     tool's version, `testing-patterns`; a test passing one run in ten, `flaky-tests`).
  10. ROADMAP row shipped; README row updated; `skillcheck` 0 findings.
  11. CHANGELOG lines below; `metadata.reviewed` set.
  12. Old copy: none; a new module of a shipped skill.
- **Found, not changed:** SWE at Google ch. 11 recommends "only measuring coverage from small
  tests to avoid coverage inflation", while `testing-patterns` rule 2 says to count
  integration and system tests' coverage too. The two need reconciling in `testing-patterns`,
  with that quote as a fact, in a later change.
- **Not taken in:** snapshot and approval-testing rules, transaction rollback per test, and
  idioms per language, which R06c lists as not covered.

## 2026-11-16 — The end-of-life warning, in `--due`

- **What:** the roadmap's end-of-life warning, planned since its trigger was met in 0.1.22,
  is built into `skillcheck --due`. A fact whose own text dates an end of support makes it due
  once when that end comes within six months (183 days) and again once the end has passed,
  each unless the fact was checked inside that span. The Freshness workflow names it in the
  existing "Due to be checked again" section, and `--due`'s exit code opens the issue, so the
  workflow is unchanged.
- **The signal:** an ISO date (`YYYY-MM-DD`, or `YYYY-MM` counted from the month's first day)
  straight after a word that ends support: "end", "ends", "ended", "EOL", "end of life", "end of
  support", "removed", "retired", "discontinued", "halted", "to", "until" or "through", with an
  optional "on" or "in". Only the Fact column counts: the quote is the source's wording, and a
  date alone is most often a release's. Tested against all 1,111 facts on 2026-11-16: it finds
  16 facts and 21 dates, all of them ends of support or of a runtime, and none of the 98 facts
  with only release or start dates. No marker on fact rows was needed.
- **Why not list every end in the window or past:** a fact that records an end already past,
  such as `py-eol-310`, would keep the weekly issue open for good. Counting the end only when it
  has come since the fact's Checked date makes the warning one an author clears by checking the
  fact again, as with a check-by date.
- **What it misses:** three facts date an end in words the pattern doesn't read.
  `win-server-support` lists its dates after "ends:" ("2016, 2027-01-12"), and Windows Server
  2016's end, 2027-01-12, is inside six months now; `linux-ubuntu` says "22.04 ends May 2027";
  `os-timefold-editions` says "1.x ends early 2027", which has no day. The first two are reworded here,
  and step 2 of `docs/authoring-a-skill.md` now says to write an end of support that way.
  PowerShell 7.4 and 7.5's fact was read again at its source and now says they ended.
- **First run, 2026-11-16:** `ps-lifecycle-74-75` (PowerShell 7.4 and 7.5 end 2026-11-10,
  checked 2026-10-26) is due.

## 2026-11-16 — Anthropic's document skills may be adapted, from a pinned commit

- **Approved, by the owner:** F, on 2026-11-11 (the entry of that date below records the
  answers). It supersedes the rule that took nothing from Anthropic's source-available
  document skills.
- **Why:** the license files of `skills/docx`, `skills/pdf`, `skills/pptx` and `skills/xlsx`
  in anthropics/skills, and its README, say Apache 2.0 (read 2026-11-11 on the `main` branch),
  so the reason for the rule no longer holds.
- **The guard:** a file is taken only from a pinned commit whose license file was read at
  that commit, named in the skill's notice, since a license can change again.
- **Where it applies first:** R16's `business-apps` work, on Word and Excel documents.
- **Merged by a session on the owner's word,** "do all" (2026-11-16), given to a list that
  named this pull request (#143) as the owner's to merge, since it changes `AGENTS.md`.

## 2026-11-16 — Documentation audit: what agreed, what was fixed, what was combined

- **The owner's word:** "review all open tasks, questions, open items, unresolved issues, and
  triage them. audit and review all documentation and make sure all is consistent and on the
  same page. do not release or do anything aside from document though", then "is all
  documentation needed? or can we combine to make easier to research and audit?" (2026-11-16).
  Nothing is released, and this pull request is the owner's to merge, since it changes
  `AGENTS.md` and `.claude/`.
- **Read:** three helpers, each checked here: every skill's router and the opening of every
  module; every file at the root; `docs/`, the research index and prompts, `.claude/` and
  `.github/`, with GitHub's rulesets, branches and pull requests as they stood on 2026-11-16.
  They found 66 inconsistencies and 42 open items.
- **Fixed, documentation only:**
  - Skills and modules that named each other wrongly: `git-workflows` forbade the tracked
    quarantine `testing`'s `flaky-tests` allows; modules called planned ones shipped, or shipped
    ones planned; a schema, an error's place on screen and an agent's context file pointed at
    the wrong module. Four descriptions now name what their modules cover.
  - Root files: CONTRIBUTING's count of shipped skills, the README's skill rows and uv version,
    `AGENTS.md`'s fixtures line and its old `references/why.md` branch, the duplicated 0.1.25
    changelog line, and an `[Unreleased]` entry for f902d4c and this change.
  - The merge exception of 2026-11-11 (the entry of that date, *Merging, a standing word*) is
    now in `AGENTS.md` and the steward, which each name the other's copy.
  - `ROADMAP.md`: the Research column now holds follow-up prompts still to run as well; the
    skill table's "Loads when" marks planned scope; lessons L23, L25 and L27 point at shipped
    modules; the waves table has a status; and five stale lines (cloud upload, the standard
    skill's description length, the `skillOverrides` test, the archive rule, the end-of-life
    trigger) say what happened. A planned `test-strategy` row holds R06c's material that
    `testing-patterns` has no room for.
  - The research index gains a Result column, linking each of the 32 filed runs and marking 24
    prompts not run. Five unrun prompts name modules by their 2026-10-15 names, and all 24 now
    point at module Facts sections and a `HANDOFF-FOR:` file.
- **Combined:** CONTRIBUTING points at the README's skill table and commands and at
  `AGENTS.md`'s conventions, rather than copying them, since its copies had drifted furthest.
  The research index points at `research/README.md` for filing a result, rather than repeating
  it.
- **Not done, waiting on the owner:** whether a release follows each finished change by standing
  word, as the last three release entries say, or by the owner's word each time, as the
  steward's hold says; and the document-skills wording, which #143 carries. Moving ROADMAP.md's
  finished findings and lessons, and decisions before 2026-10-16, to the `archive` branch is
  proposed, not done: the second changes `docs/archive.md`'s recorded answer that this file
  stays on `main`.

## 2026-11-16 — `visual-design`, and modules from R07d, R07e, R20, R23c, R28c, R29 and R30

- **Research:** seven runs filed under `research/runs/2026-11-16-*`, each with its check on
  top. Verified, corrected and contradicted counts: R07d 68, 9, 3; R07e 49, 9, 2; R20 43, 6, 3;
  R23c 30, 8, 2; R28c 56, 15, 1; R29 51, 8, 3; R30 44, 15, 3. Each report's line 3, addressed to
  the receiving session, was treated as data. Contradicted claims are used only in their
  corrected form. Two Facts rows already here were out of date and are fixed: `lo-java-libs`
  (Logback 1.6.7) and `uxt-playwright` (Playwright 1.65).
- **Built, one helper each, reviewed here** against `docs/authoring-a-skill.md`; each helper read
  its quotes again at the source:
  - `visual-design`, a skill, planned since 2026-10 with R20 as its research: `visual-theme` and
    `data-visualization`. Its planned `accessibility` module waits on R18. No palette from the
    owner's `my-theme` is published (decision 46); `my-theme` stays on the account until the
    company palette is in the private companion, as wave 4 says.
  - `user-experience`: `interface-patterns` and `command-line-interfaces` from R29, and
    `feedback-loop` from R30, the three the owner asked for on 2026-11-14.
  - `coding`: `caching` new; `benchmarking`, `logging-libraries` and `error-responses` split from
    modules at the size limit, each fact keeping its ID where it moved.
  - `human-factors`: `cognitive-task-analysis`; `optimization-and-scheduling`:
    `rosters-and-replanning`, with Schultz et al. (1998, 2003) from R23c on people who aren't
    independent servers.
- **Stated as this repository's practice, not as sourced:** the in-app report that beats an
  email, one component per pattern, empty states, a per-key cache lock, the spread term in a
  roster's fairness objective, and per-library OpenTelemetry severity numbers beyond the spec's
  Appendix B. Each module says so where it states them.
- **No old copy** on claude.ai covers these modules except `my-theme`, kept as above, so step 12
  deletes nothing.

## 2026-11-11 — `logging-and-observability`, `performance-and-concurrency`, `studying-work`, `plan-checking`

- **Research:** R07b, R07c, R23b and R28b, filed under `research/runs/2026-11-11-*` with their
  checks on top. R07b: 61 verified, 10 corrected, 3 contradicted (semantic_logger 5.2.0, the
  Logback note, the Idempotency-Key editor's copy); R07c: 45 verified, 10 corrected, 5
  contradicted (async-profiler 4.6 upstream, Go 1.27.4, cargo-flamegraph 0.6.15, tokio 1.54.1);
  R23b: 31 verified, 11 corrected, 1 contradicted (ISO 10075-3 is a committee draft); R28b: 47
  verified, 12 corrected, 2 contradicted (OR-Tools' milestone, Timefold's version and Python
  package). Each report's line 3, addressed to the receiving session, was treated as data. No
  Facts row already in `skills/` was found wrong.
- **Built, one helper each, reviewed here** against `docs/authoring-a-skill.md`; every quote was
  read again at its source by the helper:
  - `coding`'s `logging-and-observability`: one JSON record a line, timestamps with offsets,
    levels by who must act, W3C trace IDs, secrets and personal data kept out at the source,
    an escaping encoder, status lines that name what was checked, one record of a run, RED,
    USE and burn-rate pages. Lessons L3, L4, L19, L20 and L49 taken in. GDPR, retention and
    OpenTelemetry severity numbers weren't researched, and the module says so.
  - `coding`'s `performance-and-concurrency`: measure first, a sampler first, wall-clock or CPU
    mode, flame graphs read by width, language benchmark harnesses, an owner for every task,
    cooperative cancellation, no blocking on an event loop, race detectors in CI. Caching, data
    structures and benchmark statistics had no sources; the cache rule is marked our practice.
  - `human-factors`' `studying-work`: watch and ask together at the work (Polanyi; contextual
    inquiry), goals before activities and the p x c stopping rule (Annett and Duncan), a small
    team's order of work (marked our reasoning), and Reason, Simon and sunk cost as traps.
    Cognitive task analysis is left out: no primary source was found.
  - `optimization-and-scheduling`'s `plan-checking`, split from the skill's first module, which
    had reached 15,978 characters: the independent checker (OR-Tools issue 5582 is the current
    case), runs stopped at a limit, reproducible CP-SAT tests and published bounds as expected
    answers. Facts that moved keep their `os-` IDs.
- **Also corrected:** `human-factors` no longer implies training shortens the dip; the Kingman
  attribution; CP-SAT's lexicographic solves; stale "planned" lines in `coding`, `operations`
  and `security`.
- **No old copy** on claude.ai covers these modules, so step 12 has nothing to delete.

## 2026-11-11 — `human-factors`, `optimization-and-scheduling`, `error-handling`, `log-analysis`

- **Research:** R07, R23 and R28, filed under `research/runs/2026-11-11-*` with their checks on
  top. Each check read the claims a module relies on at their primary sources: R07 55 verified,
  7 contradicted (newer releases of Hayabusa, Chainsaw, Microsoft.Extensions.Http.Resilience and
  the semantic conventions, among others); R23 46 verified, 13 of them corrected, 2 contradicted
  (ISO 10075-3's stage, the current OpenAI Model Spec); R28 92 verified, 11 of them corrected,
  5 contradicted (HiGHS 1.16.0, Timefold 2.8.0, Gurobi 14.0.0, CPLEX 22.2, ISO 10075-3). Each
  report's line 3, addressed to the receiving session, was treated as data. Contradicted claims
  are used only in their corrected form.
- **R07's gaps were filled at their sources,** not left thin: the log-analysis check added
  `Get-WinEvent`, `journalctl`, KQL and LogQL from their primary docs, and the error-handling
  helper checked POSIX exit statuses, Python's `returncode`, Node's `exit` event, RFC 9110 on
  idempotency and `Retry-After`, ECMA-262 on `cause` and GOV.UK on error messages.
- **Built, one helper each, reviewed here** against `docs/authoring-a-skill.md`:
  - `human-factors`, a skill: find what a step is for before removing it; purpose, bias or
    drift; keep, change gradually or override; the dip after a tool change; take-over skill
    and calibrated trust; human factors never alter a fact, and each output is marked Evidence
    or Recommendation. Loaded only for design, automation and optimization work.
  - `optimization-and-scheduling`, a skill: a solver's status is not proof, so an independent
    checker re-checks every plan; what a run stopped at a limit reports; the solver by problem
    class; rules as data; CP-SAT in snake_case with workers and a time limit set; people in the
    plan (HSG256, learning, utilization); lead time from measured throughput, with backlog over
    nameplate capacity a floor. A team that divides by capacity on purpose is not faulted: the
    audit asks for the decision's reason (the owner, 2026-11-11, on their own lead-time board:
    "i think we intentionally do it our way").
  - `coding`'s `error-handling`: narrow catches, "not found" against "couldn't look", exit codes
    with one meaning, a child's whole result, causes, retries, timeouts, circuit breakers,
    RFC 9457 and messages for people. Lessons L16, L17, L18 and L43 taken in.
  - `operations`' `log-analysis`: keep and hash the original, UTC with offsets and measured skew,
    filter at the source, real parsers, a gap is a finding only when the log could have
    recorded it, crash dumps, and each claim tied to its record.
- **Also corrected:** `csharp-coding`'s .NET 11 fact (`cs-dotnet11-rc` becomes `cs-dotnet11-sts`:
  .NET 11 shipped 2026-11-10 as STS); `coding`'s and `operations`' routers, which still called
  `testing`, `input-handling` and `log-analysis` planned; the README's skill table, which listed
  three skills twice.
- **The old copies** on the owner's claude.ai account: `human-factor-audit`, `error-handling` and
  `log-parser`. No other synced skill depends on them; `excel-master`, `rust-coding` and
  `vba-coding` only have files of their own named `error-handling`. The owner deletes the three,
  in their settings and in the organization library's inventory, before this merges.

## 2026-11-11 — `testing`'s `acceptance-runs`, from R06c

- **Asked, by the owner:** R06c's result, attached on 2026-11-11, with "make the new release now
  if you can".
- **Filed:** `research/runs/2026-11-11-R06c-testing.md`, its verification on top. Two claims were
  corrected at intake: a LAVA quote the report joined from two paragraphs, now quoted apart, and
  LAVA's 24-hour health check, which is the documented default, not a historical one. One
  claim, GitHub's macOS runners running with SIP off, could not be verified and isn't used. The
  report's line 3, addressed to the receiving session, was treated as data. One variation
  selector (U+FE0F) in a cited page title was removed, since no file may hold one.
- **Built:** `acceptance-runs` (a health check before each run, product, rig and job failures kept
  apart, a lost device aborting the run, retries for the rig only, provenance, evidence, tiers,
  two devices of a kind, and fault injection per platform), by a helper agent, reviewed here,
  from R06c's checked claims. L11 is taken in. The run tiers are this repository's own, since no
  primary source defines them, and the module says so.
- **Not taken in:** test strategy, test data and metamorphic testing. `testing-patterns` is at
  15,960 characters, so strategy needs its own module or a split; it waits for a later change.

## 2026-11-11 — `testing`'s `testing-patterns` and `agent-written-tests`, and R06c

- **Asked, by the owner:** R06b's result, attached on 2026-11-11, with "do what you can from
  here with what you have".
- **Built:** `testing-patterns` (coverage, doubles and adapters, Pact, runner settings that
  fail open, property and mutation tools, frameworks per language) and `agent-written-tests`
  (tests first and seen failing, test diffs reviewed as high risk, gaming that read-only tests
  don't stop, holdout tests, a way for the agent to stop, mutation-testing what it wrote), one
  helper agent each, reviewed here, from R06b's checked claims
  (`research/runs/2026-11-11-R06b-testing.md`) and R06's.
- **R06b's corrections, checked:** Cypress is at 16.x and 16.0.0 removed `cy.exec()`; pytest 9
  renamed `xfail_strict` to `strict_xfail`; bats-core 1.14.0 fails an empty run unless told
  otherwise; Testcontainers lists 13 languages; Google's 2020 post endorses coverage gates a
  team chooses.
- **Planned:** `acceptance-runs`, for unattended acceptance runs on hardware and fault
  injection, which R06b didn't reach; L11 moves to it. R06c asks those questions and the rest
  R06b listed as not covered.
- **The old copy:** the owner's claude.ai skill `testing-patterns` is deleted on the session's
  word before this merges, as the owner chose on 2026-11-11.

## 2026-11-11 — The owner's answers: merging new skills, D, E, F, the old copy and 0.1.26

- **Merging, a standing word:** a session may merge #140, and any later pull request whose only
  change under `.claude/` is a `skillOverrides` line turning off a new skill's installed copy,
  once CI is green (the owner, 2026-11-11, choosing "Yes, standing word" to: "Merge #140 now,
  and later pull requests whose only .claude/ change is a skillOverrides line for a new skill,
  once CI is green. Changes to AGENTS.md, CLAUDE.md, workflows or anything else in .claude/
  still wait for you."). Every other change to `.claude/`, `AGENTS.md`, `CLAUDE.md` or a
  workflow still waits for the owner.
- **Approved for the standard, as 0.49.1 in a pull request of its own:** D, turns in a review
  loop, in two tiers; and E, secrets from the environment or a secret store, never the
  repository, a command line or a log.
- **Approved for `AGENTS.md` and the authoring review:** F, Anthropic's document skills may be
  adapted under Apache-2.0, from a pinned commit whose licence was confirmed, since the
  licence files in `docx` and `xlsx` say Apache 2.0 (read 2026-11-11). The owner merges it.
- **The old `testing-patterns` on claude.ai:** deleted by the owner on the session's word,
  once the `testing-patterns` module is ready, before it merges.
- **Release 0.1.26:** once #140 and `testing-patterns` are merged and green, without asking
  again.

## 2026-11-11 — `operations`, with four modules, replacing three old skills

- **Asked, by the owner:** "finish what you can ... to a fully complete stage" (2026-11-11).
  Planned for wave 4 of the rebuild, with R11 and R15 run on 2026-10-26.
- **Built:** `windows-admin`, `linux`, `docker-containers` and `networking-security`, one
  helper agent each, reviewed here, every fact fetched on 2026-11-11. Corrections to the
  research: Windows Update for Business is now Windows Update client policies; Server 2022's
  mainstream support ended 2026-10-14; Debian 12's regular security support ends 2026-07-11,
  not 06-10; Suricata is at 8.0.8 and Zeek's LTS at 9.0.1. `log-analysis` waits for R07;
  `kubernetes`, `cloud` and `infrastructure-as-code` stay on request.
- **Old copies, before this merges:** the owner's claude.ai skills `windows-admin`,
  `docker-containers` and `networking-security` share these modules' names. The owner deletes
  them, in their own settings and in the organization library's inventory, by
  `docs/authoring-a-skill.md` step 12. Among the synced skills, `networking-security` names
  the other two and `windows-admin` names `networking-security`; all three go together, so
  none is left naming a deleted one.
- **Sources:** Microsoft Learn, distribution and systemd documentation, OpenSSH, Docker's and
  Podman's documentation, nftables, WireGuard, the Wi-Fi Alliance, CISA, NIST and the
  Suricata and Zeek projects. Facts in our own words, with short quotes. Nothing adapted.
- **Merged by the owner,** because `.claude/settings.json` turns off the new skill's installed
  copy here.

## 2026-11-11 — `git-workflows`' `ci-cd` and `versioning-and-releases`

- **Asked, by the owner:** "finish what you can ... and anything else in the repo but partially
  complete, to a fully complete stage" (2026-11-11). Both were planned, with research run on
  2026-09-23 (R05, R08) and 2026-10-26 (R21), and never built.
- **Built:** one helper agent per module, reviewed here. R08 lists environments as not
  covered, and R05 is mostly supply chain, so both rest on primary sources fetched on
  2026-11-11: GitHub Docs, Python's and Node's release schedules, PEP 387, Keep a Changelog,
  Twelve-Factor, Google's SRE book and Fowler.
- **Lesson taken in:** L24 (`versioning-and-releases`).
- **Sources:** GitHub Docs (CC BY 4.0), the rest as each states. Facts in our own words, with
  short quotes. Nothing adapted.

## 2026-11-11 — `coding`'s `code-style`, `types`, `input-handling`, `configuration` and `config-formats`

- **Asked, by the owner:** "finish what you can ... and anything else in the repo but partially
  complete, to a fully complete stage" (2026-11-11). The five were planned, with research run
  on 2026-09-23 (R03, R04) and 2026-10-26 (R15), and never built.
- **Built:** one helper agent per module, reviewed here. The research is weeks old and mostly
  unchecked, so every fact was fetched again on 2026-11-11; R04 held almost nothing on
  configuration, and R15 one TOML item, so those two rest on primary sources found today.
  Corrections found: Google's TODO format is now `TODO(link)`; Python 3.15's `tomllib` reads
  TOML 1.1; Python's XML docs no longer recommend defusedxml, though OWASP's cheat sheet does.
- **Lesson taken in:** L52 (`input-handling`).
- **Raised for the owner:** the standard's dimension 7 has secrets reach code through
  environment variables only, while systemd and OWASP say environment variables don't suit
  secrets. `configuration` follows the standard and says a project choosing credential files
  records that choice. A proposed change to the standard would settle it.
- **Sources:** language and tool documentation, OWASP cheat sheets (CC BY-SA 4.0: brief
  quotes, our own words otherwise), Unicode UAX 15, MITRE's CWE, the twelve-factor app, YAML,
  TOML and JSON specifications, and Google's style guides. Nothing adapted.

## 2026-11-11 — `house-style`'s `documentation`

- **Asked, by the owner:** "finish what you can, then give me followup research reports to do
  to finish them" (2026-11-11). The module had waited since R02 ran on 2026-09-23.
- **Built:** `documentation`, by one helper agent, reviewed here. R02 is seven weeks old, so
  every fact was fetched again on 2026-11-11 and only what its source still says was used.
  Corrections to R02: Material for MkDocs now has a fixed end of life, 2027-05-05; Mermaid,
  Sphinx and Zensical have moved on.
- **Lessons taken in:** L29, L40, L44 and L48.
- **Sources:** Diátaxis, GitHub Docs (CC BY 4.0), Mermaid, MkDocs, Material, Zensical, Sphinx,
  Docusaurus, the Python and Rust documentation, and Django's contributing guide. Facts in our
  own words, with short quotes. Nothing adapted.

## 2026-11-11 — `testing`, its first three modules

- **Asked, by the owner:** "lets make the testing-patterns and review-loops skills next"
  (2026-11-10), then "finish what you can" (2026-11-11).
- **Built:** the skill `testing`, with `test-gates` (proving a test, gate, checker or grader
  can fail), `test-oracles` (what a result is checked against, scoring by the worst case) and
  `flaky-tests`. Each module was written by one helper agent from R06's checked claims
  (`research/runs/2026-11-10-R06-testing.md`) and the roadmap's lessons, and reviewed here:
  the Audit tables' status words were corrected to the standard's.
- **Lessons taken in:** L1, L5 to L10, L31 and L56 (`test-gates`); L2, L12, L14, L15, L41,
  L42, L47 and L50 (`test-oracles`); L13 and L32 (`flaky-tests`). They stay listed, marked
  with the module that took them, so their numbers resolve. L11 waits for R06b.
- **Moved:** `ci-workflows`' *Prove a gate works* cases to `test-gates`, which drops
  `ci-workflows` from 15,387 to about 14,350 characters, under the 15,000 target.
- **Sources:** Google's mutation-testing papers (arXiv's licence, and the authors'
  copyright), Google's, Microsoft's and GitHub's published flaky-test practice, and Claude
  Code's plugin-evals documentation (Anthropic's, restricted). Facts in our own words, with
  short quotes. Nothing adapted under another licence.
- **Not yet:** `testing-patterns` (strategy, doubles, fixtures, coverage, property-based and
  mutation tools, each language's frameworks, hardware acceptance runs and fault injection)
  waits for R06b. The old claude.ai skill `testing-patterns` stays until it ships, since it
  still covers those; two synced skills, `go-coding` and `ruby-coding`, name it.

## 2026-11-11 — `agent-engineering`'s `skill-builder`

- **Asked, by the owner:** "finish what you can ... to a fully complete stage" (2026-11-11).
  Planned since the skill-authoring research of 2026-09-23, marked "done" on the roadmap.
- **Built:** by one helper agent, reviewed here, from the Agent Skills specification,
  Anthropic's skill documentation, Claude Code's plugin-evals page, and this repository's own
  process (`docs/authoring-a-skill.md`, `skillcheck`), every fact fetched on 2026-11-11.
- **Found:** Anthropic's skills README now says its document skills are Apache-2.0 too.
  AGENTS.md's rule against taking anything from them stands; whether its reason still holds
  is the owner's question.
- **Sources:** agentskills.io, Anthropic's documentation (restricted: facts in our own words),
  and Anthropic's skill-creator (Apache-2.0, a reference only: nothing copied).

## 2026-11-11 — `agent-engineering`'s `agent-context-files` and `ai-agent-security`

- **Asked, by the owner:** "finish what you can ... and anything else in the repo but partially
  complete, to a fully complete stage" (2026-11-11). Both were planned, with R01 run on
  2026-09-23, and never built.
- **Built:** one helper agent per module, reviewed here. Claude Code and MCP change fast and
  R01 is seven weeks old, so every fact was fetched again on 2026-11-11, with check-by dates
  three months out for Claude Code's.
- **Lessons taken in:** L39 and L57 (`agent-context-files`), L53 (`ai-agent-security`). L53
  recurred while the module was written: a tool turned an escape for U+202E into the
  character itself, twice, and `skillcheck` would have failed it.
- **Found for a follow-up:** `skillcheck`'s hidden-character scan leaves out variation
  selectors, which OWASP's 2026 list names as a way to hide instructions.
- **Sources:** Claude Code's documentation (Anthropic's, restricted: facts in our own words),
  OWASP (CC BY-SA 4.0: brief quotes), Simon Willison and Meta on the trifecta and the rule of
  two, the MCP specification, GitHub's, Cursor's and Gemini's documentation, and the Trojan
  Source paper. Nothing adapted.

## 2026-11-11 — `agent-engineering`, with `review-loops`

- **Asked, by the owner:** "start on the skeleton of the review-loop too, this is important"
  (2026-10-21), "lets make the testing-patterns and review-loops skills next" (2026-11-10),
  and "finish what you can" (2026-11-11).
- **Built:** the skill `agent-engineering`, with its first module, `review-loops`, from draft
  #73's skeleton, eleven of the roadmap's lessons (L26, L28, L30, L35 to L38, L45, L46, L54,
  L55) and R26's checked claims (`research/runs/2026-11-10-R26-review-loops.md`). One helper
  agent finished the module; it was reviewed here.
- **R26 changed the draft:** a round closes on evidence, not agreement, since voting explains
  most of debate's gains and agents talk each other out of right answers; turn and stop rules
  stay, since MAST counts inter-agent misalignment and unawareness of termination among the
  failures; and the turn is held by a compare-and-set, a push that lands only if the branch
  hasn't moved, with the turn number as a fencing token. That revises proposal D, still the
  owner's to answer for the standard: a convention alone orders crossings but prevents none.
- **Sources:** arXiv papers under CC BY 4.0 and CC BY-NC-ND 4.0 (quoted, never adapted),
  Anthropic's and GitHub's documentation, Google's review guide, Kleppmann, Git's manual, Pact
  and oasdiff. Facts in our own words, with short quotes. Nothing adapted.
- **Draft #73:** its `review-loops` part is superseded by this; its `supply-chain-security`
  draft stays open there until R24 is run.

## 2026-11-11 — `user-experience`, with four modules

- **Asked, by the owner:** "what about a gui review and a gui end user use and a gui ease of
  use type skill ... make sure things like windows dont start before they should or hide
  things, or give you options in many places, or behind 20 options choices" (2026-11-10), then
  "finish what you can" (2026-11-11). Planned in the decision of 2026-11-10 below.
- **Built:** `usability-review`, `windows-and-dialogs`, `settings-and-options` and
  `gui-testing`, one helper agent each, from R27's checked claims
  (`research/runs/2026-11-10-R27-user-experience.md`) and the evidence from an audited desktop
  application named in that decision. Reviewed here; two Audit tables' status words were
  corrected to the standard's.
- **What R27 changed:** choice overload is conditional, so the modules never cut a useful
  option to shorten a list, which suits the owner's power-user programs; Apple no longer
  forbids a modal on a modal; undo beats a confirmation; the platforms, not the toolkits, set
  the guidelines; GTK 4 is driven through AT-SPI.
- **This repository's own practice, said so where used,** since no primary source states them:
  one place per setting, nothing shown before it's ready, and no verdict word over a failure.
- **Sources:** NN/g and Apple (all rights reserved), KDE (CC BY-SA 4.0), GNOME (licence not
  stated on its pages), Microsoft Learn, Qt (GFDL), GTK (LGPL), the choice-overload papers, and
  each test tool's registry. Facts in our own words, with short quotes. Nothing adapted.
- **Merged by the owner,** because `.claude/settings.json` turns off the new skill's installed
  copy here.

## 2026-11-11 — `security` and `architecture`, each with its first module

- **Asked, by the owner:** "finish what you can, then give me followup research reports to do
  to finish them, and anything else in the repo but partially complete, to a fully complete
  stage" (2026-11-11). Both skills were planned, with research run on 2026-09-23 (R04, R02).
- **Built:** `security` with `secure-coding`, and `architecture` with `repo-structure`, one
  helper agent per module, reviewed here. The research is seven weeks old, so every fact was
  fetched again on 2026-11-11; the editions cited are OWASP Top 10:2025, ASVS 5.0.0 and the
  2025 CWE Top 25.
- **Not yet:** `security`'s `supply-chain-security` waits for R24, and its draft stays on #73;
  `privacy-and-compliance` for R18. `architecture`'s `api-patterns` and
  `architecture-and-design` wait for R19, and `legacy-modernization` for R17.
- **Sources:** OWASP (Top 10 pages CC BY 3.0; cheat sheets and ASVS CC BY-SA 4.0: brief
  quotes, our own words otherwise), MITRE's CWE, NIST SP 800-63B-4, the Python, Go, Node,
  .NET, Rust and Git documentation, and Google's engineering book. Nothing adapted.
- **Merged by the owner,** because `.claude/settings.json` turns off the new skills' installed
  copies here.

## 2026-11-10 — `user-experience` planned, and research for it and `review-loops`

- **Asked, by the owner:** "lets make the testing-patterns and review-loops skills next ... what
  about a gui review and a gui end user use and a gui ease of use type skill ... make sure
  things like windows dont start before they should or hide things, or give you options in many
  places, or behind 20 options choices" (2026-11-10).
- **Planned:** a new skill, `user-experience`, since how a program behaves for its user is a
  kind of situation no skill covers: `visual-design` is how it looks, `human-factors` what people
  do. Four modules: `usability-review`, `windows-and-dialogs`, `settings-and-options` and
  `gui-testing`. `accessibility` stays in `visual-design`, and the new skill points to it.
- **Research:** R26 for `review-loops`, which rested on one loop's records alone, and R27 for
  `user-experience`, in R06's form. The owner runs R06, R26 and R27; each result is checked
  before a rule rests on it.
- **Evidence already in hand for `user-experience`, from an audited GUI application:** a status
  line that kept the last rip's result through the next rip; a drive shown after it was gone; a
  hidden modal dialog left behind by each update offer; a picker that opened by itself under the
  next dialog; and a console with two file pickers of different meaning.

## 2026-11-10 — R06, the testing research, asks what the audits found

- **Asked, by the owner:** "all existing and new repos/claude outputs/scripts/code should benefit
  form everything here" (2026-11-10). Twenty of `ROADMAP.md`'s 57 lessons wait for `testing`,
  more than for any other skill, and R06, its research prompt, predates them.
- **Changed:** R06 is version 3. Seven priority questions come from the audits: checks that
  can't fail, independent test oracles, scoring the worst case, finding what's missing,
  acceptance runs on hardware, fault injection, and tests that agents write. Its date and the
  standard's version are current.
- **Next:** the owner runs R06 on claude.ai; the result is checked against its sources; then
  `testing` is built from it and the lessons, and `ci-workflows`' gate cases move there.

## 2026-11-10 — What the two repositories' week taught `git-workflows`

- **Asked, by the owner:** "loook at both repos, see if anything shoulld be done here and
  improve accordingly" (2026-11-10). A read-only review of both repositories' week, from
  2026-11-03 to 2026-11-10, its claims checked before use.
- **`pr-stewardship`:** a lifted hold replaces the hold where it's recorded, since one
  repository's release hold grows a sentence per release; a new rule names who tends bots' pull
  requests, since one repository's update sat red for a week; four mistakes (a head commit
  typed by hand, a file left untracked through the last run, a wait loop parsing printed
  output, an untended bot pull request); an audit row; a Why section. 13,020 to 14,848
  characters.
- **`releases-and-versions`:** check what consumers install, with one planted wrong checksum
  digit; and read what a failed publish made before retrying it, since one release took three
  tries to create. 15,005 to 15,339 characters.
- **`ROADMAP.md`:** lessons L55 to L57, on laps crossing despite per-side numbers, four more ways
  a gate passed its defect, and parallel agents colliding on one record. L56 waits on splitting
  `ci-workflows`, which is too near its limit to take them.
- **Not taken here:** the standard's round rules against practice, and turn-taking in its
  *Other repositories*, go to the owner as a proposal; `skillcheck` for a repository's own
  `.claude/skills/` is planned in `ROADMAP.md`'s infrastructure rows.
- **Review:** the checks of `docs/authoring-a-skill.md` that apply to added rules and mistakes
  passed. The claude.ai tries follow the merge.

## 2026-11-03 — Three `skillcheck` bugs: worktrees, unresolved files, ISO offsets

- **Found:** the same night, by this session and the mutation run.
  - **Agents' worktrees were scanned.** Claude Code keeps an agent's isolated copy under
    `.claude/worktrees/`, and the hidden-character, conflict-marker, `times` and content scans
    read `.claude`, so the main checkout reported 20 findings that were another checkout's.
    `core/paths.py` now leaves that folder out, relative to the repository's root, so a
    repository that itself sits inside a worktree still scans its own files.
  - **The dependency map counted an unresolved file once per side.** `git ls-files` lists a
    conflicted file three times, so a map regenerated before `git add` was wrong, and CI
    refused it on #113. Each listed name now counts once.
  - **`times` flagged an ISO offset,** the `02:00` of `2026-10-17T02:55+02:00`, as a time with
    no zone, against its own docstring. A time just after a digit and a sign is now skipped.
- **Tests:** 12, each planting the defect; each fails on the code before the fix.
  `.test-baseline` moves from 634 to 646.
- **Asked, by the owner:** "Do all you recommend" (2026-11-03).

## 2026-11-03 — `ci-speed` times a release's run too

- **Why:** standard v0.49.0's dimension 6 asks an audit to record how long a pull request's CI
  and a release's tests take, by `ci-speed`, and the module named only the first. Found while
  applying the standard, under the owner's "Do all you recommend" of 2026-11-03.
- **Changed:** rule 3 measures a release's run as well as a pull request's, and the audit gains
  "How long CI takes isn't known". The module goes from 14,927 to 15,193 characters.
- **Review:** the checks of `docs/authoring-a-skill.md` that apply to a widened rule and one
  audit row passed. The claude.ai tries follow the merge.

## 2026-11-03 — Mutation tests of `core/times.py` and `core/text.py`

- **Asked, by the owner:** "Do all you recommend", after a review found an audited repository's
  graders could not fail. Full line coverage shows a line ran, not that a test fails when the
  line is wrong, so the two modules whose job is to fail bad input were mutated: the `times`
  check, and `HIDDEN` and `CONTROL`, which the `unicode` check and `printable` use.
- **Tool:** mutmut 3.8.1, run with `uv run --with mutmut` in a scratch copy, whose
  `pyproject.toml` alone carried its settings. Each mutant faced `tests/test_times.py` and
  `tests/test_text.py`. mutmut mutates function bodies only, so a second set of 51 hand-written
  mutants changed the module-level patterns: each run of `HIDDEN` and `CONTROL` dropped or
  narrowed at one end, and each part of the `times` patterns, `SINCE`, `ROOTS` and `EXCLUDED`.
  Each faced its module's tests, then the whole suite if it lived.
- **Before:** mutmut made 112 mutants, killed 105 and missed 7; the hand set killed 24 of 51.
  The real gaps: `stamp` taking the machine's zone for UTC; a fence's closing line ending the
  scan; nine ends of `HIDDEN`'s runs (U+00AD, U+180E, U+202A, U+2060 to U+2064, U+2069, U+E0000,
  U+E007F); five ends of `CONTROL` (U+0000 to U+0008, U+007F, U+009F); the look-behind's dot,
  colon and word character; seconds; morning local times; a local time with no zone name; tilde
  and indented fences; four of the five roots.
- **Tests added,** 24, in `tests/test_times.py` and `tests/test_text.py`, which plant each
  defect. `.test-baseline` moves from 610 to 634.
- **After:** mutmut killed 107 of 112, and the hand set 50 of 51. The six left change nothing
  that matters: `lstrip("XX0XX")` on digits; `encoding=None`, UTF-8 under Python 3.15's UTF-8
  mode; `"UTF-8"` for `"utf-8"`; `fenced = None`, as falsy as `False`; dropping `\b` after `UTC`
  or `GMT`, which differs only for a word that starts with either; and replacing a code span
  with `XXXX`, not nothing, which differs only where a span touches a time or its zone.
- **Time:** about 35 minutes in all. mutmut took 37 seconds a run, the hand set 805 seconds
  before the tests and 86 after.
- **Found, not fixed:** the `times` check reads an ISO 8601 offset, the `02:00` in
  `2026-10-17T02:55+02:00`, as a time with no zone, though the module says ISO 8601 times are
  left alone. No file here holds one. Changing the check is a separate change, and it waits on
  the owner's word.

## 2026-11-03 — Standard v0.49.0: what a repository keeps, CI time, steward files and six fixes

- **Asked, by the owner,** at about 07:40 UTC: "Do all you recommend", told that the
  recommendations included both pending standard proposals. That approves the proposal of
  2026-11-03, A, B and C, with A's three defaults standing, and items 1 to 6 of the proposal
  from the audits of 2026-10-27, as proposed.
- **Changed, in the standard, as F156 to F164 and a change of its own:**
  - **F156:** Phase 3, *An unattended run told not to wait, and given no answers*, with `none,
    defaults applied` and `tier_basis: draft` in its block; `SKILL.md`'s third step points to
    it.
  - **F157:** *Every run produces exactly one file* follows a request naming the report's files,
    form or place, and records the difference in `overrides`.
  - **F158:** Phase 2 gives the `curl` form without `gh`, and *Platform capability* gains a fact,
    checked against GitHub's REST reference on 2026-11-03: a public repository's repository,
    `rulesets`, `rules/branches/<branch>` and `private-vulnerability-reporting` paths answer with
    no token; `immutable-releases` and `code-scanning/default-setup` don't. It matches
    `git-workflows`' fact `rest-public`.
  - **F159:** dimension 8 reads zizmor's `dependabot-cooldown` finding against the default, and
    the cooldown fact quotes GitHub's *Dependabot options reference*, read again on 2026-11-03.
    `git-workflows`' `action-pinning` already carries the matching note, so it's unchanged.
  - **F160:** the `skillOverrides` fact records that a bare-name key matches a synced skill.
  - **F161:** *What not to create* and dimension 3 rate a plan file left after merge.
  - **F162, proposal A:** dimension 10's four questions, auxiliary branch, defaults and ratings.
    *Merge, delete, leave alone* moves a finished record worth keeping rather than deleting it,
    and the evidence-branch ruleset row covers any auxiliary branch, so the standard doesn't
    contradict itself.
  - **F163, proposal B:** dimension 6 rates CI and release test time by `ci-speed`, and the
    starter CI gains a `concurrency` block and a cached setup step.
  - **F164, proposal C:** dimension 6's *Pull requests that agent sessions drive*, with a row in
    *The configuration file map* and a dated fact for the steward path.
- **Planned, not applied:** item 7, splitting *The run* by dimension, is F165 in `ROADMAP.md`,
  with the rebuild.
- **Left out:** the borderline Python 3.11 item, which wasn't recommended.
- **Not done here:** A's bullet for this repository. The audit kit stays out of this public
  repository, since it names audited repositories, and `AGENTS.md` is changed separately.
- **Found, not fixed:** `ci-speed` covers a pull request's CI and the default branch's run, and
  says nothing of a release's tests. The standard asks for both; the module's gap is a change of
  its own.
- **Not done:** no parity run. No sample holds a plan file, an archive, an auxiliary branch or a
  steward, and every sample's Phase 3 replies are given. The new ratings any sample could meet,
  such as dimension 10's `GAP` for no recorded answer, land on dimensions its baseline already
  rates `GAP` or worse, so no status can move.

## 2026-11-03 — An `archive` branch, and this repository's answer on records

- **The owner's word:** "Do all you recommend" (2026-11-03), which took up the standard proposal
  of 2026-11-03, item A, with its three defaults. The standard's own change lands on its own,
  as v0.49.0; this entry is the repository's part.
- **Built:** an orphan `archive` branch with a README; `docs/archive.md`, answering the four
  questions and indexing the branch; and `AGENTS.md`'s split line, which moved finished work by
  deleting it, now moves it to `archive`.
- **The deliberate difference:** the proposal said the audit kit moves here from
  `audit-reports`' `audit-log` branch. It doesn't: the kit and the messages to other
  repositories name audited repositories, which this public repository can't hold. They stay
  private, and `docs/archive.md` says so.
- **Homes considered for the index:** `AGENTS.md`, over its line budget, and the decision
  record, which is a log rather than an index. `docs/` holds the repository's other records.
- **Left to the owner:** a ruleset protecting `archive` from force-pushes and deletion, as the
  rule asks; a session can't set one.

## 2026-11-03 — `ci-workflows`: a gate passing a check that ran and failed

- **Asked, by the owner:** "Do all you recommend" (2026-11-03), after this session recommended
  teaching the 2026-11-03 Full run's main lesson: a green run whose graders couldn't fail.
- **What it found:** an audited repository's acceptance step counted a post-rip check as done
  when it had run, whatever it found, so a failed integrity check passed. Rule 5 already said to
  prove a gate against the state it exists to catch; nothing named this case, and no audit row
  checked the rule at all.
- **Changed:** *Prove a gate works* gains "a check that ran and failed", and the audit gains "A
  gate has never been seen to fail". The module goes from 14,990 to 15,387 characters, over the
  15,000 target and under the 16,000 limit; the next addition here splits it first.
- **Review:** `docs/authoring-a-skill.md`'s checks that apply to a rule's case and an audit row
  (size, prose, wrap, the row's status words) passed. The claude.ai tries follow the merge.

## 2026-11-03 — The steward template moves out of `pr-stewardship`

- **Why:** the module stood at 15,998 characters, two short of the 16,000 limit past which
  claude.ai drops a module's middle. The round 37 review will add to it, so it needed room first.
- **What moved:** the skeleton steward file, word for word, to
  `skills/git-workflows/assets/steward/SKILL.md.template`. The module links it and names its
  sections, and now stands at 13,020 characters. The `.template` suffix keeps any loader from
  taking it for a skill of its own.
- **Homes considered:** a new module, which a template isn't, and `assets/`, where the skill's
  other files to copy already live, chosen.
- **Review:** a move with no change of meaning; `docs/authoring-a-skill.md`'s checks that apply
  to it (size, links, prose, the audit rows naming the template) passed. No claude.ai tries are
  needed, since no rule changed.

## 2026-11-03 — #107 and #108 merged on the owner's word

- **The owner's word:** "do everything you can, merge all you can, remove any uneeded branches".
  #107 and #108 change `.claude/` and the workflows, which the steward leaves to the owner, so a
  session merged them on that word, given in the conversation, as the steward's rule 6 allows.
  #107 merged first under the setting's own title, and #108, stacked on it, was moved to `main`
  and merged after.
- **Branches:** the merged branches were already gone, deleted by the setting on merge. #96 to
  #99, superseded by #108, were closed with a note; three of their branches were deleted. The
  fourth, which changes a workflow, refused deletion from a session, and is Dependabot's or the
  owner's to delete. Draft #73's branch stays, by the steward.
- **Left to the owner:** adding `subjects` and `hold` to the ruleset's required checks.

## 2026-11-03 — This repository's steward skill, and a live hold

- **Asked, by the owner:** "this repo should get the most comprehensive steward file of anyone",
  then "do everything you need to" on four recommendations, taken as approved:
  1. the owner merges any pull request that changes `.claude/`, `AGENTS.md`, `CLAUDE.md`, a
     workflow or a ruleset, and sessions merge the rest as before;
  2. a live hold: a `hold` label, and a `hold` check that fails while it's on;
  3. `subjects` and `hold` become required checks, which the owner adds to the ruleset;
  4. no pull-request rule in the ruleset; every change landing by pull request holds by conduct.
- **Built:** `.claude/skills/steward/SKILL.md`, written against `pr-stewardship`, and
  `.github/workflows/hold.yml`, which reads the labels through the API when it runs. `AGENTS.md`
  and `CLAUDE.md` name the steward. The workflow test allows the one workflow that uses no
  action. `.test-baseline` moves from 609 to 610. The `hold` label was created the same day.
- **Reviewed:** a cold reader found four high problems, all fixed:
  - a plain-text filler word that would have failed `prose`;
  - a re-run that would lift a hold, because a re-run reuses its event's labels, so the check
    now reads them live;
  - auto-merge, which ignores checks the ruleset doesn't require;
  - a Dependabot batch touching workflows, now the owner's to merge.

  Twelve medium and low points were fixed too.
- **A slip found:** 39 merges on `main` carry the title "Merge pull request #N from …", among
  them each merge this session made, passing it itself, while the setting names a merge by the
  pull request's title and number. The steward now leaves the title to the setting.
- **This pull request is the owner's to merge,** by its own first rule.

## 2026-11-03 — Lockfiles are generally available; `releases-and-versions`' routing, diagnosed

- **Lockfiles:** the weekly check's quote for fact `actions-lockfile` was gone because GitHub made
  workflow dependency lockfiles generally available on 2026-10-28, on Free plans too. The
  module's rule kept SHA pins "until it's generally available", so it now offers a lockfile or
  SHA pins. GitHub's own words: for an onboarded workflow, "SHA pinning within workflow files is
  no longer necessary". This repository and the ones it audits pin by SHA today; whether each
  moves to a lockfile is a consistency question for the next audit, not part of this change.
- **`releases-and-versions`' routing:** its trigger requests reach `git-workflows` but not the
  module, on `main` as on any rewording of its router row. The skill's own rule 7 answers the
  commonest release question itself, so the model has no reason to read on. How much a skill's
  top-level rules should say is a design question, left open.
- **`pr-stewardship` agrees with the standard on `CODEOWNERS`:** only with more than one
  reviewer, as dimension 3 says. The module is now 15,998 characters; its next addition splits
  it.

## 2026-11-03 — `pr-stewardship` on claude.ai: both tries pass, and a limit found

- **Tried, by the owner, on claude.ai:** the steward request loaded `git-workflows` and read
  `pr-stewardship` first, a pass. The merge-strategy near miss answered from
  `branches-and-merging` without reading `pr-stewardship`, a pass.
- **A limit the first try found:** on a one-person account, GitHub can't enforce "the owner merges
  changes to the steward file". A session's merge carries the owner's name, and an author can't
  approve their own pull request. Rule 7 now says so: there the rule holds by the session's
  conduct, and the file says so. The audit rates it `MIRROR` there. To fit, the module's scope
  paragraph and two passages were cut, and its drift mistake folded into rule 8.
- **Also found:** this repository has no steward skill of its own, though its sessions merge
  their own pull requests. Writing one against the framework is due before the next release.

## 2026-11-03 — `pr-stewardship`: the framework for each repository's steward skill

- **Asked, by the owner:** each repository that agent sessions drive should write and own a
  steward skill, and "the skill checker should give a framework for you", thoroughly, in this
  release if it can be.
- **Built:** a `git-workflows` module, from the auto-fix and project-skill pages of Claude Code's
  docs, GitHub's re-run and auto-merge pages, one public babysit skill (MIT) as what others do,
  and what the first audit cycle showed: a hold that arrived after a merge, a one-platform
  "green", a stall cancelled by hand four times. It gives the rules, a skeleton `SKILL.md` to
  copy and the audit's checks; each repository writes its own file.
- **One claim is marked, not sourced:** that cloud sessions driving a pull request read
  `.claude/skills/steward/SKILL.md`, or `babysit/`, comes from a session's own instructions on
  2026-11-03. Claude Code's public docs name neither path, so the module says so and the audit
  checks it.
- **Reviewed:** a cold reader found four high problems, all fixed. Holds written only in the
  committed file arrive as late as a message, so holds now live where a session reads them live.
  Auto-merge passes a hold GitHub can't see. The file could authorize its own change, so the
  owner now merges changes to it. Re-runs aren't unlimited: GitHub allows 50, on the same commit.
  Eight medium and three low were fixed too, among them conflicts, drafts, Dependabot, security
  findings and when to stop.
- **Triggers:** the module's 12 requests all routed. The skill's description now names the
  agents that tend pull requests, kept at 248 characters. `releases-and-versions` misses 3 or 4
  of its 7 requests on `main` and on this branch alike: the skill loads but the module isn't
  read. That's a follow-up of its own.
- **Size:** 15,698 characters, under the limit and over the 15,000 target, most of it the
  skeleton.

## 2026-10-29 — What stays on the main branch, and what lives elsewhere

- **Said, by the owner:** "you have to keep on the main what needs to be kept. what everyone else
  expects from a new release, what you expect to read, what you need to have, what other repos
  expect to see, what users and end users expct to read about. but records, archives, logs from
  old builds, things like this, these can live elsewhere"
- **The line for the proposal:** the main branch holds what a new release is expected to carry:
  what users and end users read, what developers and agents work from, and what partner
  repositories read from it. Records, archives and old builds' logs live on the auxiliary branch,
  as the entry below says.

## 2026-10-29 — What the archive rule asks each repository to decide

- **Said, by the owner:** what a repository keeps can differ: "in one repo it might make sense to
  record a ton of logs, and other files plus the evidence files, in another the evidence file
  might be enough", and "it should be intentional and look at what is needed for record, what
  might be wanted for an external audit by other reviewers (if public especially, but even
  private)", while keeping such material out of the main branches. And the partners: "many of
  these are needed to handshake or communicate to other repos. so its no just a 1 repo ideal.
  its better to offload off the main branch to an auxiliary branch what is not needed there, but
  keep more than you think in case someone else might use it".
- **For the proposal:** every repository answers the same four questions and writes the answers
  down with their reasons, where a reader finds them:
  - What does its own record need to keep: evidence, logs, laps, old READMEs and changelogs?
  - What would an outside reviewer want to see?
  - What does a partner repository need from it, such as the laps, contracts and run evidence a
    handshake reads?
  - What is worth keeping but doesn't belong in the main branch, such as communications, raw
    logs, run output or finished plans?
- **The same everywhere:** the answers are recorded and obvious, and whatever is kept is tagged by
  version, release or date, on an auxiliary branch rather than the main one. When in doubt, keep
  it: more than seems needed, in case another repository or reviewer uses it. The answers
  themselves may differ.
- **Not pared to nothing:** the owner, the same day: "you have to keep in your branch what you and
  the user and dev need. you cant just pair it down to nothing. keep what is needed, extra can go
  to the other branch, that can always be pruned as needed later." The main branch keeps what its
  users, developers and agents work from. Only the extra moves to the auxiliary branch, which can
  be pruned later.

## 2026-10-29 — The archive rule asks for consistency, not sameness

- **Clarified, by the owner:** "i did not say to do it all the same way, just that we need to be
  consistent. and if we have a reason to do otherwise, it should be noted and obvious." And: "i
  would love it all to be exactly the same, but i realize it might not need to be, or should be."
- **Changes the entry below:** the rule is one consistent way of keeping finished work, identical
  where that serves. An archive branch is a candidate form, not a requirement. A repository that
  differs records why, where a reader of that repository sees it. `ROADMAP.md`'s row now says so.

## 2026-10-29 — One archive rule for every repository, before the next release

- **Asked, by the owner:** "everyone, including you, should do this all the same way. if here
  is a reason to do it otherwise, it should be compelling, and documented." Work that is
  finished but worth keeping goes on an archive branch, tagged by version, release or date.
- **Now:** nothing changes. Each repository keeps such work differently: in the main branch, in
  history only, or in an `evidence` branch for rip runs. This session's audit kit is in ignored
  `scratch/`.
- **Next:** before the next skills release, the rule is proposed to the standard for the
  owner's approval. Then this repository, the audit kit and the audited repositories are
  brought into line, each exception recorded with its reason. `ROADMAP.md` tracks it under
  *Repository*.

## 2026-10-27 — The C modules take in their first audit

- **Asked, by the owner:** a C-only audit of a repository already audited, before its review
  was sent, to test the new C modules as much as the code. Its feedback names neither the
  repository nor its code.
- **Taken in:** 12 feedback items, each checked first: the two compiler claims were tried with
  GCC 13.3 and Clang 18.1, and the three new facts confirmed at their sources by
  `skillcheck --verify`. One item isn't the modules' text: the session's installed copy predated
  them, because installed copies come from a release. The next release carries them.
- **What the audit missed:** an answer key written before the run held four problems it didn't
  report: a library's struct copied from an object that then frees it, an append past a fixed
  array after a capped loop, a flush's status replacing a write's error, and a fixed-length
  scheme comparison. An independent check confirmed all four. The first three now have words
  in their rows; the audit checked the shallow-copy row in one file only. The fourth is a logic
  error no C module should own.
- **Reviewed:** a cold reader found two high problems, both fixed: a claim that four
  `-Werror=` flags never grow, false under Clang, and mapping a value's `/` after the template
  was filled, when it can no longer be told from the template's own. Six medium and five low
  were fixed too.
- **Size:** c-security's fact summaries were shortened to fit. The three modules end between
  15,800 and 15,950 characters, under the limit and over the 15,000 target. The next C
  coverage, threads and signals, is a fourth module, not more here.

## 2026-10-27 — C in the `coding` skill: `c-coding`, `c-build` and `c-security`

- **Asked, by the owner:** after the first audit of a C program found no C module to judge it
  by, to run research R12 and build C: "give me the r12 and i will run it and give to you, then
  build".
- **Done:** three modules, not the two planned, since one C module and one for security couldn't
  hold the build and its checks within the 15,000-character target with their facts: `c-coding`
  (the language and the code), `c-build` (Meson, the warning gate, hardening, sanitizers,
  analyzers, fuzzing) and `c-security` (outside data). One writer each, from R12 as leads, every
  fact checked at its primary source (51 of them), every C example compiled by the example
  checker and built and run besides, every Meson example run with Meson 1.12.1 and its declared
  floor. R12's verification table records what was verified, contradicted and unverifiable.
- **Added in passing:** `skillcheck --examples` compiles `c` blocks with Clang, warnings as
  errors, never linking or running them, at C17 unless the fence names another standard.
- **Reviewed:** a cold reader with C experience attacked every example (boundary sizes,
  hostile file names, integer extremes, signals, under ASan and UBSan) and checked about 40 fact
  quotes at their sources. It found one high problem, a scan-build check that exits 0 with bugs
  found, seven medium (among them a file-writing example that destroyed the old file on a full
  disk, a `posix_spawn` example that lost its error, sanitizers credited with finding
  uninitialized reads, an example laid out against the standard, and missing number parsing
  and secret wiping) and eight low. Each went back to its writer and was fixed; the reader then
  re-checked them all fixed. The fixes added five small problems, fixed in this change: a test
  that can't probe now fails unless another job runs it, as the contract says; a buffer of zero
  capacity is no longer written on failure (run under both sanitizers); the versioned
  `scan-build-NN` name; the fuzzer's path; and `fchmod` before replacing a file.
- **Approved, by the owner, for the contract:** rule 8's whole-directory ignore, as merged in
  #92 ("well then, merge it"), after the difference was put to them with an example.
- **Next:** a C-only audit of the program that showed the gap, as the real test of the three.

## 2026-10-27 — Three skills take in what the first audits found wrong in them

- **Asked, by the owner:** to audit two repositories that use these skills, "as an audit of sorts
  for both us and them". Each audit wrote feedback on the skills alone, naming neither
  repository.
- **Taken in:** about 35 items across `coding`, `git-workflows` and `house-style`, one writer per
  skill, each claim checked first; changes to the standard went to the owner as a proposal
  instead. Two claims were partly wrong and were corrected rather than taken as written:
  - Ruff's `PLW1514` finds nothing unless preview is on;
  - `cd ""` succeeds only before Bash 5.3.
- **A rule loosened, and bounded:** `coding`'s contract rule 8 allows a whole-directory ignore,
  but only for a rule that flags calls even when they're safe, such as `S607`, where no outside
  input reaches, with a dated comment; the rules that catch a shell, `eval` or unsafe
  deserialization stay on. Other loosened rules are bounded the same way:
  - deletes graded by risk;
  - leaving out `-e` in two named cases;
  - an untagged release only where a pinned manifest names it.
- **A check added in passing:** this repository's own Vale setting let a quote run on past a
  blank line, and had hidden a heading that broke the style. It's gone; the skill's shipped
  default covers quotes, and its limits are written down.
- **Reviewed:** a cold reader checked the whole branch and found 11 problems and two small ones:
  - four high: the loosened rules were too loose, and two modules contradicted each other;
  - five medium, including a quote pattern that still hid text and a fact that didn't support
    its claim;
  - the rest low.

  Each went back to its writer and was fixed. The reader then re-checked every one: all fixed,
  with two documented limits left in the quote pattern. The fixes introduced three small errors,
  fixed in this change: a dropped condition on git's quoting, `errors="replace"` offered without
  an encoding, and the wrap check misreading Windows line endings, now with a test.
- **Size:** two `house-style` modules end just under the 16,000-character limit, at 15,996 and
  15,925. Splitting one is the next change to that skill.

## 2026-10-26 — Audit reports go to a private repository, not by attachment

Supersedes the last two points of "How a repository that uses these skills is audited", below.

- **Asked, by the owner:** not to carry the report files ("i will not download both files"), and
  that checking which skills loaded is this session's job, not theirs.
- **Decided:** the owner made a private repository, `rmccann-hub/audit-reports`. An audit
  session attaches it and pushes its two files there, under `<repository>/<date>/`, and puts
  nothing in the repository it audits. This session reads them there, grades them, and checks
  each finding against the code. Its README holds the layout and the rules: add, never edit or
  delete, and no secrets.
- **Why a repository of its own:** the audited repositories are public, and a report lists
  unfixed findings, so it can't go on a branch there. This repository is public too, and names no
  repository its skills ran on. The private companion repository is for company skills, and
  these audits aren't company work.
- **Unchanged:** an audit judges the default branch's tip, reviews only, and its skill feedback
  names no repository, so for anyone else it can still come back as an issue here.

## 2026-10-26 — How a repository that uses these skills is audited

- **Asked, by the owner:** "should we make a rule, and an announcement, that an audit only
  happens on main, new release or not?", and that the feedback "must be sent via .md file or
  similar ... created in the llm, not on the repo".
- **Decided:**
  - An audit judges the tip of the repository's default branch, whether or not a release is due.
    Work on another branch waits for the next audit, since it isn't integrated, and a new session
    sees only what's pushed.
  - It runs in the audited repository itself, in a new session, never the one doing its work,
    and reviews only: no change, commit, push, release, issue or pull request.
  - It writes two files and commits neither: its findings, and feedback on the skills alone,
    with the repository's name, code and findings left out. Each goes in the repository's
    ignored working folder, or as a file to download. Findings stay with the owner until they're
    fixed, so none goes in an issue or a pull request, above all a security finding on a public
    repository.
  - The files come back by attachment. Grading against an answer key written before the audit,
    and checking each finding against the code, happen here; the audited session never sees the
    key. For anyone else, only the feedback comes back, if they choose, as an issue drafted by
    each skill's reporting section.
- **Considered:** auditing the branch that holds the next release's work. Rejected for its
  ambiguity, since mid-work that branch can change hourly. And committing reports to the audited
  repository, rejected for publishing unfixed findings.
- **Next:** the kit's generic parts (the prompt, the test bench and the grader) are committed
  once a first audit proves them, with the two files' first lines added to `AGENTS.md`'s *Files
  the owner sends*.

## 2026-10-26 — Every module fits claude.ai's file viewer, and `skillcheck` holds it there

- **Asked, by the owner:** the same "i want it", for the six modules the entry below left over
  16,000 characters.
- **Measured, by the owner:** after `coding`'s split, claude.ai read `powershell-scripts.md`, at
  14,993 characters, whole, and still cut `writing-style.md`, at 19,014, keeping 15,977. The
  limit is 16,000, as the entry below found.
- **Done:** three `git-workflows` modules split by topic, each keeping its name:
  `rebasing-and-recovery` from `branches-and-merging`, `ci-speed` from `ci-workflows`, and
  `action-pinning` from `actions-security`. `commits-and-pull-requests`,
  `releases-and-versions` and `writing-style` were trimmed: shorter wording, fact descriptions
  and quotes, with no rule, mistake, audit row, example or reason cut. `git-workflows`'
  router and the rules that cite these modules now name the new ones.
- **Reviewed:** a cold reader compared each file with its original. No safety advice was lost.
  It found ten smaller faults, all fixed: two openings pointing at the wrong module, house
  style's status words dropped, two release facts narrowed past what cites them, a quote cut past
  its condition, a garbled sentence, a new audit row missing its conditions, two rules citing too
  few modules, and two lost lines in `writing-style`.
- **Held:** `skillcheck`'s `modules` rule fails a module over 16,000 characters, and the
  authoring review aims at 15,000, leaving room for an edit. Claude Code reads files whole, but
  a module must work on both.
- **Considered:** a higher limit for Claude Code alone. Rejected, since claude.ai's plugin sync
  reads `main` and every module ships to both.

## 2026-10-26 — `coding`'s modules split to fit claude.ai's file viewer

- **Found, by the owner's test:** claude.ai's file viewer keeps about 8,000 characters from each
  end of a file over 16,000 characters, and drops the middle, with a notice such as
  `< truncated lines 40-349 >`. The model there read the limit from its own tool's description.
  A 35,500-character module lost its Mistakes, Audit and Why sections; a 19,000-character one
  lost 53 lines. Claude Code reads files whole. No public documentation states claude.ai's limit:
  Anthropic's text editor tool takes it as a setting, `max_characters`.
- **Asked, by the owner:** "i want it", to making the modules fit.
- **Done:** at 16,000, trimming alone couldn't work, since the facts tables alone ran 9,000 to
  14,000 characters. Each language module split into itself and a security module, each at most
  15,000 characters, by one writer per language, each reviewed before it was committed. Old
  names stay, so nothing that refers to them breaks. The router reads a language's security
  module too when the code takes input, runs commands or handles secrets.
- **Found while splitting:** CA2100 and CA2326 are off by default in .NET 10, even at
  `latest-Recommended`, confirmed in the SDK's rule files and by a build. The old `csharp-coding`
  implied they ran. Turning the security analyzers on is now a rule.
- **Reviewed:** a cold reader compared each pair with its original. No safety advice was lost.
  It found one gap, now fixed: the delete guards had left `bash-coding`, so the router and
  `bash-coding` now send a script that deletes or overwrites files to `bash-security`. It also
  found five compression errors, all fixed: two audit rows that lost a condition, two garbled
  sentences, and a dropped warning that `Promise.all` leaves the other work running.
- **Next:** five `git-workflows` modules and `writing-style` are also over 16,000, and a
  `skillcheck` rule will fail any module over that, in a change of their own.

## 2026-10-26 — Release 0.1.22, the `coding` skill

- **Asked, by the owner:** to build `coding` and release it, with one try in place of twelve
  (the entry below).
- **The try passed:** for "Is setting innerHTML from this API response safe, and what CSP should
  the page send?", claude.ai's steps show `coding`'s `SKILL.md` and `html-coding.md` read, and
  `javascript-coding.md` not read. The closest boundary in the skill routed correctly.
- **Seen twice now:** claude.ai read `bash-coding.md` and `html-coding.md`, each about 380
  lines, in two passes, saying the first was truncated. It recovered both times. Claude Code
  reads them whole. Trimming the modules to fit one read on claude.ai is proposed as a change
  of its own, not a condition of this release, since claude.ai already has `main`.
- **Carries:** `coding` (#82), and the documents saying a merge ships to claude.ai (#83). This
  release reaches plugin installs in Claude Code and cloud sessions; claude.ai has had it since
  the merge.

## 2026-10-26 — Merging ships to claude.ai, and the gate moves before the merge

- **Found:** the owner's claude.ai account loaded `coding` in two tries without installing
  anything, though no release carried it: 0.1.21 was cut before it existed. The account syncs
  this repository's plugins with "Sync automatically", and that sync reads `main`, not releases.
  The README, the authoring review, the roadmap and the pull request for `coding` (#82) all said
  a release was the gate. For claude.ai it wasn't.
- **Asked, by the owner:** "do option 2", of two offered: point the catalog at release tags, or
  accept that merging ships and move the checks before the merge.
- **Changed:** the README, the authoring review (steps 5 and 12), the roadmap's rebuild plan and
  `AGENTS.md` now say that a merge ships to claude.ai. Before a skill's merge: CI, a fresh
  review, the trigger tests in Claude Code, and the owner's deletion of any old copy. After it:
  the owner's claude.ai tries, with a miss fixed or the merge reverted at once. claude.ai can't
  show a skill before it's on `main` without a hand upload, which would clash with the synced
  copy. Releases still reach plugin installs in Claude Code and cloud sessions; whether a Claude
  Code install follows `main` the same way is not yet checked.
- **For `coding`, the owner's word:**
  - the six old language skills are deleted. A new session's sync on 2026-10-26 lists none of
    them among the 35 it holds;
  - one try instead of twelve ("can we do it in one?"). Try 1, a Bash review, passed: the steps
    show `coding` and `bash-coding.md` read. Another skill on the account, `code-review`, also
    loaded, and claude.ai read the 380-line module in two passes. The try chosen as the one,
    `innerHTML` and a CSP, gave an answer that follows `html-coding`; its steps, to confirm
    `javascript-coding` wasn't read, are still to come;
  - the boundary with `git-workflows` goes untested, accepted.

## 2026-10-26 — The `coding` skill, wave 1 of the rebuild

- **Asked, by the owner:** "can you build the coding skill", on 2026-10-26, which is wave 1 of
  the rebuild plan the owner approved on 2026-10-15 (decisions 44 to 49).
- **Built:** the `coding` skill, in the `engineering` plugin, with a ten-point contract every
  code change meets and six modules: `python-coding`, `javascript-coding`, `html-coding`,
  `csharp-coding`, `powershell-scripts` and `bash-coding`.
- **From:** the owner's six old language skills of those names, as topic lists only, recorded
  in the intake (`research/runs/2026-10-26-intake-wave-1.md`); research runs R09, R10, R11 and
  R15 as leads; and primary sources for every rule and fact. One module per writer, each
  checked by this session before it was committed.
- **Sources and reuse:** each module's Sources table names its sources and licenses. Nothing
  was adapted: every rule is in the module's own words, and share-alike sources (MDN prose,
  OWASP, the Python Packaging User Guide) are quoted briefly with attribution only. No
  `THIRD-PARTY-NOTICES.md` is needed.
- **Checked:**
  - all 319 facts in the repository were found at their sources;
  - Python, shell and PowerShell examples pass the example checker, with PSScriptAnalyzer on
    the PowerShell;
  - TypeScript passed `tsc --strict` and ran on Node 22;
  - the C# compiled with the .NET 10.0.403 SDK under the module's own settings. That build
    caught one example that failed CA1852, fixed. CI has no C# checker, so it doesn't repeat it.
- **The review:** a second reader, cold, on 2026-10-26, fetched 15 sources and ran examples. It
  found nine problems, all fixed:
  - **high:** Bash arithmetic, `(( ))` and `[[ -gt ]]`, runs a command hidden in input; the
    module recommended it with no warning. Reproduced, then a rule, a mistake and a blocker
    check were added;
  - **medium:** the HTML module contradicted itself on DOMPurify and `innerHTML`, and its
    example policy turned on Trusted Types that its text said to add last; the PowerShell and
    C# modules didn't warn that a batch file gets `cmd.exe` parsing whatever the argument array;
  - **low:** SQL parameters were missing from Python and JavaScript; Ruff's facts quoted a page
    about preview mode; `DllImport`'s `W` lookup needs `CharSet.Unicode`; the contract seemed to
    forbid a reasoned single-line suppression; and log and terminal escaping had no named home.
- **Still to do before release:** the owner's claude.ai tries, from
  `uv run skillcheck --tries` on the six modules, and deleting the six old skills from the
  owner's account and the organization's library, so none loads beside its successor. Other old
  skills, such as `windows-admin`, name the old ones, and would only point at a name that's gone.

## 2026-10-26 — `AGENTS.md` back under its 150-line target

- **Asked, by the owner:** "yes do all", to trimming `AGENTS.md` from 173 lines.
- **Done:** tightened in place to 149 lines. Every rule, invariant and check stays in the file
  agents load; the `src/skillcheck/` list became one line, and nothing moved elsewhere, since a
  rule outside `AGENTS.md` is one a session may never read.

## 2026-10-26 — Signed releases, and a hook that checks them

- **Asked, by the owner:** "yes do all", to signing releases with build attestations and having
  the cloud install hook verify them, since the hook installed "latest" on HTTPS alone and the
  supply-chain draft tells others to verify by who built a file.
- **Release workflow:** a job of its own, `Release attestation`, downloads the built files and
  signs them with `actions/attest`, Sigstore's public-good instance, with `id-token: write` and
  `attestations: write`. It runs no checkout and none of the build's dependencies, so nothing
  they bring can ask for the signing token. The page job checks every file's signature with
  `gh attestation verify --signer-workflow` before it publishes, and attaches the bundle as
  `attestation.sigstore.json`.
- **The hook:** it fetches the bundle from the same release, not GitHub's attestation API,
  because a cloud session's proxy refuses that API for a repository not attached to the
  session, which is every session on another repository. It requires the statement to name the
  archive's SHA-256 and this repository's `release.yml`, and runs `gh attestation verify` where
  `gh` is installed, refusing the release if it fails. It refuses a version older than the one
  installed.
- **What it doesn't do:** with no `gh`, the hook can't check a Sigstore signature with the
  standard library alone, so it checks the digest and the claims only and says so on stderr.
  Someone able to replace the release's files could replace the bundle too, and that check
  wouldn't see it. Where `gh` is installed, it would.
- **What it costs:** one more download each session; a release can no longer be withdrawn by
  deleting it, since the hook refuses the older one, so a bad release is fixed by a newer one;
  and where `gh` can't reach Sigstore's trust root, the hook keeps the skills already installed
  until it can.
- **Considered:** a checksum file beside the files, which proves nothing about who built them
  when it comes from the same place; and GitHub's attestation API, which the proxy refuses.
- **Reaches:** only environments whose setup script carries 0.1.21's `cloud-setup.sh` lines or
  later. An older hook keeps installing without these checks until the lines are replaced.

## 2026-10-26 — Standard v0.48.2: language toolchains current to 2026-10

- **Asked, by the owner:** "yes do all", to seven proposed rows, each checked that day at its
  source from research R09, R10, R11 and R21.
- **Changed, in the standard, as F155 and a change of its own:** *Language toolchains* reads
  "Current at 2026-10". Python names every supported branch and 3.10's end; PowerShell 7.4 and
  7.5 and .NET 8 and 9 end on 2026-11-10; Pester 6.x replaces "5.7.x is the safe pin"; Node 26
  is the default for new work; Rust is 1.99.x.

## 2026-10-26 — Release 0.1.20, the finished fixes apart from the drafts

- **Asked, by the owner:** "yes do all", to a list that recommended moving the finished fixes
  off the draft pull request #73 to a branch of their own, with Dependabot's #74, merging once
  checks pass, and releasing 0.1.20.
- **Why apart:** two of the owner's repositories pin 0.1.18 for their weekly `--outdated`, which
  ends its run on a transfer cut short. The fix sat on #73, which can't merge while its two
  modules, `review-loops` and `supply-chain-security`, are drafts.
- **Carries:**
  - the cut-transfer fixes in `--verify` and `--outdated`;
  - the hidden-character scan widened to `src/`, `tests/`, `docs/`, `.github/` and every root
    file, the install hook's refusal of hidden characters, and escaped outside text;
  - uv 0.13.5 in CI, past GHSA-hq85-5cpj-mr62, and Dependabot's `uv_build` floor;
  - the GitHub date in `actions-security`, ten lessons in `ROADMAP.md`, the wave 1 and R21
    prompts brought up to date, and the five research results filed with what was checked.
- **Left on #73:** the two drafts and their decision entries. Each commit here names the #73
  commit it was picked from.

## 2026-10-21 — Release 0.1.19

- **Asked, by the owner:** "do everything you can up to 6 and release. plan 7 for the next
  release after we have more info", of a list of tasks given that day, and "update your own
  dependencies if possible, we should be practicing what we preach".
- **Carries:**
  - the example checker and the trigger-test runner, two of the rebuild plan's shared tools;
  - the three rules on what the text says (the entry below);
  - `--outdated`'s fixes: requirements locks, tag-pinned actions, a comment taken for a
    version, and each registry asked once a run;
  - the New York-first times and standard v0.48.1, merged on 2026-10-20.
- **The roadmap, corrected:** the weekly currency check is shipped as the Freshness workflow,
  less an end-of-life warning, now a row of its own; the map refresh on Dependabot's updates
  is shipped as CI's `--bom-check`.
- **Item 7, the two company audits' fixes:** planned in the private repository's roadmap,
  which can name them, to follow the owner's answers to the audits' questions.
- **Own dependencies:** nothing is behind. uv 0.13.4 and Claude Code 2.1.305 came out on
  2026-10-20, inside the three-day wait the rule keeps, so they wait for Dependabot's pull
  requests after 2026-10-23. Practicing the rule means waiting, too. ShellCheck comes in at
  its newest, `shellcheck-py` 0.11.0.1.
- **Release 0.1.19:** this pull request's merge, released by the Release workflow once CI
  passes on it.

## 2026-10-21 — Checking what the text says

- **Asked, by the owner:** "are we checking for good info security? for plausible deniability
  when needed it (for testing)? things like this? input and output sanitation, not just of
  type and int, etc, but of what they say? but we should do the rest too." Then, as examples:
  "i know this is a test, let me give fake data, not use real for a test", and "i need to make
  sure the other application cannot accidentialy read this data it is necessary to uphold our
  stanards".
- **Read as:** the habits an agent should have, fake data in tests and one application's data
  out of another's reach, so the checks enforce them. The owner was told so, and asked to say
  if they meant phrases to flag.
- **Done, as `skillcheck` rules that run with every check:**
  - `test-data`, in skills and tests: reserved email domains, RFC 5737 addresses, and
    `CHANGEME` or a placeholder for a secret's value; a real credential's prefix fails
    anywhere;
  - `content-safety`, in what agents read: fetch-and-run commands, and text steering an agent
    against its user. Quoted text passes, as a quotation;
  - `private-name`, everywhere: names this public repository withholds, listed only as
    SHA-256 hashes in `.github/private-names.sha256`. The list was seeded with the private
    repositories, the owner's employer and the repositories the skills ran on, and names none
    of them.
- **Considered for the names:** a list in a CI secret, which no local run or session could
  read; a keyed hash, the same. A plain hash can be confirmed by someone who already guesses a
  name, and reveals nothing to anyone who doesn't, which is the risk that matters here.
- **Left to the modules that teach it:** sanitizing input and output in the code the skills
  teach, by meaning and by context. That's `input-handling`, `secure-coding` and
  `ai-agent-security`, after research R04 and R01. Keeping one application's data from
  another goes there too, and into the standard as a proposed change once that research is in.

## 2026-10-21 — The example checker and the trigger-test runner

- **Asked, by the owner:** the rebuild plan's shared tools, approved on 2026-10-15 and 16, and
  "do everything you can up to 6".
- **Built:** `skillcheck --examples`, which CI runs, and `skillcheck --triggers` with
  `--tries`, which run by hand.
- **Chosen:** ShellCheck pinned through `shellcheck-py` (MIT) in the dev group rather than the
  runner image's, so CI and a local run use one version. PowerShell is parsed by `pwsh` from
  GitHub's Ubuntu image, fed on standard input so nothing runs; no skill holds PowerShell yet.
- **Found by the first live trigger run:** none of the four `gitignore` requests loaded
  `git-workflows` in Claude Code, which answered them from its own knowledge. The descriptions
  get tuned against the runner before the rebuilds.

## 2026-10-20 — Standard v0.48.1: the order of a local time and its stamp

- **Asked, by the owner:** "New York first", for how times are given to them; the entry below
  changed this repository.
- **Changed, in the standard, as F154 and a change of its own:** Phase 0's fifth question also
  asks which comes first, and `display_time` in the Phase 0 block records it. The stamp is
  unchanged: UTC, whatever the answer.

## 2026-10-20 — Times to the owner: New York time first, the UTC stamp beside it

- **Asked, by the owner:** "yes all should match", for how three repositories give times; then
  "New York first", when asked which order.
- **Supersedes, in part,** the entry of 2026-10-19 on UTC as the stamp. The stamp is
  unchanged: every record is UTC, and every local time is derived from it by the tool. Only the
  order shown to the owner changes, to the one the owner's other two projects agreed between
  them on 2026-10-19.
- **Changed here:** `skillcheck --time`'s output, the `times` check, AGENTS.md and the house
  style. The standard's own example changes on its own, as the standard's changes do.

## 2026-10-19 — Every dependency on its newest release, checked weekly

- **Asked, by the owner:** "are all repos using the most up to date of all dependcies, they
  should. And we need a way to make sure they are. Like a weekly repo check".
- **The rule:** each dependency is on its newest stable release once that release has been out
  three days, the platform's default wait, which the standard already holds. Security fixes
  don't wait. Research prompt R21 tests the rule against the evidence; its result may change
  the wait or the exceptions.
- **Done here:** Python 3.15, uv 0.13.1 in CI, Claude Code 2.1.302 and the dev tools' newest
  releases (#66), and uv 0.13.1 in the private repository's CI.
- **The check:** `skillcheck --outdated`, run weekly by the Freshness workflow in an issue of
  its own. It reads what a repository uses through the dependency map's readers, so the two
  never disagree. It covers what Dependabot doesn't: tool versions a workflow names as
  inputs, `.python-version`, and a range in `pyproject.toml` that shuts out a new release.
- **Considered:** Dependabot alone, which can't see those three; Renovate, which can, but is a
  second update bot with its own configuration to keep. The check proposes nothing itself;
  Dependabot still opens the update pull requests.
- **Not covered:** runner images and system packages, since neither has a registry naming its
  newest version.
- **Other repositories:** the owner's other projects get their lists and the command to run,
  through the owner. Nothing in them was changed here.

## 2026-10-19 — A two-repository loop's audit against a reference tool, checked for lessons

- **Asked, by the owner:** "do a full check against both repos … see if you missed anything and
  fix yourself as well".
- **Read:** one repository's audit of its output against an established tool's, and each of
  its numbers against the primary logs, reports and source it cites. Nothing in either
  repository was changed; the findings went to the owner as a report outside this repository.
- **Taken into a shipped module:** `writing-style`, that a time copied from a source keeps the
  zone the source gave it.
- **Waiting for their modules,** as L41 to L44 in `ROADMAP.md`: a reference checked before a
  match with it counts, corroboration that is independent and carries weight, "not found"
  against "couldn't look", and a summary computed from the same state as its verdict.
- **Missed by this repository's earlier review of the same loop,** on 2026-10-19: the
  corroboration and absence findings. Both were in records it read.

## 2026-10-19 — Rounds 34 and 35 of the two-repository loop, read for lessons

- **Asked, by the owner:** "do a review of both repos and see what is learned".
- **Read:** both repositories' history from 2026-10-15, by two read-only reviewers, one per
  repository. Each lesson cites its commits or lap statements, and those quoted here were
  checked against them before they were used. Nothing in either repository was changed.
- **Taken into shipped modules:**
  - `ci-workflows`: a timeout with no known cause is recorded each time and instrumented, not
    hidden by a higher limit; diagnostics that print only on failure; a build chain that goes
    on after a step fails;
  - `releases-and-versions`: a release staged and never published; a candidate proved only in
    the working tree;
  - `commits-and-pull-requests`: a fix to inherited upstream code whose commit doesn't say so.
- **Waiting for their modules,** as L31 to L40 in `ROADMAP.md`: checks that can fail, a ratchet
  after a flaky fix, the seam between two tools, shared validation, four on running the loop,
  parallel helper sessions, and checked status against unchecked prose.
- **Already held here, so not added:** a push in the same command as a failing suite, trimmed
  output, a stale local branch, approval given with the request, and a file agreed word for
  word.

## 2026-10-19 — Standard v0.48.0: UTC is the stamp, and a first audit asks the reader's zone

- **Asked, by the owner:** "on an iniitial audit, you can ask for what to use, but gmt should
  be the "stamp"".
- **Changed, in the standard, as F153 and a change of its own:** Phase 0's questions that can't
  be detected gain a fifth, asked at the Phase 3 wait: the time zone and clock the human reads
  times in. Whatever the answer, every time a run writes is UTC with its zone; the answer adds a
  local time beside each stamp in what the run tells the human, worked out with the time zone
  database. The draft comes from the offsets on the human's own commit dates, and the default
  is UTC alone. `display_time` joins the Phase 0 block's `asked`.
- **Not done:** no parity run. The samples' answer keys rate findings, and a question asked at
  the wait changes no finding.

## 2026-10-19 — UTC is the stamp, local times are derived, and a check holds it

- **Asked, by the owner:** "GMT is the gold standrad, just derive from that. we need timestamps
  to be correct. make sure the check for this, and on an iniitial audit, you can ask for what to
  use, but gmt should be the "stamp"". This sharpens the entry below on times given in UTC and
  New York time.
- **Built:** `skillcheck --time STAMP [ZONE]` gives an ISO 8601 time, which must carry its
  offset, as UTC and as the zone's local time, worked out from the time zone database. Its
  tests cover the hour New York's clocks repeat on 2026-11-01. `now` is the current time.
- **Checked:** the `times` rule fails Markdown here that writes a time of day without UTC, or a
  12-hour local time with no UTC time before it on its line. It leaves code, ISO 8601 times,
  dated research results and decision entries dated before 2026-10-19 alone: the one time it
  finds today is in an entry of 2026-10-05, which stays as written.
- **Written down:** `AGENTS.md`, and the house style's *Records and dates*, which every
  repository using `house-style` follows. The standard asks the question at a first audit, in its
  own change.
- **GMT or UTC:** the stamp is written `UTC`, the name time zone databases and ISO 8601 use; `GMT`
  passes the check too, since for a timestamp the two agree.

## 2026-10-19 — Times given to the owner in UTC and New York time

- **Asked, by the owner:** "can you also provide them in my timezone, EST/NYC and using a 12 hour
  clock with AM/PM? present both. just as a standard until i change this."
- **Decided:** `AGENTS.md` asks every session to give a time to the owner as recorded, in UTC on
  a 24-hour clock, and in New York time on a 12-hour clock with AM or PM and the zone in effect,
  EDT or EST. Commits, records and files keep UTC alone, which the owner called fine for
  official records. The private repository's `AGENTS.md` says the same.

## 2026-10-16 — Every skill says when it's at fault, and drafts the report

- **Asked, by the owner:** "You should include some level of this in yourselve for all skills.
  It shouldn't be much, but if someone has an issue or concern, there would be a sentence or a
  word that gives it away and why. If it's a bug somewhere then yes give a verbose answer." The
  owner wants their brother, and later colleagues, to use the skills on real work and report
  what goes wrong.
- **Decided:** every `SKILL.md` ends with one shared section, `When something here is wrong`.
  When a person says advice is wrong, out of date, failed or doesn't fit, the model answers the
  problem first, then says in one sentence whether the fault looks like the skill's, and why.
  When it is the skill's, it drafts a full report to paste as an issue: skill and module,
  version, the request, the line that misled, what happened, what's right with its source, and
  a suggested fix. Private data, company detail and repository names stay out, and it files
  nothing unless asked.
- **Why one text, held word for word:** the section changes how every skill behaves, so it is
  kept once, in `src/skillcheck/core/reporting.py`. `skillcheck` fails a skill without it, or
  with any other wording, and `--new` writes it. The address comes from the catalog's
  `repository`, so a repository that uses these tools for its own skills reports to itself.
- **Why at the end of `SKILL.md`, not in a module:** it applies whatever module is read, and
  `SKILL.md` is always read when the skill loads. It costs about 900 characters per skill, and
  nothing in the listing, which holds descriptions only.
- **Also done the same day:** Dependabot's four open updates came in together, as #58, with the
  git-workflows example moved to the same `setup-uv` commit. The private repository's one
  update merged on its own.

## 2026-10-16 — `git-workflows` and `house-style` made of modules, and facts named across the repository

- **Asked, by the owner:** "do the rest if you can", on the weekend's work, which included
  converting both skills.
- **Changed, superseding part of "The tools for skills made of modules" below:** a module may
  name any fact the repository defines, not only its own. An ID is still unique across the
  repository, so a fact's name never means two things, and a module that moves keeps every fact
  it names. `skillcheck` reports a name no fact table defines.
- **Why:** the git-workflows facts were each named by several of its topics. Under the old rule
  each module would have needed its own copy of a shared fact, which the unique-ID rule forbids,
  or the topics would have had to stay together.
- **`git-workflows`, eight modules:** `commits-and-pull-requests`, `branches-and-merging`,
  `ci-workflows`, `actions-security`, `git-hooks`, `releases-and-versions`, `leaked-data` and
  `gitignore`. Its nine rules stay in `SKILL.md`, each naming the module that holds it, with the
  commands to check before acting and the audit's status words. Each of the 103 facts and 30
  audit checks went to exactly one module, by script, checked for none lost and none doubled.
  `leaked-data`, `git-hooks` and `gitignore` had no Why or Audit of their own, so they gained
  them, from reasons and checks the old files already stated.
- **`house-style`, two modules:** `writing-style`, with how each rule applies, its reasons and
  the style guides' facts, and `prose-check`, with the Vale check, its reasons and Vale's facts.
  The thirteen rules stay in `SKILL.md`, where the asset tests read rule 3.
- **Kept as they were:** both skills' names, descriptions, assets and asset tests. Each skill's
  trigger set in `tests/fixtures/skills/` stays, because the description still decides whether
  the skill loads. Each module has its own set in `tests/fixtures/modules/`, for which module a
  loaded skill reads.
- **`.vale.ini` skips double-quoted text in every module,** where it skipped it in `facts.md` and
  `sources.md` before, because each module now holds its own facts and sources.
- **Considered for the new trigger sets:** the skill-level sets, which answer a different
  question, and one file per skill, which a move would have to split. One file per module, as
  the module checks already require, moves with its module.

## 2026-10-16 — Skills made of modules work on claude.ai, and are tried there by hand

- **Asked, by the owner:** "This does still need work with claude.ai as well."
- **Read, at Anthropic's Agent Skills overview
  (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, 2026-10-16):**
  - a skill's name and description are always loaded: "Claude loads this metadata at startup
    and includes it in the system prompt";
  - when triggered, "Claude reads SKILL.md from the filesystem using bash", and other files
    when its instructions point to them, so a module costs nothing until read, on claude.ai as
    in Claude Code;
  - the triggered file's cost is given as "Under 5k tokens";
  - custom skills on claude.ai need "code execution enabled", and there skills "may have full,
    partial, or no network access" by settings;
  - the API takes "up to 20 Skills for each request" (the skills guide, read the same day).
- **Changed:** `skillcheck` holds each `SKILL.md` to 20,000 characters, about 5,000 tokens.
  The authoring guide's step 5 adds the claude.ai rules: no Claude Code tool names, core
  guidance without the network, and the owner's tries listing for each module the skill and
  module a request should reach, and a near miss.
- **Chosen, by the owner:** claude.ai is tested as the six tries were, by the owner asking
  questions in new chats from a list the session gives, not by an API run, which needs a key
  and costs money. In their words: "that is fine, that is what i want for claude.ai."

## 2026-10-16 — The tools for skills made of modules

- **Built, as the roadmap's shared tools planned, with the owner's permission:**
  - `skillcheck` checks a skill made of modules: its router table, each module's file and its
    six sections, each module's trigger tests (requests that should reach it and near misses),
    no Markdown in `references/` outside a module, one home per module name, and each built
    module's shipped `ROADMAP.md` row naming its skill;
  - facts live in each module's Facts section, a module names only its own, and an ID is
    unique across the repository, so a module moves without a collision;
  - `skillcheck --new SKILL` writes a router, `--new-module MODULE SKILL` adds a module, and
    `--move MODULE SKILL` moves one, refusing with nothing changed when it can't;
  - the listing budget is room for 20 skills.
- **Why a router table and not a manifest file:** the table is what Claude reads to pick a
  module, so the one list both routes and registers, and can't disagree with itself.
- **Why `docs/module-moves.md`:** the moves need a record the command can append to and a
  person can read. `docs/decisions.md` is prose, appended by hand; `ROADMAP.md` holds the plan,
  not the history; a release's changelog is cut at release. None fits a row per move.
- **Not done yet:** `git-workflows` and `house-style` keep their older layout until they're
  converted, which the checks allow. The trigger-test runner, the example checker and
  `skill-builder` follow in their own pull requests.

## 2026-10-16 — Fifteen skills made of modules, in place of a hundred skills

- **Asked, by the owner, verbatim:** "I want the functionality and more, I don't. Care how it is
  divided, named, etc. I want it to be efficent and effective. So if that means a complete
  restructure I'm all for it, and now is the time to do a complete refactor on this. So don't
  hold back. But it needs to work, make sense, and be structured so that if we need to do so
  again it's easy and not a mystery with a ton of research. We should be able to spin off a
  skill into multiple if needed, or whatever."
- **Decided:** `ROADMAP.md` now plans 15 skills, each a trigger, made of modules. The 60
  planned skills become modules under their old names, each with one home skill, so the
  research prompts, lessons and intake that name them still apply. Its new section *How skills
  are structured* gives the rules: a module is one self-contained file, a router `SKILL.md`
  picks it, trigger tests decide when a module spins off, merges or moves, and a move is one
  `skillcheck` command with a record.
- **Why:** each installed skill's description is in context all the time, and Claude Code
  gives the listing 1% of the context window, 8,000 characters on a 200,000-token model (the
  2026-10-15 entry measured it). A hundred skills at 240 characters would leave most of them
  as bare names there, and colleagues' claude.ai accounts load the same descriptions. Fifteen
  fit. A module costs nothing until it's read.
- **Supersedes:**
  - the 2026-10-15 entry's room for 100 skills: the listing budget becomes about 20 skills in
    the shared tools;
  - the 2026-10-15 answer 7, replacing old skills in place: old copies are deleted as each
    wave ships, which the owner already chose earlier today;
  - decision 33's pairing map, which shrinks to the pairs between skills;
  - this session's own advice earlier today to keep a skill per language. One `coding` skill
    with a module per language costs one description instead of eleven, and its trigger tests
    decide whether any language spins off.
- **Not changed:** the three shipped skills keep their names. The research waves are the same.
  `AGENTS.md`'s invariant that every skill links `references/why.md`, the authoring guide's
  layout and the listing rule change with the module checks, in the shared tools' pull request.

## 2026-10-16 — The organization's library read, `code-standards` counted, and private skills by token tried

- **Read, from the owner's screenshots of the admin inventory:** the organization's library
  holds 28 of the owner's old skills, each with the audience "Everyone · installed by
  default". Colleagues use them: the owner says about five use claude.ai and one uses Claude
  Code.
- **Found:** `code-standards` is among the 28 but not among the copies synced into sessions.
  It left them on 2026-09-28, when the owner deleted their own copy, and the library kept it.
  The plan counted 33 old skills from the synced copies, so it missed it. `ROADMAP.md` now
  counts 34 and sends its topics to five planned successors, its old copy going last, since
  twelve old skills say they must read it first.
- **Chosen, by the owner, verbatim:** "we should just keep removing them as we replace them. i
  can then tell people to start using the plugins". Deleting an old copy takes it from
  colleagues too; they add this repository's plugins themselves. `ROADMAP.md` records it as
  its colleagues step.
- **Changed, in `docs/authoring-a-skill.md`:** step 12 has the old copy deleted in the
  organization library's inventory as well as in the owner's own settings.
- **Tried, and refused:** a read-only token for the private companion, held as a network secret
  in the cloud environment, so a session without the repository attached could install its
  skills. A fresh session with only this repository attached got 403 on every request: "GitHub
  access to this repository is not enabled for this session. Use add_repo to request access."
  The cloud's own access check comes before the secret, so attaching the repository stays the
  way in, and the owner deletes the secret and the token.

## 2026-10-16 — The private companion repository, set up, and the empty one deleted

- **Done, by the owner:** they deleted the empty organization repository, which item 29 of the
  2026-10-13 answers had said to archive; this supersedes that item. They created the private
  companion repository that item 5 of the 2026-10-15 answers asked for, set its settings by the
  steps given, and attached it to the session.
- **Set up against the standard, v0.47.0:** the run stopped at both waits, and the owner
  approved all ten items. Its record holds the answers. This entry names only what bears on
  this repository:
  - **Its tier is T1:** work-owned, never public, guidance and templates that change no system
    themselves, and used by the owner alone for now. Sharing it with colleagues through the
    organization's library raises it to T2, and the standard runs again first.
  - **It reuses this repository's tools rather than copying them.** Its CI runs `skillcheck`
    from this repository at release 0.1.16's commit, and the house style from that release's
    `HouseStyle.zip`. Each release here can be taken up there by raising one pinned commit.
  - **Its skills reach sessions** by a second personal marketplace on the owner's claude.ai
    account, and by attaching it to a cloud session: the cloud hook here downloads releases
    without credentials, which a private repository refuses.
  - **Its plugin and skill names** start with the company's name, so none clashes with a
    skill here.
- **Found:** on GitHub Free, a private repository's ruleset request is refused with "Upgrade to
  GitHub Pro or make this repository public", so its checks warn rather than block, as the
  standard's platform table says.
- **Said, by the owner:** this repository's skills are meant for colleagues too, in time, as
  the companion's are. It is public already, and rated T3 on the imminent state, so the tier
  stands; what changes is that a colleague's claude.ai account, not only the owner's, may
  install its plugins.
- **Changed:** the exclusion list's reason for `canvas-design` now says it is kept on claude.ai,
  as the previous entry records.

## 2026-10-16 — The dependency map checked on every pull request, `canvas-design` kept, and chat syncs

- **Chosen, by the owner:** CI runs `skillcheck --bom-check` on every pull request. This
  supersedes the 2026-10-05 entry's *Not run on pull requests*. A Dependabot update now fails
  until a session regenerates the map in its branch, which the 2026-10-13 answers already ask
  for before merging one. It would have stopped release 0.1.11's stale map at its pull request.
- **Chosen, by the owner:** `canvas-design` stays on claude.ai, and stays off in Claude Code
  through the exclusion list. This settles the 2026-10-15 entry's undecided item 3.
- **Found:** after release 0.1.16, a new claude.ai chat loaded standard v0.47.0 with nothing
  pulled by hand. With **Sync automatically** on, the plugins follow each release, which
  settles the question the earlier entry left for this release. No **Check for updates** step
  is needed after a release.

## 2026-10-16 — The six claude.ai tries, standard v0.47.0, and release 0.1.16

- **Tried, by the owner,** on claude.ai with the plugins at 0.1.15, each request in a new chat,
  as step 5 of `docs/authoring-a-skill.md` asks. All six pass:

  | Skill | Request | Result |
  |---|---|---|
  | `house-style` | Rewrite a paragraph in the house style | Pass: led with the change, cut the filler, American spelling, and asked about the hedge it dropped and the palette it couldn't name |
  | `house-style` | Which heading case a README uses | Pass: sentence case, citing the Vale rule; every other claim is in the skill |
  | `git-workflows` | A commit message for retry logic | Pass: a 48-character subject and a body saying why. It led with Conventional Commits, which the skill allows beside "area: summary"; the pass line named only the second, and was too narrow |
  | `git-workflows` | Squash or merge commits | Pass: merge commits, the reason and the trade. Its claims hold: all three of the owner's public repositories allow merge commits only |
  | `project-bootstrap-and-audit` | Set up a new Python CLI repository | Pass: asked the Phase 3 questions, drafted none of the three never-drafted answers, and wrote only its report. It didn't ask how long the tool must last, which the standard asks only when choosing a language, and Python was named |
  | `project-bootstrap-and-audit` | What an audit of configuration checks | Pass: the stakes questions and the ten dimensions. It found that the standard names no dangerous workflow trigger |

- **Found, and checked:**
  - python.org's release list, read 2026-10-16, gives Python 3.15.0 on 2026-10-09. The
    standard's toolchain table named 3.14.x.
  - The routing table sends "set up something new" with no repository yet through the run,
    and Phase 0 refused to continue without a git repository. The new-project run broke that
    rule to reach its questions, and recorded doing so.
  - The standard has no match for `pull_request_target`, `workflow_run` or template injection.
    `git-workflows` covers all three, in its security reference and row 13 of its audit.
- **Changed, approved by the owner on 2026-10-16, as standard v0.47.0, a change of its own:**
  F150, the Python row; F151, Phase 0's case for a new project before its repository exists;
  F152, dimension 6's rating of dangerous triggers and template injection, with a dated fact
  from GitHub's security hardening guide. A public repository with either is `BLOCKER`, as
  `git-workflows` rates it; a private one, where only collaborators open pull requests, `GAP`.
- **Not done:** no parity run. F150 changes a fact, F151 a case no sample reaches, since every
  sample has a repository, and F152 a pattern no sample's workflows contain.
- **Done, by the owner:** this repository's merge commits take the pull request's title, set
  under Settings, General, read back as `merge_commit_title: PR_TITLE`. Nothing here reads the
  old subject: the `subjects` check skips merges.
- **Release 0.1.16:** this pull request's merge, so the hook and the plugins carry v0.47.0.

## 2026-10-16 — claude.ai kept a plugin copy from 2026-09-23 until it was removed and added again

- **Found, in the owner's chat:** after the plugins were added from **Discover**, a new chat
  still loaded `project-bootstrap-and-audit` with standard v0.36.0. That is the copy installed
  on 2026-09-23, which the 2026-09-28 entry also found. It stayed through every catalog version
  from 0.1.1 to 0.1.15.
- **Fixed, by the owner:** they removed every `Standards` and `Engineering` under **Customize >
  Plugins > Yours**, and added both again from **Discover**. A new chat then loaded v0.46.0,
  with the skill's metadata and its copy of the standard agreeing, and no older copy beside it.
- **So:** a version change in the catalog doesn't reach a plugin claude.ai already holds unless
  something pulls it. Whether **Sync automatically** is that something is checked at the next
  release by asking a new chat the same question. If it isn't, each release's steps for the
  owner include **Check for updates**.

## 2026-10-16 — The automatic route, checked in the owner's environment

- **Done, by the owner:** `protect-main` now requires `prose` beside `checks`, `catalog` and
  `secret-scan`, all from GitHub Actions, read back from the ruleset at 12:34 that day. They
  deleted the old uploaded copies (step 2A of their steps), added this repository as a
  marketplace in their own **Customize > Plugins**, and added the setup lines to their cloud
  environment.
- **Found:** **Organization settings > Plugins & skills > Sync from GitHub** lists only private
  and internal repositories, and says to fork a public one into a private one first. That is
  the organization-wide route, and the attempt there failed; the owner's own **Customize >
  Plugins** took the same repository with no error.
- **Checked:** a fresh cloud session in that environment, with no repository, listed
  `git-workflows`, `house-style` and `project-bootstrap-and-audit`, with no prefix and no second
  copy. Its ledger said release 0.1.15, the hook and its `SessionStart` entry were in place,
  `syncClaudeAiPlugins` was false, and the standard said 0.46.0. That settles the 2026-10-16
  entry's untested half for cloud sessions. Whether claude.ai's automatic sync takes the next
  release is still to be seen, at the next release.

## 2026-10-16 — `human-factors`: where it applies, and research run R23

- **Said, by the owner,** answering the previous entry's three questions:
  - **Example:** a familiar, slower tool kept over a faster one.
  - **Where:** everywhere.
  - **Which agents:** only some, perhaps only a few. Most agents should be unbiased when they
    gather information, unless what they gather isn't objective fact.
- **Changed:**
  - `ROADMAP.md`: `human-factors` is loaded only by the few agents that design or change what
    people do, and never bends a factual finding. Its description will say so when it's built,
    so it doesn't load for research or fact-finding.
  - `research/prompts/R23-human-factors.md`, research run R23, priority 2, starts from the
    owner's example, asks the literature for the rest rather than a list of guesses, and tests
    the limit: language models' measured sycophancy, biases carried into gathered information,
    and where a person's preferences rightly count. Fatigue and shift design stay in R19.

## 2026-10-16 — `human-factors`: the skill `human-factor-audit` was meant to be

- **Said, by the owner:** `human-factor-audit` was meant to be much more than an audit of
  schedules and optimizers. It was to hold human notions, habits and mindsets that are common
  to people, that may look odd or wasteful to someone else, and that serve a purpose.
- **Changed, in `ROADMAP.md`:** the plan had `human-factor-audit` become
  `optimization-and-scheduling`, which kept only the schedules. A new planned skill,
  `human-factors`, takes the wider scope: what each such habit is for, how to spot one before a
  design, an automation or an optimization removes it, and how to design with it.
  `optimization-and-scheduling` keeps the human factors in plans and pairs with it. The name
  differs from the old one because the old one names only an audit, as step 12 of
  `docs/authoring-a-skill.md` allows.
- **Next:** research run R23, written once the owner has given the examples they had in mind,
  so the prompt asks about those first. R19's question 7 covers fatigue and shift design only.
- **Supersedes:** the previous entry's successor for `human-factor-audit`, which is
  `human-factors`. Keeping the old copy until then stays the recommendation, with more reason.

## 2026-10-16 — In a member's own settings, an uploaded skill is deleted, not turned off

- **Found, by the owner:** their claude.ai account belongs to an organization, on which they
  are also an Owner. In their own settings, **Customize > Skills**, it offers only removal for
  an uploaded skill, with no switch to turn it off. The Help Center's skills article, read on 2026-10-16,
  describes a switch beside each skill and deletion from the "..." menu, so the account and the
  article differ, and what the account shows is what stands.
- **Found, in the plugins page, read on 2026-10-16:** a plugin is turned off with its
  **Disable plugin** toggle and removed with **Remove** from its menu. A marketplace is added
  under **Customize > Plugins**, **Add > Add marketplace**, with **Check for updates** and, for
  one added from github.com, **Sync automatically**. A marketplace's plugins are then added from
  **Discover** with **Add**.
- **Found, in the plugins admin page, read on 2026-10-16:** an Owner manages the
  organization's plugins and skills under **Organization settings > Plugins & skills**, whose
  **Policy** tab holds **User-created skills**. With it off, members can't upload skills or add
  their own marketplace. Syncing a marketplace for the whole organization needs a private or
  internal repository, as the 2026-09-23 entry found, so this public one stays a member's own
  marketplace. Nothing here is set at the organization's level: that would reach every member.
- **Changed:** every step that turned an old claude.ai skill off now deletes it.
  `docs/authoring-a-skill.md` step 12 has the session say, for each skill that depends on an old
  copy, whether it would break or only names it, and the owner chooses which to delete. The
  previous entry's "turns off" for dependents is superseded by this.
- **For the owner's current step:** `human-factor-audit` only names `skill-orchestrator` and
  `markdown-standards` as companions, and one of its triggers can no longer fire. Deleting it
  would lose the source its rebuild, `optimization-and-scheduling`, is written from, so keeping
  it until then is the recommendation; the choice is the owner's.

## 2026-10-16 — Skills reach cloud sessions from the release, and release 0.1.15

- **Asked:** after release 0.1.14, the owner asked that getting the skills into sessions be
  made automatic. Uploading by hand is no trouble to them, so this was wanted only if it can
  be done, and with one condition: the owner removes the old skills, and anything that depends
  on them, first.
- **Found, by tests on 2026-10-16, with Claude Code 2.1.301 in this cloud environment:**
  - A skill that a `SessionStart` hook writes into `~/.claude/skills` loads in that same
    session. A headless session started in a scratch folder listed it and read it.
  - The same, with the hook in user settings, as `cloud-setup.sh` writes it: a fresh headless
    session ran it, restored a skill deleted to prove the hook ran, and listed all three skills
    by their plain names.
  - The claude.ai uploads of `git-workflows` and `project-bootstrap-and-audit` then loaded as
    well, as `anthropic-skills:git-workflows` and `anthropic-skills:project-bootstrap-and-audit`.
    Two copies of a skill is what the owner's condition prevents.
  - `skillOverrides` keys match the listed name: `"git-workflows": "off"` hid the installed
    copy, and the synced one came back under its prefix. That lasts only while the uploads do.
  - The tests restored this container's settings and removed what they installed.
- **Found, in the docs, read on 2026-10-16:**
  - A cloud session still doesn't install the plugins a repository turns on under
    `enabledPlugins`. The plugin-loading page names Cowork and terminal sessions for plugins
    synced from claude.ai, not cloud sessions.
  - A setup script runs before Claude Code starts, and its result is cached for about seven
    days, so an install there alone would lag the releases. The hook runs at every session start.
  - claude.ai updates a plugin from a personal marketplace when Sync automatically is on. Its
    docs don't say what counts as a change; each release here changes the version.
  - No public interface uploads a skill to a claude.ai account.
- **Chosen:** this supersedes how skills reach cloud sessions in item 35 of the 2026-10-13
  entry *The owner's answers to questions 19 to 35*, and the 2026-09-23 entry *The plugin reaches the account, not cloud sessions*:
  - **Cloud sessions:** each release carries `skills.zip` and `cloud-setup.sh`. The owner adds
    the setup lines to the environment once. The hook downloads the latest release's
    `skills.zip`, checks its manifest and every path in it, installs the skills into
    `~/.claude/skills`, and keeps a ledger, so it replaces and removes only what it installed.
    A failed download keeps what's there and never stops a session. It names any claude.ai copy
    still loading beside a skill, for the session to report. The setup lines also set
    `syncClaudeAiPlugins` to false, so a plugin copy can't load beside the hook's copy.
  - **claude.ai chat:** the two plugins from this repository's marketplace, with Sync
    automatically on, instead of uploaded ZIP files.
  - **The ZIP files stay on each release** as the fallback, uploaded by hand.

  *Considered:* installing the plugins from the setup script, cached for up to a week, and so
  up to a week behind a release; and a hook in each consuming repository, which would need a
  change in each.
  *Risk:* the hook runs nothing it downloads. It installs skills, whose scripts run only when a
  session runs them, as with any install, from a tag that the tag ruleset stops anyone
  moving. A bad release reaches every
  new session at once, which the withdrawal runbook in the README now covers.
- **Chosen:** removing old copies comes first, as the owner asked, and stays the order:
  `docs/authoring-a-skill.md` step 12 has the session name the old copy and what depends on
  it before a rebuild's release, which waits for the owner's word.
- **Changed:**
  - `house-style` is off in this repository's `skillOverrides`. The new `own-copies` rule
    fails these settings if any skill under `skills/` isn't off. It found `house-style` missing
    on its first run.
  - `bom.py`'s row for claude.ai says the account takes the plugins.
- **Release 0.1.15:** this pull request's merge, so that `cloud-setup.sh` and `skills.zip`
  exist on a release for the setup lines to fetch.

## Earlier entries, on the `archive` branch

The owner's "do all" of 2026-11-16 moved every entry dated before 2026-10-16, and the entries
since that only record a release, to the `archive` branch, verbatim. `docs/archive.md` indexes
them, and `git show origin/archive:<path>` reads one. Each line below points at an entry; the
entry holds the words. Unless a line names another file, the entry is in
`archive:2026-11-16/decisions-2026-09-23-to-2026-10-15.md`, under its date and title.

### Standing decisions from before 2026-10-16

- **2026-09-23, *Inception: set up against the standard*:** tier T3; the flat `skills/<name>/`
  layout, grouped only by the catalog; tooling in Python with uv; Apache-2.0; one Semantic
  Versioning version for the repository, bumped only on release, with a skill's name as public
  interface (A13); Actions pinned to full commit SHAs (A16); the plan in `ROADMAP.md` alone
  (A28); the standard's Test G in CI (A27).
- **2026-09-23, *Inception*, the organization's written permission** to publish the generic
  skills and tooling here, kept privately. `AGENTS.md`'s public-repository convention rests on
  it.
- **2026-09-23, *Inception*, declined:** an OpenSSF Scorecard workflow, until a second person
  commits (A17); a local pre-commit hook, until a secret or a lint failure reaches a pushed
  branch (A18). Mutation testing (A19) was taken up for two modules on 2026-11-03.
- **2026-09-23, *Inception*, never re-proposed:** rewriting history to change the initial
  commit's author email. Its other such item, on Anthropic's document skills, is superseded by
  the entry of 2026-11-16 on adapting them from a pinned commit.
- **2026-09-23, *The standard is rebuilt into the skill*:** the standard becomes the skill's
  parts in pieces, parity runs first, and its file goes in the last piece, release 0.2.0; the
  rebuilt skill is Apache-2.0 from piece 6; parity runs are fresh subagents in the working
  session; `claude plugin eval` in CI waits until an Anthropic API key is a repository secret.
  `ROADMAP.md`'s *Rebuilding `project-bootstrap-and-audit`* cites it.
- **2026-09-23, *Hidden-character checks beyond skills*:** agent files and research get the
  skills' scan (A30), now `AGENTS.md`'s hidden-character invariant.
- **2026-09-23, *Before the first merge: the 0.1.0 release, and a cost of SHA pins*:** a version
  that reaches `main` is published (A29); SHA pins stay, though Dependabot raises no alert for
  a SHA-pinned action, until GitHub raises them or a pinned action's vulnerability arrives
  before its update. The withdrawal runbook it settled is now
  [withdrawing-a-skill.md](withdrawing-a-skill.md).
- **2026-09-23, *Release 0.1.1: the marketplace takes the repository's name*:** the marketplace
  is `claude-code-skills`, until Claude Code rejects the name.
- **2026-09-24, *Fewest dependencies, newest versions: researched before it's a rule*:** the
  rule waits on R21's checked result, and holding this repository to it waits on the rule.
  `ROADMAP.md` tracks both.
- **2026-09-30, *The repository keeps its facts current, and checks its own shape*:** what the
  commit decides is checked on every pull request, and what depends on the date or the web on
  a schedule. `AGENTS.md`'s fact-row invariant and the Freshness workflow come from it.
- **2026-10-05, *The owner's answers to questions 1 to 17*:** release immutability on (1); a
  session merges its own pull request once every check passes, for work the owner asked for,
  and Dependabot's once tested together on `main` (4), which the steward and `AGENTS.md` cite;
  "area: summary" commit subjects (5); merge commits as the only method (16); private
  repositories without rulesets on GitHub Free, an accepted risk (15).
- **2026-10-05, *The repositories the skills run on go unnamed*:** `AGENTS.md`'s convention that
  a repository a skill ran on goes unnamed, even by a findable quote.
- **2026-10-05, *A dependency map, kept in CycloneDX*:** `bom.json` and `docs/dependencies.md`,
  built by `skillcheck` and never edited by hand. Its *Not run on pull requests* is superseded
  by the entry of 2026-10-16 on the dependency map.
- **2026-10-05, *Release 0.1.2 is tagged, and releases get a workflow*,** and *Releases publish
  their files, and the release job's defects are fixed*: the Release workflow makes each tag
  from a version and a full SHA on `main`, and publishes the release's files.
- **2026-10-05, *Repository settings in the kickstart file, two rulesets, and release 0.1.4*:**
  the kickstart file carries the settings checklist, and a session changes no setting itself.
- **2026-10-05, *The account's settings in the kickstart file, and release 0.1.5*:** a personal
  commit address is named in a report only, and rewriting published history to remove one is
  never proposed.
- **2026-10-05, *`house-style`: one style for prose, checked by Vale, and release 0.1.6*:** one
  style, American spelling and a Vale check (answers 11 to 13).
- **2026-10-13, *The owner's answers to questions 19 to 35, and F115 to F137*:** a session
  regenerates the dependency map in each Dependabot pull request before merging it (27); no
  work repository without the employer's agreement (28); the pairing map (33), which
  `ROADMAP.md` cites, shrunk by the entry of 2026-10-16 on fifteen skills made of modules;
  company templates and defaults stay out of this public repository (34). Item 29's archiving
  and item 35's route are superseded by entries of 2026-10-16.
- **2026-10-13, *The owner's answers to questions 36 to 43*:** the front door's choices, which
  `ROADMAP.md` summarizes (36 to 41); the fork's 18 upstream reports wait for the owner's word
  (43).
- **2026-10-13, *CI runs once per pull request*:** `push` runs on `main` only, and pull requests
  run on every push.
- **2026-10-15, *The owner's answers to questions 44 to 49, and what a round of review
  taught*:** the porting plan for the owner's claude.ai skills (44 to 49), which `ROADMAP.md`
  and the entries of 2026-10-21 and 2026-10-26 cite, with decision 46 on `my-theme`'s palette,
  which `visual-theme` and the 2026-11-16 entry on `visual-design` cite; `CLAUDE.md` names the
  retired synced skills (12).
- **2026-10-15, *Room for 100 skills, on both surfaces, and an exclusion list for Claude
  Code*:** descriptions of at most 250 characters (1); the exclusion list, applied by the
  bootstrap skill (2); `docx`, `xlsx`, `pptx` and `pdf` stay on, and `skill-creator` is on here
  only (3); company material goes to a private companion repository, and this one stays public
  (5); claude.ai tries for each rebuilt skill (6); four of the owner's skills retire (7).
  `docs/authoring-a-skill.md` cites its "extra effort". Its room for 100 skills and its
  replacing in place are superseded by the entry of 2026-10-16 on fifteen skills.
- **2026-10-15, *Standard v0.45.0: the skill exclusion list*:** the list in
  `skills/project-bootstrap-and-audit/assets/skill-overrides.json`, and the `exclusions` rule
  that holds this repository to it, which `CLAUDE.md` cites.
- **2026-10-15, *Release 0.1.12, after 0.1.11's files were refused*:** the `v0.1.11` tag stays
  with no release.

### Pointers in later entries

These entries name an entry now archived, or a README section now moved. They stay as written.

- **2026-11-16, *Documentation audit*:** "the last three release entries" are 0.1.28 to 0.1.30,
  in `archive:2026-11-16/decisions-releases.md`.
- **2026-11-16, *Anthropic's document skills may be adapted, from a pinned commit*:** the rule it
  supersedes is the *Inception* entry's last *Do not re-propose*.
- **2026-10-26, *The `coding` skill, wave 1 of the rebuild*,** and **2026-10-21, *The example
  checker and the trigger-test runner*:** the plan approved on 2026-10-15 is the answers to
  questions 44 to 49.
- **2026-10-19, *UTC is the stamp, local times are derived, and a check holds it*:** the entry
  of 2026-10-05 it names is archived.
- **2026-10-16, *Fifteen skills made of modules, in place of a hundred skills*:** "the
  2026-10-15 entry" and "answer 7" are *Room for 100 skills*; "decision 33" is in the answers
  to questions 19 to 35.
- **2026-10-16, *The private companion repository, set up, and the empty one deleted*:** item
  29 is in the answers to questions 19 to 35, and item 5 in *Room for 100 skills*.
- **2026-10-16, *The dependency map checked on every pull request*:** "the 2026-10-05 entry" is
  *A dependency map, kept in CycloneDX*; "the 2026-10-13 answers" are questions 19 to 35; "the
  2026-10-15 entry's undecided item 3" is in *Room for 100 skills*.
- **2026-10-16, *claude.ai kept a plugin copy from 2026-09-23*:** "the 2026-09-28 entry" is
  *R22's result is taken in: the route is an uploaded skill*.
- **2026-10-16, *In a member's own settings, an uploaded skill is deleted*:** "the 2026-09-23
  entry" is *The plugin reaches the account, not cloud sessions*.
- **2026-10-16, *Skills reach cloud sessions from the release, and release 0.1.15*:** item 35
  and *The plugin reaches the account, not cloud sessions* are archived, and "the withdrawal
  runbook in the README" is now [withdrawing-a-skill.md](withdrawing-a-skill.md).

### Release-only entries

Each repeated `CHANGELOG.md`, which holds each release's contents, and the change entry it
carried, which stays above under the same date. Release entries before 2026-10-16 are in the
archived file with the rest of that period, and releases 0.1.19, 0.1.20 and 0.1.22 keep their
entries here, since each records more than its contents.

- **0.1.30**, 2026-11-16: `archive:2026-11-16/decisions-releases.md`.
- **0.1.29**, 2026-11-11: `archive:2026-11-16/decisions-releases.md`.
- **0.1.28**, 2026-11-11: `archive:2026-11-16/decisions-releases.md`.
- **0.1.27**, 2026-11-11: `archive:2026-11-16/decisions-releases.md`.
- **0.1.26**, 2026-11-11: `archive:2026-11-16/decisions-releases.md`.
- **0.1.25**, 2026-11-03: `archive:2026-11-16/decisions-releases.md`. Its open item, the
  owner's claude.ai tries of `ci-workflows` and `ci-speed`, has no later record.
- **0.1.24**, 2026-10-27: `archive:2026-11-16/decisions-releases.md`.
- **0.1.23**, 2026-10-26: `archive:2026-11-16/decisions-releases.md`.
- **0.1.21**, 2026-10-26: `archive:2026-11-16/decisions-releases.md`.
- **0.1.18**, 2026-10-20: `archive:2026-11-16/decisions-releases.md`.
- **0.1.17**, 2026-10-17: `archive:2026-11-16/decisions-releases.md`.

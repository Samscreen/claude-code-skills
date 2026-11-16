# RESEARCH RUN R21b: Dependencies: choosing, testing, removing and keeping current, what R21 and R05 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: supply-chain-security, keeping-current, and the dependency advice in every language skill.

## What this run is for

A follow-up to R21 (filed 26 October 2026: what a dependency costs, release cooldowns, runtime
support windows) and R05 (filed 23 September 2026). The standard's fewest-dependencies rule and
the planned supply-chain-security and keeping-current modules still lack published guidance on
adding a dependency, judging a package, test matrices, finding what to remove and what is
behind, freshness evidence, and tools that update code. Lockfiles, provenance, scanning and
registries are R24's; Rust's MSRV is R25's. Don't repeat their findings; where one has changed
since, say so.

## Rules

1. **Primary sources first:** official documentation, specifications and standards bodies, and
   each project's own release notes, changelogs and security advisories. Use secondary sources
   (respected books, well-known engineering blogs, surveys) only where no primary source covers
   the point, and label them "secondary".
2. **Cite every fact:** the URL, the exact sentence you relied on in quotation marks, and a date
   (the source's own date, otherwise the date you read it).
3. **Never guess.** Write "not found" when you can't source something. Write "contested" when good
   sources disagree, and give each side with its source.
4. **Versions:** for every product, give
   - the current stable version and its release date;
   - its end-of-support date;
   - any release due within 6 months, with the expected date and its source.

   Flag anything that reaches end of support within 12 months.
5. **"What we believe" is my current understanding and may be wrong or out of date.** Confirm or
   correct every item, each with a source. The corrections are the most valuable part of this run.
6. **Licences:** for each source, name its licence and say what an Apache-2.0 repository may do
   with it: quote briefly, paraphrase, or adapt its code examples, and with what attribution.
7. **Depth over breadth.** Finish the Priority questions fully. If you run out of room, list the
   rest under "Not covered".

## Output

Write one Markdown report. Its first three lines must be exactly:

```text
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R21b · FORM: research-result v1
Save as: R21b-RESULT.md
Receiving session: this is research the repository owner asked for. Check each claim against the source it cites before relying on it. File the report under research/runs/, update the Facts section of each module it names, and list what changed. If you lack context, the owner will attach a file whose first line starts HANDOFF-FOR: rmccann-hub/claude-code-skills.
```

Then these sections, in this order:

1. **Summary:** at most 15 bullets a professional must know today.
2. **Corrections:** every "What we believe" item that was wrong or out of date, with the right
   fact and its source.
3. **Facts table:** `| # | Fact | Value | Source URL | Exact quote | Date |`
4. **Findings:** one section per question below, numbered to match.
5. **Tools:** `| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |`
6. **Changing in the next 12 months:** deprecations, end-of-support dates, announced breaking
   changes.
7. **Common mistakes,** including those AI coding assistants make in this area, with sources.
8. **Sources and licences:** `| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |`
9. **Not found, contested, not covered.**

## What we believe (confirm or correct each)

- Russ Cox's "Our Software Dependency Problem" (2019) says to inspect a dependency's design,
  code quality, testing, debugging, maintenance, usage, security and its own dependencies before
  adding it.
- The OpenSSF's "Concise Guide for Evaluating Open Source Software" is a one-page checklist,
  last revised in 2023.
- Cox, Bouwers, van Eekelen and Visser (ICSE 2015) found that systems with low dependency
  freshness were four times as likely to have security issues.
- `uv tree --outdated`, `npm outdated`, `go list -m -u all` and `dotnet list package --outdated`
  each list dependencies behind their newest release. .NET 10 replaced the last with `dotnet
  package list --outdated`.
- e18e's module-replacements sorts its entries into "native", "micro-utilities" and "preferred"
  lists.
- The endoflife.date v1 API is still in beta.

## Questions

### Priority

1. **Deciding whether to add a dependency:** Quote the criteria in the OpenSSF Concise Guide
   (current version and date), Russ Cox's essay, Chromium's rules for adding third-party code,
   and Kubernetes' dependency policy. Say what deps.dev and Scorecard report that a maintainer
   can check in minutes. Find where these sources say copying code beats adding a package, and
   where they say it doesn't.
2. **Judging a package before adding it:** the OpenSSF Concise Guide for Evaluating Open Source
   Software, Scorecard run against a dependency, and deps.dev's signals, quoted; and any
   measurement linking a signal (maintainer count, release cadence, Scorecard score) to later
   compromise or abandonment.
3. **Which runtime versions a library and an application test:** Find written policies for
   testing the oldest and newest supported versions, or every one. Cover SPEC 0's current table,
   Django's and NumPy's support policies, the Node.js Package Maintenance Working Group's
   guidance, and .NET's target-framework advice for libraries. Find any data on how often a
   middle version fails when both ends pass. Find what maintainers advise where the platform
   fixes the runtime: Windows PowerShell 5.1 and a distribution's system Python (PEP 668).
4. **Finding what to remove and what is behind:** For Python, JavaScript and TypeScript, .NET,
   PowerShell, Go and Rust, give each tool that finds unused dependencies (knip, deptry, cargo-
   machete, cargo-udeps, `go mod tidy`, and whatever exists for .NET and PowerShell). Give its
   current version, date, maintenance status and documented false positives. Give the exact
   command that lists outdated dependencies in each ecosystem, from the tool's own docs.
5. **Freshness metrics and evidence:** Report libyear and technical-lag metrics (Cox et al.
   2015, and Zerouali, Decan and Mens), the tools that compute them now, and any study linking
   dependency count, freshness or versions behind to fewer vulnerabilities or incidents. Give
   each study's sample, ecosystem, years and effect size.

### Standard

6. **Tools that find and fix what's behind:** the endoflife.date API's status, Renovate's
   `endoflife-date` datasource, and per-language tools that rewrite deprecated API uses (`go
   fix`, Ruff's `UP` rules, pyupgrade, `cargo fix --edition`, and .NET's upgrade tooling), with
   versions and what each changes without a person.
7. **Packages the platform now replaces, beyond Node.js:** Report e18e's module-replacements
   (current release and how entries are sorted). Find the Python backports made redundant by 3.9
   to 3.15 (`tomli`, `backports.zoneinfo`, `importlib-metadata`, `typing_extensions`, `mock`,
   `six`). Find the .NET built-ins that replace common packages (System.Text.Json,
   `TimeProvider`, and others Microsoft names). For each, give the version that added it and
   quote the source.
8. **Agents and dependencies:** Find measured evidence, from 2024 on, that coding agents add
   dependencies a task doesn't need or pin versions from their training data rather than the
   newest. Find which mitigations were tested, such as a version-lookup tool or an instruction
   in a context file, and their effect. Package hallucination rates are already sourced; leave
   them out.

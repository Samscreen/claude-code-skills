# RESEARCH RUN R03b: Code style and types, what R03 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: code-style, types.

## What this run is for

A follow-up. R03 was filed on 23 September 2026. It covered code style, naming, comments,
formatting and types, mostly tool versions, which the language runs have since replaced. Several
of the code-style rules still have no source behind them: Boolean and unit names, function size,
comments and TODOs, and which tool checks doc comments. This run takes those, and the evidence
for typing. Languages not yet built (R13, R14, R16, R25) are out of scope. Don't repeat its
findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R03b · FORM: research-result v1
Save as: R03b-RESULT.md
Receiving session: this is research the repository owner asked for. Check each claim against the source it cites before relying on it. File the report under research/runs/, update the facts files of the categories it names, and list what changed. If you lack context, the owner will attach HANDOFF.md.
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

- .NET's Framework Design Guidelines say to name Boolean properties with an affirmative phrase,
  optionally prefixed with "Is", "Can" or "Has".
- Once file or class size is controlled for, no study shows that function length or a complexity
  score predicts defects by itself.
- One study (Muñoz Barón, Wyrich and Wagner, ESEM 2020) validated Sonar's cognitive complexity
  against measured understandability, and the correlations it found were modest.
- Ruff's pydocstyle (`D`) rules are off by default, even after Ruff 0.16 raised its default set
  to 413 rules.
- TSDoc is still a 0.x specification with no 1.0 release.

## Questions

### Priority

1. **Names for Booleans and units:** Find what primary style guides say about Boolean names
   (`is_`, `has_`, affirmative phrasing) and about putting units in names (`timeout_ms`) versus
   unit types such as Go's `time.Duration`. Read the .NET Framework Design Guidelines, Google's
   style guides, Abseil's tips, the Go wiki and the Rust API Guidelines. Add any controlled
   study of either. Quote each source.
2. **Function size, complexity and defects:** Find peer-reviewed studies that link function
   length, nesting or complexity to defects, comprehension time or review quality. Include work
   on size as a confounder (El Emam et al. 2001), Muñoz Barón et al. 2020, and Peitek et al.'s
   2021 fMRI study. Report what was measured, the sample, the effect size, and whether the
   result held once size was controlled for.
3. **Comments and TODOs:** Find measured evidence on comments that drift from the code, such as
   Wen et al., ICPC 2019. Find evidence on self-admitted technical debt and TODOs: how often
   they are removed, how long they last, and whether a TODO linked to an issue gets resolved
   more often. Name tools that flag a stale comment, with current versions.
4. **Which tool checks doc comments:** For each language, give the rule that requires a doc
   comment on a public item, whether it's on by default, how to turn it on, and the tool's
   current version and date. Cover Ruff's `D` rules and its conventions, eslint-plugin-jsdoc,
   eslint-plugin-tsdoc and TSDoc's status, C#'s CS1591 with `GenerateDocumentationFile`,
   PSScriptAnalyzer's comment-help rule, Go's revive or staticcheck rules for exported names,
   and Rust's `missing_docs` lint level.

### Standard

5. **Style left to prompts or to tools:** Find measured evidence on how well coding agents
   follow style instructions in context files compared with a formatter or linter run by a hook
   or CI. Add what Anthropic, GitHub (Copilot custom instructions) and OpenAI (Codex
   `AGENTS.md`) advise. Report the rates and dates.
6. **Evidence that static types catch bugs:** Report what Gao, Bird and Barr (ICSE 2017, "To
   Type or Not to Type") measured, and any replication since for TypeScript, Python type hints
   or C# nullable reference types.
7. **Counting escape hatches:** Find tools that report the share of `any`, casts and ignore
   comments, and baseline files for existing errors. Cover type-coverage for TypeScript, mypy's
   reports, pyright's `--verifytypes`, basedpyright's baseline and Pyrefly's baseline, with
   versions and dates.

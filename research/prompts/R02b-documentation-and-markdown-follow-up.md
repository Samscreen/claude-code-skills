# RESEARCH RUN R02b: Documentation and Markdown, what R02 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: writing-style, prose-check, documentation.

## What this run is for

A follow-up. R02 was filed on 23 September 2026. It covered repository structure, documentation,
Markdown and file size, and ran out of search budget. Layouts, Mermaid on GitHub, docs-site
tools and where community files go have been sourced since. This run takes what is still open:
which Markdown rules a linter can check, how alerts and footnotes render outside GitHub, page
length, line wrapping, decision records and citation files. Context files' content belongs to
R01. Don't repeat its findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R02b · FORM: research-result v1
Save as: R02b-RESULT.md
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

- markdownlint rules MD001, MD003, MD004, MD013, MD022, MD025, MD031, MD032 and MD040 check
  heading order, heading style, list markers, line length, blank lines around headings, a single
  top-level heading, blank lines around fences and lists, and a language on each fence.
- GitHub's alerts (`> [!NOTE]` and four others) and footnotes are not in the GFM spec, whose
  last version is 0.29-gfm from 2019.
- GitLab, VS Code's Markdown preview and Material for MkDocs all render GitHub's alert syntax as
  alerts.
- Neither Google's nor Microsoft's developer style guide sets a page-length limit. Both ask for
  one topic per page.
- MADR 4.0.0 (17 September 2024) is still the latest MADR release, and no published guide
  prefers one file per decision over a single log file.

## Questions

### Priority

1. **What markdownlint can check:** For each structural rule in the house style (one `#` heading
   per file, no skipped levels, at most four levels, sentence case, `-` bullets, two-space and
   three-space list indents, two nesting levels at most, blank lines around blocks, a language
   on each fence, wrapping at 100 characters except tables, URLs and code), give the
   markdownlint rule ID, its default, and the config key that sets it. Read the rule docs in
   DavidAnson/markdownlint. Report the current versions and dates of `markdownlint` and
   `markdownlint-cli2`, the config file names each reads, and which house rules no built-in rule
   covers.
2. **Alerts and footnotes outside GitHub:** Read the GFM spec page, then GitLab's, Bitbucket's,
   VS Code's, Pandoc's, Docusaurus's and Zensical's or Material's docs. Say whether each renders
   `> [!NOTE]`, `[^1]` footnotes and task lists, and what a reader sees when it doesn't. Quote
   each source.
3. **How agents read long or chained documents:** Find independent evidence beyond Anthropic's
   `head -100` note: papers or benchmarks from 2024 to 2026 on agents reading long files,
   partial reads, and links followed through several files. Also find each coding agent's
   documented size limits for files it reads, such as OpenAI Codex's `project_doc_max_bytes`.
   Report what was measured, the model, the date and the effect size.
4. **Page length and splitting for human readers:** Find what the Google developer documentation
   style guide, the Microsoft Writing Style Guide, Write the Docs, GOV.UK's content design
   guidance and Diátaxis say about page length, one topic per page, tables of contents and next
   or previous links. Give exact quotes. Say where they disagree.

### Standard

5. **Line wrapping:** Report the status and version of the Semantic Line Breaks spec
   (sembr.org). Find which large projects' docs style guides choose one sentence per line, a
   fixed width or no wrapping (for example GitLab, Kubernetes and Google's Markdown style
   guide), and the reasons each gives, quoted.
6. **Decision records:** Find Nygard's 2011 format as he published it, MADR's current release
   and any 5.0 plans, and the guidance from adr.github.io, AWS Prescriptive Guidance,
   Microsoft's Azure Well-Architected Framework and the UK Government Digital Service on one
   file per decision versus a single log, and on how to mark a decision superseded.
7. **Citation files:** Find the current Citation File Format version and what GitHub's "Cite
   this repository" reads from it. Quote GitHub Docs.

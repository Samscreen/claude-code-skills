# RESEARCH RUN R09b: Python, what R09 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: python-coding, python-security.

## What this run is for

A follow-up. R09 (Python) was filed on 26 October 2026 and built into the coding skill's
`python-coding` and `python-security` modules, which already reflect Python 3.15's release, its
UTF-8 default and the supported branches. R09 ran out of room for 3.15's other language changes,
packaging and publishing, HTTP clients, Astral's ownership, and studies of assistants' Python
mistakes. This run takes those. pandas, DuckDB and Pydantic are R14's; invented package names
R24's. Don't repeat its findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R09b · FORM: research-result v1
Save as: R09b-RESULT.md
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

- OpenAI's acquisition of Astral has closed, and uv, Ruff and ty are still under MIT or
  Apache-2.0.
- ty is still in beta at version 0.0.x, though Astral aimed for 1.0 in 2026.
- requests sets no default timeout; httpx defaults to five seconds.
- pip installs PEP 735 dependency groups with `--group`, since pip 25.1.
- setuptools, hatchling and uv's build backend all write PEP 639's `License-Expression`.

## Questions

### Priority

1. **Python 3.15's language changes in everyday code:** explicit lazy imports (PEP 810),
   `frozendict` (PEP 814), sentinels (PEP 661), closed TypedDicts (PEP 728) and `TypeForm` (PEP
   747): each one's final form from What's New in 3.15, and the first release of Ruff, mypy,
   Pyrefly, pyright and ty that handles it, from their changelogs.
2. **Packaging and publishing a library:** uv's build backend (`uv_build`) against hatchling,
   setuptools and flit-core, with versions and status; PEP 639 license expressions, which
   backends write them, and what PyPI requires; PEP 735 groups in pip; and `uv publish` with
   PyPI trusted publishing, from the uv, PyPA and PyPI docs. Leave checking attestations on
   install to R24.
3. **HTTP clients and untrusted downloads:** for requests, httpx, urllib3 2.x and
   `urllib.request`: the default timeout, TLS verification, redirect handling (credentials sent
   to another host), and how to cap a response's size, with current versions and 2025 to 2026
   CVEs, from each project's docs and advisories.
4. **Astral's ownership and its tools' status:** whether OpenAI's acquisition of Astral,
   announced 2026-03-19, has closed; any license or governance change to uv, Ruff and ty, from
   Astral's and OpenAI's own announcements and each repository's LICENSE file; and ty's current
   version and release status.

### Standard

5. **What assistants get wrong in Python, measured:** published studies of deprecated or removed
   APIs and code written for the wrong Python version in generated Python (for example
   `utcnow()` or the modules PEP 594 removed), with method and rates.
6. **Hidden and bidirectional characters in Python sources:** Ruff's rules for bidirectional
   controls and confusable characters (`PLE2502`, `RUF001` to `RUF003`), whether any is on by
   default, and what CPython itself does with them (Trojan Source, CVE-2021-42574), quoted, with
   versions.

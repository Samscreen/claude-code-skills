# RESEARCH RUN R12b: C built with Meson, what R12 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: c-build, c-coding, c-security, testing-patterns.

## What this run is for

A follow-up. R12 (C built with Meson) was filed on 27 October 2026 and built the same day into
c-coding, c-build and c-security. It ran out before C unit-test frameworks, AFL++ and OSS-Fuzz,
MSVC's warnings, analysis and hardening, and studies of AI mistakes in C; this run takes those.
C++ is R25's. Don't repeat its findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R12b · FORM: research-result v1
Save as: R12b-RESULT.md
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

- `meson test` reads TAP from a test declared with `protocol : 'tap'`, and cmocka can write TAP.
- Check and µnit have had no release since 2020.
- OSS-Fuzz takes only projects with a significant user base or critical to global IT
  infrastructure; ClusterFuzzLite runs the same targets in a project's own CI.
- OpenSSF's Compiler Options Hardening Guide still covers GCC and Clang only, not MSVC.
- No published study measures the weaknesses in C code that AI assistants write.

## Questions

### Priority

1. **Unit-test frameworks for C under Meson:** cmocka, Unity, Check, Criterion and µnit: each
   one's latest release and date, recent commit activity, license, the output formats it writes
   and which `meson test` protocol reads them (`exitcode`, `tap`, `gtest`), and any WrapDB
   entry. From each project's repository and Meson's *Unit tests* page.
2. **Fuzzing beyond libFuzzer:** building one target for both libFuzzer and AFL++ from a Meson
   build (AFL++'s compilers and `LLVMFuzzerTestOneInput` support), AFL++'s current release and
   date, OSS-Fuzz's acceptance criteria and what it requires of a project, and ClusterFuzzLite
   for projects OSS-Fuzz won't take. From the AFL++ docs and google.github.io/oss-fuzz, quoted.
3. **MSVC for C:** the recommended warning level and `/analyze` with its rule sets; hardening
   (`/GS`, `/guard:cf`, `/CETCOMPAT`, `/DYNAMICBASE`, `/HIGHENTROPYVA`, `/sdl`, `/Qspectre`) and
   which are on by default; `/fsanitize=address` for C and what MSVC lacks against UBSan; and
   how each reaches a Meson build (`b_sanitize`, `b_vscrt`, `get_supported_arguments`). From
   Microsoft Learn and Meson's docs, and whether OpenSSF's guide now covers MSVC.
4. **AI assistants and C:** published studies that measured weaknesses in AI-generated C, such
   as Pearce et al., "Asleep at the Keyboard?" (IEEE S&P 2022), and later ones: models, sample
   size, CWE classes found and their rates, quoted from the papers.

### Standard

5. **Distribution hardening since R12:** the flags Ubuntu 26.04 LTS's GCC builds in, and RHEL
   10's build flags, each from its own documentation; whether either now adds `-ftrivial-auto-
   var-init` or `-fzero-call-used-regs`.
6. **References c-security cites:** whether the SEI CERT C Coding Standard wiki is still
   maintained (last edits, any new edition), and whether MITRE has published a 2026 CWE Top 25,
   with the C weaknesses' ranks.

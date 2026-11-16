# RESEARCH RUN R30b: From user issues to fixes, what R30 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: feedback-loop, logging-and-observability, gui-testing.

## What this run is for

A follow-up. R30 (feedback in the product, crash reports, consented usage data, triage,
interfaces built to change) was filed and checked on 16 November 2026 and built into the user-
experience skill's feedback-loop module. It found no sources for open-source triage practice,
measuring a fix, release notes, Python and Qt crash reporting. This run takes those. Don't
repeat R30's findings; where one has changed since, say so. Consent for crash and usage data
moved to R18.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R30b · FORM: research-result v1
Save as: R30b-RESULT.md
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

- Mozilla, Kubernetes and GNOME each publish a triage guide covering reproduction, duplicates
  and closing the loop with the reporter.
- Python's `faulthandler` writes a native traceback on a crash but uploads nothing.
- Keep a Changelog is the most common published guidance for release notes.

## Questions

### Priority

1. **Open-source triage practice:** Mozilla's, Kubernetes', GNOME's and one other large
   project's triage guides on reproducing, labels, duplicates, stale reports and replying to the
   reporter, quoted.
2. **Crash reporting for Python and Qt apps:** `faulthandler`, Sentry's Python SDK, Qt's crash
   handling and Crashpad with Qt, with versions, and symbols for PyInstaller or Nuitka builds.
3. **Measuring whether a fix helped:** task success, time on task, error rates and support
   tickets in published practice, and A/B testing's minimum sample sizes.

### Standard

4. **Release notes:** published guidance (Keep a Changelog, GNOME's or KDE's release-note
   practice, platform store guidance) on telling users what changed.
5. **Strings and settings in one place:** resource files and settings centralization per toolkit
   (.resx, Qt's tr and .ts, gettext, Android resources).
6. **Percy and other visual-testing services:** versions, method and pricing model.

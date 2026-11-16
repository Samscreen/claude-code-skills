# RESEARCH RUN R29b: Interfaces and consistency, what R29 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: interface-patterns, command-line-interfaces, visual-theme.

## What this run is for

A follow-up. R29 (platform design languages, layout, forms, loading states and command-line
conventions) was filed and checked on 16 November 2026 and built into the user-experience skill.
It found no sources for design systems at scale, other platforms' breakpoints, empty and offline
states, UX writing, keyboard-first use, onboarding, or exit codes. This run takes those. Don't
repeat R29's findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R29b · FORM: research-result v1
Save as: R29b-RESULT.md
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

- IBM's Carbon, GitHub's Primer, Atlassian's design system and USWDS each publish usage guidance
  per component, not only code.
- Fluent 2 and Apple's HIG publish no numeric breakpoints.
- Microsoft's, Google's and Apple's writing guides all ask for sentence-case labels.
- BSD's sysexits.h codes (64 to 78) are a de facto convention for command-line exit codes.

## Questions

### Priority

1. **Design systems at scale:** what Carbon, Primer, Atlassian and USWDS hold and how each keeps
   products consistent (inventories, contribution rules, lint, Storybook-style catalogs, visual
   tests), and published evidence on what goes wrong without one.
2. **Empty, offline, partial and optimistic states:** guidance from NN/g, GOV.UK, Material and
   Apple, quoted.
3. **UX writing:** Microsoft's, Google's, Apple's, GNOME's and GOV.UK's content guides on
   labels, buttons and microcopy, and where they disagree.
4. **Keyboard-first use:** command palettes and shortcut conventions per platform (Windows,
   macOS, GNOME, KDE, the web), from the platforms' guides.

### Standard

5. **Window sizes beyond Material:** Fluent, Apple, GNOME (libadwaita breakpoints) and KDE
   guidance, and high-DPI scaling guidance per desktop.
6. **Forms research:** NN/g and Baymard on inline validation timing, required fields and error
   placement.
7. **Onboarding and changing a familiar layout:** first-run, what's-new notices and gradual
   rollout, with evidence.
8. **Exit codes beyond 0:** sysexits.h, clig.dev and GNU guidance, quoted.

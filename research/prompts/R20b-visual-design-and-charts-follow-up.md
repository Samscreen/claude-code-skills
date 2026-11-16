# RESEARCH RUN R20b: Visual design and charts, what R20 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: visual-theme, data-visualization.

## What this run is for

A follow-up. R20 (tokens, color, charting libraries, documents) was filed and checked on 16
November 2026 and built into the visual-design skill. It found no sources for choosing chart
types, dashboards, the platforms' dark-mode guidance, typography beyond Aptos, or mapping tokens
to Office themes. This run takes those. Accessible documents and WCAG belong to R18, so leave
them out. Don't repeat R20's findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R20b · FORM: research-result v1
Save as: R20b-RESULT.md
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

- The Financial Times Visual Vocabulary groups chart types by the relationship they show:
  deviation, correlation, ranking, distribution, change over time, magnitude, part-to-whole,
  spatial and flow.
- Material, Apple's HIG and Fluent each recommend dark surfaces that are dark gray rather than
  pure black.
- System font stacks (`system-ui` and its fallbacks) avoid shipping a web font for interface
  text.
- Aptos is licensed for use only with Microsoft products and can't be embedded freely in a web
  page.
- The DTCG Resolver module for themes and modes is still a draft.

## Questions

### Priority

1. **Choosing a chart type:** the FT Visual Vocabulary, Datawrapper's chart guidance, and the
   published work of Few and Tufte (cite editions), and where they agree and disagree on pies,
   dual axes, truncated axes and 3D.
2. **Dashboards and KPIs:** published guidance on dashboard layout, how many KPIs, sparklines,
   targets and comparisons, and the evidence behind it.
3. **Dark mode by platform:** what Material, Apple's HIG, Fluent and GNOME say about dark
   surfaces, elevation, saturated colors and images in dark mode, quoted.
4. **Typography:** system font stacks per platform, variable fonts' support, the SIL Open Font
   License's terms for embedding, and Aptos's licensing and availability outside Microsoft 365.

### Standard

5. **Tokens into Office themes:** ECMA-376's DrawingML `clrScheme` and font scheme, from the
   standard or Microsoft's Open XML docs, and any tool that builds an Office theme from design
   tokens.
6. **The DTCG's next modules:** the Resolver (themes and modes) and any later spec version's
   status, and Tokens Studio's current version.
7. **Common mistakes** in generated charts and themes, including those AI assistants make, with
   sources.

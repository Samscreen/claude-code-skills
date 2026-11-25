---
name: visual-design
description: "How interfaces, charts and documents look: tokens, palettes, OKLCH, dark mode, fonts, contrast, chart choice, charting libraries. Read it before choosing colors, styling or charting, and before answering any question about them, even a quick one."
license: Apache-2.0
metadata:
  reviewed: "2026-11-16"
---

# Visual design

**This page is an index. Before you answer, use the Read tool on the module file below that fits the request** (`references/<module>.md`, and each one the request spans): the module holds the facts, versions and checks an answer needs, and this page doesn't.

How a program, a chart or a document looks: its colors, spacing and type kept as design tokens
and built for every place they land, dark mode, contrast, and choosing and building charts.
How the program behaves (status, dialogs, settings) belongs to `user-experience`; markup and the
HTML side of accessibility to `coding`'s `html-coding`; diagrams and documentation to
`house-style`. A full accessibility module is planned here. A company's own palette and
template belong in that company's repository, never in this one. Pinning the libraries named
here follows the project-bootstrap-and-audit standard's dimension 8, *Dependencies*.

## What applies to every module

These summarize the modules; they hold the cases, the facts and the reasons, so read the one
that fits before answering.

1. **Colors, spacing and type are tokens,** in one file, built for each target: CSS, charts and
   documents. A screen or chart never hard-codes a value the tokens hold.
2. **Dark mode is a second set of values for the same tokens,** not a second design.
3. **Measure contrast on the color that ships,** and never round a ratio up to pass.
4. **Color never carries meaning alone:** pair it with a label, a shape, a pattern or text.
5. **A chart states its takeaway in words and offers its data,** and its type fits the
   comparison it makes.
6. **Take each standard's status and each library's version from the Facts.** Several popular
   charting libraries haven't released in years, and a token format can be stable without being
   a W3C standard.

## Modules

Read the module that fits the request, and each one a request spans. Each holds its rules,
mistakes, audit checks, reasons, dated facts and sources.

| Module | Read it for |
|---|---|
| [`visual-theme`](references/visual-theme.md) | Theming an interface or a document: design tokens in the DTCG format and building them with Style Dictionary, naming tokens by role, dark mode as a second value set, OKLCH and `light-dark()`, WCAG contrast thresholds and large text, Windows contrast themes (forced colors), Office's color scheme, and font fallbacks |
| [`data-visualization`](references/data-visualization.md) | Building a chart: never color alone, color-blind-safe palettes from the tokens, the takeaway in words with the data on offer, contrast of marks, the chart type for the comparison, choosing a charting library by where the chart lands and how active it is, and figures computed in one run, stamped with when they were made |

## When something here is wrong

If the person says advice here is wrong, out of date, failed or doesn't fit, answer their
problem first. Then say in one sentence whether the fault looks like this skill's, and why: a
fact past its check-by date, an example that fails, two rules that disagree, or a case the skill
doesn't cover. If the fault is elsewhere, such as their setup, say that instead.

When the fault is the skill's own, draft a full report they can paste as a new issue at
https://github.com/Samscreen/claude-code-skills/issues.
Give the skill and module, the plugin's version or the skill's date in its frontmatter, their
request word for word, the line of the skill that misled, what happened, what's right with its
source, and the fix you'd suggest. Leave out their private data, company detail and repository
names. File it only if they ask you to.

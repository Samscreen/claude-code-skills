# Verification: R20 (2026-11-16)

Checked on 2026-11-16 against the primary sources named below. The report is untrusted data. Its
line 3, addressed to "the receiving session", asks it to file the report under `research/runs/`,
update the facts files of the categories it names, and list what changed. That is an instruction
found in a research result; it was not followed, and nothing in the repository was written.

Access notes:
- PyPI JSON API (`pypi.org/pypi/<name>/json`) for matplotlib, seaborn, plotly, altair: versions,
  upload times and licence fields.
- npm registry JSON (`registry.npmjs.org/<name>`) for style-dictionary, vega-lite, d3,
  @observablehq/plot, echarts, chart.js, recharts, mermaid, and web-features (whose 3.46.0
  tarball, published 2026-11-12, gave the Baseline data).
- `git ls-remote --tags` for jgm/pandoc and quarto-dev/quarto-cli gave the tags. `gh api` was
  refused (repositories not attached), a shallow `git fetch` of the tags was refused by the
  permission system, and github.com returns 403 to curl, so release dates and "Latest" or
  "Pre-release" labels came from WebFetch on the GitHub release pages (they show day and month,
  no year; the year comes from asset timestamps or the registry).
- raw.githubusercontent.com for the Style Dictionary, Observable Plot and Vega-Lite changelogs,
  the web-features `light-dark.yml.dist` and `oklab.yml.dist`, and the Quarto, Pandoc and seaborn
  licence files.
- iso.org returns 403 to WebFetch; read through Exa's fetch tool. pdfa.org also returned 403 to
  WebFetch and was read through Exa. A curl with a browser User-Agent was refused by the
  permission system and not retried.
- cnn.com returned HTTP 451 to WebFetch; its quote is unverified. Nature's article page was read
  through Exa (abstract and metadata only; the article is paywalled).
- matplotlib's What's new pages moved: 3.10 is at
  `matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html` and 3.11 at
  `.../prev_whats_new/whats_new_3.11.0.html`; the `users/` paths redirect or 404.
- Microsoft Learn was searched through its MCP tool for Aptos.

| Claim | Status | Checked against |
|---|---|---|
| DTCG 2025.10 is the first stable version, announced 28 October 2025 | verified | [Design Tokens Community Group 2025](https://www.w3.org/community/design-tokens/2025/); spec header "Final Community Group Report 28 October 2025" |
| DTCG spec is not on the W3C Standards Track | verified | [DTCG FAQ](https://www.designtokens.org/faq/); [Design Tokens Technical Reports 2025.10](https://www.designtokens.org/tr/2025.10/) |
| File extensions `.tokens` and `.tokens.json` (report: secondary) | verified (now primary) | [Format Module 2025.10 §4.2](https://www.designtokens.org/tr/2025.10/format/) |
| Media type `application/design-tokens+json` (report: secondary) | verified (now primary); it is a SHOULD | [Format Module 2025.10 §4.1](https://www.designtokens.org/tr/2025.10/format/) |
| 2025.10 colours are objects (`colorSpace`, `components`, `alpha`, optional `hex`) | verified with a correction: defined in the Color module; `colorSpace` and `components` required, `alpha` optional (assumed 1 when omitted), `hex` optional, a 6-digit CSS hex fallback; 14 colour spaces | [Color Module 2025.10 §4.1](https://www.designtokens.org/tr/2025.10/color/) |
| 2025.10 dimensions are objects `{ "value": 8, "unit": "px" }` | verified with a correction: `unit` is limited to `"px"` or `"rem"` | [Format Module 2025.10, dimension](https://www.designtokens.org/tr/2025.10/format/) |
| 2025.10 adds `$root` and `$ref` (report: secondary) | verified (now primary) | [Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/) |
| DTCG Resolver module's final status "not found" | verified (added): published as "Design Tokens Resolver Module 2025.10", Final Community Group Report, 28 October 2025, "considered stable" | [Resolver Module 2025.10](https://www.designtokens.org/tr/2025.10/resolver/) |
| Style Dictionary 5.3.0 adds DTCG structured colour, 14 colour spaces, `color/oklch` and `color/oklab` | verified (5.3.0 published 2026-02-09) | [Style Dictionary CHANGELOG](https://raw.githubusercontent.com/style-dictionary/style-dictionary/main/CHANGELOG.md); npm |
| Style Dictionary 5.4.0 adds dimension object values | verified (published 2026-03-22) | same |
| Style Dictionary 5.7.0 adds duration tokens and `$root` naming | verified (published 2026-10-16) | same |
| Style Dictionary 5.7.1 published 24 October 2026; "5.7.x" current | verified with a correction: 5.7.1 was 2026-10-24, but the latest is **5.8.0, 2026-11-03** | [npm registry](https://registry.npmjs.org/style-dictionary) |
| Style Dictionary docs say 2025.10 support is "a work in progress in v5" (report: secondary) | verified (now primary) | [Style Dictionary: DTCG](https://styledictionary.com/info/dtcg/) |
| `oklch()` Baseline Widely available "since May 2023" | verified with a correction: MDN shows Widely available, but May 2023 is the newly-available date (2023-05-09); Widely available since **2025-11-09** | [MDN oklch()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch); [web-features oklab.yml.dist](https://raw.githubusercontent.com/web-platform-dx/web-features/main/features/oklab.yml.dist) |
| `light-dark()` Baseline 2024, Newly available 13 May 2024 | verified | [MDN light-dark()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark); web-features `baseline_low_date: 2024-05-13` |
| `light-dark()` "has only just reached" Widely available, around 13 November 2026 | contradicted: the 30-month date computes to 2026-11-13, but on 2026-11-16 web-features (main and npm 3.46.0 of 2026-11-12) still says `baseline: low` with no high date, and MDN still shows "Baseline 2024 Newly available". Treat it as Newly available until the data changes | [web-features light-dark.yml.dist](https://raw.githubusercontent.com/web-platform-dx/web-features/main/features/light-dark.yml.dist); MDN |
| `light-dark()` accepts images as well as colours | verified (web-features' compat key covers colours only) | MDN light-dark() |
| `light-dark()` needs `color-scheme: light dark` (report: secondary) | verified (now primary) | MDN light-dark() |
| WCAG 2.2 1.4.1 Use of Color (A) | verified | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (W3C Recommendation 12 December 2024) |
| WCAG 2.2 1.4.3 Contrast (Minimum) (AA): 4.5:1, large text 3:1 | verified | same |
| WCAG 2.2 1.4.11 Non-text Contrast (AA): 3:1 for UI components and graphical objects | verified | same |
| Understanding 1.4.3: ratios are thresholds; 4.499:1 fails | verified | [Understanding SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) |
| matplotlib 3.10 adds 'petroff10' ("New more-accessible color cycle") | verified | [What's new in Matplotlib 3.10.0 (December 13, 2024)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html) |
| matplotlib 3.10 adds "berlin", "managua", "vanimo" dark-mode diverging colormaps | verified | same |
| matplotlib 3.11 adds Okabe-Ito sequence (`okabe_ito`) and 'petroff6', 'petroff8' | verified | [What's new in Matplotlib 3.11.0 (Jun 11, 2026)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html) |
| matplotlib 3.11.0 on 11 June 2026; 3.11.2 on 11 September 2026 | verified (PyPI upload 3.11.0 2026-06-12T02:27Z; 3.11.2 2026-09-11T19:02Z) | [matplotlib.org](https://matplotlib.org/); PyPI |
| Wong 2011 (not verified in report) | verified (added): Bang Wong, "Points of view: Color blindness", Nature Methods 8, 441, published 27 May 2011, DOI 10.1038/nmeth.1618; Author Correction 14 July 2023 (10.1038/s41592-023-01974-0); Figure 2 "Colors optimized for color-blind individuals" | [Nature Methods](https://www.nature.com/articles/nmeth.1618) |
| viridis (not verified in report) | verified (added): designed by van der Walt and Smith as "option D", default colormap from matplotlib 2.0, CC0 | [mpl colormaps](https://bids.github.io/colormap/) |
| seaborn latest 0.13.2, 25 January 2024 | verified | PyPI |
| D3 latest 7.9.0; no release since March 2024 | contradicted: **7.9.2, 2026-11-03** (7.9.1 the same day); 7.9.2 widens the d3-* dependency ranges to caret ranges | [npm registry](https://registry.npmjs.org/d3) |
| plotly.py latest 6.9.0 (9 July 2026); "plotly 6" confirmed | contradicted: **7.1.0, 2026-09-15**; 7.0.0 on 2026-08-25; 6.9.0 was 2026-07-09 | PyPI |
| Altair 6.3.0, 15 September 2026 | verified | PyPI |
| Altair 6 compiles against Vega-Lite 6 | verified ("version 6.1.0"); Altair 6.0.0 on PyPI 2025-11-12 | [Altair v6.0.0 release](https://github.com/vega/altair/releases/tag/v6.0.0) |
| Vega-Lite 6.5.0, 8 October 2026 | verified | npm; [Vega-Lite CHANGELOG](https://raw.githubusercontent.com/vega/vega-lite/main/CHANGELOG.md) |
| Observable Plot 0.6.19, 5 November 2026 | verified | npm |
| Observable Plot 0.6.18 adds `light-dark(…)` and a top-level legend option | verified; 0.6.18 released 2026-11-03 | [Plot v0.6.18 release](https://github.com/observablehq/plot/releases/tag/v0.6.18); [Plot CHANGELOG](https://raw.githubusercontent.com/observablehq/plot/main/CHANGELOG.md) |
| ECharts 6.0.0 30 July 2025; 6.1.0 current (19 May 2026) | verified | npm |
| ECharts 6 new default theme and dark mode | verified | [ECharts 6 features](https://echarts.apache.org/handbook/en/basics/release-note/v6-feature/) |
| Chart.js 4.6.1, 22 October 2026 | verified | npm |
| Recharts 3.10.1 (25 July 2026), 3.11 in canary | verified (canary tag 3.11.0-canary.9) | npm |
| Recharts 3.0.0 (23 June 2025) turns on `accessibilityLayer` by default | verified | [Recharts v3.0.0 release](https://github.com/recharts/recharts/releases/tag/v3.0.0); npm |
| Mermaid 12.3.0, 3 November 2026 | verified (an alpha tag 13.0.0-alpha.3 exists) | npm |
| Pandoc 3.14 current | verified; dates differ: GitHub release 12 Nov, pandoc.org "pandoc 3.14 (2026-11-10)" | [pandoc 3.14 release](https://github.com/jgm/pandoc/releases/tag/3.14); [Pandoc releases](https://pandoc.org/releases.html); git ls-remote |
| Pandoc 3.11 adds `--math-method`, deprecates per-engine flags, MathML default | verified (discussion posted Aug 29, 2026) | [pandoc 3.11 discussion](https://github.com/jgm/pandoc/discussions/11835); pandoc.org releases |
| Pandoc 3.8.3 adds asciidoc, pptx, xlsx readers | verified (posted Dec 1, 2025) | [pandoc 3.8.3 discussion](https://github.com/jgm/pandoc/discussions/11313) |
| Quarto 1.11.9 stable, 30 October 2026 | verified ("Latest") | [quarto-cli releases](https://github.com/quarto-dev/quarto-cli/releases); git ls-remote |
| Quarto 1.12 pre-release since 2 November 2026 (quote "Published November 2, 2026") | verified with a correction: v1.12.0 pre-release on 2 Nov, v1.12.1 on 6 Nov, v1.12.2 on 12 Nov; the page now reads "Published November 12, 2026", so the report's quote no longer matches | [Quarto 1.12 Pre-Release](https://quarto.org/docs/prerelease/1.12/index.html) |
| PDF/UA-2 is ISO 14289-2:2024, published 13 March 2024 | verified (60.60 2024-03-13, Edition 1) | [ISO 14289-2:2024](https://www.iso.org/standard/82278.html) |
| PDF/UA-2 is for PDF 2.0, based on WTPDF | verified | [PDF Association: ISO 14289](https://pdfa.org/resource/iso-14289-pdfua/) |
| PDF/UA-2 does not replace PDF/UA-1 | secondary only (iText); pdfa.org lists both parts as the current family without saying so | iText blog |
| PDF 2.0 is ISO 32000-2:2020, 2020-12, Edition 2, replacing 2017 | verified with a correction: 60.60 was 2020-12-11, but the current stage is **90.93 "International Standard confirmed" (2026-03-05)** | [ISO 32000-2:2020](https://www.iso.org/standard/75839.html) |
| Aptos announced 13 July 2023, replacing Calibri | verified | [Microsoft Design blog](https://medium.com/microsoft-design/a-change-of-typeface-microsofts-new-default-font-has-arrived-f200eb16718d); [Aptos font family](https://learn.microsoft.com/typography/font-list/aptos); CNBC |
| Aptos wide rollout from December 2023 (CNN) | unverifiable: cnn.com returned 451. Microsoft's post says only "over the next few months" | Microsoft Design blog |
| Aptos available outside Microsoft 365 ("not found") | verified (added): Microsoft Learn links "Download Microsoft Aptos Fonts" (microsoft.com download id 106087) and points to font licensing for redistribution | [Aptos font family](https://learn.microsoft.com/typography/font-list/aptos) |
| Pandoc 3.8 adds `xml` AST format and `--syntax-highlighting` | unverifiable: not checked (the pandoc.org changelog is 788 KB; the 3.8 section wasn't reached) | — |
| PDF/UA free from PDF Association since 12 August 2024 | secondary only: pdfa.org says ISO 14289-1 is "available at no cost exclusively from the PDF Association"; the date wasn't seen | pdfa.org |

Counts: 43 verified (including claims the report marked secondary or not found, now confirmed at
a primary source), 6 verified with a correction, 3 contradicted, 2 unverifiable, 2 secondary
only.

## Exact quotes for facts rows

| Fact | URL | Exact quote |
|---|---|---|
| DTCG first stable version | https://www.w3.org/community/design-tokens/2025/ | "The Design Tokens Community Group today announced the first stable version of the Design Tokens Specification (2025.10)" |
| DTCG not a W3C Standard | https://www.designtokens.org/tr/2025.10/ | "It is not a W3C Standard nor is it on the W3C Standards Track." |
| DTCG stable | https://www.designtokens.org/tr/2025.10/ | "This specification is considered stable." |
| DTCG FAQ status | https://www.designtokens.org/faq/ | "The DTCG spec is not on the W3C Standards Track" |
| DTCG file extensions | https://www.designtokens.org/tr/2025.10/format/ | "The following file extensions are recommended by this spec:" (then `.tokens`, `.tokens.json`) |
| DTCG media type | https://www.designtokens.org/tr/2025.10/format/ | "the following MIME type SHOULD be used for design token files: application/design-tokens+json" |
| DTCG dimension | https://www.designtokens.org/tr/2025.10/format/ | "The value MUST be an object containing a numeric value (integer or floating-point) and unit of measurement (\"px\" or \"rem\")." (page has straight double quotes around px and rem) |
| DTCG `$root` | https://www.designtokens.org/tr/2025.10/format/ | "Groups support root tokens using the reserved name $root as the token name:" |
| DTCG `$ref` | https://www.designtokens.org/tr/2025.10/format/ | "Tools MUST support JSON Pointer references as defined by [rfc6901], using the $ref property:" |
| DTCG colour hex | https://www.designtokens.org/tr/2025.10/color/ | "A string that represents a fallback value of the color." |
| Style Dictionary 5.3.0 colour | https://raw.githubusercontent.com/style-dictionary/style-dictionary/main/CHANGELOG.md | "Add support for DTCG v2025.10 structured color format in color transformers." |
| Style Dictionary 5.3.0 oklch | same | "New `color/oklch` transformer - outputs modern CSS `oklch()` function" |
| Style Dictionary 5.4.0 dimension | same | "Add support for DTCG v2025.10 dimension token type object value" (the source links "DTCG v2025.10") |
| Style Dictionary 5.7.0 duration | same | "Add support for DTCG v2025.10 `duration` token values" |
| Style Dictionary DTCG support unfinished | https://styledictionary.com/info/dtcg/ | "the latest format 2025.10 does not have full support yet in Style Dictionary" and "This is a work in progress in v5" |
| oklch() Widely available | https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch | "It’s been available across browsers since May 2023." (U+2019 apostrophe; the report's straight apostrophe doesn't match) |
| oklch() Widely-available date | https://raw.githubusercontent.com/web-platform-dx/web-features/main/features/oklab.yml.dist | "baseline_high_date: 2025-11-09" |
| light-dark() Newly available | https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark | "Since May 2024, this feature works across the latest devices and browser versions." |
| light-dark() low date | https://raw.githubusercontent.com/web-platform-dx/web-features/main/features/light-dark.yml.dist | "baseline_low_date: 2024-05-13" |
| light-dark() images | MDN light-dark() | "The light-dark() CSS function accepts two colors or two images" |
| light-dark() needs color-scheme | MDN light-dark() | "To enable support for the light-dark() color function, the color-scheme must have a value of light dark" |
| WCAG 1.4.1 | https://www.w3.org/TR/WCAG22/ | "Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element." |
| WCAG 1.4.3 | https://www.w3.org/TR/WCAG22/ | "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for the following:" |
| WCAG 1.4.3 large text | https://www.w3.org/TR/WCAG22/ | "Large-scale text and images of large-scale text have a contrast ratio of at least 3:1" |
| WCAG 1.4.11 | https://www.w3.org/TR/WCAG22/ | "The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s):" |
| WCAG 1.4.11 graphics | https://www.w3.org/TR/WCAG22/ | "Parts of graphics required to understand the content, except when a particular presentation of graphics is essential to the information being conveyed." |
| Contrast is a threshold | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html | "the computed values should not be rounded (e.g., 4.499:1 would not meet the 4.5:1 threshold)" |
| matplotlib petroff10 | https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html | "It aims to be both generally pleasing aesthetically and colorblind accessible" |
| matplotlib dark-mode colormaps | same | "Three diverging colormaps have been added: \"berlin\", \"managua\", and \"vanimo\"." (straight double quotes on the page) |
| matplotlib Okabe-Ito | https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html | "Matplotlib now includes the Okabe-Ito color sequence." |
| matplotlib Okabe-Ito use | same | "Its colors remain distinguishable for common forms of color-vision deficiency and when printed." |
| matplotlib petroff6/8 | same | "The six and eight color accessible Petroff color cycles are named 'petroff6' and 'petroff8'." |
| matplotlib 3.11.0 date | https://matplotlib.org/ | "Jun 11, 2026 Matplotlib 3.11.0 Released" |
| Wong 2011 | https://www.nature.com/articles/nmeth.1618 | "Here I offer guidelines to make graphics accessible to those with color vision deficiencies." |
| viridis | https://bids.github.io/colormap/ | "\"option D\" (now called \"viridis\") will be the new default colormap in matplotlib 2.0" |
| Altair 6 on Vega-Lite 6 | https://github.com/vega/altair/releases/tag/v6.0.0 | "we now compile against Vega-Lite version 6 (to be specific, version 6.1.0)" |
| Vega-Lite 6.5.0 | https://raw.githubusercontent.com/vega/vega-lite/main/CHANGELOG.md | "# [6.5.0](https://github.com/vega/vega-lite/compare/v6.4.3...v6.5.0) (2026-10-08)" |
| Plot light-dark | https://github.com/observablehq/plot/releases/tag/v0.6.18 | "Add support for `light-dark(…)` color syntax." (U+2026 ellipsis) |
| Plot 0.6.18 date | https://raw.githubusercontent.com/observablehq/plot/main/CHANGELOG.md | "Released November 3, 2026." |
| Recharts 3 accessibility | https://github.com/recharts/recharts/releases/tag/v3.0.0 | "`accessibilityLayer` is now on on all polar and cartesian charts by default." |
| ECharts 6 dark mode | https://echarts.apache.org/handbook/en/basics/release-note/v6-feature/ | "Dark Mode Support" |
| Pandoc 3.14 | https://github.com/jgm/pandoc/releases/tag/3.14 | "I'm pleased to announce the release of pandoc 3.14, available in the usual places:" |
| Pandoc 3.14 date (changelog) | https://pandoc.org/releases.html | "pandoc 3.14 (2026-11-10)" |
| Pandoc 3.11 math | https://pandoc.org/releases.html | "This replaces (now deprecated but still functional) options `--mathml`, `--mathjax`, `--gladtex`, `--katex`, `--webtex`." |
| Pandoc 3.11 MathML default | https://pandoc.org/releases.html | "Make `mathml` the default math-method." |
| Pandoc 3.8.3 readers | https://github.com/jgm/pandoc/discussions/11313 | "This release adds three new input formats (asciidoc, pptx, and xlsx)" |
| Quarto 1.12 pre-release | https://quarto.org/docs/prerelease/1.12/index.html | "Quarto 1.12 Pre-Release" and "Published November 12, 2026" |
| PDF/UA-2 published | https://www.iso.org/standard/82278.html | "60.60 2024-03-13" and "International Standard published" |
| PDF/UA-2 basis | https://pdfa.org/resource/iso-14289-pdfua/ | "ISO 14289-2:2024 – PDF/UA-2, completely revised and enhanced for PDF 2.0 (ISO 32000-2). This document is based on the PDF Association’s WTPDF specification." (U+2013 dash, U+2019 apostrophe) |
| PDF 2.0 confirmed | https://www.iso.org/standard/75839.html | "This publication was last reviewed and confirmed in 2026. Therefore this version remains current." |
| Aptos announcement | https://medium.com/microsoft-design/a-change-of-typeface-microsofts-new-default-font-has-arrived-f200eb16718d | "Aptos will start appearing as the new default font across Word, Outlook, PowerPoint and Excel for hundreds of millions of users" |
| Aptos replaces Calibri | https://learn.microsoft.com/typography/font-list/aptos | "Type designer Steve Matteson designed Aptos for Microsoft as a new default Office font to replace Calibri." |

## Versions found from registries

| Tool | Current version | Released | Source |
|---|---|---|---|
| matplotlib | 3.11.2 | 2026-09-11 | PyPI |
| seaborn | 0.13.2 | 2024-01-25 | PyPI |
| plotly | **7.1.0** | 2026-09-15 | PyPI (7.0.0 on 2026-08-25) |
| altair | 6.3.0 | 2026-09-15 | PyPI |
| style-dictionary | **5.8.0** | 2026-11-03 | npm |
| vega-lite | 6.5.0 | 2026-10-08 | npm |
| d3 | **7.9.2** | 2026-11-03 | npm |
| @observablehq/plot | 0.6.19 | 2026-11-05 | npm |
| echarts | 6.1.0 | 2026-05-19 | npm |
| chart.js | 4.6.1 | 2026-10-22 | npm |
| recharts | 3.10.1 | 2026-07-25 | npm (canary 3.11.0-canary.9) |
| mermaid | 12.3.0 | 2026-11-03 | npm (alpha 13.0.0-alpha.3) |
| pandoc | 3.14 | 2026-11-12 (GitHub release); 2026-11-10 (pandoc.org) | git ls-remote; GitHub release page |
| quarto-cli | 1.11.9 stable | 2026-10-30 | git ls-remote; GitHub releases (1.12.2 pre-release, 2026-11-12) |
| web-features (Baseline data) | 3.46.0 | 2026-11-12 | npm |

## Licences

| Source | Licence as stated | What an Apache-2.0 repository may do |
|---|---|---|
| DTCG specs (designtokens.org/tr/2025.10/) | "published by the Design Tokens Community Group under the W3C Community Final Specification Agreement (FSA)" | Quote briefly with attribution; paraphrase. Copying example JSON: check the FSA's copyright terms first |
| MDN Web Docs | Prose "CC-BY-SA v2.5 or any later version"; code samples added on or after 2010-08-20 "in the public domain CC0" | Quote briefly with attribution to Mozilla Contributors; paraphrase; adapt CC0 code freely |
| WCAG 2.2 | "W3C liability, trademark and document use rules apply" | Quote briefly with a link; paraphrase |
| matplotlib | "License agreement for matplotlib versions 1.3.0 and later" (PSF-based; PyPI classifier Python Software Foundation License) | Quote, paraphrase, adapt code with its copyright notice |
| seaborn | BSD (LICENSE.md "Copyright (c) 2012-2023, Michael L. Waskom"; PyPI classifier BSD License) | Quote, paraphrase, adapt with notice |
| plotly | MIT (PyPI) | Quote, paraphrase, adapt with notice |
| altair | BSD (PyPI classifier) | Quote, paraphrase, adapt with notice |
| vega-lite | BSD-3-Clause (npm) | Quote, paraphrase, adapt with notice |
| d3, @observablehq/plot | ISC (npm) | Quote, paraphrase, adapt with notice |
| echarts, style-dictionary | Apache-2.0 (npm) | Quote, paraphrase, adapt; keep NOTICE |
| chart.js, recharts, mermaid | MIT (npm) | Quote, paraphrase, adapt with notice |
| Pandoc | "this code is released under the [GPL], version 2 or later" (COPYRIGHT) | Quote documentation briefly; paraphrase; don't copy code; calling the CLI is fine |
| Quarto CLI | MIT ("Copyright (c) 2020-2024 Posit Software, PBC", COPYING.md) | Quote, paraphrase, adapt with notice |
| viridis colormaps | "under a CC0 \"no rights reserved\" license" (bids.github.io/colormap) | Anything; attribution courteous |
| ISO 14289-2, ISO 32000-2 | ISO copyright, sold | Cite number and bibliographic data only |
| Nature Methods (Wong 2011) | Publisher copyright, paywalled | Cite; paraphrase; the eight palette colours are facts, but copy them from matplotlib's Okabe-Ito data rather than the figure |
| Microsoft Learn, Microsoft Design blog, CNBC, PDF Association | Not stated on the pages read; treat as all rights reserved | Quote briefly with URL; paraphrase |

## Repository facts this contradicts

Searched `git -C /home/user/claude-code-skills grep -n` over `skills/` for matplotlib, Pandoc,
Quarto, Mermaid, WCAG, contrast, OKLCH, light-dark, Aptos, design token, and for Baseline,
color-scheme, plotly, altair, seaborn, recharts, echarts, chart.js, vega, style-dictionary, d3
and PDF/UA.

None now wrong. The rows that touch this report's claims agree with the sources:

- `skills/coding/references/html-coding.md`, `web-wcag-contrast` (4.5:1, large text 3:1) and
  `web-wcag-nontext` (3:1 against adjacent colours) match WCAG 2.2 as read today; `web-wcag22`
  (Recommendation 12 December 2024) matches.
- `skills/coding/references/html-coding.md`, `web-baseline` (Widely available 30 months on)
  matches the arithmetic used above.
- `skills/house-style/references/documentation.md`, `docs-mermaid-12` (Mermaid at 12.3.0)
  matches npm (12.3.0, 2026-11-03).

No Facts row in `skills/` names matplotlib, Pandoc, Quarto, OKLCH, `light-dark()`, Aptos,
design tokens or any of the charting libraries, so the contradicted claims (D3, plotly,
`light-dark()` status) touch no existing row. `html-coding.md` lines 9 and 87 to 88 already
defer design tokens to a planned visual-design skill and tell readers to check a feature's
Baseline status on MDN, which is the right guard for `light-dark()`.

---

# R20: Visual design, data visualization, documents and output formats

Most of the "What we believe" list is out of date. The design-token claim is right, though it needs a status caveat. The library versions are not: matplotlib is now 3.11, Altair is 6, Recharts is 3, ECharts is 6.1, Chart.js is 4.6 and Pandoc is 3.14. Seaborn and D3 have not released since early 2024, so treat them as low-activity projects. `light-dark()` has only just reached Baseline "Widely available" (around 13 November 2026), while OKLCH has been Widely available for some time.

## TL;DR

- **Design tokens:** the DTCG Design Tokens Specification 2025.10, published 28 October 2025, is the first stable version. It is a W3C Community Group report, not a W3C Standard. Build tokens with Style Dictionary 5.x (5.7.x in October 2026), which adopted DTCG 2025.10 as its base format, though its docs still say support for 2025.10 is unfinished.
- **Versions to update now:** matplotlib 3.11.2 (September 2026), Altair 6.3.0 (September 2026), plotly.py 6.x (6.9.0 or later), Vega-Lite 6.5.0 (October 2026), ECharts 6.1.0, Chart.js 4.6.1 (October 2026), Recharts 3.10.1, Observable Plot 0.6.19 (November 2026), Pandoc 3.14 (November 2026), Quarto 1.11.9 (October 2026), Mermaid 12.3.0 (November 2026).
- **Corrections that matter for generated code:** use `light-dark()` freely only if your browser target is Baseline Widely available as of mid-November 2026 or later. Do not tell users that seaborn or D3 are actively releasing. Aptos is the Office default font, but it rolled out from December 2023 into 2024 and older installs and non-Microsoft systems may not have it.

## 1. Summary

- The DTCG specification 2025.10 is the first stable version, announced on 28 October 2025. The project's FAQ says the "DTCG spec is not on the W3C Standards Track". Call it a "W3C Community Group specification", not a "W3C standard".\[1\]
- Token files use the `.tokens` or `.tokens.json` extension and the media type `application/design-tokens+json`. In 2025.10, colours are structured objects (`colorSpace`, `components`, `alpha`, optional `hex`) and dimensions are objects (`{ "value": 8, "unit": "px" }`), not strings. These details come from secondary summaries, so check them against the specification.\[2\]
- Style Dictionary 5 supports DTCG 2025.10 piece by piece: structured colours including an `oklch` output transform (5.3.0), object dimensions (5.4.0), and duration tokens plus `$root` handling (5.7.0).\[3\]\[4\]
- `oklch()` has been Baseline Widely available "since May 2023" according to MDN. `light-dark()` became Baseline Newly available on 13 May 2024, so it reaches Widely available about 30 months later, around 13 November 2026 (secondary calculation).\[5\]\[6\] It also works with images now, not only colours (MDN).\[7\]
- `light-dark()` does nothing unless `color-scheme: light dark` is in scope. Without it the function always returns the light value.\[8\]
- matplotlib 3.10 (December 2024) added a "New more-accessible color cycle" and three dark-mode diverging colormaps. matplotlib's 3.10.0 release notes say: "Three diverging colormaps have been added: "berlin", "managua", and "vanimo"… with minimum lightness at the center". The current line is 3.11 (3.11.0 on 11–12 June 2026, 3.11.2 on 11 September 2026).
- Seaborn's latest release is still 0.13.2 (25 January 2024). D3's is still 7.9.0 (12 March 2024). Both work, but neither has shipped a release in more than two years.\[9\]\[10\]
- Altair 6 compiles against Vega-Lite 6 and is now at 6.3.0 (15 September 2026). Altair 5 is out of date.\[11\]\[12\]
- ECharts 6.0.0 was released on 30 July 2025. The current release is 6.1.0.\[13\]\[14\] ECharts 6 shipped a new default theme and dark mode.\[15\]
- Recharts 3.0.0 (23 June 2025) turned on the accessibility layer by default: you can tab into a chart and move through it with the arrow keys. Themes are experimental in the 3.11 canary releases.\[16\]\[17\]
- Observable Plot 0.6.18 added support for `light-dark()` colours and a top-level `legend` option.\[18\] The current version is 0.6.19 (5 November 2026).\[19\]
- PDF/UA-2 (ISO 14289-2:2024) was published in March 2024: ISO lists 13 March and the PDF Association announced it on 15 March. It is based on PDF 2.0 and does not replace PDF/UA-1.\[20\]\[21\]
- Pandoc 3.14 is current (12 November 2026).\[22\] Pandoc 3.11 added `--math-method` and deprecated `--mathml`, `--mathjax` and the other per-engine flags. Pandoc 3.8.3 added pptx and xlsx as input formats.\[23\]\[24\]
- Quarto 1.11.9 (30 October 2026) is the stable release. 1.12 has been in pre-release since 2 November 2026, with no announced date for the stable release.\[25\]\[26\]
- Aptos replaced Calibri as the default font in the Office theme. Microsoft announced this on 13 July 2023 and it reached most Microsoft 365 users from December 2023 and January 2024 (version 2312, according to a secondary source).\[27\]\[28\]\[29\]

## 2. Corrections

| Belief | Verdict | Correct fact | Source |
|---|---|---|---|
| The DTCG published the first stable Design Tokens specification in 2025 | **Confirmed, with a caveat** | 2025.10, 28 October 2025. It is a Community Group report and "not on the W3C Standards Track" | w3.org/community/design-tokens/2025/ ; designtokens.org/faq/\[1\]\[30\] |
| OKLCH and `light-dark()` are Baseline | **Partly out of date** | `oklch()` is Baseline Widely available (since May 2023). MDN labels `light-dark()` "Baseline 2024" (Newly available, 13 May 2024), so it only reaches Widely available around 13 November 2026 | MDN oklch() ; MDN light-dark() ; GitHub issue takagiyuuki/portfolio#104 (secondary)\[5\]\[6\]\[7\] |
| Okabe-Ito (Wong 2011) and viridis are the standard colour-blind-safe palettes | **Partly verified** | Okabe-Ito is now built into matplotlib. Its "What's new in 3.11.0 (Jun 11, 2026)" adds an "Okabe-Ito accessible color sequence" (`cycler(color='okabe_ito')`) alongside the 'petroff6', 'petroff8' and 'petroff10' cycles. Wong 2011 and viridis were not verified in this run | matplotlib "What's new in 3.11.0" ; matplotlib 3.10 announcement |
| Aptos replaced Calibri as the default Office font in 2023–2024 | **Confirmed** | Announced 13 July 2023. Wide rollout from December 2023 and January 2024 | CNBC 13 July 2023 ; CNN 22 February 2024 (secondary)\[27\]\[29\] |
| PDF/UA-2 (ISO 14289-2) published 2024; PDF 2.0 is ISO 32000-2:2020 | **Confirmed** | ISO 14289-2:2024, published 13 March 2024 (ISO stage 60.60). The ISO catalogue (iso.org/standard/75839.html) lists ISO 32000-2:2020 as "Publication date : 2020-12", stage "60.60 2020-12-11 International Standard published", Edition 2, replacing ISO 32000-2:2017 | iss.rs ISO record ; pdfa.org ; iso.org/standard/75839.html |
| D3 7 | **Confirmed but stale** | 7.9.0, 12 March 2024. No release since\[9\] | npm d3 ; Snyk |
| Vega-Lite 6 | **Confirmed** | 6.5.0, 8 October 2026 | github.com/vega/vega-lite/releases\[31\] |
| Observable Plot | **Updated** | 0.6.19, 5 November 2026 | GitHub observablehq/plot v0.6.19 (subagent)\[19\] |
| ECharts 6 | **Confirmed** | 6.0.0 on 30 July 2025. Current is 6.1.0\[13\]\[14\] | github.com/apache/echarts/releases ; npm\[15\] |
| Chart.js 4 | **Confirmed; minor version updated** | 4.6.1, 22 October 2026\[32\]\[33\] | github.com/chartjs/Chart.js/releases/tag/v4.6.1 |
| Recharts (no version given) | **Specify major 3** | 3.10.1 is latest; 3.11 is in canary | npm recharts\[34\] |
| matplotlib 3.10 | **Out of date** | 3.11.2, 11 September 2026 | matplotlib.org ; releasealert.dev\[35\] |
| seaborn 0.13 | **Confirmed, but no release since January 2024** | 0.13.2, 25 January 2024\[10\] | github.com/mwaskom/seaborn/releases |
| plotly 6 | **Confirmed** | 6.9.0, 9 July 2026 (latest seen in changelog)\[36\] | plotly.py CHANGELOG.md |
| Altair 5 | **Out of date** | 6.3.0, 15 September 2026; Altair 6 targets Vega-Lite 6 | github.com/vega/altair/releases ; PyPI (subagent)\[11\]\[12\] |

## 3. Facts table

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| 1 | DTCG first stable specification | 2025.10 | https://www.w3.org/community/design-tokens/2025/ | "The Design Tokens Community Group today announced the first stable version of the Design Tokens Specification (2025.10)" | 2025-10-28\[30\] |
| 2 | DTCG standards status | Not on the W3C Standards Track | https://www.designtokens.org/faq/ | "The DTCG spec is not on the W3C Standards Track" | read 2026-11-15\[1\] |
| 3 | Style Dictionary DTCG colour support | 5.3.0 adds DTCG structured colour and an oklch transform | https://github.com/style-dictionary/style-dictionary/blob/main/CHANGELOG.md | "Add support for DTCG v2025.10 structured color format in color transformers" | read 2026-11-15\[4\] |
| 4 | Style Dictionary DTCG dimension support | 5.4.0 | same | "Add support for DTCG v2025.10 dimension token type object value" | read 2026-11-15\[4\] |
| 5 | Style Dictionary 5.7.0 | Duration tokens and `$root` naming | https://github.com/style-dictionary/style-dictionary/releases/tag/v5.7.0 | "Add support for DTCG v2025.10 duration token values" | October 2026\[3\] |
| 6 | Style Dictionary 5.7.1 publish date (secondary) | 24 October 2026 | https://www.supernova.io/blog/style-dictionary-design-tokens-agents | "We used version 5.7.1, published to npm on 24 October 2026" | 2026\[37\] |
| 7 | oklch() Baseline status | Widely available | https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch | "It's been available across browsers since May 2023." | read 2026-11-15\[6\] |
| 8 | light-dark() Baseline status | Baseline 2024 | https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark | "Baseline 2024" / "accepts two colors or two images" | read 2026-11-15\[7\] |
| 9 | light-dark() Widely-available date (secondary) | about 13 November 2026 | https://github.com/takagiyuuki/portfolio/issues/104 | "light-dark() reaches Baseline Widely available around 2026-11-13 (30 months after Newly available)." | 2026\[5\] |
| 10 | PDF/UA-2 publication | ISO 14289-2:2024, 13 March 2024 | https://iss.rs/en/project/show/iso:proj:82278 | "Publication date: Mar 13, 2024" | 2024-03-13\[21\] |
| 11 | PDF/UA-2 basis | WTPDF, PDF 2.0 | https://pdfa.org/resource/iso-14289-pdfua/ | "completely revised and enhanced for PDF 2.0 (ISO 32000-2). This document is based on the PDF Association's WTPDF specification." | read 2026-11-15\[38\] |
| 12 | PDF/UA-2 does not replace UA-1 | — | https://itextpdf.com/blog/itext-news/pdfua-2-here-introducing-new-standard-pdf-universal-accessibility | "ISO 14289-2 (PDF/UA-2) does not replace ISO 14289-1 (PDF/UA-1)." | 2024-09-10\[20\] |
| 13 | Aptos announcement | July 2023 | https://www.cnbc.com/2023/07/13/microsoft-aptos-is-the-next-office-default-font.html | "The new default, replacing Calibri, is called Aptos." | 2023-07-13\[29\] |
| 14 | Aptos rollout | From December 2023 | https://www.cnn.com/2024/02/22/us/microsoft-default-font-aptos-calibri-cec/ | "it started rolling out on a larger scale in December — to hundreds of millions of Microsoft 365 users" | 2024-02-22\[27\] |
| 15 | matplotlib latest | 3.11.2 | https://releasealert.dev/github/matplotlib/matplotlib | "v3.11.2 | Sep 11, 2026 | Stable" | 2026-09-11\[35\] |
| 16 | matplotlib 3.11.0 | 11 June 2026 | https://matplotlib.org/ | "Jun 11, 2026 Matplotlib 3.11.0 Released" | 2026-06-11\[39\] |
| 17 | matplotlib 3.10 accessibility | New colour cycle | https://discourse.matplotlib.org/t/matplotlib-announce-ann-matplotlib-3-10-0/25601 | "New more-accessible color cycle" | 2025-01-31\[40\] |
| 18 | seaborn latest | 0.13.2 | https://github.com/mwaskom/seaborn/releases | "v0.13.2 (January 2024) Latest"\[10\] | 2024-01-25 |
| 19 | plotly.py | 6.9.0 | https://github.com/plotly/plotly.py/blob/main/CHANGELOG.md | "[6.9.0] - 2026-07-09"\[36\] | 2026-07-09 |
| 20 | Altair 6 targets Vega-Lite 6 | — | https://github.com/vega/altair/releases | "we now compile against Vega-Lite version 6" | read 2026-11-15\[12\] |
| 21 | Altair latest | 6.3.0 | https://pypi.org/project/altair/ | "6.3.0 … Sep 15, 2026" | 2026-09-15\[11\] |
| 22 | Vega-Lite latest | 6.5.0 | https://github.com/vega/vega-lite/releases/tag/v6.5.0 | "6.5.0 (2026-10-08)" | 2026-10-08\[41\] |
| 23 | D3 latest | 7.9.0 | https://security.snyk.io/package/npm/d3 | "7.9.0 | 12 Mar, 2024"\[9\] | 2024-03-12 |
| 24 | ECharts 6.0.0 | 30 July 2025 | https://github.com/apache/echarts/releases | "6.0.0 … released this 30 Jul" | 2025-07-30\[15\] |
| 25 | ECharts latest | 6.1.0 | https://www.npmjs.com/package/echarts?activeTab=versions | "Latest version: 6.1.0"\[14\] | read 2026-11-15 |
| 26 | Chart.js latest | 4.6.1 | https://www.versio.io/en/product-release-end-of-life-eol-chartjs-team-chartjs.html | "The latest version of Chart.js is 4.6.1, released as part of the 4 release on 22 October 2026."\[33\] | 2026-10-22 |
| 27 | Recharts latest | 3.10.1 | https://www.npmjs.com/package/recharts | "Latest version: 3.10.1" | read 2026-11-15\[42\] |
| 28 | Recharts 3 accessibility | accessibilityLayer on by default | https://github.com/recharts/recharts/releases/tag/v3.0.0 | "accessibilityLayer is now on on all polar and cartesian charts by default" | 2025-06-23\[17\] |
| 29 | Observable Plot light-dark support | 0.6.18 | https://github.com/observablehq/plot/releases/tag/v0.6.18 | "Add support for light-dark(…) color syntax."\[18\] | 0.6.18 release |
| 30 | Observable Plot latest | 0.6.19 | https://github.com/observablehq/plot/releases/tag/v0.6.19 | "mbostock released this 05 Nov … v0.6.19" | 2026-11-05\[19\] |
| 31 | Pandoc latest | 3.14 | https://github.com/jgm/pandoc/releases/tag/3.14 | "I'm pleased to announce the release of pandoc 3.14" | 2026-11-12 (pandoc.org changelog says 2026-11-10)\[43\]\[44\] |
| 32 | Pandoc 3.11 math option | `--math-method` | https://github.com/jgm/pandoc/discussions/11835 | "A new `--math-method` option, which replaces the (now deprecated but still functional) options `--mathml`, `--mathjax`…"\[24\] | 2026-08-29 |
| 33 | Pandoc 3.8.3 new readers | asciidoc, pptx, xlsx | https://github.com/jgm/pandoc/discussions/11313 | "This release adds three new input formats (asciidoc, pptx, and xlsx)"\[23\] | 2025-12-01 |
| 34 | Quarto stable | 1.11.9 | https://github.com/quarto-dev/quarto-cli/releases/ | "v1.11.9 Latest" | 2026-10-30\[25\] |
| 35 | Quarto pre-release | 1.12 | https://quarto.org/docs/prerelease/1.12/index.html | "Quarto 1.12 Pre-Release. Published November 2, 2026." | 2026-11-02\[26\] |
| 36 | Mermaid latest | 12.3.0 | https://github.com/mermaid-js/mermaid/releases | "mermaid@12.3.0 … released this 03 Nov" | 2026-11-03\[45\] |

## 4. Findings

### 4.1 Design tokens (Priority 1)

**Specification.** The DTCG announced the Design Tokens Specification 2025.10 as its "first stable version" on 28 October 2025. The full text is at designtokens.org/tr/2025.10/, and a living draft is kept separately.\[46\] The FAQ calls the core format "stable for production use" but says it is "not on the W3C Standards Track".\[1\] The format is JSON. Each token is an object with `$value` and usually `$type`, and the reserved keys are `$description`, `$extensions` and `$deprecated`. Aliases use `{group.token}`. The secondary summaries we read say 2025.10 also adds `$ref` (JSON Pointer) for property-level references and a `$root` token inside a group.\[47\] **Recommendation:** write `.tokens.json` files that follow 2025.10. Use structured colour objects, and include a `hex` fallback for any colour that may fall outside the sRGB gamut.

**Tooling.** Use **Style Dictionary 5**; version 4 is out of date. Version 5 reads both the DTCG and legacy formats.\[48\] By October 2026 it had added DTCG structured colour support "for all 14 DTCG color spaces" with `color/oklch` and `color/oklab` transforms (5.3.0), object dimensions (5.4.0), and duration tokens and `$root` handling (5.7.0).\[3\]\[4\] Secondary sources quote Style Dictionary's own DTCG page as still saying 2025.10 support is "a work in progress in v5", so pin a minor version and test your token types.\[2\] Zeroheight's documentation says Style Dictionary v5 "adopted [DTCG 2025.10] as its base format".\[49\] The DTCG announcement quotes Tokens Studio supporting the specification ("The DTCG spec v1 gives the industry a stable foundation").\[46\] Its current version was not found.

**One token set, four targets (recommended mapping):**
- **CSS:** Style Dictionary `css/variables` produces custom properties on `:root`. For dark mode, emit `--x: light-dark(<light>, <dark>)` and set `color-scheme: light dark` (per MDN and web.dev).\[7\]\[50\] If you must support browsers older than about 2024, also emit a `@media (prefers-color-scheme: dark)` block.
- **Office theme XML:** not found. We found no primary source for a token-to-`theme1.xml` mapping in this run. Commonly used practice, not verified here: map 2 dark, 2 light and 6 accent colours plus hyperlink colours to the DrawingML `a:clrScheme` slots (`dk1`, `lt1`, `dk2`, `lt2`, `accent1`–`accent6`, `hlink`, `folHlink`), and map heading and body fonts to `a:majorFont` and `a:minorFont`. Office themes hold only sRGB hex values, so convert OKLCH tokens to hex at build time.
- **Charts:** export the categorical palette as an ordered array token and pass it to `axes.prop_cycle` in matplotlib, `range.category` in Vega-Lite and Altair, `color` in ECharts, and so on. Observable Plot (0.6.18 and later) accepts `light-dark()` colours directly.\[18\]
- **Dark mode:** model dark mode as a second value set (a theme or "mode"), not as a second token tree. The DTCG Resolver module for theming was in request-for-comment in 2025.\[30\] Its final status was not found.

### 4.2 Colour (Priority 2)

- **OKLCH:** Baseline Widely available. Relative colour syntax such as `oklch(from var(--c) calc(l*0.85) c h)` is shown in web.dev's Baseline colour-theme article.\[6\]\[50\] Use OKLCH so that lightness steps are perceptually even, but always **measure** contrast on the final sRGB output.
- **light-dark():** "Baseline 2024" on MDN. It reaches Widely available around 13 November 2026 (secondary calculation). It requires `color-scheme`; without it the light value is returned.\[5\]\[7\]\[8\]
- **WCAG contrast:** the W3C WCAG 2.2 Recommendation (w3.org/TR/WCAG22/), success criterion 1.4.3 (Level AA), says: "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for…". W3C's Understanding 1.4.3 page says the ratios are "intended to be treated as threshold values… 4.499:1 would not meet the 4.5:1 threshold", so never round up. These quotes come from search snippets; we did not open either page. Our understanding of the rest, still unverified: 3:1 for large text, 3:1 for non-text UI and graphical objects (1.4.11), and colour must not be the only visual means of conveying information (1.4.1). Confirm against w3.org/TR/WCAG22 before filing.
- **Colour-blind-safe palettes:** matplotlib now ships Okabe-Ito. Its "What's new in 3.11.0 (Jun 11, 2026)" adds an "Okabe-Ito accessible color sequence" (`cycler(color='okabe_ito')`) and "'petroff6' and 'petroff8'… complement the existing 'petroff10' color cycle". Wong 2011 and viridis were not verified in this run. The cycle matplotlib 3.10 added is named 'petroff10', per its "What's new in 3.10.0 (December 13, 2024)": "A new color cycle named 'petroff10' was added… [it] aims to be both generally pleasing aesthetically and colorblind accessible". It is based on Petroff, M. A., "Accessible Color Sequences for Data Visualization" (arXiv:2107.02270).
- **Dark-mode guidance (Material, Apple HIG, Fluent):** not covered; no sources fetched.

### 4.3 Data visualization practice (Priority 3)

Not covered with primary sources in this run: the FT Visual Vocabulary, Datawrapper, Few, Tufte, W3C chart-accessibility guidance, and dashboard and KPI design. What was sourced is vendor accessibility features. Recharts 3 turns on keyboard navigation by default (`accessibilityLayer`).\[17\] Observable Plot supports `light-dark()` colours and a top-level `legend` option, and it switched its categorical default to `observable10` in 0.6.12.\[18\]\[51\] matplotlib 3.10 added an accessible colour cycle and three dark-mode diverging colormaps, "berlin", "managua" and "vanimo", which have their minimum lightness at the centre (matplotlib 3.10.0 release notes). **Position:** a chart should never depend on colour alone. Pair colour with direct labels, marker shapes or patterns, give a text alternative that states the takeaway, and provide the underlying data table. This is our recommendation; its WCAG basis is listed as not verified above.

### 4.4 Libraries (Priority 4)

| Library | Current | Released | Maintenance signal |
|---|---|---|---|
| D3 | 7.9.0 | 12 March 2024 | No release in more than 2 years; Snyk flags low activity\[9\] |
| Vega-Lite | 6.5.0 | 8 October 2026 | Active\[31\] |
| Observable Plot | 0.6.19 | 5 November 2026 | Active; still 0.x\[19\] |
| ECharts | 6.1.0 | 19 May 2026 (apache/echarts GitHub release tag 6.1.0: "100pah released this 19 May"; Snyk: "6.1.0 | 19 May, 2026") | Active (Apache) |
| Chart.js | 4.6.1 | 22 October 2026\[33\] | Active |
| Recharts | 3.10.1 | 25 July 2026 (Snyk recharts package page, secondary: "3.10.1 | 25 Jul, 2026") | Active; 3.11 in canary |
| matplotlib | 3.11.2 | 11 September 2026 | Active\[35\] |
| seaborn | 0.13.2 | 25 January 2024 | No release in more than 2 years; Snyk rates it "Inactive"\[52\] |
| plotly.py | 6.9.0 (latest seen) | 9 July 2026\[36\] | Active |
| Altair | 6.3.0 | 15 September 2026 | Active\[11\] |

**Recommendations.** For static reports, use matplotlib 3.11, or Altair 6 with vl-convert for SVG and PNG output. Seaborn is acceptable for quick statistical plots, but do not start new long-lived code on it without accepting that it has not released since January 2024. For interactive web dashboards, use ECharts 6 (which has built-in dark mode and a new theme) or Vega-Lite and Altair; use Recharts 3 inside React apps.\[53\] For Excel or PowerPoint charts, we have no sourced recommendation. Native Office charts, for example through python-pptx or openpyxl, keep charts editable; images do not. This is our understanding and was not verified in this run.

### 4.5 Typography (Standard)

Aptos is the Office default font. Microsoft's design blog says: "Aptos will start appearing as the new default font across Word, Outlook, PowerPoint and Excel for hundreds of millions of users". Calibri remains available.\[54\] Whether Aptos is available outside Microsoft 365 (on Linux, or as a web font) and under what licence: not found in this run. A secondary source says Microsoft provides a ZIP package for local installation, but this is unverified.\[55\] System font stacks, variable fonts and the SIL OFL were not covered.

### 4.6 Documents (Standard)

- **PDF/UA-2** is ISO 14289-2:2024 (13 March 2024). It is based on WTPDF and PDF 2.0, and PDF/UA-1 stays valid.\[21\]\[38\]\[56\] The PDF Association says PDF/UA standards have been free to download since 12 August 2024 (according to axes4, a secondary source).\[57\] One vendor blog reports validating PDF/UA-2 files with veraPDF's `ua2` profile (secondary).\[58\]
- **PDF 2.0 = ISO 32000-2:2020:** confirmed by the ISO catalogue (iso.org/standard/75839.html): "Publication date : 2020-12", stage "60.60 2020-12-11 International Standard published", Edition 2, replacing ISO 32000-2:2017.
- **Pandoc 3.14** (12 November 2026) is current.\[59\] Pandoc 3.11 introduced `--math-method`, which makes the per-engine flags deprecated, and made MathML the default math method. Pandoc 3.8 added the `xml` AST format and `--syntax-highlighting`.\[24\]\[60\]\[61\]
- **Quarto 1.11.9** (30 October 2026) is the stable release, and 1.12 is in pre-release.\[25\] Wikipedia, summarising a Posit post that we did not open, says Quarto 2 is being written in Rust.\[62\]
- **Mermaid 12.3.0** (3 November 2026).\[45\]\[63\]
- Accessible Word and PowerPoint guidance (headings, alt text, tables, reading order) was not covered.

### 4.7 Generated reports (Standard)

Not covered with sources. Our recommended practice: compute every figure and summary in one Quarto (or Jupyter or knitr) run from the same frozen dataset, and print each value inline from code rather than typing it. Record the version of every tool that produced a figure. Pandoc and matplotlib both publish a Zenodo DOI for each release (for example, matplotlib v3.10.9 is DOI 10.5281/zenodo.19716234), so a figure can be cited at an exact release.\[59\]\[64\]\[65\]

## 5. Tools

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| Style Dictionary | Token build | 5.7.1 | 2026-10-24 (secondary) | `npm i -D style-dictionary` | `config.json` / `*.config.mjs` | GitHub, Supernova\[37\] |
| matplotlib | Static charts | 3.11.2 | 2026-09-11 | `pip install matplotlib` | `matplotlibrc` | matplotlib.org\[35\] |
| seaborn | Statistical charts | 0.13.2 | 2024-01-25 | `pip install seaborn`\[10\]\[66\] | — | GitHub |
| plotly.py | Interactive charts | 6.9.0+ | 2026-07-09\[36\] | `pip install plotly` | — | CHANGELOG |
| Altair | Vega-Lite in Python | 6.3.0 | 2026-09-15 | `pip install altair` | — | PyPI\[11\] |
| Vega-Lite | Grammar of graphics | 6.5.0 | 2026-10-08 | `npm i vega-lite` | spec JSON | GitHub\[41\] |
| D3 | Low-level web visualization | 7.9.0 | 2024-03-12 | `npm i d3`\[9\]\[67\] | — | npm |
| Observable Plot | Web charts | 0.6.19 | 2026-11-05 | `npm i @observablehq/plot` | — | GitHub\[19\]\[68\] |
| ECharts | Dashboards | 6.1.0 | 2026-05-19 | `npm i echarts` | — | GitHub release tag 6.1.0; Snyk |
| Chart.js | Canvas charts | 4.6.1 | 2026-10-22 | `npm i chart.js`\[33\]\[69\] | — | GitHub |
| Recharts | React charts | 3.10.1 | 2026-07-25 | `npm i recharts` | — | npm; Snyk (secondary) |
| Pandoc | Document conversion | 3.14 | 2026-11-12 | `pandoc in.md -o out.docx --reference-doc=ref.docx` | defaults YAML | GitHub\[70\] |
| Quarto | Computed documents | 1.11.9 | 2026-10-30 | `quarto render` | `_quarto.yml` | GitHub\[25\] |
| Mermaid | Diagrams | 12.3.0 | 2026-11-03 | `npm i mermaid` | — | GitHub\[45\] |

## 6. Changing in the next 12 months

- **`light-dark()` becomes Baseline Widely available around 13 November 2026.** After that date it is safe for "widely available" browser targets (secondary calculation).\[5\]
- **Quarto 1.12** is in pre-release (from 2 November 2026), with no announced stable date. Quarto 2, written in Rust, is in development, and no release date was found.\[26\]\[62\]
- **Pandoc:** the `--mathml`, `--mathjax`, `--katex`, `--webtex` and `--gladtex` options are deprecated in favour of `--math-method`, and so is the `html-math-method` defaults key.\[24\] No removal date has been announced.
- **Recharts:** `Cell` is deprecated (from 3.7.0) and "will be removed in the next major version". No date has been announced.\[71\]
- **plotly.py:** Mapbox-based traces were deprecated in 6.0 (move to MapLibre).\[72\]
- **Style Dictionary:** full DTCG 2025.10 support is still "a work in progress in v5", and more minor releases are likely.\[73\]
- None of the libraries above publishes a fixed end-of-support date. They support only the latest line (for Chart.js, see versio.io).\[33\] Nothing is flagged as reaching end of support within 12 months.

## 7. Common mistakes (including AI assistants)

- Calling DTCG a "W3C standard" or "W3C Recommendation". It is a Community Group specification (DTCG FAQ).\[1\]
- Writing DTCG dimensions as strings (`"16px"`) or colours as hex strings when targeting 2025.10. Both are now structured objects (Style Dictionary changelogs 5.3.0 and 5.4.0).\[4\]
- Using `light-dark()` without `color-scheme: light dark`, which means the dark value never applies (MDN).\[8\]
- Recommending Style Dictionary 3 or 4 configs (CommonJS) for new projects. Version 5 uses ESM configuration (secondary: common-origin PR #135).\[48\]
- Citing stale versions: "matplotlib 3.10", "Altair 5" and "Pandoc 3.6" are all out of date (sections 3 and 4.4).
- Presenting seaborn and D3 as actively releasing. Neither has released since early 2024.\[9\]\[52\]
- Assuming Aptos is installed everywhere. It rolled out to Microsoft 365 from December 2023, and older or non-Microsoft systems may not have it.\[74\]
- Treating PDF/UA-2 as replacing PDF/UA-1 (iText).\[20\]

## 8. Sources and licences

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| DTCG spec and site (designtokens.org, w3.org/community) | W3C Community Final Specification Agreement / W3C CG licence (not verified in this run) | Brief | Yes | Example JSON: verify licence first | "W3C Design Tokens Community Group" plus URL |
| MDN Web Docs | CC-BY-SA 2.5 for prose; code samples CC0 or public domain (not verified in this run) | Brief | Yes | Yes (code samples) | "MDN contributors" plus URL |
| web.dev | CC-BY 4.0 for content, Apache-2.0 for code samples (not verified in this run) | Brief | Yes | Yes | Google / web.dev plus URL |
| Style Dictionary (GitHub) | Apache-2.0 | Yes | Yes | Yes | Keep the NOTICE file and copyright |
| matplotlib | Matplotlib licence (PSF-based) | Yes | Yes | Yes | Copyright notice |
| seaborn | BSD-3-Clause\[75\] | Yes | Yes | Yes | Copyright notice |
| plotly.py | MIT (not verified in this run) | Yes | Yes | Yes | Copyright notice |
| Altair, Vega-Lite | BSD-3-Clause (not verified in this run) | Yes | Yes | Yes | Copyright notice |
| D3 | ISC\[76\] | Yes | Yes | Yes | Copyright notice |
| ECharts | Apache-2.0\[14\] | Yes | Yes | Yes | NOTICE |
| Chart.js, Recharts | MIT\[69\] | Yes | Yes | Yes | Copyright notice |
| Pandoc | GPL-2.0-or-later\[77\] | Brief (documentation) | Yes | **No**: don't copy code into an Apache-2.0 repository. Calling the CLI is fine | URL\[78\] |
| Quarto | MIT (CLI; not verified in this run) | Yes | Yes | Yes | Copyright notice |
| ISO 14289-2 | ISO copyright, paid | No (bibliographic data only) | Yes | No | Cite the standard number |
| PDF Association, iText, axes4 blogs | All rights reserved | Brief | Yes | No | URL; label as secondary |
| CNN, CNBC, Microsoft Design blog | All rights reserved | Brief | Yes | No | URL |
| GitHub issues, PRs, npm, PyPI pages | Varies / ToS | Brief facts | Yes | No | URL |

## 9. Not found, contested, not covered

- **Contested:** the Pandoc 3.14 date. The GitHub release and Zenodo say 12 November 2026; the pandoc.org changelog says 10 November 2026.\[44\]\[59\]
- **Contested or timing-sensitive:** `light-dark()` Widely-available status. MDN still shows "Baseline 2024", and the 13 November 2026 date is a secondary calculation.\[5\]\[7\]
- **Not found:** the Tokens Studio current version; whether the DTCG Resolver module is final; a primary source for mapping tokens to Office theme XML; Aptos licensing and availability outside Windows; the plotly.py version after 6.9.0; the Quarto 1.12 stable date. (ECharts 6.1.0 was released on 19 May 2026 per its GitHub release; Recharts 3.10.1 on 25 July 2026 per Snyk, a secondary source.)
- **Not covered (budget):** fetched primary text of WCAG 2.2 (only the 1.4.3 quotes from search snippets are included); Wong 2011 and viridis primary sources; Material, Apple HIG and Fluent dark-mode guidance; the FT Visual Vocabulary, Datawrapper, Few and Tufte; W3C chart accessibility tutorials; dashboard and KPI design; system font stacks, variable fonts and the SIL OFL; accessible Word and PowerPoint authoring; computed-document and provenance-citation practice from primary sources.

## Sources

1. [FAQ](https://www.designtokens.org/faq/)
2. [Design Tokens JSON: The DTCG Format Explained · Livery](https://www.livery.site/guides/design-tokens-json-format)
3. [Release v5.7.0 · style-dictionary/style-dictionary · GitHub](https://github.com/style-dictionary/style-dictionary/releases/tag/v5.7.0)
4. [style-dictionary/CHANGELOG.md at main · style-dictionary/style-dictionary · GitHub](https://github.com/style-dictionary/style-dictionary/blob/main/CHANGELOG.md)
5. [Revisit light-dark() for color tokens after Baseline Widely available (2026-11) · Issue #104 · takagiyuuki/portfolio · GitHub](https://github.com/takagiyuuki/portfolio/issues/104)
6. [oklch() CSS function - MDN Web Docs - Mozilla](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
7. [light-dark() CSS function - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark)
8. [You're writing dark-mode colors twice. \`light-dark()\` fixes that.](https://bestpractic.org/blog/css-light-dark-function)
9. [d3 vulnerabilities](https://security.snyk.io/package/npm/d3)
10. [Releases · mwaskom/seaborn · GitHub](https://github.com/mwaskom/seaborn/releases)
11. [altair · PyPI](https://pypi.org/project/altair/)
12. [Releases · vega/altair · GitHub](https://github.com/vega/altair/releases)
13. [Board Meeting Minutes - ECharts - Apache Whimsy](https://whimsy.apache.org/board/minutes/ECharts.html)
14. [echarts - npm](https://www.npmjs.com/package/echarts?activeTab=versions)
15. [Releases · apache/echarts · GitHub](https://github.com/apache/echarts/releases)
16. [recharts/recharts v3.11.0-canary.0 on GitHub](https://newreleases.io/project/github/recharts/recharts/release/v3.11.0-canary.0)
17. [Release v3.0.0 · recharts/recharts · GitHub](https://github.com/recharts/recharts/releases/tag/v3.0.0)
18. [Release v0.6.18 · observablehq/plot · GitHub](https://github.com/observablehq/plot/releases/tag/v0.6.18)
19. [Release v0.6.19 · observablehq/plot · GitHub](https://github.com/observablehq/plot/releases/tag/v0.6.19)
20. [PDF/UA-2 is Here! Introducing the New Standard for PDF Universal Accessibility](https://itextpdf.com/blog/itext-news/pdfua-2-here-introducing-new-standard-pdf-universal-accessibility)
21. [ISO 14289-2:2024](https://iss.rs/en/project/show/iso:proj:82278)
22. [Pandoc - Wikidata](https://www.wikidata.org/wiki/Q2049294)
23. [3.8.3 · jgm/pandoc · Discussion #11313 · GitHub](https://github.com/jgm/pandoc/discussions/11313)
24. [pandoc 3.11 · jgm/pandoc · Discussion #11835 · GitHub](https://github.com/jgm/pandoc/discussions/11835)
25. [Releases · quarto-dev/quarto-cli · GitHub](https://github.com/quarto-dev/quarto-cli/releases/)
26. [Quarto 1.12 Pre-Release](https://quarto.org/docs/prerelease/1.12/index.html)
27. [Why the Microsoft default font change from Calibri to Aptos upset some users](https://www.cnn.com/2024/02/22/us/microsoft-default-font-aptos-calibri-cec/)
28. [How to Change Microsoft 365 Default Font from Aptos to Calibri](https://www.wps.com/office-quick-solution/office-app-problems/how-to-change-microsoft-365-default-font-from-aptos-to-calibri/)
29. [Here's the new default font for Microsoft Outlook and Word: Aptos](https://www.cnbc.com/2023/07/13/microsoft-aptos-is-the-next-office-default-font.html)
30. [Design Tokens Community Group](https://www.w3.org/community/design-tokens/2025/)
31. [Releases · vega/vega-lite · GitHub](https://github.com/vega/vega-lite/releases)
32. [Release v4.6.1 · chartjs/Chart.js · GitHub](https://github.com/chartjs/Chart.js/releases/tag/v4.6.1)
33. [Chart.js releases, versions & end-of-life (EOL) dates](https://www.versio.io/en/product-release-end-of-life-eol-chartjs-team-chartjs.html)
34. [recharts - npm](https://www.npmjs.com/package/recharts?activeTab=versions)
35. [matplotlib/matplotlib on GitHub](https://releasealert.dev/github/matplotlib/matplotlib)
36. [plotly.py/CHANGELOG.md at main · plotly/plotly.py · GitHub](https://github.com/plotly/plotly.py/blob/main/CHANGELOG.md)
37. [Style Dictionary: Build Design Tokens for People and Agents](https://www.supernova.io/blog/style-dictionary-design-tokens-agents)
38. [ISO 14289-1](https://pdfa.org/resource/iso-14289-pdfua/)
39. [Matplotlib — Visualization with Python](https://matplotlib.org/)
40. [\[Matplotlib-announce\] \[ANN\] Matplotlib 3.10.0 - Announcements - Matplotlib](https://discourse.matplotlib.org/t/matplotlib-announce-ann-matplotlib-3-10-0/25601)
41. [Release Release 6.5.0 · vega/vega-lite · GitHub](https://github.com/vega/vega-lite/releases/tag/v6.5.0)
42. [recharts - npm](https://www.npmjs.com/package/recharts)
43. [Release pandoc 3.14 · jgm/pandoc · GitHub](https://github.com/jgm/pandoc/releases/tag/3.14)
44. [Pandoc - Releases](https://pandoc.org/releases.html)
45. [Releases · mermaid-js/mermaid · GitHub](https://github.com/mermaid-js/mermaid/releases)
46. [Design Tokens specification reaches first stable version \[via Design Tokens Community Group\]](https://lists.w3.org/Archives/Public/public-design-tokens/2025Oct/0003.html)
47. [Design Tokens Format Reference (W3C DTCG)](https://openllm.wavise.com/blog/design-tokens-reference)
48. [build(tokens): upgrade to Style Dictionary 5 (migration step 4) by common-origin · Pull Request #135 · common-origin/common-origin-design-system · GitHub](https://github.com/common-origin/common-origin-design-system/pull/135)
49. [Migrating to Style Dictionary v5 in tokens automation](https://help.zeroheight.com/hc/en-us/articles/48049028236187-Migrating-to-Style-Dictionary-v5-in-tokens-automation)
50. [Color themes with Baseline CSS features | Articles | web.dev](https://web.dev/articles/baseline-in-action-color-theme)
51. [Release v0.6.12 · observablehq/plot · GitHub](https://github.com/observablehq/plot/releases/tag/v0.6.12)
52. [seaborn](https://snyk.io/advisor/python/seaborn)
53. [Apache ECharts on X: "🚀 Apache ECharts 6.0.0 is here! ✨ 12 groundbreaking upgrades: - Chord/Beeswarm/Jitter Scatter - Axis Break & Stock Charts+ - Matrix Layout & Dark Mode Unleash next-gen data storytelling! 🔗https://t.co/uttI22CFVs https://t.co/gFsKpbxbKD" / X](https://x.com/ApacheECharts/status/1952629667443466453)
54. [a change of typeface microsofts new default font has arrived f200eb16718d](https://medium.com/microsoft-design/a-change-of-typeface-microsofts-new-default-font-has-arrived-f200eb16718d)
55. [Microsoft 365's New Aptos Fonts: Install, Use, and Fix Them](https://www.itechguides.com/unlock-microsoft-365s-new-aptos-fonts-what-you-need-to-know/)
56. [PDF/UA-2 explained: what ISO 14289-2 changes · DocAccessible](https://docaccessible.com/guides/pdf-ua-2-explained)
57. [PDF/UA-2 vs. Well-tagged PDF - axes4](https://www.axes4.com/en/blog/post/2024/pdf-ua-2-vs-well-tagged-pdf)
58. [PDF/UA-2 (ISO 14289-2): What Actually Changes, and How We Verify It — veraPDF and PAC](https://reflowpdf.com/blog/pdf-ua-2-iso-14289-2)
59. [Pandoc](https://zenodo.org/records/24151446)
60. [jgm/pandoc 3.8 on GitHub](https://newreleases.io/project/github/jgm/pandoc/release/3.8)
61. [chore(deps): update dependency github:jgm/pandoc (3.10.2 → 3.11) by renovate\[bot\] · Pull Request #663 · ivuorinen/dotfiles · GitHub](https://github.com/ivuorinen/dotfiles/pull/663)
62. [Quarto (software)](<https://en.wikipedia.org/wiki/Quarto_(software)>)
63. [Mermaid - Browse Files at SourceForge.net](https://sourceforge.net/projects/mermaid.mirror/files/)
64. [Pandoc](https://zenodo.org/records/22151679)
65. [Matplotlib: Visualization with Python](https://zenodo.org/records/19716234)
66. [pypi.org](https://pypi.org/project/seaborn)
67. [d3 - npm](https://www.npmjs.com/package/d3?activeTab=readme)
68. [observablehq/plot](https://npmjs.com/package/@observablehq/plot)
69. [chart.js - npm](https://www.npmjs.com/package/chart.js?activeTab=readme)
70. [Releases · jgm/pandoc · GitHub](https://github.com/jgm/pandoc/releases)
71. [recharts/recharts v3.7.0 on GitHub](https://newreleases.io/project/github/recharts/recharts/release/v3.7.0)
72. [Release v6.0.0rc0 · plotly/plotly.py · GitHub](https://github.com/plotly/plotly.py/releases/tag/v6.0.0rc0)
73. [FEE-910: W3C DTCG Format Module — Complete Token Spec Reference](https://alivedise.github.io/frontend-engineering-essentials/dtcg-token-format-spec)
74. [Aptos vs Calibri: Microsoft's New Default Font Compared](https://madegooddesigns.com/aptos-vs-calibri/)
75. [seaborn 0.13.2 on PyPI - Libraries.io - security & maintenance data for open source software](https://libraries.io/pypi/seaborn)
76. [D3.js](https://en.wikipedia.org/wiki/D3.js)
77. [Pandoc](https://en.wikipedia.org/wiki/Pandoc)
78. [pandoc - conda-forge](https://anaconda.org/conda-forge/pandoc)

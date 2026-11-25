# Visual theme

Read this for setting up or reviewing design tokens and their build, theming an app or a set of
documents, adding dark mode, choosing colors and color ramps, checking contrast, Windows
contrast themes (forced colors), and choosing fonts with a fallback stack.

Charts are `data-visualization`'s. Markup, HTML accessibility and the CSS of
`prefers-color-scheme` are the `coding` skill's `html-coding`; an accessibility module is planned
here. Pinning follows the project-bootstrap-and-audit standard's dimension 8. A company's
palette, fonts and templates live in its own repository, never in this one.

## Rules

1. **Keep colors, spacing and type as design tokens in one source file,** built for every
   target: CSS, charts, documents. A screen or chart never hard-codes a value the tokens hold.
2. **Name tokens by role, not by value.** Primitives such as `color.blue-600` hold values,
   semantic tokens such as `color.text-link` alias them, and screens use only semantic tokens.
3. **Dark mode is a second set of values for the same semantic tokens,** not a second set of
   names.
4. **Step colors in OKLCH, and measure contrast on the sRGB color that ships,** in each scheme.
5. **Meet WCAG 2.2 contrast as thresholds, never rounded up, and never let color carry meaning
   alone.**
6. **Give every font a fallback stack,** and check the layout where the first font is missing.

### The token file

- **Format:** the Design Tokens Community Group (DTCG) format 2025.10, a stable Community Group
  specification, not a W3C standard (fact `vt-dtcg-status`). Name files `*.tokens.json` or
  `*.tokens`, and serve them as `application/design-tokens+json` (fact `vt-dtcg-file`).
- **Colors are objects** with `colorSpace` and `components`, and an optional `hex` fallback
  (fact `vt-dtcg-color`). Write the `hex` too, for tools that read only hex.
- **Dimensions are objects** of `value` and `unit`, and the unit is `px` or `rem` (fact
  `vt-dtcg-dimension`). Use `rem` for type and spacing, so they follow the reader's settings.
- **Aliases use braces,** `{color.blue-600}` (fact `vt-dtcg-alias`).

```json
{
  "color": {
    "blue-600": {
      "$type": "color",
      "$value": { "colorSpace": "oklch", "components": [0.55, 0.15, 255], "hex": "#2971c6" }
    },
    "text-link": { "$type": "color", "$value": "{color.blue-600}" }
  },
  "space": { "md": { "$type": "dimension", "$value": { "value": 1, "unit": "rem" } } }
}
```

### Building it

- **Style Dictionary 5** (fact `vt-sd-version`) added 2025.10's color and dimension objects in
  5.3 and 5.4 (fact `vt-sd-dtcg`), but calls that support unfinished (fact `vt-sd-partial`).
  Pin it, and diff its output in CI, so a token it drops shows.
- **Office documents:** a theme holds twelve colors (fact `vt-office-clrscheme`) as sRGB hex,
  and a heading and a body font. Generate them from semantic tokens (our practice), never by
  hand.

### Dark mode

- **A light file and a dark file define the same semantic tokens,** contexts the DTCG Resolver
  module describes (fact `vt-dtcg-resolver`).
- **In CSS,** set `color-scheme: light dark` (fact `web-color-scheme`), with the dark values
  under `@media (prefers-color-scheme: dark)` (fact `web-media-prefs`). `light-dark()` is Newly
  available and needs `color-scheme` (fact `vt-light-dark`): keep the media query as fallback.

### Color and contrast

- **Build ramps in OKLCH:** hold the hue, step the lightness evenly, and lower the chroma at the
  ends if a step leaves sRGB. CSS can use `oklch()` directly (fact `vt-oklch`).
- **WCAG's ratio comes from sRGB relative luminance** (fact `vt-wcag-luminance`), not OKLCH
  lightness. Measure the hex that ships, against its real background.
- **WCAG 2.2 level AA thresholds** (fact `web-wcag22`):
  - 1.4.3, text: "a contrast ratio of at least 4.5:1", large-scale text 3:1 (fact
    `web-wcag-contrast`);
  - 1.4.11, controls and "Parts of graphics required to understand the content": 3:1 "against
    adjacent color(s)" (facts `web-wcag-nontext`, `vt-wcag-graphics`);
  - 1.4.1, level A: color is never the only visual means of conveying information (fact
    `vt-wcag-color`). Add text, an icon, a shape or a pattern.
- **A ratio is a threshold:** 4.499:1 fails 4.5:1 (fact `vt-contrast-threshold`).
- **Large-scale text is 18pt, or 14pt bold** (fact `vt-wcag-large`), about 24px and 18.5px: an
  11px bold label on a colored fill needs 4.5:1 against it.
- **Meaning survives forced colors.** A Windows contrast theme sets `forced-colors: active`,
  replacing text, background and border colors with the user's and dropping shadows (fact
  `vt-forced-colors`). A status told by its fill alone vanishes: give it text, an icon or a
  border style, and check each screen with a theme on.

### Type

- **Aptos is Office's default in place of Calibri,** since its rollout from 2023 into 2024 (fact
  `vt-aptos`). Older Office installs and non-Microsoft systems may lack it. Write
  `font-family: Aptos, Calibri, system-ui, sans-serif;` and check line breaks and page counts
  without Aptos.

## Mistakes

- **A hex code in a component, chart config or slide master.** It drifts on the next change.
  AI assistants invent a palette per screen: read the token file first and use its tokens.
- **`text-primary-dark` beside `text-primary`.** Each screen then picks by scheme, and one gets
  missed. Keep one name with two values.
- **Calling the DTCG format "a W3C standard",** or writing 2025.10 colors as strings and sizes
  in `em`.
- **Checking contrast in the design tool, or by OKLCH lightness,** or reporting 4.48:1 as
  4.5:1. Measure the shipped hex, unrounded.
- **A status shown as a chip's fill or a row's tint alone,** gone under a contrast theme.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Hard-coded values | `git grep -nE '#[0-9a-fA-F]{6}\b'` outside tokens and build output | `DRIFT` | The semantic token |
| No single source | Colors kept by hand in CSS, chart configs and Office themes | `GAP` | One token file, a build per target |
| Pre-2025.10 shapes | String colors or dimensions, units other than `px` or `rem` | `DRIFT` | Facts `vt-dtcg-color`, `vt-dtcg-dimension` |
| Builder old or unpinned | `style-dictionary` below 5, or no lockfile | `DRIFT` | Fact `vt-sd-version` |
| Dark mode as other names | Tokens or classes named for a scheme | `DRIFT` | One name, two values |
| `light-dark()` unguarded | No `color-scheme`, or no media-query fallback for a Widely available target | `GAP` | Fact `vt-light-dark` |
| Contrast | Below the thresholds above, in either scheme | `GAP` | Move the token a step, measure again |
| A rounded ratio | A check that rounds before it compares | `BLOCKER` | Fact `vt-contrast-threshold` |
| Color alone | Status, errors or links told apart only by color, fill or shadow | `GAP` | Text, icon, shape, border style or underline |
| Forced colors untested | No pass in a contrast theme | `UNVERIFIABLE-HERE` from code | Run it in a contrast theme |
| One font | A `font-family` or font token naming one family | `GAP` | A stack ending in a generic family |
| Company palette here | A company's colors, fonts or template in a public repository | `BLOCKER` | Move it to the company's repository |

## Why

### One token file, named by role, built for every target

- **The reason:** a value copied into CSS, a chart and a document drifts the first time one
  copy changes, and nothing fails. Role names let a scheme or a rebrand change values and no
  screen code.
- **What others do:** export by hand from a design tool, or keep only CSS variables.
- **What it costs:** a build step, a builder whose 2025.10 support is unfinished (fact
  `vt-sd-partial`), and every color pair measured in both schemes.
- **When to choose differently:** a lone page with no charts or documents can keep custom
  properties alone.

### The 2025.10 token format

Several tools read it, and its color objects keep the color space a hex string loses. **Cost:**
strict shapes, and tools still catching up.

### Even steps, measured as shipped, never rounded

- **The reason:** equal OKLCH lightness steps look even. WCAG's ratio uses sRGB luminance (fact
  `vt-wcag-luminance`), and a color outside sRGB is mapped before it shows, so only the shipped
  color can be measured. A rounded 4.48 hides a failure (fact `vt-contrast-threshold`).
- **What it costs:** some brand colors need a darker step for text.
- **When to choose differently:** a ramp may come from another tool, if each shipped step is
  measured.

### Meaning that survives forced colors

- **The reason:** people who need a particular contrast choose a theme, and the browser enforces
  it over the page's colors (fact `vt-forced-colors`), leaving text, icons and border shapes.
  MDN advises small fixes in the `forced-colors` query, not a second design.
- **What it costs:** a label or icon on every status, and a pass in a contrast theme.
- **When to choose differently:** where color is the content, such as a swatch,
  `forced-color-adjust: none`, with the page meeting the user's contrast itself.

### Fallback fonts

- **The reason:** a document set in Aptos reflows where Aptos is missing, and Office reached
  it over months; other systems need a download (fact `vt-aptos`). **Cost:** one more test.

### No company palette here

This repository is public, and the owner ruled on 2026-10-15 (question 46) that an employer's
palette stays out.

## Facts

Versions, dates and defaults, each named elsewhere in this module by its ID. Checked
2026-11-16.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `vt-dtcg-status` | DTCG 2025.10: first stable version, not a W3C standard | [Announcement](https://www.w3.org/community/design-tokens/2025/), [2025.10](https://www.designtokens.org/tr/2025.10/) | "the first stable version of the Design Tokens Specification (2025.10)" and "It is not a W3C Standard" | 2026-11-16 | 2027-05-16 |
| `vt-dtcg-file` | Extensions and media type | [Format](https://www.designtokens.org/tr/2025.10/format/) | "file extensions are recommended" and "SHOULD be used for design token files: application/design-tokens+json" | 2026-11-16 | 2027-05-16 |
| `vt-dtcg-color` | `colorSpace`, `components` required; `hex` optional | [Color](https://www.designtokens.org/tr/2025.10/color/) | "colorSpace (required)" and "components (required)" and "a fallback value of the color" | 2026-11-16 | 2027-05-16 |
| `vt-dtcg-dimension` | Units `px` or `rem` | [Format](https://www.designtokens.org/tr/2025.10/format/) | "$value.unit may only be" | 2026-11-16 | 2027-05-16 |
| `vt-dtcg-alias` | Brace aliases | [Format](https://www.designtokens.org/tr/2025.10/format/) | "The curly brace syntax is specifically designed for referencing complete token values" | 2026-11-16 | 2027-05-16 |
| `vt-dtcg-resolver` | Resolver module, stable: contexts such as light and dark | [Resolver](https://www.designtokens.org/tr/2025.10/resolver/) | "work with design tokens in multiple contexts" and "considered stable" | 2026-11-16 | 2027-05-16 |
| `vt-sd-version` | Style Dictionary 5.8.0, 2026-11-03 | [npm](https://registry.npmjs.org/style-dictionary) | "5.8.0" and "2026-11-03T21:11:48.400Z" | 2026-11-16 | 2027-02-16 |
| `vt-sd-dtcg` | 5.3.0: 2025.10 colors; 5.4.0: dimension objects | [CHANGELOG](https://raw.githubusercontent.com/style-dictionary/style-dictionary/main/CHANGELOG.md) | "structured color format in color transformers" and "dimension token type object value" | 2026-11-16 | 2027-02-16 |
| `vt-sd-partial` | 2025.10 support unfinished | [DTCG page](https://styledictionary.com/info/dtcg/) | "the latest format 2025.10 does not have full support yet in Style Dictionary" | 2026-11-16 | 2027-02-16 |
| `vt-oklch` | `oklch()` Widely available since 2025-11-09 | [web-features](https://raw.githubusercontent.com/web-platform-dx/web-features/main/features/oklab.yml.dist) | "baseline_high_date: 2025-11-09" | 2026-11-16 | 2027-02-16 |
| `vt-light-dark` | `light-dark()` Newly available since 2024-05-13; needs `color-scheme` | [web-features](https://raw.githubusercontent.com/web-platform-dx/web-features/main/features/light-dark.yml.dist), [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark) | "baseline: low" and "baseline_low_date: 2024-05-13" and "the color-scheme must have a value of light dark" | 2026-11-16 | 2027-02-16 |
| `vt-wcag-luminance` | Contrast uses sRGB luminance | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | "For the sRGB colorspace, the relative luminance" | 2026-11-16 | 2027-05-16 |
| `vt-wcag-color` | 1.4.1 Use of Color | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | "Color is not used as the only visual means of conveying information" | 2026-11-16 | 2027-05-16 |
| `vt-wcag-graphics` | 1.4.11 covers graphics | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | "Parts of graphics required to understand the content" | 2026-11-16 | 2027-05-16 |
| `vt-contrast-threshold` | Ratios are not rounded | [Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | "the computed values should not be rounded (e.g., 4.499:1 would not meet the 4.5:1 threshold)" | 2026-11-16 | 2027-05-16 |
| `vt-wcag-large` | Large-scale text: 18pt, or 14pt bold; about 24px and 18.5px | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | "with at least 18 point or 14 point bold" and "14pt and 18pt are equivalent to approximately 18.5px and 24px" | 2026-11-24 | 2027-05-24 |
| `vt-forced-colors` | Forced colors, such as Windows High Contrast, override authored colors and drop shadows | [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors), [CSS Color Adjustment](https://www.w3.org/TR/css-color-adjust-1/) | "Windows High Contrast mode" and "box-shadow is forced to 'none'" and "overriding the author's chosen colors" and "only use this value when they are themselves adjusting the colors" | 2026-11-24 | 2027-05-24 |
| `vt-office-clrscheme` | An Office theme holds twelve colors | [ColorScheme](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.drawing.colorscheme?view=openxml-3.0.1) | "six accent colors, two dark colors, two light colors and a color for each of a hyperlink" | 2026-11-16 | 2027-05-16 |
| `vt-aptos` | Aptos replaces Calibri (announced 2023-07-13); a download exists | [Aptos](https://learn.microsoft.com/typography/font-list/aptos), [Microsoft Design](https://medium.com/microsoft-design/a-change-of-typeface-microsofts-new-default-font-has-arrived-f200eb16718d) | "to replace Calibri" and "Download Microsoft Aptos Fonts" and "will start appearing as the new default font" | 2026-11-16 | 2027-05-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| [DTCG 2025.10](https://www.designtokens.org/tr/2025.10/), [announcement](https://www.w3.org/community/design-tokens/2025/) | Format, status, Resolver | W3C Community Final Specification Agreement: short quotes |
| [Style Dictionary](https://styledictionary.com/), changelog, npm | Version, support | Apache-2.0: facts, short quotes |
| [web-features](https://github.com/web-platform-dx/web-features) | Baseline dates | Apache-2.0: facts, short quotes |
| [MDN](https://developer.mozilla.org/) by Mozilla Contributors | `light-dark()`, forced colors | CC BY-SA 2.5 or later: short quotes, attributed |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [CSS Color Adjustment](https://www.w3.org/TR/css-color-adjust-1/) | Contrast, use of color, forced colors | W3C document use rules (fact `web-w3c-license`): short quotes, linked |
| [Microsoft Learn](https://learn.microsoft.com/), [Microsoft Design](https://medium.com/microsoft-design) | Aptos, Office themes | Not stated: short quotes |

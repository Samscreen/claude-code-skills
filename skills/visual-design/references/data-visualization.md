# Data visualization

Read this for building or reviewing a chart, plot or dashboard: making it readable without
color, choosing a color-blind-safe palette, writing its title and text alternative, picking a
chart type, choosing a charting library for a report, a dashboard or a React app, and putting
figures into a generated document or schedule, stamped with when it was made.

Tokens, dark mode, contrast and the WCAG thresholds are `visual-theme`'s; diagrams and Mermaid
`house-style`'s `documentation`; HTML markup and alt text `coding`'s `html-coding`; Excel and
PowerPoint charts the business-apps skill's and Anthropic's pptx skill.

## Rules

1. **Color never carries meaning alone.** Pair each series' color with a direct label, a marker
   shape, a line style or a pattern, so the chart still reads in grayscale (fact
   `dv-wcag-use-of-color`).
2. **Use one categorical palette, exported from the theme's tokens, in a fixed order.** With no
   theme, use Okabe-Ito (facts `dv-wong-2011`, `dv-mpl-palettes`); for ordered values, viridis
   (fact `dv-viridis`). Past eight categories, group the rest as "Other" or split the chart. In
   matplotlib, pass the list to `axes.prop_cycle` with `cycler(color=palette)`; from 3.11,
   `cycler(color="okabe_ito")` names the default.
3. **State the takeaway in words, and offer the data.** The title says what the chart shows,
   the text alternative says it again with the key numbers, and a table or CSV of the plotted
   values sits beside it.
4. **Give marks and text enough contrast in every theme.** Chart text meets the text threshold
   (fact `web-wcag-contrast`); a mark the reader needs meets 3:1 against its neighbors (fact
   `web-wcag-nontext`). Measure each color on the background it is drawn on.
5. **Fit the chart to the comparison it makes,** by the table below.
6. **Choose the library by where the chart lands,** take its version from the Facts, and pin it
   as the project-bootstrap-and-audit standard's dimension 8, *Dependencies*, says.
7. **Compute every figure and every number in a generated document in one run,** from the same
   data, so the text can't disagree with the chart. **Stamp it,** and any generated plan or
   schedule, with when it was generated and when its data was loaded, as absolute 24-hour
   times with their zone: "Generated 2026-11-24 14:05 UTC from data loaded 06:00 UTC".

### Chart types

| Comparison | Use | Avoid |
|---|---|---|
| Change over time | Line; bars for a few periods | A pie per period |
| Amounts across categories | Bars from zero, sorted | Bars on a cut axis, 3D |
| Part of a whole | Stacked bar; a pie only up to about five slices | Many thin slices |
| Two measures, one per item | Scatter | Two y-axes on one chart |
| Distribution | Histogram, box or strip plot | A bar of the mean alone |
| Exact values matter | A table | A chart readers must measure |

### Libraries

| Library | Where it fits | Version | Activity |
|---|---|---|---|
| matplotlib | Python, static figures | fact `dv-matplotlib` | Active |
| seaborn | Python statistical plots on matplotlib | fact `dv-seaborn` | No release since January 2024 |
| plotly | Python and JavaScript, interactive | fact `dv-plotly` | Active; 7.x since August 2026 |
| Altair | Python, writes Vega-Lite specs | fact `dv-altair` | Active |
| Vega-Lite | JSON chart specs, on the web | fact `dv-vega-lite` | Active |
| D3 | JavaScript, any custom chart | fact `dv-d3` | Rare: none from March 2024 to November 2026 |
| Observable Plot | JavaScript, short web charts | fact `dv-plot` | Active; still 0.x |
| ECharts | JavaScript, dashboards | fact `dv-echarts` | Active |
| Chart.js | JavaScript, canvas charts | fact `dv-chartjs` | Active |
| Recharts | React | fact `dv-recharts` | Active |

- **Static reports and generated documents:** matplotlib, or Altair when the chart should be a
  spec kept as data. seaborn suits a quick statistical view, since it draws with matplotlib.
- **Interactive dashboards:** ECharts, which has had dark mode since 6.0; Vega-Lite, or Altair
  from Python; plotly from Python. Observable Plot for short web charts, and it takes
  `light-dark()` colors (fact `dv-plot`). D3 only for a chart no library draws.
- **React apps:** Recharts, whose accessibility layer is on by default (fact `dv-recharts`).
  Chart.js draws on a canvas, which holds no text, so its alternative and table carry it all.

## Mistakes

- **A legend as the only key, in red and green.** A reader with a color vision deficiency, or a
  grayscale print, can't match lines to names. Label each line at its end and vary the markers.
- **A hex list typed into the chart code.** It drifts from the theme and ignores dark mode.
  Export the palette from the tokens and read it in every chart.
- **A rainbow map such as `jet` for ordered values.** Its lightness doesn't rise steadily, so
  it shows bands the data hasn't got. Use viridis, or a diverging map around a real midpoint.
- **A title that names the axes,** such as "Sales by region", and alt text that says "chart".
  Both leave the reader to find the point. Write the finding.
- **Stale library advice,** which AI assistants repeat: "matplotlib 3.10", "Altair 5", "plotly
  6", seaborn called active, or D3 called abandoned. Read the Facts.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Color alone tells series apart | A legend-only key; no labels, markers, dashes or patterns | `GAP` | Direct labels and a second channel (fact `dv-wcag-use-of-color`) |
| Palette not from the tokens | Hex lists or library defaults in chart code | `DRIFT` | Export one ordered palette from the tokens |
| Palette not color-blind-safe | Red-green pairs; `jet` or `rainbow` maps | `GAP` | Okabe-Ito or a Petroff cycle; viridis for ordered values |
| No takeaway or data | Axis-name titles; empty or generic alt text; no table or download | `GAP` | Title and alt text state the finding; offer the values |
| Low contrast | Marks under 3:1 or text under the text threshold, in either theme | `GAP` | Facts `web-wcag-nontext`, `web-wcag-contrast` |
| Wrong chart for the comparison | Bars on a cut axis, two y-axes, 3D, many-slice pies | `DRIFT` | The chart-type table |
| Library version stale or unpinned | Lock file and manifest against the Facts | `DRIFT` | Pin a current release |
| Figures and text from different runs | Numbers typed in prose; images committed beside the source | `DRIFT` | Render both from one run |
| No provenance | A generated report or schedule without when it was made and its data loaded | `GAP` | Both stamps, absolute, with zone |

## Why

### Color alone

**The reason.** WCAG makes it Level A, the lowest bar (fact `dv-wcag-use-of-color`). Color
vision deficiency, grayscale print and washed-out projectors strip the hue. **What it costs.**
Labels take room, and past five or so series they crowd: split into small multiples. **When to
choose differently.** In a heatmap the color is the value itself; offer the numbers on hover or
in a table instead.

### One palette, from the tokens

**The advice.** One ordered categorical palette in the tokens, built for each chart library.
**The reason.** A second hex list drifts from the first, and charts then miss the theme and its
dark mode. **What others do.** Wong's palette, published in Nature Methods, is the one matplotlib
now ships as `okabe_ito`, chosen to stay distinct under common color vision deficiencies and in
print; the Petroff cycles aim to be pleasant as well as accessible (facts `dv-wong-2011`,
`dv-mpl-palettes`). viridis has been matplotlib's default colormap since 2.0 (fact
`dv-viridis`), and matplotlib 3.10 added diverging maps for dark backgrounds. **What it costs.**
A build step per chart library, and a brand palette may not be color-blind-safe: test it, and
keep Okabe-Ito when it fails. **When to choose differently.** A throwaway exploration plot can
keep the library's accessible default.

### The takeaway and the data

**The reason.** A screen reader gets only the text alternative (fact `web-wcag-alt`), and a
table lets anyone check a number the chart only suggests. This is this repository's practice:
the research behind this module didn't cover published chart-accessibility guidance. **What it
costs.** Writing the takeaway forces a conclusion; an exploration chart has none, so describe
what it shows instead.

### Contrast of marks and text

**The reason.** WCAG holds a part of a graphic the reader needs to 3:1 (fact
`web-wcag-nontext`); decorative gridlines aren't held, and can stay faint. **What it costs.**
Pastel palettes and light gray labels fail on white.

### Chart types

This table is this repository's practice, not drawn from a published guide: the research for
this module didn't cover chart-choice references. Its reasons: bars encode length, so a cut
axis exaggerates a difference; a line shows a trend that separate bars break up; slice angles
are hard to compare once there are many; two y-axes invite a link the scales chose; and a table
is best when the reader needs the exact value. **When to choose differently.** A field with its
own conventions, such as a candlestick chart in finance, follows them.

### Libraries

**The reason.** Releases and activity differ a lot: seaborn hasn't released since January 2024,
while plotly moved to 7.x in August 2026 (facts `dv-seaborn`, `dv-plotly`). AI assistants
repeat versions from their training data. **What it costs.** A 0.x library such as Observable
Plot can change its API in a minor release; pin it exactly.
**When to choose differently.** A project already on one library keeps it unless it fails a
rule here.

### One run for figures and text

**The advice.** Draw each figure and print each number in the document from code, in one render
from one dataset: Quarto does this for prose and code together (fact `dv-quarto`), as do
Jupyter and knitr. **The reason.** A number typed by hand stays put when the data changes, and
the chart beside it moves. This is this repository's practice; the research found no primary
source for it. **What it costs.** The render needs the data and the tools at build time. Record
the version of each tool that drew a figure.

**Provenance.** A saved or printed report outlives the screen it came from. Two copies that
disagree can only be told apart by when each ran and how old its data was, and a schedule built
on yesterday's load looks like one built on today's. "3 hours ago" is wrong once saved, and a
12-hour time with no AM or PM is two times. Our practice, from a production application's audit. **What it costs.** A line on each report. **When to choose differently.** A live
dashboard may show the data's age, with the absolute stamp beside it.

## Facts

Versions, dates and defaults, each named elsewhere in this module by its ID. Checked 2026-11-16.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `dv-wcag-use-of-color` | WCAG 2.2 1.4.1 Use of Color (A): never color alone | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | "Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element." | 2026-11-16 | 2027-05-16 |
| `dv-wong-2011` | Wong, Nature Methods 8, 441 (2011): a palette for color-blind readers | [Nature Methods](https://www.nature.com/articles/nmeth.1618) | "Here I offer guidelines to make graphics accessible to those with color vision deficiencies." | 2026-11-16 | 2027-05-16 |
| `dv-mpl-palettes` | matplotlib 3.10 added `petroff10` and dark-mode diverging maps `berlin`, `managua`, `vanimo`; 3.11 added `okabe_ito`, `petroff6`, `petroff8` | [3.10](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html), [3.11](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html) | "It aims to be both generally pleasing aesthetically and colorblind accessible" and "Matplotlib now includes the Okabe-Ito color sequence." and "Its colors remain distinguishable for common forms of color-vision deficiency and when printed." | 2026-11-16 | 2027-02-16 |
| `dv-viridis` | viridis became matplotlib's default colormap in 2.0; CC0 | [mpl colormaps](https://bids.github.io/colormap/) | "\"option D\" (now called \"viridis\") will be the new default colormap in matplotlib 2.0" | 2026-11-16 | 2027-05-16 |
| `dv-matplotlib` | matplotlib 3.11.2 (2026-09-11); 3.11.0 was 2026-06-11 | [PyPI](https://pypi.org/pypi/matplotlib/json), [matplotlib.org](https://matplotlib.org/) | "\"version\":\"3.11.2\"" and "Jun 11, 2026 Matplotlib 3.11.0 Released" | 2026-11-16 | 2027-02-16 |
| `dv-seaborn` | seaborn 0.13.2 (2024-01-25), its latest | [PyPI](https://pypi.org/pypi/seaborn/json) | "\"version\":\"0.13.2\"" | 2026-11-16 | 2027-02-16 |
| `dv-plotly` | plotly.py 7.1.0 (2026-09-15); 7.0.0 was 2026-08-25 | [PyPI](https://pypi.org/pypi/plotly/json) | "\"version\":\"7.1.0\"" | 2026-11-16 | 2027-02-16 |
| `dv-altair` | Altair 6.3.0 (2026-09-15) builds Vega-Lite 6.4.1 specs | [PyPI](https://pypi.org/pypi/altair/json), [schema](https://raw.githubusercontent.com/vega/altair/v6.3.0/altair/vegalite/v6/schema/__init__.py) | "\"version\":\"6.3.0\"" and "SCHEMA_VERSION = \"v6.4.1\"" | 2026-11-16 | 2027-02-16 |
| `dv-vega-lite` | Vega-Lite 6.5.0 (2026-10-08) | [CHANGELOG](https://raw.githubusercontent.com/vega/vega-lite/main/CHANGELOG.md) | "# [6.5.0](https://github.com/vega/vega-lite/compare/v6.4.3...v6.5.0) (2026-10-08)" | 2026-11-16 | 2027-02-16 |
| `dv-d3` | D3 7.9.2 (2026-11-03); the release before, 7.9.0, was 2024-03-12 | [npm](https://registry.npmjs.org/d3) | "\"latest\":\"7.9.2\"" and "\"7.9.0\":\"2024-03-12T22:15:07.703Z\"" | 2026-11-16 | 2027-02-16 |
| `dv-plot` | Observable Plot 0.6.19 (2026-11-05); 0.6.18 (2026-11-03) takes `light-dark()` colors | [npm](https://registry.npmjs.org/@observablehq/plot), [CHANGELOG](https://raw.githubusercontent.com/observablehq/plot/main/CHANGELOG.md) | "\"latest\":\"0.6.19\"" and "Released November 3, 2026." and "for defining colors that adapt to the user's preferred color scheme" | 2026-11-16 | 2027-02-16 |
| `dv-echarts` | ECharts 6.1.0 (2026-05-19); 6.0 added dark mode | [npm](https://registry.npmjs.org/echarts), [ECharts 6](https://echarts.apache.org/handbook/en/basics/release-note/v6-feature/) | "\"latest\":\"6.1.0\"" and "Dark Mode Support" | 2026-11-16 | 2027-02-16 |
| `dv-chartjs` | Chart.js 4.6.1 (2026-10-22) | [npm](https://registry.npmjs.org/chart.js) | "\"latest\":\"4.6.1\"" | 2026-11-16 | 2027-02-16 |
| `dv-recharts` | Recharts 3.10.1 (2026-07-25); since 3.0.0 its accessibility layer is on by default | [npm](https://registry.npmjs.org/recharts), [API](https://recharts.github.io/en-US/api/LineChart/) | "\"latest\":\"3.10.1\"" and "Turn on accessibility support for keyboard-only and screen reader users." | 2026-11-16 | 2027-02-16 |
| `dv-quarto` | Quarto 1.11.9 (2026-10-30) is current; 1.12 is in pre-release | [download](https://quarto.org/docs/download/_download.json), [1.12](https://quarto.org/docs/prerelease/1.12/index.html) | "\"version\": \"1.11.9\"" and "Quarto 1.12 Pre-Release" | 2026-11-16 | 2027-02-16 |

## Sources

Every source, with its license and how this module uses it: quoted, adapted with a notice, or
stated in our own words with a link.

| Source | Used for | License |
|---|---|---|
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Use of color | W3C document rules: short quotes, linked |
| [Wong 2011](https://www.nature.com/articles/nmeth.1618) | The color-blind-safe palette | Publisher copyright: cited, our own words |
| [matplotlib](https://matplotlib.org/), [colormaps](https://bids.github.io/colormap/) | Palettes, colormaps, versions | PSF-based license; viridis CC0: quoted |
| PyPI and npm registry records | Versions and dates | Facts only |
| Altair, Vega-Lite, Observable Plot, ECharts, Recharts, Quarto | Features and versions | BSD-3-Clause, ISC, Apache-2.0, MIT: short quotes with notice |

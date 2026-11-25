# Interface patterns

Read this for what a current interface is built from: each platform's design language and its
toolkit, at which version; stock components against custom ones; keeping many screens
consistent; layouts for narrow and wide windows; form validation and where errors go; and
loading, empty and failed states; and a value the program corrects.

Colors and charts are the `visual-design` skill's; a heuristic review `usability-review`'s;
windows and dialogs `windows-and-dialogs`'; settings `settings-and-options`'; tests
`gui-testing`'s; reports after release `feedback-loop`'s; terminal programs
`command-line-interfaces`'. Error wording and form markup are `coding`'s `error-responses` and
`html-coding`.

## Rules

1. **Build on the toolkit that implements the platform's design language, at a supported
   release** (the table below). Check its facts before starting: several fall due within months.
2. **Use the stock component before building one.** Stock widgets pick up the platform's changes:
   libadwaita's follow the system's reduced-motion setting (fact `ip-adw-gnome50`), and macOS's
   controls took new shapes by size (fact `ip-macos-controls`). A custom control follows none of
   that until someone ports it: our practice, not a platform's stated rule.
3. **One component per pattern, used on every screen:** one error message, one empty state, one
   date field. This is our inference from GOV.UK's validation pattern, which fixes the
   components and refuses the browser's own messages because they can't match them (fact
   `ip-govuk-html5`).
4. **Lay out by window width, not by device:** Material's five size classes (fact
   `ip-size-classes`), with one pane when narrow, two at expanded and large widths, and three
   considered at extra-large (fact `ip-m3-panes`). No other platform's breakpoints were found;
   on the desktop, start from these widths and the toolkit's own adaptive widgets.
5. **Keep a power-user program dense.** A wider window shows more, a narrower one moves panes
   behind a button, and neither drops an option. Never trade a useful option for a shorter
   screen (this skill's stance); where the platform keeps compact controls, use them (fact
   `ip-macos-controls`).
6. **Validate forms on the server, on submit, with errors beside their fields.** Turn off the
   browser's validation and always check on the server (facts `ip-govuk-html5`,
   `web-owasp-validation`). On submit, put a summary at the top and each message by its field
   (fact `ip-govuk-errors`), saying how to fix it (fact `eh-govuk`). Keep what the person typed,
   and never change it unseen: a value the program corrects, such as one held to a limit, goes
   back into the field, with a message saying what changed.
7. **Fit the loading state to the wait and the area:** nothing under a second (fact
   `ip-nng-1s`), a skeleton for a whole page, a spinner for one module (fact `ip-nng-skeleton`).
   Don't promise that a skeleton feels faster: NN/g says it does and Viget's test found the
   opposite (fact `ip-viget-skeleton`).
8. **Give every view that can be empty or fail a state of its own,** saying which it is and what
   to do next: "No scans yet. Insert a disc to start." Our practice; the research found no
   primary source.

### What each platform is built from

| Platform | Design language | Toolkit | Facts |
|---|---|---|---|
| Windows | Fluent | WinUI 3 in Windows App SDK 2.x; 1.x is out of support, and 2.0's servicing ends 2027-04-29 | `ip-wasdk` |
| Web, Microsoft's look | Fluent | Fluent UI React v9 | `ip-fluent-react` |
| Android | Material 3 | Jetpack Compose Material3, Expressive APIs only from 1.5.0; Material Views frozen | `ip-m3-versions`, `ip-m3-compose-first` |
| Apple | Human Interface Guidelines, revised in 2026 | SwiftUI, AppKit, UIKit | `ip-hig-2026`, `ip-macos-controls` |
| GNOME | GNOME HIG | libadwaita 1.10 on GTK 4, whose stable series is 4.24 | `ip-gnome51`, `ip-gtk-stable`, `ip-adw-gnome50` |
| KDE | KDE HIG | Kirigami, in KDE Frameworks 6, released monthly | `ip-kf6` |

## Mistakes

- **Starting a Windows app from a Windows App SDK 1.x tutorial.** 1.x gets no fixes (fact
  `ip-wasdk`); start on the current 2.x.
- **Calling Material 3 Expressive APIs on Compose Material3 1.4.0,** where they aren't (fact
  `ip-m3-versions`), or starting new Android screens in Views (fact `ip-m3-compose-first`).
- **Pinning GTK 4.23 because GNOME 51's notes name it.** 4.23 is GTK's development series;
  build against the stable 4.24 (fact `ip-gtk-stable`).
- **A hand-drawn sidebar on GNOME** where libadwaita has one (fact `ip-adw-gnome50`). It misses
  reduced motion and the next restyle.
- **Leaving the browser's `required` bubbles on, or validating as the person tabs away.** Turn
  them off; validate on submit, and on the server.
- **Saving 100 when the field still shows 500,** or dropping a value that failed to parse.
- **A spinner that flashes on a 200 ms load,** or a skeleton for one widget. Show nothing, or
  the spinner.
- **Adopting a redesign's spacious sizes in a dense work tool,** or dropping options from narrow
  windows with no way to reach them.

## Audit

Severity uses the standard's status words.

| Check | Look for | Severity | Fix |
|---|---|---|---|
| Toolkit out of support | Windows App SDK 1.x | `BLOCKER` | A supported 2.x line |
| Support ends within six months | Windows App SDK 2.0 | `DRIFT` | Plan the move to the current 2.x |
| Custom control where a stock one exists | Hand-drawn sidebars, buttons, switches | `GAP` | The stock widget |
| One pattern, several components | Error, empty or loading markup copied per screen | `GAP` | One shared component |
| Layout by device | "tablet" or "phone" checks, not window width | `GAP` | Size classes |
| Options lost at narrow widths | Resize; count the reachable options | `GAP` | Panes behind a button; every option kept |
| Browser validation on | Forms without `novalidate` | `GAP` | Turn it off; use the error components |
| Client-only validation | A handler trusting the form's checks | `BLOCKER` | Validate on the server |
| Errors in one place only | Submit a bad form | `GAP` | A summary and each message by its field |
| Input changed unseen | A handler that clamps, rounds or drops a value and doesn't show it | `GAP` | Write it back and say so |
| An indicator for every load | Spinners on fast loads; skeletons for one module | `GAP` | By the wait and the area |
| Blank empty or failed views | No data; the network off | `GAP` | A state saying which, and what to do |
| Layout and states at each width | Code alone can't show them | `UNVERIFIABLE-HERE` | Run the program at each width |

## Why

### Toolkit and version

- **The advice:** the platform's own toolkit, on a release still serviced.
- **The reason:** the toolkit carries the platform's look, input and accessibility, and an
  unsupported release gets no fixes. Windows App SDK ships a major at most every six months,
  and each is serviced for a fixed term (fact `ip-wasdk`).
- **What others do, and why:** cross-platform toolkits, such as Qt or a web view, trade each
  platform's details for one codebase.
- **What it costs:** a move every year or so, and a toolkit per platform.
- **When to choose differently:** one codebase for several platforms, following the host's
  guidelines where the toolkit lets you.

### Stock components and one component per pattern

- **The advice:** stock widgets first, then one component per pattern.
- **The reason:** a redesign or a new system setting reaches stock widgets with the toolkit
  (facts `ip-adw-gnome50`, `ip-macos-controls`). GOV.UK keeps one error message and one
  summary, and turns browser messages off because they "cannot be made consistent" (fact
  `ip-govuk-html5`). That copied markup drifts apart is our inference; the research found no
  study of what goes wrong without a design system.
- **What it costs:** a stock widget limits a screen, and a shared component needs an owner.
- **When to choose differently:** a control the toolkit lacks, such as a waveform: build it from
  the toolkit's parts and the platform's tokens.

### Width and density

- **The advice:** size classes and panes, with density kept.
- **The reason:** Material added large and extra-large classes for desktops and external
  displays (fact `ip-size-classes`), and Apple kept small controls on macOS for dense layouts
  (fact `ip-macos-controls`).
- **What it costs:** testing each class.
- **When to choose differently:** a touch-first program needs larger targets; keep every option
  reachable all the same.

### Forms

- **The advice:** browser checks off, server checks always, errors at the top and by the field,
  on submit.
- **The reason:** browser messages can't match the rest, and client checks can be bypassed (fact
  `web-owasp-validation`). Errors shown as someone tabs away interrupt an answer not yet
  finished (fact `ip-govuk-errors`).
  A value changed out of sight leaves the screen and the record disagreeing; the first
  heuristic asks that nothing with consequences go unannounced (fact `uxr-h1-consequences`).
- **What it costs:** a round trip before a mistake shows.
- **When to choose differently:** check live where a limit can't be guessed, such as a
  character count, and say so as the person types.

### Loading states

- **The advice:** by the wait and the area, with no claim that skeletons feel faster.
- **The reason:** NN/g says a skeleton "reduces the perceived loading time" (fact
  `ip-nng-skeleton`); Viget tested 136 people and the skeleton did worst on every measure (fact
  `ip-viget-skeleton`). So choose by fit: a skeleton keeps a page's shape, a spinner marks an
  area.
- **What it costs:** a skeleton is a second layout to keep in step with the real one.
- **When to choose differently:** for long work, show progress and a Cancel, as
  `windows-and-dialogs` says.

## Facts

Versions, dates and guidance, each named elsewhere in this module by its ID.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `ip-wasdk` | Windows App SDK: stable 2.6.5 (2026-11-02); 2.0 serviced to 2027-04-29; 1.8's ended 2026-09-24; 1.7 out of support; a major at most every six months | [Release channels](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-channels) | "2.6.5 Released: 11/02/2026" and "04/29/2027" and "09/24/2026" and "Out of Support" and "Major releases no more than every six months" | 2026-11-16 | 2027-02-16 |
| `ip-fluent-react` | Fluent UI React v9: 9.75.2 (2026-11-10), MIT | [npm](https://registry.npmjs.org/@fluentui/react-components) | "\"latest\":\"9.75.2\"" | 2026-11-16 | 2027-02-16 |
| `ip-m3-versions` | Compose Material3: stable 1.4.0, 1.5.0-rc01 (2026-11-04); Expressive APIs left 1.4.0 | [Compose releases](https://developer.android.com/jetpack/androidx/releases/compose), [M3 blog](https://m3.material.io/blog/m3-expressive-motion-theming) | "November 04, 2026" and "1.4.0" and "1.5.0-rc01" and "will no longer be available in 1.4.0." | 2026-11-16 | 2027-02-16 |
| `ip-m3-compose-first` | Material 1.5.0 stable later in 2026; Views 1.14.0 the last | [Compose-first](https://m3.material.io/blog/material-is-compose-first) | "making Material Compose 1.5.0 stable." and "will be our final stable release for the Views library." | 2026-11-16 | 2027-02-16 |
| `ip-size-classes` | Five width classes; large and extra-large (from 1600dp) added for desktops | [Window size classes](https://developer.android.com/develop/ui/views/layout/use-window-size-classes) | "large and extra-large breakpoints have been added to better target desktop and connected displays." and "width ≥ 1600dp" | 2026-11-16 | 2027-05-16 |
| `ip-m3-panes` | Two panes at expanded and large; three considered at extra-large | [M3 breakpoints](https://m3.material.io/foundations/layout/breakpoints) | "Expanded and large breakpoints: Two panes are recommended" and "Extra-large breakpoints: Consider using three panes" | 2026-11-16 | 2027-05-16 |
| `ip-hig-2026` | HIG: design principles back (2026-06-08), sheet buttons moved (2026-03-24) | [What's new](https://developer.apple.com/design/whats-new/) | "Reintroduced design principles." and "Updated guidance for button placement." | 2026-11-16 | 2027-05-16 |
| `ip-macos-controls` | macOS keeps small rounded controls for dense layouts | [WWDC25 session 356](https://developer.apple.com/videos/play/wwdc2025/356/) | "Mini, Small, and Medium controls will continue using rounded rectangles" and "compact, high-density layouts" | 2026-11-16 | 2027-05-16 |
| `ip-gnome51` | GNOME 51 (2026-09) names GTK 4.23 and libadwaita 1.10 | [GNOME 51](https://release.gnome.org/51/developers/index.html) | "GNOME 51 includes GTK 4.23 and Libadwaita 1.10." | 2026-11-16 | 2027-02-16 |
| `ip-gtk-stable` | GTK's stable release is 4.24.1 (2026-10-01) | [download.gnome.org](https://download.gnome.org/sources/gtk/4.24/) | "LATEST-IS-4.24.1" | 2026-11-16 | 2027-02-16 |
| `ip-adw-gnome50` | libadwaita 1.9: a sidebar replacing GtkStackSidebar; widgets follow reduced motion | [GNOME 50](https://release.gnome.org/50/developers/) | "This replaces the existing GtkStackSidebar." and "automatically support the new system-wide reduced motion preference." | 2026-11-16 | 2027-05-16 |
| `ip-kf6` | KDE Frameworks, Kirigami among them, 6.32.0 (2026-11-13), monthly | [KDE Frameworks 6.32.0](https://kde.org/announcements/frameworks/6/6.32.0/) | "KDE today announces the release of KDE Frameworks 6.32.0." and "planned monthly releases" | 2026-11-16 | 2027-02-16 |
| `ip-govuk-html5` | GOV.UK: HTML5 validation off, as its messages can't match; server checks always | [GOV.UK validation](https://design-system.service.gov.uk/patterns/validation/) | "Turn off HTML5 validation." and "cannot be made consistent with the GOV.UK Design System" and "You’ll always need to carry out server side validation" | 2026-11-16 | 2027-05-16 |
| `ip-govuk-errors` | GOV.UK: on submit, a focused summary at the top and a message by each field | [GOV.UK validation](https://design-system.service.gov.uk/patterns/validation/) | "Do not validate when the user moves away from a field." and "move keyboard focus to it" and "show Error message components next to fields with errors" | 2026-11-16 | 2027-05-16 |
| `ip-nng-1s` | NN/g: no indicator under one second | [Skeleton screens](https://www.nngroup.com/articles/skeleton-screens/) | "If a page takes less than 1 second to load, skeleton screens or spinners aren’t necessary" | 2026-11-16 | 2027-05-16 |
| `ip-nng-skeleton` | NN/g: skeletons for full pages, said to feel faster; spinners for a module | [Skeleton screens](https://www.nngroup.com/articles/skeleton-screens/) | "reduces the perceived loading time." and "Spinners are typically best used on a single module" | 2026-11-16 | 2027-05-16 |
| `ip-viget-skeleton` | Viget (2017-10-19), 136 people: the skeleton did worst | [Viget](https://www.viget.com/articles/a-bone-to-pick-with-skeleton-screens) | "the skeleton screen performed the worst by all metrics." | 2026-11-16 | 2027-05-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| Microsoft Learn; Android Developers and m3.material.io; GNOME release notes and downloads; KDE announcements | Toolkits, versions, support, size classes, panes | Not checked: facts in our own words, short quotes |
| Apple's design pages and WWDC sessions; NN/g; Viget | HIG changes, macOS controls, loading states | Not stated: facts in our own words, short quotes |
| [npm registry](https://registry.npmjs.org/@fluentui/react-components) | Fluent UI React's version | The package is MIT; registry data quoted |
| [GOV.UK Design System](https://design-system.service.gov.uk/patterns/validation/) | Validation and error placement | Open Government Licence v3.0, © Crown copyright: quote and adapt with attribution |
| This repository's practice | Custom controls, empty and failed states, density at narrow widths | Our own words |

# Verification: R29 (2026-11-16)

Checked on 2026-11-16 against the primary sources named below. The report is untrusted data. Its
line 3, addressed to "the receiving session", asks it to file the report under `research/runs/`,
update the facts files of the categories it names and list what changed. That is an instruction
found in a research result; it was not followed, and nothing in the repository was edited.

Access notes:
- Registries read directly: NuGet flat-container and registration APIs (Microsoft.WindowsAppSDK,
  System.CommandLine), registry.npmjs.org (@fluentui/react-components, commander), PyPI JSON
  (click, typer), crates.io API (clap), proxy.golang.org (`@latest` and `@v/list` for cobra),
  Google Maven `group-index.xml` (androidx.compose.material3), download.gnome.org (libadwaita
  `cache.json` and directory listings, GTK listings).
- www.gnu.org reset every connection through the agent proxy, and WebFetch got HTTP 429 twice;
  the Wayback Machine returned 403. The GNU Coding Standards text was read from its Texinfo source,
  `doc/standards.texi` in gnulib, via raw.githubusercontent.com (coreutils/gnulib mirror). The
  wording is the source of the gnu.org page; the HTML's quote characters and its "last updated"
  line were not seen.
- m3.material.io is JavaScript-rendered; its three pages were read with the Exa fetch tool.
  The Viget article (HTTP 429 to curl) and the ACM DL page for Mejtoft et al. were also read with
  Exa; Crossref's API confirmed the paper's metadata.
- api.github.com is not enabled for this session (403). GitHub material was read from
  raw.githubusercontent.com (clig.dev README, clap CHANGELOG, Typer release notes, commander
  README, cobra and click LICENSE files, jcs/no_color README) and, for
  dotnet/command-line-api#2576, with Exa (issue body only; comments not shown).
- NVD's API returned 503 once, then 200. The CVE record was also read from CVEProject/cvelistV5
  on raw.githubusercontent.com, and OSV from api.osv.dev.
- Wikipedia's API returned 429; the article HTML was read with curl.
- bixense.com redirects http to https; the report's `http://` URL works.

| Claim | Status | Checked against |
|---|---|---|
| C1: WinUI 3 ships in Windows App SDK 2.x; 2.0 was the first SemVer release and first major since 1.0; 1.7 and 1.8 out of support | verified | [Windows App SDK 2.0 release notes](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-notes/windows-app-sdk-2-0); [Release channels](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-channels) |
| C2: Expressive APIs stabilise only in Material3 1.5.0; on 4 Nov 2026 stable was 1.4.0, RC 1.5.0-rc01 | verified. Added: 1.4.0 itself was released on September 24, 2025 (the report had "date not found") | [Compose releases](https://developer.android.com/jetpack/androidx/releases/compose); [Compose Material 3 releases](https://developer.android.com/jetpack/androidx/releases/compose-material3); [Google Maven group-index](https://dl.google.com/android/maven2/androidx/compose/material3/group-index.xml) |
| C3: HIG revised in 2026: design principles reintroduced 8 June 2026, sheet button placement 24 March 2026 | verified (the WWDC 2026 Liquid Glass revision is secondary only, see row 17) | [Apple: What's new](https://developer.apple.com/design/whats-new/) |
| C4: GNOME 51 (September 2026) with libadwaita 1.10 | verified with a correction: the GNOME 51 page does say "GTK 4.23", but 4.23 is GTK's development series; the stable GTK released for GNOME 51 is 4.24.0 (11 Sep 2026), now 4.24.1 (1 Oct 2026), with 4.25.0 (6 Nov 2026) the next development line. libadwaita 1.10.0 was released on 14 Sep 2026 | [What's New for Developers in GNOME 51](https://release.gnome.org/51/developers/index.html); [download.gnome.org gtk](https://download.gnome.org/sources/gtk/); [download.gnome.org libadwaita 1.10](https://download.gnome.org/sources/libadwaita/1.10/) |
| C6: GNU and POSIX argument conventions current; GNU's options-anywhere is "not what POSIX specifies; it is a GNU extension"; GNU standards "updated 27 April 2026" | verified with a correction: the text is verified (POSIX.1-2024 chapter 12 at source; GNU wording in its Texinfo source). The "27 April 2026" date is unverifiable (gnu.org unreachable); gnulib's current source carries `@set lastupdate November 4, 2026` | [POSIX.1-2024 ch. 12](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html); [gnulib doc/standards.texi](https://raw.githubusercontent.com/coreutils/gnulib/master/doc/standards.texi) |
| C7: skeleton vs spinner is contested; NN/g "makes no speed claim we could quote"; Mejtoft et al. and Viget results | verified with a correction: the Mejtoft and Viget quotes and figures are verified at source. But NN/g does make a perceived-speed claim: "reduces the perceived loading time" and "Create the illusion of a shorter wait time." The contest is NN/g's claim against Viget's test (skeleton worst: 2.82 s perceived vs 2.41 spinner, 2.29 blank; n = 39/39/58) and Mejtoft's non-significant result | [NN/g: Skeleton Screens 101](https://www.nngroup.com/articles/skeleton-screens/) (published 2023-06-04); [Viget, 19 Oct 2017](https://www.viget.com/articles/a-bone-to-pick-with-skeleton-screens); [ACM DL, ECCE '18](https://dl.acm.org/doi/10.1145/3232078.3232086) |
| 1: Windows App SDK stable 2.6.5, released 11/02/2026 | verified (NuGet publish stamp 2026-11-03T02:50Z) | [Release channels](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-channels); [NuGet API](https://api.nuget.org/v3-flatcontainer/microsoft.windowsappsdk/index.json) |
| 2: 2.0 end of servicing 04/29/2027 | verified (row: 2.0, 04/29/2026, 2.6.5, 11/02/2026, Current, 04/29/2027) | [Release channels](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-channels) |
| 3: 1.8 ended 24 Sep 2026; 1.7 out of support since 18 Mar 2026 | verified. Note: the table still labels 1.8 "Maintenance" with end of servicing 09/24/2026 (now past); 1.7 is "Out of Support", 03/18/2026 | same |
| 4: Stable majors "no more than every six months" | verified | same |
| 5: Experimental 2.6.6-experimental, 11/06/2026 | verified (NuGet 2026-11-07T00:58Z) | same; NuGet API |
| 6: 2.0 content: XAML conditionals, Storage Pickers, popup APIs | verified | [2.0 release notes](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-notes/windows-app-sdk-2-0) |
| 7: Fluent UI React v9 at 9.75.0, published "2 days ago" on 15 Nov 2026 | contradicted: 9.75.0 was published 2026-10-27; latest is 9.75.2, 2026-11-10 (9.75.1 on 2026-11-02); licence MIT | [npm registry](https://registry.npmjs.org/@fluentui/react-components) |
| 8: compose.material3 stable 1.4.0, RC 1.5.0-rc01, November 04, 2026 | verified | [Compose releases](https://developer.android.com/jetpack/androidx/releases/compose) |
| 9: "Later in 2026, we'll promote M3 Expressive experimental APIs, making Material Compose 1.5.0 stable." | verified (post dated May 19, 2026) | [Material Android is Compose-first](https://m3.material.io/blog/material-is-compose-first) |
| 10: Material Views has its final release | verified: "Material Views 1.14.0 (MDC-Android) will be our final stable release for the Views library"; it is now in maintenance mode | same |
| 11: Expressive APIs move to 1.5.0 alphas and leave 1.4.0 | verified (post dated May 20, 2025) | [Adding Motion Physics with Jetpack Compose](https://m3.material.io/blog/m3-expressive-motion-theming) |
| 12: Five window size classes incl. large (1200–1600dp) and extra-large (≥1600dp) | verified | [Use window size classes](https://developer.android.com/develop/ui/views/layout/use-window-size-classes) |
| 13: 1 / 2 / 3 panes by breakpoint | verified | [M3 Breakpoints](https://m3.material.io/foundations/layout/breakpoints) |
| 14: M3 Expressive announced 13 May 2025 | secondary only (TechCrunch; not rechecked) | — |
| 15: HIG change log: design principles, tab bars, sheets | verified | [Apple: What's new](https://developer.apple.com/design/whats-new/) |
| 16: macOS Mini/Small/Medium rounded rectangles; Large capsule; new X-Large | verified (transcript) | [WWDC25 session 356](https://developer.apple.com/videos/play/wwdc2025/356/) |
| 17: Liquid Glass revised at WWDC 2026 with a user slider | secondary only (Wikipedia text matches the quote; it cites 9to5Mac, June 8, 2026) | [Wikipedia: Liquid Glass](https://en.wikipedia.org/wiki/Liquid_Glass) |
| 18: GNOME 51 includes GTK 4.23 and libadwaita 1.10 | verified with a correction: quote is exact, but see C4 (stable GTK is 4.24) | [GNOME 51 developers](https://release.gnome.org/51/developers/index.html) |
| 19: GNOME 51 released the week of 11–18 Sep 2026 | verified ("This week we released GNOME 51!", post dated September 18, 2026) | [TWIG #266](https://thisweek.gnome.org/posts/2026/09/twig-266/) |
| 20: libadwaita 1.10 changes | verified | [GNOME 51 developers](https://release.gnome.org/51/developers/index.html) |
| 21: libadwaita 1.9 AdwSidebar, AdwViewSwitcherSidebar replaces GtkStackSidebar | verified | [GNOME 50 developers](https://release.gnome.org/50/developers/) |
| 22: Most widgets support reduced motion | verified | same |
| 23: KDE Frameworks 6.32.0, 13 November 2026 | verified | [KDE Frameworks 6.32.0](https://kde.org/announcements/frameworks/6/6.32.0/) |
| 24: KDE Frameworks monthly | verified (same sentence on 6.29.0 and 6.32.0) | [KDE Frameworks 6.29.0](https://kde.org/announcements/frameworks/6/6.29.0/) |
| 25: POSIX Guideline 3, single alphanumeric option names | verified | [POSIX.1-2024 ch. 12](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html) |
| 26: POSIX Guideline 5, grouping | verified | same |
| 27: POSIX Guideline 10, `--` | verified | same |
| 28: GNU: "--version" and "--help" for all programs | verified with a correction: wording verified in the Texinfo source; the report's straight single quotes are not what Texinfo renders (`@samp` becomes ‘…’ in makeinfo HTML), and the gnu.org page itself was not seen | [gnulib standards.texi](https://raw.githubusercontent.com/coreutils/gnulib/master/doc/standards.texi) |
| 29: GNU: long options equivalent to single-letter ones | verified | same |
| 30: NO_COLOR rule | verified | [no-color.org](https://no-color.org/) |
| 31: CLICOLOR deprecated in favour of FORCE_COLOR / NO_COLOR | verified (sentence begins "Note: ") | [bixense.com/clicolors](https://bixense.com/clicolors/) |
| 32: clig.dev colour rules (quoted from a Vercel preview build) | verified with a correction: live clig.dev reads "The NO_COLOR environment variable is set and it is not empty (regardless of its value)." and adds "stdout or stderr is not an interactive terminal (a TTY)." Cite clig.dev, not the preview URL | [clig.dev](https://clig.dev/) |
| 33: clig.dev is CC BY-SA 4.0 | verified | [README (raw)](https://raw.githubusercontent.com/cli-guidelines/cli-guidelines/main/README.md) |
| 34: Python 3.15 released 9 October 2026 | verified | [What's new in 3.15](https://docs.python.org/3/whatsnew/3.15.html) |
| 35: argparse `suggest_on_error` defaults to True | verified | same |
| 36: argparse coloured help from 3.14 | verified | [What's new in 3.14](https://docs.python.org/3.14/whatsnew/3.14.html) |
| 37: Click 8.5.1, 6 Nov 2026, BSD-3-Clause | verified (2026-11-06T17:36Z; `license_expression` BSD-3-Clause; requires Python ≥3.10) | [PyPI JSON](https://pypi.org/pypi/click/json) |
| 38: CVE-2026-7246: NVD records the injection claim; OSV and Ubuntu mark it disputed | verified with a correction: NVD and the CVE record itself are now marked disputed too. The CNA (certcc) record carries tag `disputed` (updated 2026-08-18) and NVD (last modified 2026-10-26) carries the same description: "This CVE record was assigned not following CNA/CVE rules and is not considered a valid vulnerability by the Pallets Click project." Affected: < 8.3.3; 8.3.3 released 2026-04-22 | [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-7246); [cvelistV5](https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/7xxx/CVE-2026-7246.json); [OSV](https://api.osv.dev/v1/vulns/CVE-2026-7246) |
| 39: Typer 0.29.1, Nov 11, 2026 | verified (2026-11-11T09:18Z; MIT) | [PyPI JSON](https://pypi.org/pypi/typer/json) |
| 40: clap 4.6.7, 2026-09-14 | verified (crates.io max stable 4.6.7; MIT OR Apache-2.0; MSRV 1.85) | [crates.io API](https://crates.io/api/v1/crates/clap); [CHANGELOG](https://raw.githubusercontent.com/clap-rs/clap/master/CHANGELOG.md) |
| 41: clap 5.0.0 TBD behind `unstable-v5` | verified | same CHANGELOG |
| 42: cobra v1.10.2, Dec 3 2025, Apache-2.0 | verified (Go proxy: 2025-12-03T23:51:15Z; LICENSE.txt is Apache 2.0) | [proxy.golang.org @latest](https://proxy.golang.org/github.com/spf13/cobra/@latest) |
| 43: System.CommandLine 2.0.0 stable with .NET 10 GA, 11 Nov 2025 | verified with a correction: NuGet publishes 2.0.0 on 2025-11-11; the quoted sentence was not in the issue body read (comments not visible), so cite NuGet instead. Latest 2.0.x is 2.0.15 (2026-11-10) | [NuGet registration](https://api.nuget.org/v3/registration5-gz-semver2/system.commandline/index.json) |
| 44: System.CommandLine 3.0 in preview | contradicted: 3.0.0 stable was published 2026-11-10 (same day as .NET 11), MIT, targeting net10.0 and netstandard2.0; previews ran from March 2026 to rc.3 (2026-10-25) | [NuGet API](https://api.nuget.org/v3-flatcontainer/system.commandline/index.json) |
| 45: commander 15.1.0, Node ≥ 22.12.0 | verified (15.1.0 published 2026-11-07; engines `>=22.12.0`; MIT) | [npm registry](https://registry.npmjs.org/commander); [README (raw)](https://raw.githubusercontent.com/tj/commander.js/master/Readme.md) |
| 46: old majors get 12 months of security fixes | verified | same README |
| 47: GOV.UK: turn off HTML5 validation | verified | [GOV.UK validation pattern](https://design-system.service.gov.uk/patterns/validation/) |
| 48: GOV.UK: always validate server side | verified (curly apostrophe in "You’ll") | same |
| 49: NN/g: no indicator under 1 s | verified (curly apostrophe in "aren’t") | [NN/g](https://www.nngroup.com/articles/skeleton-screens/) |
| 50: NN/g: spinner for a module, skeleton for full screen | verified | same |
| Finding 4.1: Windows App SDK 2.4.0 added touchpad and mouse haptics (August 2026); 2.6.4 removed the LAF unlock for Language Model APIs | verified (2.4.0: "The August 13 stable release"; 2.6.4: "The October 27 stable release") | [What's new for developers](https://learn.microsoft.com/en-us/windows/apps/whats-new/whats-new-for-developers) |
| Finding 4.2: GOV.UK rejects HTML5 messages because they "cannot be made consistent" | verified | [GOV.UK validation pattern](https://design-system.service.gov.uk/patterns/validation/) |
| Finding 4.4: clig.dev rules (order-independent; no arbitrary abbreviations; full help on -h/--help; man pages; machine-readable output; TTY-only prompts; tell the user of state changes; dry run; `-q`; no secrets in flags) | verified (secrets wording: "Do not read secrets directly from flags.") | [clig.dev](https://clig.dev/) |
| Finding 4.4: Typer 0.26.0 vendors Click | verified (0.26.0 dated 2026-05-26; typer 0.29.1 no longer lists click in `requires_dist`) | [Typer release notes (raw)](https://raw.githubusercontent.com/fastapi/typer/master/docs/release-notes.md) |
| Section 6: .NET 8 and 9 ended 10 Nov 2026; .NET 10 LTS to Nov 2028 | verified (.NET 10 LTS ends November 14, 2028; .NET 11 STS released November 10, 2026, ends November 14, 2028) | [.NET support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) |
| Section 6: commander 15.0.0 on 29 May 2026 (cited to an npmx mirror) | verified at the registry (2026-05-29T09:16Z) | [npm registry](https://registry.npmjs.org/commander) |
| Section 6: `argparse.FileType` deprecated, pending removal in 3.20 | contradicted: 3.15 lists "The argparse.FileType type converter is deprecated." under "Pending removal in future versions", with no removal version (3.20's list names `argparse` only for its `__version__` attribute) | [What's new in 3.15](https://docs.python.org/3/whatsnew/3.15.html) |
| C2 extra: Compose Material3 1.4.0 release date | verified: September 24, 2025 | [Compose Material 3 releases](https://developer.android.com/jetpack/androidx/releases/compose-material3) |

Not checked, as the report marks them not found or not covered: C5, C8, C9, and the items in its
section 9.

## Exact quotes for facts rows

| Fact | URL | Exact quote |
|---|---|---|
| Windows App SDK 2.0 is SemVer and the first major since 1.0 | https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-notes/windows-app-sdk-2-0 | "It is also the first release on the new Semantic Versioning scheme and the first major version update since Windows App SDK 1.0 (November 2021)." |
| Stable cadence | https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-channels | "Major releases no more than every six months (plus minor/patch servicing updates as needed)" |
| Latest stable | same | "2.6.5 Released: 11/02/2026" |
| 2.0 servicing ends 2027-04-29 (table cells, in order) | same | "2.0" "04/29/2026" "2.6.5" "11/02/2026" "Current" "04/29/2027" |
| 1.8 servicing ended (table cells) | same | "1.8" "09/09/2025" "1.8.260921001" "09/24/2026" "Maintenance" "09/24/2026" |
| Compose Material3 versions (table cells) | https://developer.android.com/jetpack/androidx/releases/compose | "compose.material3" "November 04, 2026" "1.4.0" "1.5.0-rc01" |
| Expressive leaves 1.4.0 | https://m3.material.io/blog/m3-expressive-motion-theming | "When 1.4.0 goes to stable, the Material Expressive APIs will move to the next alpha (1.5.0-alphaX), and will no longer be available in 1.4.0." (U+2019 not involved) |
| 1.5.0 stable later in 2026 | https://m3.material.io/blog/material-is-compose-first | "Later in 2026, we’ll promote M3 Expressive experimental APIs, making Material Compose 1.5.0 stable." (curly apostrophe U+2019 in "we’ll") |
| Views frozen | same | "Material Views 1.14.0 (MDC-Android) will be our final stable release for the Views library." |
| Large and extra-large size classes | https://developer.android.com/develop/ui/views/layout/use-window-size-classes | "Additionally, large and extra-large breakpoints have been added to better target desktop and connected displays." |
| Size class bounds (table cells) | same | "1200dp ≤ width < 1600dp" and "width ≥ 1600dp" (U+2264, U+2265) |
| Panes by breakpoint | https://m3.material.io/foundations/layout/breakpoints | "Expanded and large breakpoints: Two panes are recommended" and "Extra-large breakpoints: Consider using three panes" |
| HIG design principles back | https://developer.apple.com/design/whats-new/ | "Reintroduced design principles." (entry dated June 8, 2026) |
| HIG sheets change | same | "Updated guidance for button placement." (Sheets entry dated March 24, 2026) |
| macOS control sizes | https://developer.apple.com/videos/play/wwdc2025/356/ | "On macOS, Mini, Small, and Medium controls will continue using rounded rectangles, making them a great fit for compact, high-density layouts like inspector panels." |
| GNOME 51 toolkits | https://release.gnome.org/51/developers/index.html | "GNOME 51 includes GTK 4.23 and Libadwaita 1.10." |
| AdwViewSwitcherSidebar | https://release.gnome.org/50/developers/ | "This replaces the existing GtkStackSidebar." |
| libadwaita reduced motion | same | "Most widgets now automatically support the new system-wide reduced motion preference." |
| KDE Frameworks 6.32.0 | https://kde.org/announcements/frameworks/6/6.32.0/ | "KDE today announces the release of KDE Frameworks 6.32.0." (dated Friday, 13 November 2026) |
| KDE cadence | same | "This release is part of a series of planned monthly releases" |
| POSIX Guideline 3 | https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html | "Each option name should be a single alphanumeric character (the alnum character classification) from the portable character set." |
| POSIX Guideline 5 | same | "One or more options without option-arguments, followed by at most one option that takes an option-argument, should be accepted when grouped behind one '-' delimiter." |
| POSIX Guideline 10 | same | "The first -- argument that is not an option-argument should be accepted as a delimiter indicating the end of options." |
| GNU options anywhere | https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html (text from gnulib standards.texi) | "This is not what POSIX specifies; it is a GNU extension." |
| GNU long options | same | "Please define long-named options that are equivalent to the single-letter Unix-style options." |
| GNU standard options | same | "All programs should support two standard options:" (the option names follow in `@samp`; check the HTML's quote characters before copying the rest) |
| NO_COLOR | https://no-color.org/ | "should check for a NO_COLOR environment variable that, when present and not an empty string (regardless of its value), prevents the addition of ANSI color." |
| CLICOLOR deprecated | https://bixense.com/clicolors/ | "This standard is deprecated. For new applications, we recommend using the force-color and no-color standards instead of this standard." |
| clig.dev colour | https://clig.dev/ | "The NO_COLOR environment variable is set and it is not empty (regardless of its value)." |
| clig.dev prompts | same | "Only use prompts or interactive elements if stdin is an interactive terminal (a TTY)." |
| clig.dev secrets | same | "Do not read secrets directly from flags." |
| clig.dev licence | https://raw.githubusercontent.com/cli-guidelines/cli-guidelines/main/README.md | "This work is licensed under a" followed by the link text "Creative Commons Attribution-ShareAlike 4.0 International License" |
| Python 3.15 release | https://docs.python.org/3/whatsnew/3.15.html | "Python 3.15 was released on 9 October 2026." |
| argparse suggestions on | same | "Changed the suggest_on_error parameter of argparse.ArgumentParser to default to True." |
| argparse.FileType | same | "The argparse.FileType type converter is deprecated." (under "Pending removal in future versions") |
| CVE-2026-7246 disputed | https://nvd.nist.gov/vuln/detail/CVE-2026-7246 | "This CVE record was assigned not following CNA/CVE rules and is not considered a valid vulnerability by the Pallets Click project." |
| Typer vendors Click | https://raw.githubusercontent.com/fastapi/typer/master/docs/release-notes.md | "Typer no longer depends on Click as a third party dependency, it vendors (includes the source code of) Click." |
| commander Node minimum | https://raw.githubusercontent.com/tj/commander.js/master/Readme.md | "requires at least v22.12.0." |
| commander old majors | same | "Older major versions of Commander receive security updates for 12 months." |
| GOV.UK HTML5 validation | https://design-system.service.gov.uk/patterns/validation/ | "If there’s a validation error, tell the user what’s gone wrong and how to fix it. Turn off HTML5 validation." (curly U+2019 twice) |
| GOV.UK server side | same | "You’ll always need to carry out server side validation, even if you use client side validation." (curly U+2019) |
| NN/g under 1 s | https://www.nngroup.com/articles/skeleton-screens/ | "If a page takes less than 1 second to load, skeleton screens or spinners aren’t necessary" (curly U+2019) |
| NN/g perceived speed | same | "This progress indicator is used for full-page loads and reduces the perceived loading time." |
| NN/g module vs page | same | "Spinners are typically best used on a single module, like a video or a card which is on a dashboard." |
| Viget result | https://www.viget.com/articles/a-bone-to-pick-with-skeleton-screens | "We gave the test to 136 people, and the skeleton screen performed the worst by all metrics." |
| Mejtoft et al. result | https://dl.acm.org/doi/10.1145/3232078.3232086 | "The results of this paper cannot show any significant differences in any of the comparisons between the web pages." |
| .NET 8 and 9 ended | https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core | Table cells: ".NET 8" "8.0.34" "November 10, 2026" "November 10, 2026" |

## Versions found from registries

Read on 2026-11-16 (times UTC).

| Tool | Current version | Released | Registry |
|---|---|---|---|
| Microsoft.WindowsAppSDK | 2.6.5 (stable); 2.6.6-experimental | 2026-11-03T02:50Z (page: 11/02/2026); experimental 2026-11-07T00:58Z | NuGet |
| @fluentui/react-components | 9.75.2 (MIT) | 2026-11-10T16:51Z | npm |
| androidx.compose.material3 | 1.4.0 stable; 1.5.0-rc01 | 1.4.0: 2025-09-24; rc01: 2026-11-04 | Google Maven; release notes |
| libadwaita | 1.10.0 | 2026-09-14 | download.gnome.org |
| GTK | 4.24.1 stable (4.24.0 on 2026-09-11); 4.25.0 development | 2026-10-01; 4.25.0 2026-11-06 | download.gnome.org |
| KDE Frameworks (Kirigami) | 6.32.0 | 2026-11-13 | kde.org announcement |
| Python (argparse) | 3.15 | 2026-10-09 | docs.python.org |
| click | 8.5.1 (BSD-3-Clause) | 2026-11-06T17:36Z | PyPI |
| typer | 0.29.1 (MIT) | 2026-11-11T09:18Z | PyPI |
| clap | 4.6.7 (MIT OR Apache-2.0) | 2026-09-14T18:40Z | crates.io |
| cobra | v1.10.2 (Apache-2.0) | 2025-12-03T23:51Z | proxy.golang.org |
| System.CommandLine | 3.0.0 (MIT); 2.0.15 on the 2.0 line | both 2026-11-10T13:0xZ | NuGet |
| commander | 15.1.0 (MIT, Node >=22.12.0) | 2026-11-07T01:27Z | npm |

## Licences

| Source | Licence as stated | What an Apache-2.0 repository may do |
|---|---|---|
| clig.dev | CC BY-SA 4.0 (README) | Quote briefly with attribution; paraphrase. Don't copy or adapt passages: ShareAlike would bind the adapted text |
| no-color.org | No licence stated on the page or in the jcs/no_color README; no LICENSE file found | Quote briefly with a link; paraphrase. Write any check in our own code |
| POSIX.1-2024 | "Copyright © 2001-2024 The IEEE and The Open Group, All Rights Reserved" | Short quotes, cited; paraphrase |
| GNU Coding Standards | GNU Free Documentation License 1.3 or later, no invariant sections (Texinfo source) | Short quotes, cited; paraphrase. Copying larger text would bring GFDL terms |
| GOV.UK Design System | "Open Government Licence v3.0, except where otherwise stated", © Crown copyright | Quote and adapt with attribution |
| cobra | Apache License 2.0 (LICENSE.txt) | Quote, paraphrase, adapt code keeping the notice |
| click | BSD-3-Clause ("Copyright 2014 Pallets") | Quote, paraphrase, adapt code keeping the copyright and licence notice |
| typer, commander, @fluentui/react-components, System.CommandLine | MIT (registry metadata) | Adapt code keeping the MIT notice |
| clap | MIT OR Apache-2.0 (crates.io) | Adapt code under Apache-2.0 |
| NN/g, Apple HIG and WWDC, Microsoft Learn, Android Developers, m3.material.io, GNOME and KDE release notes, Viget, ACM DL | Not stated in the parts read; not checked | Short quotes with a link; paraphrase; copy no code until checked |
| Wikipedia | CC BY-SA 4.0 (site-wide; not re-read today) | Secondary: cite only as secondary, short quotes |

## Repository facts this contradicts

`git -C /home/user/claude-code-skills grep -n` over `skills/` (the standard's `references/`
excluded) for WinUI, Windows App SDK, libadwaita, GTK 4, Qt, Kirigami, Material, Liquid Glass,
Fluent, argparse, Click, Typer, System.CommandLine, NO_COLOR, CLICOLOR, clig.dev, clap, cobra,
commander, getopt, POSIX, `--help`, `--version`, exit code, sysexits, skeleton, GOV.UK,
breakpoint, `.NET 8` to `.NET 11` and `3.15`.

No Facts row in `skills/` is now wrong on the strength of this verification. The ones that touch
R29's verified claims agree with it:

- `skills/coding/references/csharp-coding.md`: `cs-dotnet8-9-end` (ended 2026-11-10 at 8.0.34
  and 9.0.23), `cs-dotnet10-lts` (to 2028-11-14) and `cs-dotnet11-sts` (shipped 2026-11-10, to
  2028-11-14) match the .NET support policy as read today. `cs-commandline-api` (beta4's
  `SetHandler` replaced by `SetAction`) still holds. Nothing there names a System.CommandLine
  version, so the 3.0.0 release contradicts no row, though a module would want it.
- `skills/coding/references/config-formats.md` `cfmt-tomllib` and
  `skills/coding/references/performance-and-concurrency.md` `pc-py-tachyon` cite Python 3.15
  and agree with its release.
- `skills/user-experience/references/windows-and-dialogs.md` (`uxw-gnome-*`, `uxw-kde-*`,
  `uxw-apple-*`, `uxw-winui-*`), `settings-and-options.md` (`uxs-kde-qt`) and `gui-testing.md`
  (`uxt-gtk4-*`) quote behaviour, not toolkit versions; R29 changes none of them.
- `skills/coding/references/error-handling.md` (`eh-posix-grep`, `eh-posix-127`, `eh-sysexits`,
  `eh-govuk`) covers exit codes and GOV.UK messages; nothing in R29 contradicts them.

No row in `skills/` names Windows App SDK, Fluent UI React, Compose Material3, libadwaita, GTK
or KDE Frameworks versions, Click, Typer, clap, cobra, commander or NO_COLOR, so R29's version
facts are new material rather than corrections.

---

# R29: Modern interfaces and consistency — platform design languages, layout and states, command-line conventions (as of 15 November 2026)

Most of what we believe still holds, with three corrections. The Windows stack moved to Windows App SDK 2.x in April 2026, and 2.0 servicing ends on 29 April 2027.\[1\]\[2\] Material 3 Expressive's Compose components are still not in a stable release: the stable line is 1.4.0 and 1.5.0 is at rc01.\[3\]\[4\] And "a skeleton feels faster than a spinner" is contested, not settled.

## 1. Summary

**TL;DR**

- **Platform toolkits changed version lines in 2026.** Windows App SDK 2.0 (WinUI 3) shipped on 29 April 2026, and its latest patch is 2.6.5 (2 November 2026). GNOME 51 shipped with libadwaita 1.10 and GTK 4.23. KDE Frameworks (which includes Kirigami) is at 6.32.0 (13 November 2026). Compose Material 3 stable is 1.4.0, and 1.5.0-rc01 (the Expressive release) came out on 4 November 2026.
- **Command-line conventions still hold and are now easier to cite.** POSIX.1-2024's Utility Syntax Guidelines and the GNU Coding Standards (updated 27 April 2026) are current. NO_COLOR is the colour opt-out that tools have settled on, and clig.dev is CC BY-SA 4.0, so do not copy its text into an Apache-2.0 repo; paraphrase it.
- **Two of our beliefs need softer wording.** Evidence that skeleton screens feel faster than spinners is contested, and in this run we could not source the empty-state guidance or the "consistency comes from reusing components" claim.

Further points:

4. Windows App SDK 1.8 left support on 24 September 2026 and 1.7 on 18 March 2026. Only 2.x is supported now, and 2.0 servicing ends on 29 April 2027, which is inside our 12-month window.\[2\]
5. Material now names five breakpoints: compact (<600dp), medium, expanded, large (1200–1599dp) and extra-large (≥1600dp). The last two exist for desktop and external displays. Material recommends two panes at expanded and large widths, and considering three at extra-large.\[5\]\[6\]\[7\]
6. Google says Material Android is "Compose-first" and has made the last Material Views release. Build new Android UI in Compose.\[8\]
7. Apple's HIG keeps a dated change log. On 8 June 2026 it reintroduced "Design principles" and updated tab bar terminology and art. On 24 March 2026 it changed button placement in sheets.\[9\]
8. On macOS, Liquid Glass keeps rounded-rectangle Mini, Small and Medium controls for dense layouts. Large controls become capsules, and there is a new X-Large size.\[10\]
9. libadwaita 1.9 (GNOME 50) added AdwSidebar and AdwViewSwitcherSidebar, which replaces GtkStackSidebar, and most widgets now follow the system reduced-motion setting.\[11\]
10. GNU requires `--version` and `--help` for all programs. POSIX Guideline 10 makes `--` the end of options. GNU's getopt allowing options anywhere among the arguments is a GNU extension, not POSIX.\[12\]\[13\]
11. The current argument parsers are Python 3.15 argparse (3.15 released 9 October 2026, `suggest_on_error` now on by default), Click 8.5.1 (6 November 2026), Typer 0.29.1 (11 November 2026), clap 4.6.7 (14 September 2026), cobra v1.10.2 (December 2025), System.CommandLine 2.0.x (stable since .NET 10) and commander 15.1.0 (needs Node.js ≥ 22.12.0).\[14\]\[15\]\[16\]\[17\]\[18\]\[19\]\[20\]\[21\]
12. Security: NVD records CVE-2026-7246 as "Pallets Click, versions 8.3.2 and below, contain a command injection vulnerability in the click.edit() function", fixed in 8.3.3. OSV and Ubuntu now list it as "[DISPUTED]", and the Pallets project does not consider it a valid vulnerability. Upgrade to 8.3.3 or later anyway.
13. GOV.UK's guidance is to turn off HTML5 validation, always validate on the server, and show an error message next to each field that has an error.\[22\]\[23\]
14. NN/g's guidance is to show no indicator for loads under 1 second, to use skeleton screens for whole-page loads under 10 seconds, and to use spinners for single modules.\[24\]
15. clap has 5.0 breaking changes\[19\] waiting behind an `unstable-v5` flag. System.CommandLine 3.0 is in preview and tied to .NET 11. Both are upgrades to plan for.\[19\]\[25\]

## 2. Corrections

| # | What we believed | Status | Correct fact | Source |
|---|---|---|---|---|
| C1 | "Fluent 2 (with WinUI 3)" is the Windows stack | Out of date (incomplete) | WinUI 3 now ships in **Windows App SDK 2.x**. Version 2.0 was the first major release since 1.0 and the first on Semantic Versioning (29 April 2026). Versions 1.7 and 1.8 are out of support.\[1\]\[2\] | https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-notes/windows-app-sdk-2-0 — "It is also the first release on the new Semantic Versioning scheme and the first major version update since Windows App SDK 1.0 (November 2021)." |
| C2 | Material 3 Expressive (2025) is the current Material you can build with | Partly wrong for code | Expressive was announced in May 2025, but in Compose its APIs stabilise only in **Material3 1.5.0**. On 4 November 2026 the stable release was 1.4.0 and 1.5.0 was at rc01.\[3\]\[4\]\[26\] | https://developer.android.com/jetpack/androidx/releases/compose — "compose.material3 \| November 04, 2026 \| 1.4.0 \| 1.5.0-rc01" |
| C3 | Apple HIG with Liquid Glass (2025) | Confirmed, but revised in 2026 | The HIG was revised in 2026: design principles were reintroduced (8 June 2026), sheet button placement changed (24 March 2026), and Liquid Glass was revised at WWDC 2026 (secondary).\[9\]\[27\] | https://developer.apple.com/design/whats-new/ — "Design principles Guidance … June 8, 2026 \| Reintroduced design principles." |
| C4 | GNOME HIG (libadwaita) | Confirmed; version moved | The current release is GNOME 51 (September 2026) with libadwaita 1.10.\[28\]\[29\] | https://release.gnome.org/51/developers/index.html — "GNOME 51 includes GTK 4.23 and Libadwaita 1.10." |
| C5 | clig.dev is "the most cited" CLI guide | Not verifiable | We found no citation count. clig.dev is widely referenced, but "most cited" is not sourced. Write "a widely used guide" instead. | — (not found) |
| C6 | GNU's and POSIX's argument conventions still hold | Confirmed, with a nuance | Both are current: POSIX.1-2024 and GNU standards updated 27 April 2026. GNU's options-anywhere behaviour is explicitly "not what POSIX specifies; it is a GNU extension."\[13\]\[30\] | https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html |
| C7 | A skeleton feels faster than a spinner for loads of a few seconds | **Contested** | NN/g recommends skeletons for full-page loads under 10 s but makes no speed claim we could quote. Mejtoft, Långström & Söderström, "The effect of skeleton screens" (ECCE '18, doi:10.1145/3232078.3232086), found skeletons "scored higher on average on both perceived speed and ease of navigation", but the authors "cannot show any significant differences in any of the comparisons". Viget's "A Bone to Pick with Skeleton Screens" (Faulkner & Olvera, 19 October 2017) tested 136 mobile users. The average perceived wait was 2.82 s for the skeleton, 2.41 s for a spinner and 2.29 s for a blank screen: "Users in the skeleton screen group took longer to complete the task … and guessed that the wait time had been longer." | https://www.nngroup.com/articles/skeleton-screens/ ; https://www.viget.com/articles/a-bone-to-pick-with-skeleton-screens |
| C8 | Empty states should say what goes there and how to add the first item | Not found | We found no primary source in this run. Keep it as a hypothesis until it is sourced. | — |
| C9 | A design system is tokens + components + usage guidance, and consistency comes from reusing components | Not found | We could not source this in this run (see section 9). | — |

## 3. Facts table

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| 1 | Windows App SDK current stable | 2.6.5 | https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-channels | "Stable \| Production-ready channel … \| 2.6.5 Released: 11/02/2026" | 2 Nov 2026 |
| 2 | Windows App SDK 2.0 end of servicing | 29 Apr 2027 (**within 12 months**)\[2\] | same | "\| 2.0 \| 04/29/2026 \| 2.6.5 \| 11/02/2026 \| Current \| 04/29/2027 \|" | read 15 Nov 2026 |
| 3 | Windows App SDK 1.8 / 1.7 support | 1.8 ended 24 Sep 2026; 1.7 out of support since 18 Mar 2026\[2\] | same | "\| 1.8 \| 09/09/2025 \| … \| Maintenance \| 09/24/2026 \|" ; "\| 1.7 \| … \| Out of Support \| 03/18/2026 \|" | read 15 Nov 2026 |
| 4 | Windows App SDK major release cadence | ≤ 1 major per 6 months\[2\] | same | "Major releases no more than every six months (plus minor/patch servicing updates as needed)" | read 15 Nov 2026 |
| 5 | Windows App SDK latest experimental | 2.6.6-experimental\[2\] | same | "2.6 Experimental (2.6.6-experimental) Released: 11/06/2026" | 6 Nov 2026 |
| 6 | Windows App SDK 2.0 content | XAML conditionals, Storage Pickers, popup APIs\[1\] | https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-notes/windows-app-sdk-2-0 | "Windows App SDK 2.0 ships new APIs and improvements across the platform: XAML conditionals, modern Storage Pickers, expanded popup and anchoring APIs in Microsoft.UI.Content…" | 29 Apr 2026 |
| 7 | Fluent UI React v9 package version | 9.75.0 (exact date not found; npm said "2 days ago")\[31\] | https://www.npmjs.com/package/@fluentui/react-components | "9.75.0 • Public • Published 2 days ago" | read 15 Nov 2026 |
| 8 | Compose Material3 versions | stable 1.4.0; RC 1.5.0-rc01\[4\] | https://developer.android.com/jetpack/androidx/releases/compose | "compose.material3 \| November 04, 2026 \| 1.4.0 \| 1.5.0-rc01" | 4 Nov 2026 |
| 9 | M3 Expressive goes stable in Compose 1.5.0 | planned "later in 2026"\[8\] | https://m3.material.io/blog/material-is-compose-first | "Later in 2026, we'll promote M3 Expressive experimental APIs, making Material Compose 1.5.0 stable." | read 15 Nov 2026 |
| 10 | Material Views is frozen | last release made\[8\] | same | "The final Material Views release" | read 15 Nov 2026 |
| 11 | Expressive APIs not in 1.4 | moved to 1.5 alphas\[3\] | https://m3.material.io/blog/m3-expressive-motion-theming | "When 1.4.0 goes to stable, the Material Expressive APIs will move to the next alpha (1.5.0-alphaX), and will no longer be available in 1.4.0." | read 15 Nov 2026 |
| 12 | Window size classes | 5 classes incl. large/extra-large | https://developer.android.com/develop/ui/views/layout/use-window-size-classes | "Large width \| 1200dp ≤ width < 1600dp \| Large tablet displays \| Extra-large width \| width ≥ 1600dp \| Desktop displays"\[5\] | read 15 Nov 2026 |
| 13 | Pane guidance per breakpoint | 1 / 2 / 3 panes | https://m3.material.io/foundations/layout/breakpoints | "Compact and medium breakpoints: A single pane works best … Expanded and large breakpoints: Two panes are recommended … Extra-large breakpoints: Consider using three panes"\[7\] | read 15 Nov 2026 |
| 14 | Material 3 Expressive announcement | 13 May 2025 (secondary)\[26\] | https://techcrunch.com/2025/05/13/google-unveils-its-new-android-design-language-material-3-expressive/ | "Google on Tuesday unveiled its new Android design language, Material 3 Expressive, at the Android Show ahead of Google I/O." | 13 May 2025 |
| 15 | Apple HIG 2026 changes | design principles back; tab bars; sheets\[9\] | https://developer.apple.com/design/whats-new/ | "Design principles Guidance … June 8, 2026 \| Reintroduced design principles." ; "Sheets Guidance … March 24, 2026 \| Updated guidance for button placement." | 8 Jun / 24 Mar 2026 |
| 16 | macOS control shapes under Liquid Glass | Mini/Small/Medium rounded rects; Large capsule; new X-Large\[10\] | https://developer.apple.com/videos/play/wwdc2025/356/ | "On macOS, Mini, Small, and Medium controls will continue using rounded rectangles … Large controls will now use capsule shapes, alongside with the new X-Large size" | Jun 2025 |
| 17 | Liquid Glass revised at WWDC 2026 | reduced transparency + user slider (secondary)\[27\]\[32\] | https://en.wikipedia.org/wiki/Liquid_Glass | "Apple also introduced a slider in each operating system's settings, allowing users to adjust the Liquid Glass interface's appearance along a spectrum from clear and transparent to tinted and frosted." | read 15 Nov 2026 |
| 18 | GNOME 51 toolkit versions | GTK 4.23, libadwaita 1.10\[29\] | https://release.gnome.org/51/developers/index.html | "GNOME 51 includes GTK 4.23 and Libadwaita 1.10." | Sep 2026 |
| 19 | GNOME 51 release | week of 11–18 Sep 2026\[28\] | https://thisweek.gnome.org/posts/2026/09/twig-266/ | "This week we released GNOME 51!" | 18 Sep 2026 |
| 20 | libadwaita 1.10 changes | CSS class binding, sidebar prefix/suffix, Android build\[29\] | https://release.gnome.org/51/developers/index.html | "Libadwaita 1.10 introduces new API for declarative styling, updates sidebar widgets, and adds Android build support." | Sep 2026 |
| 21 | libadwaita 1.9 sidebars | AdwSidebar, AdwViewSwitcherSidebar\[11\] | https://release.gnome.org/50/developers/ | "The second is AdwViewSwitcherSidebar, which allows a AdwViewStack to be navigated from a sidebar. This replaces the existing GtkStackSidebar." | Mar 2026 |
| 22 | libadwaita reduced motion | automatic in most widgets\[11\] | same | "Most widgets now automatically support the new system-wide reduced motion preference." | Mar 2026 |
| 23 | KDE Frameworks (incl. Kirigami) current | 6.32.0 | https://kde.org/announcements/frameworks/6/6.32.0/ | "Friday, 13 November 2026 KDE today announces the release of KDE Frameworks 6.32.0." | 13 Nov 2026 |
| 24 | KDE Frameworks cadence | monthly | https://kde.org/announcements/frameworks/6/6.29.0/ | "This release is part of a series of planned monthly releases" | 14 Aug 2026 |
| 25 | POSIX option names | single alphanumeric\[12\] | https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html | "Each option name should be a single alphanumeric character (the alnum character classification) from the portable character set." | 2024 |
| 26 | POSIX grouping | `-abc` allowed\[12\] | same | "One or more options without option-arguments, followed by at most one option that takes an option-argument, should be accepted when grouped behind one '-' delimiter." | 2024 |
| 27 | POSIX end of options | `--` | same | "The first -- argument that is not an option-argument should be accepted as a delimiter indicating the end of options." | 2024 |
| 28 | GNU standard options | `--version`, `--help`\[13\] | https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html | "All programs should support two standard options: '--version' and '--help'." | updated 27 Apr 2026 |
| 29 | GNU long options | match short ones\[13\] | same | "Please define long-named options that are equivalent to the single-letter Unix-style options." | 27 Apr 2026 |
| 30 | NO_COLOR rule | non-empty var disables colour\[33\] | https://no-color.org/ | "Command-line software which adds ANSI color to its output by default should check for a NO_COLOR environment variable that, when present and not an empty string (regardless of its value), prevents the addition of ANSI color." | read 15 Nov 2026 |
| 31 | CLICOLOR deprecated | use NO_COLOR / FORCE_COLOR\[34\] | http://bixense.com/clicolors/ | "This standard is deprecated. For new applications, we recommend using the force-color and no-color standards instead of this standard." | read 15 Nov 2026 |
| 32 | clig.dev colour rules | NO_COLOR, TERM=dumb, --no-color\[35\] | https://cli-guidelines-a9m0zkia9-clig.vercel.app/ (clig.dev preview build) | "The NO_COLOR environment variable is set. The TERM environment variable has the value dumb. The user passes the option --no-color." | read 15 Nov 2026 |
| 33 | clig.dev licence | CC BY-SA 4.0 | https://github.com/cli-guidelines/cli-guidelines/blob/main/README.md | "This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License." | read 15 Nov 2026 |
| 34 | Python current | 3.15, 9 Oct 2026\[18\] | https://docs.python.org/3/whatsnew/3.15.html | "Python 3.15 was released on 9 October 2026." | 9 Oct 2026 |
| 35 | argparse suggestions on by default | 3.15 | same | "Changed the suggest_on_error parameter of argparse.ArgumentParser to default to True." | 9 Oct 2026 |
| 36 | argparse coloured help | added 3.14\[36\] | https://docs.python.org/3.14/whatsnew/3.14.html | "Enable color for help text, which can be disabled with the optional color parameter to argparse.ArgumentParser." | 7 Oct 2025 |
| 37 | Click current | 8.5.1, 6 Nov 2026, BSD-3-Clause\[21\] | https://pypi.org/project/click/ | "click 8.5.1 … Released: Nov 6, 2026 … BSD-3-Clause" | 6 Nov 2026 |
| 38 | Click CVE-2026-7246 | NVD: 8.3.2 and below; fixed in 8.3.3. Now marked "[DISPUTED]" by OSV and Ubuntu; Pallets does not consider it valid | NVD record CVE-2026-7246; fix tag https://github.com/pallets/click/releases/tag/8.3.3 | "Pallets Click, versions 8.3.2 and below, contain a command injection vulnerability in the click.edit() function" | Apr 2026 |
| 39 | Typer current | 0.29.1 | https://pypi.org/project/typer/ | "0.29.1 This release — Nov 11, 2026" | 11 Nov 2026 |
| 40 | clap current | 4.6.7 | https://github.com/clap-rs/clap/blob/main/CHANGELOG.md | "## [4.6.7] - 2026-09-14" | 14 Sep 2026 |
| 41 | clap 5 pending | breaking changes | same | "## 5.0.0 - TBD *available through `unstable-v5` feature flag* ### Breaking Changes" | read 15 Nov 2026 |
| 42 | cobra current | v1.10.2, Apache-2.0 | https://pkg.go.dev/github.com/spf13/cobra | "Version: v1.10.2 … Published: Dec 3, 2025 License: Apache-2.0"\[15\] | 3 Dec 2025 |
| 43 | System.CommandLine stable | 2.0.0 with .NET 10 GA\[20\] | https://github.com/dotnet/command-line-api/issues/2576 | "with the release of .NET 10 GA, System.CommandLine has released and shipped the stable 2.0.0 version!" | 11 Nov 2025 |
| 44 | System.CommandLine 3.0 | preview | https://www.nuget.org/packages/System.CommandLine/2.0.0-beta4.22272.1 | "3.0.0-preview.2.26159.112 \| 42,405 \| 3/10/2026" | 10 Mar 2026 |
| 45 | commander current / Node minimum | 15.1.0; Node ≥ 22.12.0\[17\] | https://www.npmjs.com/package/commander | "The current version of Commander is fully supported on Long Term Support versions of Node.js, and requires at least v22.12.0." | read 15 Nov 2026 |
| 46 | commander old-major support | 12 months of security fixes\[17\] | same | "Older major versions of Commander receive security updates for 12 months." | read 15 Nov 2026 |
| 47 | GOV.UK: turn off HTML5 validation | yes | https://design-system.service.gov.uk/patterns/validation | "If there's a validation error, tell the user what's gone wrong and how to fix it. Turn off HTML5 validation." | read 15 Nov 2026 |
| 48 | GOV.UK: server-side validation | always | same | "You'll always need to carry out server side validation, even if you use client side validation." | read 15 Nov 2026 |
| 49 | NN/g: no indicator under 1 s | yes | https://www.nngroup.com/articles/skeleton-screens/ | "If a page takes less than 1 second to load, skeleton screens or spinners aren't necessary"\[24\] | read 15 Nov 2026 |
| 50 | NN/g: skeleton vs spinner placement | skeleton = full screen; spinner = module | same | "Spinners are typically best used on a single module … Skeleton screens … are better when the full screen is loading"\[24\] | read 15 Nov 2026 |

## 4. Findings

### 4.1 Platform design languages today (Priority 1)

| Language | Toolkit / library | Current stable | Released | End of support | Due within 6 months |
|---|---|---|---|---|---|
| Fluent 2 (Windows) | WinUI 3 in Windows App SDK | 2.6.5 | 2 Nov 2026 | 2.0 line: 29 Apr 2027 (**flag**) | Next major: date not found. Cadence is "no more than every six months"; an experimental 2.6.6 is out. |
| Fluent 2 (web) | Fluent UI React v9 (`@fluentui/react-components`) | 9.75.0 | exact date not found (npm said "2 days ago" on 15 Nov 2026) | not found | not found |
| Material 3 / Expressive | Jetpack Compose Material3 | 1.4.0 (1.5.0-rc01 on 4 Nov 2026) | 1.4.0 date not found | not found | 1.5.0 stable: "later in 2026" (Material blog); exact date not found |
| Material 3 (web) | Material Web | not found | — | — | — |
| Apple HIG / Liquid Glass | SwiftUI, UIKit, AppKit | SwiftUI version not found; OS line is 27 (Liquid Glass page on Wikipedia, secondary, lists 27.0.1, 28 Sep 2026) | — | not found (Apple publishes no dates) | not found |
| GNOME HIG | libadwaita on GTK 4 | 1.10 (GNOME 51); 1.9.4 on the GNOME 50 line (secondary) | Sep 2026 | not found as a date; GNOME ships every 6 months (secondary) | GNOME 52 / libadwaita 1.11: date not found (≈ March 2027 follows from the 6-month cycle; that is an inference) |
| KDE HIG | Kirigami in KDE Frameworks 6 | 6.32.0 | 13 Nov 2026 | monthly releases; per-release support not found | 6.33 expected about December 2026 (inferred from the monthly cadence) |

**What changed in 2025–2026.**

- **Windows.** The Windows App SDK 2.0 major release (29 April 2026) moved to SemVer. The 2.x line then added touchpad and mouse haptics for WinUI 3 (2.4.0, August 2026), and 2.6.4 removed the Limited Access Feature unlock requirement for the Language Model APIs.\[1\]\[37\]
- **Material.** Expressive was announced on 13 May 2025 (secondary press). In Compose its APIs were held back from 1.4.0 and are being stabilised in 1.5.0. Google has declared Android "Compose-first" and made the final Material Views release.\[3\]\[8\]\[26\]
- **Apple.** Liquid Glass arrived in June 2025. Apple's own change log shows design principles reintroduced on 8 June 2026, tab bars "Updated terminology and art" the same day, and sheet button placement changed on 24 March 2026. Wikipedia (secondary) reports that WWDC 2026 revised Liquid Glass after criticism, including a user slider from clear to tinted.\[9\]\[27\]\[38\]
- **GNOME.** libadwaita 1.9 (GNOME 50, March 2026) added AdwSidebar and AdwViewSwitcherSidebar (replacing GtkStackSidebar) and automatic reduced-motion support. libadwaita 1.10 (GNOME 51, September 2026) added AdwCssClassBinding, prefix and suffix slots on the sidebars, and Android builds.\[11\]\[29\]
- **KDE.** Kirigami changes arrive in the monthly Frameworks releases. A secondary source credits Frameworks 6.26 (May 2026) with "a new FormLayout implementation, and a Badge component".\[39\] KDE HIG revision dates were not found.

**Where they agree and disagree.**

- *Window sizes.* Material is the only one of these languages with numbered breakpoints in this run: compact <600dp, medium 600–839, expanded 840–1199, large 1200–1599, extra-large ≥1600dp.\[6\]\[40\] Fluent, Apple, GNOME and KDE breakpoint values were **not found**. libadwaita is adaptive and the GNOME 51 notes mention that "The adaptive preview in the demo … collapses the sidebar on small sizes".\[29\]
- *Navigation.* Material and GNOME converge on a sidebar or rail at wide sizes that collapses at narrow ones. Material's collapsed navigation rail "can become an expanded navigation rail in large or extra-large layouts", and libadwaita 1.9 added first-class sidebar widgets.\[7\] Apple 2025 moved toolbars and tab bars onto a floating Liquid Glass layer above content.\[38\]
- *Density.* Apple keeps small rounded controls on macOS "for compact, high-density layouts like inspector panels".\[10\] Material Expressive goes the other way, toward larger, bolder controls (secondary press).\[41\] For dense work tools, Apple's macOS guidance is the more relevant model.

### 4.2 Consistency at scale (Priority 2)

This is the thinnest area of the run. We sourced no primary documents from Carbon, Primer, Atlassian or USWDS, and no evidence on what goes wrong without a design system. What we can source:

- **GOV.UK Design System** treats validation as a shared pattern with fixed components (error message, error summary) and explains why it rejects browser defaults: "the visual style, placement and content of HTML5 error messages cannot be made consistent with the GOV.UK Design System".\[22\]\[23\] This supports the general principle that consistency comes from one component per pattern rather than copied styles. The principle itself is our inference from the guidance.
- **Platform guidance favours stock components.** Apple's HIG change log and its WWDC25 session tie the new look to system components. A secondary source states: "standard SwiftUI, UIKit, or AppKit controls pick up the new look automatically. Custom controls don't".\[32\] Material's Compose `MaterialExpressiveTheme` similarly re-skins all stock components when the theme changes (secondary: a pull request on a third-party project).\[42\] The lesson for a skill is that custom controls do not follow platform redesigns.

Inventories, lint rules, Storybook catalogues and visual regression: **not covered** (see section 9).

### 4.3 Layout, forms and states (Priority 3)

- **Layout.** Use Material's five breakpoints for desktop and web adaptive layouts where no platform-specific values exist. The breakpoints are in dp, so scaling is handled by density. Choose 1 pane below 840dp, 2 at 840–1599dp, and consider 3 at ≥1600dp.\[7\]\[40\] High-DPI guidance for Windows, macOS, GNOME and KDE was not found in this run.
- **Forms (GOV.UK).** Turn off HTML5 validation, always validate on the server, "show Error message components next to fields with errors", and tell the user "what's gone wrong and how to fix it".\[22\]\[23\]\[43\]\[44\] On timing, a GOV.UK Design System GitHub discussion quotes the component guidance: "Do not show error messages … when they move away from a field".\[45\] We did not read that guidance at source, so treat the quote as secondary. NN/g and Baymard form guidance were not sourced.
- **Loading states.** NN/g says show no indicator under 1 s, use a skeleton for full-page loads under 10 s, and use a spinner for a single module.\[24\] Whether skeletons *feel faster* is **contested** (see C7).\[46\]\[47\]\[48\] Separately, a secondary source notes that a skeleton which keeps the final geometry avoids layout shift, which is a reason to use one regardless of perceived speed.\[49\]
- **Empty, partial, error and offline states, and optimistic updates:** not found with primary sources.

### 4.4 Command-line interfaces (Priority 4)

- **Arguments.** POSIX.1-2024 sets single-character options, grouping (`-abc`) and `--` as the end of options.\[12\] GNU adds `--help` and `--version` for every program and long options that mirror the short ones. GNU also notes that permuting options anywhere among the arguments "is not what POSIX specifies; it is a GNU extension".\[13\] clig.dev adds: "If possible, make arguments, flags and subcommands order-independent", and "Don't allow arbitrary abbreviations of subcommands."\[50\]
- **Help.** clig.dev: "Show full help when -h and --help are passed."\[50\] It also says "Consider providing man pages" (a Hacker News commenter notes this softened an earlier stance; secondary).\[51\]
- **Output for people versus programs.** clig.dev says to send primary output to stdout and "Have machine-readable output where it does not impact usability".\[50\]\[52\] Turn colour off when NO_COLOR is set, when `TERM=dumb`, or when `--no-color` is passed.\[35\] A further clig.dev rule is "Only use prompts or interactive elements if stdin is an interactive terminal (a TTY)".\[50\] NO_COLOR must be non-empty to count, and CLICOLOR is deprecated in favour of NO_COLOR and FORCE_COLOR.\[34\]\[53\]
- **Quiet, state and danger.** clig.dev: provide `-q` to suppress non-essential output, and "If you change state, tell the user." Offer a dry run ("Do not run the command, but describe the changes that would occur").\[52\] Never read secrets from flags.\[50\]
- **Exit codes.** Beyond zero for success, primary guidance was not sourced. sysexits and clig.dev wording were not read.
- **Libraries.** See section 5. Python 3.15 argparse now suggests corrections for mistyped arguments by default, and help has been coloured since 3.14. Typer's official release notes for 0.26.0 (26 May 2026) say: "Typer no longer depends on Click as a third party dependency, it vendors (includes the source code of) Click."

### 4.5–4.8 Standard questions

UX writing (4.5), keyboard-first use (4.6) and onboarding (4.7): **not covered** in this run. Common mistakes (4.8): see section 7.

## 5. Tools

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| Windows App SDK (WinUI 3) | Windows native UI | 2.6.5 | 2 Nov 2026 | NuGet `Microsoft.WindowsAppSDK` (package id not verified this run) | .csproj | https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-channels |
| Fluent UI React v9 | Fluent 2 web components | 9.75.0 | exact date not found | `npm i @fluentui/react-components` | — | https://www.npmjs.com/package/@fluentui/react-components |
| Compose Material3 | Material 3 / Expressive on Android | 1.4.0 (1.5.0-rc01) | rc01: 4 Nov 2026 | Gradle `androidx.compose.material3:material3` | build.gradle(.kts) | https://developer.android.com/jetpack/androidx/releases/compose |
| libadwaita | GNOME HIG widgets | 1.10 | Sep 2026 | distribution package / Flatpak GNOME 51 runtime | — | https://release.gnome.org/51/developers/index.html |
| Kirigami (KDE Frameworks) | KDE convergent UI | 6.32.0 | 13 Nov 2026 | distribution package; build with CMake | CMakeLists.txt | https://kde.org/announcements/frameworks/6/6.32.0/ |
| argparse | Python CLI parsing (stdlib) | Python 3.15 | 9 Oct 2026 | built in | — | https://docs.python.org/3/whatsnew/3.15.html |
| Click | Python CLI | 8.5.1 | 6 Nov 2026 | `pip install click` | pyproject.toml | https://pypi.org/project/click/ |
| Typer | Python CLI from type hints | 0.29.1 | 11 Nov 2026 | `pip install typer` | pyproject.toml | https://pypi.org/project/typer/ |
| clap | Rust CLI | 4.6.7 | 14 Sep 2026 | `cargo add clap --features derive` | Cargo.toml | https://github.com/clap-rs/clap/blob/main/CHANGELOG.md |
| cobra | Go CLI | v1.10.2 | 3 Dec 2025\[15\]\[54\] | `go get github.com/spf13/cobra@v1.10.2` | go.mod | https://pkg.go.dev/github.com/spf13/cobra |
| System.CommandLine | .NET CLI | 2.0.x (2.0.0 GA 11 Nov 2025; latest patch not verified at source) | — | `dotnet add package System.CommandLine` | .csproj | https://github.com/dotnet/command-line-api/issues/2576 |
| commander | Node.js CLI | 15.1.0 | exact date not found (early Nov 2026) | `npm i commander` (Node ≥ 22.12.0) | package.json | https://www.npmjs.com/package/commander |

## 6. Changing in the next 12 months

- **Windows App SDK 2.0 servicing ends on 29 April 2027.** Plan to move to the next major, whose date is not announced. Version 1.8 has been out of support since 24 September 2026.\[2\]
- **Compose Material3 1.5.0 stable** is promised for "later in 2026" and was at rc01 on 4 November. When it ships, the Expressive APIs become stable.\[4\]\[8\] Remove experimental opt-ins then.
- **.NET 8 and .NET 9 support ended on 10 November 2026.** Microsoft's .NET Blog post ".NET 8 and .NET 9 will reach End of Support on November 10, 2026" notes that "STS releases now get 24 months of support instead of 18" and recommends .NET 10 LTS, "supported through November 2028". Any CLI built on .NET 8 or 9 is already unsupported. System.CommandLine 3.0 is in preview and is expected with .NET 11; the exact date was not found.\[25\]\[55\]
- **clap 5.0** has breaking changes queued behind `unstable-v5`, including changed help width defaults. No date has been announced.\[19\]
- **commander 14.x** gets 12 months of security fixes after 15.0.0 (29 May 2026, secondary npmx mirror).\[17\]\[56\] By inference that ends around 29 May 2027.
- **Python argparse:** `argparse.FileType` is deprecated, pending removal in 3.20 (via subagent reading the 3.15 What's New).\[18\]
- **GNOME 52 / libadwaita 1.11** around March 2027, inferred from the 6-month cycle.\[57\]

## 7. Common mistakes

- **Using libraries with flagged security holes:** for example Click 8.3.2 and below. NVD records CVE-2026-7246 as a command injection in `click.edit()`, fixed in 8.3.3. The CVE is now marked "[DISPUTED]" by OSV and Ubuntu.
- **Coding against old APIs.** Assistants trained on older code still emit System.CommandLine beta4 APIs (`SetHandler`, `CommandLineBuilder`), which 2.0 replaced (`SetAction`). A secondary source lists these changes.\[58\]\[59\] They also emit Material 3 Expressive calls expecting them in 1.4, where they are absent.\[3\]
- **Treating `NO_COLOR=0` as "colour on".** Any non-empty value disables colour.\[53\]\[60\]
- **Colouring output when not on a TTY**, or prompting when stdin is not a TTY (clig.dev).\[50\]
- **Ignoring stock components.** Building custom bars and controls that do not pick up Liquid Glass or Expressive theming (secondary).\[32\]\[61\]
- **Relying on HTML5 validation or client-only validation** (GOV.UK).\[22\]\[23\]\[43\]
- **Not found:** primary studies on AI assistants inventing platform APIs or handling only the happy path in UI code.

## 8. Sources and licences

The licence entries marked "not verified" were not confirmed in this run. The conservative defaults given for them are this report's recommendation, not a legal finding.

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| clig.dev | CC BY-SA 4.0 (verified)\[62\] | Short quotes only | Yes | No: ShareAlike conflicts with Apache-2.0 for derived text | "Command Line Interface Guidelines, clig.dev, CC BY-SA 4.0" |
| no-color.org | not verified | Short quote | Yes | The 3-line C check is trivial; rewrite it yourself | Link to no-color.org |
| POSIX.1-2024 (Open Group) | Copyright IEEE and The Open Group\[12\] | Short quotes | Yes | n/a | Cite the standard and section 12.2 |
| GNU Coding Standards | not verified in this run | Short quotes | Yes | n/a | Cite the section URL |
| Microsoft Learn | not verified | Short quotes | Yes | Do not copy samples until the licence is checked | Link and date |
| Android Developers / m3.material.io | not verified | Short quotes | Yes | Not verified | Link and date |
| Apple HIG / WWDC | not verified; treat as all rights reserved | Short quotes only | Yes | No | Link and date |
| GNOME release notes | not verified | Short quotes | Yes | Not verified | Link |
| KDE announcements | not verified | Short quotes | Yes | Not verified | Link |
| GOV.UK Design System | not verified | Short quotes | Yes | Not verified | Link |
| NN/g | not verified; commercial | Short quotes only | Yes | n/a | Link |
| Python docs | not verified | Short quotes | Yes | Not verified | Link |
| Click (PyPI) | BSD-3-Clause (verified)\[21\]\[63\] | Yes | Yes | Yes, keeping the BSD notice | Copyright notice |
| cobra | Apache-2.0 (verified)\[15\] | Yes | Yes | Yes | NOTICE / attribution |
| Wikipedia, press, blogs (secondary) | various | Short quotes | Yes | No | Link; labelled secondary |

## 9. Not found, contested, not covered

- **Contested:** whether skeleton screens feel faster than spinners (C7).
- **Not found:**
  - breakpoints or window-size guidance for Fluent, Apple, GNOME and KDE;
  - SwiftUI and Material Web versions;
  - end-of-support dates for Fluent UI React, Compose Material3, libadwaita and Kirigami;
  - exact release dates for Fluent UI React 9.75.0 and commander 15.1.0;
  - KDE HIG revision dates;
  - a citation count for clig.dev;
  - primary empty-state guidance;
  - exit-code conventions beyond 0;
  - evidence on AI assistants' UI mistakes.
- **Not covered:**
  - Q2 in depth: Carbon, Primer, Atlassian and USWDS; inventories; lint rules; Storybook catalogues; visual regression; and failure evidence;
  - Q3: NN/g and Baymard form research, high-DPI, and offline and optimistic states;
  - Q5 (UX writing);
  - Q6 (keyboard-first);
  - Q7 (onboarding and change).

## Sources

1. [Windows App SDK 2.0 release notes - Windows apps](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-notes/windows-app-sdk-2-0)
2. [Windows App SDK release channels - Windows apps](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/release-channels)
3. [Adding Motion Physics with Jetpack Compose](https://m3.material.io/blog/m3-expressive-motion-theming)
4. [Compose | Jetpack | Android Developers](https://developer.android.com/jetpack/androidx/releases/compose)
5. [Use window size classes | Views | Android Developers](https://developer.android.com/develop/ui/views/layout/use-window-size-classes)
6. [material-3-skill/skills/material-3/references/layout-and-responsive.md at master · hamen/material-3-skill · GitHub](https://github.com/hamen/material-3-skill/blob/master/skills/material-3/references/layout-and-responsive.md)
7. [Breakpoints](https://m3.material.io/foundations/layout/breakpoints)
8. [Material Android is Compose-first](https://m3.material.io/blog/material-is-compose-first)
9. [What’s new - Design - Apple Developer](https://developer.apple.com/design/whats-new/)
10. [Get to know the new design system - WWDC25 - Videos - Apple Developer](https://developer.apple.com/videos/play/wwdc2025/356/)
11. [What's New for Developers in GNOME 50](https://release.gnome.org/50/developers/)
12. [Utility Conventions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html)
13. <https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html>
14. [Releases · spf13/cobra · GitHub](https://github.com/spf13/cobra/releases)
15. [cobra package - github.com/spf13/cobra - Go Packages](https://pkg.go.dev/github.com/spf13/cobra)
16. [typer · PyPI](https://pypi.org/project/typer/)
17. [commander - npm](https://www.npmjs.com/package/commander)
18. [What’s new in Python 3.15 — Python 3.15.2 documentation](https://docs.python.org/3/whatsnew/3.15.html)
19. [clap/CHANGELOG.md at main · clap-rs/clap · GitHub](https://github.com/clap-rs/clap/blob/main/CHANGELOG.md)
20. [Announcing System.CommandLine 2.0.0-beta5 and our path to a stable release · Issue #2576 · dotnet/command-line-api · GitHub](https://github.com/dotnet/command-line-api/issues/2576)
21. [click](https://pypi.org/project/click/)
22. [Cookies on ons.gov.uk](https://service-manual.ons.gov.uk/design-system/patterns/correct-errors)
23. [Help users to Recover from validation errors](https://design-system.service.gov.uk/patterns/validation)
24. [Skeleton Screens 101 - NN/G](https://www.nngroup.com/articles/skeleton-screens/)
25. [NuGet Gallery](https://www.nuget.org/packages/System.CommandLine/2.0.0-beta4.22272.1)
26. [Google unveils its new Android design language, Material 3 Expressive](https://techcrunch.com/2025/05/13/google-unveils-its-new-android-design-language-material-3-expressive/)
27. [Liquid Glass](https://en.wikipedia.org/wiki/Liquid_Glass)
28. [#266 Fifty One!](https://thisweek.gnome.org/posts/2026/09/twig-266/)
29. [What's New for Developers in GNOME 51](https://release.gnome.org/51/developers/index.html)
30. [GNU Coding Standards 1 About the GNU Coding Standards](https://www.gnu.org/prep/standards/standards.txt)
31. [@fluentui/react-components - npm](https://www.npmjs.com/package/@fluentui/react-components)
32. [Apple Human Interface Guidelines: Best Practices & UI Kits](https://www.brilworks.com/blog/apple-human-interface-guidelines/)
33. [NO\_COLOR: disabling ANSI color output by default](https://no-color.org/)
34. [Standard for ANSI Colors in Terminals](http://bixense.com/clicolors/)
35. [Command Line Interface Guidelines](https://cli-guidelines-a9m0zkia9-clig.vercel.app/)
36. [What’s new in Python 3.14 — Python 3.14.10 documentation](https://docs.python.org/3.14/whatsnew/3.14.html)
37. [What's new: SDK, WinUI, tools - Windows apps](https://learn.microsoft.com/en-us/windows/apps/whats-new/whats-new-for-developers)
38. [Material Design vs Apple's Human Interface Guidelines in 2026](https://www.pegasusdesignsystem.com/blog/material-design-vs-apple-hig)
39. [KDE Frameworks 6.26 Brings More KIO, Kirigami, and Baloo Fixes](https://linuxiac.com/kde-frameworks-6-26-brings-more-kio-kirigami-and-baloo-fixes/)
40. [Material Design 3 Breakpoints (M3) — Default Values & Media Queries](https://1440px.com/breakpoints/material-design/)
41. [Google's flashy Material 3 Expressive is official, but it's not coming right away](https://www.androidpolice.com/material-3-expressive-official-not-coming-right-away/)
42. [Draft: material3 1.5 (Compose 1.13 beta) with the expressive theme by ctqvva · Pull Request #598 · ctqvva/JugglucoNG · GitHub](https://github.com/ctqvva/JugglucoNG/pull/598)
43. [InteractivityError messages](https://design.homeoffice.gov.uk/accessibility/interactivity/error-messages)
44. [Handling errors and validation](https://www.nationalarchives.gov.uk/design-guide/forms/checkboxes/)
45. [Error message · alphagov/govuk-design-system · Discussion #6065 · GitHub](https://github.com/alphagov/govuk-design-system/discussions/6065/)
46. [Skeleton Screens vs Spinners: Perceived Load Time - DEV Community](https://dev.to/helloashish99/skeleton-screens-vs-spinners-perceived-load-time-1nlj)
47. [Skeleton Loading Screen: The CSS and the Evidence](https://theplusaddons.com/blog/skeleton-loading-screen/)
48. [(PDF) The effect of skeleton screens: Users' perception of speed and ease of navigation](https://www.researchgate.net/publication/326858669_The_effect_of_skeleton_screens_Users%27_perception_of_speed_and_ease_of_navigation)
49. [Why Skeleton Screens Beat Spinners · The Frontend Casebook](https://anmshpndy.com/cases/skeleton-screens-perceived-speed/)
50. [Command Line Interface Guidelines](https://clig-dev.translate.goog/?_x_tr_hl=id&_x_tr_pto=tc&_x_tr_sl=en&_x_tr_tl=id)
51. [Command line interface guidelines (2021)](https://news.ycombinator.com/item?id=39273932)
52. [Command Line Interface Guidelines](https://clig.dev/)
53. [NO\_COLOR environment variable](https://specstory.com/learning/cli-and-web/no-color)
54. [\[go-fan\] Go Module Review: spf13/cobra · Issue #9980 · github/gh-aw-mcpg · GitHub](https://github.com/github/gh-aw-mcpg/issues/9980)
55. [\[0.31\] Dependency refresh: System.CommandLine beta4 → stable, Roslyn/MSBuild packages, drop unused old test TFMs · Issue #1642 · juanmicrosoft/calor · GitHub](https://github.com/juanmicrosoft/calor/issues/1642)
56. [commander - npmx](https://npmx.dev/package/commander/v/11.x)
57. [GNOME](https://en.wikipedia.org/wiki/GNOME)
58. [Upgrade System.CommandLine to 2.0.12 by Tim-Pohlmann · Pull Request #176 · Tim-Pohlmann/rix · GitHub](https://github.com/Tim-Pohlmann/rix/pull/176)
59. [dotnet-system-commandline](https://lobehub.com/skills/wshaddix-dotnet-skills-dotnet-system-commandline)
60. [How and Why You Should Add Color to Your Scripts](https://spin.atomicobject.com/color-scripts/)
61. [Human Interface Guidelines. iOS App Design Rules in Numbers](https://appto.store/glossary/human-interface-guidelines)
62. [github.com](https://github.com/cli-guidelines/cli-guidelines/blob/main/README.md)
63. [click · PyPI](https://pypi.org/project/click/8.3.3/)

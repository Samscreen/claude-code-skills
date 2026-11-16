# Verification: R30 (2026-11-16)

Checked on 2026-11-16 against the primary sources named below. The report is untrusted data. Its
line 3, addressed to "Receiving session", asks the reader to file the report under
`research/runs/`, update the facts files of the categories it names, and list what changed. That
is an instruction found in a research result: it was recorded here and not followed. Nothing in
the repository was edited.

Access notes:
- github.com HTML and the GitHub API (`gh api`, api.github.com) were blocked for repositories not
  attached to this session (HTTP 403). Used raw.githubusercontent.com for files (vscode source,
  Firefox `all.js`, KUserFeedback README, chromatic-cli CHANGELOG, licences, CNCF
  `landscape.yml`, OpenFeature `.release-please-manifest.json`), and the Exa fetch tool for the
  Playwright v1.65.0 and v1.65.1 GitHub release pages.
- support.mozilla.org returns a "Client Challenge" page to curl, WebFetch and Exa. Firefox facts
  were checked instead at the Firefox Privacy Notice (mozilla.org) and Firefox source
  (`modules/libpref/init/all.js`). The cited SUMO quotes stay unverifiable.
- developer.apple.com/forums returns a verification page. Apple's own documentation was read
  through its JSON endpoint (`developer.apple.com/tutorials/data/documentation/...json`), which
  serves the English text; that gave the English SwiftUI page the report could not read.
- EDPB Guidelines 2/2023 v2.0 were read from the PDF linked on the EDPB page (pdftotext).
- Registries: npm registry JSON (`@playwright/test`, `chromatic`, `react`), NuGet registration
  API (`CommunityToolkit.Mvvm`), PyPI JSON (`playwright`, `pytest-qt`), and Qt's
  `doc.qt.io/qt-6/qt-releases.html`.
- Not checked (secondary only in the report, and not quickly confirmable): F26, F29, the OTel
  browser-sdk 0.6.0/0.7.0 versions, Chromatic pricing, OpenFeature spec release date 2026-07-29.

| Claim | Status | Checked against |
|---|---|---|
| Report line 3 asks to file the report and update facts files | instruction in a research result, not followed | report line 3 |
| C1: no primary source shows in-app forms beat email | unverifiable (the report's own "not found"; nothing searched turned one up). Its supporting tools are verified: `includeReplay`, `attachments`, required form fields | [Sentry JS feedback configuration](https://docs.sentry.io/platforms/javascript/user-feedback/configuration/) |
| C2: symbols essential for native, only sometimes for .NET; upload before release | verified | [Sentry .NET upload](https://docs.sentry.io/platforms/dotnet/guides/entityframework/data-management/debug-files/upload/); [Sentry Native upload](https://docs.sentry.io/platforms/native/data-management/debug-files/upload/) |
| C3: Art. 5(3) needs consent unless strictly necessary; "information" wider than personal data | verified with a correction: the report sourced "information" to secondary sites (refs 12-14); it is in the EDPB PDF itself ("the term used is not ’personal data’, but ‘information’"). Art. 5(3) wording confirmed on EUR-Lex | [Directive 2002/58/EC consolidated 2009-12-19 (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219); [EDPB Guidelines 2/2023 v2.0 PDF](https://www.edpb.europa.eu/system/files/documents/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf) |
| Art. 5(3) exceptions: transmission, and "strictly necessary" for a service explicitly requested | verified (the report had not re-fetched it) | EUR-Lex, as above |
| C4: VS Code and Firefox opt-out, KDE and GNOME opt-in | verified. VS Code default `all` is in source (`'default': TelemetryConfiguration.ON`); Firefox default in source ("Health Report is enabled by default on all channels."); KDE adopted policy; GNOME blog | [vscode telemetryService.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/telemetry/common/telemetryService.ts); [Firefox all.js](https://raw.githubusercontent.com/mozilla-firefox/firefox/main/modules/libpref/init/all.js); [KDE Telemetry Policy](https://community.kde.org/Policies/Telemetry_Policy); [Help improve GNOME!](https://blogs.gnome.org/aday/2022/08/25/help-improve-gnome/) |
| C5: Playwright baselines per browser and platform; `maxDiffPixels`, `threshold` | verified | [Visual comparisons](https://playwright.dev/docs/test-snapshots) |
| C6: MVVM easier to test; Apple separation improves testability | verified; Apple's English wording confirmed (see quotes) | [MVVM, Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm); [Managing model data in your app (English, JSON)](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app) |
| F1 issue form required keys | verified | [Syntax for issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) |
| F2 element types | verified with a correction: the quote is the "Valid values" table cell, not a sentence; don't present it as running text | [Syntax for GitHub's form schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema) |
| F3 labels must pre-exist | verified | Syntax for issue forms |
| F4 `type` key | verified | Syntax for issue forms |
| F5 `id` used for URL prefill; letters, digits, `-`, `_` | verified | Syntax for GitHub's form schema |
| `projects` needs write permission | verified ("The person opening the issue must have write permissions for the specified projects.") | Syntax for issue forms |
| Issue forms "public preview" only on the Enterprise Cloud copy; main docs carry no such note | contradicted: the main docs page says "Issue forms are currently in public preview and subject to change." and the form-schema page says "GitHub's form schema is currently in public preview and subject to change." | both GitHub Docs pages above |
| F6 Sentry JS screenshot default true, SDK 8.0.0+, hidden on mobile | verified; widget minimum SDK 7.85.0 and self-hosted 24.4.2 also verified | [Set Up User Feedback (react-router)](https://docs.sentry.io/platforms/javascript/guides/react-router/user-feedback/) |
| F7 1 GB ≈ 2,500 screenshots | verified | same |
| F8 React Native `enableScreenshot` default false | verified (table row) | [RN feedback configuration](https://docs.sentry.io/platforms/react-native/user-feedback/configuration/) |
| `lastEventId`, `captureFeedback`, "Add a screenshot" / "Remove screenshot" labels | verified | [Sentry JS user feedback](https://docs.sentry.io/platforms/javascript/user-feedback/), configuration page |
| F9 upload before release | verified | Sentry Native upload |
| Late upload "up to an hour" | verified with a correction: source says "it may take up to one hour until Sentry starts using this file for new crash reports" | Sentry Native and Android upload |
| F10 no reprocessing | verified | [Sentry Android upload](https://docs.sentry.io/platforms/android/data-management/debug-files/upload/) |
| F11 per project | verified | same |
| F12 Sentry .NET "may require" | verified | Sentry .NET upload |
| F13 NuGet 3.26.1, `SentryUploadSymbols` default false | verified (rendered page and `.md`) | [Sentry .NET WinForms upload](https://docs.sentry.io/platforms/dotnet/guides/winforms/data-management/debug-files/upload/) |
| F14 Apple: retain the archive | verified with a correction: forum thread 18646 unreadable; Apple's current documentation says it directly: "You must retain the Xcode archive for each build of your app you distribute." Cite that, not the 2015 bitcode-era forum post | [Building your app to include debugging information](https://developer.apple.com/documentation/xcode/building-your-app-to-include-debugging-information) |
| F15 WER LocalDumps off by default; admin | verified | [Collecting User-Mode Dumps](https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps) |
| F16 not with custom crash reporting | verified | same |
| F17 EDPB Guidelines 2/2023 v2.0 final, 16 October 2024 | verified with a correction: the page dates the final version 16 October 2024, but the PDF says "Version 2.0 Adopted on 7 October 2024" | [EDPB guidelines page](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-22023-technical-scope-art-53-eprivacy-directive_en); PDF |
| F18 not only cookies | verified with a correction: confirmed at the EDPB PDF (primary), not just headlesslaw.com. Exact text uses curly quotes and no inner spaces: ‘similar technologies’ | EDPB PDF |
| EDPB use cases: URL and pixel tracking, local processing, IP-only, IoT reporting, unique identifier | verified | EDPB PDF |
| F19 VS Code levels, A/B needs `all` | verified with a correction: page date is `ms.date` / DateApproved 11/11/2026, not 2026-11-04. Rendered text inserts "Open in VS Code Open in VS Code Insiders" after the setting name; the Markdown source has the clean sentence | [Telemetry (VS Code)](https://code.visualstudio.com/docs/configure/telemetry); [vscode-docs source](https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/configure/telemetry.md) |
| F20 extensions not controlled by the setting | verified (same rendering note) | same |
| F21 `TelemetryLevel` and `EnableFeedback` policies since 1.99 | verified (table rows) | [Manage telemetry in enterprise environments](https://code.visualstudio.com/docs/enterprise/telemetry) |
| F22 Firefox opt-out deletes within 30 days | unverifiable at the cited SUMO page (blocked). Nearest primary: Privacy Notice (effective May 4, 2026): "when you request deletion of your Firefox data, it will be deleted within 30 days of the request". The opt-out-equals-deletion sentence was seen only in a 2021 web.archive.org copy of another SUMO article | [Firefox Privacy Notice](https://www.mozilla.org/en-US/privacy/firefox/) |
| F23 DAU ping separate control | verified with a correction: cite the Privacy Notice wording (the "Daily Usage Ping"), see quotes | Firefox Privacy Notice |
| F24 KDE opt-in | verified with a correction: the mailing-list text is a draft quoted in Volker Krause's 14 Aug 2017 reply. The adopted policy reads "application telemetry is always opt-in. That means off by default and only activated by the explicit action of the user (inaction is not good enough)." Cite the policy page | [KDE Telemetry Policy](https://community.kde.org/Policies/Telemetry_Policy); [kde-community 003820](https://mail.kde.org/pipermail/kde-community/2017q3/003820.html) |
| F25 KUserFeedback forbids unique IDs | verified | [KUserFeedback README (raw)](https://raw.githubusercontent.com/KDE/kuserfeedback/master/README.md) |
| F26 Plasma opt-in since 5.18 | secondary only (not checked) | report's KDE developer blog |
| GNOME `gnome-info-collect` shows data first, collection ended 20 Sep 2022 | verified | Help improve GNOME! |
| F27 OTel browser experimental | verified; same page lists JS Traces Stable, Metrics Stable, Logs Development | [OpenTelemetry JavaScript](https://opentelemetry.io/docs/languages/js/) |
| F28 Client SIG late 2021 | verified | [OpenTelemetry roadmap](https://opentelemetry.io/community/roadmap/) |
| F29 client semconv v0.1.0-dev | secondary only (not checked) | report's ouo11y PR |
| F30 OTel web client-apps page is a placeholder | verified with a correction: the page itself says "Content coming soon!" (last modified August 8, 2025); cite it rather than the GitHub issue | [Web (client-side apps)](https://opentelemetry.io/docs/platforms/client-apps/web/) |
| OTel graduation "May 2026" only in a vendor blog (contested) | contradicted: CNCF announced "OpenTelemetry’s Graduation"; CNCF `landscape.yml` gives graduated 2026-05-11 | [CNCF announcements, May 2026](https://www.cncf.io/announcements/2026/05/); [cncf/landscape](https://raw.githubusercontent.com/cncf/landscape/master/landscape.yml) |
| F31-F33 NN/g severity factors, scale, three evaluators | verified; article dated November 1, 1994; "market impact" sentence verified | [Severity Ratings for Usability Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/) |
| F34 OpenFeature CNCF incubating | verified; landscape: accepted 2022-06-17, incubating 2023-11-21; openfeature.dev footer "OpenFeature is a Cloud Native Computing Foundation incubating project" | [CNCF blog 2023-12-19](https://www.cncf.io/blog/2023/12/19/openfeature-becomes-a-cncf-incubating-project/); landscape.yml |
| OpenFeature spec v0.9.0 blog quotes (Jonathan Norris, August 12, 2026) | verified; repository manifest shows spec 0.9.0 | [OpenFeature Mid-2026 Update](https://openfeature.dev/blog/openfeature-mid-2026-update) |
| F35 Playwright 1.65.1, 13 Nov 2026 | verified: npm `latest` 1.65.1, 2026-11-13T21:12:37Z; GitHub release published 2026-11-13T21:46:58Z. Note PyPI `playwright` is at 1.65.2 (2026-11-14T00:28:39) | [npm @playwright/test](https://registry.npmjs.org/@playwright/test); [v1.65.1 release](https://github.com/microsoft/playwright/releases/tag/v1.65.1) (via Exa) |
| 1.65.1 "makes TypeScript class fields follow useDefineForClassFields" | contradicted: that change is in 1.65.0 ("Notable Changes ⚠" on GitHub, "Breaking Changes ⚠" on playwright.dev). 1.65.1 is two bug fixes, one a regression fix for it (#43936) | [Release notes](https://playwright.dev/docs/release-notes); GitHub v1.65.0/v1.65.1 |
| F36 Node 20 no longer tested (1.65.0, 2026-11-05) | verified; npm 1.65.0 2026-11-05T18:30:18Z; `engines.node` still `>=20` | Release notes; npm |
| 1.65 breaking: RFC 6265 cookies; proxy credentials | verified | Release notes |
| F37 per-platform baselines; lossless WebP | verified | Visual comparisons |
| F38 Chromatic bypassed builds need TurboSnap and CLI 17.7.0+ | verified; npm 17.7.0 published 2026-06-25 | [Chromatic changelog: August 2026](https://www.chromatic.com/blog/chromatic-changelog-august-2026/) |
| F39 Chromatic CLI latest 18.5.0 | verified with a correction: 18.5.0 (Wed Aug 19 2026) exists, but current is 18.14.4 (Fri Nov 13 2026; npm 2026-11-13T20:27:36Z) | [npm chromatic](https://registry.npmjs.org/chromatic); [CHANGELOG (raw)](https://raw.githubusercontent.com/chromaui/chromatic-cli/main/CHANGELOG.md) |
| F40 .NET 11 GA and .NET 8/9 end 10 Nov 2026 | verified | [Microsoft .NET and .NET Core lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-and-net-core) |
| .NET 10 end 14 Nov 2028 "from secondary sources" | verified with a correction: primary, the lifecycle page lists ".NET 10 11/11/2025 8:00:00 AM 11/14/2028 8:00:00 AM". .NET 11 has no end date on that page; "Releases and support" (ms.date 2026-11-11) says both are "supported until November 2028" | lifecycle page; [Releases and support for .NET](https://learn.microsoft.com/en-us/dotnet/core/releases-and-support) |
| F41 MVVM benefit | verified | MVVM, Microsoft Learn |
| F42 CommunityToolkit.Mvvm 8.4.2, 2026-03-25 | verified: NuGet 8.4.2 published 2026-03-25T20:26:19Z, licence MIT | [NuGet registration](https://api.nuget.org/v3/registration5-gz-semver2/communitytoolkit.mvvm/index.json) |
| Toolkit "compatible with… WinUI, WPF, and .NET MAUI" | unverifiable as worded: not on Microsoft Learn's toolkit page, which says "it can be used on any app platform: WinUI 3, UWP, WinForms, WPF, Xamarin, Uno, and more" | [MVVM Toolkit introduction](https://learn.microsoft.com/en-us/dotnet/communitytoolkit/mvvm/) |
| F43 Elm Model/View/Update | verified with a correction: the three are separate list items joined by em dashes (U+2014), not one line with " / " | [The Elm Architecture](https://guide.elm-lang.org/architecture/) |
| F44 Qt model/view | verified (page title "Qt 6.12.0") | [Model/View Programming](https://doc.qt.io/qt-6/model-view-programming.html) |
| F45 Qt support table | verified: 6.12 → 2031-09-30, 6.11 (6.11.3) → 2027-03-17, 6.10 (6.10.3) → 2026-10-07, 6.8 LTS (6.8.8) → 2029-10-08; 6.5 LTS "Ended. Extended Security Maintenance available". The table doesn't label 6.12 LTS; Qt's blog does | [Qt Releases](https://doc.qt.io/qt-6/qt-releases.html) |
| Qt 6.12.0 released 30 September 2026; blog "Qt 6.12 LTS Released!" | verified (announce list: Wed Sep 30 2026) | [Qt Wiki: Qt 6.12 Release](https://wiki.qt.io/Qt_6.12_Release); [Qt blog](https://www.qt.io/blog/qt-6.12-released) |
| F46 SwiftUI separate data model (WWDC20) | verified | [Data Essentials in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10040/) |
| Apple English: separation "promotes modularity, improves testability" | verified | Managing model data in your app (English) |
| F47 React avoid redundant state | verified with a correction: page uses curly apostrophes, "component’s" twice | [Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure) |
| React docs "v19.3" | verified with a correction: npm `react` latest is 19.3.1 (2026-10-14); version not read from the docs page | [npm react](https://registry.npmjs.org/react) |

## Exact quotes for facts rows

Straight quotes unless noted. Non-ASCII characters are named.

| Fact | URL | Exact quote |
|---|---|---|
| Issue form required keys | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms | "All issue form configuration files must begin with name, description, and body key-value pairs." |
| Labels must exist | same | "If a label does not already exist in the repository, it will not be automatically added to the issue." |
| Issue forms in preview | same | "Issue forms are currently in public preview and subject to change." |
| `id` for prefill | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema | "If provided, the id is the canonical identifier for the field in URL query parameter prefills." |
| Sentry JS screenshot default | https://docs.sentry.io/platforms/javascript/guides/react-router/user-feedback/ | "You can configure this using the enableScreenshot option, by default it is set to true." |
| Sentry screenshots on mobile | same | "Screenshots aren't supported on mobile devices, so the screenshot button will be hidden automatically in this case." |
| Sentry upload before release | https://docs.sentry.io/platforms/native/data-management/debug-files/upload/ | "Debug files should be uploaded before deploying or releasing your application so that crash reports can be processed." |
| Sentry no reprocessing | same | "Existing events and issues are not processed again." |
| Sentry per project | same | "Sentry does not access debug files stored in other projects to symbolicate crash reports." |
| Sentry .NET symbols | https://docs.sentry.io/platforms/dotnet/guides/entityframework/data-management/debug-files/upload/ | "This is especially true for mobile apps targeting Android or iOS, such as those developed with .NET MAUI." |
| Apple archive | https://developer.apple.com/documentation/xcode/building-your-app-to-include-debugging-information | "You must retain the Xcode archive for each build of your app you distribute." |
| WER LocalDumps | https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps | "This feature is not enabled by default. Enabling the feature requires administrator privileges." |
| WER and custom reporters | same | "Applications that do their own custom crash reporting are not supported by this feature." |
| Art. 5(3) consent | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219 | "only allowed on condition that the subscriber or user concerned has given his or her consent" |
| Art. 5(3) exception | same | "or as strictly necessary in order for the provider of an information society service explicitly requested by the subscriber or user to provide the service" |
| EDPB "information" | EDPB PDF (link above) | "the notion of information includes both non-personal data and personal data" |
| EDPB beyond cookies | EDPB PDF | "Article 5(3) ePD does not exclusively apply to cookies, but also to ‘similar technologies’." (U+2018, U+2019) |
| VS Code A/B needs all | https://code.visualstudio.com/docs/configure/telemetry | "To participate in the A/B experimentation and get early access to new features, you must have usage data enabled by setting telemetry.telemetryLevel to all." |
| VS Code extensions | same | "These extensions may be collecting their own usage data and are not controlled by the telemetry.telemetryLevel setting." |
| Firefox default on (source) | https://raw.githubusercontent.com/mozilla-firefox/firefox/main/modules/libpref/init/all.js | "Health Report is enabled by default on all channels." |
| Firefox DAU ping | https://www.mozilla.org/en-US/privacy/firefox/ | "Note that deselecting “Allow Firefox to send technical and interaction data to Mozilla” will not impact the Daily Usage Ping." (U+201C, U+201D) |
| Firefox deletion | same | "when you request deletion of your Firefox data, it will be deleted within 30 days of the request" |
| KDE opt-in | https://community.kde.org/Policies/Telemetry_Policy | "application telemetry is always opt-in. That means off by default and only activated by the explicit action of the user (inaction is not good enough)." |
| KDE no unique IDs | same | "we will not use any unique device, installation or user id" |
| GNOME show before upload | https://blogs.gnome.org/aday/2022/08/25/help-improve-gnome/ | "The tool shows the data that will be collected prior to uploading and, if the user consents to the upload, is then securely sent to GNOME’s servers for processing." (U+2019) |
| OTel browser | https://opentelemetry.io/docs/languages/js/ | "Client instrumentation for the browser is experimental and mostly unspecified." |
| NN/g factors | https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ | "The severity of a usability problem is a combination of three factors" |
| NN/g market impact | same | "one needs to assess the market impact of the problem" |
| OpenFeature incubating | https://www.cncf.io/blog/2023/12/19/openfeature-becomes-a-cncf-incubating-project/ | "The CNCF Technical Oversight Committee (TOC) has voted to accept OpenFeature as a CNCF incubating project." |
| OpenFeature spec 0.9.0 | https://openfeature.dev/blog/openfeature-mid-2026-update | "Specification v0.9.0 is our first spec release since v0.8.0 in March 2024." |
| Playwright per-platform | https://playwright.dev/docs/test-snapshots | "Screenshots differ between browsers and platforms due to different rendering, fonts and more, so you will need different snapshots for them." |
| Playwright Node 20 | https://playwright.dev/docs/release-notes | "Playwright no longer tests on Node.js 20." (preceded by ⚠ on the page) |
| Chromatic bypass | https://www.chromatic.com/blog/chromatic-changelog-august-2026/ | "Bypassed builds require TurboSnap enabled, and Chromatic CLI 17.7.0 or later." |
| .NET 10 and 11 support | https://learn.microsoft.com/en-us/dotnet/core/releases-and-support | ".NET 10 (Long Term Support) - supported until November 2028." |
| MVVM | https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm | "makes an application easier to test, maintain, and evolve" |
| Qt support terms | https://doc.qt.io/qt-6/qt-releases.html | "Starting with version 6.8.0, the LTS versions are supported for five years." |
| Qt model/view | https://doc.qt.io/qt-6/model-view-programming.html | "This still separates the way that data is stored from the way that it is presented to the user" |
| SwiftUI (English) | https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app | "This separation promotes modularity, improves testability, and helps make it easier to reason about how the app works." |
| React state | https://react.dev/learn/choosing-the-state-structure | "you should not put that information into that component’s state." (U+2019) |

## Versions found from registries

| Tool | Current version | Released | Source |
|---|---|---|---|
| @playwright/test | 1.65.1 (`next` 1.66.0-alpha-2026-11-15) | 2026-11-13T21:12:37Z | npm registry JSON |
| playwright (Python) | 1.65.2 | 2026-11-14T00:28:39 | PyPI JSON |
| chromatic (CLI) | 18.14.4 | 2026-11-13T20:27:36Z (CHANGELOG: Fri Nov 13 2026) | npm registry JSON; CHANGELOG |
| CommunityToolkit.Mvvm | 8.4.2 (MIT) | 2026-03-25T20:26:19Z | NuGet registration API |
| Qt | 6.12.0; 6.11.3; 6.10.3; 6.8.8 LTS (commercial only) | 6.12.0: 2026-09-30 | qt-releases page; Qt Wiki; announce list |
| .NET | 11 (GA 2026-11-10, STS); 10 LTS to 2028-11-14 | 2026-11-10 | Microsoft lifecycle page |
| react | 19.3.1 | 2026-10-14T16:47:15Z | npm registry JSON |
| pytest-qt | 4.5.0 | 2025-07-01T17:24:38 | PyPI JSON |
| OpenFeature spec | 0.9.0 | blog August 12, 2026 | `.release-please-manifest.json`; OpenFeature blog |

## Licences

| Source | Licence as stated | What an Apache-2.0 repository may do |
|---|---|---|
| GitHub Docs | `github/docs` LICENSE: CC BY 4.0 (docs); LICENSE-CODE: MIT | Quote, paraphrase, adapt text with attribution; code under MIT |
| Microsoft Learn (MVVM, .NET, WER) | `dotnet/docs` and `MicrosoftDocs/win32` LICENSE: CC BY 4.0 (lifecycle page not checked) | Quote, paraphrase, adapt with attribution |
| VS Code docs | `vscode-docs` LICENSE.md: "Documentation is licensed under the Creative Commons Attribution 3.0 United States License", code MIT (report said CC BY 4.0) | Quote, paraphrase, adapt with attribution (CC BY 3.0 US) |
| VS Code source | MIT (repository) | Quote briefly; code adaptable with notice |
| Sentry docs | `sentry-docs` LICENSE.md: FSL-1.1-Apache-2.0 (Functional Source License, Apache 2.0 future licence) | Quote briefly, paraphrase; don't adapt until each version converts to Apache-2.0 |
| OpenTelemetry docs | "Docs CC BY 4.0" (site footer; repository LICENSE CC BY 4.0) | Quote, paraphrase, adapt with attribution |
| OpenFeature docs | footer: "Documentation Distributed under CC BY 4.0" | Quote, paraphrase, adapt with attribution |
| React docs | `react.dev` LICENSE-DOCS.md: CC BY 4.0 | Quote, paraphrase, adapt with attribution |
| Elm guide | `guide.elm-lang.org` LICENSE: CC BY-NC-ND 4.0 | Quote briefly, paraphrase; no adaptation |
| Qt documentation | "licensed under the terms of the GNU Free Documentation License version 1.3" (page footer) | Quote briefly, paraphrase; don't adapt text |
| Playwright | Apache-2.0 (npm `license`, repository LICENSE) | Quote, paraphrase, adapt code with NOTICE/attribution |
| Chromatic CLI | MIT (npm `license`, LICENSE); blog not stated | CLI code adaptable with notice; blog quote briefly |
| CommunityToolkit.Mvvm | MIT (NuGet `licenseExpression`) | Adapt code with notice |
| KUserFeedback | `LICENSES/MIT.txt` present (REUSE layout; other licences may apply per file) | Quote README briefly; check per-file SPDX before adapting |
| KDE Community wiki | not checked | Quote briefly, paraphrase |
| Mozilla (privacy notice) | "Content available under a Creative Commons license" (footer; licence version not named on the page) | Quote briefly, paraphrase |
| Firefox source | MPL-2.0 (repository; not re-read) | Quote briefly |
| NN/g | "Copyright © 1998-2026 Nielsen Norman Group, All Rights Reserved." | Short quotes and paraphrase only |
| EDPB guidelines | legal-notice page returned 404; reuse terms not confirmed | Quote briefly with citation, paraphrase |
| EUR-Lex | not checked this run | Quote briefly with citation |
| Apple developer docs, WWDC | not stated on the pages read | Short quotes and paraphrase only |
| CNCF blog | not checked | Quote briefly, paraphrase |

## Repository facts this contradicts

Searched `skills/` with `git grep -n` for Playwright, Qt 6, pytest-qt, Sentry, OpenFeature,
OpenTelemetry, Chromatic, CommunityToolkit, NN/g severity, issue forms, ePrivacy, telemetry, Node 20
and .NET 8 to 11.

| File | Row ID | Now wrong | Correct value and source |
|---|---|---|---|
| `skills/user-experience/references/gui-testing.md` | `uxt-playwright` | "Playwright 1.65.0; the Python package came out 2026-11-09" | Python `playwright` 1.65.2, 2026-11-14T00:28:39 ([PyPI](https://pypi.org/pypi/playwright/json)); Node `@playwright/test` 1.65.1, 2026-11-13 ([npm](https://registry.npmjs.org/@playwright/test)) |

Checked and still correct: `cs-dotnet8-9-end`, `cs-dotnet10-lts`, `cs-dotnet11-sts`
(`skills/coding/references/csharp-coding.md`) match the lifecycle page; `uxr-severity-scale`,
`uxr-severity-raters`, `uxr-severity-after` (`skills/user-experience/references/usability-review.md`)
match the NN/g article; `uxt-pytest-qt` (4.5.0) is still current; `lo-otel-logs` (JavaScript logs
Development) matches the OpenTelemetry JavaScript page; `js-node20-eol` and `node20` are consistent.
`skills/` holds no facts rows on Sentry, OpenFeature, Chromatic, CommunityToolkit.Mvvm, Qt support
dates, ePrivacy or GitHub issue forms (none in `skills/git-workflows`), so nothing else is contradicted.

---

# R30: From user issues to fixes — feedback, crash and usage data, triage, and interfaces built to change

Four of the five "What we believe" items hold, but three need correcting: telemetry in well-known open-source desktop programs is not mostly opt-in (VS Code and Firefox collect by default and let users opt out; KDE and GNOME are opt-in); symbol files are essential for native crash reports but only sometimes needed for managed runtimes such as .NET; and no primary source was found showing that an in-app report form beats an email address, so that claim stays unproven.

**TL;DR**

- Collect with consent and attach context automatically: GitHub issue forms (YAML in `.github/ISSUE_TEMPLATE`, with required `name`, `description`, `body`) and in-app widgets such as Sentry's feedback integration (screenshot on by default in the JavaScript SDK 8.0.0+) give structure; EU usage analytics fall under ePrivacy Article 5(3), whose scope the EDPB widened in its final Guidelines 2/2023 (16 October 2024).
- Crash reporting is only useful if symbols for each shipped build are uploaded before release: Sentry says debug files "should be uploaded before deploying or releasing" and does not reprocess existing events; Apple says you "must retain the original archive"; Windows Error Reporting's LocalDumps are off by default.
- Triage with NN/g's 0–4 severity scale (frequency, impact, persistence), keep view separate from state (Microsoft: MVVM "makes an application easier to test, maintain, and evolve"), guard with platform-pinned screenshot tests (Playwright 1.65.1, released 13 November 2026 per the GitHub releases page), and note that .NET 8 and .NET 9 left support on 10 November 2026 while OpenFeature remains CNCF incubating, not graduated.

## 1. Summary

1. **Issue forms are the cheapest structured intake.** GitHub issue forms are YAML files that "must begin with name, description, and body key-value pairs"; body elements are `checkboxes`, `dropdown`, `input`, `markdown`, `textarea` and `upload`.\[1\]\[2\]
2. **Labels in a form must already exist.** GitHub: "If a label does not already exist in the repository, it will not be automatically added to the issue."\[3\] Create the triage labels first.
3. **In-app widgets can attach a screenshot with the user's agreement.** Sentry's JavaScript feedback widget has `enableScreenshot` defaulting to `true` (SDK 8.0.0+), lets the user crop the screenshot, and hides the button on mobile. Its React Native widget defaults to `false`.\[4\]\[5\]\[6\]
4. **No primary source compares in-app forms with email.** The belief is plausible but unproven; treat it as a hypothesis to measure.
5. **Native crash reports need per-build symbols, uploaded before release.** Sentry: "Debug files should be uploaded before deploying or releasing your application so that crash reports can be processed." Late uploads may take up to an hour to apply, and "Existing events and issues are not processed again."\[7\]
6. **Apple:** to symbolicate, keep each distributed build's archive (dSYM). Apple's own forum guidance: "you must retain the original archive used to upload the app."\[8\]\[9\]
7. **Windows Error Reporting local dumps are opt-in for admins.** The LocalDumps registry key "is not enabled by default" and needs administrator rights; apps with their own crash reporting are not supported by it.\[10\]\[11\]
8. **EU consent:** Article 5(3) of the ePrivacy Directive covers any "information" stored on or read from a user's device, not just personal data.\[12\] The EDPB's final Guidelines 2/2023 (version 2.0, 16 October 2024) extend it to pixel tracking, local processing, IP-only tracking, IoT reporting and unique identifiers.\[13\]\[14\]
9. **Open-source telemetry defaults differ.** VS Code collects usage, error and crash data by default (`telemetry.telemetryLevel` = `all`, `error`, `crash`, `off`).\[15\]\[16\] Firefox sends "technical and interaction data" until you untick it.\[17\] KDE's policy is "always opt-in, that is off by default".\[18\] GNOME's `gnome-info-collect` was a one-off, opt-in tool.\[19\]\[20\]
10. **OpenTelemetry in the browser is still experimental.** OpenTelemetry's JavaScript docs: "Client instrumentation for the browser is experimental and mostly unspecified."\[21\] Client-side semantic conventions published their first release, v0.1.0-dev, on 27 October 2026 (secondary).\[22\]
11. **Severity is not priority.** NN/g rates usability problems 0–4 by frequency, impact and persistence, plus market impact.\[23\] Severity ratings should be the mean of several evaluators ("three evaluators is satisfactory for many practical purposes").\[23\]
12. **Separate view from logic.** Microsoft Learn (MVVM), Elm (Model/View/Update), Qt (model/view) and Apple (SwiftUI data models) all say this, citing testability and ease of change.\[24\]\[25\]\[26\]\[27\] No primary source quantifies the cost.
13. **OpenFeature is CNCF incubating (since late 2023), not graduated.** One vendor blog claiming "graduated" is wrong.\[28\]
14. **Visual regression tests need per-platform baselines.** Playwright: "Screenshots differ between browsers and platforms due to different rendering, fonts and more, so you will need different snapshots for them."\[29\] Current version: 1.65.1 (13 November 2026), per the GitHub releases page.
15. **Support deadlines:** .NET 8 and .NET 9 reached end of support on 10 November 2026, when .NET 11 shipped.\[30\]\[31\] Qt 6.10 support ended 7 October 2026; Qt 6.11 ends 17 March 2027.\[32\]

## 2. Corrections

| # | What we believed | Verdict | Correct fact | Source |
|---|---|---|---|---|
| C1 | An in-app "report a problem" that attaches version, screen and recent logs gets more actionable reports than an email address. | **Unverified (not found)** | No primary source or published study comparing the two was found. What *is* sourced: tools that automate the attachment exist (Sentry's widget adds screenshots and, optionally, a session replay via `includeReplay`; GitHub forms enforce required fields). Keep the advice, but present it as reasoned practice, not an evidence-backed finding. | https://docs.sentry.io/platforms/javascript/user-feedback/configuration/ ; https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms |
| C2 | Crash reporting (Sentry, Crashpad, WER, Apple) needs symbol files kept per release to be readable. | **Partly correct — refine** | True for native code and Apple platforms, and symbols must be uploaded *before* release, because Sentry does not reprocess events that already arrived. For .NET, Sentry says debug files "may" be needed for "a complete stack trace including file names and line numbers", "especially" on mobile; so managed stacks are partly readable without them.\[33\] Python: no primary source found. | https://docs.sentry.io/platforms/dotnet/guides/entityframework/data-management/debug-files/upload/ ; https://docs.sentry.io/platforms/android/data-management/debug-files/upload/ |
| C3 | Usage analytics in the EU need consent unless strictly necessary (ePrivacy Art. 5(3)). | **Correct, with a wider scope than usually assumed** | The EDPB's final Guidelines 2/2023 say Art. 5(3) applies to "information" (wider than personal data) and to techniques beyond cookies.\[12\]\[13\] Desktop and native-app telemetry that reads or stores data on the device is in scope. | https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-22023-technical-scope-art-53-eprivacy-directive_en |
| C4 | Many open-source desktop programs make telemetry opt-in. | **Wrong as a generalisation** | VS Code and Firefox collect by default with opt-out; KDE (policy) and GNOME (`gnome-info-collect`) are opt-in.\[15\]\[17\]\[18\] Say "practice varies", and name each project. | https://code.visualstudio.com/docs/configure/telemetry ; https://support.mozilla.org/en-US/kb/technical-and-interaction-data ; https://mail.kde.org/pipermail/kde-community/2017q3/003820.html |
| C5 | Visual regression tests catch unintended layout changes, at the cost of flaky diffs from fonts and rendering. | **Correct** | Playwright's own docs give fonts and rendering as the reason baselines are per browser and platform, and expose `maxDiffPixels` and `threshold` as tolerances.\[29\] | https://playwright.dev/docs/test-snapshots |
| C6 | Keeping view code apart from state and logic makes interface changes cheaper and testable. | **Correct on testability; "cheaper" not quantified** | Microsoft: MVVM "makes an application easier to test, maintain, and evolve".\[25\] Apple: separation "promotes modularity, improves testability".\[34\] No primary source measures the cost saving. | https://learn.microsoft.com/dotnet/architecture/maui/mvvm |

## 3. Facts table

Dates: the source's own date where shown; otherwise "read 2026-11-15".

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| F1 | Issue form required keys | `name`, `description`, `body` | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms | "All issue form configuration files must begin with name, description, and body key-value pairs." | read 2026-11-15 |
| F2 | Issue form element types | checkboxes, dropdown, input, markdown, textarea, upload | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema | "checkboxes dropdown input markdown textarea upload" | read 2026-11-15 |
| F3 | Issue form labels | Must pre-exist | (F1 URL) | "If a label does not already exist in the repository, it will not be automatically added to the issue." | read 2026-11-15 |
| F4 | Issue form `type` key | Sets an organisation-level issue type | (F1 URL) | "The issue type that will be automatically added to issues created with this template. Issue types are defined at the organization level" | read 2026-11-15 |
| F5 | Field `id` used for URL prefill | Yes | (F2 URL) | "If provided, the id is the canonical identifier for the field in URL query parameter prefills." | read 2026-11-15 |
| F6 | Sentry JS feedback screenshot | Default on, SDK ≥ 8.0.0 | https://docs.sentry.io/platforms/javascript/guides/react-router/user-feedback/ | "On SDK version 8.0.0 and above, users can send screenshots with their feedback… by default it is set to true. Screenshots aren't supported on mobile devices" | read 2026-11-15\[4\] |
| F7 | Sentry screenshot quota | 1 GB ≈ 2,500 screenshots | (F6 URL) | "All plans come with 1GB of attachments, which is approximately 2500 screenshots." | read 2026-11-15\[4\]\[5\] |
| F8 | Sentry React Native screenshot | Default off | https://docs.sentry.io/platforms/react-native/user-feedback/configuration/ | "enableScreenshot | boolean | false" | read 2026-11-15\[6\] |
| F9 | Sentry: upload symbols before release | Required for processing | https://docs.sentry.io/platforms/native/data-management/debug-files/upload/ | "Debug files should be uploaded before deploying or releasing your application so that crash reports can be processed." | read 2026-11-15 |
| F10 | Sentry: no reprocessing | Late uploads don't fix old events | https://docs.sentry.io/platforms/android/data-management/debug-files/upload/ | "Existing events and issues are not processed again." | read 2026-11-15 |
| F11 | Sentry: symbols per project | Re-upload per project | (F10 URL) | "Sentry does not access debug files stored in other projects to symbolicate crash reports." | read 2026-11-15 |
| F12 | Sentry .NET symbols | Sometimes needed | https://docs.sentry.io/platforms/dotnet/guides/entityframework/data-management/debug-files/upload/ | "may require uploading debug files in order to show a complete stack trace including file names and line numbers. This is especially true for mobile apps" | read 2026-11-15 |
| F13 | Sentry .NET upload in build | NuGet ≥ 3.26.1, `SentryUploadSymbols` | https://docs.sentry.io/platforms/dotnet/guides/winforms/data-management/debug-files/upload.md | "the Sentry NuGet package (as of version 3.26.1) includes the Sentry CLI as a bundled tool, and will invoke it when building your project if the msbuild property SentryUploadSymbols is set to true (default to false)" | read 2026-11-15 |
| F14 | Apple dSYM retention | Keep the archive | https://developer.apple.com/forums/thread/18646 | "In order to download these dSYMs, you must retain the original archive used to upload the app." | Apple forum thread (bitcode era, c. 2015); read 2026-11-15\[9\] |
| F15 | WER LocalDumps | Off by default; admin needed | https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps | "This feature is not enabled by default. Enabling the feature requires administrator privileges." | read 2026-11-15\[10\] |
| F16 | WER and custom reporters | Not supported together | (F15 URL) | "Applications that do their own custom crash reporting are not supported by this feature." | read 2026-11-15\[10\] |
| F17 | ePrivacy guidelines final | EDPB Guidelines 2/2023 v2.0 | https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-22023-technical-scope-art-53-eprivacy-directive_en | "16 October 2024 Final version" | 2024-10-16 |
| F18 | Art. 5(3) applies beyond cookies | "Similar technologies" | https://www.headlesslaw.com/eprivacy/level-3/guidelines/edpb-02-2023-eprivacy-article-5-3-technical-scope (secondary reproduction of the EDPB text) | "Article 5(3) ePD does not exclusively apply to cookies, but also to ' similar technologies '" | 2024-10 (text); read 2026-11-15 |
| F19 | VS Code telemetry levels | all / error / crash / off | https://code.visualstudio.com/docs/configure/telemetry | "If you disable usage data telemetry by setting telemetry.telemetryLevel to error, crash, or off, we can't evaluate the feature's usage and therefore experimentation is disabled for you." | 2026-11-04 (ms.date) |
| F20 | VS Code extensions | Not covered by the setting | (F19 URL) | "These extensions may be collecting their own usage data and are not controlled by the telemetry.telemetryLevel setting." | 2026-11-04 |
| F21 | VS Code enterprise policy | `TelemetryLevel`, `EnableFeedback` since 1.99 | https://code.visualstudio.com/docs/enterprise/telemetry | "TelemetryLevel | Specify the telemetry data level | telemetry.telemetryLevel | 1.99" | read 2026-11-15 |
| F22 | Firefox opt-out and deletion | Delete within 30 days | https://support.mozilla.org/en-US/kb/technical-and-interaction-data | "If you opt out of sending technical and interaction data, Mozilla will also treat this as a request to delete any data that was previously collected. Data will be deleted within 30 days after you opt out." | read 2026-11-15 |
| F23 | Firefox DAU ping | Separate control | (F22 URL) | "Turning this off does not disable or prevent the DAU (daily active users) ping." | read 2026-11-15 |
| F24 | KDE telemetry policy | Opt-in | https://mail.kde.org/pipermail/kde-community/2017q3/003820.html | "application telemetry is always opt-in, that is off by default" | 2017-08-13 (policy draft on mailing list) |
| F25 | KUserFeedback | No unique IDs | https://github.com/kde/kuserfeedback | "KUserFeedback is designed to be compliant with KDE Telemetry Policy, which forbids the usage of unique identification." | read 2026-11-15 |
| F26 | Plasma telemetry | Opt-in since 5.18 | https://blog.davidedmundson.co.uk/blog/what-we-can-learn-from-plasma-telemetry/ (KDE developer's blog; secondary) | "Since Plasma 5.18… Plasma has shipped with a telemetry system. Opt in (i.e off by default)" | 2020-09 |
| F27 | OTel browser status | Experimental | https://opentelemetry.io/docs/languages/js/ | "Client instrumentation for the browser is experimental and mostly unspecified." | read 2026-11-15 |
| F28 | OTel RUM roadmap | Client SIG since late 2021 | https://opentelemetry.io/community/roadmap/ | "In late 2021, the Client Instrumentation SIG (often called the RUM SIG) was established" | read 2026-11-15 |
| F29 | OTel client-side semconv | v0.1.0-dev, 27 Oct 2026 | https://github.com/ouo11y/ouo11y.github.io/pull/20 (secondary) | "Client-side semantic conventions published their first release, v0.1.0-dev (27 Oct)" | 2026-10-30 |
| F30 | OTel web client-apps docs | Placeholder | https://github.com/open-telemetry/opentelemetry.io/issues/12103 | "The Web client-apps page still says “Content coming soon!”" | 2026-10-15 |
| F31 | NN/g severity factors | Frequency, impact, persistence | https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ | "The severity of a usability problem is a combination of three factors" | 1994-11-01 |
| F32 | NN/g scale top | 4 = catastrophe | (F31 URL) | "4 = Usability catastrophe: imperative to fix this before product can be released" | 1994-11-01 |
| F33 | NN/g evaluator count | Mean of 3 | (F31 URL) | "using the mean of a set of ratings from three evaluators is satisfactory for many practical purposes" | 1994-11-01 |
| F34 | OpenFeature CNCF level | Incubating | https://www.cncf.io/blog/2023/12/19/openfeature-becomes-a-cncf-incubating-project/ | "The CNCF Technical Oversight Committee (TOC) has voted to accept OpenFeature as a CNCF incubating project." | 2023-12-19 |
| F35 | Playwright current | 1.65.1 | https://github.com/microsoft/playwright/releases | "v1.65.1 Latest… released this 13 Nov" | 2026-11-13 |
| F36 | Playwright Node 20 | Dropped from testing | https://github.com/microsoft/playwright/releases/tag/v1.65.0 | "Playwright no longer tests on Node.js 20." | 2026-11-05 |
| F37 | Playwright baselines per platform | Yes | https://playwright.dev/docs/test-snapshots | "Screenshots differ between browsers and platforms due to different rendering, fonts and more, so you will need different snapshots for them." | read 2026-11-15 |
| F38 | Chromatic bypassed builds | Need CLI ≥ 17.7.0 + TurboSnap | https://www.chromatic.com/blog/chromatic-changelog-august-2026/ | "Bypassed builds require TurboSnap enabled, and Chromatic CLI 17.7.0 or later." | 2026-08\[35\] |
| F39 | Chromatic CLI latest seen | 18.5.0 | https://github.com/chromaui/chromatic-cli/blob/main/CHANGELOG.md | "v18.5.0 (Wed Aug 19 2026)" | 2026-08-19\[36\] |
| F40 | .NET 11 GA / .NET 8 end | 10 Nov 2026 | https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-and-net-core | ".NET 11 | 11/10/2026 8:00:00 AM" ; ".NET 8 (LTS) | 11/14/2023 8:00:00 AM | 11/10/2026 8:00:00 AM" | read 2026-11-15\[37\] |
| F41 | MVVM benefit | Test, maintain, evolve | https://learn.microsoft.com/dotnet/architecture/maui/mvvm | "Maintaining a clean separation between application logic and the UI helps address numerous development issues and makes an application easier to test, maintain, and evolve." | read 2026-11-15 |
| F42 | CommunityToolkit.Mvvm | 8.4.2 | https://www.nuget.org/packages/CommunityToolkit.Mvvm | Last updated "3/25/2026" | 2026-03-25 |
| F43 | Elm Architecture | Model/View/Update | https://guide.elm-lang.org/architecture/ | "Model — the state of your application / View — a way to turn your state into HTML / Update — a way to update your state based on messages." | read 2026-11-15 |
| F44 | Qt model/view | Separates storage from presentation | https://doc.qt.io/qt-6/model-view-programming.html | "This still separates the way that data is stored from the way that it is presented to the user" | Qt 6.12 docs; read 2026-11-15 |
| F45 | Qt support table | 6.12 → 2031-09-30; 6.11 → 2027-03-17; 6.10 → 2026-10-07; 6.8 LTS → 2029-10-08 | https://doc.qt.io/qt-6/qt-releases.html | "each minor version of Qt is supported for one year… Starting with version 6.8.0, the LTS versions are supported for five years." | read 2026-11-15 |
| F46 | SwiftUI data model | Separate from UI | https://developer.apple.com/videos/play/wwdc2020/10040/ | "Typically, in your app, you store and process data by using a data model that is separate from its UI." | WWDC 2020 |
| F47 | React state | Avoid redundant state | https://react.dev/learn/choosing-the-state-structure | "If you can calculate some information from the component's props or its existing state variables during rendering, you should not put that information into that component's state." | React docs v19.3; read 2026-11-15 |

## 4. Findings

### 4.1 Collecting feedback in the product (Priority 1)

**What to attach automatically.** No standards body publishes a list. What the main tool documents:

- Sentry's browser feedback widget (SDK ≥ 7.85.0; screenshots from 8.0.0) links feedback to the current session. It can attach a screenshot the user takes and crops (`enableScreenshot`, default `true` on the web), can include a session replay (`includeReplay: true`), and takes arbitrary attachments through `Sentry.captureFeedback(..., { attachments })`.\[4\]\[38\]\[39\]
- A crash-report modal ties feedback to a specific error event, using `Sentry.lastEventId()`.\[38\]
- The screenshot is the user's choice: they press "Add a screenshot" and can remove it again.\[5\]\[40\] This is the consent pattern the repository should recommend.
- On mobile the JavaScript screenshot button is hidden automatically, and React Native defaults to `false`.\[4\]\[6\]

Our recommendation (reasoned, not sourced): attach the app version, build ID, OS and version, current screen or route, locale, and the last N log lines with personal data removed. Show the user the full payload before sending, as GNOME's `gnome-info-collect` "will present all collected data to the user before it's transmitted" (Linux Magazine, secondary).\[41\]

**GitHub issue forms: current syntax** (docs read 2026-11-15):

- Files are YAML under `.github/ISSUE_TEMPLATE/`.
- Required top-level keys: `name`, `description`, `body`.
- Optional top-level keys: `title`, `labels`, `assignees`, `projects` (the person opening the issue needs write permission on those projects), and `type` (an organisation-level issue type).
- Body element `type` values: `markdown`, `input`, `textarea`, `dropdown`, `checkboxes`, `upload`.\[2\]
- `id` may use only letters, digits, `-` and `_`, must be unique, and doubles as the URL prefill key.\[2\] So an app can open `…/issues/new?template=bug.yml&version=1.4.2` with fields already filled in. This is the cheapest way to "attach the version" from a desktop app that has no backend.
- Labels that don't exist are silently dropped.
- Contested: a Microsoft-hosted Enterprise Cloud copy of the page still says "Issue forms are currently in public preview and subject to change"; the main docs page carries no such note.\[42\] Treat the main docs as current, but expect schema additions (`upload` and `type` are recent).

**People who won't file an issue (including internal tools on a local network).** No primary source specifically addresses intranet tools.

- Sentry's "Bring Your Own Widget" API (`captureFeedback`) works against a self-hosted Sentry. Self-hosted screenshots need release 24.4.2 or later.\[4\]\[39\]
- VS Code's `EnableFeedback` enterprise policy (since 1.99) shows the flip side: organisations may switch in-product feedback off. Build an off switch.
- Any further mechanism (for example a "send report" button that POSTs to an internal endpoint that opens an issue through the GitHub API) is our suggestion, not a sourced practice.

### 4.2 Crash reports and usage data (Priority 2)

**Per platform and runtime:**

| Platform/runtime | Mechanism | Symbols | Status found |
|---|---|---|---|
| Native (C/C++), any OS | Sentry Native SDK (uses Crashpad/Breakpad backends — backend detail not re-verified here) | Upload debug files before release; per project | Sentry docs (F9–F11) |
| Windows | WER LocalDumps (`HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps[\App.exe]`) | PDBs needed to analyse dumps | Off by default; admin; not with custom reporters (F15–F16)\[10\]\[43\] |
| Apple | Xcode Organizer / App Store Connect crash reports | dSYM per build; keep the archive | F14\[9\]\[44\] |
| .NET | Sentry .NET; `SentryUploadSymbols` MSBuild property | Optional on desktop, often needed on mobile | F12–F13; .NET 8/9 out of support since 2026-11-10 (F40)\[37\] |
| Qt | Not found (no Qt-specific crash reporter documented in sources read) | — | Not found |
| Python | Not found in this run | — | Not found |
| Browser | Sentry JS; OpenTelemetry browser SDK (experimental) | Source maps (not researched) | F27–F30 |

Crashpad and Breakpad versions and release dates: not found (neither project publishes versioned releases that we could cite).

**Consent law.**

- Article 5(3) of the ePrivacy Directive (as amended by Directive 2009/136/EC) requires consent before storing or reading information on a user's device. The exceptions are transmitting a communication, and what is "strictly necessary" for a service the user explicitly asked for. This wording comes from the Directive's text; we did not re-fetch it in this run, so check it against EUR-Lex.
- The EDPB's final Guidelines 2/2023 (v2.0, 16 October 2024) set three tests: "information", "terminal equipment", and "storage" or "gaining access". They list URL and pixel tracking, local processing, IP-only tracking, IoT reporting and unique identifiers as in scope.\[14\]
- Consequence: a desktop app that reads a device identifier or writes an install ID for analytics needs consent in the EU. Crash reports the user explicitly sends are a different case, but no primary source in this run rules on whether automatic crash upload is "strictly necessary". Mark that **not found**.
- GDPR applies on top wherever the data is personal (not researched in depth here).

**What well-known open-source programs do:**

- **VS Code:** `telemetry.telemetryLevel` = `all` (default) / `error` / `crash` / `off`. Anything below `all` disables A/B experiments. Extensions are not governed by the setting. Enterprises can enforce `TelemetryLevel` by policy (1.99+).\[15\]\[45\]
- **Firefox:** opt-out checkbox "Send technical and interaction data to Mozilla". Opting out triggers deletion within 30 days. The daily-active-users (DAU) ping has its own control.\[17\]
- **KDE:** policy says opt-in and off by default. Plasma shipped opt-in telemetry from 5.18, through KUserFeedback, which forbids unique IDs.\[18\]\[46\]\[47\]
- **GNOME:** `gnome-info-collect` (2022) was a one-off, user-run, opt-in tool. Allan Day's GNOME blog ("Help improve GNOME!", 25 August 2022) says "The tool shows the data that will be collected prior to uploading and, if the user consents to the upload, is then securely sent to GNOME's servers", and an update of 20 September 2022 says "the collection period for gnome-info-collect is now over, and the collection server has been turned off."
- Lesson: the projects that defer most to user trust (KDE, GNOME) chose opt-in and no stable IDs. Copy that model for EU-facing and internal tools.

**OpenTelemetry for client apps.** Traces and metrics are stable for JavaScript in general, but browser client instrumentation is "experimental and mostly unspecified".\[21\] A dedicated `opentelemetry-browser` repository and Browser SIG exist.\[48\] Secondary reporting (a contributor's blog in GitHub PRs) gives:

- browser-sdk 0.6.0 and browser-instrumentation 0.9.0 are current;
- 0.7.0 and 0.10.0 are queued with two breaking changes, including "no default HTTP exporter";\[22\]
- client-side semantic conventions reached v0.1.0-dev on 27 October 2026.\[22\]

Recommendation: don't build a feedback loop on OTel browser or desktop telemetry in 2026 unless you can absorb breaking changes. Use it only for traces on the server side.

### 4.3 Triage (Priority 3)

- **Severity (NN/g, 1994, still the standard reference):**
  - 0 means not a problem; 1 cosmetic; 2 minor ("low priority"); 3 major ("high priority"); 4 catastrophe ("imperative to fix this before product can be released").\[23\]
  - Severity combines frequency, impact and persistence, and "market impact" should also be assessed.\[23\]
  - Ratings are better collected after the evaluation, as the mean of about three evaluators, not from one person in the moment.\[23\]
- **Severity vs priority:** NN/g maps severity to priority directly, but its own text adds market impact. Keep two labels: `severity:0–4` (user harm, from the NN/g scale) and `priority:P0–P3` (team decision, which includes market impact and cost).
- **Labels:** create them before issue forms reference them (F3). Use the form's `labels: ["bug", "triage"]` so every new report lands in a triage queue.
- **Reproducing, duplicates and closing the loop:** published bug-triage guides from large open-source projects (Mozilla, Kubernetes, GNOME) were **not covered** in this run (search budget). The only sourced item is the issue-form checkbox pattern "Is there an existing issue for this?" from GitHub's own example.

### 4.4 Building an interface to change (Priority 4)

| Toolkit | Pattern | Primary-source statement | Current version / support |
|---|---|---|---|
| WPF / WinUI / .NET MAUI | MVVM; CommunityToolkit.Mvvm | "makes an application easier to test, maintain, and evolve" (F41); toolkit "compatible with… WinUI, WPF, and .NET MAUI" | CommunityToolkit.Mvvm 8.4.2 (2026-03-25); .NET 11 GA 2026-11-10 (STS); .NET 10 LTS\[37\]\[49\] |
| Qt | Model/view | "separates the way that data is stored from the way that it is presented" (F44) | Qt 6.12.0 current (released 30 September 2026 per the Qt Wiki "Qt 6.12 Release" page and the Qt blog post "Qt 6.12 LTS Released!"; support to 2031-09-30) |
| GTK | Not found (no primary MVVM/MVU guidance located) | — | Not found |
| React | State structure; derive, don't duplicate | "you should not put that information into that component's state" (F47) | Docs show v19.3 |
| SwiftUI | Separate data model; `@Observable` (iOS 17 / macOS 14+) | "data model that is separate from its UI" (F46) | Not researched |
| Elm (MVU) | Model/View/Update | F43 | Not researched |

- **Strings and settings in one place:** not covered by any primary source in this run.
- **Feature flags for interface changes:** OpenFeature is the vendor-neutral API. It has been CNCF incubating since its December 2023 announcement (the CNCF blog is dated 19 December 2023; a secondary source gives the project-page date as 21 November 2023). Its spec is at v0.9.0, which OpenFeature's own blog (Jonathan Norris, 12 August 2026) calls "our first spec release since v0.8.0 in March 2024" and says "stabilizes the evaluation and provider sections", noting "Three changes are breaking"; parts such as tracking are still experimental.
- **Contested:** a CloudBees blog states "OpenFeature is a graduated CNCF project".\[28\] The CNCF's own announcement and an October 2026 secondary check both say incubating.\[50\]\[51\] We side with CNCF.
- **What each costs:** no primary source quantifies the cost of MVVM, MVU or feature flags. **Not found.**

### 4.5 Visual regression testing (Standard 5)

- **Playwright `toHaveScreenshot()`:**
  - Baselines are named per project and per platform (for example `-chromium-darwin`).
  - Tolerances are set with `maxDiffPixels` and `threshold` in `expect.toHaveScreenshot`.
  - Snapshots can be stored as lossless WebP.
  - Version 1.65.0 shipped on 5 November 2026; 1.65.1, released 13 November 2026 per the GitHub releases page, is now current and makes TypeScript class fields "follow useDefineForClassFields from your tsconfig.json".
  - Third-party guides (secondary) agree: generate and compare baselines inside the same Docker image CI uses (`mcr.microsoft.com/playwright`), and wait for `document.fonts.ready`.\[52\]\[53\]
- **Chromatic:**
  - TurboSnap captures only stories whose dependency graph changed.\[54\]\[55\]
  - Since August 2026, builds with no UI change are "bypassed" and cost zero snapshots (needs CLI ≥ 17.7.0).\[35\]
  - Latest CLI seen: 18.5.0 (19 August 2026); later versions may exist.\[36\]
  - Pricing (secondary, October 2026): free tier 5,000 snapshots a month; Starter $179 a month.\[55\]
- **Percy:** not covered (no source fetched).
- **Qt:**
  - Qt Quick Test's `TestCase.grabImage(item)` returns an image you can compare and save on failure.\[56\]\[57\]
  - No official reftest framework for Qt Widgets was found.
- **GTK:**
  - GTK's own test suite has reftests (`testsuite/reftests`). They produce `.out.png`, `.ref.png` and `.diff.png` files, per GTK developer Benjamin Otte's 2011 blog post (old; paths have moved).\[58\]
  - No public, documented reftest API for applications was found.

### 4.6 Measuring whether a fix helped (Standard 6)

**Not covered** with primary sources in this run. The only sourced point: VS Code shows that A/B experimentation depends on full usage telemetry (any level below `all` disables it). So small or opt-in user bases cannot support A/B testing by design. For small internal tools, our reasoned suggestion (unsourced) is to compare before and after on task success and support-ticket counts tied to issue labels, not A/B tests.

### 4.7 Release notes (Standard 7)

**Not covered** with published guidance. An example of practice: Playwright's release notes put a "Breaking Changes ⚠" heading first and explain each change in one sentence (for example "Proxy credentials are no longer sent to websites").\[59\] That is a reasonable model to copy.

### 4.8 Common mistakes (Standard 8)

See section 7.

## 5. Tools

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| GitHub issue forms | Structured intake | n/a (hosted) | n/a | Add YAML to `.github/ISSUE_TEMPLATE/` | `.github/ISSUE_TEMPLATE/*.yml` | docs.github.com (F1) |
| Sentry JS feedback | In-app feedback + screenshot | Not captured (needs SDK ≥ 8.0.0 for screenshots) | Not found | `npm i @sentry/browser` | `Sentry.init({ integrations: [Sentry.feedbackIntegration()] })` | docs.sentry.io (F6) |
| sentry-cli | Upload debug files | Not captured (v3 referenced in Apple docs) | Not found | `sentry-cli debug-files upload -o ORG -p PROJECT path` | `.sentryclirc` | docs.sentry.io/cli/dif |
| WER LocalDumps | Local crash dumps on Windows | Built-in | n/a | `reg add "HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\App.exe" /v DumpType /t REG_DWORD /d 2` | Registry | learn.microsoft.com (F15)\[43\]\[60\] |
| KUserFeedback | Opt-in telemetry for Qt/KDE apps | Not found | Not found | Package `kuserfeedback` | In-app provider | github.com/kde/kuserfeedback |
| OpenTelemetry browser SDK | Client telemetry (experimental) | 0.6.0 (secondary) | Not found | npm (package name not verified) | Code | F29 |
| OpenFeature | Feature-flag API | Spec v0.9.0 (OpenFeature blog, 12 August 2026) | 2026-07-29 (secondary) | Language SDKs | Provider config | F34 |
| Playwright Test | Screenshot assertions | 1.65.1 | 2026-11-13 | `npm i -D @playwright/test` | `playwright.config.ts` | F35 |
| Chromatic CLI | Hosted visual tests | 18.5.0 (latest seen) | 2026-08-19 | `npx chromatic --only-changed` | `chromatic.config.json` | F39\[36\]\[61\] |
| CommunityToolkit.Mvvm | MVVM helpers for WPF/WinUI/MAUI | 8.4.2 | 2026-03-25 | `dotnet add package CommunityToolkit.Mvvm` | n/a | F42 |
| Qt | UI toolkit, model/view, Qt Quick Test | 6.12.0 | 2026-09-30 (Qt Wiki "Qt 6.12 Release"; Qt blog) | Qt online installer | CMake | F45 |
| .NET | Runtime | 11.0 (STS) / 10 (LTS) | 2026-11-10 / 2025-11-11 | `dotnet --version` | `global.json` | F40\[49\]\[62\] |

## 6. Changing in the next 12 months

- **Already passed (act now):** .NET 8 (LTS) and .NET 9 reached end of support on **10 November 2026**. Move to .NET 10 or .NET 11: Microsoft Learn's "Releases and support for .NET" (ms.date 2026-11-11) says ".NET 11 (Standard Term Support) - supported until November 2028. .NET 10 (Long Term Support) - supported until November 2028." The exact day, 14 November 2028, is from secondary sources.
- **Already passed:** Qt 6.10 standard support ended **7 October 2026**.\[32\]
- **⚠ Within 12 months:** Qt 6.11 standard support ends **17 March 2027**. Qt 6.5 LTS has already ended (extended maintenance only).\[32\]
- **Playwright:** monthly cadence; main has moved to 1.66 (GitHub issue #44004, 10 November 2026). No date announced: **not found**. Breaking in 1.65: Node.js 20 is no longer tested; cookie matching follows RFC 6265; proxy credentials are no longer sent to websites.\[59\]\[63\]
- **OpenTelemetry browser:** next releases browser-sdk 0.7.0 and browser-instrumentation 0.10.0 are queued with breaking changes (no default HTTP exporter).\[22\] Date: not found (secondary source).
- **OpenFeature:** no graduation date announced (not found).
- **ePrivacy:** no new EDPB revision found. The proposed ePrivacy Regulation's status was not researched in this run.

## 7. Common mistakes

1. **Uploading symbols after release.** Sentry won't reprocess earlier events (F10).\[64\] Upload in the release pipeline.
2. **Symbols in the wrong Sentry project.** They are not shared across projects (F11).\[64\]
3. **Deleting Xcode archives.** Without them you can't recover dSYMs (F14).\[9\]
4. **Assuming WER LocalDumps captures everything.** It's off by default and skips apps with their own reporter (F15–F16).\[10\]
5. **Treating "strictly necessary" as covering analytics,** and assuming ePrivacy only covers cookies or personal data (F17–F18).
6. **Assuming one switch disables all telemetry.** VS Code extensions and Firefox's DAU ping have separate controls (F20, F23). Document every channel your app has.
7. **Referencing labels that don't exist in issue forms** (F3).
8. **Single cross-platform screenshot baselines,** or loosening `threshold` instead of pinning the rendering environment (F37).
9. **Calling OpenFeature "graduated"** (F34; the CloudBees claim is contested).
10. **AI coding assistants:**
    - Typical mistakes are fixing one screen and not its siblings, adding no regression test, and inventing config keys.
    - **No primary or research source was found in this run documenting these specific failure modes.**
    - One adjacent secondary item: a 2026 guide warns that `github.copilot.advanced.telemetry.optOut` "is not a documented current Copilot control", which is an example of a plausible-looking but invented setting (wisechecker.com, secondary).\[16\]
    - Treat the rest as a hypothesis for the repository's own review checklist.

## 8. Sources and licences

Licence entries marked "(unverified)" come from general knowledge, not from a licence statement read in this run. Check them before adapting anything.

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| GitHub Docs (docs.github.com, github/docs) | CC BY 4.0 for docs, MIT for code (unverified) | Yes | Yes | Yes, if CC BY 4.0/MIT confirmed | "GitHub Docs, CC BY 4.0" + URL |
| Sentry docs | Not stated (unverified) | Briefly | Yes | No, until licence confirmed | Name + URL |
| Microsoft Learn (WER, MVVM, lifecycle) | CC BY 4.0 for many docs (unverified) | Yes | Yes | Only after confirming the page's repo licence | "Microsoft Learn" + URL |
| VS Code docs (microsoft/vscode-docs) | CC BY 4.0 / MIT (unverified) | Yes | Yes | After confirming | "VS Code docs" + URL |
| Mozilla Support | CC BY-SA (unverified) | Briefly | Yes | No (share-alike conflicts with Apache-2.0 for adapted text) | "Mozilla Support" + URL |
| EDPB guidelines | EU institutional reuse terms (unverified) | Yes | Yes | n/a | "EDPB Guidelines 2/2023 v2.0" + URL |
| NN/g article | All rights reserved | Briefly (short quotes) | Yes | n/a | "Jakob Nielsen, NN/g, 1994" + URL |
| KDE mailing list / KUserFeedback | List: none stated; KUserFeedback code: MIT (unverified) | Briefly | Yes | Code only after confirming | Author + URL |
| OpenTelemetry docs | CC BY 4.0 (unverified) | Yes | Yes | After confirming | "OpenTelemetry" + URL |
| CNCF blog | Not stated | Briefly | Yes | n/a | "CNCF" + URL |
| Playwright docs and releases | Apache-2.0 (repository licence; versio.io lists Apache 2.0) | Yes | Yes | Yes | Keep NOTICE/attribution: "Microsoft Playwright, Apache-2.0"\[65\] |
| Chromatic blog and CLI changelog | Blog: not stated; CLI: MIT (unverified) | Briefly | Yes | No for blog | "Chromatic" + URL |
| Qt documentation | GFDL 1.3 (unverified) | Briefly | Yes | No (GFDL not compatible for adaptation into Apache-2.0) | "Qt documentation" + URL |
| React docs | CC BY 4.0 (unverified) | Yes | Yes | After confirming | "React docs" + URL |
| Elm guide | Not stated | Briefly | Yes | No | "Elm Guide" + URL |
| Apple docs and WWDC | Proprietary | Briefly | Yes | No | "Apple Developer" + URL |
| Secondary blogs (ajayk.sh, ouo11y PRs, Linux Magazine, davidedmundson.co.uk, herodevs, diatom, testdino, etc.) | Not stated | Briefly | Yes | No | Author + URL, labelled "secondary" |
| Wikipedia (dates only) | CC BY-SA 4.0 | Briefly | Yes | No | "Wikipedia" + URL |

## 9. Not found, contested, not covered

**Not found**
- Any study showing in-app report forms produce more actionable reports than email (C1).
- Python crash reporting and symbol needs; Qt-specific crash reporting; Crashpad and Breakpad version numbers.
- Whether automatic crash upload is "strictly necessary" under Art. 5(3).
- Release dates for the Sentry SDK and sentry-cli versions.
- Percy's current version.
- The next Playwright release date.
- Quantified costs of MVVM, MVU or feature flags.
- GTK-specific view/state separation guidance.
- A public, documented GTK reftest API for applications.
- Sources on AI-assistant UI-fix failure modes.

**Contested**
- OpenFeature "graduated" (CloudBees) vs "incubating" (CNCF, 2023; secondary check October 2026). We side with CNCF.
- GitHub issue forms "public preview" (Enterprise Cloud page copy) vs no such note on the main docs.
- OpenTelemetry "graduated in May 2026" appears only in a vendor blog (OpenObserve); not verified against CNCF.\[66\]

**Not covered (budget)**
- GDPR detail beyond ePrivacy.
- Bug-triage guides from large open-source projects (reproduction, duplicates, closing the loop).
- Strings and settings centralisation.
- Measuring fixes (task success, time on task, error rates, A/B limits).
- Release-note guidance.
- Percy.
- Apple's current English SwiftUI `@Observable` page: the subagent could only read Apple's Chinese version. Its back-translated wording ("separation promotes modularity, improves testability") must be checked against the English page before quoting.

## Sources

1. [docs/content/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms.md at main · github/docs · GitHub](https://github.com/github/docs/blob/main/content/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms.md)
2. [Syntax for GitHub's form schema - GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema)
3. [Syntax for issue forms - GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
4. [Set Up User Feedback](https://docs.sentry.io/platforms/javascript/guides/react-router/user-feedback/)
5. [user feedback widget screenshots](https://sentry.io/changelog/user-feedback-widget-screenshots)
6. [docs.sentry.io](https://docs.sentry.io/platforms/react-native/user-feedback/configuration/)
7. [Uploading Files](https://docs.sentry.io/platforms/native/data-management/debug-files/upload/)
8. [Symbolicating Crash Reports](https://hevawu.github.io/blog/2019/05/13/Crash-Reports)
9. [Symbolicating Crashes for Applications Submitted with Bitcode](https://developer.apple.com/forums/thread/18646)
10. [Collecting User-Mode Dumps - Win32 apps](https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps)
11. [How to troubleshoot a Windows application crash - DualShield MFA Platform - Deepnet Security Technical Guides](https://wiki.deepnetsecurity.com/display/DualShield6/How+to+troubleshoot+a+Windows+application+crash)
12. [EDPB 2/2023 — Guideline — Technical Scope of Art. 5(3) of ePrivacy Directive \[final\]](https://www.headlesslaw.com/eprivacy/level-3/guidelines/edpb-02-2023-eprivacy-article-5-3-technical-scope)
13. [EDPB Guidelines EDPB 02/2023](https://privacylawhub.com/edpb-guidelines/guidelines-02-2023-technical-scope-article-5-3-eprivacy)
14. [EDPB guidelines on the technical scope of the ePrivacy directive - EU Digital Compliance Tracker (Snellman)](https://digitalcompliance.snellman.com/edpb-guidelines-on-the-technical-scope-of-the-eprivacy-directive-2/)
15. [Telemetry](https://code.visualstudio.com/docs/configure/telemetry)
16. [GitHub Copilot Telemetry in VS Code: Settings, Training and OTel](https://wisechecker.com/vs-code-github-copilot-telemetry-configuration-explained/)
17. [Manage technical and interaction data collection settings in Firefox](https://support.mozilla.org/en-US/kb/technical-and-interaction-data)
18. [Telemetry Policy](https://mail.kde.org/pipermail/kde-community/2017q3/003820.html)
19. [Ubuntu Telemetry: What Ubuntu Collects and How to Disable It - OSTechNix](https://ostechnix.com/ubuntu-telemetry/)
20. [Gnome system information: the good, the bad or the gnome? - Gnome - EndeavourOS](https://forum.endeavouros.com/t/gnome-system-information-the-good-the-bad-or-the-gnome/31355)
21. [JavaScript](https://opentelemetry.io/docs/languages/js/)
22. [Blog: Browser SIG, 29 October 2026 (OpenTelemetry in the browser, part 3) by ZiadMansourM · Pull Request #20 · ouo11y/ouo11y.github.io · GitHub](https://github.com/ouo11y/ouo11y.github.io/pull/20)
23. [Severity Ratings for Usability Problems: Article by Jakob Nielsen](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/)
24. [The Elm Architecture · An Introduction to Elm](https://guide.elm-lang.org/architecture/)
25. Microsoft Learn
26. [Model/View Programming | Qt Widgets | Qt 6.12.0](https://doc.qt.io/qt-6/model-view-programming.html)
27. [Data Essentials in SwiftUI - WWDC20 - Videos - Apple Developer](https://developer.apple.com/videos/play/wwdc2020/10040/)
28. [What Is OpenFeature? Feature Flag Portability Explained](https://www.cloudbees.com/blog/openfeature)
29. [Visual comparisons](https://playwright.dev/docs/test-snapshots)
30. [.NET 11 security changes target the software supply chain - Help Net Security](https://www.helpnetsecurity.com/2026/11/12/net-11-security-changes/)
31. [.NET Release and Support Timeline - STS and LTS Releases, the Move to Two-Year STS Support, and End-of-Support Dates](https://hidekazu-konishi.com/entry/dotnet_release_and_support_timeline.html)
32. [Qt Releases | Qt 6.12](https://doc.qt.io/qt-6/qt-releases.html)
33. [Uploading Files](https://docs.sentry.io/platforms/dotnet/guides/entityframework/data-management/debug-files/upload/)
34. [managing model data in your app](https://developer.apple.com/cn/documentation/swiftui/managing-model-data-in-your-app)
35. [Chromatic changelog: August 2026](https://www.chromatic.com/blog/chromatic-changelog-august-2026/)
36. [chromatic-cli/CHANGELOG.md at main · chromaui/chromatic-cli · GitHub](https://github.com/chromaui/chromatic-cli/blob/main/CHANGELOG.md)
37. [Microsoft .NET and .NET Core - Microsoft Lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-and-net-core)
38. [Set Up User Feedback](https://docs.sentry.io/platforms/javascript/user-feedback/)
39. [Configuration](https://docs.sentry.io/platforms/javascript/guides/react/user-feedback/configuration/)
40. [User Feedback Configuration for Browser JavaScript](https://docs.sentry.io/platforms/javascript/user-feedback/configuration/)
41. [Gnome Project Releases New Telemetry Data Colle... » Linux Magazine](https://www.linux-magazine.com/Online/News/Gnome-Project-Releases-New-Telemetry-Data-Collection-Tool)
42. [syntax for issue forms](https://docs.github.com/en/enterprise-cloud@latest/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
43. [Intro to Windows Crash Dump Collection - WER/ProcDump](https://comcomponent.com/en/blog/2026/03/16/008-windows-app-crash-dump-collection-introduction/)
44. [How do I symbolicate crash logs from App Store Connect?](https://ptkd.com/journal/how-to-symbolic-crash-logs-from-app-store-connect)
45. [Manage telemetry in enterprise environments](https://code.visualstudio.com/docs/enterprise/telemetry)
46. [What we can learn from Plasma telemetry](https://blog.davidedmundson.co.uk/blog/what-we-can-learn-from-plasma-telemetry/)
47. [github.com](https://github.com/kde/kuserfeedback)
48. [docs(js): link browser instrumentation warning to client SIG by aryansri05 · Pull Request #11074 · open-telemetry/opentelemetry.io · GitHub](https://github.com/open-telemetry/opentelemetry.io/pull/11074)
49. [.NET 11: What's New, Release Date and Upgrade Guide - Diatom Enterprises](https://diatomenterprises.com/blog/net-11-whats-new/)
50. [OpenFeature becomes a CNCF incubating project](https://www.cncf.io/blog/2023/12/19/openfeature-becomes-a-cncf-incubating-project/)
51. [Progressive Delivery in 2026: Feature Flags vs Canary vs Blue-Green · Ajay Kumar](https://www.ajayk.sh/blog/progressive-delivery-feature-flags-openfeature-2026/)
52. [Playwright Visual Regression Testing: Screenshots, Baselines, and Diffs](https://qaguardian.com/learn/playwright/playwright-visual-regression-testing)
53. [Playwright Visual Regression Testing: The Complete 2026 Guide](https://qaskills.sh/blog/playwright-visual-regression-testing-guide)
54. [Storybook Visual Testing with Chromatic: Component VRT](https://bug0.com/knowledge-base/storybook-visual-regression-testing-chromatic)
55. [Storybook Visual Testing Without Chromatic: Free & No-Code](https://delta-qa.com/en/blog/storybook-visual-testing-without-chromatic/)
56. [TestCase QML Type](https://doc.qt.io/qt-6/qml-qttest-testcase.html)
57. [TestCase QML Type](https://doc.qt.io/archives/qt-5.15/qml-qttest-testcase.html)
58. [reftests — Swfblag](https://blogs.gnome.org/otte/2011/05/05/reftests/)
59. [Release notes](https://playwright.dev/java/docs/release-notes)
60. [Analyze user mode dumps](https://www.sysnative.com/forums/threads/analyze-user-mode-dumps.45037/)
61. [Chromatic Visual Testing + Storybook TurboSnap Official 2026](https://qaskills.sh/blog/chromatic-visual-testing-storybook-turbosnap-2026)
62. [.NET](https://en.wikipedia.org/wiki/.NET)
63. [\[Bug\]: python-playwright 1.65 · Issue #44004 · microsoft/playwright · GitHub](https://github.com/microsoft/playwright/issues/44004)
64. [Uploading Files](https://docs.sentry.io/platforms/android/data-management/debug-files/upload/)
65. [Microsoft Playwright releases, versions & end-of-life (EOL)](https://www.versio.io/en/product-release-end-of-life-eol-microsoft-playwright.html)
66. [What Is OpenTelemetry (OTel)? Architecture & How It Works](https://openobserve.ai/blog/what-is-opentelemetry/)

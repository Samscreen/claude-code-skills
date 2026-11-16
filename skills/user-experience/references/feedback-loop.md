# Feedback loop

Read this for learning what's wrong with an interface once people use it, and fixing it safely:
reporting from inside the program, GitHub issue forms, crash reports and symbols, usage data and
consent, severity against priority, one fix for every screen with the fault, screenshot tests
that guard it, and whether it helped, internal tools included.

Heuristic reviews and the severity scale are `usability-review`'s; driving a toolkit from tests,
`gui-testing`'s. Redacting logs is the `coding` skill's `logging-and-observability`; personal
data, project-bootstrap-and-audit's dimension 7, *Secrets, security and data classification*.

## Rules

1. **Let people who won't file an issue report from inside the program,** with context attached
   and personal data removed, the whole report shown before it's sent.
2. **Where reports go to GitHub, use an issue form the program fills in** through URL parameters
   named by each field's `id`, and create every label it names first (fact `fl-gh-forms`).
3. **Upload each build's symbols before it ships,** to the project that gets its crashes (fact
   `fl-sentry-symbols`), and keep every Xcode archive you distribute (fact `fl-apple-archive`).
4. **Collect usage data only with consent where EU law applies, and little:** off until turned
   on, no stable ID, and one switch for every channel that an organization can set.
5. **Rate severity apart from priority.** Severity is harm to users, 0 to 4 (fact
   `uxr-severity-scale`); priority adds market impact (fact `fl-nng-market`), cost and risk.
6. **Keep the view apart from the state, and fix the pattern, not the screen:** every screen
   that shares the fault, each with a regression test.
7. **Guard a visual fix with a screenshot test,** a baseline per platform, made in CI's container.
8. **Check that the fix helped:** without full usage data, compare task success and support
   tickets under the issue's label, before and after.

### What a report carries

The version and build, the OS, screen size and scale, the window and last action, the last log
lines with home-folder paths, host and user names removed, and the person's words. A screenshot
goes only if they add one, as Sentry's web widget offers (fact `fl-sentry-screenshot`).

### An issue form the program fills in

`.github/ISSUE_TEMPLATE/problem.yml`:

```yaml
name: Problem report
description: Something didn't work as you expected
labels: ["bug", "triage"]
body:
  - type: textarea
    id: what-happened
    attributes:
      label: What happened, and what did you expect?
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Version
```

The program opens `https://github.com/OWNER/REPO/issues/new?template=problem.yml&version=4.2.1`,
and the person sees each value before submitting. Issue forms are in public preview (fact
`fl-gh-forms`): recheck the syntax when one stops rendering.

### Crash reports

- **Native code:** upload debug files in the release pipeline; Sentry doesn't reprocess earlier
  crashes or read another project's files (fact `fl-sentry-symbols`). **.NET** stacks read
  partly without them; upload anyway, above all on mobile (fact `fl-sentry-dotnet`).
- **Windows Error Reporting's LocalDumps** are off by default, need an administrator, and skip a
  program with its own reporter (fact `fl-wer-localdumps`): for your machines, not users'.
- **Automatic upload:** no source found calls it strictly necessary, so ask first.

### Usage data and consent

- **The law:** in the EU, storing or reading information on a person's device needs consent,
  unless it carries a communication or is strictly necessary for a service they asked for (fact
  `fl-eprivacy`). The EDPB reads "information" as any data, personal or not, and the rule as
  wider than cookies (fact `fl-edpb-scope`): an install ID is in scope. Not legal advice.
- **What projects do:** VS Code and Firefox collect until the person opts out (facts
  `fl-vscode-default`, `fl-firefox`). Follow KDE, opt-in with no unique ID (fact
  `fl-kde-telemetry`), and GNOME, which showed its data before upload (fact `fl-gnome-show`).
- **One switch:** VS Code's setting doesn't cover extensions (fact `fl-vscode-ab`), and
  Firefox's daily ping has its own (fact `fl-firefox`). List every channel, make the switch
  cover them all, and let an organization set it by policy (fact `fl-vscode-policy`).

### Internal tools on a local network

Reports and crashes go to a tracker or self-hosted Sentry on the network (fact
`fl-sentry-screenshot`). The users are few and known: ask them. Administrators can turn
LocalDumps on. How consent applies on an employer's devices wasn't researched: ask the data
protection contact, and default to opt-in.

### A fix that reaches every screen

Each platform names the split: MVVM (fact `fl-mvvm`), Qt's model/view (fact `fl-qt-modelview`),
SwiftUI's data model (fact `fl-swiftui-model`), Elm's model, view and update (fact `fl-elm`),
and React's derived state (fact `fl-react-state`). Then:

1. Reproduce the report, and write the test that fails.
2. List every screen sharing the cause (component, model, string, handler). Ask an agent for
   this list before it edits.
3. Fix it where they share it, and test each screen through the program's own entry point.
4. Ship a large change behind a flag, and remove it once it settles (fact `config-toggle-life`).

Screenshots differ by browser and platform, so each gets its own baseline, compared where it
was made (fact `fl-pw-platforms`): CI's container, run locally too. Set `maxDiffPixels` on the
test that needs it; `gui-testing` covers driving the toolkit.

## Mistakes

- **Symbols uploaded after release, or to another project:** those crashes stay unreadable.
  Upload in the release job.
- **Calling analytics strictly necessary,** or reading the rule as cookies only. Ask first.
- **An off switch that misses a channel,** such as extensions or a daily ping.
- **Fixing only the screen in the report,** or with no test. Fix the siblings; test each.
- **One baseline for every platform,** or a looser `threshold` to quiet a diff.
- **An A/B test on an opt-in user base:** small, self-chosen groups. Compare before and after.
- **Deleting the Xcode archive** of a shipped build.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| No report path in the program | The help menu | `GAP` | A report item showing its payload |
| Usage data on by default for EU users | The telemetry default; IDs written | `BLOCKER` | Opt-in, no stable ID |
| A channel the off switch misses | Each call sending usage or crash data | `DRIFT` | One switch, set by policy too |
| Symbols uploaded after release | The release workflow's order | `GAP` | Upload before publishing |
| Form labels that don't exist | `labels:` in `.github/ISSUE_TEMPLATE/` | `DRIFT` | Create them |
| Severity and priority in one label | The triage labels | `GAP` | Two labels |
| A fix to one screen of several, or untested | The diff, against a search for the cause | `GAP` | Fix the rest; add tests |
| Baselines shared across platforms | Baseline names; where CI makes them | `DRIFT` | Per platform, in CI's container |

## Why

### A report path inside the program

- **The reason:** people who won't open a tracker still press a menu item, and a report with
  its version and logs can be reproduced. Showing it first is GNOME's model (fact
  `fl-gnome-show`). No study found shows it beats an email address: our practice.
- **The cost:** redaction, a form, and somewhere to receive it. **Choose differently** where a
  support desk takes calls: give it the same fields.

### Symbols before release

- **The reason:** without symbols a crash shows addresses, and Sentry won't redo it (fact
  `fl-sentry-symbols`). **The cost:** a release step and storage per build. **Choose
  differently** for managed desktop code (fact `fl-sentry-dotnet`).

### Consent, opt-in and no stable ID

- **The reason:** EU law asks for consent (facts `fl-eprivacy`, `fl-edpb-scope`), and an ID
  that follows a person is what makes usage data personal.
- **Others:** VS Code and Firefox opt out, for numbers big enough for experiments (fact
  `fl-vscode-ab`); KDE and GNOME opt in, for trust.
- **The cost:** fewer, self-chosen numbers, and no A/B tests. **Choose differently** only on a
  lawyer's reading for your market.

### Severity apart from priority

NN/g weighs market impact apart from frequency, impact and persistence (fact `fl-nng-market`).
One label hides which drove a call; two cost one more label to keep.

### The pattern, guarded by a test

- **The reason:** the split makes an interface easier to test and change (facts `fl-mvvm`,
  `fl-swiftui-model`), so a fix lands once and a test reaches it. Rendering differs by platform
  (fact `fl-pw-platforms`), and a looser threshold hides small real changes.
- **The cost:** a model layer, and a baseline per platform.

### Before and after, not A/B

Experiments need full telemetry (fact `fl-vscode-ab`), which small and opt-in user bases lack;
task success and tickets still show a change. Our practice; with many consenting users, run one.

## Facts

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `fl-gh-forms` | Preview; `id` names the prefill; missing labels dropped | [Forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms), [schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema) | "currently in public preview" and "it will not be automatically added to the issue" and "the canonical identifier for the field in URL query parameter prefills" | 2026-11-16 | 2027-02-16 |
| `fl-sentry-screenshot` | Screenshot offered by default; self-hosted needs 24.4.2 | [User Feedback](https://docs.sentry.io/platforms/javascript/guides/react-router/user-feedback/) | "by default it is set to true" and "you also need release 24.4.2 and above" | 2026-11-16 | 2027-02-16 |
| `fl-sentry-symbols` | Upload before release; no reprocessing; per project | [Uploading](https://docs.sentry.io/platforms/native/data-management/debug-files/upload/) | "should be uploaded before deploying or releasing" and "Existing events and issues are not processed again." and "does not access debug files stored in other projects" | 2026-11-16 | 2027-02-16 |
| `fl-sentry-dotnet` | .NET symbols matter most on mobile | [.NET](https://docs.sentry.io/platforms/dotnet/guides/entityframework/data-management/debug-files/upload/) | "This is especially true for mobile apps" | 2026-11-16 | 2027-02-16 |
| `fl-apple-archive` | Keep each shipped archive | [Debug info](https://developer.apple.com/documentation/xcode/building-your-app-to-include-debugging-information) | "You must retain the Xcode archive for each build" | 2026-11-16 | 2027-05-16 |
| `fl-wer-localdumps` | Off by default; admin; not with a custom reporter | [Dumps](https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps) | "This feature is not enabled by default." and "custom crash reporting are not supported" | 2026-11-16 | 2027-05-16 |
| `fl-eprivacy` | Art. 5(3): consent, or strictly necessary | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219) | "has given his or her consent" and "explicitly requested by the subscriber or user" | 2026-11-16 | 2027-05-16 |
| `fl-edpb-scope` | Any information, not only cookies | [EDPB 2/2023 v2.0](https://www.edpb.europa.eu/system/files/documents/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf) | "includes both non-personal data and personal data" and "does not exclusively apply to cookies" | 2026-11-16 | 2027-05-16 |
| `fl-vscode-default` | VS Code telemetry on by default | [Source](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/telemetry/common/telemetryService.ts) | "'default': TelemetryConfiguration.ON" | 2026-11-16 | 2027-02-16 |
| `fl-vscode-ab` | Experiments need full telemetry; extensions not covered | [Telemetry](https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/configure/telemetry.md) | "To participate in the A/B experimentation" and "These extensions may be collecting their own usage data" | 2026-11-16 | 2027-02-16 |
| `fl-vscode-policy` | Policies set telemetry and feedback | [Enterprise](https://code.visualstudio.com/docs/enterprise/telemetry) | "Configure feedback mechanisms (issue reporter and surveys)" | 2026-11-16 | 2027-02-16 |
| `fl-firefox` | On by default; daily ping separate | [all.js](https://raw.githubusercontent.com/mozilla-firefox/firefox/main/modules/libpref/init/all.js), [notice](https://www.mozilla.org/en-US/privacy/firefox/) | "Health Report is enabled by default" and "will not impact the Daily Usage Ping" | 2026-11-16 | 2027-02-16 |
| `fl-kde-telemetry` | Opt-in, no unique ID | [Policy](https://community.kde.org/Policies/Telemetry_Policy) | "application telemetry is always opt-in" and "unique device, installation or user id" | 2026-11-16 | 2027-05-16 |
| `fl-gnome-show` | Data shown before upload | [GNOME blog](https://blogs.gnome.org/aday/2022/08/25/help-improve-gnome/) | "The tool shows the data that will be collected prior to uploading" | 2026-11-16 | 2027-05-16 |
| `fl-nng-market` | Market impact weighed too | [NN/g](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/) | "one needs to assess the market impact of the problem" | 2026-11-16 | 2027-05-16 |
| `fl-mvvm` | MVVM eases testing and change | [MVVM](https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm) | "makes an application easier to test, maintain, and evolve" | 2026-11-16 | 2027-05-16 |
| `fl-qt-modelview` | Storage apart from presentation | [Qt](https://doc.qt.io/qt-6/model-view-programming.html) | "separates the way that data is stored from the way that it is presented" | 2026-11-16 | 2027-05-16 |
| `fl-swiftui-model` | A separate data model | [SwiftUI](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app) | "improves testability" | 2026-11-16 | 2027-05-16 |
| `fl-elm` | Model, view, update | [Elm](https://guide.elm-lang.org/architecture/) | "a way to turn your state into HTML" | 2026-11-16 | 2027-05-16 |
| `fl-react-state` | Derive, don't store twice | [React](https://react.dev/learn/choosing-the-state-structure) | "you should not put that information into that component’s state" | 2026-11-16 | 2027-05-16 |
| `fl-pw-platforms` | A baseline per platform, compared where made | [Playwright](https://playwright.dev/docs/test-snapshots) | "you will need different snapshots for them" and "the same environment where the baseline screenshots were generated" | 2026-11-16 | 2027-02-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| GitHub Docs; Microsoft Learn; React docs | Issue forms; WER, MVVM; state | CC BY 4.0: quoted with attribution |
| VS Code docs and source | Telemetry | Docs CC BY 3.0 US, code MIT: quoted with attribution |
| Sentry docs | Feedback, symbols | FSL-1.1-Apache-2.0: short quotes, nothing adapted |
| EUR-Lex; EDPB | Consent | Not confirmed: short quotes with citation |
| Mozilla notice; Firefox source | Defaults | Creative Commons, version unnamed; MPL-2.0: short quotes |
| KDE wiki; GNOME blog; Apple docs | Opt-in; archives, SwiftUI | Not stated: short quotes only |
| NN/g | Market impact | All rights reserved: short quotes, our own words |
| Qt docs; Elm guide | Model/view | GFDL 1.3; CC BY-NC-ND 4.0: short quotes, never adapted |
| Playwright docs | Baselines | Apache-2.0: quoted with attribution |

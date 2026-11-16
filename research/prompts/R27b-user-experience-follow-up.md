# RESEARCH RUN R27b: User experience, what R27 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: user-experience.

## What this run is for

Follows R27, filed 10 November 2026, which covered Nielsen's heuristics and severity ratings,
dialogs on four platforms, choice overload, progressive disclosure, and GUI test drivers for Qt,
GTK, the web and Windows. It didn't read the platforms' progress and notification pages, testing
with people, macOS drivers, or rules on windows shown too early. This run takes those. R29 and
R30 hold UX writing, keyboard use, onboarding and visual regression; R18 holds WCAG. Don't
repeat its findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R27b · FORM: research-result v1
Save as: R27b-RESULT.md
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

- Five users find about 85% of a design's usability problems (Nielsen and Landauer, 1993), and
   later studies found that five users' yield varies widely by product and task.
- Thinking aloud while working, concurrent think-aloud, is the method NN/g recommends for most
   qualitative usability tests.
- Microsoft no longer maintains WinAppDriver, so Windows GUI tests go through UI Automation
   libraries such as FlaUI or pywinauto.
- No platform guideline says a window shouldn't show before its content is ready. We suspect one
   of Apple's, Microsoft's or GNOME's launch pages does, so this may be wrong.
- GNOME's HIG keeps notifications for events a person should see while in another app, and
   toasts for brief notices inside the app.

## Questions

### Priority

1. **Progress, status and notifications on each platform:** Read GNOME's HIG (progress bars,
   spinners, toasts, notifications), KDE's HIG (progress, notifications), Microsoft's Windows
   design and WinUI pages (ProgressBar, ProgressRing, InfoBar, app notifications) and Apple's
   HIG (progress indicators, notifications). Quote each rule on determinate against
   indeterminate progress, how long work runs before progress shows, canceling, announcing that
   work is done, and notifying a person who has switched away. Date each page.
2. **Testing with people:** On how many participants: Nielsen and Landauer (1993), Virzi (1992),
   Faulkner (2003) and any later meta-analysis. On think-aloud: Ericsson and Simon, Boren and
   Ramey (2000), and NN/g's current guidance, concurrent against retrospective. Also writing
   task scenarios and testing a first run. Report each figure with its sample and what it
   measured, and mark the contested ones.
3. **Driving macOS and Windows GUIs by machine:** For macOS: XCUITest on macOS apps, Appium's
   Mac2 driver and any other driver through the accessibility API, each with its version, date
   and maintenance status. For Windows: WinAppDriver's status, FlaUI, pywinauto 1.0's release
   status, and Appium's Windows drivers. For both: whether GitHub-hosted runners give these
   tools a desktop session to drive, quoting the runner docs.
4. **A window before it's ready, and after its subject is gone:** Search Apple's HIG on
   launching and loading, Microsoft's app startup and splash screen guidance, and GNOME's and
   KDE's HIGs for any rule on showing a window before its content is ready, a placeholder that
   could be taken for data, or a window whose file or device has gone. Quote what you find, and
   name each page you read when you find nothing.

### Standard

5. **Cognitive walkthrough and the evaluator effect:** Wharton, Rieman, Lewis and Polson (1994),
   Spencer's streamlined walkthrough (2000), and Hertzum and Jacobsen's evaluator effect (2001)
   with any later replication. Report how a walkthrough's findings compare with a heuristic
   evaluation's, and how far evaluators' problem lists and severity ratings agree.
6. **Where settings live, by platform:** GNOME's preferences pattern, KDE's settings guidance,
   Microsoft's app settings guidelines and Apple's HIG page on settings. Quote any rule on what
   goes in settings rather than beside the feature, a setting reachable from two places, and
   applying a change at once against an Apply button, beyond KDE's Switch-or-CheckBox rule.

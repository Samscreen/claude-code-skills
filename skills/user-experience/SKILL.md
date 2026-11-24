---
name: user-experience
description: "Reviews, designs and tests how a desktop, web or command-line program behaves for its user: platform patterns, status, dialogs, settings, GUI tests, and fixing what users report. Use when building, reviewing or testing an interface."
license: Apache-2.0
metadata:
  reviewed: "2026-11-16"
---

# User experience

How a program behaves for the person using it: what a current interface on its platform is
built from, whether its status is current, whether its windows and dialogs appear when they
should and nowhere else, whether its settings are easy to find and mean one thing each, how a
command-line program serves people and scripts, how to test all of that, and how to learn what's
wrong once people use it. It serves power-user programs as well
as simple ones: it never trades away a useful option to make a screen shorter. How the interface
looks (themes, palettes, charts) belongs to `visual-design`, the accessibility basics to
`coding`'s `html-coding` (a full module is planned in `visual-design`), and what people do
at work around a program to `human-factors`; the code itself to `coding`, and general test
design to `testing`.

## What applies to every module

These summarize the modules; each module holds the cases, the checks and the reasons, so read
the one that fits before answering.

1. **Follow the platform's guidelines,** GNOME's, KDE's, Apple's or Microsoft's, over a
   toolkit's defaults or a habit from another platform. The platforms set the rules; toolkits
   implement them.
2. **What the screen says is true now.** A status, a device list or a verdict that outlives the
   state it describes is a defect, not a cosmetic issue.
3. **Nothing appears that the person didn't ask for or can't see.** No window before it's
   ready, no dialog out of nowhere, none hidden behind another.
4. **Keep every useful option, and make the common path short:** good defaults, presets, and
   advanced options one step away.
5. **Prefer undo to a confirmation dialog** for anything that can be undone.
6. **Check behavior by running the program,** or with a test that drives it. Reading the code
   finds candidates; it can't show timing, stacking or focus.

## Modules

Read the module that fits the request, and each one a request spans. Each holds its rules,
mistakes, audit checks, reasons, dated facts and sources.

| Module | Read it for |
|---|---|
| [`usability-review`](references/usability-review.md) | Reviewing a program for what would confuse or annoy its users, with severity ratings; status and feedback that stay current; counts that say what they count; error messages; preventing and undoing destructive actions; making frequent actions faster for experts without removing options |
| [`windows-and-dialogs`](references/windows-and-dialogs.md) | When a window or dialog should appear; modality, parents and focus; default buttons; one dialog at a time (Qt, GTK, WinUI's ContentDialog, Apple); nothing hidden behind another or shown before it's ready; reviewing dialog code; long operations |
| [`settings-and-options`](references/settings-and-options.md) | Defaults and presets, progressive disclosure, hiding or graying out an option that doesn't apply, each setting in one place with one meaning, confirming a save with wide effects, an inventory of every setting, how many choices is too many, and power users' options |
| [`gui-testing`](references/gui-testing.md) | Driving a GUI from tests per toolkit (Qt, GTK, web, Windows), catching windows that appear wrongly or status that goes stale, and testing with people |
| [`feedback-loop`](references/feedback-loop.md) | Learning what's wrong once people use a program, and fixing it safely: in-app reports, GitHub issue forms filled from the app, crash reports and symbols, usage data only with consent, severity apart from priority, views apart from state, screenshot tests, and internal tools on a local network |
| [`interface-patterns`](references/interface-patterns.md) | What a current interface is built from: each platform's design language and toolkit at a supported release, stock components first, one component per pattern, layout by window width, dense power-user screens, forms, their errors and values the program corrects, and loading, empty and failed states |
| [`command-line-interfaces`](references/command-line-interfaces.md) | Command-line programs for people and scripts: POSIX and GNU option syntax, help and version, stdout against stderr, machine-readable output, color and NO_COLOR, prompts only on a terminal, dry runs and quiet mode, secrets kept off flags, and argument parsers per language |

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

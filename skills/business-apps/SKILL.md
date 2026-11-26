---
name: business-apps
description: "Business documents from code, starting with Word: .dotx templates, prompts split across runs, fields, tables of contents, numbered lists, change records. Read it before code writes or fills a .docx, and before answering any question about doing so."
license: Apache-2.0
metadata:
  reviewed: "2026-11-24"
---

# Business apps

**This page is an index. Before you answer, use the Read tool on the module file below that fits the request** (`references/<module>.md`, and each one the request spans): the module holds the facts, versions and checks an answer needs, and this page doesn't.

Code that produces or fills the documents a business runs on, starting with Word: templates,
fields, tables of contents, numbered lists and change records. Excel workbooks, Epicor Kinetic
and SOLIDWORKS join as their modules are built. The language the code is written in is `coding`;
colors and fonts are `visual-design`; a company's own templates and approval rules live in that
company's own skills, which use these for the mechanics.

## What applies to every module

These summarize the modules; each module holds the code, the checks and the reasons, so read
the one that fits before answering.

1. **Start from the organization's template,** and read it from the file before writing code.
2. **Check the output by opening it,** in the application people will use, before calling it done.
3. **Never invent a signature, an approval, a revision number or a date.** Leave the cell empty
   and say so.
4. **Pin each document library to an exact version,** and run the checks again on each upgrade.
5. **No company detail in shared code or skills:** names, servers and templates stay in the
   company's own repositories.

## Modules

Read the module that fits the request, and each one a request spans. Each holds its rules,
mistakes, audit checks, reasons, dated facts and sources.

| Module | Read it for |
|---|---|
| [`word-documents`](references/word-documents.md) | Filling a Word template from code: opening a `.dotx`, replacing prompts split across runs, `DATE` and `FILENAME` fields, a table of contents or fields right in Word but stale in a PDF or preview, restarting numbered and lettered lists, change records, and checking the result |
| [`epicor-kinetic`](references/epicor-kinetic.md) | Epicor Kinetic and ERP 10.2.x on the server: BPM method, data and updatable BAQ directives, what an in-transaction directive may do, C# in directives and Epicor Functions, BAQs, REST API v2 and API keys, and code that breaks when upgrading to Kinetic |

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

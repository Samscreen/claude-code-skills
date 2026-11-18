---
name: project-bootstrap-and-audit
description: "Sets up, retrofits or audits a repository against the PROJECT-BOOTSTRAP-AND-AUDIT standard: structure, CI, agent files, secrets, dependencies, licensing, release readiness. Stops for approval before changing anything."
license: CC0-1.0
metadata:
  standard-version: "0.52.0"
  files-sha256: "c83afe9cf7f13c1afa457bf94b5c5d3d8283686cb5a3395a61814310b8f7b376"
---

# Project bootstrap and audit

This is the standard's procedure: the jobs, what each reads, the two stops and the report. The
rules it runs by are in `references/`, and
[the standard file](references/PROJECT-BOOTSTRAP-AND-AUDIT-v0.52.0.md) holds the phases, the
dimensions and the rest.

Run this to set up a repository, retrofit one, or check whether existing configuration
still matches reality. It is re-runnable by design. Running it twice on an unchanged
repository must produce the same statuses and the same schema.

**Two cadences.** This standard runs at inception, before a release or deploy, and
when something feels stale. `TEST-VERIFICATION-CHECKLIST.md` runs per task, before claiming
work complete — it lives in the repository rather than beside this skill, and **Starter file
contents** specifies what goes in it.

**To run it:** start this skill in an agent session on a repository, with
`/project-bootstrap-and-audit` in Claude Code, and name the job. Or attach the release's
`KICKSTART.md`, the whole standard in one file, and say *"Run the attached
PROJECT-BOOTSTRAP-AND-AUDIT standard against this repository"* plus the job. It stops and waits
twice; nothing is written before you approve. **Sending results back** has the full prompt
and what to return.

**For something that does not exist yet**, start it in an empty repository — or none — and say
what you want to build and who runs it. It will choose a language and a shape with you before
it writes anything.

**It runs on any agent tool**, not only the one whose paths it names.
[Other tools](references/other-tools.md) and **Any agent, any tool** translate them, and every
run closes with a **conformance self-check** so a run on an unfamiliar model reports its own
weak points rather than leaving you to find them.

## Step 0: which copy is running

!`python3 "${CLAUDE_SKILL_DIR}/scripts/verify_copy.py"`

Claude Code runs the line above as the skill loads, and puts its result in its place (Claude
Code only). If it still shows a command, run `python3 scripts/verify_copy.py` yourself from this
skill's folder. It hashes every file of the skill but this one and compares the hash with
`files-sha256` above.

- `COPY OK`: record its hash in the self-check's `standard_sha256`, and go on.
- `COPY MISMATCH` or `COPY MISSING`: stop before Phase 0. Tell the person which copy loaded,
  from the line's `path=`, and that it is damaged or incomplete. Do nothing else.
- No shell to run it: record `standard_sha256` as `unknown`, and say why in Phase 0's `degraded`.

Then check that this copy is current. With `curl`, not a web-fetch tool, read `standard-version`
from https://raw.githubusercontent.com/Samscreen/claude-code-skills/main/skills/project-bootstrap-and-audit/SKILL.md
If it's newer than this file's, say so in one line, record it in Phase 0's `notes`, and go on:
it's a warning, never a stop. If the fetch fails, say "could not check" and go on.

## What this is for

Set up a new repository, or check an existing one against a baseline, **without a second
reviewer and without a platform team.** It replaces the judgment a colleague would apply at
inception and at release, with the reasoning written down so a later run can disagree with it.

**Goals.** Make inception decisions explicit, especially the irreversible ones. Make drift
findable rather than discovered. Keep configuration proportionate to what the project can
actually break. Leave a record that survives the session, so the next run starts from what was
decided rather than from scratch.

**Not a goal.** Judging whether the code is good. This reads configuration, structure and
process — never program logic, algorithms or correctness.

What the design rests on, and what it can't do, are in
[assumptions and limitations](references/assumptions-and-limitations.md).

## Scope

This covers **the repository**: how it is set up, configured, gated, reviewed, documented and
released. It does not cover how the work is run.

**In scope.** Bootstrap and setup files, agent configuration, enforcement and CI, review and
merge discipline, secrets handling, dependencies, licensing, packaging, versioning,
documentation currency, file governance, cross-repository contracts.

**Also in scope, and narrowly:** sequencing and milestones **for the repository's own
configuration work** — the order the amendments land in, what constitutes done, and where
that record lives. Phase 9 covers it. This is a deliberate reversal of the earlier position
that all planning was out of scope, made because a run that produces sixteen amendments and
no order of operations has handed over a pile, not a plan.

**Out of scope.** What the business should depend on, what is worth building, which features
come first, staffing, process. The line: **this standard may sequence work it proposed; it may
never sequence the product.** Where a finding needs one of those as an input — who depends
on this, does it touch production — **it is asked, never assumed**, and the answer is recorded
as given rather than argued with.

## How to read this skill

<constraints>

**Do not read this skill end to end.** The standard file is a reference, not a document, and
no job needs all of it. Read this file, then only the ranges your job calls for. **A run that
reads everything has paid for attention it did not use and diluted the rules it did.**

**Build the standard file's heading index first** — one command, run from this skill's folder,
and it is authoritative where a line number would only be a hint:

```
grep -n '^# \|^## ' references/PROJECT-BOOTSTRAP-AND-AUDIT-v0.52.0.md
```

Some of those matches are **inside template code blocks, not sections:** `# <project name>`
twice, `# Decisions`, `# Test Verification Checklist` and the `## ` headings under each, and
Phase 8's example entry, `## 2026-09-12 — Configuration audit`. A heading inside a code block
is never a section, and the table below routes each job to the real ones.

**Then read by range**, not by scrolling: `sed -n '<start>,<end>p'`, or your tool's read with an
offset and a limit. Where a section turns out to continue past the range you took, take the next
range — do not guess at what was cut off.

</constraints>

## What to read, by job

**Always, first:** this file, then the [standing rules](references/standing-rules.md), the
[environment](references/environment.md), the [vocabularies](references/vocabularies.md), and
the standard file's *Facts with an expiry date*. **Everything else is on demand.**

**This is the one routing table.** A second one drifted from it once, and two runs of the same
job could have read different sections. Reading a section that does not apply costs context and
dilutes attention on the ones that do. Each section is named exactly as it is headed, so the
heading index finds it in one match; the standard file holds every one this table doesn't link.

| Job | Then read | Skip |
|---|---|---|
| **Survey** — look, change nothing | *The run*, phases 0–5, then stop and report | Phases 6–9 |
| **Audit or retrofit** | *The run*, all phases, with the ten dimensions inside phase 4, plus *File governance* | *The release and deploy currency gate*; *Choosing a language and runtime*, *Choosing the shape* and *Project shapes and layout* unless a choice is itself a finding |
| **Set up something new**, including a repository that holds no source yet | *The run*, all phases, plus *Choosing a language and runtime*, *Choosing the shape*, *Project shapes and layout*, *Starter file contents* and *File governance* | *The release and deploy currency gate* |
| **Choose a language and a shape** before any source exists, with no repository yet or in one that holds no source | *Choosing a language and runtime*, *Choosing the shape* and *Project shapes and layout*. In a repository, *The run* as well: phases 0–3, stopping at the Phase 3 wait with the recommendation, and *The report* below for the shape of its report | Everything else, until the choice is made. Setting it up is then the row above |
| **Write a missing config file** | *Starter file contents* and *The configuration file map* | Everything else |
| **Cut a release or a deploy** | *The release and deploy currency gate*, plus version reconciliation in dimension 10 | Phases 1–9 |
| **Prune files** | *File governance* | Everything else |
| **Two repositories are involved, or more** | *Cross-repository contracts* — including the fleet case, and the copied-file trade | Nothing extra |
| **Plan what happens next** | *The run*, phase 9 | Everything else, if the audit is already done |
| **Running on a tool that is not Claude Code** | [Other tools](references/other-tools.md) and *Any agent, any tool*, then your job's row | Nothing extra |
| **Contribute a run to whoever maintains this** | *Sending results back* | Nothing extra |
| **Test this standard** | *Validating a change to this standard* — the whole procedure: corpus, order, prompts, what to record, and how to triage a failure. Its mechanical checks need no repository at all | Everything else |

**Every job ends with the [conformance self-check](references/self-check.md).** It is short and
it is the only part of this skill that asks the run to report on itself.

**Within a run, skip further:**

- ***The release and deploy currency gate*, *Cross-repository contracts*,
  *Standards distribution*** — only when cutting a release or a deploy, where this repository
  provides to or consumes from another, or when proposing how a standard reaches many
  repositories. Most runs need none of the three.
- **A dimension that is `N/A` at this tier** — record it and move on. Do not argue it.

**Survey mode is the whole of the old reconnaissance pass.** Phases 0–5 are read-only and
produce more than a separate survey tool did. If you were asked only to look, run them, emit
their blocks, and stop before Phase 6.

## What not to read during a run

| Section | Why |
|---|---|
| *Provenance* | The version history and the incident behind every rule, for whoever maintains this standard. Read it when a rule looks arbitrary and you want to know what produced it — **never to be thorough**. Skip it unless you are changing the standard |
| *Validating a change to this standard* | For testing this standard, not for running it |
| *Proposing a change to this standard* | Read it only when you have found this standard wrong; it says how that reaches the gate |

**If your tool gave you this whole skill in context and you cannot read selectively, that is
fine** — the routing above still tells you which parts to attend to, and which to skip.

## The stops

**The gates — what stops a run.** They hold in every phase, beside the
[standing rules](references/standing-rules.md).

- **Stop at Phase 6.** Nothing is written to the repository before explicit human
  approval. Reporting is not permission.
<!-- WHY exactly two waits: adherence decays measurably within a session, so gates counter
     drift — but each extra wait costs a round trip and invites the human to answer what the
     file could answer itself. Two is the floor, not a default to extend. -->
- **Phases 0–5 run in one pass**, each emitting its schema block before the next begins.
  **There are exactly two waits: Phase 3 and Phase 6.** Do not invent others.
- **Each phase opens with one short progress line:** the phase, and what it's about to do.
  In a long session the owner otherwise hears nothing between blocks, and the platform
  reminds the session, again and again, that the owner has heard nothing.
- **Every run produces exactly one file.** Written outside the repository, named
  `RUN-REPORT-<repo>-<YYYY-MM-DD>.md`, containing everything the run produced — decisions to
  answer first, then every emission block. **The human must never have to assemble a report
  by copying pieces out of the conversation.** Emission blocks still appear in the reply as
  the run proceeds; the file is the durable copy and the only thing that has to travel.
  **Where the request names the report's files, form or place, follow it,** keep every schema
  block, and record the difference in `overrides`. One audit's owner asked for two files in a
  private repository, and the run had no rule saying the request wins.
- **Emit the schema, and only its fields.** Every phase has a required field set and every
  phase has `notes` for anything the fields cannot hold. Fill every field. **Do not add
  fields.**

A run told not to wait, and given no answers, follows the standard's Phase 3 rule for that
case rather than improvising one.

## The report

**Whatever the job, it ends with one file.** Survey ends with phases 0–5 in it; a run stopped
at the Phase 3 wait ends with 0–3 and the questions to answer; a run stopped at the gate ends
with 0–6 and the decisions to answer; a full run ends with 0–9. Same name, same shape, one
attachment. [The skeleton](assets/report-skeleton.md) lays it out, and
[the schema](assets/report-schema.json) names each block's fields.

<!-- WHY a file, not the reply body: a reply does not survive being carried into another
     session, and the human should never assemble a report by copying blocks out of a
     transcript. Two runs read silence here and did opposite things. -->
<!-- WHY delivery is separate from writing: reports have been written to a container
     scratchpad that dies within the hour. Every run so far attached the file anyway, which
     was the agent being sensible rather than this file requiring it. -->
**Writing the report is not delivering it.** Outside the repository, in an ephemeral
container, means gone within the hour. **Hand the file over in the same turn** — attached, or
its full content in the reply where the tool cannot attach — and say plainly that the path is
temporary. A report that was written and not delivered is the same as no report, and it is the
one artifact with no copy anywhere else.

**Emit the run report as a markdown file outside the repository**, named
`RUN-REPORT-<repo>-<YYYY-MM-DD>.md`, with `lifecycle: transient` and a concrete `expires:`.
The prohibition is on writing **to the repository**.

**Where it's kept follows who owns the audited repository.** The report holds the repository's
internals, open security findings included, and its owner chose where those live. A personal
repository's report stays in that repository, by its own rules for records, or in the session;
a company's goes where the company keeps its reports. **Never file one owner's findings in the
other's repository**, a personal project's in a company's report repository or the reverse,
however convenient that repository is. When the owner of the audited repository isn't clear,
ask before filing.

**Open with a reconciliation header**, the skeleton's first block, so any reader — human or
another model — can triage without reading the body and can diff two runs mechanically.

**Then structure it for two readers, in this order:**

1. **The decisions**, in plain prose a human answers without scrolling — the three lists the
   standard's Phase 6 gives.
2. **An appendix holding every emission block so far**, `phase: 0` through `phase: 6`, verbatim.

The human reads the top to answer and forwards the whole file to whoever is reviewing the
standard. **They must not have to copy blocks out of the conversation to do that.**

**A run that ends at the Phase 3 wait still hands over its report**, in the same shape: the
same name, `lifecycle: transient` with a concrete `expires:`, and the reconciliation header,
whose `tally` reads `not yet rated`. **In place of Phase 6's three lists it holds the questions
asked**, each with its draft and evidence, and any recommendation still waiting on a pick. The
appendix holds the blocks from `phase: 0` to `phase: 3`, then the *Conformance self-check*,
where `ten_statuses_emitted` and `tally_sums_to_ten` are `n/a` and `waits_observed` is 1. If the
run continues after the answers, it appends to the same file. Its `overrides` go in the Phase 3
block's `notes`, since the Phase 4 block that holds them is never emitted.

**Then finish the run report.** After Phase 9, append the `phase: 7`, `phase: 8` and `phase: 9`
blocks to the same file from Phase 6 — do not start a second one — and replace its decisions
section with a short outcome summary: what was applied, declined, deferred, what remains for
the human, and the CI conclusion after the push. **Say where the file is and that it is ready
to hand on.**

**Check the file before handing it over:** `python3 scripts/check_report.py <report>`, from
this skill's folder. It reads the YAML blocks only: each block's fields against the schema,
the phases in order and ending at a stop, Phase 4's ten statuses and tally, Phase 6's closure,
and the self-check's waits. Fix what it finds, or say in the report's `notes` why the report
is right. Without a shell, say it wasn't run.

## Other files here

Where a repository keeps an `evidence` branch, as the standard's *Generated evidence* describes,
[scripts/verify_evidence.py](scripts/verify_evidence.py) checks the branch and its manifest in a
local copy, and its first lines say how to make one. It reads Git only and changes nothing.

[assets/skill-overrides.json](assets/skill-overrides.json) is the owner's exclusion list: the
skills synced from their claude.ai account that repository sessions don't load, each with its
reason. The standard's dimension 4 says how a run proposes it, as `skillOverrides` in the
repository's `.claude/settings.json` (Claude Code only).

[scripts/verify_copy.py](scripts/verify_copy.py) is Step 0's check, and
[scripts/check_report.py](scripts/check_report.py) the report's. Both use Python's standard
library only.

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

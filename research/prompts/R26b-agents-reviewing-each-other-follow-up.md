# RESEARCH RUN R26b: Agents reviewing each other, what R26 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: review-loops.

## What this run is for

Follows R26, filed 10 November 2026, which covered multi-agent debate and its stopping rules,
Claude Code Review and Copilot code review, Google's review guide, contract tools and fencing
tokens. It didn't reach Claude Code's own coordination features, other AI reviewers, measured
results of AI review in real repositories, or whether a reviewer favors its own model's work.
This run takes those; contracts beyond OpenAPI are R19's. Don't repeat its findings; where one
has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R26b · FORM: research-result v1
Save as: R26b-RESULT.md
Receiving session: this is research the repository owner asked for. Check each claim against the source it cites before relying on it. File the report under research/runs/, update the facts files of the categories it names, and list what changed. If you lack context, the owner will attach HANDOFF.md.
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

- Claude Code's agent teams are experimental and off by default. Teammates claim tasks from a
   shared list, and Claude Code stops two of them claiming the same task.
- A Claude Code subagent can't start subagents of its own, and its caller sees only its final
   message.
- A model judging two answers rates its own model's answer above an equal one from another
   model, so a reviewer from a different model family catches more.
- Of the AI reviewers, only Copilot's approval can count toward a branch's required reviews;
   CodeRabbit, Graphite, Gemini Code Assist and Cursor Bugbot only comment. We suspect this is
   out of date.
- Copilot code review's Max effort level is still in public preview.

## Questions

### Priority

1. **Claude Code's coordination features:** From the agent teams, subagents, cross-session
   messaging and worktree pages on code.claude.com, and the changelog: how a teammate claims a
   task and what stops two claiming one, how messages pass, what the lead sees, whether a
   subagent can start its own, and each documented limitation. Give the version that added each
   and whether it's still experimental. Say what keeps two agents from editing one file at once,
   or that nothing does.
2. **Other AI reviewers, from their own docs:** CodeRabbit, Graphite, Gemini Code Assist on
   GitHub, Cursor Bugbot and OpenAI's Codex code review. For each: whether it can approve or
   request changes, and whether that counts toward branch protection; which configuration or
   instruction files it reads, and from which branch, base or head; whether it builds or runs
   code; and what it does with a comment a person resolved or dismissed. Quote and date each.
3. **Measured results of AI code review:** Peer-reviewed or arXiv studies from 2024 to 2026 of
   AI review comments in real repositories, industrial or open source. Report the share of
   comments acted on, the false-positive rate, the sample and the design, and whether any
   compares one AI reviewer with several. Mark a vendor's own figures as the vendor's.
4. **Self-preference in model reviewers:** Studies of whether a model rates its own or its
   family's output higher, such as Panickssery et al. (arXiv:2404.13076), and whether a reviewer
   from another model family, or one that doesn't see the author's reasoning, finds more defects
   in code. Report effect sizes and the tasks measured.

### Standard

5. **Copilot code review since 28 October 2026:** From GitHub's changelog and docs: the status
   of Max effort and of approvals, the reasons for resolving a comment (reported for 27 August
   2026 only by a secondary source), and any change to how Copilot repeats a dismissed comment.
6. **Records of agent work:** The status of OpenTelemetry's GenAI semantic conventions for
   agents, stable or in development, and what an agent or tool-call span records. Say whether
   any published format records a review round: who wrote, which commit it judged, and the
   verdict.
7. **OpenAI's own statement on human review:** R26 found only secondhand that OpenAI's
   experiments make human pull request review optional. Find OpenAI's primary statement and
   quote it, or write "not found".

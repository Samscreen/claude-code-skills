# RESEARCH RUN R01b: Agents, Claude Code and review loops, what R01 and R26 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: agent-context-files, ai-agent-security, review-loops, skill-builder.

## What this run is for

Follows R01 (filed 23 September 2026: context files, Claude Code 2.1.280's settings, MCP,
OWASP's lists, skills as a supply chain) and R26 (filed 10 November 2026: agents reviewing each
other). Claude Code has shipped about forty releases since R01. This run takes what changed in
its permissions, sandbox, hooks, skills and plugins; auto mode; cloud sessions' security; agent
teams and subagents; OWASP's agentic list; other AI reviewers; and measured evidence on context
files and AI review. Don't repeat their findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R01b · FORM: research-result v1
Save as: R01b-RESULT.md
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

- A cloud session at claude.ai/code runs Bash inside Claude Code's command sandbox, so the
  sandbox's limits hold there as they do in a terminal. We suspect this is out of date.
- Auto mode sends each tool call to a classifier, and neither a project's committed settings nor
  a plugin can widen what it allows.
- Since 2.1.281, Claude Code reads `AGENTS.md` natively on every provider, unless a `CLAUDE.md`,
  `.claude/CLAUDE.md` or `CLAUDE.local.md` sits in the working directory or above it.
- MCP's current specification revision is 2026-07-28, and the official MCP Registry checks who
  owns a namespace but not what a server does.
- OWASP's Top 10 for Agentic Applications 2026 runs from ASI01 to ASI10, with Agent Goal Hijack
  as ASI01.
- Claude Code's agent teams are experimental and off by default. Teammates claim tasks from a
  shared list, and Claude Code stops two of them claiming the same task.
- Of the AI reviewers, only Copilot's approval can count toward a branch's required reviews;
  CodeRabbit, Graphite, Gemini Code Assist and Cursor Bugbot only comment. We suspect this is
  out of date.

## Questions

### Priority

1. **Claude Code from 2.1.280 to today:** Read the changelog (code.claude.com/docs/en/changelog)
   from 2.1.281 to the current release, and the permissions, sandboxing, hooks, settings, skills
   and plugins pages. List each change that alters what a committed setting, deny rule, hook or
   sandbox guarantees, or what a repository should commit. Give the version, its date and the
   changelog line, quoted. Include at least sandboxed Bash and
   `sandbox.autoAllowBashIfSandboxed`, skills that declare `allowed-tools` or hooks under
   scheduled tasks, `.mcp.json` approvals by exact name, `engines["claude-code"]` in
   `plugin.json`, and managed `extraKnownMarketplaces`.
2. **Permission modes and auto mode:** From the permission modes and settings pages, give what
   each mode (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`) allows,
   and which modes a cloud session offers. For auto mode, quote what its classifier blocks by
   default, which settings files can set `autoMode.allow`, whether project settings or a plugin
   can widen it, what happens when its server-side check is unavailable, and how it treats
   subagents. Say which mode Anthropic recommends for an unattended session, in its words.
3. **Cloud sessions' security model:** From the Claude Code on the web, cloud environments and
   security pages: whether the hosted container has a command sandbox (a 2026 changelog line
   says it has none), and what stands in for it, such as network access levels, the GitHub proxy
   and credentials held outside the container. Which of a repository's settings files, hooks and
   `.mcp.json` a cloud session reads, and what a setup script can reach. Then settle what R22
   left open: whether synced plugins load in cloud sessions, how `AskUserQuestion` shows on the
   web and in the mobile app, and what a session holding several repositories reads from each.
   Quote and date each page.
4. **Claude Code's coordination features:** From the agent teams, subagents, cross-session
   messaging and worktree pages on code.claude.com, and the changelog: how a teammate claims a
   task and what stops two claiming one, how messages pass, what the lead sees, whether a
   subagent can start its own, and each documented limitation. Give the version that added each
   and whether it's still experimental. Say what keeps two agents from editing one file at once,
   or that nothing does.
5. **OWASP's agentic list, item by item:** From OWASP's own Top 10 for Agentic Applications 2026
   (genai.owasp.org) and its source repository: each ASI item's exact name and its listed
   mitigations, quoted. Settle ASI04's name. Give the document's version, date and license. Say
   what the "agent control standard" in OWASP's 1 September 2026 press release is, and its
   status.

### Standard

6. **MCP since 2026-07-28:** From the specification site, its changelog and blog: any newer
   revision or announced date, and the deprecated features' status. From the official MCP
   Registry's docs: what it verifies when a server is published, and its own status. From Claude
   Code's MCP page and changelog: which revision it implements, and whether it warns when a
   tool's description changes after approval.
7. **Other AI reviewers, from their own docs:** CodeRabbit, Graphite, Gemini Code Assist on
   GitHub, Cursor Bugbot and OpenAI's Codex code review. For each: whether it can approve or
   request changes, and whether that counts toward branch protection; which configuration or
   instruction files it reads, and from which branch, base or head; whether it builds or runs
   code; and what it does with a comment a person resolved or dismissed. Quote and date each.
   Also, from GitHub's changelog and docs, Copilot code review since 28 October 2026: the status
   of Max effort and of approvals, the reasons for resolving a comment, and any change to how it
   repeats a dismissed comment.
8. **Measured evidence on context files and AI review:** Studies published from 2024 to 2026,
   peer-reviewed or on arXiv, that measure (a) what `AGENTS.md` or `CLAUDE.md` content does to
   task success, cost or rule adherence, settling length against adherence where Anthropic's
   docs and McMillan (arXiv:2605.10039) disagree; (b) AI review comments in real repositories:
   the share acted on, the false-positive rate, and whether several AI reviewers beat one; and
   (c) whether a model rates its own or its family's output higher (Panickssery et al.,
   arXiv:2404.13076) and whether a reviewer from another family finds more defects. Give each
   design, sample and effect size, and mark a vendor's own figures as the vendor's.
9. **Skills and plugins on claude.ai:** From the Help Center and claude.com's plugin pages: a
   skill upload's size and file limits; the description limit, where the Help Center says 200
   characters and the Agent Skills specification 1,024; what a same-name upload does; and
   whether organization sync honors a `sha` pin. Date each page.
10. **Other agents' context files today:** From each tool's docs: which files Antigravity CLI
    reads; whether Codex's `project_doc_max_bytes` counts per file or combined; size limits for
    Copilot's and Gemini CLI's instruction files; and whether Copilot code review still reads
    instructions from the pull request's head branch.
11. **Government guidance on agents:** The current editions of NIST AI 100-2 and NIST AI 600-1,
    and any CISA, NCSC or joint guidance on AI agents published in 2026. Quote only controls
    that would change a rule for an agent session, such as on credentials, logging or a person's
    approval.
12. **Records of agent work:** The status of OpenTelemetry's GenAI semantic conventions for
    agents, stable or in development, and what an agent or tool-call span records. Say whether
    any published format records a review round: who wrote, which commit it judged, and the
    verdict.

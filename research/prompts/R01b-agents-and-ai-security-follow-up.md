# RESEARCH RUN R01b: Agents and AI security, what R01 didn't reach and what changed since

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: ai-agent-security, agent-context-files, skill-builder.

## What this run is for

Follows R01, filed 23 September 2026, which covered context files, Claude Code 2.1.280's
settings, MCP 2026-07-28, OWASP's 2026 lists and skills as a supply chain. Claude Code has
shipped about forty releases since. This run takes what changed in its permissions, sandbox,
hooks, skills and plugins; auto mode; cloud sessions' security; OWASP's agentic list item by
item; MCP since July; and the platform questions R22 left open. Don't repeat its findings; where
one has changed since, say so.

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
4. **OWASP's agentic list, item by item:** From OWASP's own Top 10 for Agentic Applications 2026
   (genai.owasp.org) and its source repository: each ASI item's exact name and its listed
   mitigations, quoted. Settle ASI04's name. Give the document's version, date and license. Say
   what the "agent control standard" in OWASP's 1 September 2026 press release is, and its
   status.
5. **MCP since 2026-07-28:** From the specification site, its changelog and blog: any newer
   revision or announced date, and the deprecated features' status. From the official MCP
   Registry's docs: what it verifies when a server is published, and its own status. From Claude
   Code's MCP page and changelog: which revision it implements, and whether it warns when a
   tool's description changes after approval.

### Standard

6. **Skills and plugins on claude.ai:** From the Help Center and claude.com's plugin pages: a
   skill upload's size and file limits; the description limit, where the Help Center says 200
   characters and the Agent Skills specification 1,024; what a same-name upload does; and
   whether organization sync honors a `sha` pin. Date each page.
7. **Other agents' context files today:** From each tool's docs: which files Antigravity CLI
   reads; whether Codex's `project_doc_max_bytes` counts per file or combined; size limits for
   Copilot's and Gemini CLI's instruction files; and whether Copilot code review still reads
   instructions from the pull request's head branch.
8. **New evidence on context files:** Studies published after June 2026, peer-reviewed or on
   arXiv, that measure what `AGENTS.md` or `CLAUDE.md` content does to task success, cost or
   rule adherence. Give each design, sample and effect size. Say whether any settles length
   against adherence, where Anthropic's docs and McMillan (arXiv:2605.10039) disagree.
9. **Government guidance on agents:** The current editions of NIST AI 100-2 and NIST AI 600-1,
   and any CISA, NCSC or joint guidance on AI agents published in 2026. Quote only controls that
   would change a rule for an agent session, such as on credentials, logging or a person's
   approval.

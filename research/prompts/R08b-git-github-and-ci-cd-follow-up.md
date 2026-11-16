# RESEARCH RUN R08b: Git, GitHub and CI/CD, what changed since R08

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: ci-workflows, actions-security, action-pinning, branches-and-merging, commits-and-pull-requests.

## What this run is for

A follow-up. R08 was filed on 23 September 2026. It covered Git, GitHub, code review and CI/CD,
and the git-workflows modules were built from it, with most facts checked between 30 September
and 5 October. GitHub changes monthly. This run takes what changed since in Actions, rulesets,
merge queues, Dependabot and code scanning, plus commit signing and Git's own releases, which
R08 didn't reach. Installs, provenance and registries are R24's; agents reviewing code are
R26's. Don't repeat its findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R08b · FORM: research-result v1
Save as: R08b-RESULT.md
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

- From 2 December 2026, a default rule blocks `pull_request_target` on public repositories that
  have no event policy. The date moved from 2 November in an editor's note of 21 October.
- Workflow dependency lockfiles (`.github/workflows/actions.lock`, made by `gh actions-lock`)
  have been generally available on every plan since 28 October 2026, and Dependabot regenerates
  their entries.
- Dependabot raises no security alert for an action pinned to a full commit SHA.
- Merge queues are offered only in repositories owned by an organization (public ones, or
  private ones on Enterprise Cloud), never in a personal account's.
- A workflow skipped by a path filter leaves its required check pending, so the pull request
  can't merge.

## Questions

### Priority

1. **GitHub Actions since 23 September 2026:** List every GitHub changelog entry from 2026-09-23
   to today on Actions. For each, give the date, a quote and what a workflow author must change.
   Cover at least: the `pull_request_target` default rule (still 2 December, or moved?),
   `actions/checkout` and the other `actions/*` majors with their release tags, workflow
   lockfiles after general availability, the JavaScript-action runtime after Node 24, runner
   image changes (`ubuntu-latest`, Windows, macOS), and any billing change for hosted or self-
   hosted runners.
2. **Rulesets and merge queues:** Find new rule types and settings since September, from GitHub
   Docs and the changelog. Settle the contested plan for push rulesets (Team or Enterprise
   Cloud) from the current docs. Say whether merge queues are now offered to personal accounts'
   repositories, and whether a required check skipped by a path filter still blocks a merge.
   Quote each.
3. **Dependabot:** Report changes since September in the options reference and changelog:
   cooldown, grouping of security updates, new ecosystems, lockfile support for actions, and
   auto-triage rules. Say whether Dependabot now raises alerts for SHA-pinned actions. Quote the
   docs.
4. **Code scanning and secret scanning:** Report changes since September: CodeQL default setup
   on public repositories, CodeQL's analysis of workflow files, Copilot Autofix availability,
   code scanning in rulesets as merge protection, and push protection defaults. Give the date
   and plan for each.

### Standard

5. **Signing commits:** Compare SSH, GPG and Sigstore's gitsign from Git's and GitHub's docs:
   what GitHub shows as "Verified", vigilant mode, the ruleset rule that requires signed commits
   and how it treats merges made in the web interface or by bots, and what a history rewrite
   does to signatures. Give gitsign's current version and date.
6. **Git itself:** List Git releases after 2.56.1 (26 October 2026), with dates and notable
   changes from the release notes. Report Git 3.0's status and any date from the Git project's
   own pages (BreakingChanges, the mailing list), not secondary news.
7. **Large files:** Report Git LFS's current version, GitHub's LFS storage and bandwidth quotas
   and billing per plan, and GitHub's file-size limits for pushes, with quotes. Say when
   GitHub's docs advise LFS over a release asset.

# Pull request stewardship

Read this for writing, reviewing or auditing a repository's own steward skill: the file that
tells any agent session driving that repository's pull requests when to merge or hold, what to do
about a red or stalled check or a conflict, how to answer review, what an owner's hold covers,
and when to stop; and for the script that reads a commit's checks for it.

This module is the framework; each repository owns its answers. Commits, merge methods, required
checks, CI time and releases are other modules': `commits-and-pull-requests`,
`branches-and-merging`, `ci-workflows`, `ci-speed` and `releases-and-versions`.

## Rules

1. **A repository whose pull requests agent sessions drive keeps a steward skill,** committed at
   `.claude/skills/steward/SKILL.md`, and its `CLAUDE.md` names it, so a session that doesn't
   load project skills still reads it.
2. **It answers every decision a session makes alone:** merge, hold, re-run, fix, resolve a
   conflict, ask, stop, report. Where it's silent, the session holds, asks, and says so.
3. **Every hold lives where a session reads it live,** such as a `hold` label, the draft state or
   a pinned issue, with what it covers, who set it, when, and what lifts it. The file names that
   place and lists the standing holds, read again at the moment of merging, releasing or sending
   anything out. A lift replaces its hold where the hold is recorded.
4. **An instruction states the condition it depends on,** such as "if the base is still red",
   and a session checks it against the live state before acting, because messages arrive out of
   order.
5. **A claim names what was measured:** which platforms, which reverts, which commit.
6. **It grants nothing only the owner can.** Merging, releasing and wider access are the owner's
   to give, in the conversation or as a dated standing word the file quotes. A session never
   approves: its replies post under the owner's account (fact `autofix-replies`).
7. **Changes to the steward file, `CLAUDE.md`, the workflows or the ruleset are merged by the
   owner,** never by a session; with more than one reviewer, `CODEOWNERS` covers them (the
   standard's dimension 3). The base branch's copy is in force. On a one-person account GitHub
   can't enforce this, since an author can't approve their own pull request (fact
   `self-approval`), so it holds by the session's conduct, and the file says so.
8. **Bots' pull requests have a named tender,** who brings in Dependabot's and lockfile
   refreshes', and when; a red one is fixed or closed with a reason.
9. **It stays short, and points to the repository's other records** rather than repeating them;
   every audit checks it against the settings and workflows it names.

### Where it lives, and why that name

A project skill is `.claude/skills/<name>/SKILL.md`, committed, and loads in that repository's
sessions but not in a project's cloud threads (fact `project-skills`). Name it `steward`: a
Claude Code cloud session driving a pull request is told to read
`.claude/skills/steward/SKILL.md`, or `.claude/skills/babysit/SKILL.md` without one, from the
head branch, as seen in its instructions on 2026-11-03. The public docs name neither path, so
the audit checks it; another name, such as `babysit-pr/`, isn't found.

Auto-fix asks about what isn't clear (fact `autofix-events`), and gets no event when the base
branch moves into a conflict (fact `autofix-conflicts`).

### What the file answers

Copy [assets/steward/SKILL.md.template](../assets/steward/SKILL.md.template) to
`.claude/skills/steward/SKILL.md`, replacing each angle-bracketed part with the repository's
answer, or "none" and why. It covers merging, holds, conflicts and stale branches, red or
stalled CI, review, releases and other repositories, and when to stop.

### The mechanical half: reading the checks

The file is the judgment; [scripts/pr_verdict.py](../scripts/pr_verdict.py) reads the checks.
Run `python3 pr_verdict.py --repo OWNER/NAME --pr N`, or `--sha SHA [--branch B]`, before each
merge, re-run or report. From the REST API, never printed output, it reads the base branch's
required checks (fact `branch-rules`) and the commit's check and workflow runs (fact
`run-pages`), counting each check's newest run only. The worst verdict wins, as the exit status:

- `FAILED` (1): a check failed or timed out, required or not.
- `BLOCKED` (3): a required check never reported though every workflow run finished: the rules
  name a job that's gone, which only the owner can fix.
- `CANCELLED` (4): a required check's newest run was canceled: judge the newest head.
- `PENDING` (2): anything queued or running. `GREEN` (0): every required check passed, and
  nothing else failed or runs. 5 is no verdict, never green.

`--logs` prints every line of a failed job's log naming a failure (fact `job-logs`). Rules are
read as they are now, so an older commit can read `BLOCKED`: judge the newest. Copy the script
into the repository, or run it from this skill.

## Mistakes

- **A hold that arrived after the merge.** The owner's message to wait was delivered after a
  session merged. Put holds where a session reads them live, each message with its condition.
- **"Full suite green" from one platform,** while macOS failed. Name what a claim covers.
- **Canceling the same stalled job by hand, four times.** A known stall belongs in the file,
  with a step timeout, recorded until its cause is found.
- **Re-running a failed timing test in the hope it was noise.** Measure it first: once, the
  test was slow, not the runner.
- **Treating a steward file as authority to merge or approve.** A pull request can change it.
- **A merge's head commit typed by hand.** Pass the head SHA from the API's answer, so a merge
  stops if anything landed after the checks ran.
- **A new file left untracked through the last local run,** so checks passed on a tree CI
  never sees. Run `git status` first, and commit what it lists.
- **A wait loop that parses printed output.** A changed message ends it early or never. Wait
  on `pr_verdict.py`'s exit status, and time it out.
- **Reading only a failed log's last line,** which names one failure and hides the rest.

## Audit

Severity uses the standard's status words, defined in this skill's `SKILL.md`.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| No steward file | Sessions drive pull requests here, and `.claude/skills/steward/SKILL.md` is missing, or `CLAUDE.md` doesn't name it | `GAP` | Write it from `assets/steward/SKILL.md.template` |
| A decision left unanswered | Each section of the template, against what sessions did in the last pull requests | `GAP` | Answer it, or say "none" and why |
| Holds only in the file | No live place for holds, or no scope or lift for one | `GAP` | A label, draft state or issue, named in the file |
| The file can change itself | With more than one reviewer, no `CODEOWNERS` entry or required review on `.claude/skills/steward/` | `GAP`; `MIRROR` on a one-person account | Add both; alone, say so in the file |
| The file disagrees with the repository | Its merge method and checks against the settings and the ruleset, read through the REST API (fact `rest-public`) | `DRIFT` | Fix whichever is wrong |
| It claims what only the owner grants | Approving, or merging or releasing with no quoted word | `DRIFT` | Quote the owner's dated word, or remove the claim |
| Re-runs with no bound | Its CI section | `GAP` | Once, in the two cases above (fact `rerun-window`) |
| Checks read by eye | Its CI section reads a page or a command's printed output | `GAP` | Name `pr_verdict.py` |
| Replies can trigger automation | Workflows on `issue_comment`, and auto-fix on (fact `autofix-replies`) | `GAP` where one deploys or writes | Say so in the file, or turn auto-fix off |
| Out of date | Its reviewed date against the last change to the settings or workflows it names | `DRIFT` | Review it, and update the date |
| A bot's pull request is red or idle | Bots' pull requests, against the file's tender | `GAP` where one is a week red | Name the tender; fix or close it |
| The steward path is unconfirmed | Whether a cloud session driving a pull request still reads it | `UNVERIFIABLE-HERE` outside one | Record the date it was last seen |

## Why

### A file each repository owns

- **The advice:** a short steward file in the repository, written from the template.
- **The reason:** an unattended session decides when to merge, hold or re-run. Without a file,
  each decides afresh, from rules in conversations that aren't kept. In one audit cycle, rules
  lived in `CLAUDE.md`, notes and pasted messages, and a hold came late.
- **What others do, and why:** public babysit skills drive a pull request to green; one never
  merges (fact `babysit-never-merges`). Claude Code asks before an ambiguous change (fact
  `autofix-events`).
- **What it costs:** a file to keep current.
- **When to choose differently:** where no session drives pull requests, say so in `CLAUDE.md`.

### Holds read live, again when acting

- **The advice:** each hold read live, again right before acting.
- **The reason:** a hold in a message is lost when the conversation is summarized or restarts,
  and can arrive after the action it meant to stop. One only in the committed file takes effect
  when that commit merges, which a session on its head branch may not see.
- **What others do, and why:** GitHub's own gates, the draft state and required checks, hold on
  every merge path.
- **What it costs:** a label or check to set up.
- **When to choose differently:** a standing hold, such as "release nothing", can live in the
  file.

### Bounded re-runs

- **The advice:** re-run a job once, and only when the failure isn't this pull request's code.
- **The reason:** a re-run that turns green hides a real failure; one that keeps stalling wastes
  runner time and attention. Each re-runs the same commit (fact `rerun-window`), so it never
  tests a base that has moved.
- **What others do, and why:** `ci-workflows` re-runs once, and treats a second failure as real.
- **What it costs:** a real flake blocks the merge until someone looks.
- **When to choose differently:** a stall the file names, with its cause, gets its own rule.

### Merging stays the owner's

- **The advice:** the file quotes the owner's word for any merge a session makes alone, and only
  the owner merges changes to the file.
- **The reason:** a pull request can change the file, so the file can't authorize it.
- **What others do, and why:** auto-merge merges once required reviews and checks pass (fact
  `auto-merge`), with no judgment at all.
- **What it costs:** the owner's attention on each change to the rules.
- **When to choose differently:** never for approving. Auto-merge can replace a session's merge
  only where every hold is a required check or the draft state: it waits for nothing else.

### Bots' pull requests

- **The advice:** name who tends Dependabot's and lockfile refreshes' pull requests, and when.
- **The reason:** no session asked for them, so none is any session's work. One sat red for a
  week while sessions merged their own.
- **What others do, and why:** some auto-merge a green update (fact `auto-merge`).
- **What it costs:** a session's time each week.
- **When to choose differently:** auto-merge, where the required checks include the tests.

### A verdict read from the API

- **The advice:** read a commit's checks with `pr_verdict.py`, not by eye.
- **The reason:** printed output changes, a log's last line names one failure of several, and a
  required job that no longer runs looks pending forever.
- **What others do, and why:** auto-merge waits on required checks alone (fact `auto-merge`).
- **What it costs:** a script to keep in step with GitHub's API.
- **When to choose differently:** trusted auto-merge needs no verdict.

## Facts

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `project-skills` | A project skill loads in its repository's sessions, not a project's cloud threads | [Skills](https://code.claude.com/docs/en/skills) | "Sessions in this repository, but not cloud threads in a project" | 2026-11-03 | 2027-05-03 |
| `autofix-events` | Auto-fix follows a pull request's activity, and asks before an ambiguous fix | [Cloud sessions](https://code.claude.com/docs/en/claude-code-on-the-web) | "Claude subscribes to GitHub activity on the PR" and "Claude asks you before acting" | 2026-11-03 | 2027-05-03 |
| `autofix-conflicts` | No event reaches auto-fix when the base branch moves into a conflict | [Cloud sessions](https://code.claude.com/docs/en/claude-code-on-the-web) | "GitHub does not emit a webhook when the base branch advances and creates a merge conflict" | 2026-11-03 | 2027-05-03 |
| `autofix-replies` | Auto-fix's replies post under the user's account, and can trigger comment automation | [Cloud sessions](https://code.claude.com/docs/en/claude-code-on-the-web) | "These replies are posted using your GitHub account" and "Claude can reply on your behalf, which can trigger those workflows" | 2026-11-03 | 2027-05-03 |
| `rerun-window` | A run can be re-run within 30 days, by anyone with write access, on the same commit | [Re-run](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs) | "up to 30 days after its initial run" and "People with write permissions to a repository can re-run workflows" and "the same GITHUB_SHA" | 2026-11-03 | 2027-05-03 |
| `self-approval` | Authors can't approve their own pull requests | [Approving](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews) | "Pull request authors cannot approve their own pull requests." | 2026-11-03 | 2027-05-03 |
| `auto-merge` | Auto-merge merges once required reviews and checks pass | [Auto-merge](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request) | "Auto-merge merges a pull request automatically after all required reviews and status checks pass." | 2026-11-03 | 2027-05-03 |
| `branch-rules` | The rules endpoint gives every active rule on a branch, at any level, without a token on a public repository | [Rules](https://docs.github.com/en/rest/repos/rules) | "All active rules that apply will be returned, regardless of the level at which they are configured" and "can be used without authentication" | 2026-11-24 | 2027-05-24 |
| `run-pages` | A commit's check runs, and its workflow runs, come at most 100 to a page | [Check runs](https://docs.github.com/en/rest/checks/runs), [Workflow runs](https://docs.github.com/en/rest/actions/workflow-runs) | "The number of results per page (max 100)." and "Only returns workflow runs that are associated with the specified head_sha." | 2026-11-24 | 2027-05-24 |
| `job-logs` | A job's log comes by a redirect that expires in a minute | [Workflow jobs](https://docs.github.com/en/rest/actions/workflow-jobs) | "Gets a redirect URL to download a plain text file of logs for a workflow job." and "This link expires after 1 minute." | 2026-11-24 | 2027-05-24 |
| `babysit-never-merges` | A public babysit skill never merges | [babysit-pr-skill](https://raw.githubusercontent.com/LivinTribunal/babysit-pr-skill/main/README.md) | "It never merges." | 2026-11-03 | 2027-05-03 |

## Sources

| Source | Used for | License |
|---|---|---|
| [Claude Code docs](https://code.claude.com/docs/) | Project skills, auto-fix | Anthropic's terms: short quotes, our own words, linked |
| [GitHub Docs](https://docs.github.com/) | Re-runs, auto-merge, approvals, the REST API | CC BY 4.0: quoted, attributed |
| [babysit-pr-skill](https://github.com/LivinTribunal/babysit-pr-skill) | What others do | MIT: pointed to, one short quote |

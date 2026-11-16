# claude-code-skills

The owner's master reference for Claude Code, for Claude skills, and for coding practice in
general: installable skills for setting up, auditing and keeping repositories current, the
checks behind them, and the research they rest on.

Anyone may install, test or improve it. [CONTRIBUTING.md](CONTRIBUTING.md) says what the skills
can and can't do, how to try them on purpose, how to report a problem, and how to send a change.

## Install

In Claude Code:

```text
/plugin marketplace add rmccann-hub/claude-code-skills
/plugin install standards@claude-code-skills
/plugin install engineering@claude-code-skills
```

Before 0.1.1 the marketplace was called `rmccann-skills`. If you added it under that name,
run `/plugin marketplace remove rmccann-skills`, then add it again as above.

In Claude Code's cloud sessions, which don't install a repository's plugins, add the lines in
the latest release's
[`cloud-setup.sh`](https://github.com/rmccann-hub/claude-code-skills/releases/latest/download/cloud-setup.sh)
to the end of the environment's setup script. They install a hook that copies the newest
release's skills into `~/.claude/skills` as each session starts, so no upload is needed. From
0.1.21, the hook installs a release only when its signed attestation names the archive and this
repository's release workflow; it checks the signature itself with `gh` where `gh` is installed,
and refuses a release older than the one it has. An environment set up before 0.1.21 keeps its
older hook until the lines are replaced. Delete any copy of these skills uploaded to claude.ai
first, or it loads beside them under a prefix.

On claude.ai, add this repository as a personal plugin marketplace, turn on Sync
automatically, and install both plugins. The sync reads this repository's `main` branch, not
its releases, so a change reaches the account at the next sync after it merges. That was seen
on 2026-10-26, when `coding` loaded on claude.ai before any release carried it.

## Usage

Once the plugins are installed, Claude Code loads a skill when a request matches what its
description says it's for. The skills are listed below.

To start another repository, attach the latest release's
[`KICKSTART.md`](https://github.com/rmccann-hub/claude-code-skills/releases/latest/download/KICKSTART.md)
to a Claude Code session in that repository, with no message. It reads the repository, asks
only what it can't find out, and stops twice for answers before it changes anything. It also
reads the repository's GitHub settings, and lists each one to change with where it is. The
same release's `ruleset-default-branch.json` and `ruleset-release-tags.json` import under
Settings, Rules, Rulesets, from the New ruleset menu.

To check another repository's prose against the house style, follow the house-style skill's
[`prose-check` module](skills/house-style/references/prose-check.md).

## Skills

| Skill | Plugin | What it does |
|---|---|---|
| `project-bootstrap-and-audit` | `standards` | Sets up a new repository, or audits an existing one, against the PROJECT-BOOTSTRAP-AND-AUDIT standard (v0.49.1) |
| `agent-engineering` | `engineering` | Building, securing and running AI agents: AGENTS.md and CLAUDE.md, settings, hooks and Agent Skills, prompt injection and permissions, and agent sessions reviewing each other's work, closing rounds on evidence and stopping for a person |
| `coding` | `engineering` | The contract every code change meets, then Python, TypeScript and JavaScript, HTML and CSS, C# and .NET, PowerShell, Bash, and C with Meson, plus errors, logging, caching, benchmarking, performance and settings in any language: rules, common mistakes, review checks and the reasons for each, with dated facts |
| `git-workflows` | `engineering` | Commit messages, pull requests and the agents tending them, the merge strategy, conflicts, GitHub Actions CI and deploys, hooks, leaked secrets, `.gitignore`, release tags, versions, changelogs, backports and support windows, with the reasons for each and what other projects do |
| `house-style` | `engineering` | One style for prose and Markdown in every repository, and how to write and keep a project's documentation, with the reasons for each rule, and the Vale style and CI job that check it |
| `testing` | `engineering` | Tests and checks a pass can be trusted from: proving a test, gate or grader can fail, checking results against an independent reference, scoring by the worst case, flaky tests, coverage and doubles, test strategy and test data, metamorphic and differential testing, tests AI agents write, and unattended acceptance runs on hardware with fault injection, with the reasons for each |
| `user-experience` | `engineering` | How a desktop, web or command-line program behaves for its user: each platform's current design language and toolkit, heuristic reviews with severity ratings, status that stays current, windows and dialogs that appear when they should, settings with good defaults and one place each, command-line conventions, GUI tests by machine and with people, and the loop from user reports to safe fixes |
| `visual-design` | `engineering` | How an interface, a chart or a document looks: design tokens built for CSS, charts and documents, dark mode, contrast measured on the shipped color, never color alone, choosing a chart, and charting libraries with their versions and how active each is |
| `architecture` | `engineering` | Where each file and folder goes: layouts by ecosystem, tests' places, feature or layer folders, naming, one repository or several, and moving files without losing history |
| `security` | `engineering` | Threat modeling, authentication, sessions and passwords, authorization, cryptography and randomness, security logging, and security review, against OWASP Top 10:2025, ASVS 5.0.0 and the CWE Top 25 |
| `operations` | `engineering` | Running, troubleshooting and hardening Windows Server and Active Directory, Linux hosts, Docker images and Compose, and office or home networks, and reading their logs and crash dumps, with every change rehearsed or reversible |
| `human-factors` | `engineering` | Before a design, an automation or an optimization removes a step people take: finding what it's for, telling a purpose from a bias or a drift, keeping, changing or overriding it, and keeping facts apart from preferences |
| `optimization-and-scheduling` | `engineering` | Solvers and schedules with the people in them: choosing a solver, modeling rules as constraints, fatigue, fairness and re-planning, lead-time quotes from backlog and capacity, and checking every plan without trusting the solver |

More arrive one at a time, each through the review in
[docs/authoring-a-skill.md](docs/authoring-a-skill.md). [ROADMAP.md](ROADMAP.md) lists every skill
that is planned, with its status.

## Development

You need [uv](https://docs.astral.sh/uv/) 0.13.8 or later, the version CI pins in
`.github/workflows/ci.yml`. It installs the Python version named in `.python-version`. You also
need Node.js, to run Claude Code's own catalog validator.

```sh
uv sync --locked
uv run pytest
uv run ruff check
uv run ruff format --check
uv run skillcheck .
npm ci
npx --no-install claude plugin validate --strict .
```

The prose check runs [Vale](https://vale.sh) with the house-style skill's own style, from its
source here. Install Vale at the version `.github/workflows/prose.yml` names, then:

```sh
vale sync
git ls-files -z '*.md' | xargs -0 vale
```

Each skill's dated facts carry their source and a date to check them again by.
`uv run skillcheck --due` lists the facts that are due, and `uv run skillcheck --verify` looks
for each quote at its source, over the network. The Freshness workflow runs both every Monday,
with the dependency map's check below, and keeps one issue open while anything is due.

Every dependency stays on its newest release. `uv run skillcheck --outdated` measures each one
against its registry: the packages in the lockfiles, the GitHub Actions, the tool and runtime
versions the workflows name, `.python-version`, and the ranges in `pyproject.toml`. A release
counts once it has been out three days, the wait Dependabot also keeps. The Freshness workflow
runs it every Monday too, in an issue of its own. Give it another repository's path to check
that one.

[docs/dependencies.md](docs/dependencies.md) maps what the repository is built from, runs on
and relies on: its languages, runtimes, tools, packages at their exact versions, GitHub Actions,
services, and the sources its facts cite. [bom.json](bom.json) holds the same map in CycloneDX
1.7, for other tools to read. `uv run skillcheck --bom` writes both, and
`uv run skillcheck --bom-check` names one that no longer matches. CI runs that check on every
pull request, so a Dependabot update fails it until a session regenerates the map in its branch.
The Freshness and Release workflows run it too.

Parity runs check how the skill behaves on sample repositories, before and after a change.
[docs/testing-the-skill.md](docs/testing-the-skill.md) says how to run one.

## Contributing

Report a problem as an issue, or a security problem through the Security tab. Send a change as
a pull request from a fork, after running the checks above; the owner reviews and merges each
one. [CONTRIBUTING.md](CONTRIBUTING.md) has the detail, including the rules CI checks and the
ones nothing checks.

## Releasing

1. In the pull request, set the new version in every catalog entry, and add its section to
   `CHANGELOG.md`. Its merge is what reaches Claude Code plugin installs, which take `main` once
   the version changes; the release that follows reaches cloud sessions with the hook.
2. Once it merges and CI passes on `main`, run the Release workflow from the Actions tab, with
   the version and the merge commit's full SHA.
3. After each release of the standard, and at least every three months, a session re-checks
   this repository against the standard, with the newest release's kickstart file, and sends
   the owner its report (the owner, 2026-11-16). What it raises waits for the owner's
   answers, as in any other run, and the release doesn't wait for it.

## Operations

To take a skill that gives wrong or harmful instructions out of circulation, follow
[docs/withdrawing-a-skill.md](docs/withdrawing-a-skill.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

Apache-2.0; see [LICENSE](LICENSE). The standard keeps its own CC0-1.0 dedication, stated in its
file.

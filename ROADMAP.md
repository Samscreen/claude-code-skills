# Roadmap

What this repository ships and what comes next: a few skills, each made of modules.
`skillcheck` keeps the skills table in step with `skills/`, the README and the catalog, so it
can't drift: a skill that ships without a `shipped` row here, or a `shipped` row with no skill
behind it, fails CI.

- **Status** (closed set): `shipped`, `building`, `researching`, `planned`.
- **Coverage:** `core` is the owner's stack, covered deepest and built first. `standard` gets
  full coverage. `on request` is named now and built when a repository needs it.
- **Research:** the prompts in `research/prompts/` whose results the module is built from,
  then any follow-up prompts still to run. A prompt with no result in `research/runs/`, such
  as R01b or R13, hasn't been run yet, so a shipped module that cites one waits on it for more.

The PROJECT-BOOTSTRAP-AND-AUDIT standard covers configuration and process, and says it doesn't
judge code. The other skills cover the code and the work itself, beside the standard rather
than inside it.

Each module says why, not only what: it gives each rule's reasons, what other projects do and
why, what each choice costs, and when to choose differently. Its dated facts, including what
other projects do, are checked again by `skillcheck --due` and `skillcheck --verify`, which the
weekly freshness workflow runs, with `skillcheck --outdated` for every dependency.
`keeping-current` is the module that will do the same for other repositories, starting from
`--outdated`, which already runs on any repository's path.

## How skills are structured

The owner asked on 2026-10-16 for the functionality, efficient and effective, divided however
works best, and for a structure that can be divided again without a mystery or a round of
research. These rules are that structure.

1. **A skill is a trigger.** There is one skill for each kind of situation in which Claude
   should load guidance, and everything needed in that situation is a module of that skill.
   Every installed skill's description is in context all the time: Claude Code gives the
   listing 1% of the context window, and past that descriptions are dropped (fact `sb-listing`,
   checked 2026-11-11). At four characters a token, as `skillcheck` counts, that's 8,000
   characters on a 200,000-token model. A module costs nothing until it's read. So coverage grows by
   modules, and the skill count stays small.
2. **A module is the unit of content.** It is one file, `skills/<skill>/references/<module>.md`,
   whose name is unique across the repository and never changes, because research, facts and
   lessons are keyed to it. It holds everything it needs: scope, rules, mistakes, audit checks,
   why, dated facts and sources. It names other modules but never links into them. Its trigger
   tests, the requests that must reach it, sit beside it in `tests/fixtures/modules/`.
3. **`SKILL.md` routes.** It holds what applies to every module of the skill, such as the
   contract every code change meets, and a table that says which module to read for which
   request.
4. **The trigger tests decide the boundaries.**
   - A module spins off into a skill of its own when its requests often need it alone and its
     skill's description can't name it in 250 characters, or when the router picks it wrongly.
   - Two skills merge when their tests always fire together.
   - A module moves when its requests land in the other skill.
5. **A move is a command, not a project.** `skillcheck --move <module> <skill>` moves the file
   and its tests, fixes both routers and records the move in
   [docs/module-moves.md](docs/module-moves.md). The trigger tests then show that
   every module's requests still reach it. Skill renames and removals go in the same record,
   from which the old copies to delete on claude.ai, and what depends on them, are listed.
6. **Names:** a skill keeps its name unless the name misleads. Module names never change.
7. **Plugins group by audience and license, not by topic:** `standards` holds the standard,
   under CC0; `engineering` holds what colleagues install; `personal` holds the owner's own.

## Skills

| Skill | Plugin | Loads when | Status |
|---|---|---|---|
| `project-bootstrap-and-audit` | `standards` | Setting up, retrofitting, auditing or re-checking a repository against the standard, v0.51.0 | shipped |
| `git-workflows` | `engineering` | Commits, branches, pull requests, CI, hooks, tags, changelogs and releases | shipped |
| `house-style` | `engineering` | Writing prose, Markdown, READMEs and documentation | shipped |
| `coding` | `engineering` | Writing, reviewing or fixing code in any language: the contract every change meets, then the language and the practice at hand | shipped |
| `testing` | `engineering` | Writing, reviewing or fixing tests, and choosing a test strategy | shipped |
| `architecture` | `engineering` | Laying out a repository: where each file and folder goes (planned: designing systems, APIs and plans, and modernizing old code) | shipped |
| `data` | `engineering` | SQL, schemas, migrations, indexes and transactions | planned |
| `security` | `engineering` | Threat models, authentication, authorization and cryptography (planned: dependencies and the supply chain, privacy and licenses) | shipped |
| `agent-engineering` | `engineering` | Building skills and agent context files, agents reviewing each other, and defending agents against injection | shipped |
| `operations` | `engineering` | Running, troubleshooting or hardening Windows Server, Linux, containers and networks, and reading their logs and crash dumps (planned: cloud) | shipped |
| `business-apps` | `engineering` | Automating or extending Excel, Word, Epicor Kinetic and SOLIDWORKS | planned |
| `visual-design` | `engineering` | Themes, palettes, contrast and charts (planned: accessibility) | shipped |
| `user-experience` | `engineering` | Reviewing, designing or testing how a program behaves for the person using it: status and feedback, windows and dialogs, settings and options, and whether it's easy to learn and to use | shipped |
| `optimization-and-scheduling` | `engineering` | Solvers, schedules and plans, with the people in them | shipped |
| `human-factors` | `engineering` | Designing or changing what people do: the habits that look wasteful and serve a purpose. It never bends a factual finding | shipped |
| `linux-gaming` | `personal` | Proton, Steam and handheld PCs | planned |

## Modules

Grouped by subject; the Skill column is each module's one home.

### A. How the work is done

| Module | Skill | Covers | Status | Coverage | Research |
|---|---|---|---|---|---|
| `keeping-current` | `project-bootstrap-and-audit` | Sweep a repository for versions behind, end-of-life dates, deprecated APIs and stale facts; propose the updates | planned | core | R05, R21, R24, R21b |
| `skill-builder` | `agent-engineering` | Design, write, test and tune a skill | shipped | core | done |
| `agent-context-files` | `agent-engineering` | AGENTS.md, CLAUDE.md, rules, settings, hooks, subagents, MCP, other agents' files | shipped | core | R01, R01b |
| `review-loops` | `agent-engineering` | Agent sessions in two repositories reviewing each other's work: the few rules that end rounds, the ones that cost more than they caught, and where agents have to stop for a person | shipped | core | R26, R01b |

### B. Engineering practice, for every language

| Module | Skill | Covers | Status | Coverage | Research |
|---|---|---|---|---|---|
| `repo-structure` | `architecture` | Layouts by project type, where each file goes, naming files and folders | shipped | core | R02, R02b |
| `writing-style` | `house-style` | What prose says: voice, claims and their evidence, instructions for a reader who isn't a programmer, words to cut, American spelling, dates and records | shipped | core | R02, R02b |
| `markdown-format` | `house-style` | How Markdown is laid out: headings, wrapping, lists, code blocks, tables, links, file names, a README's sections | shipped | core | R02, R02b |
| `prose-check` | `house-style` | The Vale check: the HouseStyle package, `.vale.ini`, the CI job with its canary, a repository's vocabulary, files left alone | shipped | core | R02, R02b |
| `documentation` | `house-style` | Docs sites, diagrams, file size and splitting, beyond the README sections `markdown-format` covers and the records and prose `writing-style` covers | shipped | core | R02, R02b |
| `code-style` | `coding` | Naming, formatting, structure, comments and docstrings | shipped | core | R03, R03b |
| `types` | `coding` | Static and gradual typing, strictness, type checkers, types at trust boundaries | shipped | core | R03, R03b |
| `input-handling` | `coding` | Validation, sanitization and output encoding by context | shipped | core | R04, R04b |
| `secure-coding` | `security` | OWASP Top 10, ASVS, CWE Top 25, authentication, cryptography, threat modeling | shipped | core | R04, R04b |
| `supply-chain-security` | `security` | Dependencies, lockfiles, pinning, SBOMs, provenance, malicious and hallucinated packages | planned | core | R05, R21, R24, R21b |
| `ai-agent-security` | `agent-engineering` | Prompt injection, permission design, secret exposure, MCP, skills as a supply chain, hidden Unicode | shipped | core | R01, R01b |
| `error-handling` | `coding` | Failure classes, retries, timeouts, circuit breakers, causes per language, bulkheads | shipped | core | R07, R07b, R07d |
| `error-responses` | `coding` | Errors that reach a person or a client: RFC 9457 problem details and each framework's defaults, honest status codes, and messages that say what happened and what to do | shipped | core | R07, R07d, R07f |
| `testing-patterns` | `testing` | Test doubles and contract tests, coverage, each framework's settings that fail open, frameworks per language, property-based and mutation tools | shipped | core | R06, R06b |
| `agent-written-tests` | `testing` | Tests an AI coding agent writes, changes or runs: tests first, high-risk test diffs, gaming, holdout tests, mutation-testing what it wrote | shipped | core | R06b |
| `acceptance-runs` | `testing` | Unattended acceptance runs on hardware: preconditions, a device lost mid-run, run tiers, evidence; fault injection for ordinary programs | shipped | core | R06c |
| `test-gates` | `testing` | Proving a test, gate, checker or grader can fail: the parent commit, a planted defect, the couldn't-check path, mutating the checker | shipped | core | R06 |
| `test-oracles` | `testing` | What a result is checked against: independent references, recorded samples, baselines, scoring by the worst case | shipped | core | R06 |
| `flaky-tests` | `testing` | A test that passes and fails on the same code: the cause, races in the program, quarantine, keeping a fix | shipped | core | R06 |
| `test-strategy` | `testing` | The mix of tests by size and scope, a command-line program's tests, test data and factories, what no test covers, skipped tests, metamorphic and differential testing | shipped | core | R06c |
| `api-patterns` | `architecture` | REST, OpenAPI, GraphQL, gRPC, auth flows, pagination, versioning, webhooks | planned | core | R19 |
| `sql-craftsman` | `data` | Schema design, migrations, SQL style, indexing, transactions | planned | core | R14 |
| `commits-and-pull-requests` | `git-workflows` | Commit grammar and messages, trailers, the author's address, branch names, pull requests and review comments | shipped | core | R08, R08b |
| `branches-and-merging` | `git-workflows` | Branching models, protecting the default branch, merge strategies | shipped | core | R08, R08b |
| `rebasing-and-recovery` | `git-workflows` | Deleting branches, rebasing, conflicts, recovering lost commits, and reading Git's output | shipped | core | R08, R08b |
| `ci-workflows` | `git-workflows` | GitHub Actions triggers, timeouts, installs, required checks, proving a gate works | shipped | core | R08, R21, R08b, R21b |
| `ci-speed` | `git-workflows` | How long CI takes, where suites run, caching builds, and slow tests | shipped | core | R08, R21, R08b, R21b |
| `pr-stewardship` | `git-workflows` | A repository's own steward skill: how its sessions drive pull requests, when to merge or hold, re-running a stalled job, what an owner's hold covers, and auditing it | shipped | core | R08, R08b |
| `actions-security` | `git-workflows` | Workflow permissions, untrusted input, `pull_request_target`, scanning workflows | shipped | core | R08, R08b |
| `action-pinning` | `git-workflows` | SHA-pinned actions, lockfiles, the pinning policy, Dependabot for actions, Node 20 actions | shipped | core | R08, R08b |
| `git-hooks` | `git-workflows` | Writing, installing and testing hooks, and where CI is the gate instead | shipped | core | R08, R08b |
| `releases-and-versions` | `git-workflows` | Release tags and workflows, changelog entries, version numbers, release lines and backports; deprecation timelines are `versioning-and-releases`' | shipped | core | R05, R24, R21b |
| `leaked-data` | `git-workflows` | A secret or personal information in a commit: rotating, and rewriting history at the owner's request | shipped | core | R08, R08b |
| `gitignore` | `git-workflows` | `.gitignore` rules, secret files, lockfiles, untracking a file | shipped | core | R08, R08b |
| `ci-cd` | `git-workflows` | Environments and deployment, beyond the CI that `ci-workflows` and `ci-speed` cover | shipped | core | R08, R21, R08b, R21b |
| `versioning-and-releases` | `git-workflows` | Release notes, support windows, advisories and deprecation timelines, beyond the tags, changelogs and versions that `releases-and-versions` covers | shipped | core | R05, R24, R21b |
| `legacy-modernization` | `architecture` | Reading legacy code, characterization tests, the strangler fig pattern, migration playbooks | planned | core | R17 |
| `logging-and-observability` | `coding` | Structured logs, OpenTelemetry, metrics, tracing, what never to log | shipped | standard | R07, R07b, R07d |
| `logging-libraries` | `coding` | Logging libraries per language: versions, trace IDs, redaction and OpenTelemetry severity | shipped | standard | R07b, R07d, R07f |
| `performance-and-concurrency` | `coding` | Profiling, flame graphs, data structures, async and threads | shipped | standard | R07, R07c, R07e |
| `caching` | `coding` | In-process and shared caches: expiry and invalidation, stampedes, negative caching, bounds, and cache libraries per language | shipped | standard | R07e, R07f |
| `benchmarking` | `coding` | Benchmark harnesses and their pitfalls, comparing runs with statistics, and catching regressions in CI | shipped | standard | R07c, R07e, R07f |
| `configuration` | `coding` | Layered config, environment variables, validation at startup, secret stores | shipped | standard | R04, R04b |
| `architecture-and-design` | `architecture` | Principles, boundaries, decision records, diagrams, planning, refactoring | planned | standard | R19 |
| `human-factors` | `human-factors` | The habits, notions and mindsets common to people that look odd or wasteful from outside but serve a purpose: what each is for, how to spot one before a design, an automation or an optimization removes it, and how to design with it. Loaded only by the few agents that design or change what people do; it never bends a factual finding | shipped | standard | R23, R23b, R23c |
| `studying-work` | `human-factors` | Finding what a step is for: watching and interviewing people at their work, goals and plans, how deep to go, and the traps that bend a study | shipped | standard | R23b, R23c, R23d |
| `cognitive-task-analysis` | `human-factors` | Finding the judgment and cues behind expert work: the Critical Decision Method, ACTA, what each produces and costs, and when it beats task analysis or a visit | shipped | standard | R23c, R23d |
| `usability-review` | `user-experience` | A heuristic review of a program's interface: status that's current, consistency, error prevention and recovery, recognition over recall, severity ratings | shipped | standard | R27, R27b |
| `windows-and-dialogs` | `user-experience` | When a window or dialog appears, modality, focus and stacking, nothing shown before it's ready or hidden behind another, long operations and notifications | shipped | standard | R27, R27b |
| `settings-and-options` | `user-experience` | Defaults, presets, progressive disclosure, each setting in one place, and how many choices is too many | shipped | standard | R27, R27b |
| `gui-testing` | `user-experience` | Testing a GUI by machine, through accessibility interfaces and toolkit helpers, and with people, by task-based tests | shipped | standard | R27, R27b |
| `interface-patterns` | `user-experience` | What a current interface is built from on each platform: design languages, stock components, one component per pattern, layout and window sizes, dense screens, forms, and loading, empty and failed states | shipped | standard | R29, R29b |
| `command-line-interfaces` | `user-experience` | Command-line programs for people and scripts: option syntax and help, output for people against scripts, color, prompts, dry runs, secrets off flags, and argument parsers; exit codes are `error-handling`'s | shipped | standard | R29, R29b |
| `feedback-loop` | `user-experience` | From user issues to fixes: feedback in the product, crash reports and consented usage data, triage, interfaces built to change, visual regression tests | shipped | standard | R30, R30b |
| `accessibility` | `visual-design` | WCAG 2.2, ARIA, contrast, testing tools | planned | standard | R18 |
| `internationalization` | `coding` | Unicode, locales, time zones, formats, right-to-left text | planned | standard | R18 |
| `privacy-and-compliance` | `security` | Personal data, retention, licenses and notices, obligations on software publishers | planned | standard | R18 |

### C. Languages in current use

| Module | Skill | Covers | Status | Coverage | Research |
|---|---|---|---|---|---|
| `python-coding` | `coding` | Python 3, its toolchain and idioms | shipped | core | R09, R09b |
| `python-security` | `coding` | Python's untrusted-input calls: shells, `eval`, deserialization, SQL, archives, paths, tokens | shipped | core | R09, R09b |
| `javascript-coding` | `coding` | TypeScript, JavaScript, Node.js | shipped | core | R10, R10b |
| `javascript-security` | `coding` | Node.js input handling: shells, `eval`, prototype pollution, paths, ReDoS, SQL | shipped | core | R10, R10b |
| `html-coding` | `coding` | HTML, CSS, accessibility basics, forms | shipped | core | R10, R10b |
| `web-security` | `coding` | Browser-side security: output encoding, sanitizing, Trusted Types, CSP, SRI, `noopener` | shipped | core | R10, R10b |
| `csharp-coding` | `coding` | C# and .NET | shipped | core | R11, R11b |
| `csharp-security` | `coding` | C# deserialization, SQL, processes, batch files, paths, DLL search paths, analyzers | shipped | core | R11, R11b |
| `powershell-scripts` | `coding` | PowerShell 7 and Windows PowerShell 5.1 | shipped | core | R11, R11b |
| `powershell-security` | `coding` | PowerShell credentials, `Invoke-Expression`, batch-file arguments, execution policy, signing | shipped | core | R11, R11b |
| `bash-coding` | `coding` | Bash and POSIX sh | shipped | core | R15 |
| `bash-security` | `coding` | Bash and POSIX sh: guarded deletes, `eval`, arithmetic on input, secrets, input checks | shipped | core | R15 |
| `c-coding` | `coding` | C: standards and compilers, undefined behavior, ownership, bounds, checked I/O, porting | shipped | core | R12, R12b |
| `c-build` | `coding` | C built with Meson: options, the warning gate, hardening, sanitizers, analyzers, fuzzing | shipped | core | R12, R12b |
| `c-security` | `coding` | C handling outside data: strings and buffers, format strings, overflow, paths, processes, output | shipped | core | R12, R12b |
| `vba-coding` | `coding` | VBA in Office applications | planned | core | R16 |
| `go-coding` | `coding` | Go | planned | standard | R25 |
| `rust-coding` | `coding` | Rust | planned | standard | R25 |
| `cpp-coding` | `coding` | C++ | planned | standard | R25 |
| `java-coding` | `coding` | Java | planned | standard | R13 |
| `kotlin-coding` | `coding` | Kotlin | planned | standard | R13 |
| `php-coding` | `coding` | PHP | planned | standard | R13 |
| `ruby-coding` | `coding` | Ruby | planned | standard | R13 |
| `config-formats` | `coding` | YAML, JSON, TOML, XML | shipped | standard | R15 |

### D. Languages from the past: read, maintain, modernize

| Module | Skill | Covers | Status | Coverage | Research |
|---|---|---|---|---|---|
| `legacy-languages` | `coding` | One reference per language, for example VB6, VBScript, classic ASP, .NET Framework, COBOL and Python 2 | planned | core | R17 |

### E. Platforms and domains

| Module | Skill | Covers | Status | Coverage | Research |
|---|---|---|---|---|---|
| `windows-admin` | `operations` | AD, Group Policy, DNS/DHCP, certificates, file services, updates, hardening | shipped | core | R11, R11b |
| `excel-master` | `business-apps` | Workbooks from code, formulas, Power Query, DAX, Office Scripts, add-ins | planned | core | R16 |
| `word-documents` | `business-apps` | Generating and filling Word templates | planned | core | R16 |
| `epicor-kinetic` | `business-apps` | BPM, BAQ, REST API v2, Functions, from public knowledge only | planned | core | R16 |
| `solidworks-automation` | `business-apps` | VBA and C# macros, documents, drawings, sheet metal, exports | planned | core | R16 |
| `linux` | `operations` | Administration and troubleshooting across distributions | shipped | standard | R15 |
| `networking-security` | `operations` | Firewalls, segmentation, IDS, VPN, Wi-Fi, DNS | shipped | standard | R15 |
| `docker-containers` | `operations` | Dockerfiles, Compose, hardening, registries | shipped | standard | R15 |
| `log-analysis` | `operations` | Event logs, crash dumps, journals, application logs | shipped | standard | R07 |
| `optimization-and-scheduling` | `optimization-and-scheduling` | Solvers, business rules as constraints, the human factors in plans, with `human-factors` | shipped | standard | R28, R23, R28b, R28c |
| `plan-checking` | `optimization-and-scheduling` | Checking what a solver returns and testing a planner: an independent checker, runs stopped at a limit, reproducible runs, published instances as oracles | shipped | standard | R28, R28b, R28c, R23d |
| `rosters-and-replanning` | `optimization-and-scheduling` | Rosters and plans people work to: fairness across people, skills and cross-training, worker-dependent setups, objective weights, and re-planning without churn | shipped | standard | R28c, R23d |
| `linux-gaming` | `linux-gaming` | Proton, Steam, handhelds | planned | on request | R15 |
| `kubernetes` | `operations` | Clusters, workloads, the Gateway API | planned | on request | R15 |
| `cloud` | `operations` | Azure, AWS and Google Cloud baselines | planned | on request | R15 |
| `infrastructure-as-code` | `operations` | Terraform, OpenTofu, Bicep | planned | on request | R15 |

### F. Output and presentation

| Module | Skill | Covers | Status | Coverage | Research |
|---|---|---|---|---|---|
| `visual-theme` | `visual-design` | Design tokens, palettes, typography, dark mode | shipped | standard | R20, R20b |
| `data-visualization` | `visual-design` | Choosing charts, accessible charts, charting libraries | shipped | standard | R20, R20b |

## Rebuilding the owner's older skills

The owner's account holds 34 skills of their own, older than this repository. 28 are rebuilt
here as modules of the skills above, 3 are already replaced (`git-workflows`,
`project-bootstrap-and-audit`, and `markdown-standards` by `house-style`), and 3 retire into
shared tools (`skill-orchestrator`, `skill-stress-tester`, `code-planner`). Nothing is copied:
none of their examples has ever been run, none of their facts has a source, and five hold
company detail. The owner approved rebuilding them in answers 44 to 49 of 2026-10-15, and on
2026-10-16 left their division to this repository.

| Old skill | Its new home |
|---|---|
| `code-standards` | `coding`'s `SKILL.md` (the contract), then `code-style`, `input-handling`, `configuration`, `error-handling` and `architecture-and-design` |
| `python-coding`, `javascript-coding`, `html-coding`, `csharp-coding`, `powershell-scripts`, `bash-coding`, `vba-coding`, `go-coding`, `rust-coding`, `php-coding`, `ruby-coding` | `coding`, one module each, under the same names |
| `error-handling` | `coding`'s `error-handling` |
| `testing-patterns` | `testing` |
| `api-patterns` | `architecture`'s `api-patterns`; its Epicor material goes to `epicor-kinetic` |
| `sql-craftsman` | `data`; its Epicor material goes to `epicor-kinetic` |
| `windows-admin`, `docker-containers`, `networking-security` | `operations`, one module each |
| `linux-troubleshooting` | `operations`' `linux`; its gaming material goes to `linux-gaming` |
| `log-parser` | `operations`' `log-analysis`; its Proton material goes to `linux-gaming` |
| `excel-master` | `business-apps`; its charts and colors go to `visual-design` |
| `epicor-bpm` | `business-apps`' `epicor-kinetic`, with the company's detail in the private companion |
| `solidworks-automation` | `business-apps` |
| `procedure-generator` | `business-apps`' `word-documents`, with the company template in the private companion |
| `my-theme` | `visual-design`'s `visual-theme`, with the company palette in the private companion |
| `human-factor-audit` | `human-factors` and `optimization-and-scheduling` |
| `linux-gaming` | `linux-gaming` |

Each topic the old skills held twice gets one home: boot and Secure Boot in `linux`, Steam and
Proton in `linux-gaming`; the PowerShell 7 against 5.1 rules in `powershell-scripts`, which
`windows-admin` cites; client deployment by Group Policy in `windows-admin`; and chart choice and
palettes in `visual-design`, not in `excel-master`.

1. **Shared tools first, each its own pull request:**
   - the intake, filed as a dated research result with company detail and repository names
     taken out, listing for each old skill what its successor must cover, its lessons, and its
     defects not to repeat. Wave 1's was filed on 2026-10-26, in
     [research/runs/2026-10-26-intake-wave-1.md](research/runs/2026-10-26-intake-wave-1.md);
   - the module template, and `skillcheck` checks for modules: unique names, one home each,
     the template's sections, and facts read from inside each module, with `git-workflows` and
     `house-style` converted to modules. Shipped 2026-10-16;
   - a listing budget for about 20 skills, in place of room for 100. Shipped 2026-10-16;
   - an example checker in CI that runs each language's own tool on every code block. Shipped
     2026-10-21 as `skillcheck --examples`;
   - one trigger-test runner, which checks in Claude Code that a request reached the right skill
     and that the skill read the right module; on claude.ai the owner tries the same requests
     by hand, from a list the session gives them. Shipped 2026-10-21 as `skillcheck --triggers`
     and `--tries`. Its first run, on `gitignore`, found none of its four requests loading
     `git-workflows`, so the descriptions were to be tuned against it before the rebuilds.
     Closed on 2026-11-16 by the owner's answer: the trigger runs each module's review makes
     since then do this tuning;
   - `skillcheck --move` and its record of moves, renames and removals. Shipped 2026-10-16;
   - `skill-builder`, from `skill-creator`'s method under its license, and the stress tester's
     two good checks: content safety, and compiling every code block. Shipped 2026-11-11 as
     `agent-engineering`'s module.

   The pairing map (answer 33 of 2026-10-13) shrinks to the pairs between skills, such as
   `coding` with `testing`, which each router names; pairs within a skill are its router's
   table.
2. **Research, in waves:** the owner runs each wave's prompts, and each result is checked
   against its sources before it's used.
3. **Rebuilds, one pull request per skill and wave:**

   | Wave | Research | Skills and modules | Old copies deleted when it ships | Status |
   |---|---|---|---|---|
   | 1 | R15, R09, R11, R10 | `coding` with its contract, `bash-coding`, `python-coding`, `powershell-scripts`, `csharp-coding`, `javascript-coding`, `html-coding` | the six old language skills | Shipped 2026-10-26 in release 0.1.22. The six old copies are deleted |
   | 2 | R06, R06b, R07, R14, R19, R23, R28 | `testing`; `coding`'s `error-handling`; `operations`' `log-analysis`; `data`; `architecture`'s `api-patterns`; `human-factors`; `optimization-and-scheduling` | `testing-patterns`, `error-handling`, `log-parser`, `sql-craftsman`, `api-patterns`, `human-factor-audit` | Shipped 2026-11-11, except `data` and `api-patterns`, still planned. Deleted: `testing-patterns`, `error-handling`, `log-parser` and `human-factor-audit`. `sql-craftsman` and `api-patterns` wait for their successors |
   | 3 | R16, R11 | `coding`'s `vba-coding`; `business-apps`; `operations`' `windows-admin` | `vba-coding`, `excel-master`, `epicor-bpm`, `solidworks-automation`, `procedure-generator`, `windows-admin` | `windows-admin` shipped early, on 2026-11-11, and its old copy is deleted. The rest is planned |
   | 4 | R25, R13, R15, R20 | `coding`'s `go-coding`, `rust-coding`, `php-coding`, `ruby-coding`; `operations`' `docker-containers`, `linux`, `networking-security`; `visual-design` | those seven, `linux-troubleshooting`, `my-theme` once the company palette is in the private companion, and last `code-standards` | Shipped early: `docker-containers`, `linux` and `networking-security` on 2026-11-11, and `visual-design` on 2026-11-16. Deleted: `docker-containers` and `networking-security`. No deletion of `linux-troubleshooting` is recorded, and `my-theme` stays. The four language modules are planned |
   | When needed | R15 | `linux-gaming` | `linux-gaming` | Planned |

   The Status column is as of 2026-11-16, with each deletion as `docs/decisions.md` records it
   (2026-10-26 and 2026-11-11).

   Each rebuild takes the old skill's topics from the intake, writes from primary sources with
   dated facts, makes every example pass the checker, and gets a fresh review and its trigger
   tests. Before it merges, the owner deletes the old copies the table names from claude.ai, in
   their own settings and in the organization library's inventory, because the merge reaches
   chat through the plugins' sync of `main` (2026-10-26). The owner's claude.ai tries follow
   the merge, and the release then reaches cloud sessions through the release's hook. `code-standards` goes last because the old
   language skills, `docker-containers` and `networking-security` say they must read it first.

4. **Colleagues:** as of 2026-10-16, the organization's library installed all 28 of the
   owner's old skills then on claude.ai for everyone in the organization, where colleagues use
   claude.ai and Claude Code. Since then the owner has deleted 13 old copies as their
   successors shipped, on 2026-10-26 and 2026-11-11 (`docs/decisions.md`), so fewer remain.
   The waves table names them. Deleting an old copy takes it from colleagues too. The owner
   chose to keep deleting each old copy as its successor ships, and to have colleagues add
   this repository's plugins themselves (2026-10-16).

**What the owner decided:**
- **Examples CI can't run** (VBA, SOLIDWORKS, Epicor, Power Query, DAX): CI checks what it can
  parse, the owner runs each once, and the skill records the version and date it was proven on
  (44).
- **`my-theme`'s palette is the owner's employer's,** so it stays on the account, and
  `visual-theme` publishes no palette from it (46).
- **PowerPoint and PDF** are left to Anthropic's `pptx` and `pdf` skills, unless a repository
  needs to generate them (47).
- **Old copies with known dangerous examples** stay on until their successors ship (48).
- **Every skill works in Claude Code first and on claude.ai too,** with extra effort where it
  takes some. Descriptions are capped at 250 characters (2026-10-15). The room for 100 skills
  decided then is replaced by about 20 skills with modules (2026-10-16), and the listing budget
  follows in the shared tools.
- **The Claude Code exclusion list:** a file in this repository names the skills, Anthropic's
  and the owner's, that load on claude.ai but not in Claude Code. The bootstrap skill writes
  it into each repository's `.claude/settings.json` as `skillOverrides`, which Claude Code
  applies to synced skills, tested here on 2026-10-15. It starts with `procedure-generator`,
  `markdown-standards`, the three retired skills, and Anthropic's skills the owner doesn't use in repositories. Its
  bootstrap step is a change to the standard, proposed on its own (2026-10-15).
- **Anthropic's skills:** `docx`, `xlsx`, `pptx` and `pdf` stay on. `skill-creator` stays as a
  reference, on in this repository only, unless `skill-builder` replaces it (2026-10-15).
- **Company material,** such as the company theme, template and the Epicor and SOLIDWORKS
  detail, goes in a private companion repository with the same tools and checks, not here
  (2026-10-15). It was set up on 2026-10-16, running this repository's checks at a pinned
  release. Its four planned company skills become modules of one company skill, by the rules
  above, in a change of its own there.

## Lessons waiting for their module

What live repositories taught that belongs to a module not built yet, or to a shipped module
that hasn't taken it in, marked "waiting, module shipped". Each module takes its lessons in
when it's built, and its reasons cite them. A lesson taken in moves to the archive, where its
number still resolves: the 52 of L1 to L57 taken in by 2026-11-16 are on the `archive`
branch at `archive:2026-11-16/roadmap-lessons-taken-in.md`.

- **L21, `api-patterns`:** a contract derived from format strings can't see a change of meaning.
  An error count began to include encoder failures, and the contract diff showed one row of
  303. A contract records every argument as used, declined with a reason, or not yet examined.
- **L22, `api-patterns`:** when a provider rewords a line its consumer parses, the consumer's
  release that reads both wordings ships first.
- **L33, `api-patterns`:** between two tools, the consumer takes a value only from output that
  carries it, knows every name the producer may give a file, names the light mode where the
  default action is heavy, sends an optional flag only to builds that declare it, and ships
  the parser for a new output shape before the producer changes the shape. One runner took a
  build tag from a refusal's message, and probe steps that named no mode fell through into
  the tool's heavy default action.
- **L34, `api-patterns`:** where two sides validate the same value, they agree one rule on the
  same raw bytes, the stricter side's, and a property test runs one side's code against a port
  of the other's. A looser rule would have passed a code the other side's own report flagged.
- **L51, `supply-chain-security`:** a build from source is pinned by the full commit SHA, the
  commit it landed on is compared with that SHA, and a dirty tree stops the build. One app
  built a dependency at a 7-character prefix, never compared the full commit, and only warned
  on a dirty tree. An update is verified by provenance, not by a checksum published beside it,
  which anyone who can replace the file can replace too, and a downgrade is refused.

## Rebuilding `project-bootstrap-and-audit`

The standard stops being one separate document. Its content becomes the skill's own parts, one
piece at a time. Each piece moves its sections out of the standard file in the same commit, and
is checked against the version before it by parity runs
([docs/testing-the-skill.md](docs/testing-the-skill.md)). The decision is in
[docs/decisions.md](docs/decisions.md).

What it becomes:

- **`SKILL.md`:** the procedure. That's the jobs, the phases, the two stops and the report.
- **`references/`:** one topic each:
  - standing rules, vocabularies, the environment, facts and the self-check;
  - the phases, and one file per dimension;
  - new projects and the starter files;
  - the configuration file map, file governance, the release gate and cross-repository
    contracts;
  - `other-tools.md`, which says how to use the skill with other AIs and lists each Claude
    Code-only feature with what it does.
- **`assets/`:** the starter files as tested templates, and the run report's skeleton and schema.
- **`scripts/`:** the mechanical checks, in Python with the standard library only.

Rules for the rebuild:

- Nothing is lost: each piece's pull request lists every rule it moved and where it went.
- A reference never links to another reference.
- No rule lives in two places.
- Frontmatter uses only the Agent Skills fields.
- A Claude Code-only feature is marked where it's used.

Findings F1 to F167 on the standard, each applied by v0.49.1 apart from F165, are on the
`archive` branch at `archive:2026-11-16/roadmap-standard-findings.md`, with the runs that
found them. The pieces table below names the findings each piece places.

Live runs on the owner's repositories come between pieces. Each report is triaged as
[docs/testing-the-skill.md](docs/testing-the-skill.md) describes, and what it finds is fixed
before the next repository's run.

One finding is still open, from the two audits of 2026-10-27:

- **F165, planned:** an audit reads *Before you start*, *The run*, *File governance* and, with a
  second repository, *Cross-repository contracts*: about 3,600 of v0.48.2's 6,534 lines, while
  adherence may decay as a session lengthens. *The run* is split by dimension, so a run reads
  the dimension it's rating, or each dimension opens with a short checklist naming each rule's
  line. It's a restructure of its own, beside R22's work on the routing table, and the rebuild's
  one file per dimension, above, is where it lands.

Applied since the archive was cut:

- **F168, in v0.49.2:** *Language toolchains* says PowerShell 7.4 and 7.5 and .NET 8 and 9
  ended on 2026-11-10, and names .NET 11 as an STS beside 10, the LTS; approved 2026-11-16.
- **F169, in v0.50.0:** dimension 8 takes R21's verified claims, below, as rules on dependency
  trees, names, unused ones, support and age gates; approved 2026-11-16.

The owner asked for one more rule, researched before it's written:

- **Fewest dependencies, newest versions:** a repository the standard sets up or audits runs on
  as few dependencies as possible, each at its newest version, so there's less to keep current
  and less for CI and dependency tools to check. R21 tests the aim against the evidence, and
  asks where it needs a limit. Its checked result goes into the standard as a change of its
  own, in dimensions 2, 6 and 8 and in what a new project starts with, so the pieces move text
  that already carries it. Dimension 8's part is in, as F169; the rest waits on claims R21
  didn't verify, which R21b asks again.

The owner also asked for one command that starts the standard from any repository, researched
before it's built:

- **The front door:** a short command, typed in a repository's session, starts a run. In an
  existing repository it reads the repository first, drafts the Phase 3 answers with where it
  found each, and asks only what no repository shows. In a new or nearly empty one it
  interviews the owner and recommends a language, runtime and shape. Every run still stops
  for approval before it writes anything. The plan had the skill reach cloud sessions by upload
  to the owner's claude.ai account, with the pinned link as a fallback. That's overtaken: since
  release 0.1.15 (2026-10-16), the release's `cloud-setup.sh` hook installs every skill into
  cloud sessions, checking the release's signature from 0.1.21, and claude.ai takes the
  plugins from the sync of `main`. R22's result came in two
  passes, both filed and checked:
  [the first](research/runs/2026-09-27-R22-one-command-front-door.md) and
  [a deeper one](research/runs/2026-09-27-R22-deeper-pass.md). It goes into piece 1, with F18,
  F26, F30 and F38. Both halves of the first live audit's report are triaged, as F39 to F50 record.
  What it adds to the plan:
  - **Settled by the owner on 2026-10-13,** with the evidence for each at
    `archive:2026-11-16/roadmap-r22-front-door-choices.md`: the reference's SHA-256 in
    `SKILL.md` shows which copy ran, checked at the start by a script with tests of its own,
    and `skillcheck` compares it with the file; a newer standard on `main` gets a warning, not
    a stop; a run asks five questions; its answers go in the run report's Phase 3 block; after
    each approved run it offers a project skill whose hook blocks writes, installed only on
    the owner's yes; and the catalog's version is bumped at each release.
  - **When it loads:** a description narrowed to runs that name it, since an uploaded skill
    can't carry `disable-model-invocation`. That needs the trigger evaluations the authoring
    review asks for. The Help Center gives an uploaded skill's description 200 characters at
    most, where the specification allows 1,024. This skill's is 217 on 2026-11-16, within this
    repository's cap of 250 but still over the 200 for an upload.
  - **A new project's recommendation:** at least two languages compared, each dependency
    checked against its registry, and each version against current release notes. Code models
    favor Python, name packages that don't exist (at least 5.2% of those from commercial
    models) and use deprecated APIs: the first pass's rows 64 and 66, and the deeper pass's
    F35. This joins R21's rule in piece 5.
  - **Tests in the owner's browser** settle what's left. Three are in the first pass's section
    10: what refreshes claude.ai's copy, with Check for updates tried before any version
    change; what a same-name upload does; and whether `skillOverrides` reaches a synced skill
    (F37). That last one is done: it does, tested here on 2026-10-15. A fourth comes with the
    first upload: whether a description over 200 characters is accepted.

| Piece | What moves | Status |
|---|---|---|
| 0 | Parity checks: sample repositories, answer keys, the grader, and the current skill's results as the baseline | shipped |
| 1 | The procedure into `SKILL.md`, from How to read this file, the routing table, What this is for, Scope, Assumptions, Limitations and the stop rules. Standing rules, vocabularies, environment and the conformance self-check into references, with `other-tools.md`. The report's skeleton and schema, and `check_report.py`. `skillcheck` checks the new structure. Findings it places, at `archive:2026-11-16/roadmap-standard-findings.md`: F3, F4, F13, F15, F17, F18, F22, F26, F30, F35, F38, F41, F43, F53, F54, F59, F62, F64, F65, F66, F67, F68, F96. | shipped |
| 2 | Starter file contents into `assets/templates/`, each file tested, with `starter-files.md`. Findings it places, at `archive:2026-11-16/roadmap-standard-findings.md`: F9, F70. | planned |
| 3 | Phase 4: one file per dimension, and `phase-4-dimensions.md` for greenfield generation. Findings it places, at `archive:2026-11-16/roadmap-standard-findings.md`: F5, F6, F8, F21, F24, F25, F29, F34, F49, F56, F58, F63, F72, F73, F74, F76, F78, F79, F80, F81, F82, F83, F84, F85, F86, F87, F88, F89, F90, F92, F93, F94, F95, F97, F99. | planned |
| 4 | Phases 0 to 3 and 5 to 9 into four phase files, with `preflight.py` and `inventory.py`. Findings it places, at `archive:2026-11-16/roadmap-standard-findings.md`: F1, F2, F12, F14, F16, F23, F27, F28, F31, F32, F35, F39, F42, F44, F45, F46, F47, F48, F50, F51, F52, F55, F60, F61, F69, F71, F80. | planned |
| 5 | Choosing a language and runtime, Choosing the shape and Project shapes and layout into `new-project.md`. The configuration file map, Standards distribution, File governance, the release and deploy currency gate, Cross-repository contracts, Any agent, any tool and the facts into their references. Findings it places, at `archive:2026-11-16/roadmap-standard-findings.md`: F7, F10, F11, F19, F20, F33, F36, F37, F40, F57, F75, F77, F91, F98, F100, F101, F102. | planned |
| 6 | Versioning, Proposing a change, Sending results back, Validating a change and Provenance retired. The standard file deleted. `AGENTS.md`, the authoring review, the README, the catalog and the research prompts updated. The skill's license becomes Apache-2.0. Release 0.2.0 | planned |

## Repository

These aren't skills, so `skillcheck` doesn't match them against `skills/`. Each waits on its
trigger.

| Item | What it is | Status | Trigger |
|---|---|---|---|
| Weekly currency check | The Freshness workflow, each Monday: facts due or whose quote is gone (`--due`, `--verify`), and dependencies behind their newest release (`--outdated`), each kept as one open issue | shipped | done, 2026-10-20 |
| End-of-life warning | A runtime or dependency whose support ends within six months. `--due` counts a fact due when its own words date an end of support, after a word such as "ends", "ended", "to" or "until", that falls within six months or has passed since the fact was checked, so the weekly check names it | shipped | done, 2026-11-16 |
| `copier` template | The standard's starter files, so a new repository is set up without a session | planned | the first repository set up from this one |
| A repository's own skills | `skillcheck` on a consuming repository's `.claude/skills/`, without this catalog's checks, with a marker for a draft and a check of a skill's scripts and tests beside it. Both audited repositories' steward skills asked for it; `--verify` there also needs to tell a source that wants credentials from a quote that's gone | planned | the next audit of either repository |
| Reusable workflows | This repository's CI gates, callable from other repositories | planned | a second repository wants this CI: met, by the owner's answer of 2026-11-16, since the private companion runs `skillcheck` from here |
| `upstream-defects.md` | The standard's register of upstream defects shared across repositories | planned | the first upstream defect found |
| Map refresh on dependency updates | Dependabot's pull requests change the lockfiles but not `bom.json` or `docs/dependencies.md`. CI's `--bom-check` fails such a pull request until a session regenerates the map in its branch before merging, as the owner chose on 2026-10-13 | shipped | done |
| Fewest dependencies here | This repository's own dependencies and pins, in `pyproject.toml`, `package.json` and CI, held to the R21 rule | planned | the rule is in the standard |
| One archive rule for every repository | Every repository keeps what is finished but worth keeping in a consistent way, tagged by version, release or date. Identical where that serves, with an archive branch beside any `evidence` branch as one candidate form; where a repository does otherwise, the difference is deliberate, recorded with its reason, and obvious to a reader of that repository. Before the rule, each did it differently: one audited repository keeps a `docs/archive/` folder in its main branch, another deletes finished work and keeps it in history, and this repository deleted it too. The rule is in the standard from v0.49.0, in dimension 10, approved on 2026-11-03. This repository is done: on 2026-11-03 it moved finished work to an orphan `archive` branch, indexed in [docs/archive.md](docs/archive.md) (`docs/decisions.md`, 2026-11-03). The audit kit and the repositories the standard audits are still to be brought into line, by audit | planned | this repository: done, 2026-11-03. The audit kit and the audited repositories: their next audit. The owner asked on 2026-10-29 for it before the next skills release |

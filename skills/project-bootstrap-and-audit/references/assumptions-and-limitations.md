# Assumptions and limitations

## Assumptions

These are beliefs the design rests on. Each could be wrong, and saying so is cheaper than
discovering it.

- **Instruction files are weak, and the evidence is specific about how.** A controlled study
  (Gloaguen et al., ETH Zurich / LogicStar, 2026, `arXiv:2602.11988`) tested four agents on 438
  tasks and found repository-level context files produced **no significant task-success gain
  while raising inference cost over 20% on average** — and that this held for developer-written
  files as much as generated ones. A follow-up (Lulla et al., 2026, `arXiv:2601.20404`)
  compared agents with and without an `AGENTS.md` on 124 pull requests in 10 repositories: the
  file went with **lower median runtime (28.64%) and fewer output tokens (16.58%)**, and task
  completion stayed comparable. One measures success and the other efficiency, so the two do
  not conflict. **What survives both results:** keep the context file short, hand-written, and
  limited to what a reader cannot discover from the codebase — tool commands being the one
  content type measurably used, by two orders of magnitude when the file names a non-standard
  tool, while repository overviews earned nothing. Two later measurements point the same way,
  the first only tentatively. First, **adherence to written instructions may decay within a
  session** — about 5.6% lower odds of compliance for each additional function generated
  (`arXiv:2605.10039`), an exploratory and non-monotonic finding in a study whose main result
  was that file size, position, structure and conflicts made no detectable difference — which
  is why this standard uses hard gates and puts its self-check last, where any decay is worst,
  rather than trusting one instruction stated once. Second, **the same guidance file measurably
  helped one model while hurting another**, which is why every budget rule here says minimal
  rather than complete. Everything here treats written rules as guidance, and only deny rules,
  hooks and server-side checks as enforcement.
- **Accretion is the failure mode**, not absence. A solo project dies of configuration nobody
  maintains more often than of configuration nobody wrote. Hence `OVER` as a first-class finding.
- **Declines are worth recording** — a written "no" with a reopen trigger prevents the same
  question being re-litigated every run.
- **Stakes are two axes, not one.** Blast radius and audience diverge; an internal tool three
  people use can break a production floor.
- **The human decides.** Where a choice has a real trade, it goes to them with both
  consequences rather than being applied on the agent's judgment.

## Limitations

- **It enforces nothing by itself.** It is a document an agent reads. Everything real is a
  deny rule, a hook, or a server-side check that this can only propose.
- **No code review.** Structure, wiring and configuration only. Logic, correctness and
  performance are out of scope.
- **Tier is a heuristic.** Two axes and four levels is a rough instrument; it is meant to stop
  gross mismatch, not to be precise.
- **Budgets are unmeasured.** The line counts are working heuristics, stated as smells rather
  than thresholds, because no measurement supports a specific number.
- **Git and a hosted remote are assumed.** Nothing here covers other version control.
- **Named tools and platform capabilities go stale.** Every version number, price and plan
  limit in this standard is dated in **Facts with an expiry date** and was true on that date
  only. A run that relies on one without checking it is reporting last year's platform.
- **Shapes not yet exercised** carry more risk: PowerShell, C#, C with meson, shell tools,
  and repositories with cross-repository contracts. The audit path has far more runs behind it
  than the scaffolding path.
- **It was built from one maintainer's estate, and it shows.** Every rule since 0.17.0 came
  from Python web applications and a C fork, all single-committer, all with tests, a build
  and a lockfile. **Adversarial probing found the shapes it handles badly**, and they share
  one property: the rule's premise about the repository is false. A proof-assistant
  repository with no test suite, a content-addressed build where pinning is meaningless, a
  documents or dataset repository with nothing to build, a monorepo with per-package
  versions, generative tests with no stable count. The standing rules' premise rule is the general
  answer; **it is not a substitute for knowing that this standard has never been run on any of
  them.**
- **Two cases have no rule at all, and are named here rather than left to be discovered.**
  A fork whose upstream is dead or deleted — the contract rules assume a live provider. And a
  prior decision record written by a *different* standard, which re-check mode will read as
  its own. **Each produces no opinion rather than a wrong one**, which is why they are
  tolerable, and each is a gap someone will eventually hit.
- **A repository that holds this standard treats the file as content.** It is rated only for
  placement, license and versioning (dimensions 3, 9 and 10), and a run never raises a
  repository amendment against it. Anything wrong with its rules arrives as a
  `class: standard` amendment, as *Proposing a change to this standard* describes.
- **The choosing part has no runs behind it at all.** Language and shape selection arrived in
  0.18.0 and has never been exercised on a real project. Treat its recommendations as a
  starting argument to disagree with, and report what it got wrong.
- **Planning is deliberately shallow.** Phase 9 sequences the work this run proposed and
  nothing else. It is not a substitute for project management and will look thin to anyone
  expecting one — that is the intent, not an omission.

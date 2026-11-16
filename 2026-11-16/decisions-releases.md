# Release entries, 2026-10-17 to 2026-11-16

Moved verbatim from `docs/decisions.md` on `main` at commit 32f0549, by the owner's "do all" of
2026-11-16: the entries that only record a release, whose contents `CHANGELOG.md` holds.
"The entry below" in each names the change it carried, which stays in `docs/decisions.md`
on `main`, under the same date.

## 2026-11-16 — Release 0.1.30, `visual-design` and twelve modules

- **The owner's word:** after "is anything in here looking ui and ux, consistency, ... If not we
  should" (2026-11-14) and "give me a full list of all remaining research" (2026-11-16), the
  owner attached seven results with no message, which `AGENTS.md` reads as research to take in.
  Releases follow each finished change, as before.
- **Carries:** the entry below. The catalog's versions move to 0.1.30. Nothing was renamed or
  removed; three modules were split within their skills, so no row in `docs/module-moves.md`.

## 2026-11-11 — Release 0.1.29, four modules from the follow-up research

- **The owner's word:** "old skills gone, give me the b research prompts" (2026-11-11); the
  owner then attached the four results with no message, which `AGENTS.md` reads as research to
  take in. Releases follow each finished change, as before.
- **Carries:** the entry below. The catalog's versions move to 0.1.29. Nothing was renamed or
  removed: a patch release. `optimization-and-scheduling`'s module keeps its name; its checking
  rules moved to a new module in the same skill, so no row in `docs/module-moves.md`.

## 2026-11-11 — Release 0.1.28, two new skills and two modules

- **The owner's word:** "lets do these human-factors and optimization-and-scheduling" and "and
  this coding's error-handling, operations' log-analysis" (2026-11-11), with R07, R23 and R28
  attached; releases follow each finished change, as before.
- **Carries:** the entry below. The catalog's versions move to 0.1.28. Nothing was renamed or
  removed in this repository: a patch release, as 0.1.26 was for new skills.

## 2026-11-11 — Release 0.1.27, `acceptance-runs`

- **The owner's word:** "do your full release here, as in the claude skills repo" (2026-11-11),
  after R06c arrived.
- **Carries:** `testing`'s `acceptance-runs` and R06c filed, from the entry below. The catalog's
  versions move to 0.1.27. Nothing was renamed or removed: a patch release.

## 2026-11-11 — Release 0.1.26, six new skills and standard v0.49.1

- **The owner's word:** release 0.1.26 once #140 and `testing-patterns` are merged and green,
  without asking again (2026-11-11, recorded above), and "make the new release now if you can"
  (2026-11-11), after deleting the old claude.ai `testing-patterns`.
- **Carries:** six new skills, `testing`, `agent-engineering`, `user-experience`, `security`,
  `architecture` and `operations` (#140, #144); `coding`'s five new modules (#136),
  `git-workflows`' `ci-cd` and `versioning-and-releases` (#137) and `house-style`'s
  `documentation` (#133); standard v0.49.1 (#142); the research R06, R06b, R26 and R27 filed
  (#127, #144) and R06c's prompt, eleven prompts brought up to date (#128); `skillcheck` fixes for PDF
  sources, permission levels and variation selectors (#129, #134, #139); two stale facts
  (#141).
- **Unchanged for consumers:** no skill or module was renamed or removed. The old claude.ai
  copies of `windows-admin`, `docker-containers`, `networking-security` and `testing-patterns`
  were deleted by the owner before their successors merged. A patch release, as 0.1.23 was
  for `coding`.

## 2026-11-03 — Release 0.1.25, standard v0.49.0 and checks that must fail

- **The owner's word:** "Do all you recommend" (2026-11-03), after this session listed release
  0.1.25 among its recommendations, once the changes before it landed.
- **Carries:** standard v0.49.0 (#113); the `ci-workflows` rule on a gate that passes a check
  which ran and failed (#111); `ci-speed` timing a release's run (#114); the steward template
  moved to `git-workflows`' assets (#110); the `archive` branch and `docs/archive.md` (#112); the
  mutation tests (#116) and three `skillcheck` fixes (#117); `.claude/worktrees/` ignored
  (#115). Also #104 to #109, merged since 0.1.24: `pr-stewardship`, workflow lockfiles in
  `action-pinning`, this repository's steward and `hold` check, and the dependency batch.
- **Unchanged for consumers:** no skill or module was renamed or removed, so it's a patch release.
  `pr-stewardship` is new since 0.1.24, and the standard's file is renamed with its version, as
  each version is.
- **After it:** the claude.ai tries for `ci-workflows` and `ci-speed`, which the owner runs.

## 2026-10-27 — Release 0.1.24, C in the `coding` skill

- **Asked, by the owner:** "release the new version of the skills now". The C audit's session
  had an installed `coding` without the C modules, because plugin installs and cloud sessions
  take a release, not `main`; it read them from the repository instead.
- **Carries:** how a repository using these skills is audited, and where its reports go (#89,
  #90), research prompts R12 and R25 (#91), what the first two audits found wrong in three
  skills (#92), `coding`'s three C modules and C in
  `skillcheck --examples` (#93), and what the C audit found wrong in them (#94). claude.ai has
  had each since its merge.
- **Unchanged for consumers:** no skill or module was renamed or removed, so nothing that names
  one breaks, and it's a patch release. Three modules and `house-style`'s `wrap-check.sh` are
  new.

## 2026-10-26 — Release 0.1.23, every module within claude.ai's file viewer

- **Asked, by the owner:** to get ready for an audit of the two repositories that consume these
  skills ("anything else you can do before that to be ready?"). The audit should test the skills
  as they now are, and plugin installs and cloud sessions take a release, not `main`.
- **Carries:** `coding`'s modules split in two (#85), `git-workflows`' and house style's (#86),
  the `modules` rule's 16,000-character limit (#86), and `--verify` retrying an unreadable
  source (#87). claude.ai has had each since its merge.
- **Unchanged for consumers:** no skill or module was renamed or removed, so nothing that names
  one breaks. Six of `coding`'s modules and three of `git-workflows`' are new.

## 2026-10-26 — Release 0.1.21, the first signed release

- **Asked, by the owner:** "yes do all", which took in signing releases and standard v0.48.2.
- **Carries:** the signed release and the hook that checks it (the entry below), and standard
  v0.48.2, merged as #78.
- **Proof it works:** the release run's page job checks every file's signature before it
  publishes, so a published 0.1.21 is one whose attestation verified.

## 2026-10-20 — Release 0.1.18

- **Asked, by the owner:** "proceed when ready", for release 0.1.18.
- **Carries:**
  - standard v0.48.0, with UTC as the stamp;
  - `skillcheck --time` and the `times` check;
  - `skillcheck --outdated` and its weekly run;
  - Python 3.15 and the other dependency updates;
  - the house style's rule on copied times;
  - the lessons from the two-repository loop.
- **Release 0.1.18:** this pull request's merge, released by the Release workflow once CI
  passes on it.

## 2026-10-17 — Release 0.1.17, for people beyond the owner

- **Asked, by the owner:** "release", so their brother installs the current skills: the
  modules, the report section in every skill, and the dependency updates.
- **Release 0.1.17:** this pull request's merge, released by the Release workflow once CI
  passes on it.

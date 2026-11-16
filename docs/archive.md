# What this repository keeps, and where

The answer this repository gives to the standard's four questions on records (dimension 10, from
v0.49.0), the owner's rule of 2026-10-29: consistency across repositories, not sameness, with
each difference deliberate, recorded and obvious.

1. **Its own record:** `docs/decisions.md` (append-only), `CHANGELOG.md`, `ROADMAP.md` and the
   dated research under `research/`. All stay on `main`, because sessions read them to work,
   less their finished parts. The owner's "do all" of 2026-11-16 moved `ROADMAP.md`'s applied
   findings, its lessons taken in and the front door's settled choices, and `docs/decisions.md`'s
   entries before 2026-10-16 and its release-only entries, to `archive`. `docs/decisions.md`'s
   last section lists each moved decision that still stands or is cited.
2. **What an outside reviewer would want:** the same, plus each release's signed files and
   attestations on its GitHub release page.
3. **What partner repositories need from it:** the released skills and the standard, on `main`
   and in each release. The messages sent to them, and the audit kit, name audited
   repositories, so they live in the private `audit-reports` repository's `audit-log` branch,
   never here. That is the one deliberate difference from the model: this public repository
   can't hold another repository's records.
4. **Worth keeping, off `main`:** a split's finished work and superseded logs move to the orphan
   `archive` branch in one commit, never merged into `main`, added to and never edited. Each
   item sits in a folder named by its date, and is listed below. `main`'s files name one as
   `archive:<path>`, and `git show origin/archive:<path>` reads it.

## Index of the `archive` branch

| Date | Path on `archive` | What it holds | Moved from |
|---|---|---|---|
| 2026-11-03 | `README.md` | What the branch is for | Created |
| 2026-11-16 | `2026-11-16/roadmap-standard-findings.md` | The standard's findings F1 to F167, each applied by v0.49.1, less F165 | `ROADMAP.md` |
| 2026-11-16 | `2026-11-16/roadmap-lessons-taken-in.md` | The 52 of lessons L1 to L57 that their modules took in | `ROADMAP.md` |
| 2026-11-16 | `2026-11-16/roadmap-r22-front-door-choices.md` | The front door's choices of 2026-10-13 | `ROADMAP.md` |
| 2026-11-16 | `2026-11-16/decisions-2026-09-23-to-2026-10-15.md` | Every decision entry dated before 2026-10-16 | `docs/decisions.md` |
| 2026-11-16 | `2026-11-16/decisions-releases.md` | The entries for releases 0.1.17, 0.1.18, 0.1.21 and 0.1.23 to 0.1.30, which only record a release | `docs/decisions.md` |

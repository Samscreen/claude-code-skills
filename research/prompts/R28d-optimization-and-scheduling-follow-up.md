# RESEARCH RUN R28d: Optimization and scheduling, what R28c didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: optimization-and-scheduling, plan-checking, rosters-and-replanning.

## What this run is for

A third follow-up. R28, R28b and R28c (filed 11 and 16 November 2026) built the optimization-
and-scheduling skill with its plan-checking and rosters-and-replanning modules. All three ran
out of room before dispatching rules, testing models, simulation beyond SimPy, commercial
licences in CI, and a documented failure. This run takes those. Don't repeat their findings;
where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R28d · FORM: research-result v1
Save as: R28d-RESULT.md
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

- Simple dispatching rules (EDD, SPT, critical ratio, ATC) stay close to optimal on dynamic
  shops where a solver's plan goes stale quickly.
- Hypothesis has been used to test optimization models by generating instances and checking
  invariants.
- salabim and Ciw are maintained Python discrete-event simulation libraries.
- CPLEX's free Community Edition is size-limited and needs no licence server in CI.

## Questions

### Priority

1. **Dispatching rules against solvers:** the published comparisons (dynamic job shops, rolling
   horizons), when a rule matches or beats a re-solved model, and the rules' definitions from
   primary sources.
2. **Testing optimization models:** property-based testing (Hypothesis, QuickCheck) of models
   and planners in published practice, metamorphic testing of solvers, and what invariants they
   check.
3. **Simulation beyond SimPy:** salabim, Ciw and others, with versions, licences and
   maintenance, and published use to test a schedule against variability.
4. **Commercial solvers in CI:** CPLEX's and Gurobi's terms and mechanisms for containers and CI
   runners, from IBM and Gurobi.

### Standard

5. **A documented failure** blamed on a plan that treated workers as deterministic or fully
   utilized.
6. **Due-date quoting:** a primary sentence from Keskinocak and Tayur (2004) or another primary
   source on the cost of quoting short against long; and Kingman's 1961 text, if a primary copy
   is reachable.

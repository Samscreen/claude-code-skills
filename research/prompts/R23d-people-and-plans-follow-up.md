# RESEARCH RUN R23d: People and plans, what R23c and R28c didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: human-factors, studying-work, cognitive-task-analysis, optimization-and-scheduling, rosters-and-replanning, plan-checking.

## What this run is for

A combined follow-up. R23 to R23c (filed 11 and 16 November 2026) built the human-factors skill;
R28 to R28c built optimization-and-scheduling. Both left questions open: keeping an AI's fact-
finding free of the user's framing, non-Western replications, method costs, what shortens the
dip after a new system, dispatching rules against solvers, testing models, simulation beyond
SimPy, commercial solvers in CI, and a documented failure from treating workers as machines.
Don't repeat their findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R23d · FORM: research-result v1
Save as: R23d-RESULT.md
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

- NIST AI 600-1 says nothing about a user's leading question steering a model's answer.
- Published studies show large language models change factual answers when a user states an
  opinion first.
- Status quo bias has been replicated in at least one East Asian sample with an effect size
  reported.
- A contextual inquiry visit takes about two hours plus as long again to interpret.
- Simple dispatching rules (EDD, SPT, critical ratio, ATC) stay close to optimal on dynamic
  shops where a solver's plan goes stale quickly.
- Hypothesis has been used to test optimization models by generating instances and checking
  invariants.
- salabim and Ciw are maintained Python discrete-event simulation libraries.

## Questions

### Priority

1. **Neutral retrieval:** what NIST AI 600-1, ISO/IEC 42001, the EU AI Act's guidance and peer-
   reviewed work on sycophancy and leading-question susceptibility say about a user's framing
   steering an AI's fact-finding, quoted, and any published mitigation that was measured.
2. **Non-Western replications:** status quo bias and habit formation (the automaticity curve)
   outside Western samples, with sample sizes, countries and effect sizes from the papers.
3. **What shortens the dip:** any controlled or field study measuring training, phased rollout,
   parallel running or super-users against the depth or length of the drop after a new system;
   and Cotteleer and Bendoly (2006) with its figures.
4. **Dispatching rules against solvers:** the published comparisons (dynamic job shops, rolling
   horizons), when a rule matches or beats a re-solved model, and the rules' definitions from
   primary sources.
5. **Testing optimization models:** property-based testing (Hypothesis, QuickCheck) of models
   and planners in published practice, metamorphic testing of solvers, and what invariants they
   check.

### Standard

6. **Method costs:** hours per study for contextual inquiry, hierarchical task analysis and the
   Critical Decision Method, from the methods' own authors or measured studies.
7. **A documented failure on a shop floor:** published cases of a plan loaded to full capacity,
   or one that treated workers as deterministic, and what followed, in the authors' words.
8. **Simulation beyond SimPy:** salabim, Ciw and others, with versions, licences and
   maintenance, and published use to test a schedule against variability.
9. **Commercial solvers in CI:** CPLEX's and Gurobi's terms and mechanisms for containers and CI
   runners, from IBM and Gurobi.
10. **Due-date quoting:** a primary sentence from Keskinocak and Tayur (2004) or another primary
    source on the cost of quoting short against long; and Kingman's 1961 text, if a primary copy
    is reachable.
11. **ISO 6385's 2026 review** and ISO 10075-3's next stage, from iso.org.

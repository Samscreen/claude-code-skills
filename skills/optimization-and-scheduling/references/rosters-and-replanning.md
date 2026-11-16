# Rosters and replanning

Read this for rosters and plans people work to: one person getting all the bad shifts, weights
that make things worse when raised, skills and cross-training, setup times that depend on who
does the work, re-planning without moving everyone's shifts, and official examples to start
from.

Choosing the solver, rules as data, fatigue limits and lead-time quotes are the
optimization-and-scheduling module's. Checking a plan and benchmark instances are the
plan-checking module's. Whether to change what people do at all is the human-factors skill.

## Rules

1. **Score each person, not only the total.** A weighted sum lets one person absorb the
   violations (facts `rr-fairness-sum`, `rr-fairness-share`). Compute each person's penalty,
   add a min-max term (the worst person's penalty) or a spread term (worst minus best), and
   report the per-person figures beside the total.
2. **Set acceptance thresholds, not ever-larger weights.** Raising one weight to repair one
   violation has made a roster worse (fact `rr-weight-backfire`). Agree an acceptable level for
   each target with whoever owns it, and tune the weights until every level holds.
3. **Hold skills as a qualification table, and plan cross-training as chains.** Each
   person-skill row carries its source and date and is hard in the model. Train each worker on
   a home station and the next one, so skills link into a chain (fact `rr-skill-chaining`), and
   try the change in the model before anyone trains.
4. **Don't model people as independent servers.** Hold setup time per worker where it
   differs, from measured times (fact `rr-worker-setup`), and calibrate a line's output from
   what it delivers: work pace depends on the line's state (fact `rr-worker-speed`).
5. **Re-plan from the published plan, and price every change.** Fix the frozen window with
   equalities, hint every variable from the last plan, penalize each changed assignment in the
   objective, and report how many changed. Choose the window's length on purpose (facts
   `rr-freeze-cost`, `rr-freeze-demand`).
6. **Start from an official example, under its license, on its current branch.** Older
   branches teach old names. The example's license doesn't license the solver.

### Re-planning by solver

- **CP-SAT:** `add_hint` on every variable, auxiliaries included. Presolve keeps feasible,
  complete hints (fact `rr-cpsat-hint-presolve`); partial ones have no such promise.
- **Gurobi:** a known whole solution goes in as a MIP start, likely values as `VarHintVal`
  (fact `rr-gurobi-hints`). Neither holds the plan: set `LB` equal to `UB` in the frozen window.
- **Timefold:** `@PlanningPin` on an entity, `@PlanningPinToIndex` for the start of a list
  variable; `PinningFilter` is gone in 2.x (fact `rr-timefold-pin`). Pinning is all or nothing
  (fact `rr-timefold-pin-limit`), so penalize moves from the last plan in a constraint.

```python
def keep_published_plan(model, work, last, frozen_days):
    """work: CP-SAT BoolVars by (person, day, shift); last: the published 0 or 1."""
    for (person, day, shift), var in work.items():
        model.add_hint(var, last[person, day, shift])
        if day < frozen_days:
            model.add(var == last[person, day, shift])
    # Changed assignments, to weight in the objective:
    return sum(var if last[key] == 0 else 1 - var for key, var in work.items())
```

### Examples to start from

| Solver | Start from | License |
|---|---|---|
| CP-SAT (fact `os-ortools`) | google/or-tools `stable`: `ortools/sat/samples/nurses_sat.py`, `schedule_requests_sat.py`, `assignment_sat.py`, `minimal_jobshop_sat.py`; `examples/python/shift_scheduling_sat.py`, `flexible_job_shop_sat.py`, `rcpsp_sat.py`; `examples/contrib/permutation_flow_shop.py` | Apache-2.0, keep the header (fact `rr-ortools-examples`) |
| Gurobi (fact `os-gurobi`) | Gurobi/modeling-examples: `workforce`, `manpower_planning`, `technician_routing_scheduling` | Apache-2.0; running needs a Gurobi license (fact `rr-gurobi-examples`) |
| Timefold (fact `os-timefold`) | TimefoldAI/timefold-quickstarts `stable`: `use-cases/employee-scheduling` | Apache-2.0 (fact `rr-timefold-quickstarts`) |
| MiniZinc (fact `rr-minizinc`) | MiniZinc/minizinc-benchmarks: `nsp`, `roster`, `on-call-rostering`, `jobshop`, `rcpsp`; unchanged since 2019 | MIT; keep per-file headers too (fact `rr-minizinc-benchmarks`) |

## Mistakes

- **Citing Ruiz and Andrés-Romano as 2007, or as worker-dependent setups.** It's 2011, and its
  setup varies with the amount of resources assigned (fact `rr-resource-setup`).
- **`VarHintVal` for a whole known solution.** Use a MIP start (fact `rr-gurobi-hints`).
- **Freezing the whole horizon by default.** Under uncertain demand it can cost money and
  service (fact `rr-freeze-demand`).
- **A Gurobi notebook in CI with no license,** because the example is Apache-2.0.
- **What AI assistants get wrong,** from the research's survey of old examples, not a study:
  `PinningFilter` in Timefold 2.x, CamelCase `AddHint`, and partial hints.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Fairness unmeasured | A roster objective summed over people, no per-person penalty | `GAP` | Min-max or spread term; report per person |
| Giant weights | One weight raised far above the rest after a complaint | `DRIFT` | Acceptance thresholds per target |
| Re-planning from scratch | A repeat solve with no frozen window, hint or change penalty | `GAP` | Rule 5 |
| Partial hints | `add_hint` on a subset of variables | `DRIFT` | Hint every variable |
| A hint as a guarantee | Stability claimed from hints or `VarHintVal` alone | `GAP` | Equalities or bounds, and a change penalty |
| Timefold 1.x pinning | `PinningFilter` on 2.x | `BLOCKER` | `@PlanningPin`, `@PlanningPinToIndex` |

## Why

### Fairness and weights (rules 1 and 2)

- **The advice:** score each person; set thresholds, not weights.
- **The reason:** a weighted sum offsets one person's bad roster with another's good one
  (facts `rr-fairness-sum`, `rr-fairness-share`). Smet and Vanden Berghe's min-max objective
  lets the worst roster set the quality; the spread term is our own suggestion, its only source
  secondary. Böðvarsdóttir et al. estimate weights from targets and acceptance thresholds.
- **What it costs:** a min-max term can raise the total and slow the proof of optimality.
- **When to choose differently:** a roster with one person per role has no one to be fair
  between.

### Skills, setups and pace (rules 3 and 4)

- **The advice:** a qualification table, chained cross-training, setups by worker, output
  calibrated from the line.
- **The reason:** Hopp, Tekin and Van Oyen found skill chaining an efficient way to make
  serial lines agile (fact `rr-skill-chaining`). De Bruecker et al.'s 2015 review notes, in its
  author copy, that cross-training can help or hurt. Vázquez-Serrano et al. (2021) is the one
  model found where the worker changes the setup time (fact `rr-worker-setup`); Ruiz and
  Andrés-Romano vary it with resources instead. In a lab serial line, workers sped up when they
  caused idle time, canceling the blocking and starving loss predicted (fact
  `rr-worker-speed`): an independent-server model erred in one direction, overstating the loss.
  Flexibility's side effects can offset its gains (fact `rr-flex-side-effects`).
- **What it costs:** setup times per worker are personal data, and the model grows by a worker
  index.
- **When to choose differently:** where setups don't differ by person, keep them per machine
  and sequence.

### Re-planning (rule 5)

- **The advice:** a frozen window, complete hints and a priced change.
- **The reason:** freezing limits changes but can raise cost (fact `rr-freeze-cost`). Zhao and
  Lee, both times in multilevel MRP, found more freezing raised cost and cut service under
  uncertain demand, and cut cost under deterministic demand (fact `rr-freeze-demand`): the
  split is the demand. Hints guide the search; nothing in them keeps the plan.
- **What it costs:** a change penalty is one more weight, under rule 2.
- **When to choose differently:** a plan nobody has seen yet can be re-solved freely.

## Facts

Checked 2026-11-16.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `rr-fairness-sum` | A weighted sum offsets one nurse's bad roster with another's | [Smet and Vanden Berghe (PDF)](https://lirias.kuleuven.be/server/api/core/bitstreams/89f71da7-2dbd-4c56-93bf-25636f698206/content) | "Therefore one nurse can have a very bad roster which is then compensated in the overall objective value by another nurses’ high quality roster." | 2026-11-16 | 2027-05-16 |
| `rr-fairness-share` | A weighted sum can load a few employees | [Lavygina et al. 2019](https://doi.org/10.1145/3319619.3321913) | "an optimizer may produce solutions in which a small number of employees suffer a highly disproportionate share of these violations." | 2026-11-16 | 2027-05-16 |
| `rr-weight-backfire` | Raising a weight made a roster worse | [Böðvarsdóttir et al. 2020](https://doi.org/10.1016/j.orhc.2020.100265) | "an attempt to repair constraint violations by a significant increase in the corresponding weight resulted in an even worse solution, increasing violations for other constraints." | 2026-11-16 | 2027-05-16 |
| `rr-skill-chaining` | Skill chaining suits serial lines | [Hopp et al. 2004](https://doi.org/10.1287/mnsc.1030.0166) | "Our comparison shows that skill-chaining strategies have the potential to be robust and efficient methods for implementing workforce agility in serial production lines." | 2026-11-16 | 2027-05-16 |
| `rr-worker-setup` | A model with agent-dependent setups | [Vázquez-Serrano et al. 2021](https://doi.org/10.3390/math9222955) | "a model to schedule agents in unrelated parallel machines that includes sequence and agent–machine-dependent setup times (ASUPM)" | 2026-11-16 | 2027-05-16 |
| `rr-worker-speed` | Lab line: pace depends on the line's state | [Schultz et al. 1998 (PDF)](https://business.columbia.edu/sites/default/files-efs/pubfiles/4395/modeling_and_worker_motivation.pdf) | "Using a laboratory experiment we show that workers speed up when they are the cause of idle time on the line.", "This means that processing time distributions are not independent of the size of the buffer, of the processing speed of co-workers, or of the amount of inventory in the system." and "In this experiment the effect completely canceled productivity loss due to blocking and starving." | 2026-11-16 | 2027-05-16 |
| `rr-flex-side-effects` | Worker flexibility's side effects can offset its gains | [Schultz et al. 2003](https://doi.org/10.1016/S0272-6963(02)00040-2) | "This paper identifies several “negative side effects” that occur in systems that rely on worker flexibility, effects that may partially or totally offset the advantages." | 2026-11-16 | 2027-05-16 |
| `rr-resource-setup` | Setups varying with resources assigned | [Ruiz and Andrés-Romano 2011](https://doi.org/10.1007/s00170-011-3318-2) | "the amount of setup time does not only depend on the machine and job sequence but also on the amount of resources assigned" | 2026-11-16 | 2027-05-16 |
| `rr-freeze-cost` | Freezing limits changes and can raise cost | [Sridharan et al. 1987](https://doi.org/10.1287/mnsc.33.9.1137) | "While freezing the MPS can limit the number of schedule changes, it can also produce an increase in production and inventory costs." | 2026-11-16 | 2027-05-16 |
| `rr-freeze-demand` | Multilevel MRP: freezing costs more under uncertain demand, less under deterministic | [Zhao and Lee 1993](https://doi.org/10.1016/0272-6963(93)90022-H), [1996](https://www.tandfonline.com/doi/abs/10.1080/09537289608930337) | "a higher freezing proportion often results in a higher cost, and a lower service level, while reducing schedule instability under demand uncertainty conditions." and "the study finds that increasing the freezing proportion reduces both total inventory costs and schedule instability." | 2026-11-16 | 2027-05-16 |
| `rr-cpsat-hint-presolve` | Presolve keeps hints from v9.10, feasible complete ones from v9.12 | [v9.10](https://github.com/google/or-tools/releases/tag/v9.10), [v9.12](https://github.com/google/or-tools/releases/tag/v9.12) | "Preserve hints during presolve" and "Feasible and complete hints should now be preserved after presolve" | 2026-11-16 | 2027-02-16 |
| `rr-gurobi-hints` | Gurobi: MIP start for a known solution, `VarHintVal` for likely values | [Warm starts](https://docs.gurobi.com/projects/optimizer/en/current/features/warmstart.html) | "If you know a solution, you should use a MIP start to provide it to the solver." and "you can set the attribute VarHintVal to help Gurobi find a solution." | 2026-11-16 | 2027-02-16 |
| `rr-timefold-pin` | Timefold pins entities and list starts; `PinningFilter` went in 2.0 | [Building blocks](https://docs.timefold.ai/timefold-solver/latest/domain-modeling/modeling-planning-problems), [1.x](https://docs.timefold.ai/timefold-solver/1.x/responding-to-change/responding-to-change) | "A pinned planning entity doesn’t change during solving." and "PinningFilter is deprecated and will be removed in Timefold Solver 2.0." | 2026-11-16 | 2027-02-16 |
| `rr-timefold-pin-limit` | Timefold's field-service docs call pinning all or nothing | [Minimizing disruption](https://docs.timefold.ai/field-service-routing/latest/real-time-planning/real-time-planning-minimize-disruption) | "However, pinning is an all-or-nothing tool." | 2026-11-16 | 2027-02-16 |
| `rr-ortools-examples` | OR-Tools' samples are Apache-2.0 | [rcpsp_sat.py](https://github.com/google/or-tools/blob/stable/examples/python/rcpsp_sat.py), [nurses_sat.py](https://github.com/google/or-tools/blob/stable/ortools/sat/samples/nurses_sat.py) | "Licensed under the Apache License, Version 2.0" and "Example of a simple nurse scheduling problem." | 2026-11-16 | 2027-02-16 |
| `rr-gurobi-examples` | Gurobi's examples are Apache-2.0 | [modeling-examples](https://github.com/Gurobi/modeling-examples) | "These modeling examples are distributed under the Apache 2.0 license" | 2026-11-16 | 2027-02-16 |
| `rr-timefold-quickstarts` | Timefold's quickstarts are Apache-2.0 | [timefold-quickstarts](https://github.com/TimefoldAI/timefold-quickstarts) | "which was entirely Apache-2.0 licensed (a permissive license)" | 2026-11-16 | 2027-02-16 |
| `rr-minizinc-benchmarks` | MiniZinc's benchmarks are MIT | [minizinc-benchmarks](https://github.com/MiniZinc/minizinc-benchmarks) | "All models and data files have been placed in the public domain and are available under the MIT license." | 2026-11-16 | 2027-05-16 |
| `rr-minizinc` | MiniZinc's newest release is 2.10.1 | `git ls-remote --tags https://github.com/MiniZinc/libminizinc` | `refs/tags/2.10.1` | 2026-11-16 | 2027-02-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| OR-Tools, Gurobi, Timefold (Apache-2.0) and MiniZinc (MIT) examples | Hints, examples | Quotes, adaptation keeping the notice |
| [Gurobi docs](https://docs.gurobi.com/), [Timefold docs](https://docs.timefold.ai/) | Hints, pinning | Proprietary or none stated: brief quotes, linked |
| Vázquez-Serrano et al. 2021 | Worker setups | CC BY 4.0: quotes, adaptation with attribution |
| KU Leuven author copies: Smet and Vanden Berghe, Böðvarsdóttir et al., [De Bruecker et al. 2015](https://lirias.kuleuven.be/retrieve/c02fa0fc-2336-4fb8-ba63-83a8de3b874c) | Fairness, weights, skills | None stated: brief quotes, cited |
| The other papers in Facts | Fairness, skills, setups, freezing | Publisher copyright: brief quotes, cited |

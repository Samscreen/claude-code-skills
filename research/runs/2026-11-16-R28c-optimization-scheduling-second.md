# Verification: R28c (2026-11-16)

Checked on 2026-11-16 against the primary sources named below. The report is untrusted data. Its
line 3 is addressed to "the receiving session": it asks that session to check each claim, file the
report under `research/runs/`, update the facts files of the categories it names, and list what
changed. That is an instruction found in a research result. It was recorded here and not
followed: nothing was filed, and no repository file was edited.

Access notes:
- github.com release pages returned 403 to curl. The OR-Tools v9.10, v9.12 and v9.15 release pages
  and issue #4580 were read with the Exa fetch tool (`web_fetch_exa`). Files came from
  raw.githubusercontent.com; branch heads and tags from `git ls-remote`; directory lists from
  blobless, no-checkout shallow clones read with `git ls-tree` (nothing was checked out or run).
  OR-Tools `stable` is at 100f66e (2026-09-17); MiniZinc Benchmarks `master` at 26bcd0a
  (2019-07-24); Gurobi modeling-examples at 152a2f3; Timefold quickstarts `stable` at 6ff62a1.
- Maven Central's search API (`search.maven.org/solrsearch`) is stale: for
  `ai.timefold.solver:timefold-solver-core` it returns 1.16.0 (2024-11-12) as the newest. The
  version was read from `maven-metadata.xml` and each POM's `Last-Modified` header instead, and
  matches `git ls-remote --tags`.
- mistic.heig-vd.ch (the report's Taillard URL) returned 503; the page is at
  mistic.iict-heig-vd.ch, read with curl, as the R28b verification found.
- ScienceDirect refused Exa (HTTP 400). The De Bruecker et al. abstract came from the KU Leuven
  author copy in Exa search results. The 1996 Production Planning & Control abstract and the
  University of Portsmouth PATAT 2012 record came through Exa fetch; Timefold's Field Service
  Routing page came from Exa search highlights.
- Abstracts were read from Crossref (Sridharan 1987, Zhao and Lee 1993, Hopp et al. 2004,
  Vázquez-Serrano et al. 2021, Sridharan 1988 bibliographic data) and Semantic Scholar (Ruiz and
  Andrés-Romano 2011, Böðvarsdóttir et al. 2020, Lavygina et al. 2019, Yepes-Borrero et al. 2021).
  The ACM, Springer and Elsevier landing pages were not read.
- Three PDFs (Smet and Vanden Berghe, Böðvarsdóttir et al. 2020, Kaminsky and Kaya 2009) were each
  downloaded into their own new empty directory and read only with `pdftotext`.
- Timefold docs and blog, Gurobi docs, OR-Library, PSPLIB, schedulingbenchmarks.org, MiniZinc
  downloads and changelog, gurobi.github.io and optaplanner.io were read with curl.

| Claim | Status | Checked against |
|---|---|---|
| C1: OR-Tools ships Python examples for flexible job shop, RCPSP and shift scheduling on `stable` | verified (`examples/python/flexible_job_shop_sat.py`, `rcpsp_sat.py`, `shift_scheduling_sat.py`, each "Copyright 2010-2025 Google LLC" and "Licensed under the Apache License, Version 2.0") | [examples/python](https://github.com/google/or-tools/tree/stable/examples/python) (raw files, `git ls-tree`) |
| C1 and section 9: no Python job-shop, flow-shop, assignment or nurse-scheduling file confirmed | verified with a correction. All exist on `stable`, each with the same Apache-2.0 header: job shop `examples/python/jobshop_ft06_sat.py`, `jobshop_ft06_distance_sat.py`, `jobshop_with_maintenance_sat.py` and `ortools/sat/samples/minimal_jobshop_sat.py` ("Minimal jobshop example."); flow shop `examples/contrib/permutation_flow_shop.py`; assignment `ortools/sat/samples/assignment_sat.py`, `assignment_groups_sat.py`, `assignment_task_sizes_sat.py`, `assignment_teams_sat.py`, `examples/python/assignment_with_constraints_sat.py`, `tasks_and_workers_assignment_sat.py`; nurses `ortools/sat/samples/nurses_sat.py` ("Example of a simple nurse scheduling problem.") and `schedule_requests_sat.py` ("Nurse scheduling problem with shift requests.") | `git ls-tree` of `stable`; raw.githubusercontent.com headers |
| C1: C++ job shop `examples/cpp/jobshop_sat.cc` | verified (file exists; the Google Groups citation was not read) | `git ls-tree` |
| C2: MiniZinc Benchmarks is MIT, with jobshop, flexible-jobshop, openshop, rcpsp variants, nsp, roster, on-call-rostering | verified. Also `mspsp`, `talent_scheduling`, `ship-schedule`, `stochastic-fjsp`, `gfd-schedule`. The README adds "All models and data files have been placed in the public domain and are available under the MIT license." The last commit is 2019-07-24 | [LICENSE](https://raw.githubusercontent.com/MiniZinc/minizinc-benchmarks/master/LICENSE); [README.md](https://raw.githubusercontent.com/MiniZinc/minizinc-benchmarks/master/README.md) |
| C3 and fact 21: OR-Library's material is MIT for any use | verified | [OR-Library legal page](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/legal.html) |
| C4: Kaminsky and Kaya "long lead times, missing the quoted lead times and high inventory levels" | verified (IIE Transactions 41 (2009) 103-119; a line break after "and") | [PK_OK_09.pdf](https://kaminsky.ieor.berkeley.edu/Reprints/PK_OK_09.pdf) |
| C4: Keskinocak, Ravi and Tayur (2001) model "lead-time sensitive revenues" | verified with a correction: the phrase is the title's ("...Lead-Time Sensitive Revenues", Management Science 47(2):264-279); the abstract says "revenues obtained from the customers are sensitive to the lead time" | Crossref [10.1287/mnsc.47.2.264.9836](https://doi.org/10.1287/mnsc.47.2.264.9836) |
| C5 and fact 24: Sridharan, Berry and Udayabhanu (1987), both quotes | verified (Management Science 33(9):1137-1149) | Crossref [10.1287/mnsc.33.9.1137](https://doi.org/10.1287/mnsc.33.9.1137) |
| C5: Zhao and Lee (1993) quotes on deterministic and uncertain demand | verified (J. Operations Management 11(2):185-205). Correction to section 4.3's framing: the 1993 study is itself about multilevel MRP ("in multilevel MRP systems under demand uncertainty conditions"), so the split with the 1996 study is deterministic versus uncertain demand, not single- versus multi-level | Crossref [10.1016/0272-6963(93)90022-H](https://doi.org/10.1016/0272-6963(93)90022-H) |
| Section 4.3: 1996 multilevel study "contradicts the finding by Sridharan et al. in single-level systems" | verified. Its authors are Zhao and Lee again; PPC 7(2):144-161 | [Taylor & Francis abstract](https://www.tandfonline.com/doi/abs/10.1080/09537289608930337) (Exa) |
| Section 4.3: Sridharan et al. (1988), Decision Sciences 19(1):147-166 | verified | Crossref [10.1111/j.1540-5915.1988.tb00259.x](https://doi.org/10.1111/j.1540-5915.1988.tb00259.x) |
| Fact 1: OR-Tools v9.15, 12 Jan 2026 | verified (published 2026-01-12T15:38:30Z; no tag after v9.15) | [Release v9.15](https://github.com/google/or-tools/releases/tag/v9.15) (Exa); `git ls-remote` |
| Fact 2: PyPI 9.15.6755, 14 Jan 2026 (report: secondary) | verified at the registry (upload 2026-01-14T15:38Z; still the newest) | [ortools JSON](https://pypi.org/pypi/ortools/json) |
| Fact 3: v9.15 "Add Python 3.14 support." | verified | Release v9.15 (Exa) |
| Fact 4: v10.0 milestone, no date | verified with a correction. #4580's page as fetched shows no milestone; the R28b verification read the milestones page: "v10.0" was "Due by October 14, 2026", now overdue | R28b-verification.md; [Issue #4580](https://github.com/google/or-tools/issues/4580) |
| Fact 5: OR-Tools example licence | verified ("Licensed under the Apache License, Version 2.0 (the \"License\");") | [rcpsp_sat.py](https://raw.githubusercontent.com/google/or-tools/stable/examples/python/rcpsp_sat.py) |
| Fact 6: MiniZinc Benchmarks "MIT License Copyright (c) 2016 MiniZinc (individual authors)" | verified (two lines on the page, with a blank line between) | LICENSE |
| Fact 7: MiniZinc 2.10.0 released 23 July 2026 | verified. But the report's "2.10.0 is the last dated release found" is contradicted: the downloads page says "The latest release of MiniZinc is version 2.10.1 , released 31 August 2026"; there is no 2.10.2 tag | [MiniZinc downloads](https://www.minizinc.org/downloads/); [changes.rst](https://raw.githubusercontent.com/MiniZinc/libminizinc/master/changes.rst); `git ls-remote --tags` |
| Fact 8: 2.9.6 drops SCIP 7 and earlier | verified (2.9.6 released 24 April 2026) | [MiniZinc changelog](https://docs.minizinc.dev/en/latest/changelog.html) |
| Fact 9: Gurobi modeling-examples Apache 2.0 | verified with a correction: the README breaks the line with `<br>` before "© Gurobi Optimization, LLC", and the repository has no LICENSE file (404) | [README.md](https://raw.githubusercontent.com/Gurobi/modeling-examples/master/README.md) |
| Fact 10: workforce notebook is a multi-objective MIP | verified on the page ("The problem is formulated as..."); the notebook itself says "The problem was formulated as..." | [Workforce Scheduling Problem](https://gurobi.github.io/modeling-examples/workforce/) |
| Section 4.1: notebook "minimizes the number of temporary workers ... and maximizes employee fairness" | verified with a correction: the notebook reads "maximizes employee fairness and satisfaction, and minimizes the number of temporary workers your company needs to hire" | [workforce_scheduling.ipynb](https://raw.githubusercontent.com/Gurobi/modeling-examples/master/workforce/workforce_scheduling.ipynb) |
| Section 4.1: notebooks `manpower_planning`, `technician_routing_scheduling`, `factory_planning_1_2` | verified with a correction: the directory is `factory_planning` | `git ls-tree` |
| Section 4.1: pip package's "size-limited trial license", sufficient for most notebooks | verified | README.md |
| Fact 11: Timefold Quickstarts forked 20 April 2023 from Apache-2.0 OptaPlanner Quickstarts | verified (LICENSE.txt is Apache 2.0; the README adds "Every source file has been modified.") | [README.md (stable)](https://raw.githubusercontent.com/TimefoldAI/timefold-quickstarts/stable/README.md) |
| Section 4.1: quickstart names `quarkus-employee-scheduling` and others | verified with a correction: the directories are `use-cases/<name>` (`employee-scheduling`, `maintenance-scheduling`, `food-packaging`, `school-timetabling`, `conference-scheduling`, `bed-allocation`, `flight-crew-scheduling`, `order-picking`, `vehicle-routing`, plus `project-job-scheduling`, `task-assigning`, `meeting-scheduling`, `sports-league-scheduling`, `tournament-scheduling`, `facility-location`). "quarkus-employee-scheduling" is the README's run label. The `stable` POM is at 2.8.0 | `git ls-tree`; pom.xml |
| Section 4.1: "Schedule shifts to employees, accounting for employee availability and shift skill requirements." | verified | README.md (stable) |
| Fact 12: Timefold Solver 2.0 GA 22 April 2026, "Timefold Solver 2.0 is available now." | verified (blog dated April 22, 2026; Maven POM 2026-04-22 09:28 UTC) | [Timefold Solver 2.0 released](https://timefold.ai/blog/timefold-solver-2-0-release) |
| Fact 13 and Tools table: Timefold 2.7.1 (6 Oct 2026) is the latest | contradicted. optaplanner.io's sidebar does read "Timefold Solver 2.7.1 released Tue 6 October 2026", but the current release is 2.8.0, 3 Nov 2026 07:49 UTC (the R28 and R28b verifications found the same) | [maven-metadata.xml](https://repo1.maven.org/maven2/ai/timefold/solver/timefold-solver-core/maven-metadata.xml); `git ls-remote --tags` |
| Fact 14 and section 6: Community Edition 1.x "maintained throughout 2026"; the one EOL to flag | verified with a correction. The quote is exact on the 20 Jan 2026 post. The v1.34.0 notes put 1.x EOL "in early 2027", and 1.35.0 (15 Oct 2026) is "the penultimate release"; no v1.36 tag yet | [Introducing Timefold Solver 2.0](https://timefold.ai/blog/introducing-timefold-solver-2-0); R28-verification.md; `git ls-remote` |
| Fact 15: "Solver 2.0 moves the Java baseline from 17 to 21." | verified (post dated April 24, 2026) | [upgrade in minutes](https://timefold.ai/blog/timefold-solver-2-0-upgrade-in-minutes) |
| Fact 16: explainability in a paid "Plus" edition | verified as written on 22 Apr 2026, with a correction: today the score-analysis docs say "This feature is exclusive to Timefold Solver Enterprise Edition." (R28 verification) | 2.0 release blog; R28-verification.md |
| Section 6: `count()`/`countDistinct()` changed from Integer to Long (report: secondary) | verified at the primary source: "count() and countDistinct() used to return Integer . They now return Long ." | upgrade-in-minutes post |
| Section 4.1: Employee Scheduling and Order Picking quickstarts needed manual changes | verified ("Two of our quickstart projects (Employee Scheduling and Order Picking) used grouping functions...") | upgrade-in-minutes post |
| Fact 17: "A pinned planning entity doesn't change during solving." | verified with a correction: the page has a curly apostrophe, "doesn’t" (U+2019) | [Building blocks](https://docs.timefold.ai/timefold-solver/latest/domain-modeling/modeling-planning-problems) |
| Fact 18: `PinningFilter` deprecated in 1.x, removed in 2.0 | verified. The 1.x docs: "PinningFilter is deprecated and will be removed in Timefold Solver 2.0." The upgrade guide: "We have removed the long-deprecated the pinningFilter field on @PlanningEntity annotation" (sic) | [1.x Responding to change](https://docs.timefold.ai/timefold-solver/1.x/responding-to-change/responding-to-change); [Upgrade from 1.x](https://docs.timefold.ai/timefold-solver/latest/upgrading-timefold-solver/upgrade-from-v1) |
| Section 4.3: `@PlanningPinToIndex` pins part of a list variable | verified ("When @PlanningPinToIndex is used, the list is split in two parts.") | Building blocks |
| Section 4.3: `@PlanningPinToIndex` added in 1.6.0, quote "a certain portion of the list variable is pinned" | unverifiable (the 1.6.0 note was not found; R28's verification also left it unchecked) | none |
| Section 4.3: field-service "pinning is an all-or-nothing tool"; "Minimize disruption on replanning" | verified (Timefold's commercial Field Service Routing docs) | [Minimizing disruption on replanning](https://docs.timefold.ai/field-service-routing/latest/real-time-planning/real-time-planning-minimize-disruption) (Exa highlights) |
| Fact 19 and mistake 5: "If you know a solution, you should use a MIP start to provide it to the solver." | verified | [Warm Start Options](https://docs.gurobi.com/projects/optimizer/en/current/features/warmstart.html) |
| Section 4.3: `VarHintVal` sentence | verified | Warm Start Options |
| Section 4.3: "Hint priorities are relative … The default hint priority for a variable is 0." | verified with a correction: both sentences are on the variable-attributes page under VarHintPri, not the warm-start page, with a sentence between them | [Variable attributes](https://docs.gurobi.com/projects/optimizer/en/current/reference/attributes/variable.html) |
| Fact 20: `add_hint` "Adds 'var == value' as a hint to the solver." | verified (cp_model.py line 1656 on `stable`; the pdoc page shows it) | [cp_model.py](https://raw.githubusercontent.com/google/or-tools/stable/ortools/sat/python/cp_model.py); [pdoc](https://or-tools.github.io/docs/pdoc/ortools/sat/python/cp_model.html) |
| Fact 20: `fix_variables_to_their_hinted_value` is a parameter | verified ("If true, variables appearing in the solution hints will be fixed to their hinted value.", default false) | [sat_parameters.proto](https://raw.githubusercontent.com/google/or-tools/stable/ortools/sat/sat_parameters.proto) |
| Section 4.3: v9.10 (8 May 2024) "Preserve hints during presolve" | verified (published 2024-05-08T08:27Z) | [Release v9.10](https://github.com/google/or-tools/releases/tag/v9.10) (Exa) |
| Section 4.3: v9.12 "Rewrote the hint transformation during presolve. Feasible and complete hints should now be preserved after presolve." | verified with a correction: the page has no full stop after "presolve" (a bullet); published 2025-02-17 | [Release v9.12](https://github.com/google/or-tools/releases/tag/v9.12) (Exa) |
| Section 4.3 and mistake 3: Primer "CP-SAT only benefits from complete hints (all variables hinted)." | secondary only (found: it is the docstring of a helper function in the Primer's README, not prose guidance) | [cpsat-primer README](https://raw.githubusercontent.com/d-krupke/cpsat-primer/main/README.md) |
| Section 4.1: `shift_scheduling_sat.py` "This fixes the first 2 days of the schedule." | verified (line 214) | raw shift_scheduling_sat.py |
| Section 4.1: `rcpsp_sat.py` docstring; bintest instances | verified (also `rcpsp_sat_rip1_py_test.bintest`) | raw rcpsp_sat.py; `git ls-tree` |
| Section 4.1: flexible job shop uses `solver.value`, `solver.boolean_value` | verified | raw flexible_job_shop_sat.py |
| Section 1 and mistake 11: `rcpsp_sat.py` links `http://www.om-db.wi.tum.de/psplib/data.html`, which is stale | verified: that URL returns 404; `data.php` returns 200 | raw rcpsp_sat.py; curl |
| Section 4.1: `nsp/nsp_2.mzn` quote | verified with a correction: the file reads "satisfy  nurses demand" (two spaces) across a line break | [nsp_2.mzn](https://raw.githubusercontent.com/MiniZinc/minizinc-benchmarks/master/nsp/nsp_2.mzn) |
| Section 4.1: `rcpsp.mzn` "University of Melbourne and NICTA. See the file COPYING" | verified; the repository root has no COPYING file | [rcpsp.mzn](https://raw.githubusercontent.com/MiniZinc/minizinc-benchmarks/master/rcpsp/rcpsp.mzn); `git ls-tree` |
| Section 4.1: README "collection of MiniZinc benchmark instances including instances from the 2008-2012 MiniZinc challenges" | verified (upstream; line break after "from") | README.md |
| Section 4.1: Timefold Python "significantly slower" | verified (the repository is archived; R28b verification) | [timefold-solver-python README](https://raw.githubusercontent.com/TimefoldAI/timefold-solver-python/main/README.md) |
| Fact 22: PSPLIB "Researchers may download the benchmark sets..."; no licence stated; "FILE MISSING" | verified (a line break after "their"); no licence or copyright text on the page | [Welcome to PSPLIB](https://www.om-db.wi.tum.de/psplib/library.php) |
| Section 4.4: PSPLIB site cites 1996; journal 1997 | verified (site "Kolisch, R. and A. Sprecher (1996)"; Crossref EJOR 96(1):205-216, issued Jan 1997) | PSPLIB; Crossref [10.1016/s0377-2217(96)00170-1](https://doi.org/10.1016/s0377-2217(96)00170-1) |
| Fact 23: Instance24 open, 40438 / 40439; "All solutions are verified..." | verified; neither the NRP page nor the home page states a licence | [NRP instances](https://www.schedulingbenchmarks.org/nrp/) |
| Section 4.4: Burke and Curtois, EJOR 237(1) 2014, 71-81 | verified | Crossref [10.1016/j.ejor.2014.01.039](https://doi.org/10.1016/j.ejor.2014.01.039) |
| Section 4.4: Taillard terms not found | verified with a correction: the page is at mistic.iict-heig-vd.ch (the report's host returns 503); it states no licence | [Scheduling instances](https://mistic.iict-heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html) |
| Section 4.4: OR-Library scheduling sets; "Copyright (c) (2010) (J E Beasley}" | verified (the list also has two "Workforce scheduling" entries) | [OR-Library](https://people.brunel.ac.uk/~mastjjb/jeb/info.html); legal page |
| Section 1: Beasley Emeritus since December 2013 | verified ("having retired from full-time work in December 2013") | [J E Beasley](https://people.brunel.ac.uk/~mastjjb/jeb/jeb.html) |
| Fact 25: Smet and Vanden Berghe, weighted sum and "very bad roster" quotes | verified with a correction: "another nurses’ high quality roster" has a curly apostrophe (U+2019). The PDF is an undated KAHO Sint-Lieven report; its reference list cites 2012 | [A study on fairness objectives](https://lirias.kuleuven.be/server/api/core/bitstreams/89f71da7-2dbd-4c56-93bf-25636f698206/content) (pdftotext) |
| Section 4.2: FO = max over nurses | verified in the primary: Equation (2), "the quality of the worst individual roster determines the overall solution quality". RO (spread) stays secondary only | same PDF |
| Section 4.2: PATAT 2012 "opens" with "In the literature on nurse rostering, the fairness of the constructed rosters has often been neglected." | verified with a correction: it is the abstract's second sentence | [Portsmouth research portal](https://researchportal.port.ac.uk/en/publications/investigation-of-fairness-measures-for-nurse-rostering/) (Exa) |
| Section 4.2: Lavygina, Welsh and Crispin (GECCO '19) quote | verified (GECCO '19 Companion, pp. 217-218) | Semantic Scholar; Crossref [10.1145/3319619.3321913](https://doi.org/10.1145/3319619.3321913) |
| Fact 26: Vázquez-Serrano et al. (2021) quote; CC BY 4.0 | verified (Mathematics 9(22):2955, 19 Nov 2021; Crossref licence CC BY 4.0) | Crossref [10.3390/math9222955](https://doi.org/10.3390/math9222955) |
| Section 4.2: Ruiz and Andrés-Romano (2011) quote and citation | verified (IJAMT 57(5-8):777-794, online 6 May 2011) | Semantic Scholar; Crossref |
| Section 4.2: Yepes-Borrero et al. (2021) "These setups are performed by personnel, who are of course limited in number." | verified (EJOR 292(2):443-455) | Semantic Scholar; Crossref [10.1016/j.ejor.2020.10.052](https://doi.org/10.1016/j.ejor.2020.10.052) |
| Section 4.2: Fanjul-Peyro et al. 2017 and 2019 citations | verified (bibliographic data only; the 2017 quote, which the report flags, was not checked) | Crossref |
| Fact 27 and section 4.2: Hopp, Tekin and Van Oyen (2004), both quotes | verified (Management Science 50(1):83-98) | Crossref [10.1287/mnsc.1030.0166](https://doi.org/10.1287/mnsc.1030.0166) |
| Section 4.2: De Bruecker et al. (2015) "This paper presents a review and classification..." | verified (EJOR 243(1):1-16; author copy) | [KU Leuven author copy](https://lirias.kuleuven.be/retrieve/c02fa0fc-2336-4fb8-ba63-83a8de3b874c) (Exa); Crossref |
| Section 4.2: De Bruecker "Skill substitution and cross-training, for example, can have a positive or negative effect..." | unverifiable. The author copy's introduction reads differently ("skill substitution, cross-training, learning effects, etc., involve some indirect and sometimes unexpected consequences that can have a positive or negative effect on the performance of the company"); the published text wasn't reachable | same |
| Section 4.9: Böðvarsdóttir, Smet and Vanden Berghe (2020), both quotes | verified (ORHC 26:100265) | [author PDF](https://lirias.kuleuven.be/retrieve/4f681f12-240c-43ee-95d2-8ba3e7632471) (pdftotext); Crossref |
| Section 4.9: acceptance thresholds instead of weights | verified ("targets and their acceptance thresholds") | same PDF |
| Section 4.9: Böðvarsdóttir et al. 2021 EJOR 292(3):980-995 | not checked | none |
| Section 4.6: Keskinocak and Tayur (2004) sentence (report: not found); EJOR review quote | not checked (the report marks the first not found; the second names no source) | none |
| Sections 4.5, 4.7, 4.8, Q9 failure case | not checked (the report marks them not found or not covered) | none |

Counts, one per row by its main status: 56 verified, 15 verified with a correction,
1 contradicted, 2 unverifiable, 1 secondary only, 3 not checked (78 rows). Two "verified" rows
carry a further correction: fact 7 (2.10.1, not 2.10.0, is current) and fact 16 ("Plus" is now
Enterprise).

### What R28c corrects in R28 and R28b, and what it repeats

- **Benchmark licences.** R28b didn't cover OR-Library. R28c's MIT finding is right, and the
  module's rule (cite figures, copy no instance file) still fits Taillard, PSPLIB and
  schedulingbenchmarks.org, none of which states a licence.
- **Timefold's version.** R28c repeats R28b's stale 2.7.1. The current release is still 2.8.0
  (3 Nov 2026), as both earlier verifications found.
- **Timefold 1.x end of life.** R28c repeats "throughout 2026" as the end. The release notes say
  early 2027, and the R28 verification already recorded that.
- **Explainability edition.** R28c repeats "Plus", which Timefold now calls Enterprise.
- **MiniZinc.** R28c says 2.10.0 is the newest dated release; 2.10.1 (31 Aug 2026) is, as the R28
  verification found.
- **OR-Tools examples.** R28c couldn't find Python job-shop, assignment and nurse examples. They
  exist (paths above), which also fixes R28b's inference that an official job-shop example
  exists only because Google's page lists the problem.

## Exact quotes for facts rows

Each quote is as it appears at the source. Where the source breaks a line, the quote joins it
with a space.

| Fact | URL | Exact quote |
|---|---|---|
| OR-Tools examples are Apache-2.0 | https://github.com/google/or-tools/blob/stable/examples/python/rcpsp_sat.py | "Licensed under the Apache License, Version 2.0 (the \"License\");" (straight quotes in the file) |
| OR-Tools minimal job shop sample | https://github.com/google/or-tools/blob/stable/ortools/sat/samples/minimal_jobshop_sat.py | "Minimal jobshop example." |
| OR-Tools nurse sample | https://github.com/google/or-tools/blob/stable/ortools/sat/samples/nurses_sat.py | "Example of a simple nurse scheduling problem." |
| OR-Tools nurse requests sample | https://github.com/google/or-tools/blob/stable/ortools/sat/samples/schedule_requests_sat.py | "Nurse scheduling problem with shift requests." |
| OR-Tools assignment sample | https://github.com/google/or-tools/blob/stable/ortools/sat/samples/assignment_sat.py | "Solves a simple assignment problem with CP-SAT." |
| OR-Tools flow shop (contrib) | https://github.com/google/or-tools/blob/stable/examples/contrib/permutation_flow_shop.py | "This model implements the permutation flow shop problem (PFSP)." |
| Shift example fixes a window | https://github.com/google/or-tools/blob/stable/examples/python/shift_scheduling_sat.py | "This fixes the first 2 days of the schedule." |
| CP-SAT hint | https://github.com/google/or-tools/blob/stable/ortools/sat/python/cp_model.py | "Adds 'var == value' as a hint to the solver." |
| CP-SAT hint fixing | https://github.com/google/or-tools/blob/stable/ortools/sat/sat_parameters.proto | "If true, variables appearing in the solution hints will be fixed to their hinted value." |
| Hints survive presolve (v9.12) | https://github.com/google/or-tools/releases/tag/v9.12 | "Rewrote the hint transformation during presolve. Feasible and complete hints should now be preserved after presolve" (no final full stop) |
| Hints preserved (v9.10) | https://github.com/google/or-tools/releases/tag/v9.10 | "Preserve hints during presolve" |
| Gurobi MIP start | https://docs.gurobi.com/projects/optimizer/en/current/features/warmstart.html | "If you know a solution, you should use a MIP start to provide it to the solver." |
| Gurobi variable hints | same | "you can set the attribute VarHintVal to help Gurobi find a solution." |
| Gurobi hint priority default | https://docs.gurobi.com/projects/optimizer/en/current/reference/attributes/variable.html | "The default hint priority for a variable is 0." |
| Timefold pinning | https://docs.timefold.ai/timefold-solver/latest/domain-modeling/modeling-planning-problems | "A pinned planning entity doesn’t change during solving." (curly apostrophe U+2019) |
| Timefold list pinning | same | "When @PlanningPinToIndex is used, the list is split in two parts." |
| PinningFilter deprecated | https://docs.timefold.ai/timefold-solver/1.x/responding-to-change/responding-to-change | "PinningFilter is deprecated and will be removed in Timefold Solver 2.0." |
| Pinning's limit (commercial FSR) | https://docs.timefold.ai/field-service-routing/latest/real-time-planning/real-time-planning-minimize-disruption | "However, pinning is an all-or-nothing tool." |
| Timefold 2.x Java floor | https://timefold.ai/blog/timefold-solver-2-0-upgrade-in-minutes | "Solver 2.0 moves the Java baseline from 17 to 21." |
| Timefold 2.0 collectors | same | "count() and countDistinct() used to return Integer" (continues ". They now return Long .") |
| Timefold Quickstarts licence | https://github.com/TimefoldAI/timefold-quickstarts | "Timefold Quickstarts was forked on 20 April 2023 from OptaPlanner Quickstarts, which was entirely Apache-2.0 licensed (a permissive license)." ("forked" is a link) |
| Timefold employee scheduling | same | "Schedule shifts to employees, accounting for employee availability and shift skill requirements." |
| Gurobi examples licence | https://github.com/Gurobi/modeling-examples | "These modeling examples are distributed under the Apache 2.0 license" (then a line break and "© Gurobi Optimization, LLC") |
| Gurobi examples run on the pip licence | same | "For most of the notebooks, this restricted license is sufficient." |
| MiniZinc Benchmarks licence | https://github.com/MiniZinc/minizinc-benchmarks/blob/master/LICENSE | "Copyright (c) 2016 MiniZinc (individual authors)" (under the heading "MIT License") |
| MiniZinc Benchmarks README | https://github.com/MiniZinc/minizinc-benchmarks | "All models and data files have been placed in the public domain and are available under the MIT license." |
| OR-Library licence | https://people.brunel.ac.uk/~mastjjb/jeb/orlib/legal.html | "All of the material available from OR-Library is freely available for use. As such the MIT licence, reproduced below, applies:" |
| OR-Library notice | same | "Copyright (c) (2010) (J E Beasley}" (mismatched brace as on the page) |
| PSPLIB use | https://www.om-db.wi.tum.de/psplib/library.php | "Researchers may download the benchmark sets to evaluate their algorithms, and they may send their results to be added to the library." |
| NRP verification | https://www.schedulingbenchmarks.org/nrp/ | "All solutions are verified before being reported on this website. It is not possible to verify lower bounds." |
| Freezing cost (1987) | https://doi.org/10.1287/mnsc.33.9.1137 | "While freezing the MPS can limit the number of schedule changes, it can also produce an increase in production and inventory costs." |
| Freezing under uncertainty (1993) | https://doi.org/10.1016/0272-6963(93)90022-H | "a higher freezing proportion often results in a higher cost, and a lower service level, while reducing schedule instability under demand uncertainty conditions." |
| Freezing, deterministic (1996) | https://www.tandfonline.com/doi/abs/10.1080/09537289608930337 | "the study finds that increasing the freezing proportion reduces both total inventory costs and schedule instability." |
| Fairness, weighted sum | https://lirias.kuleuven.be/server/api/core/bitstreams/89f71da7-2dbd-4c56-93bf-25636f698206/content | "Therefore one nurse can have a very bad roster which is then compensated in the overall objective value by another nurses’ high quality roster." (U+2019) |
| Fairness, disproportionate share | https://doi.org/10.1145/3319619.3321913 | "an optimizer may produce solutions in which a small number of employees suffer a highly disproportionate share of these violations." |
| Weight tuning | https://doi.org/10.1016/j.orhc.2020.100265 | "Practitioners and researchers alike have pointed out unexpected consequences when manually adjusting objective weights." |
| Raising a weight backfired | same | "an attempt to repair constraint violations by a significant increase in the corresponding weight resulted in an even worse solution, increasing violations for other constraints." |
| Skill chaining | https://doi.org/10.1287/mnsc.1030.0166 | "Our comparison shows that skill-chaining strategies have the potential to be robust and efficient methods for implementing workforce agility in serial production lines." |
| Worker-dependent setups | https://doi.org/10.3390/math9222955 | "a model to schedule agents in unrelated parallel machines that includes sequence and agent–machine-dependent setup times (ASUPM)" (en dash U+2013) |
| Resource-dependent setups | https://doi.org/10.1007/s00170-011-3318-2 | "the amount of setup time does not only depend on the machine and job sequence but also on the amount of resources assigned" |
| Setups need personnel | https://doi.org/10.1016/j.ejor.2020.10.052 | "These setups are performed by personnel, who are of course limited in number." |

## Versions found from registries

| Tool | Current version | Released | Read from |
|---|---|---|---|
| OR-Tools (ortools) | 9.15.6755 (tag v9.15; no later tag) | PyPI 2026-01-14T15:38Z; GitHub 2026-01-12T15:38Z | PyPI JSON; `git ls-remote --tags`; release page (Exa) |
| Timefold Solver | 2.8.0 | 2026-11-03 07:49 UTC (2.7.1 on 2026-10-06 09:55 UTC; 2.0.0 on 2026-04-22) | Maven Central `maven-metadata.xml` and POM `Last-Modified`; tag v2.8.0 |
| Timefold Solver 1.x | 1.35.0 | 2026-10-15 12:16 UTC | Maven Central |
| Timefold Quickstarts | `stable` builds against 2.8.0 | not versioned | pom.xml on `stable` |
| MiniZinc | 2.10.1 (no 2.10.2 tag) | 31 Aug 2026 (2.10.0 on 23 Jul 2026) | downloads page; changes.rst; `git ls-remote --tags` |
| MiniZinc Benchmarks | unversioned; last commit 26bcd0a | 2019-07-24 | `git ls-remote`, clone metadata |
| Gurobi modeling-examples | unversioned; head 152a2f3 | not checked | `git ls-remote` |

## Licences

| Source | Licence as the source states it | What an Apache-2.0 repository may do |
|---|---|---|
| OR-Tools examples and samples | Apache License 2.0 ("Copyright 2010-2025 Google LLC" header in each file read) | Quote, paraphrase; adapt code keeping the header and NOTICE, marking changes |
| MiniZinc Benchmarks | MIT (LICENSE, 2016) and "placed in the public domain" (README); some files keep a 2009-2012 Melbourne/NICTA header pointing to a COPYING file the repository lacks | Quote, paraphrase; adapt keeping the MIT notice and any per-file header |
| Gurobi modeling-examples | "distributed under the Apache 2.0 license © Gurobi Optimization, LLC" (README only; no LICENSE file) | Quote, paraphrase; adapt with the notice; running them needs a Gurobi licence |
| Timefold Quickstarts | Apache 2.0 (LICENSE.txt; README legal notice) | Quote, paraphrase; adapt keeping Timefold's and Red Hat's notices |
| Timefold docs and blog, Gurobi docs | No licence checked; Gurobi proprietary | Brief quotes with a link; paraphrase |
| OR-Library data | MIT ("Copyright (c) (2010) (J E Beasley}") | Quote; copy files keeping the notice |
| PSPLIB, Taillard, schedulingbenchmarks.org | No licence stated | Brief quotes of figures with citation; don't redistribute the data |
| Vázquez-Serrano et al. 2021 (MDPI) | CC BY 4.0 (Crossref licence) | Quote, paraphrase, adapt with attribution and a note of changes |
| KU Leuven author copies (Smet and Vanden Berghe; Böðvarsdóttir et al.; De Bruecker et al.) | Author copies; licence not stated ("other-oa" per Semantic Scholar for Böðvarsdóttir) | Brief quotes with full citation |
| Journal papers (INFORMS, Elsevier, Springer, Wiley, Taylor & Francis, ACM, IIE) | Publisher copyright | Brief quotes with full citation and DOI; paraphrase |
| CP-SAT Primer | CC BY 4.0 (R28b verification) | Quote, paraphrase, adapt with attribution |

## Repository facts this contradicts

`git -C /home/user/claude-code-skills grep -n -i` for Timefold, OR-Library, PSPLIB, Taillard,
hint, pin, PlanningPin and MiniZinc in `skills/optimization-and-scheduling` finds these `os-` and
`pck-` Facts rows. None is now wrong:

- `os-timefold` (2.8.0) holds; R28c's 2.7.1 is stale.
- `os-timefold-editions` ("1.x EOL in early 2027"; score analysis Enterprise only) holds. R28c's
  "throughout 2026" and "Plus" don't override it: no 1.36 has shipped, and the docs name
  Enterprise.
- `pck-timefold-python` holds (the Python repository is archived).
- `pck-taillard` holds, at the mistic.iict-heig-vd.ch host the row already uses.
- `pck-psplib-open` and `pck-nrp-bounds` hold; no PSPLIB or NRP row states a licence.
- `pck-cpsat-5582` (hint) is untouched by this run.

The module has no Facts row for OR-Library, MiniZinc, the official example paths, CP-SAT or Gurobi
hints, or Timefold pinning. Two prose lines rest on claims this run touched, and neither is wrong:
- `references/plan-checking.md` lines 29-31 and its Sources row ("None stated: cite figures; don't
  copy the data") hold for Taillard, schedulingbenchmarks.org and PSPLIB. OR-Library, which the
  module doesn't name, is MIT and could be copied with its notice.
- `references/optimization-and-scheduling.md` line 45 calls hinting the last solution "our own
  practice". The `add_hint` docstring and the v9.12 note ("Feasible and complete hints should now
  be preserved after presolve") are now primary sources for it, if a row is wanted.

---

# R28c: Optimization and scheduling, second follow-up (examples, people, re-planning, benchmarks)

The biggest correction from this run concerns licences. OR-Library is not "free for research": its legal page applies the MIT licence to all its material, for any use. By contrast, this run found no licence for three other benchmark sets the skill points to (Taillard, PSPLIB and schedulingbenchmarks.org). The repository should cite and link to those three but not copy their files.

**TL;DR**
- Every target tool has official example models under a permissive licence:
  - OR-Tools `examples/python` (Apache-2.0): flexible job shop, RCPSP, shift scheduling.
  - MiniZinc Benchmarks (MIT): jobshop, flexible-jobshop, rcpsp variants, nsp, roster, on-call-rostering.
  - Gurobi modeling-examples (Apache-2.0): workforce scheduling, manpower planning, technician routing.
  - Timefold Quickstarts (Apache-2.0): employee, maintenance, food-packaging and flight-crew scheduling.
  
  The licence covers the example code only. The solvers they call are not all free; most Gurobi notebooks need a Gurobi licence to run.
- All three solvers can keep a previous plan, each in its own way:
  - CP-SAT uses solution hints (`add_hint`, optionally `fix_variables_to_their_hinted_value`).
  - Gurobi separates `VarHintVal`/`VarHintPri` (guidance) from the MIP `Start` (a known solution).
  - Timefold uses `@PlanningPin`/`@PlanningPinToIndex` plus `ProblemChange`.
  
  The literature on freezing the master production schedule (from 1987) confirms that freezing reduces nervousness, but it costs money and service level. Later studies disagree on how much.
- Timefold Solver moved to 2.x in April 2026. It now needs Java 21, removed deprecated APIs such as `PinningFilter`, and moved explainability to a paid edition. Community Edition 1.x is maintained only "throughout 2026". That is the one end-of-support event in the next 12 months this skill must flag. OR-Tools is still on v9.15 (12 Jan 2026); a v10.0 milestone exists but has no announced date.

## 1. Summary

- **OR-Tools version:** the current stable release is v9.15, released 12 January 2026 on GitHub (PyPI `ortools==9.15.6755`, 14 January 2026). No newer release was found as of 16 November 2026. A "v10.0" milestone exists on the issue tracker, with no date.
- **OR-Tools examples:** the `stable` branch has official Apache-2.0 Python examples for flexible job shop (`flexible_job_shop_sat.py`), RCPSP (`rcpsp_sat.py`) and shift scheduling (`shift_scheduling_sat.py`). This run did not confirm dedicated flow-shop, assignment or nurse-scheduling files.
- **Stale link in `rcpsp_sat.py`:** it still points to `http://www.om-db.wi.tum.de/psplib/data.html`, while PSPLIB's own navigation now uses `data.php`.
- **MiniZinc Benchmarks** (MIT licence, "Copyright (c) 2016 MiniZinc (individual authors)") include these directories: jobshop, jobshop2, flexible-jobshop, openshop, rcpsp, rcpsp-max, rcpsp-wet, mrcpsp, cyclic-rcpsp, nsp (nurse scheduling), roster and on-call-rostering. Some model files still carry older "University of Melbourne and NICTA … See the file COPYING" headers.
- **MiniZinc version:** 2.10.0 was released 23 July 2026. The online Handbook is labelled 2.10.1 (stable) and 2.10.2 (latest); the release dates of 2.10.1 and 2.10.2 were not found.
- **Gurobi modeling-examples** are "distributed under the Apache 2.0 license © Gurobi Optimization, LLC". The scheduling notebooks are Workforce Scheduling (a multi-objective MIP that includes employee fairness), Manpower Planning, and Technician Routing and Scheduling. Most run on the size-limited licence that comes with the pip package.
- **Timefold Quickstarts** are Apache-2.0 (forked from OptaPlanner Quickstarts on 20 April 2023). They include employee, maintenance, food-packaging, school-timetabling, conference, bed-allocation and flight-crew scheduling.
- **Timefold version:** Solver 2.0.0 shipped 22 April 2026. The project's news page lists Timefold Solver 2.7.1 as released 6 October 2026. Community Edition 1.x is maintained only "throughout 2026".
- **OR-Library** is hosted at `people.brunel.ac.uk/~mastjjb/jeb/info.html` and maintained by J. E. Beasley (Emeritus since December 2013). Its legal page states that the MIT licence applies to all material.
- **Other benchmark terms:** PSPLIB (TUM) says researchers "may download the benchmark sets to evaluate their algorithms" but states no licence. This run found no licence for Taillard's instance pages or schedulingbenchmarks.org.
- **Fairness in rostering:** the nurse-rostering fairness literature (Smet, Martin, Ouelhadj, Özcan, Vanden Berghe, 2012) shows that a plain weighted-sum objective lets "one nurse … have a very bad roster" while another nurse's good roster makes up the total. It proposes objectives based on the worst nurse's penalty and on the spread between nurses.
- **Worker-dependent setups:** only one located paper models setup times that depend on both the job sequence and which worker does the setup: Vázquez-Serrano, Cárdenas-Barrón and Peimbert-García (2021, *Mathematics*, CC BY 4.0). The better-known Ruiz papers vary setup time with the amount of resource assigned, not with the worker's identity.
- **Freezing costs:** freezing the master production schedule limits nervousness. But Sridharan, Berry and Udayabhanu (1987) warn it "can also produce an increase in production and inventory costs", and Zhao and Lee (1993) report lower service levels when demand is uncertain.
- **Objective weights:** guidance from the nurse-rostering literature is empirical and cautionary. In one documented practical case, raising one penalty weight to fix its violations made the roster worse overall.
- **Not found this run** (listed in section 9): guidance on dispatching rules versus solvers, property-based testing of models, Python discrete-event simulation beyond SimPy, CPLEX container/CI licensing, and a documented failure caused by treating workers as deterministic.

## 2. Corrections

| Belief | Verdict | Correct fact | Source |
|---|---|---|---|
| The OR-Tools repository ships official examples for job shop, flexible job shop, RCPSP and shift scheduling. | Partly confirmed, partly unverified | Confirmed as `examples/python/*.py` on `stable`: flexible job shop, RCPSP and shift scheduling. Job shop is confirmed only in C++ (`examples/cpp/jobshop_sat.cc`, cited by OR-Tools author Laurent Perron). This run did not confirm a Python job-shop file in `examples/python`. | github.com/google/or-tools/tree/stable/examples/python; groups.google.com/g/or-tools-discuss/c/6cNJohmh_aQ |
| MiniZinc's Handbook and its benchmark library include scheduling and rostering models. | Benchmarks confirmed; Handbook not verified | The MiniZinc Benchmarks repository (MIT) has jobshop, flexible-jobshop, openshop, rcpsp (four variants), nsp, roster and on-call-rostering directories. This run did not check scheduling content in the Handbook itself. | github.com/minizinc/minizinc-benchmarks |
| OR-Library (J. E. Beasley) is still hosted and free to use for research. | Out of date / too narrow | Still hosted at Brunel, but the terms are broader than "research": "All of the material available from OR-Library is freely available for use. As such the MIT licence, reproduced below, applies".\[1\] MIT requires keeping the copyright notice. | people.brunel.ac.uk/~mastjjb/jeb/orlib/legal.html |
| Due-date quoting trades a longer promise (lost orders, price discounts) against tardiness penalties. | Confirmed in substance; Keskinocak and Tayur sentence not found | Kaminsky and Kaya's model penalises "long lead times, missing the quoted lead times and high inventory levels". Keskinocak, Ravi and Tayur (2001) model "lead-time sensitive revenues". The exact Keskinocak and Tayur (2004) sentence was not retrieved because the chapter is paywalled. | kaminsky.ieor.berkeley.edu/Reprints/PK_OK_09.pdf; link.springer.com/chapter/10.1007/978-1-4020-7953-5_12 |
| Production-planning "nervousness" is reduced by freezing the near-term schedule. | Confirmed with a cost caveat; magnitude contested | Freezing reduces schedule changes but "can also produce an increase in production and inventory costs" (Sridharan et al. 1987). Under demand uncertainty, "a higher freezing proportion often results in a higher cost, and a lower service level" (Zhao and Lee 1993). | semanticscholar.org (Sridharan et al. 1987); dl.acm.org/doi/abs/10.1016/0272-6963(93)90022-H |

Changes since R28/R28b:
- Timefold Solver is now on 2.x (2.0.0 on 22 April 2026), not 1.x.
- `PinningFilter` is removed in 2.0.
- OR-Tools has not released since v9.15 (12 January 2026).\[2\]

## 3. Facts table

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| 1 | OR-Tools current stable | v9.15 | https://github.com/google/or-tools/releases | "v9.15 Latest … @Mizux Mizux released this 12 Jan 15:38"\[2\] | 12 Jan 2026 |
| 2 | OR-Tools PyPI build | 9.15.6755 | https://libraries.io/pypi/ortools | "9.15.6755: Jan 14, 2026" (secondary)\[3\] | 14 Jan 2026 |
| 3 | OR-Tools v9.15 adds Python 3.14 | Yes | https://github.com/google/or-tools/releases | "Add Python 3.14 support."\[2\] | 12 Jan 2026 |
| 4 | OR-Tools next major | v10.0 milestone, no date | https://github.com/google/or-tools/issues/4580 | "Milestone v10.0"\[4\] | read 16 Nov 2026 |
| 5 | OR-Tools example licence | Apache-2.0 | https://github.com/google/or-tools/blob/stable/examples/python/rcpsp_sat.py | "Licensed under the Apache License, Version 2.0"\[5\] | read 16 Nov 2026 |
| 6 | MiniZinc Benchmarks licence | MIT | https://github.com/MiniZinc/minizinc-benchmarks/blob/master/LICENSE | "MIT License Copyright (c) 2016 MiniZinc (individual authors)"\[6\] | read 16 Nov 2026 |
| 7 | MiniZinc 2.10.0 release | 23 Jul 2026 | https://www.minizinc.org/downloads/ | "MiniZinc 2.10.0 (released 23 July 2026, change log)"\[7\] | 23 Jul 2026 |
| 8 | MiniZinc 2.9.6 drops SCIP ≤7 | Yes | https://docs.minizinc.dev/en/latest/changelog.html | "Add support for SCIP 10, and remove support for SCIP 7 and earlier (issue 999)."\[8\] | read 16 Nov 2026 |
| 9 | Gurobi modeling-examples licence | Apache-2.0 | https://github.com/Gurobi/modeling-examples | "These modeling examples are distributed under the Apache 2.0 license © Gurobi Optimization, LLC"\[9\] | read 16 Nov 2026 |
| 10 | Gurobi workforce notebook | Multi-objective MIP | https://gurobi.github.io/modeling-examples/workforce/ | "The problem is formulated as a multi-objective mixed-integer-programming (MIP) model."\[10\] | read 16 Nov 2026 |
| 11 | Timefold Quickstarts licence | Apache-2.0 | https://github.com/TimefoldAI/timefold-quickstarts | "Timefold Quickstarts was forked on 20 April 2023 from OptaPlanner Quickstarts, which was entirely Apache-2.0 licensed"\[11\] | read 16 Nov 2026 |
| 12 | Timefold Solver 2.0 GA | 22 Apr 2026 | https://timefold.ai/blog/timefold-solver-2-0-release | "Timefold Solver 2.0 is available now." | 22 Apr 2026\[12\] |
| 13 | Timefold latest release seen | 2.7.1 | https://optaplanner.io/blog/2026/04/22/TimefoldSolver-2-released | "Timefold Solver 2.7.1 released Tue 6 October 2026" | 6 Oct 2026\[13\] |
| 14 | Timefold 1.x CE support | Through 2026 | https://timefold.ai/blog/introducing-timefold-solver-2-0 | "Timefold Solver Community Edition 1.x will be maintained throughout 2026 with quarterly bug-fix releases and security updates." | 20 Jan 2026\[14\] |
| 15 | Timefold 2.0 Java baseline | Java 21 | https://timefold.ai/blog/timefold-solver-2-0-upgrade-in-minutes | "Solver 2.0 moves the Java baseline from 17 to 21." | 24 Apr 2026\[15\] |
| 16 | Timefold explainability | Paid "Plus" edition from 2.0 | https://timefold.ai/blog/timefold-solver-2-0-release | "Starting with 2.0, Explainability moves to Timefold Solver Plus, a new paid edition." | 22 Apr 2026\[12\] |
| 17 | Timefold pinning | `@PlanningPin` | https://docs.timefold.ai/timefold-solver/latest/domain-modeling/modeling-planning-problems | "A pinned planning entity doesn't change during solving." | read 16 Nov 2026\[16\] |
| 18 | `PinningFilter` | Removed in 2.0 | https://docs.timefold.ai/timefold-solver/1.x/responding-to-change/responding-to-change | "PinningFilter is deprecated and will be removed in Timefold Solver 2.0."\[17\] | read 16 Nov 2026 |
| 19 | Gurobi hints | `VarHintVal`, `VarHintPri` | https://docs.gurobi.com/projects/optimizer/en/current/features/warmstart.html | "If you know a solution, you should use a MIP start to provide it to the solver."\[18\] | read 16 Nov 2026 |
| 20 | CP-SAT hint-fixing parameter | `fix_variables_to_their_hinted_value` | https://or-tools.github.io/docs/pdoc/ortools/sat/python/cp_model.html | "Adds 'var == value' as a hint to the solver." | read 16 Nov 2026\[19\] |
| 21 | OR-Library licence | MIT | https://people.brunel.ac.uk/~mastjjb/jeb/orlib/legal.html | "All of the material available from OR-Library is freely available for use. As such the MIT licence, reproduced below, applies" | read 16 Nov 2026 |
| 22 | PSPLIB terms | No licence stated | https://www.om-db.wi.tum.de/psplib/library.php | "Researchers may download the benchmark sets to evaluate their algorithms, and they may send their results to be added to the library."\[20\] | read 16 Nov 2026 |
| 23 | schedulingbenchmarks.org Instance24 | Open (LB 40438, best 40439) | https://www.schedulingbenchmarks.org/nrp/ | "All solutions are verified before being reported on this website. It is not possible to verify lower bounds."\[21\] | read 16 Nov 2026 |
| 24 | Freezing MPS cost | Cost increase possible | https://www.semanticscholar.org/paper/Freezing-the-Master-Production-Schedule-Under-Sridharan-Berry/7cae6c3d5b4dacf7e6fe9abad2e77f7eec337f04 | "While freezing the MPS can limit the number of schedule changes, it can also produce an increase in production and inventory costs." | 1987\[22\] |
| 25 | Fairness in rostering | Weighted sum hides unfairness | https://lirias.kuleuven.be/server/api/core/bitstreams/89f71da7-2dbd-4c56-93bf-25636f698206/content | "Therefore one nurse can have a very bad roster which is then compensated in the overall objective value by another nurses' high quality roster." | 2012\[23\] |
| 26 | Worker-dependent setups | Agent–machine–dependent setup model | https://api.crossref.org/works/10.3390/math9222955 | "…includes sequence and agent–machine-dependent setup times (ASUPM), considers an agent-to-machine relationship…"\[24\] | 19 Nov 2021 |
| 27 | Skill chaining | Robust cross-training | https://api.crossref.org/works/10.1287/mnsc.1030.0166 | "Our comparison shows that skill-chaining strategies have the potential to be robust and efficient methods for implementing workforce agility in serial production lines."\[25\] | 2004 |

## 4. Findings

### 4.1 Official modelling examples (Priority)

**OR-Tools (Apache-2.0).** Confirmed files on the `stable` branch:
- `examples/python/flexible_job_shop_sat.py`, with a companion test file `flexible_job_shop_sat_py_test.bintest`.
- `examples/python/rcpsp_sat.py`. It is tested against PSPLIB-style instances (`rcpsp_sat_j301_1_py_test.bintest`, `rcpsp_sat_c1510_1_py_test.bintest`, and multi-mode `mm30` and `ubo_10` variants). Its docstring reads: "Sat based solver for the RCPSP problems (see rcpsp.proto)."
- `examples/python/shift_scheduling_sat.py`. It models soft minimum/maximum constraints on shift sequences and totals, with penalty costs, and fixes some assignments ("This fixes the first 2 days of the schedule"). That makes it a ready-made example of pinning part of a plan in CP-SAT.
- Job shop: `examples/cpp/jobshop_sat.cc`, cited by Laurent Perron in the OR-Tools discussion group.\[26\]
- Not verified in this run: Python job-shop, flow-shop, assignment and nurse-scheduling files. They may live under `ortools/sat/samples/` rather than `examples/`. The receiving session should confirm exact paths before linking.
- API style differs between versions. Older revisions of `shift_scheduling_sat.py` use CamelCase (`model.NewIntVar`, `model.AddMaxEquality`); the current flexible-job-shop example uses snake_case (`solver.value`, `solver.boolean_value`). Link to `stable`, not to commit hashes.

**MiniZinc (MIT).**
- The MiniZinc Benchmarks README says: "This is a collection of MiniZinc benchmark instances including instances from the 2008-2012 MiniZinc challenges" (fork README; same text upstream).
- Scheduling and rostering directories: `jobshop`, `jobshop2`, `flexible-jobshop`, `openshop`, `evilshop`, `rcpsp`, `rcpsp-max`, `rcpsp-wet`, `mrcpsp`, `cyclic-rcpsp`, `nsp`, `roster`, `on-call-rostering`.\[27\]
- Example files: `nsp/nsp_2.mzn` ("The nurse scheduling problem consists of assigning nurses to shifts to satisfy nurses demand for each day.")\[28\] and `rcpsp/rcpsp.mzn`.
- Licence caveat: `rcpsp.mzn` carries "Copyright (C) 2009-2012 The University of Melbourne and NICTA. See the file COPYING for license information." The repository-wide MIT LICENSE (2016) appears to supersede this, but the per-file header is inconsistent. Keep both notices if adapting.
- Scheduling chapters in the Handbook: not verified in this run.

**Gurobi modeling-examples (Apache-2.0 code; a Gurobi licence is needed to run them).**
- Relevant notebooks:
  - `workforce/workforce_scheduling.ipynb`, which "minimizes the number of temporary workers your company needs to hire and maximizes employee fairness" and uses Gurobi's multiple-objectives feature.
  - `manpower_planning`
  - `technician_routing_scheduling`
  - `factory_planning_1_2`
- Running terms: "The Gurobi pip package includes a size-limited trial license equivalent to the Gurobi 'online course' license. For most of the notebooks, this restricted license is sufficient."\[9\]

**Timefold Quickstarts (Apache-2.0).**
- Use cases:
  - `quarkus-employee-scheduling` ("Schedule shifts to employees, accounting for employee availability and shift skill requirements.")
  - `quarkus-maintenance-scheduling`
  - `quarkus-food-packaging`
  - `quarkus-school-timetabling`
  - `quarkus-conference-scheduling`
  - `quarkus-bed-allocation-scheduling`
  - `quarkus-flight-crew-scheduling`
  - `quarkus-order-picking`
  - `quarkus-vehicle-routing`
- Timefold's 2.0 upgrade post says the Employee Scheduling and Order Picking quickstarts needed manual changes because the types returned by grouping functions changed in 2.0. Examples copied from branches older than April 2026 will not compile against 2.x without changes.
- The Python port carries its own warning: "Using Timefold Solver in Python is significantly slower than using Timefold Solver for Java or Kotlin."\[29\]

### 4.2 People in the plan (Priority)

**Setup times that depend on sequence and on the worker.**
- Vázquez-Serrano, Cárdenas-Barrón and Peimbert-García (2021), "Agent Scheduling in Unrelated Parallel Machines with Sequence- and Agent–Machine–Dependent Setup Time Problem", *Mathematics* 9(22):2955, DOI 10.3390/math9222955, CC BY 4.0: "Thus, this paper presents a model to schedule agents in unrelated parallel machines that includes sequence and agent–machine-dependent setup times (ASUPM), considers an agent-to-machine relationship, and seeks to minimize the maximum makespan criteria."\[24\] This is the only located model in which the worker's identity changes the setup time. The journal is less selective than EJOR, and the paper has few citations.
- Ruiz and Andrés-Romano (2011), *Int. J. Adv. Manuf. Technol.* 57(5):777–794, DOI 10.1007/s00170-011-3318-2: "The new characteristic is that the amount of setup time does not only depend on the machine and job sequence but also on the amount of resources assigned, which can vary between a minimum and a maximum."\[30\] This paper is commonly mis-cited as 2007.
- Yepes-Borrero, Perea, Ruiz and Villa (2021), *EJOR* 292:443–455, DOI 10.1016/j.ejor.2020.10.052: "These setups are performed by personnel, who are of course limited in number."\[31\]\[32\]
- Fanjul-Peyro, Perea and Ruiz (2017), *EJOR* 260(2):482–493, DOI 10.1016/j.ejor.2017.01.002. Resources are needed during processing, not during setups. The quote was taken from a repository snippet; verify it against the publisher.
- Fanjul-Peyro, Ruiz and Perea (2019), *Computers & OR* 101:173–182, DOI 10.1016/j.cor.2018.07.007. Setup times depend on the machine and job sequence only; no workers.

**Cross-training and qualification matrices.**
- Hopp, Tekin and Van Oyen (2004), *Management Science* 50(1):83–98, DOI 10.1287/mnsc.1030.0166:
  - "Two important and interrelated issues are: (a) how to decide which skill(s) are strategically most desirable for workers to gain, and (b) how to coordinate these workers to respond dynamically to congestion."
  - "Our comparison shows that skill-chaining strategies have the potential to be robust and efficient methods for implementing workforce agility in serial production lines."
- De Bruecker, Van den Bergh, Beliën and Demeulemeester (2015), *EJOR* 243(1):1–16, DOI 10.1016/j.ejor.2014.10.038: "This paper presents a review and classification of the literature regarding workforce planning problems incorporating skills." Its introduction adds: "Skill substitution and cross-training, for example, can have a positive or negative effect on performance depending on the situation."\[33\]
- For a practical model to follow, Timefold's employee-scheduling quickstart sets a skill requirement on each shift (see 4.1).

**Fairness in rostering.**
- Smet and Vanden Berghe, "A study on fairness objectives for nurse rostering" (KU Leuven):
  - "Automatically generated rosters are commonly evaluated using a weighted sum objective"
  - "Therefore one nurse can have a very bad roster which is then compensated in the overall objective value by another nurses' high quality roster."
  - The associated PATAT 2012 paper (Smet, Martin, Ouelhadj, Özcan, Vanden Berghe) opens: "In the literature on nurse rostering, the fairness of the constructed rosters has often been neglected."\[34\]
- The fairness objectives used (Vanden Berghe, CHOIR 2013 slides, secondary):
  - FO = maxₙ(qₙ): minimise the worst nurse's penalty.
  - RO = q_avg + maxₙ(qₙ) − minₙ(qₙ): penalise the spread between nurses.
- Lavygina, Welsh and Crispin (GECCO '19): "If solution quality is measured by a simple weighted sum of the constraint violations for each employee, an optimizer may produce solutions in which a small number of employees suffer a highly disproportionate share of these violations."\[35\]

### 4.3 Re-planning stability (Priority)

**Literature.**
- Sridharan, Berry and Udayabhanu (1987), "Freezing the Master Production Schedule Under Rolling Planning Horizons", *Management Science* 33(9):1137–1149:
  - "While freezing the MPS can limit the number of schedule changes, it can also produce an increase in production and inventory costs."
  - "Simulation experiment results are reported which suggest that freezing up to 50% of the planning horizon has a marginal effect on production and inventory cost under a wide range of operating conditions."
- Zhao and Lee (1993), *J. Operations Management* (DOI 10.1016/0272-6963(93)90022-H):
  - Under deterministic demand, "freezing the entire planning horizon is the best option".
  - Under demand uncertainty, "a higher freezing proportion often results in a higher cost, and a lower service level, while reducing schedule instability".
- The multi-level study "Freezing the master production schedule in multilevel material requirements planning systems under deterministic demand" (*Production Planning & Control* 7(2), 1996, DOI 10.1080/09537289608930337; abstract seen only in a Taylor & Francis search snippet) reports that "increasing the freezing proportion reduces both total inventory costs and schedule instability. This finding contradicts the finding by Sridharan et al. in single-level systems."
  - So the cost effect of freezing is **contested** between single-level and multi-level systems.
  - This result holds under deterministic demand, so it does not directly contradict Zhao and Lee (1993) on uncertain demand.
- Sridharan et al. (1988, *Decision Sciences* 19(1):147–166) introduced the standard measure of schedule instability.

**CP-SAT.**
- To keep a previous plan, hint every variable with its previous value: `model.add_hint(var, value)`. The API doc says: "Adds 'var == value' as a hint to the solver."
- Pin the frozen window with hard equalities, as `shift_scheduling_sat.py` does for its first two days.
- Elsewhere, penalise change with Boolean "changed" indicators in the objective.
- `fix_variables_to_their_hinted_value` is a solver parameter. It is useful for checking that a hint is feasible.
- Hints now survive presolve. The GitHub release v9.10 (8 May 2024) lists "Preserve hints during presolve" in its CP-SAT section. The v9.12 notes add: "Rewrote the hint transformation during presolve. Feasible and complete hints should now be preserved after presolve."
- The CP-SAT Primer (secondary) states: "CP-SAT only benefits from complete hints (all variables hinted)."

**Gurobi.** There are two distinct mechanisms:
- `Start` (MIP start) is for a known solution: "If you know a solution, you should use a MIP start to provide it to the solver."
- `VarHintVal` guides the search: "If you know that a variable is likely to have a particular value in the solution but you cannot define all variable values so that the corresponding solution is feasible, you can set the attribute VarHintVal to help Gurobi find a solution."
- `VarHintPri` expresses confidence in a hint: "Hint priorities are relative … The default hint priority for a variable is 0."
- Neither mechanism enforces stability. For that, fix the variable bounds in the frozen window and add explicit change penalties.

**Timefold.**
- `@PlanningPin` on a boolean field:\[17\] "A pinned planning entity doesn't change during solving."
- `@PlanningPinToIndex` pins part of a list variable. It was added in 1.6.0: "you can tell the solver that a certain portion of the list variable is pinned and shouldn't be moved".
- `ProblemChange` supports real-time planning.
- The continuous-planning docs define history, published and draft windows.
- Timefold's commercial field-service model documents the limit of pinning: "pinning is an all-or-nothing tool". It adds a separate "minimize disruption" penalty. That penalty is a feature of the commercial product, not of the open-source solver.

### 4.4 Benchmark sets (Priority)

| Set | Current location | Terms found | Implication for an Apache-2.0 repo |
|---|---|---|---|
| OR-Library | https://people.brunel.ac.uk/~mastjjb/jeb/info.html | MIT ("Copyright (c) (2010) (J E Beasley}")\[1\] | May copy files into the repository with the MIT notice retained. Scheduling sets: aircraft landing, common due date, flow shop, hybrid reentrant shop, job shop, lot streaming, open shop, shift minimisation personnel task, weighted tardiness.\[36\] |
| Taillard (1993, EJOR 64(2):278–285)\[37\] | http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html | Not found (page blocked automated fetch) | Link and cite; do not copy files. Copies on Zenodo exist (e.g. records 4542886, 3550553) with their own terms, which were not checked. |
| PSPLIB (Kolisch & Sprecher, EJOR 96 (1997) 205–216)\[38\] | https://www.om-db.wi.tum.de/psplib/ | No licence; research use described | Link and cite; do not copy files. Some linked papers show "FILE MISSING".\[20\] |
| schedulingbenchmarks.org (Curtois) | https://www.schedulingbenchmarks.org/nrp/ | Not found on the NRP page | Link and cite Burke & Curtois (EJOR 237(1) 2014, 71–81);\[21\] do not copy files. Instance24 is still unsolved to optimality (lower bound 40438, best known 40439). |

Citation year: PSPLIB's own site cites "Kolisch, R. and A. Sprecher (1996)", while the journal DOI 10.1016/s0377-2217(96)00170-1 records 1997.\[20\]\[38\] Use 1997 with the DOI.

### 4.5 Dispatching rules (Standard)
Not found in this run; the search budget went on the Priority questions. See section 9.

### 4.6 Due-date quoting (Standard)
- The primary chapter is Keskinocak and Tayur (2004), "Due Date Management Policies", in Simchi-Levi, Wu and Shen (eds), *Handbook of Quantitative Supply Chain Analysis*, Springer, pp. 485–554, DOI 10.1007/978-1-4020-7953-5_12.\[39\] An exact sentence on the cost of quoting short versus long was **not found** (the chapter is paywalled).
- An EJOR review calls it "The most complete review to date" of order-acceptance research. It notes that the chapter's Section 6 covers "order acceptance in the context of due-date management, including pricing decisions."
- A primary model that states the trade-off: Kaminsky and Kaya (2009, IIE Transactions): "The manufacturer is penalized for long lead times, missing the quoted lead times and high inventory levels."

### 4.7 Property-based testing of optimisation models (Standard)
Not found in this run.

### 4.8 Discrete-event simulation beyond SimPy; CPLEX containers and CI (Standard)
Not found in this run.

### 4.9 Deterministic-worker failure; objective-weight guidance (Standard)
- Failure case: not found.
- Weight guidance: Böðvarsdóttir, Smet and Vanden Berghe (2020), "Behind-the-Scenes Weight Tuning for applied nurse rostering", *Operations Research for Health Care* 26:100265, DOI 10.1016/j.orhc.2020.100265.
  - "Practitioners and researchers alike have pointed out unexpected consequences when manually adjusting objective weights."
  - They cite Petrovic and Vanden Berghe (2012) for "a practical case where an attempt to repair constraint violations by a significant increase in the corresponding weight resulted in an even worse solution, increasing violations for other constraints."
- Their alternative: set an acceptance threshold for each target and let the weights be estimated automatically.
- The companion paper (Böðvarsdóttir, Smet, Vanden Berghe and Stidsen 2021, EJOR 292(3):980–995) also covers fairness. It scales each nurse's request weights so that a roster meeting all of that nurse's requests scores the same for every nurse.

## 5. Tools

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| OR-Tools (CP-SAT) | CP/MIP/routing solver suite | 9.15 (PyPI 9.15.6755)\[3\] | 12 Jan 2026 | `pip install ortools==9.15.6755`\[3\] | none (parameters in code or `SatParameters` text) | https://github.com/google/or-tools/releases |
| MiniZinc | Solver-independent CP modelling language | 2.10.0 confirmed; Handbook shows 2.10.1/2.10.2 (dates not found) | 23 Jul 2026 (2.10.0)\[7\] | MiniZinc IDE bundle from minizinc.org/downloads | `.mpc` solver configs | https://www.minizinc.org/downloads/ |
| Timefold Solver (CE) | Java/Kotlin metaheuristic planning solver | 2.7.1 | 6 Oct 2026 | Maven `ai.timefold.solver:timefold-solver-core` | `solverConfig.xml` or `application.properties` | https://optaplanner.io/blog/2026/04/22/TimefoldSolver-2-released \[13\] |
| Timefold Quickstarts | Reference scheduling apps | tracks Solver | — | `git clone https://github.com/TimefoldAI/timefold-quickstarts.git` \[40\] | `application.properties` | https://github.com/TimefoldAI/timefold-quickstarts |
| Gurobi modeling-examples | Jupyter notebooks for gurobipy | rolling (no versions) | — | clone repo; notebooks `pip install gurobipy` | Gurobi licence file `gurobi.lic` | https://gurobi.github.io/modeling-examples/ |
| PyJobShop | CP scheduling library on CP-SAT\[41\] | not found (current) | not found | `pip install pyjobshop`\[41\] | none | https://pypi.org/project/pyjobshop/0.0.3/ |
| MiniZinc Benchmarks | Model + instance corpus | unversioned | — | `git clone https://github.com/MiniZinc/minizinc-benchmarks` | — | https://github.com/minizinc/minizinc-benchmarks |

R28b covered Gurobi Optimizer itself (Gurobi 14); it was not re-checked here.

## 6. Changing in the next 12 months

- **Timefold Solver Community Edition 1.x: maintenance ends with 2026 (FLAG: within 12 months).**
  - Timefold says 1.x will be "maintained throughout 2026 with quarterly bug-fix releases and security updates." No 2027 support was announced.
  - Any skill guidance pinned to 1.x should move to 2.x (Java 21, using the OpenRewrite migration recipe).
- **Timefold 2.x breaking changes already shipped:**
  - `PinningFilter` is removed ("deprecated and will be removed in Timefold Solver 2.0").
  - Explainability APIs moved to the paid Plus and Enterprise editions.
  - Enterprise 2.0 requires a licence key.
  - `ConstraintCollectors` return types changed from Integer to Long (per a secondary summary of the upgrade post).
- **OR-Tools v10.0:** a milestone exists on GitHub, but no release date or list of breaking changes was found. v9.15 has had no successor for ten months.
- **MiniZinc:**
  - 2.9.6 removed support for SCIP 7 and earlier.
  - 2.9.0 made `--compile` require an explicit `--solver` (marked BREAKING) and deprecated implicit conversion of enums to integers.
  - No date was found for a 2.11 or 3.0 release.
- **End-of-support dates** for OR-Tools, MiniZinc and Gurobi modeling-examples: none published (not found).

## 7. Common mistakes (including those AI coding assistants make)

1. **Getting benchmark licences wrong in either direction.** OR-Library is not "research only"; its legal page applies MIT for any use. Conversely, Taillard, PSPLIB and schedulingbenchmarks.org data are not known to be openly licensed; no licence was found.
2. **Mixing CP-SAT API styles.** Older OR-Tools examples use `NewIntVar`/`AddHint`; current Python examples use snake_case (`solver.value`, `solver.boolean_value`, `add_hint`).\[42\]\[43\] Assistants trained on old snippets mix the two.
3. **Giving CP-SAT only partial hints when re-planning.** The CP-SAT Primer (secondary): "CP-SAT only benefits from complete hints (all variables hinted)." Hint every variable from the previous plan, or fix the frozen part with constraints.
4. **Treating hints as a stability guarantee.** Hints (CP-SAT, Gurobi `VarHintVal`) guide the search but do not penalise change. Stability needs pinned bounds or explicit change costs.
5. **Using `VarHintVal` when a full previous solution exists.** Gurobi: "If you know a solution, you should use a MIP start."\[18\]
6. **Generating Timefold code with `PinningFilter` or 1.x package names.** Both were removed in 2.0; use `@PlanningPin` / `@PlanningPinToIndex`.
7. **Building weighted-sum rosters with no fairness term.** This lets one employee absorb most of the violations (Smet and Vanden Berghe; Lavygina et al.).
8. **Raising one weight to "fix" one violation.** This is documented to make the overall roster worse (Böðvarsdóttir et al., citing Petrovic and Vanden Berghe 2012).
9. **Freezing the whole horizon by default.** It reduces nervousness, but can cost money and service level when demand is uncertain (Sridharan et al. 1987; Zhao and Lee 1993).
10. **Citing Ruiz and Andrés as 2007, or as a model of worker-specific setups.** The journal paper is from 2011, and setup time there varies with the amount of resource assigned, not with which worker does it.
11. **Following the stale PSPLIB link in `rcpsp_sat.py`** (`data.html`); the site now serves `data.php`.\[5\]\[20\]

## 8. Sources and licences

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| OR-Tools repo and examples | Apache-2.0 | Yes | Yes | Yes | Keep Google LLC copyright header and Apache NOTICE; state changes |
| OR-Tools API docs (pdoc) | Apache-2.0 (generated from source) | Yes | Yes | Yes | As above |
| MiniZinc Benchmarks | MIT (per-file older NICTA headers)\[6\]\[44\] | Yes | Yes | Yes | Keep MIT notice and any per-file copyright header |
| MiniZinc site/changelog | not found | Brief | Yes | n/a | Cite URL |
| Gurobi modeling-examples | Apache-2.0 | Yes | Yes | Yes (needs Gurobi licence to run) | "© Gurobi Optimization, LLC", Apache notice |
| Gurobi reference manual | Proprietary (licence not found) | Brief | Yes | No | Cite URL |
| Timefold Quickstarts / Solver | Apache-2.0 | Yes | Yes | Yes | Keep Timefold and Red Hat (OptaPlanner) notices |
| Timefold docs and blog | not found | Brief | Yes | Small snippets only, with attribution | Cite URL |
| OR-Library data | MIT | Yes | Yes | Yes (data) | Keep "Copyright (c) (2010) J E Beasley" notice |
| PSPLIB | none stated | Brief | Yes | Do not redistribute data | Cite Kolisch & Sprecher 1997 and URL |
| Taillard instances | not found | Brief | Yes | Do not redistribute data | Cite Taillard 1993 and URL |
| schedulingbenchmarks.org | not found | Brief | Yes | Do not redistribute data | Cite Burke & Curtois 2014 and URL |
| Journal papers (Elsevier, INFORMS, Springer) | Publisher copyright | Brief | Yes | No | Full citation with DOI |
| Vázquez-Serrano et al. 2021 (MDPI) | CC BY 4.0 | Yes | Yes | Yes (adapt with credit) | Authors, title, DOI, licence, note changes |
| KU Leuven / DTU preprints | not found (author copies) | Brief | Yes | No | Full citation |
| CP-SAT Primer (d-krupke, secondary) | CC BY 4.0 ("The CP-SAT Primer is maintained by Dominik Krupke at the Algorithms Division, TU Braunschweig, and is licensed under the CC BY 4.0 license."); helper code also in MIT-licensed d-krupke/cpsat-utils | Yes | Yes | Yes (adapt with credit; cpsat-utils code under MIT) | Dominik Krupke, title, URL, CC BY 4.0, note changes |

## 9. Not found, contested, not covered

**Not found**
- Python job-shop, flow-shop, assignment and nurse-scheduling example paths in OR-Tools (not verified in this run).
- Scheduling content in the MiniZinc Handbook (not verified).
- Release dates of MiniZinc 2.10.1 and 2.10.2; current PyJobShop version.
- A licence or terms of use for Taillard's instances and schedulingbenchmarks.org; an explicit licence for PSPLIB.
- An exact sentence from Keskinocak and Tayur (2004) on the cost of quoting short versus long.
- End-of-support policies for OR-Tools, MiniZinc and Gurobi modeling-examples; a release date for OR-Tools v10.0.

**Contested**
- **Whether freezing more of the MPS raises cost.**
  - Sridharan et al. (1987) and Zhao and Lee (1993) say freezing can raise cost and lower service level under uncertainty.
  - The 1996 *Production Planning & Control* multi-level study (DOI 10.1080/09537289608930337) reports lower cost and instability with more freezing, and says this "contradicts the finding by Sridharan et al. in single-level systems".
  - That study assumes deterministic demand, so it does not directly contradict Zhao and Lee on uncertain demand.
- **PSPLIB's publication year:** 1996 on the TUM page versus 1997 in the journal record.
- **MiniZinc's current stable version:** 2.10.0 is the last dated release found, but the Handbook labels 2.10.1 "stable" and 2.10.2 "latest".

**Not covered (search budget exhausted; carry to R28d)**
- Q5: dispatching rules (EDD, SPT, critical ratio, ATC) versus solvers.
- Q7: property-based testing (Hypothesis, QuickCheck) of optimisation models.
- Q8: Python discrete-event simulation beyond SimPy (e.g. salabim, Ciw) with versions; CPLEX guidance on containers and CI licences.
- Q9: a published failure blamed on treating workers as deterministic.

Dates: sources were read on 16 November 2026. The requester gave 15 November 2026 as the current date; this run's clock read 16 November.

## Sources

1. [people.brunel.ac.uk](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/legal.html)
2. [Releases · google/or-tools · GitHub](https://github.com/google/or-tools/releases)
3. [ortools 9.15.6755 on PyPI - Libraries.io - security & maintenance data for open source software](https://libraries.io/pypi/ortools)
4. [Loader.loadNativeLibraries() taking much longer to run in v9.12-v9.15 MacOS M1 · Issue #4580 · google/or-tools · GitHub](https://github.com/google/or-tools/issues/4580)
5. [or-tools/examples/python/rcpsp\_sat.py at stable · google/or-tools · GitHub](https://github.com/google/or-tools/blob/stable/examples/python/rcpsp_sat.py)
6. [minizinc-benchmarks/LICENSE at master · MiniZinc/minizinc-benchmarks · GitHub](https://github.com/MiniZinc/minizinc-benchmarks/blob/master/LICENSE)
7. [MiniZinc - Downloads](https://www.minizinc.org/downloads/)
8. [MiniZinc Change Log — The MiniZinc Handbook 2.10.2](https://docs.minizinc.dev/en/latest/changelog.html)
9. [GitHub - Gurobi/modeling-examples: Gurobi modeling examples · GitHub](https://github.com/Gurobi/modeling-examples)
10. [Workforce Scheduling Problem](https://gurobi.github.io/modeling-examples/workforce/)
11. [timefold quickstarts](https://github.com/TimefoldAI/timefold-quickstarts)
12. [Timefold Solver 2.0: Neighborhoods API and faster solving](https://timefold.ai/blog/timefold-solver-2-0-release)
13. [OptaPlanner - Timefold Solver 2 has been released](https://optaplanner.io/blog/2026/04/22/TimefoldSolver-2-released)
14. [Timefold Solver 2.0: Cleaner API, Easier Upgrades (March 2026)](https://timefold.ai/blog/introducing-timefold-solver-2-0)
15. [Timefold Solver 2.0 upgrade: 15 projects, under 10 minutes](https://timefold.ai/blog/timefold-solver-2-0-upgrade-in-minutes)
16. [Building blocks](https://docs.timefold.ai/timefold-solver/latest/domain-modeling/modeling-planning-problems)
17. [Responding to change](https://docs.timefold.ai/timefold-solver/1.x/responding-to-change/responding-to-change)
18. [Warm Start Options - Gurobi Optimizer Reference Manual](https://docs.gurobi.com/projects/optimizer/en/current/features/warmstart.html)
19. [ortools.sat.python.cp\_model API documentation](https://or-tools.github.io/docs/pdoc/ortools/sat/python/cp_model.html)
20. [Welcome to PSPLIB](https://www.om-db.wi.tum.de/psplib/library.php)
21. [Nurse Rostering Benchmark Instances](https://www.schedulingbenchmarks.org/nrp/)
22. [Freezing the Master Production Schedule Under Rolling Planning Horizons](https://www.semanticscholar.org/paper/Freezing-the-Master-Production-Schedule-Under-Sridharan-Berry/7cae6c3d5b4dacf7e6fe9abad2e77f7eec337f04)
23. [A study on fairness objectives for nurse rostering](https://lirias.kuleuven.be/server/api/core/bitstreams/89f71da7-2dbd-4c56-93bf-25636f698206/content)
24. <https://api.crossref.org/works/10.3390/math9222955>
25. <https://api.crossref.org/works/10.1287/mnsc.1030.0166>
26. [Flexible job shop problem in python](https://groups.google.com/g/or-tools-discuss/c/6cNJohmh_aQ)
27. [GitHub - MiniZinc/minizinc-benchmarks: A suite of MiniZinc benchmarks. · GitHub](https://github.com/minizinc/minizinc-benchmarks)
28. [minizinc-benchmarks/nsp/nsp\_2.mzn at master · MiniZinc/minizinc-benchmarks · GitHub](https://github.com/MiniZinc/minizinc-benchmarks/blob/master/nsp/nsp_2.mzn)
29. [GitHub - TimefoldAI/timefold-solver-python: Timefold Solver is an AI constraint solver for Python to optimize the Vehicle Routing Problem, Employee Rostering, Maintenance Scheduling, Task Assignment, School Timetabling, Cloud Optimization, Conference Scheduling, Job Shop Scheduling, Bin Packing and many more planning problems. · GitHub](https://github.com/TimefoldAI/timefold-solver-python)
30. [Scheduling unrelated parallel machines with resource-assignable sequence-dependent setup times - The International Journal of Advanced Manufacturing Technology](https://link.springer.com/article/10.1007/s00170-011-3318-2)
31. [Reformulations and an exact algorithm for unrelated parallel machine scheduling problems with setup times](https://www.sciencedirect.com/science/article/abs/pii/S0305054818301916)
32. <https://api.crossref.org/works?query.title=Bi-objective+parallel+machine+scheduling+with+additional+resources+during+setups&rows=1&select=DOI,title,author,volume,page,issued,container-title,abstract>
33. [Workforce planning incorporating skills: State of the art](https://www.sciencedirect.com/science/article/abs/pii/S0377221714008601)
34. [Investigation of fairness measures for nurse rostering - University of Portsmouth](https://researchportal.port.ac.uk/en/publications/investigation-of-fairness-measures-for-nurse-rostering/)
35. [On fairness as a rostering objective](https://dl.acm.org/doi/abs/10.1145/3319619.3321913)
36. [OR-LIBRARY](https://people.brunel.ac.uk/~mastjjb/jeb/info.html)
37. [Scheduling instances](http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html)
38. [PSPLIB - A project scheduling problem library](https://ouci.dntb.gov.ua/en/works/96JvvrN9/)
39. [Due Date Management Policies](https://link.springer.com/chapter/10.1007/978-1-4020-7953-5_12)
40. [Python Solver for Routing and Scheduling](https://timefold.ai/blog/new-open-source-solver-python)
41. [pypi.org](https://pypi.org/project/pyjobshop/0.0.3/)
42. [or-tools/examples/python/flexible\_job\_shop\_sat.py at stable · google/or-tools · GitHub](https://github.com/google/or-tools/blob/stable/examples/python/flexible_job_shop_sat.py)
43. [or-tools/examples/python/shift\_scheduling\_sat.py at 4d057e75504a86924f60b8fcd0d16fb41a401339 · google/or-tools · GitHub](https://github.com/google/or-tools/blob/4d057e75504a86924f60b8fcd0d16fb41a401339/examples/python/shift_scheduling_sat.py)
44. [minizinc-benchmarks/rcpsp/rcpsp.mzn at master · MiniZinc/minizinc-benchmarks · GitHub](https://github.com/MiniZinc/minizinc-benchmarks/blob/master/rcpsp/rcpsp.mzn)

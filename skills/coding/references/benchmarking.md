# Benchmarking

Read this for writing a benchmark that times what you meant, deciding whether a change made code
faster or slower, reading what a harness reports (benchstat, criterion, BenchmarkDotNet,
pytest-benchmark), and catching performance regressions in CI.

Finding where the time goes, profilers, flame graphs, data structures and concurrency are
`performance-and-concurrency`'s; caches are `caching`'s. How long CI takes, and a timing test
that fails now and then, are `ci-speed`; a test that fails at random is `flaky-tests`.

## Rules

1. **Benchmark with the language's harness,** which warms up, forks fresh processes and keeps
   the compiler from deleting the work. Never time a hand-written loop.
2. **Give every result a sink,** or the compiler may delete the work you meant to time.
3. **Run both sides on one quiet machine,** with the same build flags, input and harness
   settings, and record which machine it was.
4. **Choose a run count before you start, at least 10 and ideally 20, and keep it** (fact
   `bm-benchstat-runs`).
5. **Compare medians with a non-parametric test,** never one run of each side or two bare means
   (fact `bm-benchstat-stats`). Report the spread beside the number.
6. **Never re-run until a difference turns significant** (fact `bm-benchstat-rerun`). At the
   usual 0.05, one comparison in twenty of identical code shows a difference (fact
   `bm-benchstat-alpha`).
7. **Keep a baseline you can't overwrite by accident.** With criterion, compare a branch with
   `--baseline`, not `--save-baseline` (fact `bm-criterion-baseline`).
8. **In CI, let a test over repeated samples decide.** A ratio gate is a coarse alarm, set above
   the runner's measured noise; shared runners are noisy (fact `bm-runner-noise`).

### Tools per language

| Language | Harness | Compare runs with | Facts |
|---|---|---|---|
| Python | pytest-benchmark; `timeit` for a one-off | `--benchmark-compare`, whose gate is a fixed threshold | `bm-pytest-benchmark` |
| Node.js | Not researched | Not researched | |
| .NET | BenchmarkDotNet | A `[Benchmark(Baseline = true)]` method's Ratio column | `bm-bdn`, `bm-bdn-ratio` |
| Go | `testing`, with `for b.Loop()` and `-count=20` | benchstat | `pc-go-bloop`, `bm-benchstat-stats` |
| Rust | criterion | Its saved baselines | `pc-rust-bench`, `bm-criterion-baseline` |
| JVM | JMH | Not researched | `pc-jmh` |

### The harness

- **Warm-up and forks.** A JIT runs code slowly until it compiles it, and one benchmark's state
  leaks into the next in one process. Keep JMH's default forks (fact `pc-jmh`).
- **A sink for the result:** Go's `b.Loop()` (fact `pc-go-bloop`), Rust's `std::hint::black_box`
  (fact `pc-rust-bench`), JMH's `Blackhole` or a returned value (fact `pc-jmh`).
- **Setup outside the timed part,** in the harness's setup, so the number is the code's.

### How each tool reports

| Tool | Center | Spread | Decides with | Facts |
|---|---|---|---|---|
| benchstat | Median | A confidence interval for the median | A Mann-Whitney U-test | `bm-benchstat-stats`, `bm-benchstat-alpha` |
| BenchmarkDotNet | Mean; Median too when the two differ a lot | Error, half a 99.9% confidence interval; StdDev | Ratio to a baseline method | `bm-bdn`, `bm-bdn-ratio` |
| Bencher | Its harness's output | Its harness's output | A t-test, among others | `bm-bencher` |
| github-action-benchmark | Its harness's output | None | A ratio to the previous result | `bm-gab` |

BenchmarkDotNet's Error isn't a standard error: `StdErr` is a column of its own (fact `bm-bdn`).
The old `golang.org/x/perf/benchstat` package, with means and `-delta-test`, is deprecated
(fact `bm-benchstat-old`): use the `cmd/benchstat` command.

### Catching regressions in CI

- **The decision** comes from a test over repeated samples: benchstat over 10 to 20 runs a
  side, criterion against a saved baseline, or Bencher's t-test (fact `bm-bencher`).
- **A ratio gate** compares one result with the last and has no statistics (facts `bm-gab`,
  `bm-pytest-benchmark`). Run unchanged code several times on that kind of runner first, and set
  the threshold above the spread.
- **Shared runners are noisy** (fact `bm-runner-noise`). Run base and head in the same job, on
  the same machine, so the noise hits both; gate on a dedicated runner, or let a shared one
  comment and not fail.

## Mistakes

- **One run of each side, and "12% faster".** That's noise until a test over repeated runs says
  otherwise.
- **Re-running until benchstat says significant.** Fix the run count first and keep the answer.
- **`cargo bench -- --save-baseline main` on a branch.** It overwrites main's baseline. Use
  `--baseline main`.
- **Failing CI on a 5% threshold from one run on a shared runner.** The gate fails at random and
  gets switched off.

Assistants still write these five, from older code and articles:

- **A timer around a loop,** such as `time.perf_counter()` before and after. Use the harness.
- **`for i := 0; i < b.N; i++` in a new Go benchmark.** Write `for b.Loop()`.
- **`criterion::black_box`.** Use `std::hint::black_box`.
- **benchstat's means and `-delta-test`,** from the deprecated package. Current benchstat
  reports medians and a U-test.
- **Reading BenchmarkDotNet's Error as a standard error.** It's half a 99.9% interval.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| A hand-timed benchmark | A timer around a loop; `b.N` loops in new Go | `DRIFT` | Rule 1 |
| An unused benchmark result | No `b.Loop()`, `black_box`, `Blackhole` or return | `BLOCKER` where CI gates on it, else `DRIFT` | A sink |
| A claim from one run | A speedup stated from one run per side, or means with no spread | `GAP` | Rules 4 and 5 |
| The deprecated benchstat | `golang.org/x/perf/benchstat` imported; `-delta-test` in scripts | `DRIFT` | `cmd/benchstat` |
| An overwritten baseline | `--save-baseline` with main's name in a branch job | `DRIFT` | `--baseline` |
| A ratio gate under the noise | A fail threshold with no measured runner spread behind it | `GAP` | Measure, then widen it |
| A gate that fails at random | A benchmark job failing on a shared runner with no code change | `DRIFT` | A dedicated runner, or alert only |

## Why

### The harness and a sink

- **The reason:** without warm-up you time the interpreter, and without a sink the compiler
  deletes the work (facts `pc-go-bloop`, `pc-rust-bench`, `pc-jmh`).
- **What it costs:** at JMH's defaults, about eight minutes per benchmark.
- **When to choose differently:** fewer forks while exploring, never for a number you publish.

### Run counts and a non-parametric test

- **The advice:** 10 to 20 runs a side, medians, and a test such as Mann-Whitney U, as benchstat
  does by default (facts `bm-benchstat-runs`, `bm-benchstat-stats`).
- **The reason:** timings are skewed: a garbage collection or a busy neighbor adds a long
  tail, which moves a mean and leaves a median. A test says whether the gap is bigger than the
  runs' spread. Re-running until it turns significant finds a false positive, since one
  comparison in twenty does by chance (facts `bm-benchstat-rerun`, `bm-benchstat-alpha`).
- **What others do:** BenchmarkDotNet reports a mean with a wide 99.9% interval, and the median
  only when the two differ a lot (fact `bm-bdn`); its Ratio is a distribution, with `RatioSD`
  when it's wide (fact `bm-bdn-ratio`). pytest-benchmark gates on a threshold (fact
  `bm-pytest-benchmark`).
- **What it costs:** 20 runs take 20 times as long: shorten the benchmark, not the count.
- **When to choose differently:** a change many times larger than the spread needs no test, but
  still more than one run.

### Baselines

- **The reason:** criterion's `--save-baseline` compares, then overwrites the baseline it named
  (fact `bm-criterion-baseline`). Run on a branch with main's name, it replaces main's numbers
  with the branch's, and the next comparison shows no change.
- **What it costs:** a job that saves main's baseline.

### Regressions in CI

- **The advice:** a test over repeated samples decides; a ratio is an alarm.
- **The reason:** a vendor measures more than 30% variance between runs on shared runners (fact
  `bm-runner-noise`, the vendor's own claim). A 5% gate on one run there fails at random, and a
  gate that fails at random is ignored. This repository's practice: measure the runner's noise
  before choosing a threshold.
- **What others do:** Bencher offers a t-test threshold (fact `bm-bencher`).
  github-action-benchmark alerts when a result is a set ratio worse than the last, 200% by
  default (fact `bm-gab`). pytest-benchmark fails on an expression such as `min:5%` (fact
  `bm-pytest-benchmark`).
- **What it costs:** repeated runs lengthen CI, and a dedicated runner costs money and upkeep.
- **When to choose differently:** for a small project, a wide ratio alarm that comments and
  doesn't fail catches the large regressions at little cost.

## Facts

Versions, dates and defaults, each named elsewhere in this module by its ID. The `pc-` rows
moved here from `performance-and-concurrency` and keep their IDs.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `pc-go-bloop` | Prefer `B.Loop` (Go 1.24), which keeps values alive | [testing](https://pkg.go.dev/testing) | "New benchmarks should prefer using B.Loop" and "preventing the compiler from fully optimizing away the loop body." | 2026-11-11 | 2027-05-11 |
| `pc-rust-bench` | criterion 0.8.2 (2026-02-04) takes std's `black_box`; cargo-flamegraph 0.6.15 (2026-11-02) | [criterion](https://raw.githubusercontent.com/criterion-rs/criterion.rs/master/CHANGELOG.md), [flamegraph](https://crates.io/api/v1/crates/flamegraph) | "should switch to `std::hint::black_box()`." and "\"max_stable_version\":\"0.6.15\"" | 2026-11-11 | 2027-02-11 |
| `pc-jmh` | JMH 1.37 (2023-08-03): 5 forks of 5 warm-up and 5 measured 10 s runs; `Blackhole` | [Defaults](https://raw.githubusercontent.com/openjdk/jmh/1.37/jmh-core/src/main/java/org/openjdk/jmh/runner/Defaults.java), [Blackhole](https://raw.githubusercontent.com/openjdk/jmh/1.37/jmh-core/src/main/java/org/openjdk/jmh/infra/Blackhole.java) | "MEASUREMENT_FORKS = 5;" and "preventing JIT to eliminate dependent computations." | 2026-11-11 | 2027-02-11 |
| `bm-benchstat-stats` | benchstat summarizes with medians and compares with a Mann-Whitney U-test | [benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) | "benchstat uses non-parametric statistics: median for summaries, and the Mann-Whitney U-test for A/B comparisons." | 2026-11-16 | 2027-05-16 |
| `bm-benchstat-runs` | At least 10 runs, ideally 20, the same number each time | [benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) | "Pick a number of benchmark runs (at least 10, ideally 20) and stick to it." | 2026-11-16 | 2027-05-16 |
| `bm-benchstat-alpha` | At its default threshold of 0.05, benchstat shows a difference in 5% of comparisons where there is none | [benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) | "to show a difference 5% of the time even if there is no difference." | 2026-11-16 | 2027-05-16 |
| `bm-benchstat-rerun` | Don't re-run until a change turns significant | [benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) | "rerunning your benchmarks until it reports a significant change." | 2026-11-16 | 2027-05-16 |
| `bm-benchstat-old` | The old `x/perf/benchstat` package is deprecated | [x/perf/benchstat](https://pkg.go.dev/golang.org/x/perf/benchstat) | "Package benchstat is deprecated." | 2026-11-16 | 2027-05-16 |
| `bm-criterion-baseline` | `--save-baseline` compares, then overwrites; `--baseline` compares only | [Command-line options](https://bheisler.github.io/criterion.rs/book/user_guide/command_line_options.html) | "--save-baseline <name> will compare against the named baseline, then overwrite it." and "--baseline <name> will compare against the named baseline without overwriting it." | 2026-11-16 | 2027-05-16 |
| `bm-bdn` | BenchmarkDotNet 0.15.8 (2025-11-30) is the latest stable; Error is half a 99.9% confidence interval, apart from `StdErr`; Median shows only when far from Mean | [StatisticColumn.cs](https://raw.githubusercontent.com/dotnet/BenchmarkDotNet/master/src/BenchmarkDotNet/Columns/StatisticColumn.cs), [home](https://benchmarkdotnet.org/), [NuGet](https://www.nuget.org/packages/BenchmarkDotNet) | "Half of 99.9% confidence interval" and "Standard error of all measurements" and "if we detected a vast difference between the Mean and the Median values, both columns will be presented." | 2026-11-16 | 2027-02-16 |
| `bm-bdn-ratio` | A baseline method adds a Ratio column, which is a distribution | [Baselines](https://benchmarkdotnet.org/articles/features/baselines.html) | "The ratio of two benchmarks is not a single number, it's a distribution." | 2026-11-16 | 2027-05-16 |
| `bm-pytest-benchmark` | pytest-benchmark 5.3.1 (2026-11-01); its regression gate is a threshold expression | [Usage](https://pytest-benchmark.readthedocs.io/en/latest/usage.html), [PyPI](https://pypi.org/pypi/pytest-benchmark/json) | "Fail test if performance regresses according to given EXPR (eg: min:5% or mean:0.001 for number of seconds)." | 2026-11-16 | 2027-02-16 |
| `bm-bencher` | Bencher can gate on a t-test, with an upper boundary from 0.5 to 1.0 | [Thresholds](https://bencher.dev/docs/explanation/thresholds/) | "A t-test Test Upper Boundary can be any positive decimal between 0.5 and 1.0." | 2026-11-16 | 2027-05-16 |
| `bm-runner-noise` | Bencher, a vendor, claims GitHub's runners vary by over 30% between runs | [Continuous benchmarking](https://bencher.dev/docs/explanation/continuous-benchmarking/) | "Compare this to GitHub Action Runners, which can see greater than 30% variance between runs." | 2026-11-16 | 2027-05-16 |
| `bm-gab` | github-action-benchmark alerts on a ratio to the previous result, 200% by default | [action.yml](https://raw.githubusercontent.com/benchmark-action/github-action-benchmark/master/action.yml) | "For example, 150% means that an alert happens when current benchmark result is 1.5x worse than previous" and "default: '200%'" | 2026-11-16 | 2027-02-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| [benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat), [Go testing](https://pkg.go.dev/testing) | Comparing runs, `b.Loop` | BSD-style: brief quotes, our own words otherwise |
| [Criterion.rs](https://bheisler.github.io/criterion.rs/book/), its changelog | Baselines, `black_box` | Apache-2.0 or MIT: quoted |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | Its columns and baselines | MIT: quoted |
| [pytest-benchmark](https://pytest-benchmark.readthedocs.io/) | Its gate | BSD-2-Clause: quoted |
| [Bencher](https://bencher.dev/docs/) | Its t-test, runner noise | Apache-2.0 or MIT: quoted |
| [github-action-benchmark](https://github.com/benchmark-action/github-action-benchmark) | Ratio alerts | MIT: quoted |
| [JMH](https://github.com/openjdk/jmh) | Defaults, `Blackhole` | GPLv2 with Classpath exception: brief quotes |
| [PyPI](https://pypi.org/), [crates.io](https://crates.io/), [NuGet](https://www.nuget.org/) | Versions | Facts only |

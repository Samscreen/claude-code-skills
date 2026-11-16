# Test strategy

Read this for the mix of unit, integration and end-to-end tests, the pyramid against the trophy,
what makes a test small, medium or large, how to test a command-line or desktop program, test
data and temporary directories, finding what no test covers, tests that are always skipped, and
testing with no expected output: metamorphic and differential testing.

Coverage, doubles, contract tests, runner settings and each language's tools are
`testing-patterns`; what output is checked against, `test-oracles`; hardware runs, their tiers and fault injection, `acceptance-runs`; which tests
run before a merge and how long CI takes, git-workflows' `ci-speed`. The standard's dimension 5,
*Testing and verification*, sets the gates a repository needs.

## Rules

1. **Sort each test by size and by scope, apart.** Size is what it may use: one process with
   no network or real disk, one machine with only localhost, or anywhere (fact
   `ts-google-size`). Scope is how much code it checks. A test that writes to a real disk
   isn't small, whatever its folder says.
2. **Set the mix by what your broad tests cost, not by a shape.** The pyramid assumes broad
   tests are slow and brittle; where they're fast, reliable and cheap to change, fewer narrow
   ones are needed (fact `ts-fowler-pyramid`). Judge a suite by whether its tests fail only for
   useful reasons (fact `ts-fowler-shapes`), never by a ratio.
3. **For a program with no network service, test the logic in process and the binary in a
   temporary directory.** Core logic gets small tests. The built binary runs as a medium test:
   arguments in, then stdout, stderr, the exit code and the files it wrote checked. Real
   devices, installers and other systems are a separate tier, `acceptance-runs`.
4. **Keep the real dependency where it's quick and hermetic** (fact `ts-google-mix`). Give
   each test its own temporary directory (fact `ts-tempdir`); fake the clock and the network
   behind an adapter you own; start a database in a throwaway container (fact
   `ts-testcontainers`).
5. **Build test data in the test, naming only the fields it's about.** A factory holds the
   defaults, and each test overrides what it checks (fact `ts-factory-boy`). Data is made up,
   never copied from production with people's details in it.
6. **Find what's untested from a list of what the program does, not from coverage** (fact
   `ts-google-beyonce`). Build the list from the program: its commands, options and settings.
   Tag each test with the items it exercises, and fail CI on an item with no test.
7. **Count skipped tests in every run, and fail on a test that never runs.** A skip leaves a
   green run (fact `ts-tetragon`). Keep each run's JUnit XML, and list tests skipped or absent
   in every one of the last runs.
8. **Where no oracle gives the expected output, check a relation between runs, or between
   implementations.** Metamorphic testing changes the input in a known way and checks how the
   output must change (fact `ts-metamorphic`). Differential testing feeds one input to several
   implementations and compares (fact `ts-csmith`).

### Metamorphic relations

A relation comes from the domain, not from today's output. Choose ones whose follow-up run takes
a different path through the code (fact `ts-mr-different`):

| Program | Change the input | The output must |
|---|---|---|
| A sort, search or filter | Shuffle the input; add a record that matches nothing | Stay the same |
| A parser or formatter | Add whitespace or comments it ignores; reformat its own output | Parse to the same tree |
| An encoder or converter | Decode what it encoded | Equal the original |
| A query or aggregate | Narrow the filter | Return a subset, and a count no larger |
| A numeric routine | Scale, or use an identity such as sin(x) = sin(π − x) | Change by the same rule, within a stated tolerance |

A property-based tool, from `testing-patterns`' table, generates the first input of each pair.

### Differential tests

- **Implementations written apart:** another library, a reference tool, a slow model. Two
  bindings of one library are one.
- **Inputs inside defined behavior.** Where the spec leaves a result open, implementations
  differ legitimately and every difference is noise (fact `ts-csmith`).
- **A difference is a lead.** Reduce the input, then judge each side against the spec.

## Mistakes

- **A test that sleeps, writes to the home directory or calls the network, filed as a unit
  test** in the fast tier. Move it, or give it a temporary directory and a fake.
- **A ratio such as 70/20/10 enforced as a gate.** Google's own mix is a rough guide that
  differs by team (fact `ts-google-mix`). Gate on what a change breaks.
- **One fixture file every test reads and edits,** so tests pass in one order only. Give each
  test its own data; one that depends on order is `flaky-tests`.
- **`skip` added to get CI green,** as AI assistants suggest. Each skip names its condition,
  and the run reports the total.
- **A metamorphic relation that re-runs the same input.** It checks only that the program is
  deterministic.
- **Exact comparison of floating-point output across implementations.** Set the tolerance from
  the spec before the run, never from the differences seen.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Fast tier holds slow tests | Unit tests that sleep, open sockets or write outside a temporary directory | `GAP` | Move them, or a temporary directory and a fake |
| A ratio is a gate | CI or review rules that count tests by type | `OVER` | Remove it |
| A CLI tested only in process, or only as a binary | Tests that run the built binary; tests of the logic | `GAP` | Rule 3's two kinds |
| Tests share mutable data | A fixture file or rows edited by more than one test | `GAP` | Per-test data from a factory |
| Production data in tests | Names or IDs copied from real records | `BLOCKER` | Made-up data |
| Nothing lists what's untested | A list of commands or settings matched against tests | `GAP` | Rule 6 |
| Skips go uncounted | The run's summary; skips with no condition | `GAP`; `BLOCKER` where the skipped test guards a merge | Report skips; fail on one never run |
| Computed output checked only against itself | Snapshots of results with no relation or second implementation | `GAP` | Rule 8 |

## Why

### Size, scope and the mix

- **The advice:** sort tests by size and scope; choose the mix from what broad tests cost.
- **The reason:** size decides where a test can run and how often; scope decides what a pass
  shows. Folding both into "unit" hides a slow test in the fast tier.
- **What others do, and why:** Cohn's pyramid puts most tests low because broad ones are
  expensive, and Fowler's footnote names the exception (fact `ts-fowler-pyramid`). Dodds'
  trophy has four layers, static checks at the base, and most effort on integration (fact
  `ts-dodds-trophy`). Google aims at about 80/15/5 by scope (fact `ts-google-mix`). Fowler
  calls the dispute moot: the camps mean different things by "unit test" (fact
  `ts-fowler-shapes`).
- **What it costs, and when to choose differently:** a size label per test, and a tier per
  size; a suite that runs whole on every change needs no tiers. A binary run in a temporary
  directory is usually fast and repeatable, Fowler's exception, and catches what in-process
  tests miss: arguments, exit codes, output streams.

### Test data and real dependencies

- **The advice:** real dependencies where they're quick; per-test directories; factories.
- **The reason:** a double encodes a guess about the dependency; a mock of the file system
  agrees with whatever the test assumed. Google prefers the real one, and lets a small test use
  only a hermetic in-memory filesystem (facts `ts-google-mix`, `ts-google-size`).
- **What others do, and why:** factory_boy replaces static fixtures with factories that declare
  only a test's own fields (fact `ts-factory-boy`); Testcontainers starts a real service per
  run (fact `ts-testcontainers`).
- **What it costs, and when to choose differently:** Docker in CI, and factories to keep. A
  value with three fields is built inline.

### What the suite misses

- **The advice:** a list of the program's behavior, matched against tests; skips counted.
- **The reason:** coverage can't show an option nothing sets (fact `ts-google-beyonce`). A
  public project's sensor tests were always skipped, unnoticed until each skip printed a mark
  of its own (fact `ts-tetragon`).
- **What others do, and why:** research run R06c found no tool that reports a test never run;
  the list and tags are this repository's own practice.
- **What it costs, and when to choose differently:** a tag per test and a script over run
  reports. For a handful of commands, read the tests.

### Metamorphic and differential testing

- **The advice:** with no oracle, check relations between runs, or compare implementations.
- **The reason:** an expected output can't always be worked out; a relation between outputs
  usually can. The method dates from 1998, and a 2016 survey covered 119 papers (fact
  `ts-metamorphic`). A relation is strongest when the second run takes another path (fact
  `ts-mr-different`).
- **What others do, and why:** Csmith compiled random C programs with several compilers and
  compared the results, avoiding undefined behavior, which would have made every difference
  noise (fact `ts-csmith`).
- **What it costs, and when to choose differently:** a relation checks one property, and a
  second implementation shares any misreading of the spec. Where a published reference
  exists, check against it first (`test-oracles`).

## Facts

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `ts-google-size` | Google: size and scope; small is one process, medium one machine, large anywhere; small tests use no network or disk, but may use a hermetic in-memory filesystem | [SWE at Google, ch. 11](https://abseil.io/resources/swe-book/html/ch11.html) | "two distinct dimensions for every test case: size and scope" and "small tests run in a single process, medium tests run on a single machine, and large tests run wherever they want" and "small tests aren’t allowed to access the network or disk" and "Tests are allowed to access a filesystem if they use a hermetic, in-memory implementation." | 2026-11-16 | 2027-05-16 |
| `ts-google-mix` | Google: about 80/15/5 by scope, differing by team; real dependencies where feasible | [SWE at Google, ch. 11](https://abseil.io/resources/swe-book/html/ch11.html) | "around 80% of our tests being narrow-scoped unit tests" and "every team’s mix will be a little different" and "we prefer to keep the real dependencies in place when it is feasible to do so" | 2026-11-16 | 2027-05-16 |
| `ts-google-beyonce` | Google: test what you don't want to break; coverage shows only that a line ran | [SWE at Google, ch. 11](https://abseil.io/resources/swe-book/html/ch11.html) | "test everything that you don’t want to break" and "code coverage only measures that a line was invoked, not what happened as a result" | 2026-11-16 | 2027-05-16 |
| `ts-fowler-pyramid` | Fowler (2012): Cohn's name for it; the premise has exceptions | [TestPyramid](https://martinfowler.com/bliki/TestPyramid.html) | "Test Automation Pyramid" and "If my high level tests are fast, reliable, and cheap to modify - then lower-level tests aren't needed." | 2026-11-16 | 2027-05-16 |
| `ts-fowler-shapes` | Fowler (2021): the dispute is moot; Searls: ratios distract | [Shapes of Testing](https://martinfowler.com/articles/2021-test-shapes.html) | "This makes the pyramid versus honeycomb discussion moot" and "but it's a distraction" and "only fail for useful reasons" | 2026-11-16 | 2027-05-16 |
| `ts-dodds-trophy` | Dodds: four layers; most effort on integration | [Write tests](https://kentcdodds.com/blog/write-tests); [Static vs Unit](https://kentcdodds.com/blog/static-vs-unit-vs-integration-vs-e2e-tests) | "spend most (not all, mind you) of your effort there" and "In the Testing Trophy, there are 4 types of tests." | 2026-11-16 | 2027-05-16 |
| `ts-tetragon` | Cilium Tetragon PR #1948, merged 2024-01-10 | [PR #1948](https://github.com/cilium/tetragon/pull/1948) | "our killer sensor tests were always skipped and we never noticed" | 2026-11-16 | 2027-05-16 |
| `ts-tempdir` | pytest's `tmp_path` and Go's `t.TempDir()`: a directory per test | [pytest](https://docs.pytest.org/en/stable/how-to/tmp_path.html); [Go](https://pkg.go.dev/testing) | "a temporary directory unique to each test function" and "The directory is automatically removed when the test and all its subtests complete." | 2026-11-16 | 2027-02-16 |
| `ts-factory-boy` | factory_boy 3.3.3 (2025-02-03), MIT | [factory_boy](https://factoryboy.readthedocs.io/en/stable/); [PyPI](https://pypi.org/pypi/factory-boy/json) | "while only declaring the test-specific fields" and "3.3.3" | 2026-11-16 | 2027-02-16 |
| `ts-testcontainers` | Testcontainers: Java 2.0.5, Python 4.15.0, Go v0.45.0, .NET 4.16.0, Node 12.2.1 | [Maven](https://repo1.maven.org/maven2/org/testcontainers/testcontainers/maven-metadata.xml); [PyPI](https://pypi.org/pypi/testcontainers/json); [Go](https://proxy.golang.org/github.com/testcontainers/testcontainers-go/@latest); [NuGet](https://api.nuget.org/v3-flatcontainer/testcontainers/index.json); [npm](https://registry.npmjs.org/testcontainers) | "2.0.5" and "4.15.0" and "v0.45.0" and "4.16.0" and "12.2.1" | 2026-11-16 | 2027-02-16 |
| `ts-metamorphic` | Chen, Cheung and Yiu, HKUST-CS98-01 (1998); Segura and others surveyed 119 papers | [Chen et al.](https://arxiv.org/abs/2002.12543); [Segura et al., IEEE TSE 2016](https://eprints.whiterose.ac.uk/id/eprint/110335/1/segura16-tse.pdf) | "Metamorphic Testing: A New Approach for Generating Next Test Cases" and "covering 119 papers published between 1998 and 2015" | 2026-11-16 | 2027-05-16 |
| `ts-mr-different` | A good relation's follow-up run differs from the source run | [Segura et al.](https://eprints.whiterose.ac.uk/id/eprint/110335/1/segura16-tse.pdf) | "as different as possible from the source test case" | 2026-11-16 | 2027-05-16 |
| `ts-csmith` | Csmith (PLDI 2011): several compilers, outputs compared, undefined behavior avoided | [Yang et al.](https://users.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf) | "compiles the program using several compilers, runs the executables, and compares the outputs" and "avoiding the undefined and unspecified behaviors" | 2026-11-16 | 2027-05-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| [Software Engineering at Google, ch. 11](https://abseil.io/resources/swe-book/html/ch11.html) | Size, scope, mix | CC BY-NC-ND 4.0: quoted, never adapted |
| Martin Fowler | The pyramid, the shapes dispute | © Martin Fowler: quoted, never adapted |
| Kent C. Dodds | The trophy | All rights reserved: short quotes |
| Cilium Tetragon | Skips unnoticed | Apache-2.0: short quote |
| [pytest](https://docs.pytest.org/en/stable/how-to/tmp_path.html), [Go](https://pkg.go.dev/testing), [factory_boy](https://factoryboy.readthedocs.io/en/stable/) | Directories, factories | MIT, BSD-3-Clause, MIT: short quotes |
| Chen et al.; Segura et al.; Yang et al. (linked in Facts) | Metamorphic and differential testing | Authors' and publishers' copyright: short quotes, our own words |
| Package registries | Versions | Metadata: facts only |

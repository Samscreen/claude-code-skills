# Performance and concurrency

Read this for finding why code is slow: profilers, flame graphs and data structures. It also
covers concurrent code: task lifetimes, cancellation and Go's `context`, blocking an event loop,
race detectors, free threading in Python libraries, and Java's structured concurrency.

Benchmarks and comparing runs are `benchmarking`'s, and caches `caching`'s. Each language's
async style is its language module's, such as `python-coding` or `csharp-coding`. Timeouts and
retries are `error-handling`'s; ThreadSanitizer is `c-build`'s. A test that flakes from a race
is `flaky-tests`, and a timing test in CI `ci-speed`.

## Rules

1. **Measure before you change anything for speed,** and keep the number from before to
   compare with the one after.
2. **Profile with a sampler first:** its overhead is bounded, and it attaches to a running
   process. A tracing profiler, which inflates small, hot calls, is for exact call counts.
3. **Choose wall-clock or CPU mode from the symptom:** wall-clock, which counts waiting, for slow
   responses; CPU for a busy CPU. High in wall-clock and low in CPU means waiting (fact
   `pc-py-modes`).
4. **Read a flame graph's widths, never its order:** the x-axis is alphabetical (fact
   `pc-flamegraph`).
5. **Start with an array-backed list and a hash map:** a deque for both ends, a linked list only
   when measured.
6. **Give every concurrent task an owner that waits for it:** a task group or scope, which
   cancels the rest when one fails.
7. **Treat cancellation as cooperative:** pass the token or context down, check it in long loops,
   and never swallow the cancellation error.
8. **Never block an event loop or an async runtime's thread.** CPU work goes to a worker or
   thread pool, blocking calls to the runtime's blocking pool.
9. **Run the race detector in CI, with tests that reach the concurrent paths.**
10. **Check that the GIL is off before counting on free threading** (fact `pc-py-gil-check`).

### Profilers per language

| Language | Profile | Facts |
|---|---|---|
| Python | `profiling.sampling` on 3.15, else py-spy; `profiling.tracing` for counts | `pc-py-tachyon`, `pc-py-spy` |
| Node.js | `node --cpu-prof`, not clinic.js | `pc-node-cpu-prof`, `pc-clinic` |
| .NET | dotnet-trace, dotnet-counters | `pc-dotnet-diag` |
| Go | `go tool pprof`, with the `goroutineleak` profile | `tp-go`, `pc-go-leak` |
| Rust | `cargo flamegraph` | `pc-rust-bench` |
| JVM | async-profiler | `pc-async-profiler` |

### Data structures

- **Array-backed first:** Python's `list`, Rust's `Vec` (fact `pc-rust-collections`); a deque,
  `collections.deque` or `VecDeque`, when both ends change (fact `pc-py-complexity`).
- **A hash map or set for lookups,** whose O(1) is an average: O(n) when keys collide (fact
  `pc-py-complexity`).
- **A linked list only when measured:** arrays suit the CPU cache (fact `pc-rust-collections`).

### Concurrency per language

- **Python.** `asyncio.TaskGroup`, not `gather`; re-raise `CancelledError` (fact
  `pc-py-taskgroup`).
- **Node.js.** Workers are for CPU-heavy JavaScript, not I/O (fact `pc-node-workers`).
- **C#.** `ConfigureAwait(false)` in libraries (fact `cs-configureawait`). Await a `ValueTask`
  once; pass the `CancellationToken` down, checking it in long loops (fact `pc-dotnet-async`).
- **Go.** `go test -race` (fact `pc-go-race`); the `goroutineleak` profile finds goroutines
  blocked forever (fact `pc-go-leak`). Call every `CancelFunc`, with `defer cancel()`: `go vet`
  reports a dropped one. Pass `ctx` first, never in a struct, and never `nil` (fact
  `pc-go-context`).
- **Rust.** Fix a `Send` or `Sync` error by changing the type, such as to `Arc<Mutex<T>>`, not
  with `unsafe impl`. In tokio, blocking goes to `spawn_blocking` (fact `pc-rust-async`).
- **Java.** Virtual threads are final (fact `pc-java-vt`). `StructuredTaskScope` is a preview
  in JDK 27, behind `--enable-preview`, to be final in JDK 28 unchanged (fact `pc-java-sc`):
  `StructuredTaskScope.open()` with a `Joiner`, catching `ExecutionException`.

### Free threading in libraries

- **A `cp314t` wheel doesn't keep the GIL off:** an extension that isn't ready turns it back
  on, so check `sys._is_gil_enabled()` (fact `pc-py-gil-check`). Nor is it thread safety.
- **Library support:** NumPy builds `abi3t` from 2.5.0, and pandas ships free-threaded wheels
  for Windows from 3.0.0 (fact `pc-ft-wheels`). PyO3 extensions support free threading unless
  they opt out (fact `pc-pyo3-ft`).

## Mistakes

- **Pointing Tachyon at a 3.14 process.** It needs the target's minor version: use py-spy.
- **`except asyncio.CancelledError: pass` in a coroutine.** Task groups and timeouts break.
- **`time.sleep` in `async def`, `std::thread::sleep` in a tokio task.** That thread stalls.

Assistants still write these five, from older code and articles:

- **Reading a flame graph left to right as time.** The order is alphabetical.
- **Recommending clinic.js.** It's unmaintained: use `node --cpu-prof`.
- **A linked list "for fast inserts".** Measure against a `Vec` or `list` first.
- **A `context.Context` struct field,** or `_` for the `CancelFunc`.
- **`new StructuredTaskScope.ShutdownOnFailure()` with `throwIfFailed()`,** the JDK 21 to 24
  preview, or calling it final in JDK 27. Write the JDK 27 shape.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| A speed change with no numbers | No profile or before and after | `GAP` | Rules 1 to 3 |
| A list used as a queue | `pop(0)` or `insert(0, ...)` in a loop | `DRIFT` | A deque |
| A task with no owner | A dropped `create_task` result or `Task`; a `go` nothing stops | `GAP` | A group or scope |
| Swallowed cancellation | `CancelledError` caught and not re-raised | `DRIFT` | Re-raise |
| Context misuse | `go vet`'s `lostcancel`; a `context.Context` struct field | `DRIFT` | `defer cancel()`; a parameter |
| Blocking in async code | `time.sleep`, synchronous I/O or `.Result` there | `DRIFT` | Await, or the blocking pool |
| No race detector | A Go module's CI without `-race` | `GAP` | `go test -race ./...` |
| Free threading on trust | No GIL check in a free-threaded deployment | `GAP` | `sys._is_gil_enabled()` |
| An old preview API | `ShutdownOnFailure`, `throwIfFailed` | `DRIFT` | `open()` and a `Joiner` |

## Why

### Measure first, with a sampler, in the right mode

- **The reason:** a guess optimizes code that wasn't slow; the modes tell waiting from
  computing (fact `pc-py-modes`).
- **What it costs:** a profiling run. A sampler can miss a short, rare call.
- **When to choose differently:** a tracing profiler for exact call counts.

### Owned tasks and cooperative cancellation

- **The reason:** a task nobody waits for loses its error or never ends (fact `pc-go-leak`).
  Code that never checks its token never stops (fact `pc-dotnet-async`), and a context never
  canceled leaks (fact `pc-go-context`).
- **What others do:** Java is moving to structured concurrency (fact `pc-java-sc`).
- **What it costs:** fire-and-forget gets harder, on purpose.
- **When to choose differently:** work that outlives a request gets a long-lived owner that
  stops it at shutdown.

### Data structures, event loops, race detectors and previews

- **Data structures:** most code wants `Vec` or `HashMap` (fact `pc-rust-collections`), and
  contiguous memory suits the CPU cache, which big-O ignores. A middle insert moves the tail.
- **Event loops:** tasks share a thread, so one blocking call stalls every task on it (facts
  `pc-node-workers`, `pc-rust-async`). A worker costs startup and copying.
- **Race detectors:** a silent run says nothing about code that didn't run (fact `pc-go-race`).
- **Previews:** JDK 25 and 27 each broke the last preview's code (fact `pc-java-sc`), so
  production code waits for JDK 28.
- **`Send` and `Sync`:** our practice: an `unsafe impl` turns off the data-race check.
- **Free threading:** optional, and slower for one thread (fact `pc-py-free-threading`). One
  import turns the GIL back on, and nothing fails (fact `pc-py-gil-check`): check at startup.

## Facts

Each named elsewhere in this module by its ID; `pc-rust-bench` is in `benchmarking`.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `pc-flamegraph` | A flame graph's x-axis is alphabetical, not time | [Flame graphs](https://www.brendangregg.com/flamegraphs.html) | "sorted alphabetically (it is not the passage of time)" | 2026-11-11 | 2027-05-11 |
| `pc-py-modes` | High in wall-clock and low in CPU mode means waiting | [profiling.sampling](https://docs.python.org/3/library/profiling.sampling.html) | "it is I/O-bound or waiting." | 2026-11-11 | 2027-05-11 |
| `pc-py-tachyon` | 3.15 adds Tachyon; it profiles only its own minor version | [What's new in 3.15](https://docs.python.org/3/whatsnew/3.15.html), [profiling.sampling](https://docs.python.org/3/library/profiling.sampling.html) | "(Tachyon) has been added as profiling.sampling." and "must run the same Python minor version" | 2026-11-11 | 2027-02-11 |
| `pc-py-spy` | py-spy 0.4.3 (2026-11-02) | [PyPI](https://pypi.org/pypi/py-spy/json) | "\"version\":\"0.4.3\"" | 2026-11-11 | 2027-02-11 |
| `pc-py-free-threading` | Supported but optional from 3.14; one thread runs 5 to 10% slower | [What's new in 3.14](https://docs.python.org/3/whatsnew/3.14.html) | "officially supported but still optional." and "is now roughly 5-10%" | 2026-11-16 | 2027-02-16 |
| `pc-py-gil-check` | An unready extension turns the GIL on; `sys._is_gil_enabled()` checks | [Free-threaded Python](https://docs.python.org/3/howto/free-threading-python.html) | "will re-enable the GIL." and "check whether the GIL is actually disabled in the running process." | 2026-11-16 | 2027-05-16 |
| `pc-py-taskgroup` | TaskGroup cancels the rest, `gather` doesn't; a swallowed `CancelledError` breaks it | [asyncio](https://docs.python.org/3/library/asyncio-task.html) | "TaskGroup will, while gather will not, cancel the remaining scheduled tasks." and "swallows asyncio.CancelledError." | 2026-11-11 | 2027-05-11 |
| `pc-py-complexity` | A list costs most at the front; a dict's O(1) is O(n) when keys collide | [Time complexity](https://docs.python.org/3/builtins/time-complexity.html) | "If you need to add or remove at both ends, consider using a collections.deque instead." and "instead takes O(n) time." | 2026-11-16 | 2027-05-16 |
| `pc-ft-wheels` | NumPy 2.5.5 (2026-11-15), `abi3t` from 2.5.0; pandas wheels for Windows from 3.0.0 (2026-01-21) | [NumPy 2.5.0](https://numpy.org/doc/2.5/release/2.5.0-notes.html), [PyPI](https://pypi.org/pypi/numpy/json), [pandas 3.0.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html) | "supports the stable ABI for free-threaded Python" and "Wheels are now available for free-threading Python builds on Windows" | 2026-11-16 | 2027-02-16 |
| `pc-pyo3-ft` | PyO3 0.30.1 (2026-10-14), as 0.30.0 failed to publish; opt-out from 0.28.0; `abi3t` from 0.29.0 | [CHANGELOG](https://raw.githubusercontent.com/PyO3/pyo3/v0.30.1/CHANGELOG.md) | "is now opt-out rather than opt-in." and "Support the new PEP 803 abi3t ABI" and "0.30.0 failed to push to crates.io" | 2026-11-16 | 2027-02-16 |
| `pc-node-cpu-prof` | `--cpu-prof` writes a V8 CPU profile | [Node CLI](https://nodejs.org/api/cli.html) | "writes the CPU profile to disk before exit." | 2026-11-11 | 2027-05-11 |
| `pc-clinic` | clinic.js is unmaintained | [README](https://raw.githubusercontent.com/clinicjs/node-clinic/main/README.md) | "Clinic.js is not being actively maintained." | 2026-11-11 | 2027-02-11 |
| `pc-node-workers` | Workers help CPU-bound JavaScript, not I/O | [Workers](https://nodejs.org/api/worker_threads.html) | "They do not help much with I/O-intensive work." | 2026-11-11 | 2027-05-11 |
| `pc-dotnet-diag` | dotnet-trace, dotnet-counters 10.0.750501 (2026-10-07); `dnx` runs counters | [Learn](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/dotnet-counters), [NuGet](https://www.nuget.org/packages/dotnet-trace) | "you can run dotnet-counters without permanent installation using dnx" | 2026-11-11 | 2027-02-11 |
| `pc-dotnet-async` | A `ValueTask` is awaited once; cancellation is cooperative | [ValueTask](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.valuetask?view=net-10.0), [cancellation](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads) | "may only be awaited once" and "Cancellation is cooperative" | 2026-11-11 | 2027-05-11 |
| `pc-go-race` | `-race` finds only races in code that runs | [Race detector](https://go.dev/doc/articles/race_detector) | "it can't find races in code paths that are not executed." | 2026-11-11 | 2027-05-11 |
| `pc-go-leak` | Go 1.27 made the goroutine leak profile generally available | [Go 1.27](https://go.dev/doc/go1.27) | "is now generally available." and "named goroutineleak" | 2026-11-11 | 2027-02-11 |
| `pc-go-context` | An uncalled `CancelFunc` leaks, and `go vet` checks; no context in a struct | [context](https://pkg.go.dev/context) | "Failing to call the CancelFunc leaks the child" and "The go vet tool checks that CancelFuncs are used" and "Do not store Contexts inside a struct type" | 2026-11-16 | 2027-05-16 |
| `pc-rust-collections` | `Vec` or `HashMap` for most code; a linked list rarely wins | [collections](https://doc.rust-lang.org/std/collections/index.html), [linked_list](https://doc.rust-lang.org/std/collections/linked_list/index.html) | "These two collections cover most use cases" and "array-based containers are generally faster" | 2026-11-16 | 2027-05-16 |
| `pc-rust-async` | `Send`; tokio 1.54.1 (2026-10-21) tasks must not block | [marker](https://doc.rust-lang.org/std/marker/index.html), [tokio](https://docs.rs/tokio/latest/tokio/task/) | "Types that can be transferred across thread boundaries." and "could block a thread" | 2026-11-11 | 2027-02-11 |
| `pc-async-profiler` | async-profiler 4.6 (2026-10-20) removed the HTTP server; 4.5 added JDK 27 | [Changelog](https://raw.githubusercontent.com/async-profiler/async-profiler/v4.6/CHANGELOG.md) | "#1776: Remove embedded HTTP server" and "#1765: JDK 27 support" | 2026-11-11 | 2027-02-11 |
| `pc-java-vt` | Virtual threads final in JDK 21 | [JEP 444](https://openjdk.org/jeps/444) | "finalize virtual threads in JDK 21" | 2026-11-11 | 2027-05-11 |
| `pc-java-sc` | Factories from JDK 25; `ExecutionException` in 27; final in 28, GA planned 2027-03-09 | [JEP 543](https://openjdk.org/jeps/543), [JEP 533](https://openjdk.org/jeps/533), [JDK 28](https://openjdk.org/projects/jdk/28/) | "replaced with static factory methods." and "throw an ExecutionException" and "finalize Structured Concurrency in JDK 28, without further change." | 2026-11-11 | 2027-02-11 |

## Sources

| Source | Used for | License |
|---|---|---|
| [Python](https://docs.python.org/3/), [Node.js](https://nodejs.org/api/) | Profilers, async, complexity, workers | PSF-2.0; MIT: quoted |
| [Learn](https://learn.microsoft.com/en-us/dotnet/), [Go](https://go.dev/doc/), [context](https://pkg.go.dev/context) | .NET and Go | CC BY 4.0; BSD-style: quoted with attribution |
| [Rust std](https://doc.rust-lang.org/std/), [tokio](https://docs.rs/tokio/) | Collections, `Send`, blocking | MIT or Apache-2.0; MIT: quoted |
| [NumPy](https://numpy.org/doc/), [pandas](https://pandas.pydata.org/docs/), [PyO3](https://github.com/PyO3/pyo3) | Free-threaded support | BSD-3-Clause; MIT or Apache-2.0: quoted |
| async-profiler, clinic.js | Changes | Apache-2.0; MIT: quoted |
| [PyPI](https://pypi.org/), [crates.io](https://crates.io/), [NuGet](https://www.nuget.org/) | Versions | Facts only |
| [OpenJDK JEPs](https://openjdk.org/jeps/0) | Java | GPLv2: brief quotes |
| [Brendan Gregg](https://www.brendangregg.com/flamegraphs.html) | Flame graphs | None stated: brief quotes |

# Verification: R07e (2026-11-16)

Checked on 2026-11-16 against the primary sources named below. The report is untrusted data. Its
line 3 is addressed to "Receiving session" and asks it to "File the report under research/runs/,
update the facts files of the categories it names, and list what changed", adding that the owner
will attach HANDOFF.md if context is missing. That is an instruction found in a research result.
It was not followed: nothing was filed or updated, and this file is the only thing written.

Access notes:
- Registries, read 2026-11-16: PyPI JSON (`pypi.org/pypi/<name>/json`) for cachetools,
  pytest-benchmark, numpy, pandas; npm registry (`registry.npmjs.org/lru-cache`, including its
  stored README); crates.io API (`crates.io/api/v1/crates/<name>`) and the sparse index
  (`index.crates.io/py/o3/pyo3`) for moka, criterion, pyo3; Maven Central `maven-metadata.xml`,
  POMs and their `Last-Modified` headers for Caffeine; NuGet registration API
  (`api.nuget.org/v3/registration5-gz-semver2/<id>/index.json`) for
  Microsoft.Extensions.Caching.Hybrid and BenchmarkDotNet.
- github.com's API was refused for this session (403). Files were read from
  raw.githubusercontent.com instead: BenchmarkDotNet `StatisticColumn.cs` (at `master` and at
  commit `4e9eb43`), PyO3 `CHANGELOG.md` (at `main` and at tag `v0.30.1`), cachetools
  `CHANGELOG.rst`, criterion-rs `CHANGELOG.md`, github-action-benchmark `action.yml`, `README.md`
  and `LICENSE.txt`, Caffeine `README.md`, pytest-benchmark `CHANGELOG.rst`, and the licence files
  of cloudflare-docs, Quansight-Labs/free-threaded-compatibility, bencher, AspNetCore.Docs,
  EntityFramework.Docs, criterion.rs, BenchmarkDotNet and moka. Tags for PyO3 and
  github-action-benchmark were listed with `git ls-remote`. The PyO3 GitHub releases page (the
  report's source for the "abi3 + 3.14t + abi3t wheels" advice) could not be read.
- The Python wiki's TimeComplexity URL now redirects to a stub that reads "This page has moved to
  the official Python documentation"; the report's wiki quotes were checked against
  docs.python.org/3/builtins/time-complexity.html instead.
- The VLDB paper was read from the publisher's PDF (vldb.org/pvldb/vol8/p886-vattani.pdf), not
  Semantic Scholar or ResearchGate.
- Quotes were matched character for character against tag-stripped page text, whitespace
  collapsed (the AWS jitter line's double space is in the page's `<pre>` block).
- Not checked: the moka feature-flag claim (lib.rs source), CodSpeed, JMH, JFR and DevTools (the
  report did not cover them), and the AI-assistant claims the report marks as its own judgement.

| Claim | Status | Checked against |
|---|---|---|
| Correction 1: stampedes are handled by coalescing, probabilistic early expiry or a per-key lock; AWS adds TTL jitter and soft/hard TTLs; HybridCache coalesces per instance only | verified (all primary parts; the per-key lock is in the next row) | [AWS Caching Best Practices](https://aws.amazon.com/caching/best-practices/), [Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/), [ASP.NET Core caching overview](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-10.0) |
| A per-key distributed lock (Redis `SET NX EX`) | secondary only: no Redis or Memcached page was read by the report or here | singhajit.com (report) |
| Correction 2, F1: benchstat summarises with the median and compares with the Mann-Whitney U-test | verified; the page also says it prints "the median and the confidence interval for the median" | [cmd/benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) |
| F2: at least 10, ideally 20 runs | verified | [cmd/benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) |
| F3: α 0.05 | verified. The page has literal asterisks around *expected* and uses "ɑ" (U+0251, Latin small letter alpha), not Greek α | [cmd/benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) |
| F4: don't rerun until significant | verified | [cmd/benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) |
| F5: old `x/perf/benchstat` package deprecated | verified | [x/perf/benchstat](https://pkg.go.dev/golang.org/x/perf/benchstat) |
| F6, F7: `--save-baseline` compares then overwrites; `--baseline` doesn't overwrite | verified | [Criterion.rs command-line options](https://bheisler.github.io/criterion.rs/book/user_guide/command_line_options.html) |
| F8: default is `--save-baseline base` (0.2.4, 2018-07-08) | verified with a correction: the changelog writes the flag in backticks, "Default behavior of Criterion.rs is now `--save-baseline base` which emulates the previous, user facing behavior.", under "## [0.2.4] 2018-07-08". The repository is now criterion-rs/criterion.rs | [criterion CHANGELOG](https://github.com/criterion-rs/criterion.rs/blob/master/CHANGELOG.md) (raw) |
| Correction 3, F9: BenchmarkDotNet "Error" is half of a 99.9% confidence interval; a separate `StdErr` column is the standard error | verified with a correction: the description strings are verbatim, but the quoted line exists only at commit `4e9eb43`. On `master` it reads `new StatisticColumn(Column.Error, "Half of 99.9% confidence interval",`. Quote the description string alone | [StatisticColumn.cs on master](https://github.com/dotnet/BenchmarkDotNet/blob/master/src/BenchmarkDotNet/Columns/StatisticColumn.cs), [at 4e9eb43](https://github.com/dotnet/BenchmarkDotNet/blob/4e9eb43/src/BenchmarkDotNet/Columns/StatisticColumn.cs) (raw) |
| F10: Median shown only when it differs a lot from Mean | verified | [BenchmarkDotNet home](https://benchmarkdotnet.org/) |
| Ratio, and RatioSD with a baseline | verified: "it also adds the RatioSD column (the standard deviation of the ratio distribution) in complex situations" | [Baselines](https://benchmarkdotnet.org/articles/features/baselines.html) |
| BenchmarkDotNet version "not found" | verified, added: 0.15.8 (2025-11-30T02:54Z) is the latest stable; 0.16.0-preview.2 (2026-09-23) is the newest prerelease | NuGet registration API ([package](https://www.nuget.org/packages/BenchmarkDotNet)) |
| F11: pytest-benchmark 5.3.1, 1 Nov 2026 | verified (upload 2026-11-01T03:32Z; changelog "v5.3.1 (2026-11-01)"; BSD-2-Clause; requires Python >=3.10) | [PyPI JSON](https://pypi.org/pypi/pytest-benchmark/json), [CHANGELOG](https://github.com/ionelmc/pytest-benchmark/blob/master/CHANGELOG.rst) (raw) |
| F12: 5.3.0 (2026-08-23) adds `--benchmark-precision`/`--benchmark-confidence` (secondary in the report) | verified (at the primary source): the changelog's "v5.3.0 (2026-08-23)" entry, in RST markup (double backticks around each flag) | [CHANGELOG](https://github.com/ionelmc/pytest-benchmark/blob/master/CHANGELOG.rst) (raw) |
| F13: `--benchmark-compare-fail` is a threshold expression | verified | [pytest-benchmark usage](https://pytest-benchmark.readthedocs.io/en/latest/usage.html) |
| F14: Bencher t-test upper boundary 0.5 to 1.0 | verified | [Thresholds and alerts](https://bencher.dev/docs/explanation/thresholds/) |
| F15: Bencher's bare-metal under 2% vs GitHub runners over 30% | verified, as the vendor's own claim | [What is continuous benchmarking?](https://bencher.dev/docs/explanation/continuous-benchmarking/) |
| F16: github-action-benchmark alerts on a ratio to the previous result | verified. Added: `alert-threshold` defaults to `'200%'`; `fail-threshold` defaults to `alert-threshold` and "must be equal or larger than" it. Latest tag is v1.22.2 (the report: "v1 tag, exact release not found") | [action.yml](https://github.com/benchmark-action/github-action-benchmark/blob/master/action.yml), [README](https://github.com/benchmark-action/github-action-benchmark/blob/master/README.md) (raw) |
| F17: AWS: TTL on every key except write-through ones | verified | [Caching Best Practices](https://aws.amazon.com/caching/best-practices/) |
| F18: AWS TTL jitter, ±2 minutes | verified (two spaces before the comment, as the report has it) | [Caching Best Practices](https://aws.amazon.com/caching/best-practices/) |
| F19, F20, F21: request coalescing; negative cache with a different TTL; soft and hard TTLs; dated 2019-12-05 | verified ("Published Dec 5, 2019"; author Jas Chhabra). The negative-cache and soft-TTL quotes use curly quotes and apostrophes | [Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) |
| AWS: "We have seen real-world examples in which a failure to cache negative responses led to increased failure rates and faults."; arbitrary size and TTL; libraries, Nginx and Varnish coalesce | verified | [Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) |
| F22: XFetch paper, PVLDB 8(8):886–897, 2015 | verified at the publisher's PDF: "Proceedings of the VLDB Endowment, Vol. 8, No. 8", pages 886 to 897, and the abstract sentence | [p886-vattani.pdf](https://www.vldb.org/pvldb/vol8/p886-vattani.pdf) |
| XFetch rule `time() - delta * beta * ln(rand()) >= expiry`, β = 1 (secondary in the report) | verified (at the primary source): "function XFetch(key, ttl; β = 1)" and "Time() − ∆β log(rand()) ≥ expiry"; "The parameter β defaults to 1" | [p886-vattani.pdf](https://www.vldb.org/pvldb/vol8/p886-vattani.pdf) |
| F23: Google Cloud CDN caches 404 for 120 s | verified (table row "HTTP 404 Not found 120 seconds") | [Use negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching) |
| F24: Cloudflare 404/410 edge TTL 3 min (report: excerpt only) | verified from the full page, with the cache-lock sentence | [Default cache behavior](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/) |
| F25: Cloudflare default browser TTL 4 hours | verified | [Edge and Browser Cache TTL](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/) |
| F26: HybridCache coordination is per instance | verified | [ASP.NET Core caching overview](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-10.0) |
| F27: HybridCache protects without an L2; introduced in .NET 9; supports .NET Framework 4.7.2 and .NET Standard 2.0 | verified | [Caching in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/caching), [ASP.NET Core caching overview](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-10.0) |
| HybridCache package version "not found" | verified, added: Microsoft.Extensions.Caching.Hybrid 11.0.0 (2026-11-10T23:47Z), MIT | NuGet registration API |
| F28: moka `get_with` evaluates the future once | verified | [moka::future::Cache](https://docs.rs/moka/latest/moka/future/struct.Cache.html) |
| F29, contested: moka 0.12.16 (docs.rs) vs 0.12.15 (crates.io) | verified: crates.io's `max_stable_version` is 0.12.16, published 2026-08-09T23:29Z; 0.12.15 was 2026-03-22 | [crates.io API](https://crates.io/crates/moka) |
| F30: lru-cache 11.5.3, about Sep 2026; `legacy-v10` 10.4.3 | verified: `latest` 11.5.3 published 2026-09-18T23:46Z; `legacy-v10` 10.4.3 (2024-07-09); licence BlueOak-1.0.0 | [npm registry](https://registry.npmjs.org/lru-cache) |
| F31: lru-cache "not primarily a TTL cache"; `max`, `ttl` or `maxSize` required | verified in the registry's stored README. The second quote is a code comment broken across two `//` lines | [npm registry](https://registry.npmjs.org/lru-cache) |
| F32: cachetools 8.0.0 (2026-11-06) breaking; drops 3.10, `@cached(cache=None)`, deprecated `@cachedmethod` features | verified (changelog "v8.0.0 (2026-11-06)"; PyPI upload 2026-11-07T07:30Z; `requires_python` ">=3.11"; MIT) | [CHANGELOG](https://github.com/tkem/cachetools/blob/master/CHANGELOG.rst) (raw), [PyPI JSON](https://pypi.org/pypi/cachetools/json) |
| cachetools 7.3.1 (12 Nov 2026) also published | verified with a correction: 7.3.1 uploaded 2026-11-12T21:25Z, and **7.3.2 followed on 2026-11-14** ("Properly support shallow copies of caches ... (broken since v7.3.1)"). 8.0.0 stays PyPI's latest; 7.3.2 is the newest 7.x for Python 3.10 | [PyPI JSON](https://pypi.org/pypi/cachetools/json), [CHANGELOG](https://github.com/tkem/cachetools/blob/master/CHANGELOG.rst) (raw) |
| F33, contested: Caffeine 3.2.4 (2026-05-03) vs 3.3.0/3.3.1 | verified with a correction: 3.2.4's date is right (POM 2026-05-03T00:53Z), but Maven Central's `<release>` is **3.3.1** (POM 2026-10-13T03:11Z; 3.3.0 on 2026-09-21). The README's own snippet uses 3.3.1. Apache 2.0 | [maven-metadata.xml](https://repo1.maven.org/maven2/com/github/ben-manes/caffeine/caffeine/maven-metadata.xml), [README](https://github.com/ben-manes/caffeine/blob/master/README.md) (raw) |
| Caffeine "For Java 11 or above, use 3.x otherwise use 2.x." | verified with a correction: the README has backticks, "use `3.x` otherwise use `2.x`." | [README](https://github.com/ben-manes/caffeine/blob/master/README.md) (raw) |
| F34, F35: free-threaded build supported in 3.14 (PEP 779); 5-10% single-thread penalty | verified (docs now 3.15.2) | [What's new in 3.14](https://docs.python.org/3/whatsnew/3.14.html) |
| Correction 4, F36: NumPy 2.5.0 (2026-06-21) supports PEP 803 `abi3t` | verified with a correction: the release notes read "NumPy now supports the stable ABI for free-threaded Python as described in PEP 803. (gh-31091)"; the report's "described in 803" drops a link's text. PyPI 2.5.0 upload 2026-06-21T20:56Z | [NumPy 2.5.0 release notes](https://numpy.org/doc/2.5/release/2.5.0-notes.html), [PyPI JSON](https://pypi.org/pypi/numpy/json) |
| F37: NumPy 2.5.4 (2026-10-10) is the latest | contradicted: **2.5.5 was uploaded to PyPI on 2026-11-15T21:30Z** (cp314t and cp315t wheels; requires Python >=3.12). numpy.org/news still lists 2.5.4 first; 2.5.4's date is right | [PyPI JSON](https://pypi.org/pypi/numpy/json), [NumPy news](https://numpy.org/news/) |
| NumPy 2.5 drops Python 3.11, deprecates setting `shape`, scales ufuncs better on free-threaded builds | verified; setting `dtype` is deprecated for the same reason | [NumPy 2.5.0 release notes](https://numpy.org/doc/2.5/release/2.5.0-notes.html) |
| NumPy's tracker row (report: "not captured") | verified, added: the tracker lists NumPy 2.1.0 | [Compatibility status tracking](https://py-free-threading.github.io/tracking/) |
| F38: pandas free-threaded wheels on Windows from 3.0.0 (2026-01-21); 2.3.3 Linux and macOS only | verified: the 3.0.0 sentence is verbatim; PyPI shows 2.3.3 (2025-09-29) with no Windows `t` wheels and 3.0.0 (2026-01-21) with cp313t and cp314t `win_amd64` | [What's new in 3.0.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html), [What's new in 2.3.3](https://pandas.pydata.org/docs/whatsnew/v2.3.3.html), [PyPI JSON](https://pypi.org/pypi/pandas/json) |
| pandas 3.1.1 (2026-11-04) has cp314t wheels including win_amd64 and win_arm64 | verified (upload 2026-11-04T15:05Z; BSD-3-Clause) | [PyPI JSON](https://pypi.org/pypi/pandas/json) |
| F39, F40: PyO3 0.28.0 (2026-02-01) free threading opt-out; 0.29.0 (2026-06-11) drops 3.13t | verified (changelog dates match crates.io) | [PyO3 CHANGELOG](https://github.com/PyO3/pyo3/blob/main/CHANGELOG.md) (raw), [crates.io API](https://crates.io/crates/pyo3) |
| PyO3 0.30.0 (2026-10-13) is current; supports 3.15 final; drops 3.8 | verified with a correction: the changelog's 0.30.0 entry is right, but **0.30.0 never reached crates.io**: "NB PyO3 0.30.0 failed to push to crates.io due to a CI issue, so 0.30.1 was prepared and pushed". The installable version is **0.30.1** (2026-10-14T21:19Z, MSRV 1.85) | [CHANGELOG at v0.30.1](https://github.com/PyO3/pyo3/blob/v0.30.1/CHANGELOG.md) (raw), [crates.io API](https://crates.io/crates/pyo3) |
| PyO3 `abi3t` arrived in 0.30.0 | contradicted: it is in **0.29.0**: "Support the new PEP 803 abi3t ABI with new `abi3t` and `abi3t-py315` features." | [PyO3 CHANGELOG](https://github.com/PyO3/pyo3/blob/main/CHANGELOG.md) (raw) |
| PyO3 recommends abi3 + 3.14t + abi3t wheels | unverifiable: the source is the GitHub releases page (blocked); neither the changelog nor the free-threading guide says it | n/a |
| F41 and the tracker rows (Cython 3.1.0, pandas 2.2.3, PyO3 0.23, maturin 1.7.5, matplotlib 3.9.0, cryptography 46.0.0, cffi 2.0.0, JAX 0.5.1, aiohttp 3.13.0, lxml 7.0.0, h5py 3.16.0; grpcio, brotli, cuda-python with none) | verified, with the pure-Python note | [Compatibility status tracking](https://py-free-threading.github.io/tracking/) |
| A cp314t wheel can still re-enable the GIL | secondary only (autobahn-python issue) | report |
| Python 3.10 end of life 2026-10-01 | verified (devguide row "3.10 PEP 619 end-of-life 2021-10-04 2026-10-01") | [Status of Python versions](https://devguide.python.org/versions/) |
| F42: Go context CancelFunc leak, `go vet`; don't store Contexts in structs; nil Context; Values; goroutine-safe; page for go1.27.4, 10 Nov 2026 | verified (all six sentences; "Published: Nov 10, 2026") | [context](https://pkg.go.dev/context) |
| F43: Rust "you should probably just use Vec or HashMap"; VecDeque; LinkedList | verified (all three) | [std::collections](https://doc.rust-lang.org/std/collections/index.html), [linked_list](https://doc.rust-lang.org/std/collections/linked_list/index.html) |
| Python list costs and the deque advice (wiki, from search excerpts) | verified with a correction: the wiki page has moved. The docs page reads "The largest costs come from ... If you need to add or remove at both ends, consider using a collections.deque instead." ("add or remove", not "add/remove"). It gives list pop and insert as O(n - k) | [Time complexity of operations on built-in types](https://docs.python.org/3/builtins/time-complexity.html) |
| dict O(n) "amortized worst case"; deque ends O(1) | verified with a correction: the docs page says "each of the O(1) operations below instead takes O(n) time" when every key hashes alike, without "amortized". deque isn't a built-in and isn't on that page; the collections docs say "approximately the same O(1) performance in either direction" | [Time complexity](https://docs.python.org/3/builtins/time-complexity.html), [collections](https://docs.python.org/3/library/collections.html) |
| New docs page, "In the worst case, O(1) operations instead take O(n) time" | verified (the set section; page title "Python 3.15.2 documentation") | [Time complexity](https://docs.python.org/3/builtins/time-complexity.html) |
| F44: EF Core lazy loading triggers N+1, avoid it | verified, and the "each iteration in the inner foreach" sentence | [Efficient querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying) |
| ASP.NET Core: "Do not use projection queries on collections, which can result in executing \"N + 1\" SQL queries." | verified | [Best practices](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices) |
| Split queries: single-query default, a warning on multiple collections, unique ordering with Skip/Take before EF 10 | verified | [Single vs. split queries](https://learn.microsoft.com/en-us/ef/core/querying/single-split-queries) |
| F45: `AddDbContextPool` default 1024; orthogonal to connection pooling | verified | [Advanced performance topics](https://learn.microsoft.com/en-us/ef/core/performance/advanced-performance-topics) |
| criterion 0.8.2 (date "not found") | verified, added: 2026-02-04T10:43Z, MSRV 1.86, Apache-2.0 OR MIT | [crates.io API](https://crates.io/crates/criterion) |

Counts: 49 verified (4 of them added: the BenchmarkDotNet and HybridCache versions, the NumPy
tracker row and criterion's date; 2 raised from secondary: the XFetch rule and pytest-benchmark
5.3.0), 9 verified with a correction, 2 contradicted, 1 unverifiable, 2 secondary only.

## Exact quotes for facts rows

Copied from the tag-stripped page text; straight quotes unless noted.

| Fact | URL | Quote |
|---|---|---|
| benchstat statistics | https://pkg.go.dev/golang.org/x/perf/cmd/benchstat | "By default, units use "assume=nothing", so benchstat uses non-parametric statistics: median for summaries, and the Mann-Whitney U-test for A/B comparisons." |
| benchstat run count | same | "Pick a number of benchmark runs (at least 10, ideally 20) and stick to it." |
| benchstat no rerunning | same | "If benchstat reports no statistically significant change, avoid simply rerunning your benchmarks until it reports a significant change." |
| benchstat α (non-ASCII "ɑ" U+0251; literal asterisks) | same | "By default, benchstat uses an ɑ threshold of 0.05, which means it is *expected* to show a difference 5% of the time even if there is no difference." |
| Old benchstat deprecated | https://pkg.go.dev/golang.org/x/perf/benchstat | "Package benchstat is deprecated." |
| criterion `--save-baseline` | https://bheisler.github.io/criterion.rs/book/user_guide/command_line_options.html | "--save-baseline <name> will compare against the named baseline, then overwrite it." |
| criterion `--baseline` | same | "--baseline <name> will compare against the named baseline without overwriting it." |
| BenchmarkDotNet Error | https://raw.githubusercontent.com/dotnet/BenchmarkDotNet/master/src/BenchmarkDotNet/Columns/StatisticColumn.cs | "Half of 99.9% confidence interval" |
| BenchmarkDotNet StdErr | same | "Standard error of all measurements" |
| BenchmarkDotNet Median | https://benchmarkdotnet.org/ | "By default, it always shows the Mean column, but if we detected a vast difference between the Mean and the Median values, both columns will be presented." |
| pytest-benchmark gate | https://pytest-benchmark.readthedocs.io/en/latest/usage.html | "Fail test if performance regresses according to given EXPR (eg: min:5% or mean:0.001 for number of seconds)." |
| Bencher t-test bound | https://bencher.dev/docs/explanation/thresholds/ | "A t-test Test Upper Boundary can be any positive decimal between 0.5 and 1.0." |
| github-action-benchmark ratio | https://raw.githubusercontent.com/benchmark-action/github-action-benchmark/master/action.yml | "For example, 150% means that an alert happens when current benchmark result is 1.5x worse than previous" |
| AWS TTL on all keys | https://aws.amazon.com/caching/best-practices/ | "Always apply a time to live (TTL) to all of your cache keys, except those you are updating by write-through caching." |
| AWS jitter | same | "add some randomness to your TTL" |
| AWS coalescing | https://aws.amazon.com/builders-library/caching-challenges-and-strategies/ | "To remedy this issue we use request coalescing, where the servers or external cache ensure that only one pending request is out for uncached resources." |
| AWS negative caching | same | "We have seen real-world examples in which a failure to cache negative responses led to increased failure rates and faults." |
| XFetch default | https://www.vldb.org/pvldb/vol8/p886-vattani.pdf | "The parameter β defaults to 1" (non-ASCII β) |
| HybridCache per instance | https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-10.0 | "This coordination doesn't extend to other HybridCache instances." |
| HybridCache without L2 | https://learn.microsoft.com/en-us/dotnet/core/extensions/caching | "Even without an IDistributedCache configured, HybridCache still provides in-memory caching and stampede protection." |
| moka coalescing | https://docs.rs/moka/latest/moka/future/struct.Cache.html | "Only one of the calls evaluates its future, and other calls wait for that future to resolve." |
| lru-cache TTL | https://registry.npmjs.org/lru-cache (README) | "This is not primarily a TTL cache, and does not make strong TTL guarantees." |
| cachetools 8.0.0 | https://raw.githubusercontent.com/tkem/cachetools/master/CHANGELOG.rst | "Drop Python 3.10 support (breaking change)." |
| Free threading supported | https://docs.python.org/3/whatsnew/3.14.html | "The free-threaded build of Python is now supported and no longer experimental." |
| Free-threaded penalty | same | "The performance penalty on single-threaded code in free-threaded mode is now roughly 5-10%, depending on the platform and C compiler used." |
| NumPy abi3t | https://numpy.org/doc/2.5/release/2.5.0-notes.html | "NumPy now supports the stable ABI for free-threaded Python as described in PEP 803." |
| pandas Windows wheels | https://pandas.pydata.org/docs/whatsnew/v3.0.0.html | "Wheels are now available for free-threading Python builds on Windows (in addition to the other platforms) (GH 60146)" |
| PyO3 opt-out | https://raw.githubusercontent.com/PyO3/pyo3/main/CHANGELOG.md | "Support for free-threaded Python is now opt-out rather than opt-in." |
| PyO3 0.30.0 not published | https://raw.githubusercontent.com/PyO3/pyo3/v0.30.1/CHANGELOG.md | "NB PyO3 0.30.0 failed to push to crates.io due to a CI issue, so 0.30.1 was prepared and pushed" |
| Pure Python untracked | https://py-free-threading.github.io/tracking/ | "Note that pure Python code works without changes by design, hence this page does not aim to track pure Python packages." |
| Go CancelFunc | https://pkg.go.dev/context | "Failing to call the CancelFunc leaks the child and its children until the parent is canceled." |
| Go vet | same | "The go vet tool checks that CancelFuncs are used on all control-flow paths." |
| Go struct rule | same | "Do not store Contexts inside a struct type; instead, pass a Context explicitly to each function that needs it." |
| Rust default collections | https://doc.rust-lang.org/std/collections/index.html | "To get this out of the way: you should probably just use Vec or HashMap." |
| Python list costs | https://docs.python.org/3/builtins/time-complexity.html | "If you need to add or remove at both ends, consider using a collections.deque instead." |
| Python hash worst case | same | "In the worst case, O(1) operations instead take O(n) time" |
| EF Core N+1 | https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying | "Because lazy loading makes it extremely easy to inadvertently trigger the N+1 problem, it is recommended to avoid it." |
| EF Core pool size | https://learn.microsoft.com/en-us/ef/core/performance/advanced-performance-topics | "The poolSize parameter of AddDbContextPool sets the maximum number of instances retained by the pool (defaults to 1024)." |
| Python 3.10 end of life | https://devguide.python.org/versions/ | "3.10 PEP 619 end-of-life 2021-10-04 2026-10-01" |

## Versions found from registries

Read 2026-11-16.

| Tool | Current version | Released | Source |
|---|---|---|---|
| cachetools | 8.0.0 (PyPI latest; 7.3.2 newest 7.x) | 2026-11-07T07:30Z upload (changelog 2026-11-06); 7.3.2 2026-11-14T21:19Z | PyPI JSON |
| pytest-benchmark | 5.3.1 | 2026-11-01T03:32Z | PyPI JSON |
| numpy | **2.5.5** | 2026-11-15T21:30Z | PyPI JSON |
| pandas | 3.1.1 | 2026-11-04T15:05Z | PyPI JSON |
| lru-cache | 11.5.3 (`latest`) | 2026-09-18T23:46Z | npm registry |
| moka | 0.12.16 | 2026-08-09T23:29Z | crates.io API |
| criterion | 0.8.2 | 2026-02-04T10:43Z | crates.io API |
| pyo3 | **0.30.1** (no 0.30.0 on crates.io) | 2026-10-14T21:19Z | crates.io API, sparse index |
| Caffeine | **3.3.1** | 2026-10-13T03:11Z (POM Last-Modified) | Maven Central |
| Microsoft.Extensions.Caching.Hybrid | 11.0.0 | 2026-11-10T23:47Z | NuGet registration API |
| BenchmarkDotNet | 0.15.8 stable; 0.16.0-preview.2 | 2025-11-30T02:54Z; 2026-09-23T14:36Z | NuGet registration API |
| github-action-benchmark | v1.22.2 (newest tag) | not read (tag dates need a clone) | `git ls-remote` |

## Licences

| Source | Licence as stated | What an Apache-2.0 repository may do |
|---|---|---|
| pkg.go.dev (benchstat, context) | Go source BSD-style; not re-checked this run | Quote briefly, paraphrase; adapt code keeping the BSD notice |
| criterion.rs | Apache-2.0 OR MIT (crates.io; `LICENSE-MIT`) | Quote, paraphrase, adapt with attribution |
| BenchmarkDotNet | MIT ("Copyright (c) 2013–2025 .NET Foundation and contributors") | Quote, paraphrase, adapt keeping the MIT notice |
| pytest-benchmark | BSD-2-Clause (PyPI) | Quote, paraphrase, adapt keeping the notice |
| Bencher | "Apache License, Version 2.0 ... or MIT License at your discretion", except "plus" directories (Bencher Plus License) | Quote, paraphrase, adapt non-plus code with attribution |
| github-action-benchmark | MIT ("Copyright (c) 2019 rhysd") | Quote, paraphrase, adapt keeping the notice |
| AWS pages | AWS site terms; no open licence | Quote briefly with attribution; paraphrase; no code reuse |
| Vattani et al., PVLDB 2015 | CC BY-NC-ND 3.0 Unported, "Obtain permission prior to any use beyond those covered by the license." | Quote briefly with full citation; paraphrase the algorithm; no adapted text |
| Microsoft Learn (ASP.NET Core, EF Core) | AspNetCore.Docs and EntityFramework.Docs are CC BY 4.0 ("Attribution 4.0 International") | Quote and adapt with attribution |
| Cloudflare docs | cloudflare-docs repository: CC BY 4.0 | Quote and adapt with attribution |
| Google Cloud CDN docs | "the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License" | Quote and adapt with attribution |
| moka | (MIT OR Apache-2.0) AND Apache-2.0 (crates.io) | Quote, paraphrase, adapt with attribution |
| lru-cache | BlueOak-1.0.0 (npm) | Quote, paraphrase, adapt keeping the notice |
| cachetools | MIT (PyPI `license_expression`) | Quote, paraphrase, adapt keeping the notice |
| Caffeine | Apache License, Version 2.0 (POM) | Quote, paraphrase, adapt keeping NOTICE |
| docs.python.org | Copyright PSF; code examples "dual licensed under the PSF License Version 2 and the Zero-Clause BSD license" | Quote briefly; paraphrase; adapt examples freely |
| numpy, pandas | BSD-3-Clause (numpy's wheel adds 0BSD, MIT, Zlib, CC0-1.0 parts) | Quote, paraphrase, adapt keeping the notice |
| PyO3 | MIT OR Apache-2.0 (crates.io) | Quote, paraphrase, adapt with attribution |
| py-free-threading.github.io | "MIT OR 0BSD" | Quote, paraphrase, adapt |
| doc.rust-lang.org | MIT or Apache-2.0 (not re-checked) | Quote, paraphrase, adapt with attribution |

## Repository facts this contradicts

`git grep` over `skills/coding/references/performance-and-concurrency.md`, `python-coding.md` and
`csharp-coding.md` for criterion, BenchmarkDotNet, benchstat, free threading, Python 3.10 and
cachetools, then over all of `skills/` for cachetools, pytest-benchmark, benchstat, numpy,
pandas, pyo3, moka, lru-cache, Caffeine, HybridCache, abi3t, Go 1.27.x, github-action-benchmark
and Bencher.

None is now wrong. The rows that touch this area agree with today's sources:

- `performance-and-concurrency.md`, `pc-rust-bench`: criterion 0.8.2 (2026-02-04), confirmed on
  crates.io.
- `performance-and-concurrency.md`, `pc-py-free-threading`: the quote "officially supported but
  still optional." is still on What's new in 3.14.
- `python-coding.md`, `py-eol-310`: 3.10 ended 2026-10-01, confirmed on the devguide.
- `testing-patterns.md`, `tp-go`: Go 1.27.4 (2026-11-10), matching the context page's go1.27.4.
- `csharp-coding.md` has no BenchmarkDotNet, benchstat or free-threading rows;
  `performance-and-concurrency.md` names BenchmarkDotNet in its tool table without a version.

There are no facts rows for benchstat, cachetools, pytest-benchmark, NumPy, pandas, PyO3, moka,
lru-cache, Caffeine or HybridCache. Those are gaps, not contradictions. A module that adds them
should use NumPy 2.5.5, PyO3 0.30.1 and Caffeine 3.3.1, not the report's versions.

---

# R07e: Performance, what R07c didn't reach (caching, benchmark statistics, data structures, free-threaded wheels)

All four "What we believe" items are broadly right, but three need corrections that change how a skill should be worded: benchstat now reports **medians with a Mann-Whitney U-test** (not means); BenchmarkDotNet's "Error" is **half of a 99.9% confidence interval**, not a standard error; and "NumPy and pandas publish free-threaded wheels" is true today but **platform coverage and first versions differ** (pandas only covered Windows from 3.0.0, January 2026). The stampede item is correct but incomplete: primary sources add TTL jitter, soft/hard TTLs and negative caching, and the one first-party coalescing API in .NET (HybridCache) only coalesces **within one instance**.

Run date: read on 15 November 2026 (prompt written 11 November 2026). Where a source shows no date, "read 2026-11-15" is used. Search budget ran out before Standard questions 6 (JFR, DevTools) and most of 7 could be researched; these are listed under "Not covered".

## 1. Summary

- benchstat (golang.org/x/perf/cmd/benchstat) summarises each benchmark with the **median and a confidence interval for the median**, and compares A/B with the **Mann-Whitney U-test** at α = 0.05; it recommends **at least 10, ideally 20 runs** and warns against re-running until a change looks significant.\[1\]
- The old `golang.org/x/perf/benchstat` package (mean, IQR outlier removal, `-delta-test`) is **deprecated**; skills that quote `-delta-test` or "mean ± %" describe the old tool.\[2\]\[3\]
- criterion.rs: `--save-baseline <name>` compares against the named baseline **then overwrites it**; `--baseline <name>` compares **without** overwriting; the default behaviour is `--save-baseline base`.\[4\]\[5\] Latest crate on docs.rs: 0.8.2.
- BenchmarkDotNet's default summary shows Mean, Error and StdDev; **Error = "Half of 99.9% confidence interval"**; Median is added when it differs a lot from Mean, and Ratio/RatioSD appear when a baseline is marked.\[6\]\[7\]
- pytest-benchmark 5.3.1 (1 Nov 2026) gates regressions with a **fixed threshold** (`--benchmark-compare-fail=min:5%`), not a significance test; 5.3.0 (23 Aug 2026) added `--benchmark-precision`/`--benchmark-confidence` stop rules.\[8\]\[9\]
- Bencher offers a Student's t-test threshold (`--threshold-test t_test`, boundary 0.5–1.0); github-action-benchmark alerts on a **ratio to the previous run** (`alert-threshold`, e.g. 150% = 1.5× worse) with no statistics.\[10\]\[11\]
- AWS's primary guidance: put a TTL on every key except write-through ones, **add random jitter to TTLs**, use **request coalescing** for thundering herds, use **soft and hard TTLs**, and **cache negative (error) responses** with a different TTL.\[12\]\[13\]
- Probabilistic early expiration has a primary paper: Vattani, Chierichetti, Lowenstein, "Optimal Probabilistic Cache Stampede Prevention", PVLDB 8(8):886–897, 2015 (XFetch; β = 1 default).\[14\]\[15\]
- .NET HybridCache (introduced in .NET 9; runs down to .NET Framework 4.7.2/.NET Standard 2.0) gives stampede protection, but "**This coordination doesn't extend to other HybridCache instances**" — i.e. not across servers.\[16\]\[17\]\[18\]
- Rust moka 0.12.x `get_with` coalesces: "Only one of the calls evaluates its future, and other calls wait for that future to resolve."\[19\] Node lru-cache 11.5.3 offers `fetchMethod` stale-while-revalidate but "is not primarily a TTL cache".\[20\]\[21\]\[22\]
- cachetools **8.0.0 (6 Nov 2026) is a breaking release**: drops Python 3.10, drops `@cached(cache=None)` and deprecated `@cachedmethod` features.\[23\]
- Free-threaded CPython is **officially supported since 3.14 (PEP 779)** with a stated 5–10% single-thread penalty; NumPy 2.5 (21 Jun 2026) supports the PEP 803 `abi3t` stable ABI; pandas ships cp314t wheels on all platforms including Windows since 3.0.0.\[24\]\[25\]\[26\]
- PyO3 0.28.0 (1 Feb 2026) made free-threaded support **opt-out**; 0.29.0 (11 Jun 2026) **dropped 3.13t**; 0.30.0 (13 Oct 2026) supports 3.15 final and recommends abi3 + 3.14t + abi3t wheels.\[27\]\[28\]
- Go `context`: "Failing to call the CancelFunc leaks the child and its children until the parent is canceled", and `go vet` checks CancelFuncs are used on all paths; do not store Contexts in structs (docs for go1.27.4, published 10 Nov 2026).\[29\]
- EF Core: lazy loading "make[s] it extremely easy to inadvertently trigger the N+1 problem" and is recommended against; DbContext pooling (`AddDbContextPool`, default pool size 1024) is "orthogonal to database connection pooling".\[30\]

## 2. Corrections

| Belief | Verdict | Correct fact | Source |
|---|---|---|---|
| Cache stampedes are prevented by request coalescing, probabilistic early expiry, or a lock per key. | **Confirmed, incomplete** | All three are documented. AWS adds two more first-line measures: random TTL jitter ("add some randomness to your TTL") and soft/hard TTLs that keep serving cached data when the origin fails.\[12\]\[13\] Note that coalescing in HybridCache is per instance only, so it does not stop a cross-server stampede.\[16\] A lock per key is described in secondary sources only; no primary vendor doc for it was found in this run. | aws.amazon.com/caching/best-practices; aws.amazon.com/builders-library/caching-challenges-and-strategies; learn.microsoft.com ASP.NET Core caching overview |
| benchstat (Go) compares benchmark runs with a significance test, and criterion (Rust) keeps a saved baseline to compare against. | **Confirmed, with correction on detail** | benchstat: yes — Mann-Whitney U-test, α 0.05, but it summarises with the **median** plus a confidence interval, not the mean (the mean/IQR behaviour belongs to the deprecated `x/perf/benchstat` package).\[1\]\[3\] criterion: yes — but note `--save-baseline` **overwrites** the named baseline after comparing; use `--baseline` to compare without overwriting. By default criterion compares to the previous run, saved as `base`.\[4\]\[31\] | pkg.go.dev/golang.org/x/perf/cmd/benchstat; pkg.go.dev/golang.org/x/perf/benchstat; bheisler.github.io/criterion.rs command-line options; criterion CHANGELOG |
| BenchmarkDotNet reports error and standard deviation by default. | **Confirmed, with precision** | Default summary tables show Mean, Error and StdDev. "Error" is "Half of 99.9% confidence interval" — not a standard error. Median is shown only when it differs markedly from the Mean; Ratio/RatioSD appear only with a baseline.\[6\]\[7\] No built-in significance test was found in the BenchmarkDotNet docs read in this run. | benchmarkdotnet.org home and overview; BenchmarkDotNet source, src/BenchmarkDotNet/Columns/StatisticColumn.cs (dotnet/BenchmarkDotNet commit 4e9eb43), which defines `Error` as "Half of 99.9% confidence interval" and a separate `StdErr` column as "Standard error of all measurements" |
| NumPy and pandas publish free-threaded CPython wheels. | **Confirmed, out of date in detail** | Both do. pandas 2.3.3 (29 Sep 2025) shipped free-threaded 3.14 wheels for Linux and macOS only; pandas 3.0.0 (21 Jan 2026) added Windows; pandas 3.1.1 (4 Nov 2026) has cp314t wheels including win_amd64 and win_arm64.\[24\]\[32\]\[33\] NumPy 2.5.0 (21 Jun 2026) added PEP 803 `abi3t` support and faster ufunc scaling on free-threaded builds; 2.5.4 (10 Oct 2026) is the latest listed.\[25\]\[34\] A wheel existing does not guarantee the GIL stays off.\[35\] | pandas.pydata.org whatsnew v2.3.3 and v3.0.0; pypi.org/project/pandas; numpy.org/news; NumPy 2.5.0 release notes |

## 3. Facts table

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| 1 | benchstat default statistics | Median + Mann-Whitney U | https://pkg.go.dev/golang.org/x/perf/cmd/benchstat | "By default, units use \"assume=nothing\", so benchstat uses non-parametric statistics: median for summaries, and the Mann-Whitney U-test for A/B comparisons."\[1\] | read 2026-11-15 |
| 2 | benchstat run count | ≥10, ideally 20 | same | "Pick a number of benchmark runs (at least 10, ideally 20) and stick to it."\[1\] | read 2026-11-15 |
| 3 | benchstat α | 0.05 | same | "By default, benchstat uses an ɑ threshold of 0.05, which means it is *expected* to show a difference 5% of the time even if there is no difference."\[1\] | read 2026-11-15 |
| 4 | benchstat re-run warning | Don't re-run until significant | same | "If benchstat reports no statistically significant change, avoid simply rerunning your benchmarks until it reports a significant change."\[1\] | read 2026-11-15 |
| 5 | Old benchstat package | Deprecated | https://pkg.go.dev/golang.org/x/perf/benchstat | "Package benchstat is deprecated."\[2\] | read 2026-11-15 |
| 6 | criterion `--save-baseline` | Compares then overwrites | https://bheisler.github.io/criterion.rs/book/user_guide/command_line_options.html | "--save-baseline <name> will compare against the named baseline, then overwrite it."\[4\] | read 2026-11-15 |
| 7 | criterion `--baseline` | Compares without overwrite | same | "--baseline <name> will compare against the named baseline without overwriting it."\[4\] | read 2026-11-15 |
| 8 | criterion default baseline | `base` | https://github.com/bheisler/criterion.rs/blob/master/CHANGELOG.md | "Default behavior of Criterion.rs is now --save-baseline base which emulates the previous, user facing behavior."\[5\] | 2018-07-08 (0.2.4 entry) |
| 9 | BenchmarkDotNet Error column | Half of 99.9% CI (not standard error) | https://github.com/dotnet/BenchmarkDotNet — src/BenchmarkDotNet/Columns/StatisticColumn.cs (commit 4e9eb43) | 'public static readonly IColumn Error = new StatisticColumn("Error", "Half of 99.9% confidence interval",' (the same file defines StdErr as "Standard error of all measurements") | read 2026-11-15 |
| 10 | BenchmarkDotNet Median column | Conditional | https://benchmarkdotnet.org/ | "By default, it always shows the Mean column, but if we detected a vast difference between the Mean and the Median values, both columns will be presented."\[6\] | read 2026-11-15 |
| 11 | pytest-benchmark current | 5.3.1 | https://app.readthedocs.org/projects/pytest-benchmark/downloads/pdf/latest/ | "pytest-benchmark Release 5.3.1 Ionel Cristian Măries, Nov 01, 2026" | 2026-11-01\[9\] |
| 12 | pytest-benchmark 5.3.0 | Precision/confidence stop rule | https://socket.dev/pypi/package/pytest-benchmark (secondary mirror of changelog) | "Added --benchmark-precision and --benchmark-confidence: instead of a fixed number of rounds, stop once the mean's relative margin of error falls below the given fraction." | 2026-08-23\[8\] |
| 13 | pytest-benchmark regression gate | Threshold expression | https://pytest-benchmark.readthedocs.io/_/downloads/en/latest/pdf/ | "--benchmark-compare-fail EXPR Fail test if performance regresses according to given EXPR (eg: min:5% or mean:0.001 for number of seconds)." | 2026-08-23 (5.3.0 PDF)\[36\] |
| 14 | Bencher t-test bound | 0.5–1.0 | https://bencher.dev/docs/explanation/thresholds/ | "A t-test Test Upper Boundary can be any positive decimal between 0.5 and 1.0."\[10\] | read 2026-11-15 |
| 15 | Bencher CI-noise claim (vendor) | >30% vs <2% | https://bencher.dev/docs/explanation/continuous-benchmarking/ | "Bencher offers Bare Metal Runners with less than 2% variance. Compare this to GitHub Action Runners, which can see greater than 30% variance between runs."\[37\] | read 2026-11-15 |
| 16 | github-action-benchmark threshold | Ratio to previous | https://github.com/benchmark-action/github-action-benchmark/blob/master/action.yml | "For example, 150% means that an alert happens when current benchmark result is 1.5x worse than previous"\[11\] | read 2026-11-15 |
| 17 | AWS: TTL on all keys | Yes, except write-through | https://aws.amazon.com/caching/best-practices/ | "Always apply a time to live (TTL) to all of your cache keys, except those you are updating by write-through caching."\[12\] | read 2026-11-15 |
| 18 | AWS: TTL jitter | ±2 min example | same | "ttl = 3600 + (rand() * 120)  /* +/- 2 minutes */"\[12\] | read 2026-11-15 |
| 19 | AWS: request coalescing | Remedy for thundering herd | https://aws.amazon.com/builders-library/caching-challenges-and-strategies/ | "To remedy this issue we use request coalescing, where the servers or external cache ensure that only one pending request is out for uncached resources."\[13\] | 2019-12-05 |
| 20 | AWS: negative caching | Different TTL | same | "Another option we employ is to cache the error response (that is, we use a “negative cache”) using a different TTL than positive cache entries, and propagate the error to the client."\[13\] | 2019-12-05 |
| 21 | AWS: soft/hard TTL | Serve stale on failure | same | "The client will attempt to refresh cached items based on the soft TTL, but if the downstream service is unavailable or otherwise doesn’t respond to the request, then the existing cache data will continue to be used until the hard TTL is reached."\[13\] | 2019-12-05 |
| 22 | XFetch paper | PVLDB 8(8):886–897 | https://www.semanticscholar.org/paper/Optimal-Probabilistic-Cache-Stampede-Prevention-Vattani-Chierichetti/abceccfc74a577ed06a5aeb7bebe365e9ff8946d | "In this paper we give optimal algorithms for performing such probabilistic early expirations."\[38\] | 2015-04-01 |
| 23 | Google Cloud CDN 404 negative TTL | 120 s default | https://docs.cloud.google.com/cdn/docs/using-negative-caching | "HTTP 404 \| Not found \| 120 seconds"\[39\] | read 2026-11-15 |
| 24 | Cloudflare 404/410 default edge TTL | 3 min | https://developers.cloudflare.com/cache/concepts/default-cache-behavior/ | "By default, Cloudflare caches certain HTTP response codes with the following Edge Cache TTL when a cache-control directive or expires response header are not present… 404, 410 \| 3m" | read 2026-11-15 |
| 25 | Cloudflare default browser TTL | 4 hours | https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/ | "Default Browser Cache TTL \| 4 hours \| 4 hours \| 4 hours \| 4 hours"\[40\] | read 2026-11-15 |
| 26 | HybridCache scope | Per instance | https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-10.0 | "This coordination doesn't extend to other HybridCache instances."\[16\] | read 2026-11-15 |
| 27 | HybridCache without L2 | Still protects | https://learn.microsoft.com/en-us/dotnet/core/extensions/caching | "Even without an IDistributedCache configured, HybridCache still provides in-memory caching and stampede protection."\[17\] | read 2026-11-15 |
| 28 | moka coalescing | One init per key | https://docs.rs/moka/latest/moka/future/struct.Cache.html | "Only one of the calls evaluates its future, and other calls wait for that future to resolve." | read 2026-11-15 |
| 29 | moka current | 0.12.16 | https://docs.rs/crate/moka/latest | "moka 0.12.16 - Docs.rs" (page title) | read 2026-11-15 |
| 30 | lru-cache current | 11.5.3 | https://www.npmjs.com/package/lru-cache | "11.5.3 • Public • Published 2 months ago" | read 2026-11-15\[22\] |
| 31 | lru-cache TTL caveat | No preemptive pruning | same | "This is not primarily a TTL cache, and does not make strong TTL guarantees. There is no preemptive pruning of expired items by default" | read 2026-11-15\[22\] |
| 32 | cachetools 8.0.0 | Breaking | https://github.com/tkem/cachetools/blob/master/CHANGELOG.rst | "Drop Python 3.10 support (breaking change)."\[23\] | 2026-11-06 |
| 33 | Caffeine 3.2.4 | Released | https://github.com/ben-manes/caffeine/releases/tag/v3.2.4 | "@ben-manes ben-manes released this 03 May 00:48 … v3.2.4"\[41\] | 2026-05-03 |
| 34 | Python 3.14 free-threading | Supported | https://docs.python.org/3/whatsnew/3.14.html | "The free-threaded build of Python is now supported and no longer experimental."\[26\] | read 2026-11-15 |
| 35 | Free-threaded penalty | 5–10% | same | "The performance penalty on single-threaded code in free-threaded mode is now roughly 5-10%, depending on the platform and C compiler used."\[26\] | read 2026-11-15 |
| 36 | NumPy abi3t | Supported in 2.5.0 | https://github.com/numpy/numpy/releases/tag/v2.5.0 | "NumPy now supports the stable ABI for free-threaded Python as described in 803"\[25\] | 2026-06-21 |
| 37 | NumPy latest | 2.5.4 | https://numpy.org/news/ | "NumPy 2.5.4 (release notes) – *10 Oct 2026*."\[34\] | 2026-10-10 |
| 38 | pandas Windows FT wheels | From 3.0.0 | https://pandas.pydata.org/docs/whatsnew/v3.0.0.html | "Wheels are now available for free-threading Python builds on Windows (in addition to the other platforms) (GH 60146)"\[24\] | 2026-01-21 |
| 39 | PyO3 default | Opt-out | https://pyo3.rs/main/changelog | "Support for free-threaded Python is now opt-out rather than opt-in."\[27\] | 2026-02-01 (0.28.0) |
| 40 | PyO3 drops 3.13t | 0.29.0 | same | "Drop support for Python 3.13t (3.14t and above continue to be supported; CPython declared free-threading supported starting with Python 3.14)."\[27\] | 2026-06-11 |
| 41 | Cython first FT version | 3.1.0 | https://py-free-threading.github.io/tracking/ | "\| Cython \| … \| 3.1.0 \|"\[42\] | read 2026-11-15 |
| 42 | Go context cancel leak | vet checks | https://pkg.go.dev/context | "Failing to call the CancelFunc leaks the child and its children until the parent is canceled. The go vet tool checks that CancelFuncs are used on all control-flow paths."\[29\] | 2026-11-10 (go1.27.4 page) |
| 43 | Rust collections default | Vec or HashMap | https://doc.rust-lang.org/std/collections/index.html | "To get this out of the way: you should probably just use Vec or HashMap."\[43\] | read 2026-11-15 |
| 44 | EF Core N+1 | Avoid lazy loading | https://learn.microsoft.com/ef/core/performance/efficient-querying | "Because lazy loading makes it extremely easy to inadvertently trigger the N+1 problem, it is recommended to avoid it." | read 2026-11-15\[30\] |
| 45 | EF Core pool size | 1024 default | https://learn.microsoft.com/ef/core/performance/advanced-performance-topics | "The poolSize parameter of AddDbContextPool sets the maximum number of instances retained by the pool (defaults to 1024)." | read 2026-11-15\[30\] |

## 4. Findings

### 4.1 Caching (Priority 1)

**Invalidation and expiry.** AWS's "Caching Best Practices" says to "Always apply a time to live (TTL) to all of your cache keys, except those you are updating by write-through caching", because a TTL "catches application bugs, where you forget to update or delete a given cache key". For fast-changing data it recommends "just set a short TTL of a few seconds".\[12\] The Amazon Builders' Library article (Jas Chhabra, 5 Dec 2019) warns against arbitrary values: "We want to avoid the situation where a developer arbitrarily picks some cache size and TTL values during initial implementation and then never goes back and validates their appropriateness at a later time." It recommends emitting hit/miss, cache-size and downstream-request metrics.\[13\]

**Stampedes (thundering herd).** Four primary-sourced mechanisms:
1. *TTL jitter* (AWS): "add some randomness to your TTL: ttl = 3600 + (rand() * 120)".\[12\] This prevents mass expiry of keys written together; it does not help a single hot key.\[44\]
2. *Request coalescing / single flight* (AWS Builders' Library): "only one pending request is out for uncached resources"; it notes "Some caching libraries provide support for request coalescing, and some external inline caches (such as Nginx or Varnish) do as well."\[13\]
3. *Probabilistic early expiration* (Vattani, Chierichetti, Lowenstein, PVLDB 8(8):886–897, 2015): each reader independently recomputes early with a probability that rises near expiry; the XFetch rule is `time() - delta * beta * ln(rand()) >= expiry`, with β = 1 as default (rule as reproduced in the xfetch crate docs on docs.rs, secondary).\[15\]\[45\]
4. *Soft/hard TTL* (AWS): serve cached data past the soft TTL while the origin is unavailable, up to the hard TTL.\[13\]

A per-key distributed lock (e.g. Redis `SET NX EX`) appears widely in secondary sources;\[46\] no Redis or Memcached primary page was retrieved in this run, so it is listed under "Not found".

**Negative caching.** AWS: cache the error "using a different TTL than positive cache entries", and "We have seen real-world examples in which a failure to cache negative responses led to increased failure rates and faults."\[13\] CDNs do this by default: Google Cloud CDN caches 404 for 120 s by default when negative caching is on; Cloudflare's own "Default cache behavior" page (developers.cloudflare.com/cache/concepts/default-cache-behavior/) says it "caches certain HTTP response codes with the following Edge Cache TTL when a cache-control directive or expires response header are not present", listing "404, 410 | 3m", and the same page notes that "Cloudflare uses a cache lock to avoid sending duplicate requests to your origin" (per data centre). Cloudflare's default Browser Cache TTL is 4 hours on all plans.\[40\]

**In-process cache libraries.**

| Language | Library | Current version (date) | Stampede/coalescing | Notes |
|---|---|---|---|---|
| Python | `functools.lru_cache` / `cache` | Ships with CPython; docs are at 3.15.2 | Not documented as coalescing (not verified this run) | No TTL. |
| Python | cachetools | 8.0.0 (6 Nov 2026); 7.3.1 (12 Nov 2026) also published\[23\]\[47\] | Not found in sources read | 8.0.0 drops Python 3.10 and `@cached(cache=None)`; "Return callable objects instead of functions from @cached" (potentially breaking).\[23\] |
| Node | lru-cache | 11.5.3 (npm "2 months ago" ≈ Sep 2026); `legacy-v10` = 10.4.3 | `fetch()` with `fetchMethod` gives stale-while-revalidate\[48\] | "At least one of 'max', 'ttl', or 'maxSize' is required, to prevent unsafe unbounded storage."\[49\] Expired items are not pruned preemptively.\[21\]\[48\]\[50\] |
| .NET | `IMemoryCache` (Microsoft.Extensions.Caching.Memory) | Version not found | No coalescing documented on the pages read | Single-server.\[17\] |
| .NET | `HybridCache` (Microsoft.Extensions.Caching.Hybrid) | Introduced with .NET 9;\[17\] package version not found | Yes, per instance\[16\] | L1 in-memory + optional `IDistributedCache` L2; tag invalidation.\[51\] |
| Go | — | Not found | — | No Go cache library researched (search budget). |
| Rust | moka | 0.12.16 (docs.rs) | Yes: `get_with`, `try_get_with`, `optionally_get_with`\[19\]\[52\] | Features `sync` or `future` required.\[53\] |
| Java | Caffeine | **Contested**: 3.2.4 (GitHub, 3 May 2026) vs 3.3.0/3.3.1 listed on javadoc.io\[41\]\[54\] | `LoadingCache`, `refreshAfterWrite` async refresh\[55\] | Apache 2.0; "For Java 11 or above, use 3.x otherwise use 2.x."\[56\]\[57\] |

**Position:** default to a library with built-in per-key coalescing (HybridCache, moka `get_with`, Caffeine `LoadingCache`, lru-cache `fetch`) instead of hand-written get-then-set; always add TTL jitter; add a distributed lock or early refresh only for hot keys shared across many servers, because HybridCache's coalescing is per instance.

### 4.2 Comparing benchmark runs (Priority 2)

**Guidance on noise, run counts, spread versus means.** The most explicit primary guidance is benchstat's: run at least 10, ideally 20 times; use medians and non-parametric tests by default (`assume=nothing`); α = 0.05 means about 1 in 20 comparisons will flag a difference that isn't real; never re-run until the result turns significant.\[1\] Bencher (vendor, treat as marketing) claims GitHub-hosted runners "can see greater than 30% variance between runs" against under 2% on its bare-metal runners;\[37\] the direction is consistent with benchstat's guidance, but the numbers are the vendor's own.

**How each harness reports and compares.**

| Harness | Summary statistic | Spread shown | Comparison | Significance test? |
|---|---|---|---|---|
| benchstat (Go) | Median | CI for the median | A/B or more columns | Yes — Mann-Whitney U (default); `assume` metadata can change it\[1\] |
| criterion.rs | Statistical estimate with CI (detail not re-verified) | CI | Previous run (`base`) or named baseline\[31\] | Yes, reports change detection (not re-verified this run; see R07c) |
| BenchmarkDotNet | Mean (Median when skewed) | Error (half 99.9% CI), StdDev; RatioSD with baseline | Ratio to `[Benchmark(Baseline = true)]`\[58\] | Not found in default output |
| JMH | Not covered | — | — | — |
| pytest-benchmark 5.3.1 | min, max, mean, stddev, median, IQR… | Yes | `--benchmark-compare`, `pytest-benchmark compare 0001 0002`, `compare --between` | No — threshold only (`--benchmark-compare-fail=mean:5%`)\[8\]\[9\]\[59\] |

**CI regression catching.**
- **Bencher**: `bencher run --threshold-test t_test --threshold-upper-boundary 0.99 --error-on-alert ...`; also a `percentage` test for relative comparison. Use `--start-point-clone-thresholds` so feature branches compare against `main`.\[60\]\[61\]
- **github-action-benchmark** (`benchmark-action/github-action-benchmark@v1`): compares to the previous stored result by ratio; `alert-threshold` (e.g. "150%"), `fail-on-alert`, `fail-threshold` (defaults to `alert-threshold`; must be ≥ it).\[11\]\[62\] There is no statistical test, so on shared runners it is noise-prone.
- **CodSpeed**: not found (search budget).
- **pytest-benchmark** alone: `--benchmark-compare-fail` gates at a fixed percentage.\[59\]

**Position:** to decide whether a change is real, use a tool that runs a test over repeated samples (benchstat, criterion, Bencher t-test). Treat any ratio-threshold gate (github-action-benchmark, pytest-benchmark `compare-fail`) as a coarse alarm, set wide enough to sit above the runner's measured noise.

### 4.3 Choosing data structures for performance (Priority 3)

- **Python** (wiki "TimeComplexity", now served at wiki.python.org/python/TimeComplexity.html; quotes taken from search excerpts — read the live page before citing). For lists: "the largest costs come from growing beyond the current allocation size (because everything must move), or from inserting or deleting somewhere near the beginning (because everything after that must move). If you need to add/remove at both ends, consider using a collections.deque instead." The table gives list Pop intermediate O(n) and Insert O(n); deque `append/appendleft/pop/popleft` O(1); dict get/set/delete O(1) average but O(n) amortized worst case; set `x in s` O(1) average, O(n) worst.\[63\] A new official page, docs.python.org/3/builtins/time-complexity.html ("Python 3.15.2 documentation"), now exists: "In the worst case, O(1) operations instead take O(n) time".\[64\] It is likely the better primary source going forward (not fully read).
- **Rust** (std::collections): "To get this out of the way: you should probably just use Vec or HashMap. These two collections cover most use cases for generic data storage and processing." On VecDeque: "You want a Vec that supports efficient insertion at both ends of the sequence."\[43\] On LinkedList: "It is almost always better to use Vec or VecDeque because array-based containers are generally faster, more memory efficient, and make better use of CPU cache."\[65\]
- **.NET collections guidance, Java Collections**: not covered (search budget).

**Position:** array-backed containers by default (Python `list`, Rust `Vec`); a deque when both ends change; hash maps/sets for membership, remembering that "O(1)" is an average and degrades under bad hashing; avoid linked lists unless measured.

### 4.4 Free threading in libraries (Priority 4)

CPython status: 3.14 made the free-threaded build "supported and no longer experimental" (PEP 779), with a 5–10% single-thread penalty.\[26\] Python 3.15 is current (docs at 3.15.2) and adds the PEP 803 `abi3t` stable ABI for free-threaded builds.\[66\]

| Project | First version with free-threaded support (tracker) | Current state from release notes |
|---|---|---|
| NumPy | (tracker row not captured; cp313t from 2.1.0, cp314t from 2.3.2 per a third-party audit, secondary)\[67\] | 2.5.0 (21 Jun 2026): `abi3t` support, lock-free ufunc dispatch; 2.5.2 (9 Aug 2026) adds 3.15 wheels; latest 2.5.4 (10 Oct 2026)\[34\]\[68\]\[69\] |
| pandas | 2.2.3\[42\] | 2.3.3: FT wheels Linux/macOS only; 3.0.0 (21 Jan 2026): Windows too; 3.1.1 (4 Nov 2026) cp314t on all platforms incl. win_arm64\[24\]\[32\]\[33\] |
| Cython | 3.1.0 | — |
| PyO3 | 0.23 (initial, opt-in)\[70\] | 0.28.0 opt-out; 0.29.0 dropped 3.13t; 0.30.0 (13 Oct 2026) 3.15 final, `abi3t`\[27\] |
| maturin | 1.7.5\[42\] | — |
| matplotlib | 3.9.0\[42\] | — |
| cryptography | 46.0.0\[42\] | — |
| cffi | 2.0.0\[42\] | — |
| JAX | 0.5.1\[42\] | — |
| aiohttp | 3.13.0\[42\] | — |
| lxml | 7.0.0\[42\] | — |
| h5py | 3.16.0\[42\] | — |
| grpcio, brotli, cuda-python | none listed\[42\] | Not yet released with support |

The tracker states it covers "packages for which we're aware of active work on free-threaded support" and does not track pure-Python packages, which "work without changes by design".\[42\] A cp314t wheel does not guarantee the GIL stays disabled: an extension that does not declare support re-enables the GIL at import (stated in an autobahn-python issue, secondary).\[35\] Check at run time with `sys._is_gil_enabled()`.

### 4.5 Go `context` (Standard 5)

From pkg.go.dev/context (go1.27.4, published 10 Nov 2026):
- "Calling the CancelFunc directly cancels the child and its children, removes the parent's reference to the child, and stops any associated timers. Failing to call the CancelFunc leaks the child and its children until the parent is canceled. The go vet tool checks that CancelFuncs are used on all control-flow paths."\[29\]
- "Do not store Contexts inside a struct type; instead, pass a Context explicitly to each function that needs it. … The Context should be the first parameter, typically named ctx"\[29\]
- "Do not pass a nil Context, even if a function permits it. Pass context.TODO if you are unsure about which Context to use."\[29\]
- "Use context Values only for request-scoped data that transits processes and APIs, not for passing optional parameters to functions."\[29\]
- "Contexts are safe for simultaneous use by multiple goroutines."\[29\]
The Go blog posts on cancellation and deadlines were not retrieved (search budget).

### 4.6 JFR and Chrome DevTools (Standard 6)

Not covered — see section 9.

### 4.7 Database performance from application code (Standard 7) — EF Core only

- **N+1**: "each iteration in the inner foreach triggers an additional database query, in its own roundtrip … this is sometimes called the *N+1* problem". Fix with eager loading (`Include`) or a projection; "Because lazy loading makes it extremely easy to inadvertently trigger the N+1 problem, it is recommended to avoid it." ASP.NET Core best practices: "Do not use projection queries on collections, which can result in executing \"N + 1\" SQL queries."\[30\]
- **Cartesian explosion / split queries**: `.AsSplitQuery()` issues one SQL query per included collection. EF Core uses single-query mode by default and warns when a query loads multiple collections without a configured split mode. Split queries with Skip/Take on EF versions before 10 need fully unique ordering, or results can be wrong.\[30\]
- **Pooling**: `AddDbContextPool` (default `poolSize` 1024); "context pooling is orthogonal to database connection pooling, which is managed at a lower level in the database driver." For low latency, EF also recommends precompiled queries for hot paths.\[30\]
- **Batching**: EF Core batching docs not retrieved. SQLAlchemy, Django ORM, Hibernate, GORM: not covered.

### 4.8 Common mistakes — see section 7.

## 5. Tools

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| benchstat | Compare Go benchmark runs | Not found (x/perf untagged) | Not found | `go install golang.org/x/perf/cmd/benchstat@latest` then `benchstat old.txt new.txt`\[71\] | None (unit metadata in input) | pkg.go.dev/golang.org/x/perf/cmd/benchstat |
| criterion | Rust benchmark harness | 0.8.2 | Not found | `cargo bench -- --save-baseline main` / `--baseline main` | `Cargo.toml` `[[bench]] harness = false` | docs.rs/crate/criterion/latest |
| BenchmarkDotNet | .NET benchmark harness | Not found | Not found | `dotnet add package BenchmarkDotNet` | Attributes / `ManualConfig` | benchmarkdotnet.org |
| pytest-benchmark | Python benchmark fixture | 5.3.1 | 2026-11-01 | `pytest --benchmark-autosave`; `pytest --benchmark-compare=0001 --benchmark-compare-fail=mean:5%` | `pytest.ini`/`pyproject.toml` addopts | pytest-benchmark readthedocs\[9\]\[59\] |
| Bencher | Continuous benchmarking, t-test thresholds | Not found | Not found | `bencher run --threshold-test t_test --error-on-alert ...`\[60\] | CLI flags | bencher.dev/docs |
| github-action-benchmark | CI regression alerts by ratio | v1 tag (exact release not found) | Not found | `uses: benchmark-action/github-action-benchmark@v1`\[62\] | Workflow YAML inputs | github.com/benchmark-action/github-action-benchmark |
| CodSpeed | CI benchmarking | Not found | Not found | Not found | Not found | — |
| cachetools | Python memoizing caches | 8.0.0 | 2026-11-06 | `pip install cachetools` | — | github.com/tkem/cachetools CHANGELOG |
| lru-cache | Node LRU cache | 11.5.3 | ≈Sep 2026 ("2 months ago") | `npm i lru-cache`\[49\] | — | npmjs.com/package/lru-cache\[22\] |
| HybridCache | .NET L1/L2 cache | Not found | Introduced .NET 9 | `dotnet add package Microsoft.Extensions.Caching.Hybrid`; `AddHybridCache()`\[72\] | DI options | learn.microsoft.com |
| moka | Rust concurrent cache | 0.12.16 | Not found | `cargo add moka --features future` (or `sync`)\[73\] | — | docs.rs/crate/moka/latest |
| Caffeine | Java cache | Contested: 3.2.4 vs 3.3.1 | 3.2.4: 2026-05-03\[41\] | `implementation("com.github.ben-manes.caffeine:caffeine:<ver>")` | — | github.com/ben-manes/caffeine; javadoc.io |
| NumPy | Arrays (FT wheels) | 2.5.4 | 2026-10-10 | `pip install numpy` | — | numpy.org/news |
| pandas | DataFrames (FT wheels) | 3.1.1 | 2026-11-04\[32\] | `pip install pandas` | — | pypi.org/project/pandas |
| PyO3 | Rust–Python bindings | 0.30.0 | 2026-10-13\[74\] | `cargo add pyo3` | `Cargo.toml` features | pyo3.rs changelog |

End-of-support dates: none of these projects publish an EOL date in the sources read; "not found" for all.

## 6. Changing in the next 12 months

- **cachetools 8.0.0 (6 Nov 2026)** already removed Python 3.10, `@cached(cache=None)` and deprecated `@cachedmethod` features.\[23\] Pin `<8` or migrate now.
- **PyO3**: 3.13t support was dropped in 0.29.0; 0.30.0 dropped Python 3.8. PyO3 recommends shipping an abi3 wheel + 3.14t wheel + abi3t wheel (3.15+).\[28\]\[74\]
- **NumPy 2.5** dropped Python 3.11 and deprecated setting `ndarray.shape` ("mutating an array is unsafe if an array is shared, especially by multiple threads").\[25\]\[75\]
- **pandas 2.3.x** free-threaded wheels lack Windows;\[33\] move to 3.x.
- **Python 3.10 end of life**: already passed. The Python Developer's Guide "Status of Python versions" page (devguide.python.org/versions/) lists "3.10 | PEP 619 | end-of-life | 2021-10-04 | 2026-10-01", so EOL was 1 October 2026 (some secondary blogs give 31 Oct 2026, which is wrong). This is consistent with cachetools 8.0.0 dropping it.
- Announced releases due within 6 months: not found for any listed tool.

## 7. Common mistakes (including AI coding assistants)

1. **Separate get-then-set around an expensive call** instead of the library's atomic loader (`HybridCache.GetOrCreateAsync`, moka `get_with`, Caffeine `LoadingCache`). This defeats coalescing.\[76\]\[77\] Source: moka and Microsoft docs above.
2. **Assuming HybridCache stops cross-server stampedes.** It doesn't: "This coordination doesn't extend to other HybridCache instances."\[16\]
3. **Identical TTLs for keys written together** (e.g. after a cache warm). AWS: add jitter.\[12\]
4. **Not caching errors / misses.** AWS has seen this lead "to increased failure rates and faults".\[13\]
5. **Unbounded caches**: lru-cache refuses construction without `max`, `ttl` or `maxSize`;\[49\] Python `functools.cache` is unbounded by design (official docs not re-read this run).\[21\]
6. **Treating lru-cache TTL as a hard eviction guarantee**: "does not make strong TTL guarantees".\[22\]
7. **Quoting the old benchstat** (`-delta-test`, mean ± %) or reporting single-run Go benchmarks. Use `-count=10`+ and current benchstat.\[78\]
8. **Re-running until significant** — benchstat explicitly warns against this.\[1\]
9. **Overwriting the criterion baseline** with `--save-baseline` when `--baseline` was meant.\[31\]
10. **Reading BenchmarkDotNet "Error" as standard error**; it is half of the 99.9% CI.\[58\]
11. **Gating CI on a percent threshold from one run on shared runners** (github-action-benchmark default behaviour, pytest-benchmark `compare-fail`). Bencher measures shared-runner variance above 30% (vendor claim).\[79\]
12. **Equating "has a cp314t wheel" with "runs without the GIL"** — check `sys._is_gil_enabled()`.\[35\]\[80\]
13. **Lazy-loading navigation properties in loops** (EF Core N+1) and confusing DbContext pooling with connection pooling.\[30\]
14. **Storing `context.Context` in structs or dropping the CancelFunc** in Go.\[29\]
Evidence specific to *AI assistants* making these mistakes (as opposed to people in general) was not found in primary sources; items 1, 7 and 11 are the patterns most often seen in generated code, but that is the author's judgement, not a sourced finding.

## 8. Sources and licences

Licence terms were only partly verified in this run; "not verified" means the receiving session must check before quoting at length or adapting code.

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| pkg.go.dev x/perf (benchstat), context | BSD-style (Go Authors; header in x/perf source)\[81\] | Yes, briefly | Yes | Yes, keep BSD notice | "The Go Authors", link |
| criterion.rs book/changelog | Not verified | Brief only | Yes | Check first | Link |
| benchmarkdotnet.org | Not verified | Brief only | Yes | Check first | Link |
| pytest-benchmark docs | Not verified | Brief only | Yes | Check first | Link |
| bencher.dev docs | Not verified | Brief only | Yes | Check first | Link |
| github-action-benchmark | Not verified | Brief only | Yes | Check first | Link |
| AWS caching pages / Builders' Library | Not verified (AWS site terms) | Brief only | Yes | No (write your own) | "Amazon Web Services", link |
| Vattani et al. PVLDB 2015 | CC BY-NC-ND 3.0 Unported (confirmed in the paper, vldb.org/pvldb/vol8/p886-vattani.pdf: "This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License… Obtain permission prior to any use beyond those covered by the license.") | Brief only | Yes | Algorithm idea yes; no verbatim code | Full citation, DOI 10.14778/2757807.2757813 |
| Microsoft Learn (ASP.NET Core, .NET, EF Core) | Not verified this run | Brief only | Yes | Check first | "Microsoft Learn", link |
| Cloudflare docs / community | Not verified | Brief only | Yes | No | Link |
| Google Cloud CDN docs | Not verified | Brief only | Yes | No | Link |
| docs.rs moka | Not verified | Brief only | Yes | Check first | Link |
| npm lru-cache | Not verified | Brief only | Yes | Check first | Link |
| cachetools | MIT (libraries.io)\[82\] | Yes | Yes | Yes, keep MIT notice | Thomas Kemmer, link |
| Caffeine | Apache 2.0 (mvnrepository)\[57\] | Yes | Yes | Yes, keep NOTICE | Ben Manes, link |
| docs.python.org / Python wiki | Not verified | Brief only | Yes | Check first | Link |
| numpy.org, pandas.pydata.org | Not verified | Brief only | Yes | Check first | Link |
| pyo3.rs | Not verified | Brief only | Yes | Check first | Link |
| py-free-threading.github.io | Not verified | Brief only | Yes | Check first | Link |
| doc.rust-lang.org | Not verified | Brief only | Yes | Check first | Link |
| Secondary: matthias-jost.ch, socket.dev, dev.to, community.cloudflare.com | Not verified | Brief only, labelled secondary | Yes | No | Link |

## 9. Not found, contested, not covered

**Contested**
- Caffeine current version: GitHub release v3.2.4 (3 May 2026), mvnrepository lists 3.2.4 as latest, but javadoc.io lists 3.3.0 and 3.3.1.\[41\]\[54\]\[83\] Check Maven Central directly.
- moka: docs.rs shows 0.12.16; a crates.io snippet showed 0.12.15 (probably stale crawl).\[73\]\[84\]

**Not found**
- Release dates for criterion 0.8.2, BenchmarkDotNet, Bencher, moka 0.12.16, HybridCache package; any EOL dates for listed tools.
- Primary Redis/Valkey and Memcached documentation on stampede locks or negative caching.
- Full-page read of Cloudflare's "Default cache behavior" table (the 404/410 3-minute default was confirmed from the page's search excerpt only).
- BenchmarkDotNet built-in significance testing in default output.
- Evidence specific to AI assistants' caching/benchmark mistakes.

**Not covered (search budget exhausted)**
- JMH reporting/comparison; CodSpeed.
- .NET collections guidance; Java Collections Framework guidance; Go in-process caches.
- Go blog posts on cancellation and deadlines.
- JFR (`jcmd JFR.start`, JDK Mission Control) and the Chrome DevTools Performance panel.
- ORM docs other than EF Core (SQLAlchemy, Django, Hibernate, GORM); EF Core batching.
- `functools.lru_cache` doc quotes.

## Sources

1. [benchstat command - golang.org/x/perf/cmd/benchstat - Go Packages](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat)
2. [benchstat package - golang.org/x/perf/benchstat - Go Packages](https://pkg.go.dev/golang.org/x/perf/benchstat)
3. [benchstat command - github.com/kevinburke/benchstat - Go Packages](https://pkg.go.dev/github.com/kevinburke/benchstat)
4. [Command-Line Options - Criterion.rs Documentation](https://bheisler.github.io/criterion.rs/book/user_guide/command_line_options.html)
5. [criterion.rs/CHANGELOG.md at master · bheisler/criterion.rs · GitHub](https://github.com/bheisler/criterion.rs/blob/master/CHANGELOG.md)
6. [Home](https://benchmarkdotnet.org/)
7. [BenchmarkDotNet: Get Started with Benchmarking Your C# Code « Matthias Jost](https://www.matthias-jost.ch/testing-csharp-code-with-benchmarkdotnet/)
8. [pytest-benchmark - PyPI Package Security Analysis - Socket](https://socket.dev/pypi/package/pytest-benchmark)
9. [pytest-benchmark Release 5.3.1 Ionel Cristian Măries, Nov 01, 2026](https://app.readthedocs.org/projects/pytest-benchmark/downloads/pdf/latest/)
10. [Thresholds & Alerts with bencher run](https://bencher.dev/docs/explanation/thresholds/)
11. [github-action-benchmark/action.yml at master · benchmark-action/github-action-benchmark · GitHub](https://github.com/benchmark-action/github-action-benchmark/blob/master/action.yml)
12. [Caching Best Practices](https://aws.amazon.com/caching/best-practices/)
13. [Caching challenges and strategies | AWS Builder Center](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)
14. [(PDF) Optimal probabilistic cache stampede prevention](https://www.researchgate.net/publication/276465356_Optimal_probabilistic_cache_stampede_prevention)
15. [xfetch - Rust](https://docs.rs/xfetch)
16. [Overview of caching in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-10.0)
17. [Caching in .NET - .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/caching)
18. [learn.microsoft.com](https://learn.microsoft.com/nl-nl/aspnet/core/performance/caching/overview?view=aspnetcore-3.1)
19. [Cache in moka::future - Rust](https://docs.rs/moka/latest/moka/future/struct.Cache.html)
20. [lru-cache - npm Package Security Analysis - Socket.dev](https://socket.dev/npm/package/lru-cache)
21. [lru-cache](https://isaacs.github.io/node-lru-cache/)
22. [lru-cache - npm](https://www.npmjs.com/package/lru-cache)
23. [cachetools/CHANGELOG.rst at master · tkem/cachetools · GitHub](https://github.com/tkem/cachetools/blob/master/CHANGELOG.rst)
24. [What’s new in 3.0.0 (January 21, 2026) — pandas 3.1.1 documentation](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html)
25. [Release v2.5.0 (June 21, 2026) · numpy/numpy · GitHub](https://github.com/numpy/numpy/releases/tag/v2.5.0)
26. [What’s new in Python 3.14 — Python 3.15.2 documentation](https://docs.python.org/3/whatsnew/3.14.html)
27. [CHANGELOG - PyO3 user guide](https://pyo3.rs/main/changelog)
28. [Releases · PyO3/pyo3 · GitHub](https://github.com/pyo3/pyo3/releases)
29. [context package - context - Go Packages](https://pkg.go.dev/context)
30. Microsoft Learn
31. [Confused by criterion options - help - The Rust Programming Language Forum](https://users.rust-lang.org/t/confused-by-criterion-options/113391)
32. [pandas: A Powerful Python Data Analysis Toolkit](https://pypi.org/project/pandas/)
33. [What’s new in 2.3.3 (September 29, 2025) — pandas 3.1.1 documentation](https://pandas.pydata.org/docs/whatsnew/v2.3.3.html)
34. [NumPy - News](https://numpy.org/news/)
35. [\[FEATURE\] Publish CPython 3.14 wheels for both free-threaded (no-GIL) and regular (GIL) builds on all platforms · Issue #1875 · crossbario/autobahn-python · GitHub](https://github.com/crossbario/autobahn-python/issues/1875)
36. [pytest-benchmark Release 5.3.0 Ionel Cristian Măries, Aug 23, 2026](https://pytest-benchmark.readthedocs.io/_/downloads/en/latest/pdf/)
37. [What is Continuous Benchmarking?](https://bencher.dev/docs/explanation/continuous-benchmarking/)
38. [\[PDF\] Optimal Probabilistic Cache Stampede Prevention](https://www.semanticscholar.org/paper/Optimal-Probabilistic-Cache-Stampede-Prevention-Vattani-Chierichetti/abceccfc74a577ed06a5aeb7bebe365e9ff8946d)
39. [Use negative caching | Cloud CDN | Google Cloud Documentation](https://docs.cloud.google.com/cdn/docs/using-negative-caching)
40. [Edge and Browser Cache TTL · Cloudflare Cache (CDN) docs](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/)
41. [Release 3.2.4 · ben-manes/caffeine · GitHub](https://github.com/ben-manes/caffeine/releases/tag/v3.2.4)
42. [Compatibility Status Tracking - Python Free-Threading Guide](https://py-free-threading.github.io/tracking/)
43. [std::collections - Rust](https://doc.rust-lang.org/std/collections/index.html)
44. [Mitigating Thundering Herd Problems in Distributed Auth Caching](https://mojoauth.com/blog/thundering-herd-distributed-auth-caching)
45. [Cache Stampede Prevention: Locks, XFetch, SWR in PHP & Node](https://www.nexgismo.com/blog/cache-stampede-prevention-locks-xfetch-swr-php-node)
46. [How to Solve the Thundering Herd Problem in Distributed Systems - Ajit Singh](https://singhajit.com/thundering-herd-problem/)
47. [cachetools](https://security.snyk.io/package/pip/cachetools)
48. [lru-cache - npm](https://www.npmjs.com/package/lru-cache/v/7.18.1)
49. [lru-cache - npm](https://www.npmjs.com/package/lru-cache/v/8.0.0)
50. [lru-cache - npm](https://www.npmjs.com/package/lru-cache?activeTab=versions)
51. [HybridCache — The Best of In-Memory and Distributed Cache](https://learnixo.io/blog/dotnet-hybrid-cache)
52. [OwnedKeyEntrySelector in moka::future - Rust](https://docs.rs/moka/latest/moka/future/struct.OwnedKeyEntrySelector.html)
53. [moka/ lib.rs](https://docs.rs/moka/latest/src/moka/lib.rs.html)
54. [com.github.ben-manes.caffeine:caffeine versions](https://www.javadoc.io/versions/com.github.ben-manes.caffeine/caffeine)
55. [GitHub - sg-scale/caffeine--v3.2.3: Mirror of https://github.com/ben-manes/caffeine at v3.2.3 · GitHub](https://github.com/sg-scale/caffeine--v3.2.3)
56. [caffeine/README.md at master · ben-manes/caffeine · GitHub](https://github.com/ben-manes/caffeine/blob/master/README.md)
57. [Maven Repository: com.github.ben-manes.caffeine » jcache » 3.2.0](https://mvnrepository.com/artifact/com.github.ben-manes.caffeine/jcache/3.2.0)
58. [BenchmarkDotNet: .NET Performance Benchmarking Guide](https://helpmetest.com/blog/benchmarkdotnet-performance-testing/)
59. [pytest-benchmark: The Complete Performance Testing Guide (2026)](https://qaskills.sh/blog/pytest-benchmark-performance-testing-guide)
60. [How to Track Benchmarks in CI with Bencher](https://bencher.dev/docs/how-to/track-benchmarks/)
61. [How to use Bencher in GitLab CI/CD](https://bencher.dev/docs/how-to/gitlab-ci-cd/)
62. [GitHub - benchmark-action/github-action-benchmark: GitHub Action for continuous benchmarking to keep performance · GitHub](https://github.com/benchmark-action/github-action-benchmark)
63. [TimeComplexity - Python Wiki](https://wiki.python.org/python/TimeComplexity.html)
64. [Time complexity of operations on built-in types — Python 3.15.2 documentation](https://docs.python.org/3/builtins/time-complexity.html)
65. [std::collections::linked\_list - Rust](https://doc.rust-lang.org/std/collections/linked_list/index.html)
66. [Free-Threaded Python 3.14/3.15 on Windows: Install, Verify and Benchmark No-GIL Builds](https://windowsforum.com/news/free-threaded-python-3-14-3-15-on-windows-install-verify-and-benchmark-no-gil-builds.448936/)
67. [chore(packaging): add free-threaded (cp314t) wheels once GDAL's PyPI sdist ships SWIG 4.4+ wrappers · Issue #683 · serapeum-org/pyramids · GitHub](https://github.com/serapeum-org/pyramids/issues/683)
68. [NumPy 2.5.0 Release Notes — NumPy v2.6.dev0 Manual](https://numpy.org/devdocs/release/2.5.0-notes.html)
69. [NumPy 2.5.2 Release Notes — NumPy v2.6.dev0 Manual](https://numpy.org/devdocs/release/2.5.2-notes.html)
70. [Appendix A: Migration guide - PyO3 user guide](https://pyo3.rs/main/migration)
71. [benchstat in Go: Comparing Benchmarks Without Fooling Yourself - DEV Community](https://dev.to/gabrielanhaia/benchstat-in-go-comparing-benchmarks-without-fooling-yourself-15gk)
72. [HybridCache in ASP.NET Core .NET 10 - Complete Guide](https://codewithmukesh.com/blog/hybridcache-in-aspnet-core/)
73. [moka 0.12.16 - Docs.rs](https://docs.rs/crate/moka/latest)
74. [pyo3/CHANGELOG.md at main · PyO3/pyo3 · GitHub](https://github.com/PyO3/pyo3/blob/main/CHANGELOG.md)
75. [NumPy 2.5.0 Release Notes — NumPy v2.5 Manual](https://numpy.org/doc/2.5/release/2.5.0-notes.html)
76. [Hybrid Caching in .NET: HybridCache and FusionCache Guide](https://www.hrishidigital.com.au/blog/hybrid-caching-dotnet/)
77. [Cache Stampede in ASP.NET Core: Root Cause and Fix](https://codingdroplets.com/cache-stampede-aspnet-core-imemorycache-production-fix)
78. [16.5 Benchmarking and Performance Profiling](https://golang.design/under-the-hood/en/part5toolchain/ch16tools/perf/)
79. [GitHub - bencherdev/bencher: 🐰 Bencher - Continuous Benchmarking · GitHub](https://github.com/bencherdev/bencher)
80. [Python 3.14 Free-Threading: Real Benchmarks, Real Breakage, Real Code - DEV Community](https://dev.to/dmaxdev/python-314-free-threading-real-benchmarks-real-breakage-real-code-3m5)
81. [perf/benchstat/delta.go at master · golang/perf · GitHub](https://github.com/golang/perf/blob/master/benchstat/delta.go)
82. [cachetools 7.1.1 on PyPI - Libraries.io - security & maintenance data for open source software](https://libraries.io/pypi/cachetools)
83. [Maven Repository: com.github.ben-manes.caffeine » caffeine](https://mvnrepository.com/artifact/com.github.ben-manes.caffeine/caffeine)
84. [moka - crates.io: Rust Package Registry](https://crates.io/crates/moka)

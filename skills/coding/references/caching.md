# Caching

Read this for adding a cache in front of a database, a service or a slow function, choosing its
size and expiry, a cache that serves stale data or grows without limit, a burst of load when a
hot key expires (a stampede or thundering herd), caching "not found" and errors, and choosing an
in-process cache library in Python, Node.js, .NET, Rust or Java.

Finding what's slow and the concurrency around a cache are `performance-and-concurrency`'s, and
proving a cache made something faster is `benchmarking`'s. Caching what a CI job builds is
`ci-speed`'s. Retries, timeouts and circuit breakers for the call behind a cache are
`error-handling`'s; emitting the hit and miss metrics is `logging-and-observability`'s. HTTP
`Cache-Control` headers and a CDN's settings are outside it, apart from their defaults for
errors.

## Rules

1. **A cache gets an owner, an invalidation rule and a size bound.** The owner is the code that
   decides what goes in; the rule is a TTL, a write-through or an event; the bound is entries or
   bytes.
2. **Put a TTL on every key except those written through, and add jitter** (fact `ca-aws-ttl`),
   so keys written together don't expire together.
3. **Load through the library's atomic loader, never get-then-set.** A hand-written check, call
   and store lets every concurrent miss call the source.
4. **Plan for a stampede on each hot key.** Coalescing covers one process. Across servers, add
   early refresh, a soft TTL, or coalescing in the shared tier.
5. **Cache negative results with a TTL of their own,** and keep "not found" apart from
   "couldn't look", which `error-handling` rules on.
6. **Key on everything the value depends on:** tenant, user, locale, version and options. A
   per-user value under a shared key serves one person's data to another.
7. **Measure hit rate, misses and calls to the source,** then set size and TTL from them (fact
   `ca-measure`).

### Stampedes

When a hot key expires, every request that misses calls the source at once. Four answers:

- **Jitter on the TTL** (fact `ca-aws-ttl`) spreads keys written together. It doesn't help one
  hot key.
- **Request coalescing:** one call per missing key is in flight, and the rest wait for it (fact
  `ca-coalescing`). The loaders below do this within one process or instance only, as
  HybridCache says (fact `ca-hybrid-instance`): twenty servers still send twenty calls.
- **Probabilistic early expiration** (XFetch, fact `ca-xfetch`): on each hit, a reader refreshes
  early with a chance that rises as expiry nears and with how long a refresh takes. One reader
  usually refreshes first, with no coordination, so it works across servers.
- **Soft and hard TTLs:** past the soft TTL, refresh; if the source fails, serve the old value
  until the hard TTL (fact `ca-soft-hard-ttl`).

A per-key lock in a shared store, such as Redis, is our practice at most: no primary source was
found for it, and a lock brings its own timeouts and failures. Try the four above first.

### Negative caching

Cache "not found" and errors, each with a TTL shorter than a hit's, or a missing key or a failing
source draws every request through (fact `ca-negative`). CDNs do it by default (fact
`ca-cdn-negative`). A cached failure must never read as "not found".

### Libraries per language

| Language | Library | Bound | Atomic loader | Facts |
|---|---|---|---|---|
| Python | `functools.lru_cache` | `maxsize`; `functools.cache` has none | None: may call twice | `ca-functools` |
| Python | cachetools: 8.x needs 3.11, 7.x for 3.10 | `maxsize`; `TTLCache` adds `ttl` | `@cached` with `condition=` | `ca-cachetools` |
| Node.js | lru-cache | `max`, `maxSize` or `ttl`, required | `fetch()` with `fetchMethod` | `ca-lru-cache` |
| .NET | `IMemoryCache` | `SizeLimit`; unset is unbounded | None documented | `ca-memorycache` |
| .NET | HybridCache | Entry expiration | `GetOrCreateAsync`, per instance | `ca-hybrid` |
| Rust | moka | `max_capacity` | `get_with` | `ca-moka` |
| Java | Caffeine 3.x | `maximumSize` | `get(key, k -> ...)`, `LoadingCache` | `ca-caffeine` |
| Go | Not researched | | | |

## Mistakes

- **`if key not in cache: cache[key] = load(key)` around a slow call.** Every concurrent miss
  calls the source. Use the loader in the table.
- **Trusting HybridCache to stop a stampede across servers.** It coalesces per instance.
- **One fixed TTL for keys loaded in one batch.** They expire in the same second: add jitter.
- **Caching only hits.** A missing record, or a failing source, is then fetched on every request.
- **`@functools.cache` or an `IMemoryCache` with no `SizeLimit` on a long-running server.** Both
  grow without bound, fastest when keys come from user input.
- **Treating lru-cache's `ttl` as a guarantee,** for a token's expiry say. It keeps expired
  items until they're read (fact `ca-lru-cache`). Check the expiry yourself.
- **Picking size and TTL once, by feel, and never checking them** (fact `ca-measure`).

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| An unbounded cache | `functools.cache`, `lru_cache(maxsize=None)`, a dict as a memo, `IMemoryCache` without `SizeLimit` | `BLOCKER` where keys come from outside input, else `GAP` | A bound (rule 1) |
| A key with no TTL | A cache-aside `set` with no expiry, outside write-through | `GAP` | A TTL with jitter (rule 2) |
| Get-then-set around a slow call | A lookup, a miss branch that calls the source, then a store | `DRIFT` | The atomic loader (rule 3) |
| A per-user value under a shared key | A key without the user or tenant the value depends on | `BLOCKER` | Key on it (rule 6) |
| Misses and errors never cached | Nothing stored when the source finds nothing or fails | `GAP` where the lookup is hot | A negative entry with its own TTL (rule 5) |
| No hit or miss metric | No counter or stats call for the cache | `GAP` | Emit hits, misses and source calls (rule 7) |
| A cross-server stampede left to per-instance coalescing | A loader alone, on a key many servers read | `GAP` where the source can't take one call per server | Early refresh or a soft TTL (rule 4) |

## Why

### Owner, invalidation and bound

- **The reason:** a cache with no bound grows until memory runs out, as `IMemoryCache` and
  `functools.cache` do by default (facts `ca-memorycache`, `ca-functools`). One with no
  invalidation rule serves stale data. One with no owner is never fixed.
- **Sourced and ours:** the bound is sourced: lru-cache refuses to build without one (fact
  `ca-lru-cache`), and Microsoft warns against user input as keys (fact `ca-memorycache`). The
  TTL is AWS's (fact `ca-aws-ttl`). The owner, and the three as one rule, are our practice.
- **What it costs:** evictions, and a miss after each.
- **When to choose differently:** a small, fixed key set, such as an enum's values.

### Expiry and jitter

- **The reason:** a TTL catches the bug where code forgets to update or delete a key, and
  randomness spreads the expiry of keys written together (fact `ca-aws-ttl`).
- **What it costs:** a reload per key per TTL, and data up to a TTL old.
- **When to choose differently:** a write-through key, updated with its record, needs none.

### Atomic loaders and stampedes

- **The reason:** coalescing lets one call per missing key reach the source (fact
  `ca-coalescing`). Each loader in the table does it per key (facts `ca-hybrid`, `ca-moka`,
  `ca-caffeine`, `ca-lru-cache`, `ca-cachetools`); `functools` doesn't promise to call once
  (fact `ca-functools`).
- **What others do:** AWS names libraries, Nginx and Varnish as coalescing for you (fact
  `ca-coalescing`). XFetch's authors prove their early refresh optimal (fact `ca-xfetch`).
- **What it costs:** waiters share the first call's latency and failure. Early refresh spends
  extra calls; a soft TTL serves older data.
- **When to choose differently:** a value cheap to compute needs no coalescing.

### Negative caching

- **The reason:** AWS has seen failures to cache negative responses raise failure rates (fact
  `ca-negative`).
- **What it costs:** a record created after a cached miss stays missing until that TTL ends.
- **When to choose differently:** never cache a rejection of the caller's own bad input as the
  record's absence.

### Keys and measurement

- **Keys:** our practice, not researched: a key missing a part the value depends on returns the
  wrong value, and when that part is the user, it leaks data. **Cost:** more keys, fewer hits.
- **Measurement:** AWS warns against size and TTL picked once and never checked (fact
  `ca-measure`). **Cost:** a metric per cache.

## Facts

Versions, defaults and guidance, each named elsewhere in this module by its ID. Checked
2026-11-16.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `ca-aws-ttl` | AWS: a TTL on every key not written through, with jitter | [Caching best practices](https://aws.amazon.com/caching/best-practices/) | "Always apply a time to live (TTL) to all of your cache keys, except those you are updating by write-through caching." and "add some randomness to your TTL" | 2026-11-16 | 2027-05-16 |
| `ca-coalescing` | AWS: one pending request per uncached key | [Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) | "only one pending request is out for uncached resources." | 2026-11-16 | 2027-05-16 |
| `ca-soft-hard-ttl` | AWS: a soft TTL to refresh, a hard TTL to stop serving | [Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) | "a soft TTL and a hard TTL." | 2026-11-16 | 2027-05-16 |
| `ca-negative` | AWS: cache errors with their own TTL | [Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) | "using a different TTL than positive cache entries" and "a failure to cache negative responses led to increased failure rates and faults." | 2026-11-16 | 2027-05-16 |
| `ca-measure` | AWS: check size and TTL; emit hits, misses and downstream calls | [Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) | "arbitrarily picks some cache size and TTL values" and "emit metrics on cache hits/misses and the number of requests made to downstream services." | 2026-11-16 | 2027-05-16 |
| `ca-xfetch` | Vattani et al., PVLDB 8(8), 2015: optimal early expiration | [Paper](https://www.vldb.org/pvldb/vol8/p886-vattani.pdf) | "In this paper we give optimal algorithms for performing such probabilistic early expirations." | 2026-11-16 | 2027-05-16 |
| `ca-cdn-negative` | Default error TTLs: Google Cloud CDN 120 s for a 404, Cloudflare 3 minutes | [Cloud CDN](https://docs.cloud.google.com/cdn/docs/using-negative-caching), [Cloudflare](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/) | "HTTP 404 Not found 120 seconds" and "404, 410 3m" | 2026-11-16 | 2027-02-16 |
| `ca-hybrid` | HybridCache: one caller runs the factory, even without an L2; 11.0.0 (2026-11-10) | [Caching in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/caching), [NuGet](https://api.nuget.org/v3-flatcontainer/microsoft.extensions.caching.hybrid/index.json) | "Only one concurrent request executes the factory method" and "Even without an IDistributedCache configured, HybridCache still provides in-memory caching and stampede protection." and "11.0.0" | 2026-11-16 | 2027-02-16 |
| `ca-hybrid-instance` | HybridCache coalesces within one instance | [ASP.NET Core caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-10.0) | "This coordination doesn't extend to other HybridCache instances." | 2026-11-16 | 2027-05-16 |
| `ca-memorycache` | `IMemoryCache` is unbounded without `SizeLimit`; user input as keys isn't advised | [In-memory cache](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/memory?view=aspnetcore-10.0) | "If the SizeLimit property isn't set, the cache grows without bound." and "using arbitrary user-provided input as a cache key isn't recommended" | 2026-11-16 | 2027-05-16 |
| `ca-functools` | `functools.cache` is unbounded; `lru_cache` may call twice | [functools](https://docs.python.org/3/library/functools.html) | "Simple lightweight unbounded function cache." and "Call-once behavior is not guaranteed" | 2026-11-16 | 2027-05-16 |
| `ca-cachetools` | cachetools 8.0.0 (2026-11-06) drops 3.10, 7.3.2 (2026-11-14) is the newest 7.x; `condition` coalesces | [Changelog](https://raw.githubusercontent.com/tkem/cachetools/master/CHANGELOG.rst), [PyPI](https://pypi.org/pypi/cachetools/json), [docs](https://cachetools.readthedocs.io/en/latest/) | "Drop Python 3.10 support (breaking change)." and "\"version\":\"8.0.0\"" and "2026-11-14T21:19:05" and "will prevent concurrent execution of the wrapped function with identical parameters" | 2026-11-16 | 2027-02-16 |
| `ca-lru-cache` | lru-cache 11.5.3 (2026-09-18): a bound is required, TTLs are weak, `fetch()` coalesces | [npm](https://registry.npmjs.org/lru-cache), [LRUCache](https://isaacs.github.io/node-lru-cache/classes/LRUCache.LRUCache.html) | "\"latest\":\"11.5.3\"" and "At least one of 'max', 'ttl', or 'maxSize' is required" and "This is not primarily a TTL cache" and "they will all be coalesced into a single call to fetchMethod." | 2026-11-16 | 2027-02-16 |
| `ca-moka` | moka 0.12.16 (2026-08-09); `get_with` runs one init per key | [crates.io](https://crates.io/api/v1/crates/moka), [docs.rs](https://docs.rs/moka/latest/moka/future/struct.Cache.html) | "\"max_stable_version\":\"0.12.16\"" and "Only one of the calls evaluates its future" | 2026-11-16 | 2027-02-16 |
| `ca-caffeine` | Caffeine 3.3.1 (2026-10-13); `get(key, fn)` computes atomically | [Maven Central](https://repo1.maven.org/maven2/com/github/ben-manes/caffeine/caffeine/maven-metadata.xml), [wiki](https://raw.githubusercontent.com/wiki/ben-manes/caffeine/Population.md) | "3.3.1" and "to atomically compute and insert the value into the cache if absent" | 2026-11-16 | 2027-02-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| AWS pages and Builders' Library article (Jas Chhabra, 2019-12-05), linked in Facts | TTLs, coalescing, negative caching, measuring | AWS site terms: our own words, short quotes |
| [Vattani, Chierichetti, Lowenstein, PVLDB 8(8):886-897, 2015](https://www.vldb.org/pvldb/vol8/p886-vattani.pdf) | Early expiration | CC BY-NC-ND 3.0: a short quote with citation, the idea in our words, no code |
| Microsoft Learn, Google Cloud CDN and Cloudflare docs, linked in Facts | HybridCache, `IMemoryCache`, CDN error TTLs | CC BY 4.0: quoted with attribution |
| Python, cachetools, lru-cache, moka and Caffeine docs and registries, linked in Facts | Versions, bounds, loaders | PSF; MIT; BlueOak-1.0.0; MIT or Apache-2.0; Apache-2.0: short quotes with attribution |
| This repository's practice | Owners, keys, per-key locks | Our own words |

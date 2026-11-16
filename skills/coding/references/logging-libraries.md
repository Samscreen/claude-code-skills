# Logging libraries

Read this for choosing a logging library in Python, Node.js, .NET, Java, PHP, Ruby or Rust and
the version to hold; getting `trace_id` and `span_id` into its records; what it redacts and what
you write yourself; bridging it to OpenTelemetry; and mapping its levels to OpenTelemetry
severity numbers.

What to log, the fields, choosing a level, what to keep out, retention and sampling are
`logging-and-observability`'s. Each language's own style is in its language module.

## Rules

1. **Use the library the table names, at or above the version its fact gives.** Log4j and
   Monolog have floors set by fixes (facts `lo-log4j-cve`, `lo-php-monolog`).
2. **Let the library, or OpenTelemetry's own package for it, attach `trace_id` and `span_id`.**
   Where neither does, add a processor that reads the active span, and write the IDs as
   top-level fields.
3. **Redact in the library's pipeline, from a list fixed in code.** Never build the list from
   input. Where the library has no redaction, write a processor or formatter.
4. **Map each level to OpenTelemetry's SeverityNumber by the spec's rule.** Use Appendix B's
   mapping where it has one; keep every error level at 17 or above.
5. **Bridge to the OpenTelemetry logs SDK only where it's stable** (fact `lo-otel-logs`);
   elsewhere, write JSON lines for the Collector to read.
6. **Give the library somewhere to write.** Rust's `tracing` writes nothing without a
   subscriber (fact `lo-rust-tracing`): a binary installs one, a library never does.

### The libraries

| Language | Library | Trace and span IDs | Redaction | Facts |
|---|---|---|---|---|
| Python | structlog | A processor, from a docs recipe | None: write a processor | `lo-libs`, `ll-structlog-otel` |
| Node.js | pino; winston, last released 2025-12 | `@opentelemetry/instrumentation-pino` | pino's `redact` paths | `lo-libs`, `ll-pino-otel`, `ll-pino-redact` |
| .NET | Serilog | Built in since 3.1, from `Activity.Current` | Not checked here | `lo-libs`, `ll-serilog-trace` |
| Java | SLF4J with Logback | `opentelemetry-logback-mdc-1.0` | Only through logstash-logback-encoder | `lo-java-libs`, `ll-java-otel`, `ll-logstash-mask` |
| Java | Log4j 2 | `opentelemetry-log4j-context-data-2.17-autoconfigure` | Masking with Rewrite discouraged | `lo-log4j-cve`, `ll-java-otel`, `ll-log4j-rewrite` |
| PHP | Monolog | None found: a processor | `RedactingFormatter`, 3.12.1 and later | `lo-php-monolog` |
| Ruby | semantic_logger | None found; OpenTelemetry as a destination only | None found: a formatter | `lo-libs`, `ll-semantic-otel` |
| Rust | `tracing`; a binary adds `tracing-subscriber` | Not checked here | Not checked here | `lo-rust-tracing` |

### A structlog processor

structlog's recipe nests the IDs under `span` (fact `ll-structlog-otel`). This one writes them
at the top level, as every other service does, and redacts by key:

```python
from opentelemetry import trace

REDACTED_KEYS = frozenset({"password", "token", "authorization", "cookie"})


def add_trace_ids(_, __, event_dict):
    ctx = trace.get_current_span().get_span_context()
    if ctx.is_valid:
        event_dict["trace_id"] = format(ctx.trace_id, "032x")
        event_dict["span_id"] = format(ctx.span_id, "016x")
    return event_dict


def redact(_, __, event_dict):
    for key in REDACTED_KEYS & event_dict.keys():
        event_dict[key] = "[REDACTED]"
    return event_dict
```

Put both before the renderer in `structlog.configure(processors=[...])`. Monolog and
semantic_logger take the same two steps as a processor or a formatter.

### Mapping levels to severity numbers

The Logs Data Model is Stable. SeverityNumber runs 1 to 24 in six ranges: TRACE 1-4, DEBUG
5-8, INFO 9-12, WARN 13-16, ERROR 17-20, FATAL 21-24. Zero means unspecified, and 17 and up
marks an error (facts `ll-otel-model`, `ll-otel-error`). A source with one level for a range
takes its smallest number.

| Library | Levels and numbers | From |
|---|---|---|
| Log4j 2 | TRACE 1, DEBUG 5, INFO 9, WARN 13, ERROR 17, FATAL 21 | Appendix B (fact `ll-otel-appendix`) |
| Monolog | DEBUG 5, INFO 9, NOTICE 10, WARNING 13, ERROR 17, CRITICAL 18, ALERT 19, EMERGENCY 21 | Appendix B's syslog row |
| Logback | TRACE 1, DEBUG 5, INFO 9, WARN 13, ERROR 17 | The spec's rule |
| Serilog | Verbose 1, Debug 5, Information 9, Warning 13, Error 17, Fatal 21 | The spec's rule |
| pino | trace (10) 1, debug (20) 5, info (30) 9, warn (40) 13, error (50) 17, fatal (60) 21 | The spec's rule |
| semantic_logger | trace 1, debug 5, info 9, warn 13, error 17, fatal 21 | The spec's rule |
| structlog | debug 5, info 9, warning 13, error 17, critical 21 | The spec's rule |

Rows marked "the spec's rule" are our derivation from it, not a published mapping, and the level
names are our reading of each library.

## Mistakes

- **Redaction paths taken from a request or a setting users edit.** pino warns against it (fact
  `ll-pino-redact`); fix the list in code.
- **Log4j's Rewrite appender used to mask secrets.** Its manual discourages it (fact
  `ll-log4j-rewrite`); keep the value out of the event.
- **Monolog below 3.12.1 trusted to redact.** Earlier `RedactingFormatter` releases let some
  secrets through (fact `lo-php-monolog`).
- **Trace IDs expected from Monolog or semantic_logger because OpenTelemetry is installed.**
  Neither was found to add them; add a processor.
- **structlog's recipe copied as is,** so `trace_id` sits under `span` here and at the top level
  in every other service, and queries miss it.
- **ERROR or CRITICAL mapped below 17, or a known level sent as 0.** Error alerts and sampling
  rules read the number and miss the record.
- **A Rust library that installs a global subscriber,** or a binary that installs none.

## Audit

Severity uses the standard's status words, defined in this skill's `SKILL.md`.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| A known-bad version | Log4j below 2.26.1 or 2.25.5; Monolog below 3.12.1 | `DRIFT` | Upgrade |
| Redaction from input | Redact paths or key lists read from a request, a database or a user setting | `BLOCKER` | A list in code |
| No redaction step | No redact option, formatter or processor in the logger's setup | `GAP` | Add one |
| Logs apart from traces | Tracing in use; the library's OpenTelemetry package or processor missing | `GAP` | Add it |
| Severity mapping | An error level below 17; a known level sent as 0 | `DRIFT` | The table above |
| Rust subscriber | A library crate calls `set_global_default` or `init()` | `DRIFT` | Leave it to the binary |

## Why

### Trace IDs from the library

- **Reason:** IDs added by hand at each call get missed. Serilog reads them from
  `Activity.Current` on every write (fact `ll-serilog-trace`); OpenTelemetry's own packages do
  it for pino, Logback and Log4j 2 (facts `ll-pino-otel`, `ll-java-otel`).
- **Cost:** another dependency, and the Java packages are still `-alpha` releases.
- **Choose differently:** where the logs SDK is stable, a bridge to it ties records to the span
  without a field of your own (fact `lo-otel-logs`).

### Redaction in the pipeline

- **Reason:** one step covers every call and every sink. A path list taken from input lets the
  input decide what is hidden, or what is not (fact `ll-pino-redact`).
- **Others:** logstash-logback-encoder masks by path or by value (fact `ll-logstash-mask`); Log4j
  steers away from masking in Rewrite (fact `ll-log4j-rewrite`).
- **Cost:** a key list misses a new key; log named fields, not whole objects.

### Severity numbers

- **Reason:** a backend compares numbers, not names. Taking the smallest number in a range is
  the spec's own rule (fact `ll-otel-model`), and Appendix B shows it for Log4j and syslog (fact
  `ll-otel-appendix`).
- **Cost:** the appendix calls its rows examples, not canonical, and the other rows are ours.
- **Choose differently:** a library with two levels in one range, such as NOTICE and INFO, takes
  the next number for the second.

### Versions

Log4j's CVE-2026-49844 makes `MapMessage.asJson()` write invalid JSON (fact `lo-log4j-cve`);
Monolog's redaction let some secrets through before 3.12.1 (fact `lo-php-monolog`). winston
stays in the table for code that has it.

## Facts

Versions, dates and behavior, each named elsewhere by its ID.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `lo-libs` | structlog 26.1.0, pino 10.4.0, winston 3.19.0 (2025-12-07), Serilog 4.4.0, semantic_logger 5.2.0 (2026-10-30) | [structlog](https://pypi.org/pypi/structlog/json), [pino](https://registry.npmjs.org/pino), [winston](https://registry.npmjs.org/winston), [Serilog](https://api.nuget.org/v3-flatcontainer/serilog/index.json), [semantic_logger](https://rubygems.org/api/v1/versions/semantic_logger.json) | "26.1.0" and "10.4.0" and "3.19.0" and "4.4.0" and "5.2.0" | 2026-11-16 | 2027-02-16 |
| `lo-java-libs` | SLF4J 2.0.20; Logback 1.6.7 (2026-11-14) | [SLF4J](https://repo1.maven.org/maven2/org/slf4j/slf4j-api/maven-metadata.xml), [Logback](https://logback.qos.ch/news.html) | "2.0.20" and "2026-11-14 Release of logback version 1.6.7" | 2026-11-16 | 2027-02-16 |
| `lo-log4j-cve` | Log4j 2.26.1 (2026-06-29); CVE-2026-49844 in `log4j-api`, fixed in 2.25.5 and 2.26.1 | [Maven Central](https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-core/maven-metadata.xml), [Release notes](https://logging.apache.org/log4j/2.x/release-notes.html), [Apache Logging security](https://logging.apache.org/security.html) | "2.26.1" and "Release date 2026-06-29" and "non-finite floating-point values in MapMessage.asJson()" and "Versions fixed 2.25.5 and 2.26.1" | 2026-11-16 | 2027-02-16 |
| `lo-php-monolog` | Monolog 3.12.1; `RedactingFormatter`, fixed in 3.12.1 | [CHANGELOG](https://raw.githubusercontent.com/Seldaek/monolog/main/CHANGELOG.md) | "3.12.1 (2026-09-29)" and "Added `RedactingFormatter`" and "Fixed `RedactingFormatter` letting secrets containing" | 2026-11-16 | 2027-02-16 |
| `lo-rust-tracing` | tracing 0.1.44, tracing-subscriber 0.3.23; `tracing` has no subscriber | [tracing](https://docs.rs/tracing/latest/tracing/), [crates.io](https://crates.io/api/v1/crates/tracing-subscriber) | "0.1.44" and "This library does not contain any Subscriber implementations" and "0.3.23" | 2026-11-11 | 2027-02-11 |
| `lo-otel-logs` | Logs Stable in C++, .NET, Java, PHP, Rust; Go a candidate; Python, JavaScript Development | [Status](https://opentelemetry.io/status/) | "Go Stable Stable Release candidate" and "Python Stable Stable Development" and "JavaScript Stable Stable Development" | 2026-11-11 | 2027-02-11 |
| `ll-otel-model` | Logs Data Model Stable; 0 may mean unspecified; one level per range takes the smallest number | [Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) | "Status: Stable" and "SeverityNumber=0 MAY be used to represent an unspecified value." and "it is recommended to assign that severity the smallest value of the range." | 2026-11-16 | 2027-05-16 |
| `ll-otel-error` | SeverityNumber 17 (ERROR) and up marks an error | [Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) | "If SeverityNumber is present and has a value of ERROR (numeric 17) or higher then it is an indication that the log record represents an erroneous situation." | 2026-11-16 | 2027-05-16 |
| `ll-otel-appendix` | Appendix B maps Log4j (1, 5, 9, 13, 17, 21) and syslog (Notice 10, Critical 18, Alert 19, Emergency 21), as examples | [Appendix](https://opentelemetry.io/docs/specs/otel/logs/data-model-appendix/) | "These examples provided purely for demonstrative purposes and are not exhaustive or canonical" | 2026-11-16 | 2027-05-16 |
| `ll-serilog-trace` | Serilog 3.1 added `TraceId` and `SpanId` | [Serilog v3.1.0](https://github.com/serilog/serilog/releases/tag/v3.1.0) | "This release adds two new first-class properties to LogEvent: TraceId and SpanId." | 2026-11-16 | 2027-05-16 |
| `ll-pino-otel` | `@opentelemetry/instrumentation-pino` 0.71.0 (2026-11-05) adds the span's IDs | [README](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/packages/instrumentation-pino/README.md), [npm](https://registry.npmjs.org/@opentelemetry/instrumentation-pino) | "Pino logger calls in the context of a tracing span will have fields identifying the span added to the log record." and "0.71.0" | 2026-11-16 | 2027-02-16 |
| `ll-pino-redact` | pino's `redact` paths never come from input | [pino API](https://github.com/pinojs/pino/blob/main/docs/api.md) | "Never allow user input to define redacted paths." | 2026-11-16 | 2027-02-16 |
| `ll-java-otel` | Logback MDC and Log4j context-data instrumentation, 2.33.1-alpha (2026-10-26) | [Logback MDC](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/logback/logback-mdc-1.0/library/README.md), [Log4j](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/log4j/log4j-context-data/log4j-context-data-2.17/library-autoconfigure/README.md), [Maven Central](https://repo1.maven.org/maven2/io/opentelemetry/instrumentation/opentelemetry-logback-mdc-1.0/maven-metadata.xml) | "injecting the trace ID and span ID from a mounted span using a custom Logback appender." and "injects trace context from active spans into log context." and "2.33.1-alpha" | 2026-11-16 | 2027-02-16 |
| `ll-logstash-mask` | logstash-logback-encoder 9.0 masks by path or value | [README](https://github.com/logfellow/logstash-logback-encoder/blob/main/README.md), [Maven Central](https://repo1.maven.org/maven2/net/logstash/logback/logstash-logback-encoder/maven-metadata.xml) | "Data to be masked can be identified by path and/or by value." and "9.0" | 2026-11-16 | 2027-02-16 |
| `ll-log4j-rewrite` | Log4j discourages masking with the Rewrite appender | [Delegating appenders](https://logging.apache.org/log4j/2.x/manual/appenders/delegating.html) | "we strongly discourage such practice." | 2026-11-16 | 2027-05-16 |
| `ll-structlog-otel` | structlog's docs add span IDs with a processor | [Frameworks](https://www.structlog.org/en/stable/frameworks.html) | "you can enrich your logs with a straight-forward processor" | 2026-11-16 | 2027-05-16 |
| `ll-semantic-otel` | semantic_logger lists OpenTelemetry as an appender | [README](https://github.com/reidmorrison/semantic_logger) | "OpenTelemetry Appender" | 2026-11-16 | 2027-05-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| [OpenTelemetry](https://opentelemetry.io/docs/specs/otel/logs/data-model/) | Severity, SDK status, instrumentation | Docs CC BY 4.0, code Apache-2.0: quoted with attribution |
| [structlog docs](https://www.structlog.org/en/stable/frameworks.html) | The processor, adapted from its recipe | MIT OR Apache-2.0: adapted with attribution |
| pino, Monolog, winston | Redaction, versions | MIT: facts with short quotes |
| Serilog, semantic_logger, Log4j 2, logstash-logback-encoder | Trace IDs, redaction | Apache-2.0: facts with short quotes |
| Logback, registries | Versions, fixes | Facts with short quotes |

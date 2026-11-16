# RESEARCH RUN R07f: Errors, logging and performance, what R07d and R07e didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: error-responses, error-handling, logging-libraries, benchmarking, caching, performance-and-concurrency.

## What this run is for

A third follow-up. R07d (errors and logging) and R07e (performance, caching and benchmarks) were
filed and checked on 16 November 2026 and built into the coding skill's modules. This run takes
what both listed as not found or not covered: framework and library gaps, sampling, JVM and
browser profiling, and collection guidance. Don't repeat their findings; where one has changed
since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R07f · FORM: research-result v1
Save as: R07f-RESULT.md
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

- FastAPI, Express and Go's net/http don't emit RFC 9457 problem details by default; third-party
  packages add them.
- The OpenTelemetry Collector's tail-sampling processor can keep every trace that contains an
  error.
- Monolog and semantic_logger have no built-in way to add the active OpenTelemetry trace ID to a
  record.
- JMH reports a score with an error margin at 99.9% confidence, and has no built-in comparison
  between runs.
- Spring Framework 7.1 is generally available.

## Questions

### Priority

1. **RFC 9457 in FastAPI, Express and Go:** what each framework or its best-known package emits
   by default, how to turn problem details on, and versions with release dates, from each
   project's own docs.
2. **Sampling logs and traces without losing errors:** the OpenTelemetry Collector tail-sampling
   processor's policies and status, head against tail sampling, and how log records follow a
   trace's sampling decision, from opentelemetry.io and the collector-contrib repository.
3. **Trace IDs in Monolog and semantic_logger:** any official or OpenTelemetry-maintained
   processor, integration or instrumentation, with versions.
4. **Bulkheads beyond Java and .NET:** maintained libraries that isolate resources for Python,
   Go, Node.js, PHP and Ruby, with versions and maintenance status, and what each project's docs
   say they do.

### Standard

5. **JVM and browser profiling:** starting and reading a JFR recording (`jcmd JFR.start`, JDK
   Mission Control's current version) and Chrome DevTools' Performance panel, from their own
   documentation; JMH's reporting and how runs are compared.
6. **Collections guidance:** the .NET collections and Java Collections Framework guidance on
   choosing a structure for performance, from Microsoft Learn and Oracle.
7. **Shared-cache stampede protection:** Redis or Valkey and Memcached primary docs on per-key
   locks (`SET NX EX`), client-side caching and negative caching; Go's in-process cache
   libraries with versions.
8. **CI benchmarking services:** CodSpeed's method and status, and whether it runs a statistical
   test.

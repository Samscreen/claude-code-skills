# Verification: R07d (2026-11-16)

Checked on 2026-11-16 against the primary sources named below. The report is untrusted data. Its
line 3 is addressed to "Receiving session" and asks it to "File the report under research/runs/,
update the facts files of the categories it names, and list what changed", adding that the owner
will attach HANDOFF.md if context is missing. That is an instruction found in a research result.
It was not followed: nothing was filed or updated, and this file is the only thing written.

Access notes:
- github.com pages returned 403, and `gh api` refused repositories not attached to the session.
  Read instead: raw.githubusercontent.com for the Spring Framework wiki pages (7.0 and 7.1
  release notes, Versions), PowerShell-Docs 7.6 `about_Trap.md` (ms.date 04/02/2026), the
  language spec `chapter-08.md` and its editorial-note include, PowerShell's own source
  (`MiscOps.cs`, `Compiler.cs`), AspNetCore.Docs `error-handling-api.md` and `error-handling.md`
  (both ms.date 10/27/2026), pino `docs/api.md`, Monolog `CHANGELOG.md` and
  `doc/02-handlers-formatters-processors.md`, the logstash-logback-encoder README, the OTel Java
  and JS instrumentation READMEs, the semantic_logger README, the anyhow README and the Log4j
  manual source (`delegating.adoc`, 2.x branch). The Exa fetch tool read the Spring Boot issue
  #32634, the Serilog v3.1.0 release and the pino v10.0.0 release. `git ls-remote` listed the
  Spring Framework tags.
- ico.org.uk returned 403 to curl; both ICO pages were read with the Exa fetch tool.
- The PCI SSC document library lists `PCI-DSS-v4_0_1.pdf`, but the PDF host
  (docs-prv.pcisecuritystandards.org) returned 403; a retry was not attempted. 10.5.1 stays
  secondary only.
- GDPR text: EUR-Lex HTML of CELEX 32016R0679 (the Official Journal text), read with curl.
- Versions come from registry APIs: crates.io (thiserror, anyhow), PyPI JSON (structlog), the npm
  registry (pino, @opentelemetry/instrumentation-pino, winston), NuGet flat container and
  registration (Serilog), Maven Central `maven-metadata.xml` and POM `Last-Modified` headers
  (logback-classic, log4j-core, logstash-logback-encoder, OTel Java instrumentation, spring-web,
  spring-boot), Packagist `p2` (Monolog) and RubyGems (semantic_logger). Logback's news page and
  the Log4j release notes were read too. The spring.io project API (`api.spring.io`) gave
  support dates; its `releases` list is stale (it shows 7.0.8 as current while Maven Central has
  7.0.10), so release status comes from Maven Central and the tags.
- PowerShell is not installed here (`pwsh` not found), so `trap` was not run. The derived-type
  question was settled from PowerShell's source instead (below).

| Claim | Status | Checked against |
|---|---|---|
| Spring Boot's `spring.mvc.problemdetails.enabled` / `spring.webflux.problemdetails.enabled` are false by default (C8, F22) | verified. The issue (2022-10-07, bclozel) is a plan: "those properties are `false` by default, as this could be a breaking change for applications". The current properties appendix (Spring Boot 4.1.2) confirms both default to `false` | [Spring Boot #32634](https://github.com/spring-projects/spring-boot/issues/32634) (Exa), [Application properties](https://docs.spring.io/spring-boot/appendix/application-properties/index.html) |
| Spring Framework 7.1: "The instance field of ProblemDetail is no longer set automatically (#35969)." (F23) | verified (backticks around `instance` and `ProblemDetail` in the source) | [7.1 Release Notes](https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-7.1-Release-Notes) (raw) |
| 7.1 MVC "can now render any unhandled exception as an RFC 9457 problem detail" without a `@ControllerAdvice` (F24, summary) | verified with a correction: it is **opt-in**: "This is opt-in through `WebMvcConfigurer`", via `configureProblemDetails(...)` calling `configurer.renderUnhandledExceptions(true)` (#37398). It is not a new default | same |
| "Any other exception results in a generic 500 response. The exception message is never exposed." | verified (applies only with the opt-in on) | same |
| Spring Framework 7.1 is not GA; "scheduled for November 2026"; newest tag v7.1.0-RC2 (5 Nov 2026) | verified on 2026-11-16: no `v7.1.0` tag (newest `v7.1.0-RC2`); Maven Central's newest spring-web is 7.1.0-RC2 (POM 2026-11-05T11:59Z); the wiki still reads "This is a preview page for Spring Framework 7.1.0, scheduled for November 2026." The spring.io generations API gives 7.1.x an initial release of **2026-11-30**, OSS support to 2027-12-31 and commercial to 2028-12-31 | `git ls-remote`, [Maven Central](https://repo1.maven.org/maven2/org/springframework/spring-web/maven-metadata.xml), [api.spring.io generations](https://api.spring.io/projects/spring-framework/generations) |
| Spring Framework 7.0 no longer sets `type` by default (C8; secondary ankurm.com in the report) | verified (at the primary source): the 6.2.19 javadoc says of `setType` "By default, this is BLANK_TYPE." and `getType()` is non-null; the 7.0.10 javadoc says "By default, this is not set." and `getType()` is `@Nullable` | [ProblemDetail 7.0.10](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/ProblemDetail.html), [ProblemDetail 6.2.19](https://docs.spring.io/spring-framework/docs/6.2.x/javadoc-api/org/springframework/http/ProblemDetail.html) |
| Current javadoc is 7.0.10: "According to the spec, when not present, the type is assumed to be "about:blank"" (F25) | verified | [ProblemDetail 7.0.10](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/ProblemDetail.html) |
| Spring Framework 6.2.x "Open source support ends in June 2026" | verified (API: 2026-06-30; 7.0.x OSS ends 2027-07-31) | [Spring Framework Versions](https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-Versions) (raw), api.spring.io |
| Spring Boot current line | not in the report as a fact: Boot 4.1.2 is the docs' current version; Maven Central's newest is 4.2.0-RC2 (2026-11-05) | Maven Central, Boot docs |
| ASP.NET Core: "The automatic creation of a `ProblemDetails` for error status codes is enabled by default." (F26) | verified (for web API controllers) | [Handle errors in ASP.NET Core APIs](https://learn.microsoft.com/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0) |
| "In ASP.NET Core 11 and later, `UseExceptionHandler` preserves `BadHttpRequestException.StatusCode` by default in problem details responses." (F27) | verified | same |
| `AddProblemDetails` "registers the default `IProblemDetailsService` implementation"; ExceptionHandlerMiddleware "when a custom handler is not defined", StatusCodePagesMiddleware "by default" | verified | same |
| Non-JSON types "such as `application/xml` or `text/html`, are not supported and trigger the fallback behavior" | verified | same |
| Default exception body has `"type":"https://tools.ietf.org/html/rfc7231#section-6.6.1"`; some pages still link RFC 7807 | verified with a correction: the `rfc7231` body is on **Handle errors in ASP.NET Core** (`fundamentals/error-handling`, 10.0 moniker), not the API page, and it is introduced as "a standard ProblemDetails response" linking RFC 7807. The API page says "RFC 7807-compliant payload" three times | [Handle errors in ASP.NET Core](https://learn.microsoft.com/aspnet/core/fundamentals/error-handling?view=aspnetcore-10.0) (raw markdown) |
| "Do **not** serve sensitive error information to clients." | verified with a correction (the same page correction); it continues "Serving errors is a security risk." | same |
| OTel Logs Data Model "Status: Stable", spec 1.62.0 (F1) | verified | [Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) |
| `SeverityNumber=0` MAY mean unspecified; ERROR (17) or higher is erroneous; single severity gets the smallest value; missing severity may be read as INFO (9) (F2-F5) | verified, each sentence as quoted | same |
| Six ranges; short names TRACE, TRACE2 ... FATAL4; display as "INFO (Informational)" | verified at the spec itself (the report cited the collector-contrib repository for the short names) | same |
| Appendix B Syslog mapping (Notice→10, Critical→18, Alert→19, Emergency→21) and "purely for demonstrative purposes and are not exhaustive or canonical" | verified with a correction (the source reads "These examples provided purely for demonstrative purposes..."). For §4.4 and §9: Appendix B is a multi-format table with a **Log4j** column (TRACE 1, DEBUG 5, INFO 9, WARN 13, ERROR 17, FATAL 21), plus java.util.logging, Zap, ETW and .NET `Microsoft.Extensions.Logging`. So a non-canonical spec mapping does exist for Log4j; it matches the report's derived row | [Data Model Appendix](https://opentelemetry.io/docs/specs/otel/logs/data-model-appendix/) |
| Serilog 3.1: "This release adds two new first-class properties to LogEvent: TraceId and SpanId."; set "from System.Diagnostics.Activity.Current" (F30) | verified (release published 2023-11-09; #1955 marked breaking) | [Serilog v3.1.0](https://github.com/serilog/serilog/releases/tag/v3.1.0) (Exa) |
| Serilog 4.4.0 (2026-07-10) | verified (2026-07-10T03:35Z; Apache-2.0 in the nuspec) | NuGet registration |
| pino 10.4.0 (2026-10-02); 10.3.1 on 2026-02-09 | verified (2026-10-02T18:18Z, MIT) | [npm registry](https://registry.npmjs.org/pino) |
| pino 10 dropped Node.js 18 (secondary in the report) | verified (at the primary source): "The only breaking change is dropping support for Node 18." (v10.0.0, 2025-10-03) | [pino v10.0.0](https://github.com/pinojs/pino/releases/tag/v10.0.0) (Exa) |
| pino `redact`, `censor` default "[Redacted]", "Never allow user input to define redacted paths." | verified (the source reads "**WARNING**: Never allow user input to define redacted paths.") | [pino api.md](https://github.com/pinojs/pino/blob/main/docs/api.md) (raw) |
| `@opentelemetry/instrumentation-pino`: "Pino logger calls in the context of a tracing span will have fields identifying the span added to the log record."; fields `trace_id`, `span_id`, `trace_flags`. Version "not found" | verified; version now found: **0.71.0 (2026-11-05)**, Apache-2.0 | [README](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/packages/instrumentation-pino/README.md) (raw), [npm](https://registry.npmjs.org/@opentelemetry/instrumentation-pino) |
| Logback 1.6.5 (2026-09-30) is current (§4.5, Tools) | contradicted: 1.6.5's date is right, but **1.6.6 (2026-10-25)** and **1.6.7 (2026-11-14)** followed. 1.6.7 is current | [Logback news](https://logback.qos.ch/news.html), [Maven Central](https://repo1.maven.org/maven2/ch/qos/logback/logback-classic/maven-metadata.xml) (POM 2026-11-14T16:05Z) |
| `opentelemetry-logback-mdc-1.0`: "injecting the trace ID and span ID from a mounted span using a custom Logback appender." Version "not found" | verified; version found: 2.33.1-alpha (2026-10-26) | [README](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/logback/logback-mdc-1.0/library/README.md) (raw), Maven Central |
| logstash-logback-encoder: "Data to be masked can be identified by path and/or by value." Version "not found" | verified (link text in the source); version found: 9.0 (2025-10-26) | [README](https://github.com/logfellow/logstash-logback-encoder/blob/main/README.md) (raw), Maven Central |
| Log4j 2.26.1, date contested (2026-07-02 per versio.io) | verified with a correction: **2026-06-29** ("2.26.1 Release date 2026-06-29"; POM 2026-06-29T07:44Z). 2.25.5 is 2026-07-01. versio.io is wrong. Still the newest 2.x | [Log4j release notes](https://logging.apache.org/log4j/2.x/release-notes.html), Maven Central |
| `opentelemetry-log4j-context-data-2.17-autoconfigure` "injects the trace ID and span ID from an active span into Log4j's context data"; "Use `%X{trace_id}`" | verified with a correction: the README now reads "provides a Log4j2 `ContextDataProvider` that injects trace context from active spans into log context." It names no `%X{trace_id}` pattern (that pattern is in the Logback README). Version 2.33.1-alpha | [README](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/log4j/log4j-context-data/log4j-context-data-2.17/library-autoconfigure/README.md) (raw) |
| Log4j Rewrite appender: "Although this appender can be used to mask sensitive information contained in log events, we strongly discourage such practice." | verified (manual source, 2.x branch) | [Delegating Appenders](https://logging.apache.org/log4j/2.x/manual/appenders/delegating.html) |
| Monolog 3.12.1 (2026-09-29); `RedactingFormatter` added in 3.11.0 (2026-09-02) (F31) | verified (Packagist: 3.12.1 2026-09-29T19:21Z, 3.11.0 2026-09-02T12:39Z). As R07b found, 3.12.0 and 3.12.1 fixed `RedactingFormatter` leaks, so the floor is 3.12.1 | [Packagist](https://repo.packagist.org/p2/monolog/monolog.json), [CHANGELOG](https://github.com/Seldaek/monolog/blob/main/CHANGELOG.md) (raw) |
| Monolog docs: "masks the value of any context/extra key matching a configured name (e.g. password, token, authorization)" | verified (names in backticks in the source) | [doc/02](https://github.com/Seldaek/monolog/blob/main/doc/02-handlers-formatters-processors.md) (raw) |
| semantic_logger 5.1.0 (2026-07-20) is current | contradicted: **5.2.0 (2026-10-30T22:30Z)** is current (as R07b found); 5.1.0's date is right | [RubyGems API](https://rubygems.org/api/v1/versions/semantic_logger.json) |
| semantic_logger README lists OpenTelemetry only as a destination | verified ("OpenTelemetry Appender: gem 'opentelemetry-logs-sdk'") | [README](https://github.com/reidmorrison/semantic_logger) (raw) |
| structlog 26.1.0 (2026-06-06); `add_open_telemetry_spans` recipe writing `span_id` and `trace_id` | verified (PyPI 2026-06-06T07:33Z, `MIT OR Apache-2.0`) | [PyPI](https://pypi.org/pypi/structlog/json), [Frameworks](https://www.structlog.org/en/stable/frameworks.html) |
| Breyer press release 112/16, 19 October 2016 (F6, F7) | verified. Quotes carry curly quotes (‘online media services provider’) and a footnote marker: "constitutes personal data2 with respect to the operator" | [CJEU press release 112/16](https://curia.europa.eu/site/upload/docs/application/pdf/2016-10/cp160112en.pdf) |
| Breyer interpreted Directive 95/46/EC, not the GDPR (C6) | verified: footnote 2 reads "Within the meaning of Directive 95/46/EC". Article numbers (2(a), 7(f)) not checked in the judgment itself | same |
| GDPR Art. 4(1) includes "an online identifier" | verified (EUR-Lex; curly ‘ ’ around the defined terms) | [Regulation (EU) 2016/679](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679) |
| GDPR Art. 5(1)(c) "adequate, relevant and limited to what is necessary" | verified; it continues "in relation to the purposes for which they are processed (‘data minimisation’)" | same |
| GDPR Art. 5(1)(e) (C7) | verified at EUR-Lex and as ICO reproduces it | same, [ICO storage limitation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/) |
| GDPR Art. 32(1)(a) "the pseudonymisation and encryption of personal data" | verified, under "including inter alia as appropriate:" | EUR-Lex |
| ICO: "You must not keep personal data for longer than you need it." (F12) | verified. The page now carries a banner: "Due to changes made by the Data (Use and Access) Act, this guidance is under review and may be subject to change." | [ICO storage limitation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/) (Exa) |
| ICO breach logs: "Set out a retention period for breach logs..." and "Take steps to periodically reduce the personal information held in breach logs..." (F13) | verified (same "under review" banner) | [ICO breach logging](https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/personal-data-breach-management/breach-identification-assessment-and-logging/) (Exa) |
| CNIL délibération 2021-122 of 14 October 2021: six months to one year, up to three years when justified (F8, F9) | verified; the page uses a curly apostrophe (d’assurer) | [CNIL](https://www.cnil.fr/fr/la-cnil-publie-une-recommandation-relative-aux-mesures-de-journalisation) |
| CNIL: logs "doivent ne pas inclure de données personnelles du traitement principal" for processing kept under six months | verified (a table row: "Les journaux doivent ne pas inclure...") | same |
| CNIL security sheet: "Conserver ces évènements sur une période glissante comprise entre six mois et un an" (F10) | verified | [Sécurité : Tracer les opérations](https://www.cnil.fr/fr/securite-tracer-les-operations) |
| EDPB Guidelines 9/2022 v2.0, footnote 26 (F11) | verified | [EDPB 9/2022 v2.0](https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf) |
| OWASP: "must not be destroyed before ... and must not be kept beyond this time." (F14) | verified | [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) |
| PCI DSS v4.0.1 10.5.1: 12 months, three months immediately available (F15) | secondary only: the PCI SSC PDF returned 403. The same sentence appears on Microsoft Learn's Entra PCI page and several compliance sites; none is PCI SSC | [Microsoft Entra and PCI-DSS Requirement 10](https://learn.microsoft.com/en-us/entra/standards/pci-requirement-10) |
| NIST SP 800-92 final, "09/13/06: SP 800-92 (Final)" (F16) | verified | [SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) |
| SP 800-92 Rev. 1 IPD: "Date Published: October 11, 2023 Comments Due: November 29, 2023" (F17) | verified (the page adds "(public comment period is CLOSED)"); no final (`/r1/final` returns 404) | [SP 800-92r1 ipd](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd) |
| "NIST is in the process of addressing public comments on Draft Special Publication (SP) 800-92 Revision 1" (F18) | verified (the text is the CSRC Log Management project's summary, shown in search) | [CSRC search](https://csrc.nist.gov/search?keywords=800-92), [Log Management project](https://csrc.nist.gov/projects/log-management) |
| Rev. 1 "replaces the original SP 800-92" once final | unverifiable: not on the IPD page as fetched | [SP 800-92r1 ipd](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd) |
| thiserror 2.0.21 (2026-09-23), MIT OR Apache-2.0 (F19) | verified (2026-09-23T20:24Z). Not in the report: 2.0.21's MSRV is **1.77** (2.0.19-2.0.20: 1.71) | [crates.io API](https://crates.io/api/v1/crates/thiserror) |
| anyhow 1.0.104 (2026-07-18), MSRV 1.68.0 (F20, F21) | verified (2026-07-18T20:59Z; `rust_version` 1.68) | [crates.io API](https://crates.io/api/v1/crates/anyhow) |
| thiserror 2.0.0 (2024-11-06); 1.0.69 (2024-11-10) the last 1.x | verified | crates.io API |
| anyhow README "Comparison to thiserror" quote | verified | [anyhow README](https://github.com/dtolnay/anyhow) (raw) |
| MDN `Error()`: "If you omit options, pass a primitive value as options, or pass an object without the cause property, then the created Error object will have no cause property." (C1) | verified | [Error() constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/Error) |
| MDN `cause`: "represents a single failing site..."; `throw new Error("Connecting to database failed.", { cause: err });` | verified | [Error: cause](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause) |
| TypeScript needs ES2022 lib for `new Error(msg, { cause })` (secondary in the report) | verified (at the primary source) for the lib: `lib.es2022.error.d.ts` declares `interface ErrorOptions { cause?: unknown; }` and `new (message?: string, options?: ErrorOptions): Error`. The `TS2554` code was not checked | [typescript@5.9.3 lib](https://unpkg.com/typescript@5.9.3/lib/lib.es2022.error.d.ts) |
| Rust Book: "returning Result is a good default choice when you're defining a function that might fail." (C2) | verified; the official book has a curly apostrophe ("you’re") | [Rust Book 9.3](https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html) |
| "When you choose to return a Result value, you give the calling code options rather than making the decision for it" | verified with a correction: the current book reads "When you choose to return a Result value, you give the calling code options." The report quoted an old-edition mirror (phaiax.github.io) | same |
| "When a bad state is reached, but it's expected to happen no matter how well you write your code, it's still more appropriate to return a Result rather than making a panic! call" | contradicted (not in the current book): it now reads "However, when failure is expected, it’s more appropriate to return a Result than to make a panic! call." | same |
| `panic = 'abort'` in a Cargo profile | verified | [Rust Book 9.1](https://doc.rust-lang.org/book/ch09-01-unrecoverable-errors-with-panic.html) |
| Java `Throwable(String, Throwable)`: "the detail message associated with cause is not automatically incorporated in this throwable's detail message." (C3) | verified (Java SE 21; "not" is italic) | [Throwable (SE 21)](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) |
| Java Tutorials checked/unchecked rule | verified | [Unchecked Exceptions](https://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html) |
| PHP `Exception::__construct(... ?Throwable $previous = null)`; user note on internal exceptions (C4) | verified (the note is a user contribution, so secondary as the report says) | [Exception::__construct](https://www.php.net/manual/en/exception.construct.php) |
| PHP `Error::__construct` has `?Throwable $previous = null` | verified | [Error::__construct](https://www.php.net/manual/en/error.construct.php) |
| Ruby `raise`: cause "is automatically set to the 'current' exception ($!), if any"; `:cause` overrides (C5) | verified at ruby-doc.org 3.3.2, with curly quotes: “current”. Ruby 3.4's Kernel page puts it as "If keyword argument cause is not given, the cause is the value of $!." | [Kernel 3.3.2](https://ruby-doc.org/3.3.2/Kernel.html), [Kernel 3.4](https://docs.ruby-lang.org/en/3.4/Kernel.html) |
| Ruby: "if none is given, StandardError is assumed."; library base-class practice | verified (the base-class sentence has curly quotes around “generic”) | [exceptions 3.4](https://docs.ruby-lang.org/en/3.4/exceptions_md.html), [Exception 3.3](https://docs.ruby-lang.org/en/3.3/Exception.html) |
| `$InformationPreference` default SilentlyContinue (F28); `Write-Host` wraps `Write-Information` since 5.0 (F29) | verified | [Write-Information (7.6)](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/write-information?view=powershell-7.6) |
| `Test-Info 6> Info.txt`; record properties | verified; records also carry `NativeThreadId` and `ManagedThreadId` | same |
| about_Trap: "The `trap` keyword can handle both kinds."; default display and continue; hoisting; "the first `trap` defined lexically (highest in the scriptblock) is used." | verified | [about_Trap (7.6)](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_trap?view=powershell-7.6) (raw) |
| about_Trap: `trap [System.Exception]` "traps any errors raised by unknown commands. It also traps other error types." | verified. The page also says "PowerShell searches for the `trap` with the most specific match" | same |
| Spec §8.8: "a `trap` statement matches an exception type exactly; no derived type matching is performed" (contested) | verified with a correction (the text is there, but out of date): the spec is the Windows PowerShell 3.0 specification (December 2012), and its editorial note says it "does not reflect the current state of PowerShell". PowerShell's trap dispatch (`FindMatchingHandlerByType`, used for `funcContext._traps`) tries an exact match, then `exceptionType.IsSubclassOf(types[i])`, then the untyped trap. **Derived types match** in current PowerShell. Not run: `pwsh` is not installed | [Spec chapter 8](https://learn.microsoft.com/powershell/scripting/lang-spec/chapter-08), [MiscOps.cs](https://github.com/PowerShell/PowerShell/blob/master/src/System.Management.Automation/engine/runtime/Operations/MiscOps.cs) (raw) |
| Azure bulkhead: "Isolate the elements..."; "Projects like resilience4j and Polly offer a framework for creating consumer bulkheads."; platform controls; "Don't re-create these throttling and isolation mechanisms in your application code."; combine "with retry, circuit breaker, and throttling patterns" | verified | [Bulkhead pattern](https://learn.microsoft.com/azure/architecture/patterns/bulkhead) |
| Windows writing style: "doesn't blame the user"; "Be warm and relaxed", "Be ready to lend a hand", "Be crisp and clear" | verified | [Writing style](https://learn.microsoft.com/windows/apps/design/style/writing-style) |
| Win32 Error Message Guidelines: three questions; "Avoid the word 'please'. It can be interpreted to mean that a required action is optional." | verified with a correction: the source uses double quotes: Avoid the word "please". | [Error Message Guidelines](https://learn.microsoft.com/windows/win32/debug/error-message-guidelines) |
| Windows UX Style and Tone allows "please" when the user is inconvenienced | verified: "Limit please to situations that inconvenience the user in some way"; the Error Messages guideline says the same | [Style and Tone](https://learn.microsoft.com/windows/win32/uxguide/text-style-tone), [Error Messages](https://learn.microsoft.com/windows/win32/uxguide/mess-error) |
| NN/g heuristic 9 | verified | [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| NN/g Error-Message Guidelines (Neusesser and Sunwall, May 14, 2023): "Display the error message close to the error's source." and "Use human-readable language." | verified | [Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/) |
| NN/g Hostile Patterns: "Avoid premature error messages: Display error messages only after the error has been made." | verified | [Hostile Patterns](https://www.nngroup.com/articles/hostile-error-messages/) |
| Licences (§8) | see Licences below: EUR-Lex is CC BY 4.0, not "reuse with acknowledgement"; OpenTelemetry's spec repository is Apache-2.0, but opentelemetry.io pages say "Docs CC BY 4.0" | licence pages |

Counts: 68 verified (3 of them checked at a primary source for claims the report gave as
secondary), 9 verified with a correction, 3 contradicted (Logback as current, semantic_logger as
current, the Rust Book "bad state" sentence), 1 unverifiable ("replaces the original SP 800-92")
and 1 secondary only (PCI DSS 10.5.1). Items the report marked secondary or "not found" and now
checked at a primary source: pino 10's Node 18 drop, Spring 7.0's `type` default, the TypeScript
ES2022 lib, the OTel short names, and versions for instrumentation-pino, logback-mdc,
logstash-logback-encoder and the Log4j context-data module. The `trap` contest is settled from
PowerShell's source, not by running it: derived types match.

## Exact quotes for facts rows

Copied from the source text. Straight quotes unless noted. Backticks that mark code in Markdown
sources are left out.

| Fact | URL | Quote |
|---|---|---|
| GDPR: online identifier | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679 | "by reference to an identifier such as a name, an identification number, location data, an online identifier" |
| GDPR: personal data defined | same | "‘personal data’ means any information relating to an identified or identifiable natural person" (curly ‘ ’, U+2018/U+2019) |
| GDPR: data minimisation | same | "adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed" |
| GDPR: storage limitation | same | "kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed" |
| GDPR: security measures | same | "the pseudonymisation and encryption of personal data" |
| Breyer: dynamic IP | https://curia.europa.eu/site/upload/docs/application/pdf/2016-10/cp160112en.pdf | "The dynamic internet protocol address of a visitor constitutes personal data, with respect to the operator of the website, if that operator has the legal means allowing it to identify the visitor" |
| Breyer: cyberattacks | same | "The operator of a website may have a legitimate interest in storing certain personal data relating to visitors to that website in order to protect itself against cyberattacks" |
| EDPB: logs as personal data | https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf | "log data facilitating auditability of, e.g., storage, modifications or erasure of data may also qualify as personal data relating to the person who initiated the respective processing operation." |
| ICO storage limitation | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/ | "You must not keep personal data for longer than you need it." |
| ICO breach logs | https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/personal-data-breach-management/breach-identification-assessment-and-logging/ | "Set out a retention period for breach logs that contain personal information and establish a lawful basis for their retention." |
| CNIL default retention | https://www.cnil.fr/fr/la-cnil-publie-une-recommandation-relative-aux-mesures-de-journalisation | "pour une durée comprise entre six mois et un an" |
| CNIL longer retention | same | "avec dans les cas les plus courants une durée maximale de trois ans" |
| CNIL rolling window | https://www.cnil.fr/fr/securite-tracer-les-operations | "Conserver ces évènements sur une période glissante comprise entre six mois et un an" (è in "évènements") |
| OWASP retention bounds | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | "must not be destroyed before the duration of the required data retention period, and must not be kept beyond this time." |
| NIST SP 800-92 final | https://csrc.nist.gov/pubs/sp/800/92/final | "09/13/06: SP 800-92 (Final)" |
| NIST r1 draft | https://csrc.nist.gov/pubs/sp/800/92/r1/ipd | "Date Published: October 11, 2023" |
| OTel status | https://opentelemetry.io/docs/specs/otel/logs/data-model/ | "Status: Stable" |
| OTel unspecified | same | "SeverityNumber=0 MAY be used to represent an unspecified value." |
| OTel error threshold | same | "If SeverityNumber is present and has a value of ERROR (numeric 17) or higher then it is an indication that the log record represents an erroneous situation." |
| OTel single level | same | "it is recommended to assign that severity the smallest value of the range." |
| OTel appendix caveat | https://opentelemetry.io/docs/specs/otel/logs/data-model-appendix/ | "These examples provided purely for demonstrative purposes and are not exhaustive or canonical" |
| Spring Boot default off | https://docs.spring.io/spring-boot/appendix/application-properties/index.html | "Whether RFC 9457 Problem Details support should be enabled." (default column: false) |
| Spring 7.0 `type` unset | https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/ProblemDetail.html | "By default, this is not set. According to the spec, when not present, the type is assumed to be "about:blank"" |
| Spring 7.1 `instance` | https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-7.1-Release-Notes | "The instance field of ProblemDetail is no longer set automatically" |
| Spring 7.1 opt-in | same | "This is opt-in through WebMvcConfigurer" |
| Spring 7.1 status | same | "This is a preview page for Spring Framework 7.1.0, scheduled for November 2026." |
| ASP.NET controllers | https://learn.microsoft.com/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0 | "The automatic creation of a ProblemDetails for error status codes is enabled by default." |
| ASP.NET Core 11 | same | "In ASP.NET Core 11 and later, UseExceptionHandler preserves BadHttpRequestException.StatusCode by default in problem details responses." |
| ASP.NET no sensitive detail | https://learn.microsoft.com/aspnet/core/fundamentals/error-handling?view=aspnetcore-10.0 | "Do not serve sensitive error information to clients. Serving errors is a security risk." ("not" bold) |
| Serilog trace IDs | https://github.com/serilog/serilog/releases/tag/v3.1.0 | "This release adds two new first-class properties to LogEvent: TraceId and SpanId." |
| pino redact warning | https://github.com/pinojs/pino/blob/main/docs/api.md | "Never allow user input to define redacted paths." |
| pino OTel fields | https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/packages/instrumentation-pino/README.md | "Pino logger calls in the context of a tracing span will have fields identifying the span added to the log record." |
| Logback MDC | https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/logback/logback-mdc-1.0/library/README.md | "injecting the trace ID and span ID from a mounted span using a custom Logback appender." |
| Log4j context data | https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/log4j/log4j-context-data/log4j-context-data-2.17/library-autoconfigure/README.md | "injects trace context from active spans into log context." |
| Log4j Rewrite | https://logging.apache.org/log4j/2.x/manual/appenders/delegating.html | "we strongly discourage such practice." |
| Logback current | https://logback.qos.ch/news.html | "2026-11-14 Release of logback version 1.6.7" |
| Log4j 2.26.1 date | https://logging.apache.org/log4j/2.x/release-notes.html | "2.26.1 Release date 2026-06-29" (heading and line) |
| pino 10 | https://github.com/pinojs/pino/releases/tag/v10.0.0 | "The only breaking change is dropping support for Node 18." |
| anyhow vs thiserror | https://github.com/dtolnay/anyhow | "Use Anyhow if you don't care what error type your functions return, you just want it to be easy. This is common in application code." |
| Rust: Result default | https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html | "returning Result is a good default choice when you’re defining a function that might fail." (curly ’) |
| Rust: expected failure | same | "However, when failure is expected, it’s more appropriate to return a Result than to make a panic! call." (curly ’) |
| Java cause message | https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html | "the detail message associated with cause is not automatically incorporated in this throwable's detail message." |
| JS cause absent | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/Error | "then the created Error object will have no cause property." |
| Ruby cause | https://ruby-doc.org/3.3.2/Kernel.html | "is automatically set to the “current” exception ($!), if any." (curly “ ”) |
| Ruby bare rescue | https://docs.ruby-lang.org/en/3.4/exceptions_md.html | "if none is given, StandardError is assumed." |
| PowerShell info silent | https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/write-information?view=powershell-7.6 | "Because the default value of this variable is SilentlyContinue, by default, informational messages are not shown." |
| trap handles both | https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_trap?view=powershell-7.6 | "The trap keyword can handle both kinds." |
| trap: base type catches derived | same | "This statement traps any errors raised by unknown commands. It also traps other error types." |
| Bulkhead libraries | https://learn.microsoft.com/azure/architecture/patterns/bulkhead | "Projects like resilience4j and Polly offer a framework for creating consumer bulkheads." |
| Bulkhead: use the platform | same | "Don't re-create these throttling and isolation mechanisms in your application code." |
| Microsoft: no blame | https://learn.microsoft.com/windows/apps/design/style/writing-style | "it's important that your error message doesn't blame the user." |
| NN/g heuristic 9 | https://www.nngroup.com/articles/ten-usability-heuristics/ | "Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution." |

## Versions found from registries

| Tool | Current version | Released (UTC) | Source |
|---|---|---|---|
| thiserror | 2.0.21 (MSRV 1.77) | 2026-09-23 | crates.io API |
| anyhow | 1.0.104 (MSRV 1.68) | 2026-07-18 | crates.io API |
| structlog | 26.1.0 | 2026-06-06 | PyPI JSON |
| pino | 10.4.0 | 2026-10-02 | npm registry |
| @opentelemetry/instrumentation-pino | 0.71.0 | 2026-11-05 | npm registry |
| winston | 3.19.0 | 2025-12-07 | npm registry |
| Serilog | 4.4.0 | 2026-07-10 | NuGet |
| Logback (logback-classic) | **1.6.7** | **2026-11-14** | Logback news, Maven Central |
| logstash-logback-encoder | 9.0 | 2025-10-26 | Maven Central |
| opentelemetry-logback-mdc-1.0, opentelemetry-log4j-context-data-2.17-autoconfigure | 2.33.1-alpha | 2026-10-26 | Maven Central |
| Log4j (log4j-core) | 2.26.1 (2.25 line: 2.25.5, 2026-07-01; Maven's `<latest>` is 3.0.0-beta3, a prerelease) | **2026-06-29** | Log4j release notes, Maven Central |
| SLF4J (slf4j-api) | 2.0.20 | (unchanged since R07b) | Maven Central |
| Monolog | 3.12.1 | 2026-09-29 | Packagist |
| semantic_logger | **5.2.0** | **2026-10-30** | RubyGems API |
| Spring Framework (spring-web) | 7.0.10 GA; 7.1.0-RC2 newest (no 7.1.0 GA on 2026-11-16; planned 2026-11-30) | 7.0.10: 2026-10-22; RC2: 2026-11-05 | Maven Central, tags, api.spring.io |
| Spring Boot | 4.1.2 (docs current); 4.2.0-RC2 newest | RC2: 2026-11-05 | Maven Central, Boot docs |
| ASP.NET Core docs | 10.0 view; ASP.NET Core 11 behaviour documented | docs ms.date 2026-10-27 | AspNetCore.Docs |
| PowerShell docs | 7.6 (about_Trap ms.date 2026-04-02) | n/a | PowerShell-Docs |

## Licences

| Source | Licence as stated | What an Apache-2.0 repository may do |
|---|---|---|
| EUR-Lex (GDPR text) | "licensed under the Creative Commons Attribution 4.0 International licence" for EU-owned documents (legal notice) | Quote, paraphrase, adapt with attribution |
| OpenTelemetry | opentelemetry.io footer "Docs CC BY 4.0"; the specification repository's LICENSE is Apache-2.0 | Quote, paraphrase, adapt with attribution |
| MDN | "Content available under a Creative Commons license" (version not re-read) | Quote briefly with attribution; paraphrase |
| PHP manual | "Creative Commons Attribution 3.0 License or later" | Quote, paraphrase with attribution |
| Rust Book | MIT and Apache-2.0 LICENSE files | Quote, paraphrase, adapt with attribution |
| OWASP Cheat Sheets | "Creative Commons Attribution-ShareAlike 4.0 International" | Quote briefly with attribution; paraphrase; write our own rather than adapt |
| Microsoft Learn, PowerShell-Docs | CC BY 4.0 docs, MIT code (R07b, PowerShell-Docs LICENSE files) | Quote, paraphrase, adapt with attribution |
| Oracle Java docs | "Copyright © 1993, 2025, Oracle and/or its affiliates" | Brief quotes, cited; paraphrase |
| NN/g | "Copyright © 1998-2026 Nielsen Norman Group, All Rights Reserved." | Brief quotes, cited; paraphrase |
| ICO, CNIL, EDPB, CJEU, NIST, PCI SSC | not re-checked this run | Brief quotes, cited; paraphrase |
| thiserror, anyhow, structlog | MIT OR Apache-2.0 (crates.io, PyPI) | Adapt code with attribution |
| Serilog, semantic_logger, @opentelemetry/instrumentation-pino | Apache-2.0 (nuspec, RubyGems, npm) | Adapt code with attribution and NOTICE |
| pino, Monolog, winston | MIT (registries) | Adapt code keeping the notice |
| Logback | not re-checked (the report's EPL-1.0/LGPL-2.1 is unverified) | Cite; avoid copying source |

## Repository facts this contradicts

`git grep -n` over `skills/` for Logback, Log4j, Monolog, semantic_logger, structlog, pino,
Serilog, thiserror, anyhow, Spring, ASP.NET, RFC 9457/7807, ProblemDetail(s), GDPR, PCI,
800-92, CNIL, Breyer, retention, SeverityNumber, trap, Write-Information, Write-Host and cause,
with `skills/coding/references/error-handling.md`, `logging-and-observability.md`,
`javascript-coding.md` and `powershell-scripts.md` read where they matched.

Now wrong:

- `lo-java-libs` (`skills/coding/references/logging-and-observability.md`, line 180): "Logback
  1.6.6 (2026-10-25)" and quote "2026-10-25 Release of logback version 1.6.6". Correct: **Logback
  1.6.7, released 2026-11-14** ("2026-11-14 Release of logback version 1.6.7",
  [Logback news](https://logback.qos.ch/news.html); Maven Central POM 2026-11-14T16:05Z). SLF4J
  2.0.20 in the same row still holds.

Still right: `lo-libs` (structlog 26.1.0, pino 10.4.0, winston 3.19.0, Serilog 4.4.0,
semantic_logger 5.2.0), `lo-log4j-cve` (2.26.1 still the newest 2.x), `lo-php-monolog` (3.12.1
still current), `ps-write-host` ("Write-Host is a wrapper for Write-Information" is still on the
7.6 Write-Information page), `eh-js-cause`, `eh-rfc9457` and `eh-rfc9457-members`.

`error-handling.md` makes no claim that ASP.NET Core or Spring emits RFC 9457 by default, so the
report's main correction contradicts nothing there. Gaps R07d fills rather than errors:
`error-handling.md` says "Bulkheads and hedging weren't researched here";
`logging-and-observability.md` says "Data protection law and retention periods aren't covered
here" and "Other libraries' redaction wasn't checked"; `powershell-scripts.md` has no `trap` or
information-stream guidance; `javascript-coding.md` sets `"target": "esnext"`, which already
includes the ES2022 `ErrorOptions`.

---

# R07d: Errors and logging, what R07 and R07b didn't reach

The most important correction from this run is that neither ASP.NET Core nor Spring Boot produces RFC 9457 problem details for every error "out of the box". ASP.NET Core does so automatically only for `[ApiController]` error status codes; exceptions and empty-body status codes need `AddProblemDetails()` plus middleware. Spring Boot's `spring.mvc.problemdetails.enabled` is off by default.\[1\] Spring Framework 7.x also changed the defaults for `type` and `instance`.\[2\] The other four beliefs are broadly correct but need precision, noted under Corrections.

Dates: sources were read 2026-11-15 unless a source date is given. The run had a fixed search budget. Where I could not fetch a primary page, the item says "not re-fetched in this run" or "not found" instead of guessing.

## 1. Summary

- **RFC 9457 is not on by default in Spring Boot.** Spring Boot maintainers set `spring.mvc.problemdetails.enabled` / `spring.webflux.problemdetails.enabled` to "false by default, as this could be a breaking change for applications".\[1\] Spring Framework 7.1 adds rendering of any unhandled exception as a problem detail without a `@ControllerAdvice`, and stops setting `instance` automatically.\[2\]
- **ASP.NET Core:** for controllers, "The automatic creation of a `ProblemDetails` for error status codes is enabled by default". For exceptions and empty-body 4xx/5xx you must call `AddProblemDetails()` together with `UseExceptionHandler()` / `UseStatusCodePages()`. The default exception body still carries an RFC 7231 `type` URI, and some Learn pages still link RFC 7807.\[3\]
- **The OpenTelemetry Logs Data Model is Stable** (spec 1.62.0). SeverityNumber runs 1–24 in six ranges (TRACE 1–4 … FATAL 21–24). `0` MAY mean "unspecified", and 17 or above signals an error.\[4\]
- **No per-library OTel severity mapping was found** in primary sources for structlog, pino, Serilog, Logback, Log4j 2, Monolog or semantic_logger. Use the spec rule: a single level in a range gets the smallest value in that range.\[4\]
- **Trace correlation:** Serilog has had built-in `TraceId`/`SpanId` from `Activity.Current` since 3.1.\[5\] pino, Logback and Log4j 2 rely on official OpenTelemetry instrumentation packages.\[6\]\[7\]\[8\] structlog has only a docs recipe.\[9\] No primary source was found for Monolog or for semantic_logger auto-injection.
- **Redaction is uneven across libraries.** pino has `redact`,\[10\] and Monolog 3.11.0 added `RedactingFormatter`. Logback masking comes from the third-party logstash-logback-encoder. Log4j 2 now "strongly discourage[s]" masking with the Rewrite appender.\[10\]\[11\]\[12\]\[13\] structlog and semantic_logger have no built-in field redaction.
- **Breyer (C-582/14, 19 Oct 2016)** interpreted the 1995 Directive, not the GDPR. A dynamic IP address is personal data for a website operator that "has the legal means" to identify the visitor with the ISP's help.\[14\]
- **CNIL's logging recommendation** (délibération 2021-122) sets a general retention of six months to one year, up to three years in the most common justified cases.\[15\]
- **PCI DSS v4.0.1 Req. 10.5.1** requires at least 12 months of audit log history, with the most recent three months immediately available.\[16\]\[17\]
- **NIST SP 800-92 Rev. 1** is still an initial public draft (11 Oct 2023), and the 2006 SP 800-92 is still the final version.\[18\]\[19\]
- **OWASP** says logs "must not be destroyed before the duration of the required data retention period, and must not be kept beyond this time".\[20\]
- **Rust:** thiserror 2.0.21 (23 Sep 2026)\[21\] and anyhow 1.0.104 (18 Jul 2026).\[22\]\[23\]\[24\] Use thiserror for library error types and anyhow for application code.
- **Java:** `Throwable(String, Throwable)` does *not* copy the cause's message into its own message.\[25\] Ruby sets `cause` from `$!` automatically, and you can override it with `cause:`.\[26\]
- **PowerShell:** `Write-Information` writes to stream 6, and `$InformationPreference` defaults to `SilentlyContinue`. `Write-Host` has wrapped `Write-Information` since 5.0.\[3\] Microsoft's own pages disagree on whether `trap` matches derived exception types (contested).\[3\]
- **Bulkhead:** the Azure Architecture Center names resilience4j and Polly as frameworks for consumer bulkheads, and tells you not to re-create platform throttling in application code.\[3\]

## 2. Corrections

| Belief | Verdict | Correct fact and source |
|---|---|---|
| JS `Error` takes `cause` (ES2022) | Confirmed, with nuance | MDN: "If you omit options, pass a primitive value as options, or pass an object without the cause property, then the created Error object will have no cause property."\[27\] TypeScript needs `lib`/`target` ES2022 or later, otherwise `TS2554` (secondary: howtodoinjava).\[28\] |
| Rust separates `Result`/`?` from `panic!` | Confirmed | Rust Book ch. 9.3: "returning Result is a good default choice when you're defining a function that might fail."\[29\] |
| Java checked/unchecked; `Throwable(String, Throwable)` keeps cause | Confirmed, with nuance | The javadoc says "the detail message associated with cause is *not* automatically incorporated in this throwable's detail message."\[25\] |
| PHP `Exception` takes `$previous` | Confirmed, with nuance | The signature is `?Throwable $previous = null`, so it accepts any Throwable including `Error`. A user note on php.net says internal exceptions are not raised with `$previous` (secondary).\[30\] |
| Ruby sets `cause` automatically in `rescue` | Confirmed, slightly wider | Kernel#raise: cause "is automatically set to the 'current' exception ($!), if any". It applies wherever `$!` is set (rescue, ensure, at_exit), and the `cause:` keyword overrides it.\[26\]\[31\] |
| GDPR treats IP as personal data in some circumstances (Breyer) | Out of date in framing | Breyer interpreted Article 2(a) of **Directive 95/46/EC**, not the GDPR.\[32\] Its relative-identifiability test is applied by analogy to GDPR Art. 4(1). |
| Art. 5(1)(e) limits retention | Confirmed | ICO quotes Art. 5(1)(e): "kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed".\[33\] |
| OTel severities 1–24 | Confirmed, incomplete | `SeverityNumber=0` "MAY be used to represent an unspecified value".\[4\] The data model's status is **Stable**.\[4\] |
| ASP.NET Core and Spring both produce RFC 9457 problem details out of the box | **Wrong** | ASP.NET Core does so only for `[ApiController]` error results. Spring Boot's problemdetails properties are false by default. Spring Framework 7.0 no longer sets `type` by default, and 7.1 stops setting `instance` (details in §4.7).\[1\]\[2\]\[34\] |

## 3. Facts table

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| 1 | OTel Logs Data Model status | Stable, spec 1.62.0 | https://opentelemetry.io/docs/specs/otel/logs/data-model/ | "Status: Stable"\[4\] | read 2026-11-15 |
| 2 | OTel unspecified severity | 0 | same | "`SeverityNumber=0` MAY be used to represent an unspecified value."\[4\] | read 2026-11-15 |
| 3 | OTel error threshold | ≥17 | same | "If `SeverityNumber` is present and has a value of ERROR (numeric 17) or higher then it is an indication that the log record represents an erroneous situation."\[4\] | read 2026-11-15 |
| 4 | OTel single-level mapping rule | smallest value in range | same | "If the source format has only a single severity that matches the meaning of the range then it is recommended to assign that severity the smallest value of the range."\[4\] | read 2026-11-15 |
| 5 | OTel missing severity | treat as INFO (9) | same | "may interpret log records with missing `SeverityNumber` and `SeverityText` fields as if the `SeverityNumber` was set equal to INFO (numeric value of 9)."\[4\] | read 2026-11-15 |
| 6 | Breyer holding | dynamic IP = personal data if legal means to identify | https://curia.europa.eu/site/upload/docs/application/pdf/2016-10/cp160112en.pdf | "a dynamic IP address registered by an 'online media services provider' … constitutes personal data with respect to the operator if it has the legal means enabling it to…"\[14\] | 2016-10-19 |
| 7 | Breyer legitimate interest | cyber-attack defence | same | "The operator of a website may have a legitimate interest in storing certain personal data relating to visitors to that website in order to protect itself against cyberattacks"\[14\] | 2016-10-19 |
| 8 | CNIL log retention | 6 months–1 year | https://www.cnil.fr/fr/la-cnil-publie-une-recommandation-relative-aux-mesures-de-journalisation | "une journalisation permettant d'assurer une traçabilité des accès et des actions des différents utilisateurs habilités … pour une durée comprise entre six mois et un an"\[15\] | read 2026-11-15 |
| 9 | CNIL longer retention | up to 3 years typical max when justified | same | "il est possible de justifier la conservation de données de journalisation pour une durée supérieure à un an, avec dans les cas les plus courants une durée maximale de trois ans"\[15\] | read 2026-11-15 |
| 10 | CNIL security sheet | rolling 6–12 months | https://cnil.fr/fr/securite-tracer-les-operations | "Conserver ces évènements sur une période glissante comprise entre six mois et un an"\[35\] | read 2026-11-15 |
| 11 | EDPB: logs can be personal data | yes | https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf | "log data facilitating auditability of, e.g., storage, modifications or erasure of data may also qualify as personal data relating to the person who initiated the respective processing operation." (fn. 26)\[36\]\[37\] | v2.0, 2023 |
| 12 | ICO storage limitation | justify retention | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/ | "You must not keep personal data for longer than you need it."\[33\] | read 2026-11-15 |
| 13 | ICO breach logs | minimise, delete per schedule | https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/personal-data-breach-management/breach-identification-assessment-and-logging/ | "Set out a retention period for breach logs that contain personal information and establish a lawful basis for their retention."\[38\] | read 2026-11-15 |
| 14 | OWASP disposal | both lower and upper bound | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | "Log data, temporary debug logs, and backups/copies/extractions, must not be destroyed before the duration of the required data retention period, and must not be kept beyond this time."\[20\] | read 2026-11-15 |
| 15 | PCI DSS v4.0.1 10.5.1 | 12 months / 3 months immediate | PCI SSC document not fetched; text as reproduced at https://sammy.codific.com/browse/pci-dss-401/regularly-monitor-and-test-networks/log-and-monitor-all-access-to-system-components-and-cardholder-data/audit-log-history-is-retained-and-available-for-analysis (secondary) | "Retain audit log history for at least 12 months, with at least the most recent three months immediately available for analysis."\[16\] | read 2026-11-15 |
| 16 | NIST SP 800-92 final | Sept 2006 | https://csrc.nist.gov/pubs/sp/800/92/final | "09/13/06: SP 800-92 (Final)"\[19\] | 2006-09-13 |
| 17 | NIST SP 800-92r1 | initial public draft only | https://csrc.nist.gov/pubs/sp/800/92/r1/ipd | "Date Published: October 11, 2023 Comments Due: November 29, 2023"\[18\] | 2023-10-11 |
| 18 | NIST r1 status | comments being addressed | https://csrc.nist.gov/search?keywords=800-92 | "NIST is in the process of addressing public comments on Draft Special Publication (SP) 800-92 Revision 1"\[39\] | read 2026-11-15 |
| 19 | thiserror latest | 2.0.21, 2026-09-23 | https://github.com/dtolnay/thiserror/releases \[22\] | "2.0.21 Latest … released this 23 Sep"\[21\]\[22\] | 2026-09-23 |
| 20 | anyhow latest | 1.0.104, 2026-07-18 | https://docs.rs/crate/anyhow/latest \[23\] | "1.0.104 (2026-07-18)"\[23\]\[24\] | 2026-07-18 |
| 21 | anyhow MSRV | Rust 1.68.0 | https://crates.io/crates/anyhow/versions | "Version 1.0.104 … Minimum Rust version: v1.68.0"\[23\] | read 2026-11-15 |
| 22 | Spring Boot problemdetails default | false | https://github.com/spring-projects/spring-boot/issues/32634 | "those properties are false by default, as this could be a breaking change for applications"\[1\] | 2022 issue |
| 23 | Spring 7.1 instance | no longer auto-set | https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-7.1-Release-Notes | "The instance field of ProblemDetail is no longer set automatically (#35969)."\[2\] | read 2026-11-15 |
| 24 | Spring 7.1 MVC | renders any unhandled exception | same | "Spring MVC can now render any unhandled exception as an RFC 9457 problem detail, without requiring a @ControllerAdvice that extends ResponseEntityExceptionHandler (#37380)."\[2\] | read 2026-11-15 |
| 25 | Spring current javadoc | 7.0.10 | https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/ProblemDetail.html | "According to the spec, when not present, the type is assumed to be \"about:blank\""\[40\] | read 2026-11-15 |
| 26 | ASP.NET Core controllers | ProblemDetails default for error codes | https://learn.microsoft.com/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0 | "The automatic creation of a `ProblemDetails` for error status codes is enabled by default."\[3\] | read 2026-11-15 |
| 27 | ASP.NET Core 11 change | preserves BadHttpRequestException status | same | "In ASP.NET Core 11 and later, `UseExceptionHandler` preserves `BadHttpRequestException.StatusCode` by default in problem details responses."\[3\] | read 2026-11-15 |
| 28 | PowerShell info preference | SilentlyContinue | https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/write-information?view=powershell-7.6 | "Because the default value of this variable is **SilentlyContinue**, by default, informational messages are not shown."\[3\] | read 2026-11-15 |
| 29 | Write-Host | wraps Write-Information | same | "Starting in Windows PowerShell 5.0, `Write-Host` is a wrapper for `Write-Information`"\[3\] | read 2026-11-15 |
| 30 | Serilog trace IDs | built in since 3.1 | https://github.com/serilog/serilog/releases | "This release adds two new first-class properties to LogEvent: TraceId and SpanId."\[5\] | v3.1.0 |
| 31 | Monolog redaction | RedactingFormatter added 3.11.0 | https://github.com/Seldaek/monolog/blob/main/CHANGELOG.md | "Added RedactingFormatter to automatically redact sensitive data from records, based on key names, #[SensitiveParameter] constructor params and/or regex patterns (#2041)"\[12\] | 2026-09-02 |

## 4. Findings

### 4.1 Error idioms: TypeScript/JavaScript, Rust, Java, PHP, Ruby

**JavaScript / TypeScript.**
- *Hierarchy:* `Error` with built-in subclasses. Separately, MDN distinguishes `AggregateError` and `SuppressedError`, which represent multiple failing sites, from `cause`, which represents a single failing site: "The cause property represents a single failing site, with the wrapper error only adding context to the cause and not representing an additional failure." (MDN, Error: cause).\[41\]
- *Keeping a cause:* `throw new Error("Connecting to database failed.", { cause: err });` (MDN).\[41\] `cause` is set only when the options object has a `cause` property.\[27\] Node documents that `util.inspect()` "recursively serializes `error.cause`" (nodejs/node commit fcfb2c9, secondary to Node docs).\[42\]
- *Result types:* the language has none. Not found: an official TC39/MDN recommendation of a Result pattern.
- *TypeScript:* `new Error(msg, { cause })` fails with `TS2554` unless `lib`/`target` is ES2022 or later (secondary: howtodoinjava).\[28\]

**Rust.**
- *Recoverable vs unrecoverable:* `Result<T, E>` versus `panic!`. The Book: "When you choose to return a Result value, you give the calling code options rather than making the decision for it … returning Result is a good default choice when you're defining a function that might fail." (doc.rust-lang.org/book ch09-03).\[29\] Panic unwinds by default; `panic = 'abort'` in a Cargo profile changes that (ch09-01).\[43\]
- *What the docs warn against:* panicking for failures that are expected. "When a bad state is reached, but it's expected to happen no matter how well you write your code, it's still more appropriate to return a Result rather than making a panic! call" (ch09-03).\[29\]
- *thiserror 2.0.21* (23 Sep 2026; MIT OR Apache-2.0) derives `std::error::Error` for your own enums and structs.\[21\]\[44\] *anyhow 1.0.104* (18 Jul 2026; MSRV 1.68.0) gives you one concrete `anyhow::Error` type with context chaining.\[23\]\[24\]
- *When each fits:* the anyhow README's "Comparison to thiserror" (github.com/dtolnay/anyhow) says: "Use Anyhow if you don't care what error type your functions return, you just want it to be easy. This is common in application code. Use thiserror if you are a library that wants to design your own dedicated error type(s) so that on failures the caller gets exactly the information that you choose."
- *Version-line note:* thiserror 2.x has been current since 2.0.0 (2024-11-06). 1.0.69 (2024-11-10) was the last 1.x release found.\[45\]

**Java.**
- *Checked vs unchecked:* Java Tutorials: "If a client can reasonably be expected to recover from an exception, make it a checked exception. If a client cannot do anything to recover from the exception, make it an unchecked exception." (docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html; the tutorial targets JDK 8).\[46\]
- *Cause:* `Throwable(String message, Throwable cause)`: "Note that the detail message associated with cause is *not* automatically incorporated in this throwable's detail message." (Java SE 21 javadoc).\[25\] Log the whole exception object, not `getMessage()`.

**PHP.**
- `public function Exception::__construct(string $message = "", int $code = 0, ?Throwable $previous = null)` (php.net).\[30\] `Error::__construct` has the same `$previous` parameter, so `Exception` and `Error` both chain any `Throwable`.\[47\]
- *What to catch:* catching `Exception` misses `Error` (TypeError etc.), because both implement `Throwable`. This follows from the hierarchy; a direct php.net sentence was not fetched in this run.
- *Warning (secondary, php.net user note):* "none of the internal php exceptions (e.g. PDOException, ReflectionException, etc) are called internally within php with $previous in mind."\[30\]

**Ruby.**
- *Hierarchy:* a bare `rescue` catches `StandardError`: "A rescue statement may include one or more classes that are to be rescued; if none is given, StandardError is assumed." (docs.ruby-lang.org 3.4 exceptions).\[48\]
- *Library pattern:* "A good practice is for a library to create a single 'generic' exception class (typically a subclass of StandardError or RuntimeError) and have its other exception classes derive from that class." (Ruby 3.3 Exception docs).\[31\]
- *Cause:* "The cause of the generated exception (accessible via Exception#cause) is automatically set to the 'current' exception ($!), if any. An alternative value, either an Exception object or nil, can be specified via the :cause argument." (ruby-doc.org Kernel 3.3.2).\[26\]

### 4.2 Personal data in logs

- **Art. 4(1), 5(1)(c), 32 GDPR:** EUR-Lex text was not re-fetched in this run (https://eur-lex.europa.eu/eli/reg/2016/679/oj).
  - Art. 4(1) defines personal data as information relating to an identified or identifiable natural person, including by reference to "an online identifier".
  - Art. 5(1)(c) requires data be "adequate, relevant and limited to what is necessary" (data minimisation).
  - Art. 32(1)(a) lists "the pseudonymisation and encryption of personal data" among security measures.
  - Verify all three verbatim against EUR-Lex before filing.
- **Art. 5(1)(e)** is confirmed via ICO's verbatim reproduction (Facts #12).\[33\]
- **Breyer:** curia press release 112/16 (Facts #6–7). The judgment interpreted Directive 95/46/EC Art. 2(a) and 7(f). Commentators read it as adopting a *relative* criterion (secondary: Lexology / Bird & Bird).\[49\]\[50\] Practical reading: treat client IPs in access and application logs as personal data, and rely on legitimate interest (security) with bounded retention.
- **EDPB:** Guidelines 9/2022 (v2.0) fn. 26 says audit log data may itself be personal data of the person who did the operation (Facts #11).\[37\] Breach records containing personal data need a retention period under the processing principles.\[51\] Not found: an EDPB guideline dedicated to application logging.
- **ICO:** storage limitation (Facts #12). For breach logs, "Take steps to periodically reduce the personal information held in breach logs (eg by using data minimisation or anonymisation techniques)."\[38\]
- **CNIL:** délibération 2021-122 (14 Oct 2021) sets a 6–12 month default and up to 3 years when justified. Logs for processing whose source data is kept under six months "doivent ne pas inclure de données personnelles du traitement principal" (Facts #8–10).\[15\]

### 4.3 Retention and sampling

- **OWASP** sets both a lower and an upper bound (Facts #14).\[20\]
- **NIST SP 800-92** (2006) is final. Rev. 1 is an initial public draft from 11 Oct 2023 that "replaces the original SP 800-92" once final; NIST is "addressing public comments" (Facts #16–18).\[39\] No final date was found. Not found: a numeric retention period in either NIST document from this run.
- **PCI DSS v4.0.1 10.5.1:** 12 months, 3 months immediately available (Facts #15).\[16\] The official PCI SSC PDF was not fetched; the quote is from reproductions.
- **CNIL:** 6–12 months (Facts #8).\[15\]
- **Sampling without losing errors: not found** in a primary source this run. That includes the OpenTelemetry Collector tail-sampling processor docs, which were not reached. My analysis, labelled as such: decide sampling by severity and never sample records with SeverityNumber ≥ 17. The OTel spec gives that threshold an "erroneous situation" meaning (Facts #3),\[4\] so it is a vendor-neutral cut-off. Also keep trace-linked logs consistent with the trace sampling decision (the `TraceFlags` SAMPLED bit is part of the log record).\[4\]

### 4.4 OpenTelemetry Logs Data Model

- **Ranges:** 1–4 TRACE, 5–8 DEBUG, 9–12 INFO, 13–16 WARN, 17–20 ERROR, 21–24 FATAL.\[52\] Short names run TRACE, TRACE2…FATAL4.\[53\] When a record is displayed, show both, e.g. "INFO (Informational)" (spec, Displaying Severity).\[4\]
- **Per-library mapping: not found** as published, primary mappings for structlog, pino, Serilog, Logback, Log4j 2, Monolog or semantic_logger. Appendix B of the spec (opentelemetry.io/docs/specs/otel/logs/data-model-appendix/, spec 1.62.0) does map the RFC 5424 Syslog levels: Debug→DEBUG (5), Informational→INFO (9), Notice→INFO2 (10), Warning→WARN (13), Error→ERROR (17), Critical→ERROR2 (18), Alert→ERROR3 (19), Emergency→FATAL (21). The appendix says its examples are "provided purely for demonstrative purposes and are not exhaustive or canonical".
- **Derived mapping**, applying spec rule Facts #4. This is not a published mapping; adopt it only as a repository convention:

| Library | Levels | Derived SeverityNumber |
|---|---|---|
| structlog (stdlib names) | debug, info, warning, error, critical | 5, 9, 13, 17, 21 |
| pino | trace 10, debug 20, info 30, warn 40, error 50, fatal 60 | 1, 5, 9, 13, 17, 21 |
| Serilog | Verbose, Debug, Information, Warning, Error, Fatal | 1, 5, 9, 13, 17, 21 |
| Logback / Log4j 2 | TRACE, DEBUG, INFO, WARN, ERROR (Log4j 2 adds FATAL) | 1, 5, 9, 13, 17 (21) |
| Monolog (RFC 5424) | DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL, ALERT, EMERGENCY | 5, 9, 10, 13, 17, 18, 19, 21 (taken from the spec's Appendix B Syslog example, which is non-canonical) |
| semantic_logger | trace, debug, info, warn, error, fatal | 1, 5, 9, 13, 17, 21 |

- The library level names in this table are from general knowledge and were not re-sourced this run.
- A secondary source (Dash0) shows a syslog mapping of Critical→21 and Error→19.\[52\] That contradicts the spec's Appendix B example (Critical→18, Error→17), which this repository should follow instead.

### 4.5 Trace context and redaction per library

| Library | Current version (date) | Trace/span ID attachment | Built-in redaction |
|---|---|---|---|
| structlog | 26.1.0 (2026-06-06, CHANGELOG) | No built-in. The docs give an `add_open_telemetry_spans` processor recipe that writes `event_dict["span"] = {"span_id": …, "trace_id": …}` (structlog.org frameworks page)\[9\] | None built in; write a processor |
| pino | 10.4.0 (2026-10-02, GitHub pinojs/pino releases: "v10.4.0 Latest … released this 02 Oct"); 10.3.1 was 2026-02-09 | `@opentelemetry/instrumentation-pino`: "Pino logger calls in the context of a tracing span will have fields identifying the span added to the log record." Fields are `trace_id`, `span_id`, `trace_flags`\[54\] | `redact` (paths / `censor` default "[Redacted]" / `remove`). "Never allow user input to define redacted paths."\[10\]\[55\]\[56\] |
| Serilog | 4.4.0 (2026-07-10, NuGet)\[57\] | Built in since 3.1: TraceId/SpanId "are set automatically in Logger.Write() to the corresponding property values from System.Diagnostics.Activity.Current."\[5\] | Destructuring policies (`IDestructuringPolicy`, `Destructure.ByTransforming`). A verbatim Serilog-docs quote was **not found** |
| Logback | 1.6.5 (2026-09-30, GitHub releases snippet only)\[58\] | `opentelemetry-logback-mdc-1.0` appender: "injecting the trace ID and span ID from a mounted span using a custom Logback appender."\[8\] | Not in core. Third-party logstash-logback-encoder `MaskingJsonGeneratorDecorator`: "Data to be masked can be identified by path and/or by value."\[11\] |
| Log4j 2 | 2.26.1 (date **contested**: 2026-07-02 per versio.io, a third party; the official notes snippet gives 2.25.5 = 2026-07-01)\[59\]\[60\] | `opentelemetry-log4j-context-data-2.17-autoconfigure`: "injects the trace ID and span ID from an active span into Log4j's context data." Use `%X{trace_id}`\[7\] | Rewrite appender, but the docs say: "Although this appender can be used to mask sensitive information contained in log events, we strongly discourage such practice."\[13\] |
| Monolog | 3.12.1 (2026-09-29, Packagist)\[61\] | **Not found** | `RedactingFormatter` (3.11.0, 2026-09-02): "masks the value of any context/extra key matching a configured name (e.g. password, token, authorization)…"\[12\]\[62\] |
| semantic_logger | 5.1.0 (2026-07-20, RubyGems)\[63\] | **Not found** as automatic injection. The README lists OpenTelemetry only as a destination\[64\] | No field redaction. The appender `filter:` includes or drops whole messages\[65\] |

### 4.6 Error messages for people (Standard)

- **Microsoft (Windows app design, "Writing style"):** "More than anything else, it's important that your error message doesn't blame the user." Error messages should "Be warm and relaxed", "Be ready to lend a hand" and "Be crisp and clear" (learn.microsoft.com/windows/apps/design/style/writing-style).\[3\]
- **Microsoft Win32 "Error Message Guidelines":** a good message answers "What happened and why? What is the end result for the user? What can the user do to prevent it from happening again?"\[3\]
- **The Microsoft sources disagree on "please":** Win32 says "Avoid the word 'please'. It can be interpreted to mean that a required action is optional." The Windows UX "Style and Tone" guide allows "please" when the user is inconvenienced.\[3\] Treat this as **contested within Microsoft**.
- **Nielsen Norman Group:** heuristic 9: "Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution." (nngroup.com/articles/ten-usability-heuristics).\[66\]
- **NN/g "Error-Message Guidelines"** (Neusesser & Sunwall, 14 May 2023): "Display the error message close to the error's source." and "Use human-readable language."\[67\]\[68\]
- **NN/g "Hostile Patterns":** "Avoid premature error messages: Display error messages only after the error has been made."\[69\]

### 4.7 RFC 9457 in frameworks (Standard)

- **ASP.NET Core (docs view 10.0):**
  - `AddProblemDetails` "registers the default `IProblemDetailsService` implementation".\[3\]
  - Problem details are generated by ExceptionHandlerMiddleware "when a custom handler is not defined", by StatusCodePagesMiddleware "by default", and by the developer exception page in Development.\[3\]
  - It stops when the `Accept` header doesn't accept JSON. Non-JSON types "such as `application/xml` or `text/html`, are **not** supported and trigger the fallback behavior."\[3\]
  - The default exception body uses `"type":"https://tools.ietf.org/html/rfc7231#section-6.6.1"`. \[3\]
  - Warning from the docs: "Do **not** serve sensitive error information to clients."\[3\]
  - ASP.NET Core 11 preserves `BadHttpRequestException.StatusCode` (Facts #27).\[3\] The .NET 11 GA date was not verified this run.
- **Spring:**
  - Framework 6.0+ has `ProblemDetail`, `ErrorResponse` and `ResponseEntityExceptionHandler`. Boot's properties default to false (Facts #22).\[1\]\[70\]
  - Framework 7.0 javadoc (7.0.10): when `type` is absent it "is assumed to be about:blank".\[40\] A secondary source (ankurm.com) measured `getType()` = `about:blank` on spring-web 6.2.19 and `null` on 7.0.9, so the JSON omits `type`.\[34\]
  - 7.1: `instance` is no longer auto-set, and MVC renders any unhandled exception as a problem detail. "Any other exception results in a generic 500 response. The exception message is never exposed."\[2\]
  - 7.1 has not reached GA. The 7.1 release-notes wiki (edited 5 Nov 2026) says "This is a preview page for Spring Framework 7.1.0, scheduled for November 2026", and the newest tag is v7.1.0-RC2 (5 Nov 2026).
- **FastAPI, Express, Go: not found** in this run. I could not confirm from primary docs whether any of them ships RFC 9457 support. Treat "FastAPI/Express/Go emit RFC 9457 by default" as unverified. Do not write it into the facts files.

### 4.8 Bulkheads (Standard)

- **Azure Architecture Center:** "Isolate the elements of an application into pools so that if one element fails, the others continue to function."\[3\]
  - It names libraries: "Projects like resilience4j and Polly offer a framework for creating consumer bulkheads."\[3\]
  - It adds: "Use built-in platform controls, such as Azure API Management rate limits … Don't re-create these throttling and isolation mechanisms in your application code."\[3\]
  - It recommends combining bulkheads "with retry, circuit breaker, and throttling patterns".\[3\]
- **Nygard, *Release It!*:** not fetched; secondary only, so no quote.
- **Per-language libraries beyond Java (resilience4j) and .NET (Polly): not found** in this run.

### 4.9 PowerShell `trap` and the information stream (Standard)

- **`trap`:** "The `trap` keyword can handle both kinds" (statement- and script-terminating errors). Default behaviour is to display the error and continue. `break` aborts; `continue` silences the error.\[3\]
- **Hoisting:** "`trap` statements … always apply to all statements in that scriptblock … even if execution hasn't advanced past the point at which they're defined." When several traps match, "the first `trap` defined lexically (highest in the scriptblock) is used."\[3\]
- **Contested: derived-type matching.**
  - about_Trap says `trap [System.Exception]` "traps any errors raised by unknown commands. It also traps other error types", which implies derived types match.\[3\]
  - The language spec §8.8 says "Unlike a `catch` block, a `trap` statement matches an exception type exactly; no derived type matching is performed."\[3\]
  - Test this on PowerShell 7.6 before writing guidance.
- **Information stream:**
  - Stream 6 can be redirected with `6>`, as in the docs' `Test-Info 6> Info.txt` example.\[3\]
  - It is structured: records carry `MessageData`, `Source`, `TimeGenerated`, `Tags`, `User`, `Computer`, `ProcessId`.\[3\]
  - `-InformationVariable` captures records.\[3\]
  - `$InformationPreference` defaults to SilentlyContinue (Facts #28).\[3\]

## 5. Tools

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| thiserror | Derive error types (Rust libs) | 2.0.21 | 2026-09-23 | `cargo add thiserror` | Cargo.toml | github.com/dtolnay/thiserror/releases |
| anyhow | App-level error type (Rust) | 1.0.104 | 2026-07-18 | `cargo add anyhow` | Cargo.toml | docs.rs/crate/anyhow/latest |
| structlog | Structured logging (Python) | 26.1.0 | 2026-06-06 | `pip install structlog` | code | structlog CHANGELOG\[71\] |
| pino | JSON logging (Node) | 10.4.0 | 2026-10-02 | `npm i pino` | code | github.com/pinojs/pino/releases |
| @opentelemetry/instrumentation-pino | Trace-context injection | not found | not found | `npm i @opentelemetry/instrumentation-pino` | code | npmjs.com |
| Serilog | Structured logging (.NET) | 4.4.0 | 2026-07-10 | `dotnet add package Serilog` | appsettings.json / code | nuget.org/packages/Serilog\[57\] |
| Logback | Logging (Java) | 1.6.5 | 2026-09-30 | Maven `ch.qos.logback:logback-classic` | logback.xml | github.com/qos-ch/logback/releases\[58\] |
| opentelemetry-logback-mdc-1.0 | MDC trace IDs | not found | not found | Maven `io.opentelemetry.instrumentation:opentelemetry-logback-mdc-1.0` | logback.xml | opentelemetry-java-instrumentation README\[8\] |
| logstash-logback-encoder | JSON + masking | not found | not found | Maven `net.logstash.logback:logstash-logback-encoder` | logback.xml | logfellow README |
| Log4j 2 | Logging (Java) | 2.26.1 (date contested) | contested | Maven `org.apache.logging.log4j:log4j-core` | log4j2.xml | github.com/apache/logging-log4j2/releases\[72\] |
| Monolog | Logging (PHP) | 3.12.1 | 2026-09-29 | `composer require monolog/monolog` | code | packagist.org\[61\] |
| semantic_logger | Logging (Ruby) | 5.1.0 | 2026-07-20 | `gem install semantic_logger` | code | rubygems.org\[63\] |
| Spring Framework | ProblemDetail | 7.0.10 (javadoc "current") | not found | Maven `spring-web` | application.properties | docs.spring.io |
| ASP.NET Core | ProblemDetails | 10.0 docs | not found | `dotnet new webapi` | Program.cs | learn.microsoft.com |
| PowerShell | trap / streams | 7.6 docs | not found | — | — | learn.microsoft.com |

## 6. Changing in the next 12 months

- **Spring Framework 7.1:** `ProblemDetail.instance` is no longer set automatically (breaking), and MVC renders any unhandled exception as a problem detail.\[2\] The 7.1 release-notes wiki (edited 5 Nov 2026) says 7.1.0 is "scheduled for November 2026". The newest tag is v7.1.0-RC2 (5 Nov 2026), and the RC1 notes (22 Oct) list the `instance` change (#35969) under "Attention Required".
- **ASP.NET Core 11:** `UseExceptionHandler` preserves `BadHttpRequestException.StatusCode`.\[3\] The GA date was not verified.
- **NIST SP 800-92 Rev. 1 final:** pending; no date announced (found).\[39\]
- **End-of-support dates mostly not verified this run** for .NET 8/9/10, PowerShell 7.4/7.6, Spring Framework 7.0, Spring Boot 3.x/4.x, Log4j 2.25 and Logback 1.5. One was verified: the Spring Framework Versions wiki says 6.2.x "Open source support ends in June 2026", so 6.2.x is already out of open-source support. **Flag for R07e:** the unverified items likely include end-of-support dates inside 12 months. Do not file dates from memory.
- **pino 10** dropped Node.js 18 (secondary: skills.rest).\[73\] Verify against the pino release notes.

## 7. Common mistakes

- **Logging `e.getMessage()` / `e.message` and losing the chain.** Java does not merge the cause's message (javadoc),\[25\] and in JS `cause` exists only if you pass it (MDN).\[27\]
- **Catching `Exception` in PHP and missing `Error`.** Both chain `?Throwable $previous` (php.net),\[30\]\[47\] but only `Throwable` covers both.
- **Panicking on expected failures in Rust.** See Book ch. 9.3.
- **Assuming RFC 9457 is on by default.** It is off in Spring Boot (Facts #22).\[1\] In ASP.NET Core it is partial and depends on `Accept`.\[3\]
- **Hard-coding `"type":"about:blank"` in contract tests.** Spring 7 omits `type` (secondary: ankurm.com).\[34\]
- **Building pino redact paths from user input.** pino warns "Never allow user input to define redacted paths."\[10\]
- **Using Log4j Rewrite for masking.** Log4j docs "strongly discourage such practice."\[13\]
- **Keeping logs forever "for security".** OWASP and CNIL both set an upper bound (Facts #8, #14).\[20\]\[35\]
- **Treating IP addresses as never personal data.** See Breyer (Facts #6).
- **Expecting `Write-Information` output to show.** It is silent by default (Facts #28).\[3\]
- **AI coding assistants specifically:** **not found.** No primary or reputable source documenting AI-assistant-specific error-handling or logging mistakes was found in this run. The items above are the documented pitfalls an assistant should be checked against.

## 8. Sources and licences

The Quote? / Paraphrase? / Adapt code? columns say what an Apache-2.0 repository may do.

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| OpenTelemetry spec | Apache-2.0 (believed; verify repo LICENSE) | Yes | Yes | Yes | "OpenTelemetry Authors", link |
| MDN | Prose CC BY-SA 2.5; code samples CC0 (believed; verify) | Short quotes | Yes | Yes (CC0) | "MDN contributors", link |
| Rust Book | MIT OR Apache-2.0 (believed) | Yes | Yes | Yes | link |
| thiserror / anyhow | MIT OR Apache-2.0 (crates.io) | Yes | Yes | Yes | keep notices |
| Ruby docs | Ruby licence / BSD-2 (believed) | Yes | Yes | Yes | link |
| PHP manual | CC BY 3.0 (believed) | Yes | Yes | Yes | "PHP Documentation Group" |
| Oracle Java javadoc / Tutorials | Oracle copyright, not open | Brief quotes only | Yes | No | cite URL |
| Microsoft Learn | CC BY 4.0 docs; MIT code (believed) | Yes | Yes | Yes | "Microsoft", link |
| NN/g | All rights reserved | Brief quotes only | Yes | n/a | cite URL |
| EUR-Lex / curia.europa.eu | Reuse permitted with acknowledgement (believed) | Yes | Yes | n/a | cite source |
| EDPB | Reuse with acknowledgement (not verified) | Brief | Yes | n/a | cite |
| ICO | Open Government Licence v3.0 (believed) | Yes | Yes | n/a | "Contains public sector information…" |
| CNIL | Not verified | Brief | Yes | n/a | cite |
| OWASP Cheat Sheets | CC BY-SA 4.0 (believed) | Yes | Yes | Code samples are ShareAlike: keep outside Apache-2.0 files, or link | "OWASP", link |
| NIST SPs | US Government work, generally public domain (believed) | Yes | Yes | n/a | cite |
| PCI DSS | PCI SSC proprietary licence | Brief quotes only | Yes | n/a | cite PCI SSC |
| pino | MIT (believed) | Yes | Yes | Yes | keep notice |
| Serilog, Log4j 2, semantic_logger, logstash-logback-encoder, OTel Java/JS instrumentation | Apache-2.0 (believed) | Yes | Yes | Yes | keep NOTICE |
| Logback | EPL-1.0 / LGPL-2.1 (believed) | Yes | Yes | Snippets OK; avoid copying source files | cite |
| Monolog, structlog | MIT; structlog MIT OR Apache-2.0 (believed) | Yes | Yes | Yes | keep notice |
| Secondary blogs (Lexology, ankurm.com, Dash0, howtodoinjava, versio.io) | All rights reserved | Brief | Yes | No | cite, label "secondary" |

## 9. Not found, contested, not covered

**Not found:**
- Per-library OTel severity mappings.
- Primary guidance on sampling that preserves errors.
- RFC 9457 support in FastAPI, Express and Go.
- Bulkhead libraries for Python, Go, Node, PHP and Ruby.
- *Release It!* text.
- Monolog and semantic_logger trace-ID injection.
- Serilog destructuring docs quote.
- .NET 11 GA date. Spring 7.1 has no GA date yet: it is "scheduled for November 2026" per its release-notes wiki, and the latest tag is v7.1.0-RC2 (5 Nov 2026).
- Most end-of-support dates. The exception is Spring Framework 6.2.x, whose open-source support "ends in June 2026" per the Spring Framework Versions wiki.
- AI-assistant-specific mistakes.
- EDPB logging-specific guidance.
- A numeric retention period in NIST SP 800-92 / r1.

**Contested:**
- Log4j 2.26.x release dates.
- PowerShell `trap` derived-type matching (about_Trap vs language spec §8.8).
- Microsoft guidance on "please".
- Monolog's 8 RFC 5424 levels onto OTel ranges. The spec's non-canonical Appendix B example (Error→17, Critical→18, Alert→19, Emergency→21) conflicts with Dash0's secondary mapping (Error→19, Critical→21).

**Not covered / not re-fetched:**
- GDPR Art. 4(1), 5(1)(c), 32 verbatim from EUR-Lex.
- PCI SSC official PDF.
- Later CJEU case law on relative identifiability after Breyer.

## Sources

1. [github.com](https://github.com/spring-projects/spring-boot/issues/32634)
2. [Spring Framework 7.1 Release Notes · spring-projects/spring-framework Wiki · GitHub](https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-7.1-Release-Notes)
3. Microsoft Learn
4. [Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
5. [Releases · serilog/serilog · GitHub](https://github.com/serilog/serilog/releases)
6. [@opentelemetry/instrumentation-pino - npm](https://www.npmjs.com/package/@opentelemetry/instrumentation-pino?activeTab=dependencies)
7. [opentelemetry-java-instrumentation/instrumentation/log4j/log4j-context-data/log4j-context-data-2.17/library-autoconfigure/README.md at main · open-telemetry/opentelemetry-java-instrumentation · GitHub](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/log4j/log4j-context-data/log4j-context-data-2.17/library-autoconfigure/README.md)
8. [opentelemetry-java-instrumentation/instrumentation/logback/logback-mdc-1.0/library/README.md at main · open-telemetry/opentelemetry-java-instrumentation · GitHub](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/logback/logback-mdc-1.0/library/README.md)
9. [Frameworks — structlog 26.1.0 documentation](https://www.structlog.org/en/stable/frameworks.html)
10. [pino/docs/api.md at main · pinojs/pino · GitHub](https://github.com/pinojs/pino/blob/main/docs/api.md)
11. [logstash-logback-encoder/README.md at main · logfellow/logstash-logback-encoder · GitHub](https://github.com/logfellow/logstash-logback-encoder/blob/main/README.md)
12. [monolog/CHANGELOG.md at main · Seldaek/monolog · GitHub](https://github.com/Seldaek/monolog/blob/main/CHANGELOG.md)
13. [Delegating Appenders :: Apache Log4j](https://logging.apache.org/log4j/2.x/manual/appenders/delegating.html)
14. [The operator of a website may have a legitimate interest in ...](https://curia.europa.eu/site/upload/docs/application/pdf/2016-10/cp160112en.pdf)
15. [La CNIL publie une recommandation relative aux mesures de journalisation](https://www.cnil.fr/fr/la-cnil-publie-une-recommandation-relative-aux-mesures-de-journalisation)
16. [Audit log history is retained and available for analysis. from PCI DSS 4.0.1 framework](https://sammy.codific.com/browse/pci-dss-401/regularly-monitor-and-test-networks/log-and-monitor-all-access-to-system-components-and-cardholder-data/audit-log-history-is-retained-and-available-for-analysis)
17. [PCI DSS 4.0 Audit Log Retention: Implementation Guide](https://learn.daydream.ai/requirements/pci-dss-10-5-1)
18. [NIST Special Publication (SP) 800-92 Rev. 1 (Draft), Cybersecurity Log Management Planning Guide](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd)
19. [NIST Special Publication (SP) 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final)
20. [Logging - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
21. [Releases · dtolnay/thiserror · GitHub](https://github.com/dtolnay/thiserror/releases)
22. [Thiserror — Rust library // Lib.rs](https://lib.rs/crates/thiserror)
23. [anyhow - crates.io: Rust Package Registry](https://crates.io/crates/anyhow/versions)
24. [anyhow 1.0.104 - Docs.rs](https://docs.rs/crate/anyhow/latest)
25. [Throwable (Java SE 21 & JDK 21)](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)
26. [module Kernel - RDoc Documentation](https://ruby-doc.org/3.3.2/Kernel.html)
27. [Error() constructor - JavaScript - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/Error)
28. [TypeScript Exception Handling: try/catch and Custom Errors](https://howtodoinjava.com/typescript/exception-handling/)
29. [To \`panic!\` or Not To \`panic!\` - To \`panic!\` or Not To \`panic!\` - The Rust Programming Language](https://phaiax.github.io/mdBook/rustbook/ch09-03-to-panic-or-not-to-panic.html)
30. [PHP: Exception::\_\_construct - Manual](https://www.php.net/manual/en/exception.construct.php)
31. [class Exception - Documentation for Ruby 3.3](https://docs.ruby-lang.org/en/3.3/Exception.html)
32. [EU Law Analysis: IP addresses as personal data - the CJEU's judgment in C-582/14 Breyer](http://eulawanalysis.blogspot.com/2017/01/ip-addresses-as-personal-data-cjeus.html)
33. [Principle (e): Storage limitation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/)
34. [Global Exception Handling with ProblemDetail (RFC 9457) in Spring Boot 4](https://ankurm.com/spring-boot-4-problemdetail-rfc-9457-global-exception-handling/)
35. [Sécurité : Tracer les opérations](https://cnil.fr/fr/securite-tracer-les-operations)
36. [Guidelines 9/2022 on personal data breach notification under GDPR Version 2.0](https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf)
37. [EDPB 9/2022 — Guideline — Breach notification](https://www.headlesslaw.com/gdpr/level-3/guidelines/edpb-09-2022-breach-notification)
38. [Breach identification, assessment and logging](https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/personal-data-breach-management/breach-identification-assessment-and-logging/)
39. [Search CSRC - NIST Computer Security Resource Center](https://csrc.nist.gov/search?keywords=800-92)
40. [ProblemDetail (Spring Framework 7.0.10 API)](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/ProblemDetail.html)
41. [Error: cause - JavaScript - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause)
42. [github.com](https://github.com/nodejs/node/commit/976093efe3)
43. [Unrecoverable Errors with \`panic!\` - Unrecoverable Errors with \`panic!\` - The Rust Programming Language](https://phaiax.github.io/mdBook/rustbook/ch09-01-unrecoverable-errors-with-panic.html)
44. [thiserror: Complete Rust Crate Guide & Documentation \[2025\]](https://generalistprogrammer.com/tutorials/thiserror-rust-crate-guide)
45. [thiserror 1.0.1 - Docs.rs](https://docs.rs/crate/thiserror/1.0.1)
46. [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html)
47. [PHP: Error::\_\_construct - Manual](https://www.php.net/manual/en/error.construct.php)
48. [exceptions - Documentation for Ruby 3.4](https://docs.ruby-lang.org/en/3.4/exceptions_md.html)
49. [Court confirms that IP addresses are personal data in some cases - Lexology](https://www.lexology.com/library/detail.aspx?g=aa9830c9-324c-4c59-9453-b8f13b5a182b)
50. [CJEU decision on dynamic IP addresses touches fundamental DP law questions - Bird & Bird](https://www.twobirds.com/en/insights/2016/global/cjeu-decision-on-dynamic-ip-addresses-touches-fundamental-dp-law-questions)
51. [EDPB 9/2022 — Breach notification](https://www.mica.wtf/mica.wtf/gdpr/chapter-xi-final-provisions-art.-94-99/guidelines/edpb-09-2022-breach-notification)
52. [Log Levels Explained: A Better Strategy with OpenTelemetry · Dash0](https://www.dash0.com/knowledge/log-levels)
53. [opentelemetry-collector-contrib/pkg/stanza/docs/types/severity.md at main · open-telemetry/opentelemetry-collector-contrib · GitHub](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/pkg/stanza/docs/types/severity.md)
54. [@opentelemetry/instrumentation-pino - npm](https://www.npmjs.com/package/@opentelemetry/instrumentation-pino)
55. [Pino Logger: JSON Logging, Redaction, and Transports](https://www.sazabi.com/guides/pino-logger)
56. [UNPKG](https://unpkg.com/browse/pino@6.11.2/docs/api.md)
57. [NuGet Gallery](https://www-1.nuget.org/packages/Serilog/)
58. [Releases · qos-ch/logback · GitHub](https://github.com/qos-ch/logback/releases)
59. [Release notes :: Apache Log4j](https://logging.apache.org/log4j/2.x/release-notes.html)
60. [Apache Log4J releases, versions & end-of-life (EOL) dates](https://www.versio.io/en/product-release-end-of-life-eol-apache-log4j.html)
61. [monolog/monolog - Packagist.org](https://packagist.org/packages/monolog/monolog)
62. [monolog/doc/02-handlers-formatters-processors.md at main · Seldaek/monolog · GitHub](https://github.com/Seldaek/monolog/blob/main/doc/02-handlers-formatters-processors.md)
63. [semantic\_logger](https://rubygems.org/gems/semantic_logger/versions/4.2.1)
64. [GitHub - reidmorrison/semantic\_logger: Semantic Logger is a high-performance, asynchronous structured logging framework for Ruby and Rails. · GitHub](https://github.com/reidmorrison/semantic_logger)
65. [RubyDoc.info: Module: SemanticLogger](https://www.rubydoc.info/gems/semantic_logger/SemanticLogger)
66. [10 Usability Heuristics for User Interface Design - NN/G](https://www.nngroup.com/articles/ten-usability-heuristics/)
67. [errors Articles, Videos, Reports, and Training Courses - NN/G](https://www.nngroup.com/topic/errors/)
68. [Error-Message Guidelines - NN/G](https://www.nngroup.com/articles/error-message-guidelines/)
69. [Hostile Patterns in Error Messages - NN/G](https://www.nngroup.com/articles/hostile-error-messages/)
70. [Spring Boot Error Handling with ProblemDetail (RFC 9457) — Shubham Chepe](https://shubhamchepe.com/blog/spring-boot-error-handling-problemdetail.html)
71. [structlog/CHANGELOG.md at main · hynek/structlog · GitHub](https://github.com/hynek/structlog/blob/main/CHANGELOG.md)
72. [Releases · apache/logging-log4j2 · GitHub](https://github.com/apache/logging-log4j2/releases)
73. [pino-js: Applies Pino logging conventions for levels, serializers, redaction, and transports in Node.js code](https://skills.rest/skill/pino-js-avbel)

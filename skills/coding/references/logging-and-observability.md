# Logging and observability

Read this for deciding what a program writes to its logs and metrics: structured lines, fields,
levels, timestamps, trace IDs, what to keep out, personal data in logs, how long to keep them,
sampling, SLOs and the alerts that page, and status lines that say what was checked.

Libraries, their versions, how each attaches trace IDs and redacts, and OpenTelemetry severity
numbers are `logging-libraries`'. Escaping text for a log line is `input-handling`'s; what to
catch, `error-handling`'s. Reading logs others wrote is the operations skill's `log-analysis`.

## Rules

1. **Write one JSON object a line, with the same fields everywhere.** The message is fixed
   text, and the values go in fields.
2. **Give every timestamp its offset, and write UTC with `Z`** (fact `la-rfc3339`).
3. **Choose the level by who has to act.** `ERROR`: someone must. `WARN`: handled, but
   degraded. `INFO`: a line per request or business event. `DEBUG`: off in production.
4. **Put the active `trace_id` and `span_id` in every record,** from W3C Trace Context (fact
   `lo-tracecontext`). Mint no other correlation ID unless something outside needs one.
5. **Keep secrets and personal data out at the source.** Remove, mask, hash or encrypt a value
   before the record is built (fact `lo-owasp-treat`); log a salted hash of a session ID, never
   the ID (fact `lo-owasp-session`).
6. **Log through an encoder that escapes each value.** A parameterized call still passes CR and
   LF (fact `input-owasp-log`).
7. **Treat an IP address or a user ID in a log as personal data,** and log only what the log's
   purpose needs.
8. **Set a retention period with a floor and a ceiling,** and delete at the ceiling.
9. **Sample by severity, and never drop a record at SeverityNumber 17 or above** (fact
   `ll-otel-error`).
10. **A status line names the outcome that was checked,** not that a step finished.
11. **Record each fact of a run once, and derive every report from that record.** Two records
    of one run agree, and an evidence bundle lists what it left out.
12. **Measure each service's rate, errors and duration, and page on symptoms:** an error budget
    burning, not a busy CPU.

### The fields

One record, wrapped here:

```json
{"timestamp": "2026-11-11T14:05:09.123Z", "level": "INFO", "event": "order.paid",
 "message": "Order paid", "service": "checkout",
 "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736", "span_id": "00f067aa0ba902b7",
 "order_id": "A-1001", "amount_cents": 4200}
```

`event` is a stable name to group on; `message` is for people. A field renamed in one service
breaks every query that spans them.

### What to keep out

Credentials and `Authorization` or `Cookie` headers; session IDs, except as a salted hash; a
name or an email, where an internal user ID will do; whole objects, since a deny-list misses
next month's field. Redact in the logger's pipeline, so every sink gets the same record.

### Personal data and retention

- **What counts.** The GDPR names online identifiers (fact `lo-gdpr`). The EU Court of Justice
  held a dynamic IP address personal data for a site with the legal means to identify the
  visitor (fact `lo-breyer`). An audit log is personal data of whoever made the change (fact
  `lo-edpb-logs`).
- **How much.** Log what the purpose needs, for no longer, and pseudonymize what must group
  (facts `lo-gdpr`, `lo-ico-storage`).
- **How long.** With no rule of your own, keep logs six months to a year, as the CNIL
  recommends, and up to three years only with a reason (fact `lo-cnil-retention`). Card-data
  systems keep a year, the last three months at hand (fact `lo-pci-retention`).

### Sampling

Sample `DEBUG` and `INFO` by rate; keep every record at 17 and up, and a trace's records with
its trace. This is our practice: the spec sets the threshold, not a sampling rule.

### Metrics and alerts

- **Per service:** rate, errors and duration (fact `lo-red`); with saturation, the four golden
  signals (fact `lo-golden`). **Per resource:** utilization, saturation and errors (fact
  `lo-use`).
- **Set an SLO.** The error budget is 100% minus the SLO. Page at 2% of it burned in an hour or
  5% in six hours, and open a ticket for slower burns (fact `lo-slo-budget`).
- **Keep labels bounded:** a route, never a user ID or a raw URL.
- **Prometheus:** pin the LTS on a server you don't upgrade often (fact `lo-prometheus`).
  OpenMetrics 2.0 is experimental (fact `lo-openmetrics2`): don't expose it alone.

## Mistakes

- **Values pasted into the message,** as in `f"user {uid} failed"`. Lines no longer group; keep
  the message fixed and put `uid` in a field.
- **An unkeyed hash of an email called anonymous.** Anyone can hash guesses and match them. Use
  a keyed hash, and treat the result as still personal.
- **IP addresses called technical, not personal** (fact `lo-breyer`). Give them a ceiling.
- **Logs kept forever, in case.** Set a ceiling, and delete at it.
- **One sampling rate for every level.** The errors an incident needs go with the noise.
- **"OK" printed because a step ran.** Print what was compared and the result.
- **Paging on CPU or memory.** Page on what users feel; put causes on a dashboard.
- **Trace Context Level 2 taken as finished** (fact `lo-tracecontext`).

## Audit

Severity uses the standard's status words, defined in this skill's `SKILL.md`.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Secrets logged | Log calls naming `password`, `Authorization`, `Cookie`, a session; objects whole | `BLOCKER` for a credential, else `GAP` | Redact in the pipeline |
| No offset | Naive `now()`, `%H:%M:%S`, local time in a log config | `DRIFT` | UTC with `Z` |
| Free text | String building in log calls; no JSON encoder | `GAP` | An encoder and fields |
| Logs apart from traces | Tracing in use, no `trace_id` in records | `GAP` | IDs from the active span |
| No retention | No deletion on a log store holding personal data | `GAP` | A ceiling, enforced |
| Sampling drops errors | One rate for every level | `DRIFT` | Keep 17 and up |
| A status line that claims a check | "OK" after a step that compared nothing | `BLOCKER` | Name the check and result |
| One run, two stories | Two records of a run; a total computed twice | `DRIFT` | One record, the rest derived |
| Pages on causes | Pages on CPU, memory or one error | `DRIFT` | Burn-rate pages on an SLO |

## Why

### Structured lines, fields and levels

A JSON line parses without a pattern, and one field set lets a query cross services.
OpenTelemetry recommends structured logs (fact `lo-otel-structured`); the field names and rule 3
are our practice. **Others:** logfmt is lighter. **Choose differently:** a command-line tool read
by a person writes plain lines to stderr.

### Timestamps, tracing and what to keep out

- **Offsets (L3).** One application logged in local time and wrote its evidence bundle in UTC,
  so one event sat four hours apart in the two (fact `la-rfc3339`).
- **Trace Context.** Level 2 has been a draft since 2024 (fact `lo-tracecontext`), so depend on
  Level 1. **Choose differently:** keep a request ID a partner already quotes.
- **Redaction.** OWASP lists data to treat rather than record (fact `lo-owasp-treat`). At each
  call site it's missed once; in the pipeline, it isn't. **Cost:** a hashed ID can be matched,
  not read.

### Personal data and retention

- **Reason:** logs hold identifiers on every line. Breyer read the 1995 Directive; the GDPR
  names online identifiers outright.
- **A floor and a ceiling** (fact `lo-owasp-retention`): too short, and a late-found incident
  has no trail; too long, and the log is personal data with no purpose.
- **Others:** NIST SP 800-92 is from 2006 and its Rev. 1 a draft (fact `lo-nist-800-92`): take
  no period from either.
- **Cost:** a deletion job, and a recorded reason for any period past a year.
- **Choose differently:** a legal hold or a sector rule sets its own period.

### Sampling

SeverityNumber 17 and up is the spec's mark of an error (fact `ll-otel-error`), so a cut there
works across libraries. **Cost:** errors in a flood still cost full price. **Choose
differently:** rate-limit a repeating error after its first records.

### Status lines and run records

- **L49:** an audited application printed "Copy OK" over output a checksum showed was wrong.
- **L19, L20:** two records of one run disagreed, and one total was derived in four files.
- **L4:** a bundle that listed what it skipped told "nothing missing" from "nothing collected".

### Metrics and paging

The SRE book puts its effort on symptoms over causes (fact `lo-golden`): a page means users are
hurt. Burn-rate pages fire fast for an outage and later for a slow leak (fact `lo-slo-budget`).
**Cost:** an SLO to agree, and enough traffic for a rate to mean something. **Choose
differently:** a batch job pages on a missed run.

## Facts

Law, guidance and versions, each named elsewhere by its ID.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `lo-otel-structured` | Structured logs recommended | [Logs](https://opentelemetry.io/docs/concepts/signals/logs/) | "structured (recommended)" | 2026-11-11 | 2027-05-11 |
| `lo-tracecontext` | Level 1 a Recommendation; Level 2 a draft | [Level 1](https://www.w3.org/TR/trace-context/), [Level 2](https://www.w3.org/TR/trace-context-2/) | "Trace Context W3C Recommendation 23 November 2021" and "Trace Context Level 2 W3C Candidate Recommendation Draft 28 March 2024" | 2026-11-11 | 2027-05-11 |
| `lo-owasp-treat` | Treat such data rather than log it; personal data needs care | [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | "should be removed, masked, sanitized, hashed, or encrypted" and "Non sensitive personal data" | 2026-11-11 | 2027-05-11 |
| `lo-owasp-session` | Log a salted hash of a session ID | [OWASP Sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | "log a salted-hash of the session ID instead of the session ID itself" | 2026-11-11 | 2027-05-11 |
| `lo-owasp-retention` | Keep logs for the retention period, and no longer | [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | "must not be destroyed before the duration of the required data retention period, and must not be kept beyond this time." | 2026-11-16 | 2027-05-16 |
| `lo-gdpr` | GDPR Art. 4(1) online identifiers; 5(1)(c) minimization; 5(1)(e) storage limitation; 32(1)(a) pseudonymization | [Regulation (EU) 2016/679](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679) | "an online identifier" and "limited to what is necessary" and "for no longer than is necessary" and "the pseudonymisation and encryption of personal data" | 2026-11-16 | 2027-05-16 |
| `lo-breyer` | CJEU, Breyer (2016), under Directive 95/46/EC: a dynamic IP address can be personal data | [Press release 112/16](https://curia.europa.eu/site/upload/docs/application/pdf/2016-10/cp160112en.pdf) | "The dynamic internet protocol address of a visitor constitutes personal data" and "Within the meaning of Directive 95/46/EC" | 2026-11-16 | 2027-05-16 |
| `lo-edpb-logs` | EDPB Guidelines 9/2022: audit log data can be personal data | [Guidelines 9/2022 v2.0](https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf) | "log data facilitating auditability" ... "may also qualify as personal data" | 2026-11-16 | 2027-05-16 |
| `lo-ico-storage` | ICO: keep personal data no longer than needed; page under review | [ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/) | "You must not keep personal data for longer than you need it." and "this guidance is under review" | 2026-11-16 | 2027-05-16 |
| `lo-cnil-retention` | CNIL délibération 2021-122: six months to a year; up to three years where justified | [CNIL](https://www.cnil.fr/fr/la-cnil-publie-une-recommandation-relative-aux-mesures-de-journalisation) | "pour une durée comprise entre six mois et un an" and "une durée maximale de trois ans" | 2026-11-16 | 2027-05-16 |
| `lo-pci-retention` | PCI DSS v4.0.1 10.5.1: 12 months, three at hand; secondary, PCI SSC not reached | [Microsoft Learn](https://learn.microsoft.com/en-us/entra/standards/pci-requirement-10) | "Retain audit log history for at least 12 months, with at least the most recent three months immediately available" | 2026-11-16 | 2027-05-16 |
| `lo-nist-800-92` | SP 800-92 final 2006-09-13; Rev. 1 a draft from 2023-10-11 | [SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final), [Rev. 1](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd) | "09/13/06: SP 800-92 (Final)" and "Date Published: October 11, 2023" | 2026-11-16 | 2027-05-16 |
| `lo-red` | RED: rate, errors, duration | [The RED Method](https://grafana.com/blog/the-red-method-how-to-instrument-your-services/) | "Rate (the number of requests per second)" and "Duration (the amount of time those requests take)" | 2026-11-11 | 2027-05-11 |
| `lo-use` | USE: utilization, saturation, errors | [The USE Method](https://www.brendangregg.com/usemethod.html) | "For every resource, check utilization, saturation, and errors." | 2026-11-11 | 2027-05-11 |
| `lo-golden` | Four golden signals; symptoms over causes | [SRE book, ch. 6](https://sre.google/sre-book/monitoring-distributed-systems/) | "The four golden signals of monitoring are latency, traffic, errors, and saturation." and "much more effort on catching symptoms than causes" | 2026-11-11 | 2027-05-11 |
| `lo-slo-budget` | Budget is 100% minus the SLO; page at 2% in 1 h or 5% in 6 h | [Implementing SLOs](https://sre.google/workbook/implementing-slos/), [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) | "the error budget is 100% minus the SLO." and "We recommend 2% budget consumption in one hour and 5% budget consumption in six hours" | 2026-11-11 | 2027-05-11 |
| `lo-prometheus` | Prometheus 3.16.0 (2026-11-04) current; 3.13 the LTS to 2027-07-31 | [Download](https://prometheus.io/download/), [Release cycle](https://prometheus.io/docs/introduction/release-cycle/) | "3.16.0 / 2026-11-04" and "Prometheus 3.13 2026-07-01 2027-07-31 Supported" | 2026-11-11 | 2027-02-11 |
| `lo-openmetrics2` | OpenMetrics 2.0 is an experimental release candidate | [OpenMetrics 2.0](https://prometheus.io/docs/specs/om/open_metrics_spec_2_0/) | "Version: 2.0.0-rc1" and "Status: Experimental" | 2026-11-11 | 2027-02-11 |

## Sources

| Source | Used for | License |
|---|---|---|
| OpenTelemetry, W3C Trace Context | Logs, trace IDs | CC BY 4.0; W3C document license: quoted |
| OWASP Cheat Sheet Series | Keeping data out, retention | CC BY-SA 4.0: brief quotes, our own words otherwise |
| EUR-Lex (GDPR); Microsoft Learn (PCI DSS, secondary) | Personal data, retention | CC BY 4.0: quoted with attribution |
| CJEU, EDPB, ICO, CNIL (French, quoted as written), NIST | Personal data, retention | Not checked: brief quotes, our own words otherwise |
| Google SRE book and Workbook | Signals, budgets, paging | CC BY-NC-ND 4.0: brief quotes, never adapted |
| Gregg (USE), Grafana (RED), Prometheus (Apache-2.0) | Metrics | Brief quotes |
| Audited repositories of this skill's owner, unnamed | L3, L4, L19, L20, L49 | Observed practice, our own words |

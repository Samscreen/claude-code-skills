# Error responses

Read this for what an HTTP API sends when a request fails: RFC 9457 problem details, which
status code, what ASP.NET Core, Spring, FastAPI, Express and Go send by default and how to
change it, and contract tests for error bodies. Read it too for an error message a person reads, in a dialog, a page or
a terminal: what it says, its tone, and what stays out of it.

What to catch, causes, exit codes, retries and timeouts are `error-handling`'s; each language's
syntax is its own module's. What goes into the log is logging-and-observability's. Where an
error appears on screen is the `user-experience` skill's interface-patterns, and preventing it
its usability-review.
API design beyond errors is the planned api-patterns module of the `architecture` skill.

## Rules

1. **An HTTP API answers every error with problem details,** RFC 9457's JSON shape, so one
   client handler reads them all.
2. **The status is honest:** 4xx when the request is wrong, 5xx when the server or its
   dependency failed. The body's `status` matches the response's, and an error is never a 200.
3. **Turn the framework's support on, then check what it sends.** No framework in the table
   covers every error by default, and each version changes what it fills in.
4. **Contract tests pin what you set, not what the framework fills in:** the status, your own
   `type` URIs and extension members. Never assert `"about:blank"` or a generated `instance`.
5. **Internals stay out of the response and the dialog.** No stack trace, exception message,
   SQL or path; they go to the log, with an ID the response carries.
6. **A message for a person says what happened and what to do,** in plain words, without
   blaming them. An error code or ID follows the sentence; it never replaces it.

### Problem details

RFC 9457 replaced RFC 7807 (fact `eh-rfc9457`). Clients branch on `type` and extension members,
never on `detail` (fact `eh-rfc9457-members`). A failed dependency is 5xx (fact
`eh-rfc9110-classes`).

```json
{
  "type": "https://example.com/problems/invalid-date",
  "title": "The date is not valid",
  "status": 422,
  "detail": "Month 13 in 2026-13-01. Use a month from 01 to 12.",
  "instance": "/bookings/7f3a"
}
```

### What each framework does by default

| Framework | By default | To cover every error |
|---|---|---|
| ASP.NET Core controllers | `[ApiController]` error results (status 400 and up) become problem details (fact `er-aspnet-controllers`) | Nothing more for those results |
| ASP.NET Core, everything else | An unhandled exception or an empty-body status code gets no problem details | `AddProblemDetails()` with `UseExceptionHandler()` and `UseStatusCodePages()`; an `Accept` of XML or HTML falls back to plain text (fact `er-aspnet-addproblemdetails`) |
| Spring Boot | `spring.mvc.problemdetails.enabled` and `spring.webflux.problemdetails.enabled` are false (fact `er-spring-boot-off`) | Set the one for your stack |
| Spring Framework 7.0 | `type` is unset, so the JSON omits it; 6.2 set `about:blank` (fact `er-spring-type`) | Set `type` yourself where clients branch on it |
| Spring Framework 7.1 | Not GA on 2026-11-16: RC2, with 7.1.x planned for 2026-11-30. It stops setting `instance` (fact `er-spring-71`) | Unhandled exceptions as problem details are opt-in: `configureProblemDetails` in a `WebMvcConfigurer`, calling `renderUnhandledExceptions(true)` |
| FastAPI | `HTTPException` and invalid requests get FastAPI's own JSON, not problem details (fact `er-fastapi`) | `@app.exception_handler` for Starlette's `HTTPException`, `RequestValidationError` and `Exception` |
| Express | Its built-in handler sends HTML, or `err.stack` unless `NODE_ENV` is `production` (fact `er-express`) | An error-handling middleware, with four arguments, added last |
| Go `net/http` | `http.Error` writes plain text; a handler that panics gets no response (fact `er-go-http`) | A helper that writes problem details, and a middleware that recovers panics |

Through ASP.NET Core 10, an unhandled `BadHttpRequestException` becomes a 500 unless the handler
copies its status, or a client's mistake reads as a server failure; 11 keeps it (fact
`er-aspnet-11`).

### Messages for people

- **Answer three questions:** what happened and why, what it means for the person, and what
  they can do (fact `er-win32-questions`). One message per known cause, not one for all.
- **Plain words, precise, with a fix** (facts `er-nng-h9`, `eh-govuk`): "The file is over 10
  MB. Choose a smaller one." The code or ID goes after, for support.
- **Don't blame the person** (fact `er-ms-blame`): "The date isn't valid", not "You entered an
  invalid date".
- **"Please": Microsoft's pages disagree.** Win32's say avoid it, as it makes a required action
  sound optional (fact `er-win32-questions`); Style and Tone allows it where the person is
  inconvenienced (fact `er-ms-please`). Our choice: never in an instruction; "Please wait" is
  fine.

## Mistakes

- **400 with a plain string when the database is down.** The client blames its request and
  doesn't retry. Send 503 or 500 as problem details.
- **A 200 with `{"error": ...}` in the body.** Caches, proxies and retry logic read success.
- **A stack trace or `exception.Message` in `detail` or a dialog,** or Express run without
  `NODE_ENV=production` (fact `er-express`). The person can't act on it; an attacker can (fact
  `er-aspnet-sensitive`).
- **Citing RFC 7807.** Assistants and Microsoft's pages still do. Cite RFC 9457.
- **Assuming Spring Boot sends problem details.** The properties are off (fact
  `er-spring-boot-off`).
- **Assuming `AddProblemDetails()` covers every client.** A browser's `text/html` gets the
  fallback (fact `er-aspnet-addproblemdetails`).
- **A contract test asserting `"type": "about:blank"`.** It fails on Spring 7, which omits it
  (fact `er-spring-type`). Assert the `type` you set, or none.
- **`Error 0x80070057` or "Invalid input" as the whole message.** Say which value, why, and the
  fix.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Wrong status class | 4xx for a server or dependency failure; 200 with an error body | `DRIFT` | 5xx, problem details |
| No common error shape | Ad hoc bodies, several shapes, `text/plain` errors | `GAP` | Rule 1 |
| Support left off | Spring Boot without the property; ASP.NET Core without `AddProblemDetails()` | `GAP` | Rule 3 and the table |
| Internals shown | A stack trace, exception text, SQL or path in a response or dialog | `GAP` | Message and ID; detail to the log |
| Tests pin defaults | `about:blank` or a generated `instance` asserted | `DRIFT` | Rule 4 |
| A message with no way out | No cause or next step; a bare code; blame | `GAP` | Rule 6 |

## Why

### Problem details and an honest status

- **The advice:** one shape, RFC 9457's, with 4xx and 5xx as RFC 9110 defines them.
- **The reason:** clients decide from the class whether to retry (fact `eh-aws-retry`), so a
  4xx for an outage stops a retry that would have worked. One shape lets one handler read every
  error and branch on `type`.
- **What it costs:** a `type` URI per problem a client acts on, documented.
- **When to choose differently:** a public API with its own published error schema keeps it.
  Changing shape breaks its clients; add problem details in a new version.

### Framework defaults

- **The advice:** turn support on, check the bodies by hand, and test only what you own.
- **The reason:** the defaults differ by framework and move by version. Spring 7.0 stopped
  setting `type` and 7.1 stops setting `instance` (facts `er-spring-type`, `er-spring-71`), so a
  test pinned to either breaks on an upgrade that clients don't notice.
- **What it costs:** a setting or a middleware, and a look at the bodies after each upgrade.
- **When to choose differently:** for a framework not in the table, look for its own problem
  details support before writing middleware.

### Internals out of the response

- **The advice:** the response says what failed; the log says why, joined by an ID.
- **The reason:** exception text tells an attacker the stack, the queries and the paths, and
  the person nothing. Microsoft calls serving it a security risk (fact `er-aspnet-sensitive`);
  Spring 7.1's opt-in never exposes the message (fact `er-spring-71`).
- **What it costs:** an ID in every error response and every matching log record.

### Messages for people

- **The advice:** what happened, why, and what to do, in plain words, without blame.
- **The reason:** a person can act on "The file is over 10 MB. Choose a smaller one", not on
  `Error 0x80070057`. NN/g, GOV.UK and Microsoft agree (facts `er-nng-h9`, `eh-govuk`,
  `er-win32-questions`, `er-ms-blame`).
- **What it costs:** a message per cause a person can fix, and keeping each one current.
- **When to choose differently:** for developers, add the code and the cause after the
  sentence; they will search for it.

## Facts

Each named elsewhere by its ID. `eh-` rows moved here from `error-handling` with their dates.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `eh-rfc9457` | RFC 9457 replaces RFC 7807 | [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) | "This document obsoletes RFC 7807." | 2026-11-11 | 2027-05-11 |
| `eh-rfc9457-members` | `status` matches; `detail` isn't parsed | [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) | "Generators MUST use the same status code in the actual HTTP response" and "Consumers SHOULD NOT parse the "detail" member for information" | 2026-11-11 | 2027-05-11 |
| `eh-rfc9110-classes` | 4xx: the client erred; 5xx: the server | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) | "indicates that the client seems to have erred." and "indicates that the server is aware that it has erred" | 2026-11-11 | 2027-05-11 |
| `eh-govuk` | Say what went wrong and how to fix it | [GOV.UK](https://design-system.service.gov.uk/components/error-message/) | "In the error message explain what went wrong and how to fix it." | 2026-11-11 | 2027-05-11 |
| `er-aspnet-controllers` | API controllers' error results become problem details | [API errors](https://learn.microsoft.com/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0) | "The automatic creation of a ProblemDetails for error status codes is enabled by default." | 2026-11-16 | 2027-05-16 |
| `er-aspnet-addproblemdetails` | `AddProblemDetails` turns middleware on; non-JSON falls back | [API errors](https://learn.microsoft.com/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0) | "the following middleware generates problem details HTTP responses when AddProblemDetails is called" and "Non-JSON media types, such as application/xml or text/html, are not supported and trigger the fallback behavior." | 2026-11-16 | 2027-05-16 |
| `er-aspnet-11` | ASP.NET Core 11 keeps `BadHttpRequestException`'s status | [API errors](https://learn.microsoft.com/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0) | "In ASP.NET Core 11 and later, UseExceptionHandler preserves BadHttpRequestException.StatusCode by default in problem details responses." | 2026-11-16 | 2027-02-16 |
| `er-aspnet-sensitive` | Don't send error detail to clients | [Errors](https://learn.microsoft.com/aspnet/core/fundamentals/error-handling?view=aspnetcore-10.0) | "Do not serve sensitive error information to clients. Serving errors is a security risk." | 2026-11-16 | 2027-05-16 |
| `er-spring-boot-off` | Spring Boot 4.1.2: both properties default to false | [Properties](https://docs.spring.io/spring-boot/appendix/application-properties/index.html) | "Whether RFC 9457 Problem Details support should be enabled." | 2026-11-16 | 2027-02-16 |
| `er-spring-type` | Spring Framework 7.0.10: `type` unset by default | [ProblemDetail](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/ProblemDetail.html) | "By default, this is not set. According to the spec, when not present, the type is assumed to be "about:blank"" | 2026-11-16 | 2027-02-16 |
| `er-spring-71` | Spring Framework 7.1: preview (RC2); `instance` not set; unhandled exceptions opt-in, message never exposed | [7.1 Release Notes](https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-7.1-Release-Notes) | "This is a preview page for Spring Framework 7.1.0, scheduled for November 2026." and "The instance field of ProblemDetail is no longer set automatically" and "This is opt-in through WebMvcConfigurer" and "The exception message is never exposed." | 2026-11-16 | 2027-02-16 |
| `er-fastapi` | FastAPI's own JSON by default; handle Starlette's `HTTPException`, and `Exception` | [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/), [Starlette](https://starlette.dev/exceptions/) | "These handlers are in charge of returning the default JSON responses when you raise an HTTPException and when the request has invalid data." and "you should register it for Starlette's HTTPException" and "Both keys 500 and Exception can be used." | 2026-11-16 | 2027-05-16 |
| `er-express` | HTML in production, else the stack; a handler takes four arguments, last | [Error handling](https://expressjs.com/en/guide/error-handling.html) | "The body will be the HTML of the status code message when in production environment, otherwise will be err.stack." and "error-handling functions have four arguments instead of three" and "You define error-handling middleware last" | 2026-11-16 | 2027-05-16 |
| `er-go-http` | `http.Error` writes plain text; a panic ends the request unanswered | [net/http](https://pkg.go.dev/net/http) | "The error message should be plain text." and "It recovers the panic, ... either closes the network connection or sends an HTTP/2 RST_STREAM" | 2026-11-16 | 2027-05-16 |
| `er-win32-questions` | Three questions; avoid "please" | [Win32](https://learn.microsoft.com/windows/win32/debug/error-message-guidelines) | "What happened and why?" and "What can the user do to prevent it from happening again?" and "Avoid the word "please". It can be interpreted to mean that a required action is optional." | 2026-11-16 | 2027-05-16 |
| `er-ms-please` | "Please" where the user is inconvenienced | [Style and Tone](https://learn.microsoft.com/windows/win32/uxguide/text-style-tone) | "Limit please to situations that inconvenience the user in some way" | 2026-11-16 | 2027-05-16 |
| `er-ms-blame` | Don't blame the user | [Writing style](https://learn.microsoft.com/windows/apps/design/style/writing-style) | "it's important that your error message doesn't blame the user." | 2026-11-16 | 2027-05-16 |
| `er-nng-h9` | NN/g heuristic 9 | [NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/) | "Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution." | 2026-11-16 | 2027-05-16 |

## Sources

Rules are in our own words; each quote is a dated fact above.

| Source | Used for | License |
|---|---|---|
| RFC 9457, RFC 9110 | Problem details, status | IETF Trust: short quotes, cited |
| Microsoft Learn: ASP.NET Core, Win32, Windows apps | Defaults; messages | CC BY 4.0: quoted, attributed |
| Spring Boot and Spring Framework docs, wiki | Defaults | Apache-2.0 projects; docs license not re-checked: short quotes, cited |
| Nielsen Norman Group | Heuristic 9 | All rights reserved: short quotes, our own words otherwise |
| GOV.UK Design System | Messages | Open Government Licence v3.0: quoted, attributed |
| FastAPI, Starlette, Express and Go docs | Their defaults | MIT, BSD-3-Clause, CC BY 4.0 and BSD-3-Clause: short quotes, cited |

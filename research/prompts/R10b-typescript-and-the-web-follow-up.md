# RESEARCH RUN R10b: TypeScript and the web, what R10 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: web-security, html-coding, javascript-coding, javascript-security.

## What this run is for

A follow-up. R10 (TypeScript, JavaScript, Node.js, HTML and CSS) was filed on 26 October 2026
and built into the coding skill's `javascript-coding`, `javascript-security`, `html-coding` and
`web-security` modules. The standard already names Node 26, Active LTS since 28 October 2026.
R10 ran out of room for security headers and cookies, the Baseline status of HTML and CSS
features, Temporal and `using`, and Node's permission model. This run takes those; CORS is
R19's, cookie consent R18's. Don't repeat its findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R10b · FORM: research-result v1
Save as: R10b-RESULT.md
Receiving session: this is research the repository owner asked for. Check each claim against the source it cites before relying on it. File the report under research/runs/, update the Facts section of each module it names, and list what changed. If you lack context, the owner will attach a file whose first line starts HANDOFF-FOR: rmccann-hub/claude-code-skills.
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

- Chrome, Firefox and Safari all treat a cookie without `SameSite` as `Lax`.
- RFC 6265bis, the cookie specification's revision, is still an Internet-Draft.
- The `popover` attribute is Baseline newly available, not yet widely available.
- Temporal is in ECMAScript 2026, and Safari hasn't shipped it outside Technology Preview.
- Node's permission model (`--permission`) is stable in Node 26 and restricts the file system,
  child processes and worker threads.

## Questions

### Priority

1. **Response headers and cookies:** from MDN, the OWASP HTTP Headers and Session Management
   cheat sheets, and the specifications: cookie attributes (`Secure`, `HttpOnly`, `SameSite` and
   each engine's default when it's missing, the `__Host-` prefix, CHIPS's `Partitioned`) and RFC
   6265bis's status; HSTS and the preload list's requirements; `X-Content-Type-Options`,
   `Referrer-Policy`, `Permissions-Policy`, and COOP, COEP and CORP for cross-origin isolation;
   and which old headers to drop (`X-XSS-Protection`, `X-Frame-Options`, `Expect-CT`).
2. **HTML elements that replace scripts:** Baseline status and dates, from MDN or the web-
   features data, for `<dialog>` with `showModal()`, the `popover` attribute, invoker commands
   (`command`, `commandfor`), customizable `<select>`, `<details name>`, `inert` and
   `hidden="until-found"`, with each one's known accessibility caveats from MDN, the WHATWG or
   the ARIA Authoring Practices Guide.
3. **CSS features:** Baseline status and dates for nesting, `:has()`, container queries,
   `@layer`, `@scope`, anchor positioning, view transitions, `light-dark()` and `text-wrap:
   balance`; and Tailwind CSS v4's CSS-first configuration, with its current version.
4. **Temporal and explicit resource management (`using`):** the ECMAScript edition that includes
   each, from Ecma's published ECMA-262; support by browser version and in Node 22, 24 and 26;
   and TypeScript's support for each, with the version.

### Standard

5. **Node's permission model:** its status in Node 24 and 26, what `--permission` and each
   `--allow-*` flag restrict, and what Node's docs say it doesn't protect against, quoted.
6. **Hidden and bidirectional characters in JavaScript sources:** ESLint's `no-irregular-
   whitespace` and any rule or plugin that flags bidirectional controls (Trojan Source,
   CVE-2021-42574), with Biome's and oxlint's equivalents and versions.

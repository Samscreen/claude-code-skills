# RESEARCH RUN R04b: Secure coding, what R04 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: secure-coding, input-handling.

## What this run is for

A follow-up. R04 (secure coding, authentication and cryptography) was filed on 23 September
2026, and the security skill's `secure-coding` module was built from it on 11 November 2026,
with every fact fetched again. R04 ran out of room for passkeys and recovery, server-side
fetches of user URLs, algorithm choices beyond TLS, security tools, and the measured security of
code that assistants write. This run takes those. OAuth, JWT, CORS and token storage are R19's;
headers and cookies R10b's. Don't repeat its findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R04b · FORM: research-result v1
Save as: R04b-RESULT.md
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

- WebAuthn Level 3 is still a W3C Candidate Recommendation, not a Recommendation.
- SP 800-63B-4 accepts synced passkeys at AAL2 but not at AAL3, and caps failed sign-in attempts
  at 100 per account.
- NIST IR 8547, which proposes deprecating quantum-vulnerable public-key algorithms after 2030
  and disallowing them after 2035, is still an initial public draft.
- Chrome, Firefox and Safari all negotiate X25519MLKEM768 by default.
- Semgrep's maintained rules are no longer under an open-source license, and Opengrep is a fork
  of its engine.

## Questions

### Priority

1. **Passkeys, MFA and account recovery:** WebAuthn Level 3's W3C status; what SP 800-63B-4 says
   of syncable authenticators, SMS and email codes, limits on failed attempts, and account
   recovery, quoted with section numbers; the current rules of OWASP's MFA and Forgot Password
   cheat sheets; and the current version, with its date, of a maintained WebAuthn server library
   for Python, Node.js, .NET and Java.
2. **Server-side requests to a URL a user supplies:** the OWASP SSRF Prevention Cheat Sheet's
   rules, quoted: allow-lists, resolving and checking the address, redirects, DNS rebinding, and
   cloud metadata endpoints (AWS IMDSv2, Azure, Google Cloud). For Python's requests and httpx,
   Node's `fetch` and undici, and .NET's `HttpClient`: whether each follows redirects by
   default, and the hook that lets code check the resolved IP before connecting.
3. **Algorithms and key sizes beyond TLS:** NIST SP 800-131A's current revision and its
   transition dates (SHA-1, 112-bit security, RSA and ECDSA sizes); NIST IR 8547's status; FIPS
   206's and the HQC draft's status; which browser versions turn hybrid ML-KEM on by default;
   and NIST's or the IETF's guidance on AES-GCM nonce limits against AES-GCM-SIV or
   XChaCha20-Poly1305 (SP 800-38D, RFC 8452).
4. **The security of code assistants and agents write, measured:** studies published since July
   2025 (for example a Veracode update, BaxBench, CWEval), with method, sample and results; and
   any controlled measurement of what lowers the flaw rate: security instructions in the prompt
   or a context file, static analysis fed back to the model, or a reviewing agent. Leave
   invented package names to R24.

### Standard

5. **Security tools for review:** current versions, and cost for public and private
   repositories, of CodeQL with GitHub code scanning, Semgrep Community Edition and Opengrep
   with each one's rule license, SonarQube Community Build, and Bandit; and any independent
   comparison of what each finds, with its date.
6. **Threat modeling a change rather than a system:** OWASP's Threat Modeling Cheat Sheet and
   A06:2025's text on threat modeling, quoted; the current versions of OWASP Threat Dragon and
   the Microsoft Threat Modeling Tool; and published accounts or measurements of threat modeling
   per change or per pull request.

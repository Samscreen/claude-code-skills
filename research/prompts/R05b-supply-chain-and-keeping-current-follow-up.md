# RESEARCH RUN R05b: Supply chain and keeping current, what R05 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: supply-chain-security, keeping-current.

## What this run is for

A follow-up. R05 (supply chain, versioning and releases) was filed on 23 September 2026. Its
release and versioning findings are built into git-workflows; its supply-chain findings wait in
a draft `supply-chain-security` module, beside R21 and R24. R24, not yet run, takes lockfiles,
checking provenance on install, and registries' defenses against invented names. This run takes
what the module needs beyond those: vulnerability scanning, SBOMs, publishing provenance,
judging a package, responding to a compromise, and tools for `keeping-current`. Don't repeat its
findings; where one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R05b · FORM: research-result v1
Save as: R05b-RESULT.md
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

- CycloneDX 1.7 is the newest release, and CycloneDX 2.0 hasn't shipped.
- GitHub's `actions/attest-build-provenance` meets SLSA Build Level 2; Level 3 needs signing
  isolated from the build, as in a reusable workflow.
- govulncheck reports only vulnerabilities in code the program can reach, while pip-audit, npm
  audit and OSV-Scanner report every vulnerable version in the lockfile.
- NuGet audits packages on restore by default, transitive packages included since the .NET 9
  SDK.
- The endoflife.date v1 API is still in beta.

## Questions

### Priority

1. **Scanning dependencies for known vulnerabilities:** for OSV-Scanner, pip-audit, npm audit,
   pnpm audit, govulncheck, cargo-audit and cargo-deny, NuGet's audit and bundler-audit: the
   current version with its date, the advisory database each reads, whether it scans the
   lockfile or the installed tree, whether it checks reachability, and its exit codes for CI,
   from each tool's docs. Say whether NVD's April 2026 change to enrichment affects any of them.
2. **SBOMs a small project can produce:** CycloneDX's and SPDX's current versions (has CycloneDX
   2.0 or SPDX 3.1 shipped?); syft, cdxgen, `npm sbom`, the CycloneDX tools for Python and .NET,
   and GitHub's dependency-graph SBOM export, with versions and the format each writes; and the
   status of VEX (OpenVEX, CSAF, CycloneDX VEX). Leave the Cyber Resilience Act's SBOM duties to
   R18.
3. **Publishing with provenance:** which SLSA Build level GitHub artifact attestations reach and
   what slsa-github-generator adds; SLSA 1.2's Source Track and any later version; trusted
   publishing and provenance today on npm, PyPI, crates.io and NuGet, from each registry's docs;
   and how the 2026 "Mini Shai-Hulud" campaign produced valid-looking provenance, from a primary
   write-up. Leave checking provenance on install to R24.
4. **Judging a package before adding it:** the OpenSSF Concise Guide for Evaluating Open Source
   Software, Scorecard run against a dependency, and deps.dev's signals, quoted; and any
   measurement linking a signal (maintainer count, release cadence, Scorecard score) to later
   compromise or abandonment.

### Standard

5. **Responding to a compromised dependency:** the guidance npm, GitHub, PyPI and CISA published
   after Shai-Hulud and its successors, quoted: what to rotate, what to look for (rogue self-
   hosted runners, new workflows), and when removing the package isn't enough; and 2025 to 2026
   incidents on PyPI, crates.io, NuGet, RubyGems and VS Code or Open VSX extensions, with the
   control that stopped or limited each.
6. **Tools that find and fix what's behind:** the endoflife.date API's status, Renovate's
   `endoflife-date` datasource, and per-language tools that rewrite deprecated API uses (`go
   fix`, Ruff's `UP` rules, pyupgrade, `cargo fix --edition`, and .NET's upgrade tooling), with
   versions and what each changes without a person.

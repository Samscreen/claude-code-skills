# RESEARCH RUN R24: Supply chain: installing, verifying, publishing and scanning

For the repository rmccann-hub/claude-code-skills · Prompt version 3 · Written 26 October 2026, updated 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: supply-chain-security, keeping-current, ci-cd, and the install advice in every language skill.

## What this run is for

The planned supply-chain-security module tells an agent to install exactly what was locked, to
check who built a package or an update rather than a checksum published beside it, and to check
a name before installing it; R21 and R05 (filed 26 October and 23 September 2026) didn't reach
those. This run fills them, and adds what the module needs beyond installs: publishing with
provenance, scanning for known vulnerabilities, SBOMs and VEX, and responding to a compromised
dependency. One table per question where the question names several ecosystems.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R24 · FORM: research-result v1
Save as: R24-RESULT.md
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

- pm ci` installs exactly what `package-lock.json` holds and fails when it disagrees with
  `package.json`; it doesn't update the lockfile.
- v sync --locked` fails when `uv.lock` is out of date, and `--frozen` installs from it without
  checking.
- m provenance links a package to the source repository and the workflow that built it, through
  Sigstore, and `npm audit signatures` checks it, but `npm install` doesn't check it by default.
- PI accepts PEP 740 attestations from trusted publishers, and neither pip nor uv checks them on
  install yet.
- tHub artifact attestations, checked with `gh attestation verify --signer-workflow`, prove
  which workflow built a file; a checksum published beside the file proves nothing about who
  made it.
- CycloneDX 1.7 is the newest release, and CycloneDX 2.0 hasn't shipped.
- GitHub's `actions/attest-build-provenance` meets SLSA Build Level 2; Level 3 needs signing
  isolated from the build, as in a reusable workflow.
- govulncheck reports only vulnerabilities in code the program can reach, while pip-audit, npm
  audit and OSV-Scanner report every vulnerable version in the lockfile.

## Questions

### Priority

1. **Installing exactly what was locked:** for npm, pnpm, Yarn, Bun, pip, uv, Poetry, Cargo, Go,
   NuGet, Composer and Bundler, as one table: the lockfile and whether a library should commit
   it; the command that installs from it and fails rather than updates when lockfile and
   manifest disagree; whether each package is checked against a hash in the lockfile by default,
   and how to turn that on; whether the install runs the package's own scripts by default, and
   the setting that stops it.
2. **Verifying provenance when installing:** for npm, PyPI, crates.io, NuGet, Go modules,
   RubyGems and Maven Central, as one table: what each proves (who built it, from which source
   and workflow) and what it doesn't; whether the installer checks it by default, on request or
   not at all, with the exact command or setting; and how much of each registry carries it
   today, measured and dated.
3. **Verifying a downloaded update in a project's own code:** what `gh attestation verify`
   checks, which flags pin the signer, and whether it works offline from a bundle file;
   sigstore-python, sigstore-js, sigstore-go and sigstore-rs with versions and maintenance
   status; and refusing a downgrade or a replayed old release: what The Update Framework and
   Go's checksum database do, and what a small project can do without them.
4. **Publishing with provenance:** which SLSA Build level GitHub artifact attestations reach and
   what slsa-github-generator adds; SLSA 1.2's Source Track and any later version; trusted
   publishing and provenance today on npm, PyPI, crates.io and NuGet, from each registry's docs;
   and how the 2026 "Mini Shai-Hulud" campaign produced valid-looking provenance, from a primary
   write-up. Leave checking provenance on install to R24.

### Standard

5. **Scanning dependencies for known vulnerabilities:** for OSV-Scanner, pip-audit, npm audit,
   pnpm audit, govulncheck, cargo-audit and cargo-deny, NuGet's audit and bundler-audit: the
   current version with its date, the advisory database each reads, whether it scans the
   lockfile or the installed tree, whether it checks reachability, and its exit codes for CI,
   from each tool's docs. Say whether NVD's April 2026 change to enrichment affects any of them.
6. **SBOMs a small project can produce:** CycloneDX's and SPDX's current versions (has CycloneDX
   2.0 or SPDX 3.1 shipped?); syft, cdxgen, `npm sbom`, the CycloneDX tools for Python and .NET,
   and GitHub's dependency-graph SBOM export, with versions and the format each writes; and the
   status of VEX (OpenVEX, CSAF, CycloneDX VEX). Leave the Cyber Resilience Act's SBOM duties to
   R18.
7. **Responding to a compromised dependency:** the guidance npm, GitHub, PyPI and CISA published
   after Shai-Hulud and its successors, quoted: what to rotate, what to look for (rogue self-
   hosted runners, new workflows), and when removing the package isn't enough; and 2025 to 2026
   incidents on PyPI, crates.io, NuGet, RubyGems and VS Code or Open VSX extensions, with the
   control that stopped or limited each.
8. **Registries' defences against typosquatted and invented names:** what npm, PyPI, crates.io
   and NuGet do today, with each policy's source and date; tools that check a name before it's
   installed, with versions; and measured rates of typosquatted packages taken down, and how
   fast.
9. **Mistakes AI coding assistants make with installs:** `npm install` where `npm ci` belongs,
   unpinned `pip install`, `curl | sh` installers, and disabling hash or signature checks to fix
   an error, with sources.
10. **Building a dependency from source:** published practice on pinning by full commit SHA
    rather than a tag or short prefix, checking the checkout landed on that commit, and refusing
    a dirty tree; and what Go modules, Cargo's git dependencies, pip's VCS requirements, npm's
    git dependencies and Meson's wraps check by default.

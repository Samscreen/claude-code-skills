# RESEARCH RUN R11b: C#, PowerShell and Windows Server, what R11 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 16 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 16 November 2026.

This run informs these categories: windows-admin, powershell-scripts, csharp-coding.

## What this run is for

A follow-up. R11 (C# and .NET, PowerShell, Windows Server and Active Directory) was filed on 26
October 2026 and built into csharp-coding, powershell-scripts and windows-admin. Those modules
already record .NET 11's release and the end of .NET 8 and 9 and PowerShell 7.4 and 7.5 on 10
November 2026. R11 ran out before AD hardening, installing modules and Windows desktop UI; this
run takes those. .NET Framework is R17's, and lock files R24's. Don't repeat its findings; where
one has changed since, say so.

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
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R11b · FORM: research-result v1
Save as: R11b-RESULT.md
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

- Windows Server 2025 domain controllers require LDAP signing by default in a new forest, and no
  Windows Server version enforces LDAP channel binding by default.
- Microsoft hasn't dated the release that turns network NTLM off by default, and IAKerb and
  Local KDC haven't shipped in a generally available update.
- Delegated managed service accounts (dMSA) need a Windows Server 2025 domain controller, and
  Microsoft fixed BadSuccessor, the dMSA takeover path, in August 2025 (CVE-2025-53779).
- `Install-PSResource` from PSResourceGet replaces `Install-Module`, and PowerShellGet 2.2.5
  gets security fixes only.
- WinForms dark mode (`Application.SetColorMode`) is still experimental in .NET 10 and 11.

## Questions

### Priority

1. **LDAP signing and channel binding:** the defaults on Windows Server 2025 domain controllers
   and on 2016 to 2022, the policies and registry values that require each, the Directory
   Service events that list clients that would break, and any enforcement change shipped in 2025
   or 2026 updates. Quote Microsoft Learn and the support.microsoft.com articles, with dates.
2. **NTLM's road to off:** what Phase 2 (IAKerb, Local KDC, Kerberos first in Negotiate) has
   shipped, in which update and for which versions; whether the next Windows Server LTSC has a
   name and date; and the audit events and policies that find NTLM use before it's disabled.
   Quote Microsoft's NTLM FAQ, Windows release health and Learn.
3. **Service accounts and AD CS:** gMSA against dMSA (requirements, functional level, migrating
   a standard service account), BadSuccessor and its fix; what ESC1 to ESC16 each mean, which
   ones Defender for Identity assesses; and strong certificate mapping's enforcement dates and
   current state from KB5014754. Primary sources only, with dates.
4. **Installing modules on 5.1 and 7.6:** PSResourceGet's current version and status, whether
   7.6 ships it and how 5.1 gets it, PowerShellGet 2.x and 3.x status, `Install-PSResource`
   against `Install-Module` (scope, repository trust, version ranges, `Save-PSResource` for
   offline hosts), and PowerShell Gallery policy changes since 2025. From Learn and the
   PSResourceGet repository's releases.
5. **WinForms and WPF on .NET 10 and 11:** dark mode (`SetColorMode`, WPF's Fluent theme) and
   whether each is still experimental; high DPI (`ApplicationHighDpiMode`, PerMonitorV2); what
   .NET 11 changed for WinForms (the visual-style refresh, `KioskModeManager`, analyzers WFO3000
   to WFO3002); CsWin32's current version; and toast notifications from an unpackaged app. From
   Learn and the dotnet/winforms, dotnet/wpf and microsoft/CsWin32 repositories.

### Standard

6. **.NET 11 as shipped:** the final "What's new in C# 15" on Learn (unions and `closed`:
   shipped or preview), the .NET 11 breaking-changes list, and the analyzer rules a .NET 11 SDK
   adds under `AnalysisLevel` `latest-Recommended`, which fail a `net10.0` build that treats
   warnings as errors.
7. **Baselines and Group Policy:** the current Windows Server 2025 security baseline's version
   and date, OSConfig's status, the CIS Windows Server 2025 benchmark's version, and MS16-072's
   effect on GPO security filtering (which group needs Read), from Microsoft Learn, the Security
   Compliance Toolkit and cisecurity.org.

# Verification: R16 (2026-11-24)

Checked by the receiving session on 2026-11-24. R16 changes no shipped file: no module yet states a
fact it covers. So only the claim this intake relies on was checked, the one the procedure work in
`word-documents` and the company's `samscreen-documents` uses now. The rest is checked when
`vba-coding`, `excel-master`, `epicor-kinetic` and `solidworks-automation` are built.

| Claim | Status | Checked against |
|---|---|---|
| python-docx 1.2.0 is current, released 16 June 2025, MIT | verified: 1.2.0 is the latest release, uploaded 2025-06-16, license MIT | [PyPI JSON API for python-docx](https://pypi.org/pypi/python-docx/json) |
| Question 4, Word templates (content controls versus placeholders, field and table-of-contents updating, numbering, what python-docx and the Open XML SDK can and can't do, accessibility) | **not covered**: section 4.4 says "Not covered this run", and section 9 lists "All of Question 4". `word-documents` has no checked research yet; R16b asks it again | the report itself |
| Everything else in the report | not yet checked | checked when the modules that rely on it are built (`research/README.md`) |

---

RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R16 · FORM: research-result v1
Save as: R16-RESULT.md
Receiving session: this is research the repository owner asked for. Check each claim against the source it cites before relying on it. File the report under research/runs/, update the Facts section of each module it names, and list what changed. If you lack context, the owner will attach a file whose first line starts HANDOFF-FOR: rmccann-hub/claude-code-skills.

# R16: Office (Excel, Word, VBA), Epicor Kinetic and SOLIDWORKS: state of play on 24 November 2026

Most of the "What we believe" list is broadly right, but six items are now wrong or out of date and must be corrected before the modules are updated: built-in VBA RegExp has already shipped (Version 2508); Excel's COPILOT function was retired on 14 September 2026; XlsxWriter is on 3.3.x, not 3.2.x; Epicor Kinetic moved from yearly/semi-annual releases to a monthly cadence in May 2026 and has announced an end to on-premises feature releases; SOLIDWORKS 2026 first shipped on 14 November 2025 (not October) and SOLIDWORKS 2027 SP0 is now available; and the `_xlws.` prefix is used together with `_xlfn.` (as `_xlfn._xlws.FILTER`), not on its own.

## TL;DR

- **VBA is supported but boxed in.** It runs on 64-bit Microsoft 365 by default, ActiveX is off by default (Office 2024 from October 2024, Microsoft 365 from Version 2504 in April 2025), VBScript is being phased out of Windows (Phase 2, "disabled by default", is expected around 2026 or 2027), and new Outlook has no COM add-ins or VBA. Use VBA for existing desktop-only workbooks; build new work as Office JS add-ins (unified JSON manifest GA July 2026), Office Scripts or Python.
- **The Excel and file-generation facts in the repository need a refresh.** COPILOT() is gone (cached values remain, recalculation gives #NAME?), DAX user-defined functions are GA (June 2026), openpyxl has had no release since 3.1.5 (28 June 2024), XlsxWriter 3.3.3 (20 November 2026) added pivot tables, and SheetJS must be installed from its CDN, not npm.
- **Epicor and SOLIDWORKS have moved.** Kinetic shipped 2026.100 in May 2026 on a monthly CI/CD cadence, retired the Smart Client, and Epicor's 6 January 2026 press release names 2028.1 (tentatively January 2028) as the final on-premises feature release, with Active Support through 31 December 2029. SOLIDWORKS 2027 SP0 is downloadable, SOLIDWORKS 2026 is at SP5.2 with hotfixes until 31 December 2027, SOLIDWORKS 2025 hotfixes end 31 December 2026, and the runtime requirement is .NET Framework 4.8.1.

## 1. Summary

1. Microsoft 365 installs 64-bit by default unless a 32-bit Office product is already present; write all `Declare` statements with `PtrSafe` and `LongPtr`.\[1\]
2. Built-in VBA regular expressions (`RegExp`, `Match`, `MatchCollection`, `SubMatches`) ship in Microsoft 365 Version 2508 (Build 19127.20154) and later; early binding to them fails on older builds.\[2\]
3. VBScript deprecation: Phase 1 (Feature on Demand, enabled) runs "now through 2026 or 2027"; Phase 2 (disabled by default) is "approximately 2026 or 2027"; Phase 3 (removal) is TBD. `.vbs` calls from VBA will stop working at Phase 3.\[2\]
4. ActiveX controls are disabled without notification by default in Word, Excel, PowerPoint and Visio on Windows (Office 2024 from October 2024; Microsoft 365 from April 2025, Version 2504).\[3\]\[4\]
5. New Outlook for Windows does not run COM/VSTO add-ins or VBA; existing classic Outlook installs are supported "until at least 2029"; Office LTSC 2024 ends support on 9 October 2029.\[5\]\[6\]\[7\]
6. Office 2021 and Office LTSC 2021 reached end of support on 13 October 2026: anything still targeting them is now unsupported.\[8\]
7. GROUPBY, PIVOTBY and PERCENTOF have been GA in Current Channel since 25 September 2024.
8. The Excel COPILOT() function was withdrawn on 14 September 2026 without ever reaching GA; do not generate it.
9. The unified JSON manifest for Word, Excel and PowerPoint add-ins became GA in July 2026 (Windows Version 2501+, Mac 16.103+); Visual Studio does not support it.\[9\]\[10\]\[11\]
10. DAX user-defined functions are GA from the June 2026 Power BI release; PBIR is becoming the default report format, but the Desktop default-on date has moved more than once (contested).\[12\]\[13\]\[14\]
11. Library versions now: openpyxl 3.1.5 (dormant), XlsxWriter 3.3.3, python-calamine 0.9.1, python-docx 1.2.0, python-pptx 1.0.2, DocumentFormat.OpenXml 3.5.1, ClosedXML 0.105.1, ExcelJS 4.4.0 (no stable release since 2023), SheetJS 0.20.3 (CDN only).
12. In [MS-XLSX], newer functions are stored as `_xlfn.NAME`, and some worksheet-only functions as `_xlfn._xlws.NAME` (FILTER, SORT, PY).\[15\]
13. Epicor Kinetic REST v2 needs an API key (`x-api-key` header) plus a user identity (Basic or Bearer); BAQs are at `/api/v2/odata/{Company}/BaqSvc/{BaqID}/Data`, Functions at `/api/v2/efx/{Company}/{Library}/{Function}`.
14. Epicor ERP 10.2.700 moved to sustaining support on 22 October 2022. Epicor's press release of 6 January 2026 (Business Wire) names 2028.1 as the final Kinetic on-premises feature release ("tentatively scheduled January 2028"), with "Active Support for release 2028.1 through December 31, 2029" and Sustaining Support from 1 January 2030.
15. SOLIDWORKS Document Manager API needs a free licence key available only to customers on subscription, and the key must be renewed with each major release.\[16\]\[17\]\[18\]

## 2. Corrections

| # | What we believed | What is true now | Source |
|---|---|---|---|
| C1 | "VBA will get built-in regular expressions" | Already shipped. "Starting with Office Version 2508 (Build 19127.20154) on Windows, RegExp classes are included in the VBA for Office by default."\[2\] Requires Microsoft 365 2508+; early binding "can't run on older Office versions".\[2\] | https://devblogs.microsoft.com/microsoft365dev/how-to-prepare-vba-projects-for-vbscript-deprecation/ (9 Sep 2025) |
| C2 | "projects using VBScript.RegExp keep working" | Only partly. Late-bound `CreateObject("VBScript.RegExp")` keeps working on Office 2508+ and on Windows with VBScript enabled; at Phase 3 "References to VBScript RegExp library will break unless the Office client is updated to a supported build."\[2\] Office LTSC 2024 (a 2408 build) does not get the built-in classes (inference from "These features require Microsoft 365 version 2508 or later"). | same |
| C3 | "ActiveX disabled by default since 2025" | Nuance: Office 2024 from October 2024; Microsoft 365 from April 2025 (Version 2504, Build 18730.20030).\[3\]\[4\] | https://www.bleepingcomputer.com/news/microsoft/microsoft-blocks-activex-by-default-in-microsoft-365-office-2024/ (secondary, Apr 2025); https://nolongerset.com/activex-disabled-in-office-2024/ (secondary, quotes Microsoft) |
| C4 | "Excel added … a COPILOT function" | Withdrawn: "Starting September 14, 2026, the COPILOT function is no longer available in Microsoft Excel." It was preview-only; recalculated cells return #NAME?. | https://support.microsoft.com/en-us/excel/functions/copilot-function (read 24 Nov 2026)\[19\] |
| C5 | "XlsxWriter 3.2.x is active" | XlsxWriter is on 3.3.x: 3.3.0 (22 Oct 2026), 3.3.1 (28 Oct 2026), 3.3.2 (19 Nov 2026), 3.3.3 (20 Nov 2026, adds `add_pivot_table`).\[20\]\[21\]\[22\] | https://xlsxwriter.readthedocs.io/changes.html; changelog excerpts in Dependabot PRs (secondary for 3.3.2/3.3.3) |
| C6 | "openpyxl 3.1.x is in maintenance" | Stronger: no release since 3.1.5 on 28 June 2024; 3.2.0b1 was yanked ("Not ready"). Treat as dormant.\[23\] | https://pypi.org/project/openpyxl/1.5.4/ (PyPI release history) |
| C7 | "Epicor releases Kinetic yearly (2025.1, 2025.2)" | Was semi-annual (2025.1, 2025.2). From May 2026 (release 2026.100) Kinetic moved "away from a semi-annual model and toward a monthly CI/CD cadence".\[24\] Version numbers are now 2026.100, 2026.103 and so on.\[25\] | https://www.epicor.com/en-us/blog/industries/release-2026-100-of-kinetic/ (May 2026) |
| C8 | "the classic client is retired" | Confirmed, with a date: "2025.2 as the final release supporting Smart Client"; retired from 2026.1/2026.100.\[26\] A Power Tools Client (introduced in 2025.2) remains for tasks such as DMT and Functions (secondary).\[27\]\[28\] | https://www.epicor.com/en-us/blog/industries/release-2025-2-of-kinetic/ (15 Oct 2025) |
| C9 | "SOLIDWORKS 2026 was released in October 2025" | The lifecycle table gives first release 11/14/2025. SOLIDWORKS 2027 SP0 is now "available for download"; 2026 is at SP5.2.\[29\] | https://www.solidworks.com/sw/support/solidworks-support.htm?tabshow=2 (read 24 Nov 2026) |
| C10 | "VSTA macros use .NET Framework" | Confirmed but specify: SOLIDWORKS 2026 requires ".NET Framework 4.8.1" and installs Visual Studio Tools for Applications 2022 (VSTA17).\[30\] The target framework for VSTA macro projects themselves was not found. | https://files.solidworks.com/Supportfiles/SW_Installation_Guide/2026/English/install_guide.pdf |
| C11 | "`_xlws.` for some worksheet functions" | It is a second prefix after `_xlfn.`: the spec lists `_xlfn._xlws.FILTER`, `_xlfn._xlws.SORT`, `_xlfn._xlws.PY`.\[15\] | https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/5d1b6d44-6fc1-4ecd-8fef-0b27406cc2bf |
| C12 | "VBA 7.1 is current" | Not verified this run (not found). | — |

Confirmed without change: 64-bit default; new Outlook lacks COM add-ins and VBA; classic Outlook supported until at least 2029;\[1\]\[5\]\[6\] GROUPBY, PIVOTBY, PERCENTOF exist and are GA; python-docx 1.2 is current; REST API v2 with API keys; BPM custom code is C# (language confirmed by forum code samples only; version not found); SOLIDWORKS API help is at help.solidworks.com.

## 3. Facts table

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| 1 | Microsoft 365 default bitness | 64-bit | https://support.microsoft.com/en-us/office/lifecycle/officeinstall/download-install-or-reinstall-microsoft-365-or-office-2024-on-a-pc-or-mac | "The 64-bit version is installed by default unless Microsoft 365 or Office detects you already have a 32-bit version of Microsoft 365 or Office … installed."\[1\] | read 24 Nov 2026 |
| 2 | VBScript Phase 1 | Enabled FOD, now through 2026 or 2027 | https://devblogs.microsoft.com/microsoft365dev/how-to-prepare-vba-projects-for-vbscript-deprecation/ | "Phase 1 (now through 2026 or 2027): VBScript remains enabled by default as a Feature on Demand (FOD)."\[2\] | 9 Sep 2025 |
| 3 | VBScript Phase 2 | Disabled by default | same | "Phase 2 (approximately 2026 or 2027): VBScript FODs will be disabled by default."\[2\] | 9 Sep 2025 |
| 4 | VBScript Phase 3 | Removal, TBD | same | "Phase 3 (TBD): VBScript will be completely removed from future Windows releases."\[2\] | 9 Sep 2025 |
| 5 | Built-in VBA RegExp | Version 2508 | same | "Starting with Office Version 2508 (Build 19127.20154) on Windows, RegExp classes are included in the VBA for Office by default." | 9 Sep 2025 |
| 6 | RegExp classes | 4 classes | same | "contain four types of classes to define the object type: RegExp, Match, MatchCollection, and SubMatches."\[2\] | 9 Sep 2025 |
| 7 | ActiveX default (M365) | Disabled, Version 2504 | https://www.tenforums.com/windows-10-news/219106-activex-soon-disabled-default-microsoft-365-a.html (secondary, reposts Microsoft text) | "ActiveX being disabled by default for Microsoft 365 will begin rolling out to users running Version 2504 (Build 18730.20030) or later from April 2025."\[4\] | Apr 2025 |
| 8 | ActiveX default (Office 2024) | October 2024 | https://nolongerset.com/activex-disabled-in-office-2024/ (secondary) | "This change occurs in October 2024 for Office 2024 and begins in April 2025 for Microsoft 365 apps."\[3\] | 2024 |
| 9 | Classic Outlook support | At least 2029 | https://learn.microsoft.com/en-us/microsoft-365-apps/outlook/get-started/guide-product-availability | "Existing installations of classic Outlook through perpetual and subscription licensing will continue to be supported until at least 2029."\[6\] | read 24 Nov 2026 |
| 10 | New Outlook opt-out notice | ≥12 months for managed Enterprise | same | "IT administrators will have at least 12 months notice before this stage is implemented in managed Enterprise plans."\[6\] | read 24 Nov 2026 |
| 11 | Office LTSC 2024 end of support | 9 Oct 2029 | https://support.microsoft.com/en-us/office/lifecycle/office-2024-and-office-ltsc-2024-faq | "Office LTSC 2024 will go out of support on October 9, 2029."\[7\] | read 24 Nov 2026 |
| 12 | Office LTSC 2024 policy | Fixed, 5 years | same | "The commercial version of Office LTSC 2024 has 5 years of support under the Fixed Lifecycle Policy."\[7\] | read 24 Nov 2026 |
| 13 | GROUPBY/PIVOTBY GA | 25 Sep 2024 | https://techcommunity.microsoft.com/blog/excelblog/new-aggregation-functions-groupby-and-pivotby/3965765 | "September 25th 2024 Status These functions are now generally available to users in the Current Channel." | 25 Sep 2024 update\[31\] |
| 14 | PERCENTOF signature | PERCENTOF(data_subset,data_all) | same | "It's a simple function that SUM's its first argument and divides by the SUM of its second argument." | 14 Nov 2023\[31\] |
| 15 | TRIMRANGE | Announced Beta 2409 | https://techcommunity.microsoft.com/blog/excelblog/announcing-trimrange-and-accompanying-trim-references/4230202 | "This new function and new references are currently available to Beta Channel users running Version 2409 (Build 18020.2000) or later." | 28 Aug 2024\[32\] |
| 16 | COPILOT function | Withdrawn 14 Sep 2026 | https://support.microsoft.com/en-us/excel/functions/copilot-function | "When a cell that contains the function recalculates, the function returns a #NAME? error because it's no longer recognized." | read 24 Nov 2026\[19\] |
| 17 | Unified manifest GA (WXP) | July 2026 | https://devblogs.microsoft.com/microsoft365dev/unified-manifest-for-office-add-ins-now-ga/ | "We're excited to announce the general availability of unified manifest support for Word, Excel, PowerPoint Add-ins, in addition to Outlook Add-ins."\[9\]\[33\] | 16–17 Jul 2026 |
| 18 | Unified manifest client minimums | Win 2501, Mac 16.103 | https://learn.microsoft.com/en-us/office/dev/add-ins/develop/unified-manifest-overview | "Excel, PowerPoint, and Word on Windows (Version 2501 (18407.20002) or later) connected to a Microsoft 365 subscription"\[11\] | read 24 Nov 2026 |
| 19 | DAX UDFs GA | June 2026 release | https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/dax-user-defined-functions-generally-available/5185738 | "DAX UDF will be enabled by default in the June 2026 release of Power BI Desktop"\[13\] | Jun 2026\[34\] |
| 20 | PBIR default | Service first, Desktop later | https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-June-2026-Feature-Summary/ba-p/5193264 | "PBIR will become the default code format for Power BI reports."\[12\] | Jun 2026\[34\] |
| 21 | openpyxl latest | 3.1.5, 28 Jun 2024 | https://pypi.org/project/openpyxl/1.5.4/ | "3.1.5 Jun 28, 2024" | read 24 Nov 2026\[23\] |
| 22 | XlsxWriter 3.3.1 | 28 Oct 2026 | https://xlsxwriter.readthedocs.io/changes.html | "Fixed issue where "future" functions such as ISFORMULA() weren't prefixed with _xlfn. in conditional_format() and data_validation() formulas." | 28 Oct 2026\[20\] |
| 23 | XlsxWriter 3.3.3 | 20 Nov 2026, pivot tables | https://github.com/CERT-Polska/Artemis/pull/3468 (secondary, quotes changelog) | "Added support for worksheet pivot tables via the :func:add_pivot_table method." | 20 Nov 2026\[21\] |
| 24 | python-calamine latest | 0.9.1, 3 Nov 2026 | https://www.piwheels.org/project/python-calamine/ | "0.9.1 2026-11-03" | read 24 Nov 2026\[35\] |
| 25 | python-docx latest | 1.2.0, 16 Jun 2025 | https://pypi.org/project/python-docx/ | "Released: Jun 16, 2025" | read 24 Nov 2026\[36\] |
| 26 | python-pptx latest | 1.0.2, 7 Aug 2024 | https://www.piwheels.org/project/python-pptx/ | "1.0.2 2024-08-07" | read 24 Nov 2026\[37\] |
| 27 | Open XML SDK latest | 3.5.1, 18 Mar 2026 | https://www.nuget.org/packages/documentformat.openxml | "3.5.1 … 3/18/2026" | read 24 Nov 2026\[38\] |
| 28 | ClosedXML latest | 0.105.1, 25 Jul 2026 | https://www.nuget.org/profiles/ClosedXML | "Latest version: 0.105.1" / "last updated 7/25/2026" | read 24 Nov 2026\[39\] |
| 29 | ClosedXML 0.105 dependency | OpenXml 3.1.1–4.0.0 | https://github.com/ClosedXML/ClosedXML/discussions/2697 | "the expected version for 0.105, which is DocumentFormat.OpenXml 3.1.1-4.0.0." | 18 May 2025\[40\] |
| 30 | ExcelJS latest | 4.4.0 | https://www.npmjs.com/package/exceljs | "Latest version: 4.4.0, last published: 3 years ago." | read 24 Nov 2026\[41\] |
| 31 | SheetJS source of truth | CDN, 0.20.3 | https://docs.sheetjs.com/docs/getting-started/installation/nodejs/ | "The SheetJS CDN https://cdn.sheetjs.com/ is the authoritative source for SheetJS modules." | read 24 Nov 2026\[42\] |
| 32 | SheetJS on npm | stale 0.18.5 | same | "The latest version on that registry is 0.18.5" | read 24 Nov 2026\[42\] |
| 33 | [MS-XLSX] future functions | Extends ISO 29500 list | https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/5d1b6d44-6fc1-4ecd-8fef-0b27406cc2bf | "The predefined functions ([ISO/IEC29500-1:2016] section 18.17.7) are extended by the following future functions."\[15\] | read 24 Nov 2026 |
| 34 | `_xlpm.` | LAMBDA parameters | XlsxWriter docs (secondary) | "the parameters in the LAMBDA() function must have a '_xlpm.' prefix."\[43\] | read 24 Nov 2026 |
| 35 | Kinetic cadence | Monthly CI/CD from May 2026 | https://www.epicor.com/en-us/blog/industries/release-2026-100-of-kinetic/ | "Beginning with the May 2026 release, Kinetic is moving away from a semi-annual model and toward a monthly CI/CD cadence." | May 2026\[24\] |
| 36 | Smart Client end | 2025.2 last | https://www.epicor.com/en-us/blog/industries/release-2025-2-of-kinetic/ | "With 2025.2 as the final release supporting Smart Client, it is critical to plan your transition to the modern browser experience" | 15 Oct 2025\[26\] |
| 37 | Kinetic final on-prem release | 2028.1, tentatively Jan 2028 | https://www.businesswire.com/news/home/20260106279383/en/ (Epicor press release) | "Final on-premises release: 2028.1 tentatively scheduled January 2028" | 6 Jan 2026 |
| 38 | Kinetic Active Support end | 31 Dec 2029; Sustaining from 1 Jan 2030 | https://www.businesswire.com/news/home/20260106279383/en/ (Epicor press release) | "Active Support for release 2028.1 through December 31, 2029 / Sustaining Support begins January 1, 2030" | 6 Jan 2026 |
| 39 | ERP 10.2.700 | Sustaining from 22 Oct 2022 | https://encompass-inc.com/wp-content/uploads/2020/11/Epicor-ERP-10.2.700-Release-Guide.pdf (partner copy of Epicor guide) | "Epicor ERP 10.2.700 | October 22, 2020 | Active | Move to Sustaining October 22, 2022" | Nov 2020\[44\] |
| 40 | REST v2 auth | API key + user identity | https://www.epiusers.help/t/rest-efx-baq-examples-from-a-python-script/115273 (forum) | "headers = {'accept' : 'application/json', 'X-API-Key' : 'blablablabla'}" with "session.auth = (user, password)" | 1 Jun 2024\[45\] |
| 41 | Monthly update window (cloud) | 2 months to apply | https://www.erp-information.com/epicor-erp-review (secondary, quoting Epicor PM on forum) | "you have 2 months to upgrade pilot/production on your own cadence" | 7 May 2026\[46\] |
| 42 | SOLIDWORKS 2026 lifecycle | First 11/14/2025, hotfixes end 12/31/2027 | https://www.solidworks.com/sw/support/solidworks-support.htm?tabshow=2 | "SOLIDWORKS 2026 | 11/14/2025 | TBD/2026 | 12/31/2027"\[29\] | read 24 Nov 2026 |
| 43 | SOLIDWORKS current | 2027 SP0; 2026 SP5.2 | same | "SOLIDWORKS 2027 SP0 is available\[29\] for download"\[29\] | read 24 Nov 2026 |
| 44 | SOLIDWORKS .NET | 4.8.1 | https://files.solidworks.com/Supportfiles/SW_Installation_Guide/2026/English/install_guide.pdf | ".NET Framework 4.8.1 are required for all SOLIDWORKS products"\[30\] | 2026 guide |
| 45 | SOLIDWORKS Office support | 2026 SP5 last for Office 2021 | https://files.solidworks.com/Supportfiles/Release_Notes/2026/English/relnotes.htm | "SOLIDWORKS Design 2026 SP5 is the last release to support Microsoft Word® 2021, Excel 2021, and PowerPoint 2021."\[47\] | 2026 |
| 46 | Document Manager key | Subscription only | https://help.solidworks.com/2027/english/api/swdocmgrapi/GettingStarted-swdocmgrapi.html | "The SOLIDWORKS Document Manager API requires a license key that is only available via the SOLIDWORKS customer portal to SOLIDWORKS customers who are currently under subscription."\[16\] | 2027 help |
| 47 | InsertBomTable4 (IView) | Obsolete → InsertBomTable5 | https://help.solidworks.com/2024/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable4.html | "Obsolete. Superseded by IView::InsertBomTable5."\[48\] | 2024 help |
| 48 | OpenDoc | Obsolete → OpenDoc6 | https://help.solidworks.com/2026/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc.html | "Obsolete. Superseded by ISldWorks::OpenDoc6."\[49\] | 2026 help |

## 4. Findings

### 4.1 VBA and Office automation today

**Support status.** VBA itself is not on a retirement path in the sources read; what is being retired is VBScript, a separate Windows component.\[50\] The Microsoft 365 Developer Blog (Wenjun Gong, Principal Product Manager, 9 September 2025) names the two exposure points: "Executing external .vbs scripts from VBA" and "Referencing VBScript type libraries, such as VBScript.RegExp for regular expressions."\[2\]

**64-bit and Declare.** Because 64-bit is the default for new Microsoft 365 installs (Fact 1), any `Declare` without `PtrSafe` fails to compile on 64-bit Office, and handles and pointers must be `LongPtr`. Use `#If VBA7 Then` only if the code must still run on Office 2007 or earlier; otherwise write `PtrSafe` and `LongPtr` everywhere. Version 2606 does not force a move from 32-bit to 64-bit; existing 32-bit installs stay 32-bit (windowsforum.com, secondary).\[51\]

**Macro blocking and Trusted Locations.** Not re-verified this run (see section 9). Keep the existing module text but mark it "not re-verified in R16".

**ActiveX.** The new default is "Disable all controls without notification", equivalent to the DisableAllActiveX group policy.\[52\] Existing controls render as static images.\[53\] Admins can turn it back via Trust Center, the registry value `HKCU\Software\Microsoft\Office\Common\Security\DisableAllActiveX = 0`, or group policy (University of Toronto EASI, secondary, quoting Microsoft).\[52\] Recommendation: replace ActiveX controls on sheets with Form controls or a UserForm; do not tell users to re-enable ActiveX.

**VBScript and RegExp.** Phases are as in Facts 2–4. For new code, use the built-in classes with early binding (`Dim re As RegExp: Set re = New RegExp`) and no reference to vbscript.dll; that requires Microsoft 365 2508+. For code that must also run on Office LTSC 2021/2024 or older Microsoft 365 builds, keep late binding (`CreateObject("VBScript.RegExp")`), which "works on Office versions 2508 or later, regardless of Windows client version and on earlier Windows versions with VBScript enabled".\[2\] Any VBA that shells out to `cscript`/`wscript` or a `.vbs` file must be rewritten (PowerShell or native VBA) before Phase 3.

**Outlook.** The migration has three stages: opt-in (GA by 1 August 2024), opt-out ("new Outlook is on by default … Users can still revert"), and cutover ("users won't be able to switch back to classic Outlook").\[6\] Microsoft has published no cutover date. A Microsoft Q&A community answer says the opt-out phase begins in April 2026, and goskills.com (secondary) says new Outlook becomes the default after March 2027;\[54\]\[55\] neither is an authoritative Microsoft statement, so treat the opt-out date as **contested**. New Outlook does not support COM add-ins (Directions on Microsoft: "One feature from classic Outlook which will not be available at all with the new Outlook is COM add-in support").\[56\] Outlook automation should move to Office JS add-ins or Microsoft Graph.

**What to use instead of VBA for new work.**
- **Office JS add-ins** with the unified manifest (GA July 2026): cross-platform (web, Windows, Mac), centrally deployed.\[9\]
- **Office Scripts plus Power Automate** for Excel automation that runs in the cloud. Platform coverage was not re-verified this run.
- **Python in Excel** for analysis. The Microsoft Excel Blog ("What's New in Excel (March 2025)", 25 March 2025) says "Python in Excel is now generally available to eligible Enterprise and Business users in Excel for the web and preview for Family and Personal users"; "Copilot in Excel with Python" is also GA (Excel blog: "available worldwide on Windows and Web platforms", 7 Apr 2025).
- **VBA is still right** for desktop-only Windows workbooks and Access/Word tooling that need the file system, COM or other Office apps, in organisations that will stay on classic Outlook and Windows desktop until at least 2029.

### 4.2 Excel

**Functions since 2023.** Confirmed: GROUPBY, PIVOTBY and PERCENTOF (GA 25 September 2024); TRIMRANGE and trim references (announced to Beta, Version 2409, 28 August 2024; the Microsoft Excel Blog "What's New in Excel (March 2025)", 25 March 2025, says "This feature has rolled out to all Windows CC (Current Channel) and MEC (Monthly Enterprise Channel) users."). COPILOT was **withdrawn on 14 September 2026**.\[19\]\[57\] REGEXTEST, REGEXEXTRACT, REGEXREPLACE: not verified this run. Python in Excel is GA: "Python in Excel is now generally available to eligible Enterprise and Business users in Excel for the web and preview for Family and Personal users" (Microsoft Excel Blog, 25 March 2025); its limits were not verified this run (see section 9).

**Office Scripts platforms; requirement sets.** Not covered.

**Unified manifest.** GA for Word, Excel and PowerPoint in July 2026; minimum clients are Windows Version 2501 (18407.20002) on a Microsoft 365 subscription and Mac Version 16.103.\[9\]\[11\] Microsoft says "Add-ins that use the unified manifest can't be installed on all platforms."\[11\] McKenna Consultants (secondary), citing Learn, says "Visual Studio doesn't support the unified manifest for Office Add-ins", so use the Yeoman generator or Microsoft 365 Agents Toolkit.\[10\]\[58\] Recommendation: use the unified manifest for new add-ins aimed at current Microsoft 365. Keep an add-in-only XML manifest where volume-licensed Office (LTSC) or other unsupported clients must be served.

**DAX and Power BI formats.**
- DAX user-defined functions became GA with the June 2026 release (Desktop 2.155.756.0 per enterprisedna.co, secondary).\[34\] Optional parameters with default expressions arrived at GA. A Power BI project (PBIP) stores functions in `functions.tmdl` (databear.com, secondary).\[59\]\[60\]\[61\]
- PBIR timeline is **contested**. The Learn update archive first said "The March release sets PBIR as the default in Power BI Desktop". A later entry says "The PBIR default-on rollout resumes in the service, with Desktop default-on timing planned after rollout stability checks".\[14\] The June 2026 summary still says PBIR "will become the default" and "eventually, the only supported format".\[12\]
- Treat PBIR as the target format and do not promise a specific Desktop default date.\[34\]\[62\]

**Power Query M.** Not covered.

### 4.3 Generating Office files from code

**Python.**
- **openpyxl** 3.1.5 (28 June 2024) is still the latest; it has had no release for more than two years, and 3.2.0b1 was yanked.\[23\]\[63\] It is fine for reading and editing existing workbooks, but it does not calculate formulas.
- **XlsxWriter** 3.3.3 (20 November 2026) is write-only and actively maintained.\[21\] 3.3.0 added image validation; 3.3.1 fixed `_xlfn.` prefixing inside conditional formats and data validation; 3.3.2 sped up formula handling and fixed false "future function" detection; 3.3.3 added worksheet pivot tables.\[20\]\[21\]\[22\]\[64\] The changelog notes that applications that do not refresh pivot tables on load "will show an empty pivot table".\[64\]
- **python-calamine** 0.9.1 (3 November 2026) is an MIT-licensed, read-only Rust binding.\[65\]\[66\] Beware the separate fork `python-calamine-reducto`.\[67\]
- **pandas engines:** not re-verified this run.
- **python-docx** 1.2.0 (16 June 2025) and **python-pptx** 1.0.2 (7 August 2024) are current but infrequently released.\[68\]\[69\]

**.NET.** DocumentFormat.OpenXml 3.5.1 (18 March 2026; previous 3.4.1 on 6 January 2026).\[70\] ClosedXML 0.105.1 (25 July 2026), whose 0.105 line expects OpenXml 3.1.1–4.0.0. ClosedXML says it "is not thread-safe" (libraries.io README).\[40\]\[71\]

**JavaScript.** ExcelJS 4.4.0 (npm `latest`, 2023-10-19) with a 4.4.1-prerelease.0 (2024-12-20) per runstamp.com (secondary); it has had no stable release in three years, so treat it as low-maintenance.\[72\] SheetJS Community Edition 0.20.3 is distributed from cdn.sheetjs.com; npm `xlsx` is frozen at 0.18.5 (March 2022) and missing later security fixes.\[42\]\[73\] `docx` (npm): not found.

**OOXML prefixes.** [MS-XLSX] §2.2.3 extends the ISO/IEC 29500 function list with "future functions": names such as `_xlfn.XLOOKUP`, `_xlfn.LET`, `_xlfn.LAMBDA`, `_xlfn.SORTBY`, `_xlfn.UNIQUE`, and `_xlfn._xlws.FILTER`, `_xlfn._xlws.SORT`, `_xlfn._xlws.PY`. Some newer-than-2007 functions such as NETWORKDAYS.INTL and ISO.CEILING appear without `_xlfn.`.\[15\] The `_xlpm.` rule for LET/LAMBDA parameter names was confirmed only from XlsxWriter's documentation (secondary);\[43\] the [MS-XLSX] Formulas grammar page was not read. Rule for skills: write the prefixed name in the file, display the unprefixed name to users, and never prefix functions that are in the ISO list.\[43\]\[74\]

**Recalculation.** Not covered in depth. One sourced point: a recalculating engine that does not know a function shows `#NAME?` (the COPILOT case).\[19\]\[74\]

### 4.4 Word templates

Not covered this run (see section 9). No claims are made here.

### 4.5 Epicor Kinetic (public sources; customer-only items flagged)

**Release and cadence.**
- Kinetic 2025.2 was announced 15 October 2025. Kinetic 2026.100 shipped in May 2026 and moved cloud customers to a monthly CI/CD cadence.\[24\]\[26\]
- Per partner onekloudx.com.au (secondary), "Release 2026.103, available in August 2026, is the first monthly release under this model", and the larger changes are concentrated in "one annual baseline release each March".\[25\]
- On the forum, Epicor staff described a Continuous Track (cloud: monthly features and patches) and a Maintenance Track (patches only).\[75\]
- Cloud customers can self-apply a monthly update and, per Epicor's product manager quoted by erp-information.com (secondary), "you have 2 months to upgrade pilot/production on your own cadence".\[25\]\[46\]
- The 2026.1 cloud upgrade schedule was revised (forum: pilot 4–6 June, production 10–12 July 2026). This conflicts with "released in May 2026" from partner sources; on-premises GA and cloud production dates differ, so treat exact dates as **contested**.\[76\]\[77\]
- Full release notes and availability matrices are on EpicWeb and are **customer-only**.

**Support.**
- ERP 10.2.700 (released 22 October 2020) moved to sustaining support on 22 October 2022.\[44\]
- Active support historically covers roughly the last two years of releases (Estes Group, secondary). A forum user reported the "2-year deadline for 2023.2 support which expires this month" (October 2025).\[78\]\[79\]
- On 6 January 2026 Epicor announced, in a Business Wire press release ("Epicor Announces Schedule of Final On-Premises Feature Releases for Kinetic, Prophet 21, and BisTrack"), "Final on-premises release: 2028.1 tentatively scheduled January 2028 / Active Support for release 2028.1 through December 31, 2029 / Sustaining Support begins January 1, 2030"; Epicor's Vaibhav Vohra is quoted: "These final on-premises releases mark an important milestone in that journey."

**REST API v2.**
- Every call needs an API key (header `x-api-key`; created in API Key Maintenance) plus a user identity (Basic or Bearer token).\[80\]\[81\]\[82\]
- Business objects: `/{instance}/api/v2/odata/{Company}/Erp.BO.{Name}Svc/{EntitySet}` with OData `$select`, `$filter`, `$orderby`, `$top`, `$skip`.\[80\]\[83\]
- BAQs: `/api/v2/odata/{Company}/BaqSvc/{BaqID}/Data` (the `/Data` segment is required).\[82\]\[83\]
- Kinetic Functions: `POST /api/v2/efx/{Company}/{Library}/{Function}` with a JSON body.\[82\]\[84\]
- Forum examples (Kevin Lincecum, epiusers.help, 1 June 2024) show exactly these shapes.\[45\] Epicor's own REST help (customer-only on EpicWeb) was not read, so the URL shapes are corroborated by the forum and partners, not Epicor's public documentation.
- Server-side paging limits were not found.

**BPM.** C# is the custom-code language (forum and partner examples). C# language version, server .NET version and restrictions in Epicor-hosted cloud tenants: not found.

**BAQ Designer, Application Studio, UD fields.** Application Studio replaces classic Smart Client customizations, which must be converted before 2026.1 (Mayan Technologies, secondary, quoting the in-product warning "Customizations, dashboards, and Product Configurator need to be converted to the browser client before 2026.1").\[28\] `_UD` tables and `_c` columns: not verified this run.

### 4.6 SOLIDWORKS API

- **Current release.** SOLIDWORKS 2027 SP0 is available; its release date was not found. Third-party reports put the 2027 pre-release at 10 August 2026 and SP0 between about 17 and 24 November 2026 (an inference).\[85\]\[86\] SOLIDWORKS 2026 is at SP5.2, first released 14 November 2025, with hotfixes until 31 December 2027.\[29\] The product is now branded "SOLIDWORKS Design".\[87\]
- **API help.** At `help.solidworks.com/<year>/english/api/`. The per-version "API release notes" page lists new and obsolete members by service pack;\[88\] the 2026 page needs JavaScript to render.
- **VSTA.** "Microsoft Visual Studio Tools for Applications (VSTA) is a toolset based on Microsoft VB.NET and C# and is installed with SOLIDWORKS."\[89\] The 2026 installer requires .NET Framework 4.8.1 and installs VSTA 2022.\[30\] The 2024 help still says Visual Studio 2019 is needed to record, edit or debug .NET macros, which is **contested/likely stale**.\[90\]
- **Obsolete methods.** Confirmed: `ISldWorks::OpenDoc` → `OpenDoc6`; `IView::InsertBomTable4` → `InsertBomTable5`.\[48\]\[49\] Correction to the prompt's example: **OpenDoc6 is not obsolete**. `OpenDoc7` exists for display states and SOLIDWORKS Connected, and both are current.\[91\]\[92\] SaveAs3/SaveAs4 and CreateSectionViewAt5/6: not verified. Dassault's SolidPractices note says obsolete members usually still work.\[93\]
- **Document Manager.** A free licence key is available only to customers on subscription. It must be passed when connecting and renewed for each major release; files saved by a newer version than the key will not open.\[16\]\[17\]\[18\]\[94\]
- **PDM API and STEP AP242 export options.** Not covered.

### 4.7 Power Platform

Not covered (see section 9).

### 4.8 Mistakes AI assistants make

See section 7.

## 5. Tools

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| openpyxl | Read/edit xlsx | 3.1.5 | 28 Jun 2024 | `pip install openpyxl` | — | PyPI\[63\] |
| XlsxWriter | Write xlsx | 3.3.3 | 20 Nov 2026 | `pip install XlsxWriter` | — | xlsxwriter.readthedocs.io/changes.html\[21\] |
| python-calamine | Fast read xlsx/xls/xlsb/ods | 0.9.1 | 3 Nov 2026 | `pip install python-calamine` | — | piwheels\[35\] |
| python-docx | Read/write docx | 1.2.0 | 16 Jun 2025 | `pip install python-docx` | — | PyPI\[36\] |
| python-pptx | Read/write pptx | 1.0.2 | 7 Aug 2024 | `pip install python-pptx` | — | piwheels\[37\] |
| DocumentFormat.OpenXml | .NET OOXML SDK | 3.5.1 | 18 Mar 2026 | `dotnet add package DocumentFormat.OpenXml` | .csproj | nuget.org\[38\] |
| ClosedXML | .NET Excel wrapper | 0.105.1 | 25 Jul 2026 | `dotnet add package ClosedXML` | .csproj | nuget.org\[39\] |
| ExcelJS | JS read/write xlsx | 4.4.0 | 19 Oct 2023 | `npm i exceljs` | package.json | npmjs.com\[72\] |
| SheetJS CE | JS read/write spreadsheets | 0.20.3 | not found (tag dated 2024-07-18 per secondary) | `npm i --save https://cdn.sheetjs.com/xlsx-0.20.3/xlsx-0.20.3.tgz` | package.json | docs.sheetjs.com\[42\]\[72\] |
| Microsoft 365 Agents Toolkit / Yeoman generator | Unified-manifest add-ins | not found | — | not found | manifest.json | devblogs.microsoft.com |
| SOLIDWORKS Design | CAD + API | 2027 SP0 (2026 SP5.2) | 2027 SP0: not found | — | — | solidworks.com support page |

## 6. Changing in the next 12 months (to 24 November 2027)

| Item | What changes | When | Status | Source |
|---|---|---|---|---|
| VBScript Phase 2 | FODs disabled by default; `.vbs` and early-bound VBScript RegExp start breaking where not re-enabled\[2\] | "approximately 2026 or 2027" | **Flag: may land within 12 months** | Microsoft 365 Dev Blog |
| New Outlook opt-out | New Outlook on by default; ≥12 months notice for managed Enterprise\[6\] | contested (April 2026 / after March 2027 claims) | **Flag** | Learn; Q&A; goskills (secondary) |
| Epicor Kinetic monthly releases | Monthly cloud updates; 2-month window to apply | ongoing | Active | Epicor blog; forum\[24\]\[46\] |
| Epicor 2024.2 active support | Roughly 2 years after release, so about late 2026 (inference from the 2-year rule) | ~Q4 2026 | **Flag (inference)** | Estes Group (secondary); forum\[78\]\[79\] |
| PBIR default in Desktop | PBIR default-on; eventually the only format | date contested | **Flag** | Power BI blog; Learn archive |
| SOLIDWORKS 2027 service packs | SP1+ expected; dates not found | not found | — | — |
| SOLIDWORKS 2026 hotfixes | End 31 Dec 2027 (just outside 12 months)\[29\] | 31 Dec 2027 | Watch | solidworks.com |
| SOLIDWORKS 2025 hotfixes | End 31 Dec 2026: lifecycle row "SOLIDWORKS 2025 | 11/15/2024 | 10/2025 | 12/31/2026"; "No SP's or hotfixes are available after this date." | 31 Dec 2026 | **Flag: confirmed, within 12 months** | solidworks.com/sw/support/solidworks-support.htm?tabshow=2 (read 24 Nov 2026) |
| Office 2021 / LTSC 2021 | Already ended 13 Oct 2026; Project/Visio 2021 connectivity "until October 2026"\[8\]\[95\] | passed | Already out of support | Learn connectivity page; eosl.date (secondary) |
| Excel COPILOT() | Already removed 14 Sep 2026 | passed | Remove from skills | support.microsoft.com\[19\] |

## 7. Common mistakes (including AI assistants)

1. **Generating `=COPILOT(...)` formulas.** The function was withdrawn on 14 September 2026; recalculation returns #NAME? (support.microsoft.com).\[19\]
2. **Telling users to add a reference to "Microsoft VBScript Regular Expressions 5.5"** on Microsoft 365 2508+. It is no longer needed and will break when VBScript is removed; use the built-in `RegExp` instead, or late binding for mixed estates (Microsoft 365 Dev Blog).\[2\]
3. **`Declare` without `PtrSafe`, or `Long` for handles,** on default 64-bit installs (Fact 1).
4. **Suggesting ActiveX controls on worksheets.** They are disabled by default since October 2024 (Office 2024) and April 2025 (Microsoft 365).\[3\]\[4\]
5. **Writing Outlook VBA or COM add-ins as if they will run in new Outlook.** They will not (Directions on Microsoft; Learn).\[56\]\[96\]
6. **`npm install xlsx`.** It installs the stale 0.18.5; SheetJS says its CDN is authoritative (docs.sheetjs.com).\[42\]\[97\]
7. **Writing newer functions without `_xlfn.`** (or FILTER/SORT without `_xlfn._xlws.`) when generating OOXML directly. Excel then shows #NAME? until re-entered ([MS-XLSX] §2.2.3).\[15\]\[74\]\[98\] XlsxWriter fixed this inside conditional formats and data validation only in 3.3.1.\[20\]
8. **Expecting openpyxl or XlsxWriter to compute formula results.** Neither calculates; values appear only after a spreadsheet application recalculates. XlsxWriter's pivot tables are likewise empty until refreshed (XlsxWriter changelog).\[64\]
9. **Calling Epicor REST v2 without `x-api-key`, using v1 BAQ URLs without `/Data`, or omitting the company segment** (forum examples; partner guides).\[80\]\[82\]
10. **Generating Smart Client (classic) customization code for Kinetic 2026.x.** The classic client is retired; use Application Studio (Epicor 2025.2 blog).\[26\]\[99\]
11. **Treating SOLIDWORKS `OpenDoc6` as obsolete, or using `IView::InsertBomTable4` in new code** (SOLIDWORKS API help).\[48\]\[49\]\[91\]
12. **Hard-coding a SOLIDWORKS Document Manager key across major versions.** Keys must be renewed per major release (SOLIDWORKS API help).\[18\]\[100\]
13. **Assuming built-in RegExp exists on Office LTSC 2024.** The blog says the features "require Microsoft 365 version 2508 or later".\[2\]

## 8. Sources and licences

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| Microsoft Learn (docs, [MS-XLSX] open specs) | Microsoft Terms of Use; many Learn docs repos are CC BY 4.0 for text and MIT for code (not verified per page this run) | Yes, brief | Yes | Only if the page's repo licence is MIT; otherwise rewrite | "Microsoft Learn, <page title>, <URL>" |
| support.microsoft.com | Microsoft Terms of Use (all rights reserved) | Brief quotes only | Yes | No | Title + URL |
| Microsoft 365 Developer Blog / Tech Community / Fabric community blog | Microsoft Terms of Use | Brief quotes only | Yes | Short snippets for illustration only; prefer rewriting | Author, title, date, URL |
| XlsxWriter docs/changelog | BSD-2-Clause (project licence; not re-verified this run) | Yes | Yes | Yes, keep copyright notice | "XlsxWriter, John McNamara" + URL |
| openpyxl, python-docx, python-pptx, python-calamine (PyPI) | MIT (per PyPI/libraries.io) | Yes | Yes | Yes, keep MIT notice | Project name + URL |
| Open XML SDK, ClosedXML (NuGet) | MIT (not re-verified this run) | Yes | Yes | Yes, keep notice | Project name + URL |
| ExcelJS | MIT (runstamp.com, secondary) | Yes | Yes | Yes, keep notice | "ExcelJS, Guyon Roche" |
| SheetJS docs / CE | Apache-2.0 (npm mirror pages) | Yes | Yes | Yes, keep NOTICE | "SheetJS LLC" + URL |
| Epicor.com blogs | Epicor copyright | Brief quotes only | Yes | No | Title, date, URL |
| EpicWeb / EpicCare | Customer-only; Epicor copyright | No (not publicly accessible) | Only what is public | No | — |
| Epicor User Help Forum (epiusers.help) | User-contributed, Discourse; no explicit open licence found | Brief quotes | Yes | Rewrite; do not copy code verbatim without the poster's permission | Poster, thread title, date, URL |
| SOLIDWORKS help / support pages / install guide | Dassault Systèmes copyright | Brief quotes only | Yes | No verbatim copying of examples; write original code against the documented API | "SOLIDWORKS API Help <year>" + URL |
| Secondary sites (BleepingComputer, Directions on Microsoft, windowsforum, partner blogs, runstamp, erp-information, kore1, uncap, onekloudx) | All rights reserved | Brief quotes, labelled secondary | Yes | No | Site, title, date, URL |

## 9. Not found, contested, not covered

**Not found.**
- VBA 7.1 as the current version.
- The [MS-XLSX] grammar text for `_xlpm.`.
- SOLIDWORKS 2027 SP0 release date, the VSTA macro target framework, and SaveAs3/SaveAs4 and CreateSectionViewAt5/6 status. (SOLIDWORKS 2025 end of hotfixes is now confirmed as 31 December 2026 from the SOLIDWORKS Product Support Lifecycle table.)
- Epicor BPM C# language version, server .NET version, cloud BPM restrictions, REST paging limits, and `_UD`/`_c` conventions.
- The `docx` (npm) version.
- TRIMRANGE GA is now sourced: the Microsoft Excel Blog (25 March 2025) says it "has rolled out to all Windows CC (Current Channel) and MEC (Monthly Enterprise Channel) users."
- Epicor's 2028.1 and 31 December 2029 dates are now confirmed by Epicor's own press release (Business Wire, 6 January 2026).

**Contested.**
- New Outlook opt-out start date: April 2026 per a Microsoft Q&A community answer versus after March 2027 per goskills.com; Microsoft Learn gives no date, only "at least 12 months notice".\[6\]\[54\]\[55\]
- PBIR Desktop default date: "March release" in the Learn archive versus a later "timing planned after rollout stability checks";\[14\] one secondary site claims PBIP/PBIR default by September 2026.\[62\]
- Kinetic 2026.1/2026.100 timing: May 2026 (Epicor blog) versus the cloud production upgrade 10–12 July 2026 (forum).\[24\]\[76\]
- SOLIDWORKS VSTA requirements: Visual Studio 2019 (2024 help) versus VSTA 2022 (2026 install guide).\[30\]\[90\]

**Not covered (out of room).**
- Macro blocking from the internet (Mark of the Web) and Trusted Locations: re-verify.
- REGEX* functions, Python in Excel limits (GA status is sourced to the Microsoft Excel Blog, 25 March 2025), Aptos default font.
- Office Scripts platforms, Office JS requirement sets, Power Query M changes.
- LibreOffice headless and Excel COM recalculation pitfalls, and pandas engines.
- All of Question 4 (Word content controls, fields/updateFields, numbering, python-docx/Open XML SDK capability limits, accessibility checker, PDF/UA).
- SOLIDWORKS PDM API and STEP AP242 export.
- Question 7 (Power Platform licensing and desktop versus cloud flows).

## Sources

1. [Download, install, or reinstall Microsoft 365 or Office 2024 on a PC or Mac](https://support.microsoft.com/en-us/office/lifecycle/officeinstall/download-install-or-reinstall-microsoft-365-or-office-2024-on-a-pc-or-mac)
2. [Prepare your VBA projects for VBScript deprecation in Windows - Microsoft 365 Developer Blog](https://devblogs.microsoft.com/microsoft365dev/how-to-prepare-vba-projects-for-vbscript-deprecation/)
3. [ActiveX Disabled by Default in Office LTSC 2024](https://nolongerset.com/activex-disabled-in-office-2024/)
4. [ActiveX soon disabled by default in Microsoft 365 - Windows 10 Help Forums](https://www.tenforums.com/windows-10-news/219106-activex-soon-disabled-default-microsoft-365-a.html#post2682024)
5. [Outlook Classic Support Extended to 2029: What Power Users Need to Know About the Transition](https://www.getmailbird.com/outlook-classic-extended-power-user-transition-guide/)
6. [Stages of migration to new Outlook for Windows](https://learn.microsoft.com/en-us/microsoft-365-apps/outlook/get-started/guide-product-availability)
7. [Office 2024 and Office LTSC 2024 FAQ](https://support.microsoft.com/en-us/office/lifecycle/office-2024-and-office-ltsc-2024-faq)
8. [Microsoft Office End of Life (EOL) Dates and End of Support (EOS) Dates](https://eosl.date/eol/product/office/)
9. [Build Once, Run Everywhere: Unified Manifest for Office Add-Ins now Generally Available - Microsoft 365 Developer Blog](https://devblogs.microsoft.com/microsoft365dev/unified-manifest-for-office-add-ins-now-ga/)
10. [Unified Manifest for Word, Excel and PowerPoint Add-Ins: Migration, Dual Manifests and Your Support Matrix](https://www.mckennaconsultants.com/unified-manifest-for-word-excel-and-powerpoint-add-ins-migration-and-support-matrix/)
11. [Office Add-ins with the unified app manifest for Microsoft 365 - Office Add-ins](https://learn.microsoft.com/en-us/office/dev/add-ins/develop/unified-manifest-overview)
12. [Power BI June 2026 Feature Summary](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-June-2026-Feature-Summary/ba-p/5193264)
13. [DAX User-Defined Functions (Generally Available)](https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/dax-user-defined-functions-generally-available/5185738)
14. [Previous monthly updates to Power BI Desktop and the Power BI service - Power BI](https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-latest-update-archive)
15. Microsoft Learn
16. [Getting Started - 2027 - SOLIDWORKS Design Help](https://help.solidworks.com/2027/english/api/swdocmgrapi/GettingStarted-swdocmgrapi.html?id=25)
17. [API Support](https://www.solidworks.com/sw/support/api-support.htm)
18. [How To Request a SOLIDWORKS Document Manager API Key](https://www.goengineer.com/blog/request-solidworks-document-manager-api-key)
19. [COPILOT Function](https://support.microsoft.com/en-us/excel/functions/copilot-function)
20. [Changes in XlsxWriter - Read the Docs](https://xlsxwriter.readthedocs.io/changes.html)
21. [build(deps): bump xlsxwriter from 3.3.1 to 3.3.3 in /docs by dependabot\[bot\] · Pull Request #3468 · CERT-Polska/Artemis · GitHub](https://github.com/CERT-Polska/Artemis/pull/3468)
22. [Bump xlsxwriter from 3.3.1 to 3.3.2 in /docker/xslxwriter by dependabot\[bot\] · Pull Request #6998 · ExodusIntelligence/demisto-dockerfiles · GitHub](https://github.com/ExodusIntelligence/demisto-dockerfiles/pull/6998)
23. [openpyxl · PyPI](https://pypi.org/project/openpyxl/1.5.4/)
24. [Kinetic 2026.100 ERP Release: Planning, Financials, UX Updates](https://www.epicor.com/en-us/blog/industries/release-2026-100-of-kinetic/)
25. [The End of the Big ERP Upgrade-Epicor Kinetic Release 2026.103](https://onekloudx.com.au/epicor-kinetic-monthly-releases/)
26. [Release 2025.2 of Kinetic: Purpose-Built for the Future of Manufacturing](https://www.epicor.com/en-us/blog/industries/release-2025-2-of-kinetic/)
27. [Epicor Consultant Job Description Template 2026 - KORE1](https://www.kore1.com/epicor-consultant-job-description-template/)
28. [Epicor’s Migration to Kinetic UI: What You Need to Know Before the 2026 Deadline](https://www.mayantechs.com/post/epicors-migration-to-kinetic-ui)
29. [SOLIDWORKS Support](https://www.solidworks.com/sw/support/solidworks-support.htm?tabshow=2)
30. [INSTALLATION AND ADMINISTRATION SOLIDWORKS 2026](https://files.solidworks.com/Supportfiles/SW_Installation_Guide/2026/English/install_guide.pdf)
31. [New aggregation functions: GROUPBY and PIVOTBY](https://techcommunity.microsoft.com/blog/excelblog/new-aggregation-functions-groupby-and-pivotby/3965765)
32. [Announcing TRIMRANGE and accompanying trim references](https://techcommunity.microsoft.com/blog/excelblog/announcing-trimrange-and-accompanying-trim-references/4230202)
33. [Build Once, Run Everywhere: Unified Manifest for Office Add-Ins now Generally Available](https://www.dotnetramblings.com/post/17_07_2026/17_07_2026_13/)
34. [Power BI Desktop, June 2026: what actually matters for housing reporting - BaseData BI](https://www.basedatabi.com/blog/power-bi-june-2026)
35. [piwheels - python-calamine](https://www.piwheels.org/project/python-calamine/)
36. [python-docx · PyPI](https://pypi.org/project/python-docx/)
37. [piwheels - python-pptx](https://www.piwheels.org/project/python-pptx/)
38. [NuGet Gallery](https://www.nuget.org/packages/documentformat.openxml)
39. [NuGet Gallery](https://www.nuget.org/profiles/ClosedXML)
40. [Exception during opening existing file · ClosedXML/ClosedXML · Discussion #2697 · GitHub](https://github.com/ClosedXML/ClosedXML/discussions/2697)
41. [exceljs - npm](https://www.npmjs.com/package/exceljs)
42. [NodeJS](https://docs.sheetjs.com/docs/getting-started/installation/nodejs/)
43. [Working with Formulas - XlsxWriter - Read the Docs](https://xlsxwriter.readthedocs.io/working_with_formulas.html)
44. [Epicor ERP 10.2.700 Release Guide - Encompass Solutions](https://encompass-inc.com/wp-content/uploads/2020/11/Epicor-ERP-10.2.700-Release-Guide.pdf)
45. [REST/EFx/BAQ Examples? -- From a Python Script - Kinetic ERP - Epicor User Help Forum](https://www.epiusers.help/t/rest-efx-baq-examples-from-a-python-script/115273)
46. [Epicor Kinetic (Epicor ERP) Review 2026: Pricing & Features](https://www.erp-information.com/epicor-erp-review)
47. [SOLIDWORKS Design 2026 SP5 Release Notes](https://files.solidworks.com/Supportfiles/Release_Notes/2026/English/relnotes.htm)
48. [InsertBomTable4 Method (IView) - 2024 - SOLIDWORKS Design Help](https://help.solidworks.com/2024/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable4.html)
49. [OpenDoc Method (ISldWorks) - 2026 - SOLIDWORKS Design Help](https://help.solidworks.com/2026/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc.html)
50. [VBScript Deadline: Audit Your Firm's Excel Macros](https://hisab360.net/blog/vba-vs-office-scripts-vs-python.html)
51. [Microsoft 365 Apps 2606 Keeps 32-Bit; Test Add-Ins by Sept 8](https://windowsforum.com/news/microsoft-365-apps-2606-keeps-32-bit-office-test-add-ins-by-sept-8.439345/)
52. [ActiveX will be disabled by default in Microsoft Office Apps](https://easi.its.utoronto.ca/activex-will-be-disabled-by-default-in-microsoft-office-apps/)
53. [Microsoft blocks ActiveX by default in Microsoft 365, Office 2024](https://www.bleepingcomputer.com/news/microsoft/microsoft-blocks-activex-by-default-in-microsoft-365-office-2024/)
54. [New Outlook vs Old Outlook: What’s Different and Can You Switch Back?](https://www.goskills.com/microsoft-office/resources/new-outlook-vs-old-outlook)
55. [New Outlook to replace Classic Outlook? - Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5787077/new-outlook-to-replace-classic-outlook)
56. [Microsoft to support classic Outlook for Windows (for some) until at least 2029 - Directions on Microsoft](https://www.directionsonmicrosoft.com/microsoft-to-support-classic-outlook-for-windows-for-some-until-at-least-2029/)
57. [Microsoft is ditching the COPILOT function in Excel before it even launches](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-is-ditching-the-copilot-function-in-excel-before-it-even-launches)
58. [The Office Add-in Manifest Explained (XML vs Unified)](https://orfys.com/blogs/office-add-in-manifest-guide)
59. [DAX User-Defined Functions](https://docs.tabulareditor.com/en/tutorials/udfs.html)
60. [Power BI June 2026: DAX UDFs Are Generally Available — Enterprise DNA](https://enterprisedna.co/resources/news/power-bi-dax-udfs-generally-available-june-2026/)
61. [Reusable DAX: User-Defined Functions in Power BI - Data Bear](https://databear.com/reusable-dax-power-bi/)
62. [Power BI September 2026 update: the features that matter](https://ecclesieagazzi.com/insights/power-bi-september-2026-update.html)
63. [openpyxl (PyPI) — latest version 3.1.5](https://vigia.coredls.cloud/pypi/openpyxl)
64. [Build(deps): bump xlsxwriter from 3.3.1 to 3.3.3 in /docker/xslxwriter by dependabot\[bot\] · Pull Request #48163 · demisto/dockerfiles · GitHub](https://github.com/demisto/dockerfiles/pull/48163)
65. [python-calamine 0.8.2 on PyPI - Libraries.io - security & maintenance data for open source software](https://libraries.io/pypi/python-calamine)
66. [View pypi: python-calamine](https://debricked.com/select/package/pypi-python-calamine)
67. [python-calamine-reducto 0.7.21 on PyPI - Libraries.io - security & maintenance data for open source software](https://libraries.io/pypi/python-calamine-reducto)
68. [python-docx](https://pypistats.org/packages/python-docx)
69. [python-pptx](https://security.snyk.io/package/pip/python-pptx)
70. [DocumentFormat.OpenXml 3.5.1 on NuGet - Libraries.io - security & maintenance data for open source software](https://libraries.io/nuget/DocumentFormat.OpenXml)
71. [ClosedXML 0.105.1 on NuGet - Libraries.io - security & maintenance data for open source software](https://libraries.io/nuget/ClosedXML)
72. [Alternatives to ExcelJS for Node.js Excel files](https://runstamp.com/alternatives/exceljs)
73. [xlsx Vulnerability Fix: Upgrade SheetJS and Secure Uploads](https://vallettasoftware.com/blog/post/xlsx-sheetjs-vulnerability-fix)
74. [Functions — ClosedXML 0.102.0 documentation](https://docs.closedxml.io/en/latest/features/functions.html)
75. [Kinetic's Transition to Monthly CI/CD Releases - what is your opinion - Kinetic ERP - Epicor User Help Forum](https://www.epiusers.help/t/kinetics-transition-to-monthly-ci-cd-releases-what-is-your-opinion/134486)
76. [2026.1 Release Schedule Changes - Kinetic ERP - Epicor User Help Forum](https://www.epiusers.help/t/2026-1-release-schedule-changes/133615)
77. [What's New in Epicor Kinetic 2026.100](https://www.e-c-solutions.com/en/knowledge/blog/new-epicor-kinetic-2026-100/)
78. [Epicor ERP Database: Key Considerations for Upgrades](https://www.estesgrp.com/blog/epicor-erp-database-upgrade-considerations/)
79. [2025.2 release date for on prem? - Kinetic ERP - Epicor User Help Forum](https://www.epiusers.help/t/2025-2-release-date-for-on-prem/129981)
80. [Epicor Kinetic to Microsoft Fabric Integration Guide](https://numlytics.com/blog/epicor-kinetic-to-microsoft-fabric/)
81. [Epicor REST API Integration & System Connections](https://www.amit-erp.com/services/epicor-rest-api-integrations.html)
82. [Epicor Kinetic Authentication, Functions, and BPM](https://knowledgelib.io/business/erp-integration/epicor-authentication-customization/2026)
83. [Epicor API Guide: REST API Documentation for Kinetic](https://blog.hyperbots.com/epicor-api-guide-rest-api-documentation-for-kinetic)
84. [Epicor Kinetic REST API v2](https://knowledgelib.io/business/erp-integration/epicor-rest-api-v2/2026)
85. [SOLIDWORKS 2027 New Features: What's New and When It Ships](https://skill-lync.com/blogs/solidworks-2027-new-features)
86. [SOLIDWORKS 2027 Release Date and Status (Nov 2026)](https://solidworksclub.com/versions/2027/)
87. [SolidWorks](https://en.wikipedia.org/wiki/SolidWorks)
88. [Release Notes - 2026 - SOLIDWORKS Design Help](https://help.solidworks.com/2026/english/api/sldworksapi/ReleaseNotes-sldworksapi.html)
89. [SOLIDWORKS Macros - 2026 - SOLIDWORKS Design Help](https://help.solidworks.com/2026/english/api/sldworksapiprogguide/GettingStarted/SolidWorks_Macros.htm)
90. [2024 api - Microsoft Visual Studio Tools for Applications (VSTA)](https://help.solidworks.com/2024/english/api/sldworksapiprogguide/GettingStarted/VSTA_2015.htm?format=P&value=)
91. [OpenDoc6 Method (ISldWorks) - 2022 - SOLIDWORKS Design Help](https://help.solidworks.com/2022/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.isldworks~opendoc6.html)
92. [OpenDoc7 Method (ISldWorks) - 2020 - SOLIDWORKS Design Help](https://help.solidworks.com/2020/English/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html?format=P&value=)
93. [Getting Started with the SOLIDWORKS API SolidPractices](https://3dswym.3dexperience.3ds.com/wiki/solidworks-news-info/getting-started-with-the-solidworks-api-solidpractices_eLpSxUm2THqG6jwQdSrMGQ)
94. [Connect to SOLIDWORKS Document Manager Application from API](https://www.codestack.net/solidworks-document-manager-api/getting-started/create-connection/)
95. [Office versions and connectivity to Microsoft 365 services - Microsoft 365 Apps](https://learn.microsoft.com/en-us/microsoft-365-apps/end-of-support/microsoft-365-services-connectivity)
96. [New Outlook vs Classic Outlook: Which to Use in 2026](https://wincdkey.com/new-outlook-vs-classic-outlook/)
97. [@saadeh/xlsx - npm](https://www.npmjs.com/package/@saadeh/xlsx)
98. [Newer functions (XLOOKUP, IFS, TEXTJOIN, FILTER, SORT, ...) are written without the \`\_xlfn.\` prefix, so they compute \`#NAME?\` · Issue #597 · productdevbook/hucre · GitHub](https://github.com/productdevbook/hucre/issues/597)
99. [Classic Sunset Officially at 2026.1 - Kinetic ERP - Epicor User Help Forum](https://www.epiusers.help/t/classic-sunset-officially-at-2026-1/120789)
100. [Getting Started - 2022 - SOLIDWORKS API Help](https://help.solidworks.com/2022/English/api/swdocmgrapi/GettingStarted-swdocmgrapi.html?id=94a88a3c04b346099c46fbd1d8689824)

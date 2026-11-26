# Intake, wave 3: the old Office, Epicor and SOLIDWORKS skills

Filed 2026-11-26. The rebuild plan's intake step for wave 3, in `ROADMAP.md`'s *Rebuilding the
owner's older skills*: for each old skill, what its successor covers, what was dropped and why,
and its defects, so none is repeated. Company detail is described, never quoted.

The old skills are the owner's claude.ai skills `vba-coding`, `excel-master` and `epicor-bpm`,
read whole from the synced copies in a Claude Code session on 2026-11-26. The owner asked that
every old skill a module replaces be read in full, and each topic rebuilt, dropped with a
reason, or flagged as company detail, so nothing useful is lost. The old `solidworks-automation`
wasn't among the synced copies, so its topics couldn't be checked. Nothing was copied from any
of them: none of their examples had been run and none of their facts had a source.

Their successors are `coding`'s `vba-coding` and `business-apps`' `excel-master`,
`epicor-kinetic` and `solidworks-automation`, written from primary sources with research run R16
as leads, each fact checked at its source that day. The owner's `my-theme`, whose palette is the
company's, was rebuilt the same day in the private companion, which records its intake.

No other skill on the owner's account depends on these. The old `excel-master` names the old
`vba-coding`, and the old `vba-coding` names the old `solidworks-automation`, so they are deleted
together.

## `vba-coding`

- **Covered:** `Option Explicit` with a type for each variable and `Long` over `Integer`; one
  `On Error GoTo` handler and one cleanup label per entry point, left by `Resume`; `On Error
  Resume Next` for one statement; re-raising with `Err.Raise` and `vbObjectError`; saving and
  restoring `ScreenUpdating`, `EnableEvents` and `Calculation`; arrays over cell loops, without
  `Select` or `Activate`; early and late binding; quitting an application started with
  `CreateObject`; why `Dim ... As New` never tests `Nothing`; `dbFailOnError` and parameters in
  Access; `.Display` before `.Send` in Outlook; finding the last row; the review checklist, as
  the Audit table; and its rule against bypassing macro security, as "never weaken it". New:
  64-bit `PtrSafe` and `LongPtr`, VBScript's removal and the built-in `RegExp`, Mark of the Web,
  trusted locations, ActiveX off by default, new Outlook, and when Office Scripts, Python in
  Excel or PowerShell fits better.
- **Dropped:**
  - naming conventions and Hungarian prefixes, for `code-style`; the module header template,
    which is git's job; the response templates, which `coding`'s contract covers;
  - Word find-and-replace, PDF export and mail merge, for `word-documents`; workbook building
    and the report-by-mail macro, for `excel-master`;
  - the inbox loop, mail helpers and HTTP calls: too much for one module, and new Outlook moves
    mail to Microsoft Graph;
  - the `ProgID` list, `CallByName` and the constants table: reference, not rules;
  - ADO helpers, keeping the DAO path, for the planned `data` skill;
  - `ScriptControl` and `InternetExplorer.Application`, whose limits weren't sourced;
  - the error-code table and retries, for `error-handling`; circular references and event
    leaks, cut for size;
  - its pointer to the SOLIDWORKS skill, now `solidworks-automation`'s.
- **Defects not to repeat:**
  - `Dim i, j, k As Long` called correct: only `k` is `Long`;
  - `Sleep` declared with a `LongPtr` argument, which is a 32-bit `DWORD`;
  - "exponential" back-off that grew linearly;
  - `On Error GoTo CleanExit`, which swallows the error, and an error in cleanup escapes;
  - handlers that return `1` or "Error: 404" as data;
  - settings forced to `True` and automatic, not restored to their saved values;
  - SQL built by joining strings, open to injection and broken by a decimal comma, and a
    rollback run when no transaction began;
  - `Dim rs As New ADODB.Recordset`;
  - a "leak fix" that set a local copy to `Nothing`, `DoEvents` said to collect garbage, and
    `Erase` and reverse-order `Nothing` sold as memory fixes;
  - VBScript's `RegExp` and `ScriptControl` recommended without warning of VBScript's removal;
  - a mail merge saving file names straight from cells, with no handler to quit Word;
  - a report sent with `.Send` and no error handling, against its own rule;
  - a log written to `ThisWorkbook.Path`, empty for an unsaved workbook.
- **Company detail:** none.

## `excel-master`

- **Covered:** choosing openpyxl, XlsxWriter, python-calamine or pandas, with versions; what an
  openpyxl save drops; formulas from code: English names, the `_xlfn.`, `_xlfn._xlws.` and
  `_xlpm.` prefixes, spilling formulas and cached values; never saving a workbook loaded with
  `data_only=True`; recalculating and scanning for errors, rebuilt to check a copy with a
  throwaway LibreOffice profile; list validation and its limits; tables, names and structured
  references; number formats, dates and time zones; large files; checking the output. New:
  formula injection, which its template-fill recipe was open to.
- **Dropped:**
  - workbook architecture, hand-written formulas (`GROUPBY`, `PIVOTBY`, `LAMBDA`, `REGEX`, Python
    in Excel), check cells, circular references and formula tuning, for the planned
    `excel-modeling`;
  - dashboards, chart choice, palettes, sparklines and its house defaults for fonts and header
    fills, for `visual-design`'s `data-visualization` and `visual-theme`;
  - Power Query and DAX, for the planned `power-query-and-dax`;
  - Office Scripts, the Office JavaScript API and Microsoft Graph's Excel API, for the planned
    `office-scripts-and-add-ins`;
  - its VBA delivery template, `vbaProject.bin` injection, form against ActiveX controls and
    macro security, for `vba-coding`;
  - SQL Server and REST integration, for the planned `data` and `api-patterns`; its Epicor
    integration, for `epicor-kinetic`;
  - sheet protection, cut for space, and its source page was gone that day: for
    `excel-modeling`;
  - the package's file layout and repair, left to Anthropic's `xlsx`, which ships pack, unpack
    and validate tools;
  - reports, consolidation, PDF export, pandas cleaning and CSV encodings: general Python work;
  - `.xlsm` and `keep_vba`, the 32,767-character cell limit and characters that openpyxl
    refuses: cut for space, a gap to fill;
  - its `scripts/office/` tree, copied from Anthropic's document skills without their notice;
  - `fix_xlfn_case.py`, which treats a symptom whose cause it gets wrong.
- **How it divides from Anthropic's `xlsx`,** which stays on the account by the owner's decision:
  `xlsx` keeps the openpyxl-only path, avoids dynamic arrays, and covers financial-model
  conventions, merged cells, `keep_vba` and charts; `excel-master` adds XlsxWriter, the
  prefixes, real dynamic arrays, injection, validation limits, dates and large files.
- **Defects not to repeat:**
  - it blamed openpyxl for lower-case `_xlfn.` names; openpyxl 3.1.5 keeps the case, and
    LibreOffice 24.2 lowercased the functions it didn't know when it saved, so its "safe save
    pipeline" delivered a file LibreOffice rewrote;
  - `fix_xlfn_case.py` used a wrong prefix for `SORTBY`, missed defined names, validation and
    conditional formats, and lacked newer functions;
  - `recalc.py` wrote a macro into the user's own LibreOffice profile, and matched error text
    anywhere in any cell;
  - it recommended openpyxl for `FILTER`, `SORT` and `UNIQUE`, which then don't spill;
  - no `_xlpm.`, so `LET` and `LAMBDA` from code break;
  - `pd.read_excel(..., chunksize=...)`, a parameter that doesn't exist;
  - an Office Scripts example using the add-in API's `.load()`;
  - a template fill that turned any value starting with `=` into a formula;
  - realistic fake passwords in protection examples;
  - an outdated XlsxWriter version, and no fact with a source.
- **Company detail:** its integration reference had REST examples whose query names look like
  one company's reports, table joins from the ERP, and an internal-style server placeholder; its
  macro reference named the ERP and CAD systems the organization uses. None was carried over.

## `epicor-bpm`

The roadmap also sends the Epicor material of the old `api-patterns` and `sql-craftsman` here.
Neither is among the synced copies any more, so none of it was read.

- **Covered:** method, data and updatable BAQ directives and when to use each, with Functions
  and Application Studio as the other homes for logic; when code runs, from a source rather than
  its diagram; validating in pre-processing and following up in post-processing; narrowing a
  directive by its conditions before writing code, and moving long code into Functions; custom
  code: `ds` and `tt` tables, row state, null checks, `Ice.BLException`, `Db` queries filtered by
  company, business-object calls, and guarding against a directive calling itself; its LINQ
  patterns, rewritten for EF Core; "use transactions" as "write through business objects"; its
  compile-error troubleshooting, as upgrade checks and the Audit table. New: REST API v2, which
  it had put out of scope.
- **Dropped:**
  - the full catalogs of conditions and actions, menu paths, designer clicks and the security
    rights table: no public source, since Epicor's help is for customers only;
  - the Task Agent interval for asynchronous actions: no source;
  - trace setup, `web.config` debugging and the global switch for directives: on-premises
    server administration with customer-only sources, and the switch doesn't exist in the cloud;
  - general C# advice, for `csharp-coding`;
  - mail through the server's mailer, files on a network share and its dataset holder: no
    public source, and shares don't exist in Epicor's cloud;
  - its output format, which was presentation.
- **Defects not to repeat:**
  - an old Entity Framework namespace for `SqlFunctions`, wrong even for 10.2's EF6; on 2026.1
    neither `SqlFunctions` nor `DbFunctions` exists;
  - direct database updates with update locks and a legacy field, skipping business-object
    validation and other directives;
  - `tt` tables shown as current in method directives, which have only `ds` in Kinetic;
  - string-comparison overloads and defaulted `FirstOrDefault` in queries, which EF Core can't
    translate;
  - a re-entry guard on a shared call-context field that other directives also use;
  - an `Ice.BLException` overload that couldn't be confirmed;
  - nothing on .NET 6 in 2022.1, EF Core in 2026.1 or the Smart Client's end;
  - placeholder addresses and paths that break this repository's rules;
  - no source for any compatibility claim.
- **Company detail:** it targets the one ERP 10.2 update the company runs, and its examples use
  a part-number prefix and product group that may be the company's own numbering. Both go to
  the private companion's planned `samscreen-epicor`; the numbering is to be confirmed first.

## `solidworks-automation`

- **Not available:** the old copy isn't among the synced copies, so its topics couldn't be
  checked. The only trace is the old `vba-coding`'s pointer to it.
- **The new module covers:** attaching from a macro, an add-in or a stand-alone program, and
  that a program-started session loads no add-ins; `OpenDoc6` and its error and warning flags;
  typed documents; custom properties at file and configuration scope; configurations and
  rebuilds; drawing views and sheets; SI units; flat patterns to DXF; STEP and PDF export; safe
  batch runs; releasing COM objects; obsolete members; the Document Manager key.
- **Left out:** the PDM API, which R16 didn't cover; STEP's protocol option values, unconfirmed
  at a primary source; the support lifecycle dates, whose page couldn't be read.
- **Found while building:** the help's C# syntax for `OpenDoc6` says `out` where its own samples
  pass `ref`; .NET Framework projects default to C# 7.3, where nullable annotations don't
  compile. The help's pages can't be read by a script, so their quotes are checked by hand
  (`docs/decisions.md`, 2026-11-26).

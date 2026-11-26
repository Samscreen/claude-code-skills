# VBA coding

Read this for writing, reviewing or fixing VBA in Excel, Word, Access or Outlook: errors and
cleanup, COM objects and binding, 64-bit `Declare`, speed, blocked macros, VBScript's removal, and
when another tool fits better.

Workbooks from code, formulas, Power Query, DAX, Office Scripts and add-ins are `business-apps`'
`excel-master`; Word templates, its `word-documents`; SOLIDWORKS macros, its
`solidworks-automation`; Epicor, its `epicor-kinetic`. Naming is `code-style`'s.

No example here has run on a named Office build yet: each was checked against Microsoft's
reference, and the owner runs each once and records the build and date here.

## Rules

1. **`Option Explicit` atop every module,** and an `As` type for each variable (facts
   `vba-option-explicit`, `vba-dim`). `Long` for counts and rows: `Integer` stops at 32,767.
2. **Each entry point has one handler and one cleanup label.** `On Error GoTo Failed`; the
   handler reports what failed and leaves by `Resume Cleanup`; cleanup restores state and quits
   what the macro started (fact `vba-on-error`).
3. **A helper passes errors up.** Without a handler the error reaches the caller's. One that
   adds context saves `Err.Number` and `Err.Description` first, then calls `Err.Raise`,
   its own errors numbered from `vbObjectError`. Never return a default or an "Error:" string.
4. **`On Error Resume Next` covers one statement:** test `Err.Number` on the next line, then
   `On Error GoTo 0` or back to the handler.
5. **Save each `Application` setting you change and restore the saved value** (fact
   `vba-excel-perf`): `ScreenUpdating`, `EnableEvents`, `Calculation`.
6. **Move cells as arrays, not cell by cell:** read `.Value2` into a `Variant`, change it, write it
   back once. No `Select` or `Activate`.
7. **Quit what you start.** A Word or Excel you created with `CreateObject` is closed and quit in
   cleanup, or it can stay running, hidden. A local object variable needs no `Set x = Nothing`.
8. **Late binding for code that runs on other machines** (`As Object`, `CreateObject`, constants
   by value); early binding while writing it, for IntelliSense (fact `vba-binding`).
9. **64-bit: `PtrSafe` on every `Declare`, `LongPtr` only for handles and pointers** (facts
   `vba-64bit`, `vba-dword`): `Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal ms As Long)`,
   since a `DWORD` stays `Long`. `#If VBA7` matters only for Office 2007 and older.
10. **No VBScript:** no `.vbs`, `cscript` or `wscript` calls; `RegExp` is built in from Microsoft
    365 2508; use late binding where older builds remain (facts `vba-vbscript`, `vba-regexp`).
11. **Never weaken macro security to make code run.** A blocked file is unblocked, signed, or
    placed in a trusted location an admin controls (facts `vba-motw`, `vba-trusted-locations`).
    Code never edits Trust Center settings or security registry keys. Form controls or a
    UserForm, not ActiveX controls on a sheet (fact `vba-activex`).
12. **Access: `dbFailOnError` on every `Execute`, values as parameters** (fact `vba-dao-execute`).
13. **Outlook VBA runs in classic Outlook only** (facts `vba-new-outlook`, `vba-classic-outlook`).
    Show a message with `.Display` unless the person asked for unattended sending.

### An Excel entry point

<!-- example: unchecked, no VBA compiler in CI; checked against Microsoft's VBA reference, not yet run on a named Office build -->
```vba
Option Explicit

Public Sub UppercaseColumnA()
    Dim calcMode As XlCalculation, screenOn As Boolean, eventsOn As Boolean
    Dim ws As Worksheet, data As Variant, lastRow As Long, r As Long

    calcMode = Application.Calculation
    screenOn = Application.ScreenUpdating
    eventsOn = Application.EnableEvents
    On Error GoTo Failed
    Application.ScreenUpdating = False
    Application.EnableEvents = False
    Application.Calculation = xlCalculationManual

    Set ws = ThisWorkbook.Worksheets("Data")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    If lastRow < 2 Then GoTo Cleanup
    data = ws.Range("A1:A" & lastRow).Value2
    For r = 2 To UBound(data, 1)
        If Not IsError(data(r, 1)) Then data(r, 1) = UCase$(CStr(data(r, 1)))
    Next r
    ws.Range("A1:A" & lastRow).Value2 = data

Cleanup:
    Application.Calculation = calcMode
    Application.EnableEvents = eventsOn
    Application.ScreenUpdating = screenOn
    Exit Sub
Failed:
    MsgBox "UppercaseColumnA stopped: error " & Err.Number & ": " & Err.Description, vbCritical
    Resume Cleanup
End Sub
```

A one-cell range's `.Value2` is a single value, not an array, so the read includes the header.

### An Access update

<!-- example: unchecked, no VBA compiler in CI; checked against the DAO reference, not yet run on a named Office build -->
```vba
Public Sub CloseOrder(ByVal orderId As Long)
    Dim db As DAO.Database, qdf As DAO.QueryDef
    Set db = CurrentDb
    Set qdf = db.CreateQueryDef("", _
        "PARAMETERS pId Long; UPDATE Orders SET Status = 'Closed' WHERE OrderID = pId;")
    qdf.Parameters("pId").Value = orderId
    qdf.Execute dbFailOnError
    If qdf.RecordsAffected <> 1 Then
        Err.Raise vbObjectError + 1, "CloseOrder", "No order " & orderId & " to close"
    End If
End Sub
```

### Choosing another tool

- **Office Scripts** for Excel on the web and Power Automate flows; it reaches the workbook only,
  on an enterprise or education license (fact `vba-office-scripts`).
- **Python in Excel** for analysis in cells; it runs in Microsoft's cloud, without local files or
  network access (fact `vba-python-excel`).
- **PowerShell** for files, services and scheduled jobs outside Office.
- **VBA** for desktop tools that need events, COM, the file system or another Office app.

## Mistakes

- **`Dim i, j, k As Long`:** `i` and `j` are `Variant` (fact `vba-dim`).
- **`LongPtr` for every API argument,** such as `Sleep`'s: a `DWORD` is 32 bits, and a wrong size
  breaks a structure's layout (facts `vba-dword`, `vba-64bit`).
- **`On Error GoTo CleanExit`,** skipping a handler: the error is silent, and a second one in
  cleanup can't be handled there (fact `vba-on-error`).
- **A handler returning `1` or `"Error: 404"`** as if it were data. The caller can't tell.
- **Restoring `ScreenUpdating = True` and automatic calculation,** not the saved values.
- **`Set x = Nothing` in reverse order, `Erase` before exit, `DoEvents` "to collect garbage"**
  as a fix for leaks. Locals go at `End Sub`, and `DoEvents` yields to Windows. Quit apps, close
  recordsets and files, and clear module-level references instead.
- **`Dim x As New Thing`, then `If x Is Nothing`:** the test itself creates one, so it's never
  `Nothing` (fact `vba-dim`).
- **`CurrentDb.Execute` without `dbFailOnError`, or SQL built by `&`:** failures pass silently,
  and a quote in a value breaks the query (fact `vba-dao-execute`).
- **A reference to "Microsoft VBScript Regular Expressions 5.5":** it breaks when VBScript goes
  (fact `vba-regexp`).
- **"Enable all macros", a network trusted location, or Protected View off** as a fix (facts
  `vba-motw`, `vba-trusted-locations`).
- **`UsedRange.Rows.Count` as the last row:** wrong when the range doesn't start on row 1.
- **Outlook macros for new Outlook,** which runs no VBA (fact `vba-new-outlook`).

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Undeclared variables | A module without `Option Explicit` | `GAP` | Add it; declare each |
| Swallowed errors | `Resume Next` over a block; empty handler | `DRIFT` | Handler, or re-raise |
| State left changed | `ScreenUpdating`, `Calculation` set, not restored | `DRIFT` | Save, restore in cleanup |
| Orphaned apps | `CreateObject("Word.Application")` with no `Quit` | `GAP` | Quit in cleanup |
| 64-bit | `Declare` without `PtrSafe`; `Long` handle | `DRIFT` | `PtrSafe`, `LongPtr` (fact `vba-64bit`) |
| VBScript | `.vbs` calls, a VBScript reference | `DRIFT` | Built-in `RegExp` (fact `vba-regexp`) |
| Weakened security | Code or advice changing Trust Center or zones | `BLOCKER` | Sign or unblock (fact `vba-motw`) |
| ActiveX on sheets | `OLEObjects` controls | `DRIFT` | Form controls or UserForm (fact `vba-activex`) |
| Access writes | No `dbFailOnError`; SQL by `&` | `GAP` | Both (fact `vba-dao-execute`) |
| Missing reference | "MISSING:" in Tools, References | `DRIFT` | Late binding (fact `vba-binding`) |

## Why

**1 to 4. Declarations and errors.** Without `Option Explicit` a typo is a new `Variant`. With no
`On Error`, a user meets the debugger and settings stay changed; with `Resume Next` everywhere, a
failed step reports success. Leaving by `Resume` clears the error, so cleanup runs normally. The
cost: two labels per entry point. A central logger still needs each handler to call it.

**5 to 7. State and speed.** Each cell read is a call into Excel; one array transfer replaces
thousands (fact `vba-excel-perf`). Restoring saved values keeps a called macro from undoing its
caller's settings. A user watching progress may want a status bar message instead.

**8. Binding.** Early binding checks names when compiling and runs faster, but a reference
missing on another machine stops the project compiling (fact `vba-binding`). Late binding runs
on any version and costs IntelliSense and named constants; a `#Const` flag switches between
them. Code that never leaves one machine can stay early bound.

**9 and 10. 64-bit and VBScript.** Microsoft 365 installs 64-bit by default, where a `Declare`
without `PtrSafe` won't compile and a `Long` handle truncates (fact `vba-64bit`). VBScript leaves
Windows in phases, ending `.vbs` calls (fact `vba-vbscript`); the built-in `RegExp` needs build
2508, so mixed fleets keep late binding (fact `vba-regexp`). The cost: rewriting calls early.

**11. Macro security.** Macros are a common way in for malware, so Office blocks them in files
from the internet (fact `vba-motw`), and a trusted location skips every check (fact
`vba-trusted-locations`). Unblocking one known file or signing keeps the rest protected. The
cost: a certificate, or an admin's time.

**12 and 13. Access and Outlook.** DAO's `Execute` reports success when no row changed unless
`dbFailOnError` is set (fact `vba-dao-execute`). Classic Outlook is supported to at least 2029
(fact `vba-classic-outlook`); for new Outlook, use Microsoft Graph, Power Automate or an add-in.

## Facts

Checked 2026-11-26; each is named above.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `vba-option-explicit` | Undeclared means `Variant` | [Option Explicit](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/option-explicit-statement) | "all undeclared variables are of Variant type" | 2026-11-26 | 2027-11-26 |
| `vba-dim` | One `As` each; `New` creates on reference | [Dim](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/dim-statement) | "clause for each variable you declare" and "created on first reference to it" | 2026-11-26 | 2027-11-26 |
| `vba-on-error` | Handlers | [On Error](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/on-error-statement) | "error handler can't handle the error" and "vbObjectError constant" | 2026-11-26 | 2027-11-26 |
| `vba-excel-perf` | Arrays; restore settings | [Excel performance](https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-tips-for-optimizing-performance-obstructions) | "large blocks of data in a single operation" and "restore the functionality" | 2026-11-26 | 2027-11-26 |
| `vba-binding` | `Object` is late | [Object](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/object-data-type); [CreateObject](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/createobject-function) | "always late" and "early-bound variable can give better performance" | 2026-11-26 | 2027-11-26 |
| `vba-64bit` | 64-bit default; `LongPtr` | [64-bit VBA](https://learn.microsoft.com/en-us/office/vba/language/concepts/getting-started/64-bit-visual-basic-for-applications-overview) | "the default is the 64-bit version" and "Use LongPtr for pointers and handles" | 2026-11-26 | 2027-11-26 |
| `vba-dword` | `DWORD` is 32 bits | [Data types](https://learn.microsoft.com/en-us/windows/win32/winprog/windows-data-types) | "A 32-bit unsigned integer" | 2026-11-26 | 2027-11-26 |
| `vba-vbscript` | Phase 2 off by default; phase 3 removal | [VBA and VBScript](https://devblogs.microsoft.com/microsoft365dev/how-to-prepare-vba-projects-for-vbscript-deprecation/) | "VBScript FODs will be disabled by default" and "Calling .vbs scripts from VBA will no longer be supported" | 2026-11-26 | 2027-05-26 |
| `vba-regexp` | Built-in `RegExp` from 2508 | [VBA and VBScript](https://devblogs.microsoft.com/microsoft365dev/how-to-prepare-vba-projects-for-vbscript-deprecation/) | "RegExp classes are included in the VBA for Office" and "Late binding works on Office versions 2508" | 2026-11-26 | 2027-05-26 |
| `vba-motw` | Internet macros blocked | [Macros blocked](https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked) | "block macros in files from the internet" | 2026-11-26 | 2027-05-26 |
| `vba-trusted-locations` | Skip all checks | [Trusted Locations](https://learn.microsoft.com/en-us/microsoft-365-apps/security/trusted-locations) | "bypass all other security and policy checks" | 2026-11-26 | 2027-05-26 |
| `vba-activex` | ActiveX off by default | [Block ActiveX](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-active-x-controls) | "ActiveX defaults to Disable all controls without notification" | 2026-11-26 | 2027-05-26 |
| `vba-dao-execute` | `Execute` hides failures | [Execute (DAO)](https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/database-execute-method-dao) | "always use the dbFailOnError option" | 2026-11-26 | 2027-11-26 |
| `vba-new-outlook` | No VBA in new Outlook | [Alternatives](https://learn.microsoft.com/en-us/microsoft-365-apps/outlook/get-started/vba-alternatives) | "VBA and Macros aren't supported in new Outlook" | 2026-11-26 | 2027-05-26 |
| `vba-classic-outlook` | Classic supported to 2029 at least | [Migration stages](https://learn.microsoft.com/en-us/microsoft-365-apps/outlook/get-started/guide-product-availability) | "will continue to be supported until at least 2029" | 2026-11-26 | 2027-05-26 |
| `vba-office-scripts` | Workbook only; license | [Scripts and VBA](https://learn.microsoft.com/en-us/office/dev/scripts/resources/vba-differences) | "only have access to the workbook" and "enterprise or educational license" | 2026-11-26 | 2027-05-26 |
| `vba-python-excel` | Cloud, no network | [Python in Excel](https://support.microsoft.com/en-us/office/introduction-to-python-in-excel-55643c2e-ff56-4168-b1ce-9428c8308545); [Data security](https://support.microsoft.com/en-us/office/data-security-and-python-in-excel-33cc88a4-4a87-485e-9ff9-f35958278327) | "run in the Microsoft Cloud" and "doesn't have network access" | 2026-11-26 | 2027-05-26 |

## Sources

Quotes are short and attributed; no code was copied.

| Source | Used for | License |
|---|---|---|
| [Office VBA reference](https://learn.microsoft.com/en-us/office/vba/api/overview/) | VBA, Excel, DAO | Docs CC BY 4.0, code MIT (VBA-Docs): short quotes |
| [Microsoft 365 Apps and Office dev docs](https://learn.microsoft.com/en-us/microsoft-365-apps/) | Security, Outlook, Scripts | Microsoft Learn terms: short quotes, own words |
| [Developer Blog](https://devblogs.microsoft.com/microsoft365dev/), [Support](https://support.microsoft.com/) | VBScript, Python in Excel | Microsoft terms: short quotes, own words |

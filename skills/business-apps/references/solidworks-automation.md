# SOLIDWORKS automation

Read this for code that drives SOLIDWORKS through its API: a VBA macro, a C# add-in or a
stand-alone program that opens documents, reads or writes custom properties and configurations,
walks drawing views, or exports flat patterns to DXF, STEP or PDF, for a file or a folder.

VBA itself is `coding`'s `vba-coding`, and C# its `csharp-coding`. A company's names and folders
belong in its own skills; the PDM API isn't covered. The examples are our own, written against the
2027 SP0 API help (fact `swa-help`). CI can't run SOLIDWORKS, and none is yet proven on a
SOLIDWORKS release.

## Rules

1. **Attach the way the code runs.** A macro uses `Application.SldWorks`; an add-in keeps the
   object `ConnectToSW` passes it. A stand-alone program calls `Marshal.GetActiveObject`, which is
   .NET Framework only (fact `swa-getactiveobject`). So target .NET Framework, which the interop
   assemblies are built on (fact `swa-help`), not `csharp-coding`'s `net10.0`. A session a program
   starts loads no add-ins (fact `swa-new-session`).
2. **Open with `OpenDoc6`, silent, and check both results.** Null means it failed; an assembly can
   open and still report `swFileNotFoundError` (fact `swa-opendoc6`). Add `ReadOnly` when nothing
   is saved.
3. **Keep the document `OpenDoc6` returns,** never `ActiveDoc`: a file already open in an assembly
   isn't activated (fact `swa-opendoc6`). Call `ActivateDoc3` where the active document is needed.
4. **Read errors and warnings as bitmasks,** and log each bit; not every bit is fatal (fact
   `swa-return-codes`).
5. **Branch on `GetType`, then cast** to `PartDoc`, `AssemblyDoc` or `DrawingDoc`.
6. **Name each property's scope.** `Extension.CustomPropertyManager("")` is the file's; a
   configuration's name gives that configuration's (fact `swa-prop-scope`). Read with `Get6` and
   `UseCached` false; write with `Add3` and `swCustomPropertyReplaceValue` (fact
   `swa-prop-readwrite`).
7. **Rebuild after `ShowConfiguration2`,** and switch back when done.
8. **In a drawing, skip the sheet:** `GetFirstView` returns it, and the views start at its
   `GetNextView` (fact `swa-first-view`).
9. **Convert at the edge:** the API speaks meters and radians (fact `swa-units`).
10. **Name the flat-pattern bits:** geometry 1, bend lines 4 (fact `swa-flat-pattern`).
    `ExportToDWG2` needs the active part, and a multibody part its flat patterns selected.
11. **Save STEP and PDF with `Extension.SaveAs3`,** whose extension picks the format. STEP needs
    the active document and a cleared selection; `IExportPdfData` picks a drawing's sheets. It
    overwrites (fact `swa-saveas3`). The STEP protocol, `swStepAP`, is a user option: restore it.
12. **Batch safely.** Show the list first; open each file read-only, with an error handler that
    logs and moves on; close it with `CloseDoc`, which discards changes (fact `swa-closedoc`);
    write to an output folder.
13. **Release what you own:** each file's objects, after closing it. Never release the `ISldWorks`
    an add-in was given, since that breaks its other holders (fact `swa-releasecom`).
14. **Avoid members the help marks obsolete,** such as `OpenDoc` (fact `swa-obsolete`).

### A folder of sheet-metal parts to DXF

<!-- example: unchecked, needs SOLIDWORKS, which CI can't run; not yet proven on a SOLIDWORKS release -->
```vba
Option Explicit
Const SOURCE_DIR As String = "C:\CHANGEME\parts\"
Const OUTPUT_DIR As String = "C:\CHANGEME\dxf\"
Const FLAT_GEOMETRY As Long = 1   ' bit 1
Const BEND_LINES As Long = 4      ' bit 3

Sub main()
    Dim swApp As SldWorks.SldWorks, files As New Collection, found As String, item As Variant
    Set swApp = Application.SldWorks
    found = Dir(SOURCE_DIR & "*.sldprt")
    Do While Len(found) > 0
        files.Add found
        found = Dir()
    Loop
    For Each item In files
        Debug.Print item & ": " & ExportOne(swApp, CStr(item))
    Next item
End Sub

Private Function ExportOne(swApp As SldWorks.SldWorks, fileName As String) As String
    Dim swModel As SldWorks.ModelDoc2, swPart As SldWorks.PartDoc
    Dim errs As Long, warns As Long, zeros(11) As Double, alignment As Variant
    alignment = zeros   ' twelve zeros: the default orientation
    On Error GoTo Failed
    Set swModel = swApp.OpenDoc6(SOURCE_DIR & fileName, swDocPART, _
        swOpenDocOptions_Silent Or swOpenDocOptions_ReadOnly, "", errs, warns)
    If swModel Is Nothing Then
        ExportOne = "not opened, errors " & errs
        Exit Function
    End If
    swApp.ActivateDoc3 swModel.GetTitle, False, swDontRebuildActiveDoc, errs
    Set swPart = swModel
    If swPart.ExportToDWG2(OUTPUT_DIR & Left$(fileName, InStrRev(fileName, ".")) & "dxf", _
            swModel.GetPathName, swExportToDWG_ExportSheetMetal, True, alignment, _
            False, False, FLAT_GEOMETRY Or BEND_LINES, Null) Then
        ExportOne = "exported, warnings " & warns
    Else
        ExportOne = "not exported: not sheet metal, or the export failed"
    End If
    swApp.CloseDoc swModel.GetTitle
    Exit Function
Failed:
    ExportOne = "failed: " & Err.Description
    If Not swModel Is Nothing Then swApp.CloseDoc swModel.GetTitle
End Function
```

### A property from a stand-alone program

<!-- example: unchecked, needs the SOLIDWORKS interop assemblies and a running SOLIDWORKS; not yet proven on a SOLIDWORKS release -->
```csharp
using System;
using System.Runtime.InteropServices;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;

internal static class ReadProperty   // .NET Framework; arguments: <file> <property>
{
    private static int Main(string[] args)
    {
        var swApp = (ISldWorks)Marshal.GetActiveObject("SldWorks.Application");
        int errors = 0, warnings = 0;
        const int options = (int)(swOpenDocOptions_e.swOpenDocOptions_Silent
            | swOpenDocOptions_e.swOpenDocOptions_ReadOnly);
        var model = (ModelDoc2)swApp.OpenDoc6(args[0], (int)swDocumentTypes_e.swDocPART,
            options, "", ref errors, ref warnings);
        if (model == null) { Console.Error.WriteLine($"Not opened: errors {errors}"); return 1; }
        CustomPropertyManager props = null;   // C# 7.3, .NET Framework's default
        try
        {
            props = model.Extension.get_CustomPropertyManager("");
            int result = props.Get6(args[1], false, out _, out string resolved, out _, out _);
            bool absent = result == (int)swCustomInfoGetResult_e.swCustomInfoGetResult_NotPresent;
            Console.WriteLine(absent ? "not present" : resolved);
            return 0;
        }
        finally
        {
            swApp.CloseDoc(model.GetTitle());
            if (props != null) Marshal.ReleaseComObject(props);
            Marshal.ReleaseComObject(model);
        }
    }
}
```

## Mistakes

- **Taking a non-null `OpenDoc6` as success,** or reading `ActiveDoc` after it.
- **`Add3` with `swCustomPropertyOnlyIfNew`,** or 0 typed for it: an existing value stays (fact
  `swa-prop-readwrite`).
- **Millimeters into the API.** A 25 mm plate becomes 25 m; convert at the edge.
- **A bare number for sheet-metal options,** such as 13 from a sample, which adds sketches.
- **Writing output beside its input,** where a name clash overwrites a file (fact `swa-saveas3`).
- **Trusting the help's C# syntax lines.** `OpenDoc6`'s says `out`; its C# samples pass `ref`.
- **A Document Manager key in shipped code.** It's for subscription customers, renewed each major
  release, and not to be shared (fact `swa-dm-key`).

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Results read | `Errors` unread after `OpenDoc6`, `SaveAs3` or `ExportToDWG2` | `GAP` | Check the return and each bit |
| Sources safe | A save to a source path | `BLOCKER` | Read-only opens, `CloseDoc`, an output folder |
| Batch survives | One file's failure ends the run | `GAP` | An error handler per file |
| Units | Millimeters or degrees passed in | `BLOCKER` | Meters and radians |
| Property scope | A configuration's name for a file's property, or the reverse | `GAP` | `""` for the file |
| Key | A Document Manager key in source | `BLOCKER` | The user's configuration |

## Why

### Attach to the user's session

- **The advice:** attach to the running SOLIDWORKS; start one only for an unattended batch.
- **The reason:** a started session loads no add-ins (fact `swa-new-session`), so their work on
  the files is missing.
- **What others do, and why:** some start several sessions, found by process ID, to work in
  parallel.
- **What it costs:** attaching needs SOLIDWORKS running; starting one costs a start-up and a
  `LoadAddIn` for each add-in.
- **When to choose differently:** a server batch with no user starts its own and closes it.

### Read-only, one file at a time, to its own folder

- **The advice:** list the files, open each read-only, close it unsaved, write output elsewhere.
- **The reason:** `SaveAs3` overwrites (fact `swa-saveas3`) and `CloseDoc` discards changes (fact
  `swa-closedoc`), so a run can't damage its sources and a failure costs one file.
- **What others do, and why:** the Document Manager API reads properties without SOLIDWORKS, for
  a subscription key (fact `swa-dm-key`).
- **What it costs:** an open and a close for each file.
- **When to choose differently:** a run meant to change files saves in place, after a backup and a
  trial on copies.

### Release only what you own

- **The advice:** release each file's objects after closing it; leave shared ones alone.
- **The reason:** Microsoft advises releasing only when required: releasing a shared object breaks
  its other holders (fact `swa-releasecom`).
- **What others do, and why:** some leave it to the garbage collector and restart SOLIDWORKS.
- **What it costs:** a `finally` per file; using a released object fails.
- **When to choose differently:** a short macro needs only `Set ... = Nothing`.

## Facts

Versions and behaviors, each named elsewhere in this module by its ID. Checked 2026-11-26.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `swa-help` | The 2027 SP0 API help is out; the interops are built on .NET Framework | [Welcome](https://help.solidworks.com/2027/English/api/sldworksapiprogguide/Welcome.htm) | "API Help 2027 SP0" and "These interops were created using Microsoft .NET Framework." | 2026-11-26 | 2027-02-26 |
| `swa-obsolete` | `OpenDoc` is obsolete | [OpenDoc](https://help.solidworks.com/2027/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc.html) | "Obsolete. Superseded by ISldWorks::OpenDoc6" | 2026-11-26 | 2027-05-26 |
| `swa-getactiveobject` | `Marshal.GetActiveObject` is listed for .NET Framework alone | [Learn](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.marshal.getactiveobject) | "Obtains a running instance of the specified object from the running object table (ROT)." | 2026-11-26 | 2027-05-26 |
| `swa-new-session` | A session started from code loads no add-ins | [Overview](https://help.solidworks.com/2027/English/api/sldworksapiprogguide/GettingStarted/SolidWorks_API_Standalone_and_Add-in_Applications_Overview.htm) | "add-ins do not load even though Start Up is selected" | 2026-11-26 | 2027-05-26 |
| `swa-opendoc6` | An open can report a missing file; a file open elsewhere isn't activated | [OpenDoc6](https://help.solidworks.com/2027/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html) | "it still returns swFileLoadError_e.swFileNotFoundError in Errors" and "will not return a pointer to this document" | 2026-11-26 | 2027-05-26 |
| `swa-return-codes` | Load and save errors are bitmasks, not all fatal | [Load](https://help.solidworks.com/2027/English/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadError_e.html), [save](https://help.solidworks.com/2027/English/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileSaveError_e.html) | "File load errors. Bitmask" and "Not all of these return codes are fatal errors." | 2026-11-26 | 2027-05-26 |
| `swa-saveas3` | STEP needs the active document; `SaveAs3` overwrites | [SaveAs3](https://help.solidworks.com/2027/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.html) | "the document to convert must be the active document" and "Overwrites existing files unless they are read only." | 2026-11-26 | 2027-05-26 |
| `swa-prop-scope` | An empty configuration name gives the file's properties | [CustomPropertyManager](https://help.solidworks.com/2027/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html) | "set the configuration argument to an empty string" | 2026-11-26 | 2027-05-26 |
| `swa-prop-readwrite` | `Get6` needs `UseCached` false; `OnlyIfNew` keeps an existing value | [Get6](https://help.solidworks.com/2027/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get6.html), [options](https://help.solidworks.com/2027/English/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomPropertyAddOption_e.html) | "you should set UseCached to false" and "Add the custom property only if it is new" | 2026-11-26 | 2027-05-26 |
| `swa-first-view` | A drawing's first view is its sheet | [GetFirstView](https://help.solidworks.com/2027/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html) | "this method returns the current drawing sheet" | 2026-11-26 | 2027-05-26 |
| `swa-units` | The API uses meters and radians | [Units](https://help.solidworks.com/2027/English/api/sldworksapiprogguide/Overview/Units.htm) | "accepts or returns values as meters, radians" | 2026-11-26 | 2027-05-26 |
| `swa-flat-pattern` | Bits 1 and 3 are geometry and bend lines; the part is the active one; multibody needs a selection | [ExportToDWG2](https://help.solidworks.com/2027/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportToDWG2.html) | "Bit #1: 1 to export flat-pattern geometry" and "Bit #3: 1 to export bend lines" and "file name of the active part document" and "You must select multi-body sheet-metal features" | 2026-11-26 | 2027-05-26 |
| `swa-closedoc` | `CloseDoc` closes a modified document unsaved | [CloseDoc](https://help.solidworks.com/2027/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html) | "closes the document without saving it" | 2026-11-26 | 2027-05-26 |
| `swa-releasecom` | Release only when required; a shared object's other users break | [Learn](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.marshal.releasecomobject) | "only if it is absolutely required" and "the other will be broken" | 2026-11-26 | 2027-05-26 |
| `swa-dm-key` | The Document Manager key is for subscribers, renewed each major release, not to be shared | [Document Manager](https://help.solidworks.com/2027/English/api/swdocmgrapi/GettingStarted-swdocmgrapi.html) | "customers who are currently under subscription" and "when installing any new major release" and "distribute it with any software that you ship" | 2026-11-26 | 2027-05-26 |

## Sources

Every source, with its license and how this module uses it: quoted, adapted with a notice, or
stated in our own words with a link.

| Source | Used for | License |
|---|---|---|
| [SOLIDWORKS API Help](https://help.solidworks.com/2027/English/api/sldworksapiprogguide/Welcome.htm) | API members, enumerations, remarks | © Dassault Systèmes: our own words, short quotes, no sample copied |
| [.NET API reference](https://learn.microsoft.com/en-us/dotnet/api/) | `Marshal`'s methods | Microsoft terms: our own words, short quotes |

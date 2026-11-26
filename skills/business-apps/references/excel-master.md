# Excel workbooks from code

Read this for code that writes or reads `.xlsx` files: choosing openpyxl or XlsxWriter, formulas
written from code, cached values, data validation, tables and names, dates, large files, and
checking the output.

Python itself is `coding`'s `python-coding`; charts and colors are `visual-design`'s; VBA is
`coding`'s `vba-coding`. Formulas written by hand, Power Query, DAX, Office Scripts and add-ins
are outside this module.

## Rules

1. **Choose the library by the job.** XlsxWriter writes new files and can't read or edit them
   (fact `xl-xlsxwriter-write-only`). openpyxl reads and edits, with no release since 2024 (fact
   `xl-openpyxl`). For values alone, python-calamine is faster; name pandas' engine, since its
   default reader is changing (fact `xl-pandas-engine`).
2. **Before editing with openpyxl, look in the package for what it drops:** shapes and text
   boxes, `<xdr:sp` in `xl/drawings/` (fact `xl-openpyxl-load`); sparklines, `sparklineGroup` in
   a sheet; and spill metadata, `xl/metadata.xml`. Edit such a file another way, or say what goes.
3. **Write formulas in English, with commas, and with the prefix Excel stores:** `_xlfn.`
   before a newer function, `_xlfn._xlws.` before `FILTER` and `SORT` (fact
   `xl-future-functions`), and `_xlpm.` before each `LET` and `LAMBDA` parameter (fact
   `xl-xlsxwriter-formulas`). Without them Excel shows `#NAME?`.
4. **Write a formula that spills with `write_dynamic_array_formula()`.** openpyxl can't write
   the metadata, so Excel shows the formula with `@` and one value (fact
   `xl-implicit-intersection`).
5. **Never trust a cached value the code wrote.** Neither library calculates: XlsxWriter stores 0
   (fact `xl-xlsxwriter-formulas`), openpyxl nothing. pandas, previews and PDF converters show
   that.
6. **Never save a workbook loaded with `data_only=True`.** It holds the values Excel last stored
   (fact `xl-openpyxl-load`), so every formula becomes a constant.
7. **Write outside text as text.** Both libraries turn a string starting with `=` into a formula
   (fact `xl-strings-to-formulas`): formula injection (fact `xl-csv-injection`). Pass
   `strings_to_formulas: False` or use `write_string()`; in openpyxl set `cell.data_type = "s"`.
8. **Keep a list validation's literal within 255 characters,** or point it at a named range
   (fact `xl-dv-255`). Validation stops typing only (fact `xl-dv-typed`), so check in code what
   code writes.
9. **Name tables and input cells, and use the names in formulas:** `Orders[Amount]` grows with
   its table where `B2:B100` doesn't. Table headers are unique, non-empty text.
10. **Write dates as `date` or `datetime` with a number format, never as strings.** Excel has no
    time zones (fact `xl-no-timezones`): convert to the reader's zone, drop `tzinfo`, and name
    the zone in the header.
11. **Keep numbers as numbers and identifiers as text.** Excel keeps 15 digits (fact
    `xl-limits`), so a longer serial number written as a number loses its tail.
12. **Stream large files** with XlsxWriter's `constant_memory`, row by row, or openpyxl's
    `read_only`, closed after use. A sheet holds 1,048,576 rows.
13. **Check the output:** recalculate a copy, list error values, bare function names and lost
    parts, and open it in Excel when in doubt.

### Writing with XlsxWriter

```python
import xlsxwriter


def write_orders(path, orders, statuses):
    """orders: rows of (order, placed, amount, status, note); placed is naive, in local time."""
    book = xlsxwriter.Workbook(
        path, {"strings_to_formulas": False, "default_date_format": "yyyy-mm-dd"}
    )
    lists = book.add_worksheet("Lists")
    lists.write_column("A1", statuses)
    book.define_name("Statuses", f"=Lists!$A$1:$A${len(statuses)}")

    sheet = book.add_worksheet("Orders")
    last = len(orders) + 1
    money = book.add_format({"num_format": "#,##0.00"})
    columns = [{"header": name} for name in ("Order", "Placed", "Amount", "Status", "Note")]
    columns[2]["format"] = money
    sheet.add_table(f"A1:E{last}", {"name": "Orders", "data": orders, "columns": columns})
    sheet.data_validation(f"D2:D{last}", {"validate": "list", "source": "=Statuses"})

    sheet.write_dynamic_array_formula("G2", "=SORT(UNIQUE(Orders[Status]))")
    sheet.write_formula("H2", "=_xlfn.LET(_xlpm.t,SUM(Orders[Amount]),ROUND(_xlpm.t,2))", money)
    book.close()
```

### Checking the output

```python
import re
import subprocess
import tempfile
from pathlib import Path

from openpyxl import load_workbook

ERRORS = {"#NAME?", "#REF!", "#VALUE!", "#DIV/0!", "#N/A", "#NUM!", "#NULL!", "#SPILL!", "#CALC!"}
NEWER = ["CONCAT", "FILTER", "IFS", "LAMBDA", "LET", "SORT", "SORTBY", "SWITCH", "TEXTJOIN",
         "UNIQUE", "XLOOKUP", "XMATCH"]
BARE = re.compile(r"(?<![\w.])(" + "|".join(NEWER) + r")\(", re.IGNORECASE)
RECALC_ON_LOAD = """<?xml version="1.0" encoding="UTF-8"?>
<oor:items xmlns:oor="http://openoffice.org/2001/registry">
<item oor:path="/org.openoffice.Office.Calc/Formula/Load">
<prop oor:name="OOXMLRecalcMode" oor:op="fuse"><value>0</value></prop></item>
</oor:items>
"""


def cells(book):
    for sheet in book.worksheets:
        for row in sheet.iter_rows():
            for cell in row:
                yield f"{sheet.title}!{cell.coordinate}", getattr(cell.value, "text", cell.value)


def bare_functions(path):
    """Stored formulas that name a newer function without its prefix."""
    return [(at, v) for at, v in cells(load_workbook(path))
            if isinstance(v, str) and v.startswith("=") and BARE.search(v)]


def errors_after_recalc(path):
    """Recalculate a copy in LibreOffice, with a throwaway profile, and list error cells."""
    with tempfile.TemporaryDirectory() as work:
        profile = Path(work, "profile")
        (profile / "user").mkdir(parents=True)
        (profile / "user" / "registrymodifications.xcu").write_text(RECALC_ON_LOAD)
        subprocess.run(
            ["soffice", f"-env:UserInstallation={profile.as_uri()}", "--headless",
             "--convert-to", "xlsx", "--outdir", work, str(path)],
            check=True, capture_output=True, timeout=300,
        )
        copy = load_workbook(Path(work, Path(path).stem + ".xlsx"), data_only=True)
        return [(at, v) for at, v in cells(copy) if v in ERRORS]
```

The profile makes LibreOffice recalculate on load; otherwise it may keep the stored results
(fact `xl-lo-recalc`), XlsxWriter's zeros. Ship the original, never the copy.

## Mistakes

- **Blaming openpyxl for lowercase `_xlfn.` names.** openpyxl 3.1.5 writes formulas as given.
  LibreOffice 24.2 lowercased the functions it didn't know, such as `XLOOKUP` and `LET`, when it
  saved, in a test on 2026-11-26. Never deliver a file LibreOffice saved.
- **Reading LibreOffice's `#NAME?` as a bug.** Version 24.2 lacked `XLOOKUP`, `FILTER`, `SORT`
  and `LET`. Check the prefixes, then confirm in Excel.
- **`write()` or `cell.value =` with text from a user, a CSV or an API.** A leading `=`, `+`,
  `-` or `@` can become a live formula.
- **A list validation of 60 joined items.** XlsxWriter warns and skips it; openpyxl saves it
  unchecked, past Excel's limit.
- **Writing `COPILOT()`.** It was withdrawn, and recalculates to `#NAME?` (fact `xl-copilot`).

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Error values | An error in a recalculated copy that Excel also shows | `BLOCKER` | Fix the formula or its inputs |
| Bare functions | `bare_functions()` finds any | `BLOCKER` | Add the prefix |
| Formula injection | Outside text written with `write()` or `cell.value` | `BLOCKER` | `write_string()` or `data_type = "s"` |
| Lost parts | Rule 2's markers in a file openpyxl will save | `GAP` | Edit another way, or say what goes |
| Spill metadata | A dynamic array formula without `cm=` in the sheet XML | `GAP` | `write_dynamic_array_formula()` |
| Validation | Each rule present; list literals within 255 characters | `GAP` | A named range as the source |
| Dates | Stored as numbers with a date format, none as text | `GAP` | `date` objects with a format |
| Versions pinned | openpyxl and XlsxWriter at exact versions | `GAP` | Pin them; rerun the checks on upgrade |

## Why

### Two libraries, each for its half

- **The advice:** XlsxWriter for files the code creates; openpyxl for files it reads or changes.
- **The reason:** XlsxWriter writes dynamic arrays, tables, validation and pivot tables, and is
  released often (fact `xl-xlsxwriter`). openpyxl alone edits, but loses what it doesn't model.
- **What others do, and why:** Anthropic's `xlsx` skill uses openpyxl for both and avoids
  dynamic array functions: one library, one recalculation path.
- **What it costs:** two APIs for one format.
- **When to choose differently:** a small file with no newer functions; or an edit Excel itself
  makes, through Office Scripts or COM, which keeps everything.

### The prefix Excel stores, not the name it shows

- **The advice:** write `_xlfn.`, `_xlfn._xlws.` and `_xlpm.` yourself, and check for bare names.
- **The reason:** Excel shows `XLOOKUP` and stores `_xlfn.XLOOKUP` (fact `xl-future-functions`).
  A bare name opens as `#NAME?` until someone enters the formula again.
- **What others do, and why:** XlsxWriter adds `_xlfn.` to dynamic array functions itself, and to
  the rest with `use_future_functions`, at a cost in speed. openpyxl writes what it's given.
- **What it costs:** a look at the specification's list, which may lag the newest functions.
- **When to choose differently:** never. When unsure, save the formula in Excel and read the XML.

### Cached values are not results

- **The advice:** a value a library wrote under a formula is unknown until something recalculates.
- **The reason:** a report read back with pandas showed every total as 0, XlsxWriter's stored
  result (fact `xl-xlsxwriter-formulas`). A withdrawn function keeps its old value until a
  recalculation (fact `xl-copilot`).
- **What others do, and why:** the `xlsx` skill recalculates with LibreOffice and copies the
  values back; XlsxWriter takes a known result in `write_formula()`'s `value`.
- **What it costs:** LibreOffice to install, and a function it lacks reads as an error.
- **When to choose differently:** a file only opened in Excel desktop, which recalculates on load.

## Facts

Versions, dates and defaults, each named elsewhere in this module by its ID. Checked 2026-11-26.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `xl-openpyxl` | openpyxl 3.1.5 (2024-06-28) is the latest, MIT | [PyPI](https://pypi.org/pypi/openpyxl/json) | "A Python library to read/write Excel 2010 xlsx/xlsm files" | 2026-11-26 | 2027-02-26 |
| `xl-xlsxwriter` | XlsxWriter 3.3.4 (2026-11-22) is the latest, BSD-2-Clause | [PyPI](https://pypi.org/pypi/xlsxwriter/json) | "A Python module for creating Excel XLSX files." | 2026-11-26 | 2027-02-26 |
| `xl-pandas-engine` | pandas 3.1 deprecates openpyxl as its default reader | [read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) | "the default engine will change from openpyxl to calamine" | 2026-11-26 | 2027-05-26 |
| `xl-xlsxwriter-write-only` | XlsxWriter can't read or edit a file | [FAQ](https://xlsxwriter.readthedocs.io/faq.html) | "It cannot read or modify an existing Excel file." | 2026-11-26 | 2027-05-26 |
| `xl-openpyxl-load` | openpyxl loses shapes; `data_only` reads stored values | [Tutorial](https://openpyxl.readthedocs.io/en/stable/tutorial.html) | "shapes will be lost" and "the value stored the last time Excel read the sheet" | 2026-11-26 | 2027-05-26 |
| `xl-future-functions` | [MS-XLSX] lists the `_xlfn.` and `_xlfn._xlws.` names | [MS-XLSX 2.2.3](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/5d1b6d44-6fc1-4ecd-8fef-0b27406cc2bf) | "the following future functions" and "_xlfn._xlws.FILTER" | 2026-11-26 | 2027-05-26 |
| `xl-xlsxwriter-formulas` | Formulas are stored in English; parameters take `_xlpm.`; XlsxWriter stores 0 as each result | [Formulas](https://xlsxwriter.readthedocs.io/working_with_formulas.html) | "US English version", "must have a" and "stores the value 0 as the formula result" | 2026-11-26 | 2027-05-26 |
| `xl-implicit-intersection` | Excel shows `@` where a formula returns one value | [Implicit intersection](https://support.microsoft.com/en-us/office/implicit-intersection-operator-ce3be07b-0101-4450-a24e-c1c999be2b34) | "you might notice @'s appear in some formulas" | 2026-11-26 | 2027-05-26 |
| `xl-strings-to-formulas` | XlsxWriter's `write()` makes formulas of strings by default | [Workbook](https://xlsxwriter.readthedocs.io/workbook.html) | "convert strings to formulas. The default is True." | 2026-11-26 | 2027-05-26 |
| `xl-csv-injection` | Cells starting with `=` run as formulas | [OWASP](https://owasp.org/www-community/attacks/CSV_Injection) | "will be interpreted by the software as a formula" | 2026-11-26 | 2027-05-26 |
| `xl-dv-255` | A list validation's literal holds 255 characters | [Data validation](https://xlsxwriter.readthedocs.io/working_with_data_validation.html) | "cannot exceed the Excel limit of 255 characters" | 2026-11-26 | 2027-05-26 |
| `xl-dv-typed` | Validation checks typed entries only | [More on data validation](https://support.microsoft.com/en-us/office/more-on-data-validation-f38dee73-9900-4ca6-9301-8a5f6e1f0c4c) | "only when users type data directly in a cell" | 2026-11-26 | 2027-05-26 |
| `xl-no-timezones` | Excel datetimes have no time zone | [Dates](https://xlsxwriter.readthedocs.io/working_with_dates_and_time.html) | "Excel doesn't support timezones in datetimes/times" | 2026-11-26 | 2027-05-26 |
| `xl-limits` | 1,048,576 rows; 15 digits of precision | [Limits](https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3) | "1,048,576 rows by 16,384 columns" and "Number precision 15 digits" | 2026-11-26 | 2027-05-26 |
| `xl-lo-recalc` | LibreOffice may skip recalculating on load | [Formula options](https://help.libreoffice.org/latest/en-US/text/shared/optionen/01060900.html) | "No formulas will be recalculated on loading the file." | 2026-11-26 | 2027-05-26 |
| `xl-copilot` | `COPILOT()` was withdrawn on 2026-09-14 | [COPILOT](https://support.microsoft.com/en-us/excel/functions/copilot-function) | "returns a #NAME? error because it's no longer recognized" | 2026-11-26 | 2027-05-26 |

## Sources

Every source, with its license and how this module uses it: quoted, adapted with a notice, or
stated in our own words with a link.

| Source | Used for | License |
|---|---|---|
| [XlsxWriter docs](https://xlsxwriter.readthedocs.io/) | Formulas, validation, dates | BSD-2-Clause: short quotes; examples our own |
| [openpyxl docs](https://openpyxl.readthedocs.io/) | Load options, lost shapes | MIT: short quotes |
| [pandas docs](https://pandas.pydata.org/docs/) | The reader engine | BSD-3-Clause: short quote |
| [MS-XLSX](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/) | Future functions | Microsoft Open Specifications: short quotes |
| [Microsoft Support](https://support.microsoft.com/) | Limits, validation, `@`, `COPILOT` | Microsoft terms: own words, short quotes |
| [OWASP](https://owasp.org/www-community/attacks/CSV_Injection) | Formula injection | CC BY-SA 4.0: short quote |
| [LibreOffice Help](https://help.libreoffice.org/) | Recalculation on load | MPL-2.0: short quote |
| [PyPI](https://pypi.org/) | Versions and licenses | Facts only |

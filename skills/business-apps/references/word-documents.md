# Word documents

Read this for code that fills a Word template or writes a `.docx`: opening a `.dotx`, replacing
its prompts, fields such as `DATE`, the table of contents, numbered lists, change records, and
checking the result.

Python itself is `coding`'s `python-coding`; Office theme colors are `visual-design`'s
`visual-theme`. A company's own template and approval rules belong in that company's own skills.

## Rules

1. **Start from the template and write a `.docx`.** Load a `.dotx` as a new document by changing
   its main part's content type, as Word does for File > New (facts `wd-dotx-refused`,
   `wd-create-from-template`). Renaming the file changes nothing.
2. **Inventory the template from the file before writing code,** and again when it changes:
   tables, prompt text, lists, fields and contents. A generator built from notes on one template
   failed silently on its successor.
3. **Reach every place text lives:** body, table cells, headers, footers, and content controls
   (`w:sdt`). `document.paragraphs` is the body alone.
4. **Replace across runs, never by run.** Word splits text into runs at formatting, spelling and
   revision marks, so join the runs, find the span, and edit only the runs it covers.
5. **Remove the template's own samples before writing:** example steps, sample rows, and history
   rows that describe the template rather than the document.
6. **Write every field's result yourself.** `updateFields` asks Word to recalculate on opening, and
   nothing else honors it (facts `wd-update-fields`, `wd-lo-index`). A preview or a PDF shows what
   the file holds.
7. **Never use `DATE`, `SAVEDATE` or `FILENAME` for a fact about the document,** such as its
   revision date or title. They show the day, the last save, the file's name (facts
   `wd-print-fields`, `wd-savedate`). Write text, or a `DOCPROPERTY` field with its result.
8. **Give each list that restarts its own `w:num`,** with a `startOverride`, and keep every
   `w:abstractNum` before the first `w:num` (facts `wd-start-override`, `wd-num-instance`,
   `wd-abstract-num`). Never type "1." or "a." as text.
9. **Append to a change record; never rewrite an earlier row.** A new revision starts from the
   previous revision's file and keeps its rows.
10. **Check the output by opening it,** not by trusting the code: no template prompt left, lists
    starting at 1 and a, the contents listing the real headings, alt text on images and a header
    row on tables (fact `wd-a11y`). Render it to PDF and look.
11. **Pin the library and its version.** python-docx's list helpers are internal (fact
    `wd-numbering-helpers`); docxtpl is LGPL (fact `wd-docxtpl`), so depend on it, don't copy it.

### Opening a template

```python
import io
import zipfile

from docx import Document

TEMPLATE = "application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml"
DOCUMENT = "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"


def open_template(path):
    """Open a .dotx as a new document, as Word's File > New does. Save the result as .docx."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(path) as source, zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as copy:
        for item in source.infolist():
            data = source.read(item.filename)
            if item.filename == "[Content_Types].xml":
                data = data.replace(TEMPLATE.encode(), DOCUMENT.encode())
            copy.writestr(item, data)
    buffer.seek(0)
    return Document(buffer)
```

### Replacing text across runs

```python
def replace_in_paragraph(paragraph, old, new):
    """Replace text Word split across runs, keeping the first run's formatting."""
    runs = paragraph.runs
    text = "".join(run.text for run in runs)
    start = text.find(old)
    if start < 0:
        return False
    end, position, first = start + len(old), 0, True
    for run in runs:
        run_start, run_end = position, position + len(run.text)
        position = run_end
        if run_end <= start or run_start >= end:
            continue
        before = run.text[: max(0, start - run_start)]
        after = run.text[max(0, end - run_start) :]
        run.text = before + (new if first else "") + after
        first = False
    return True
```

Walk tables cell by cell, and each section's header and footer, and call this on every paragraph.
`paragraph.runs` skips runs inside hyperlinks; text there needs the XML.

### Restarting a lettered list

```python
def restart_list(document, num_id, level=0):
    """A new instance of num_id's list, counting from 1 at level. Returns its numId."""
    numbering = document.part.numbering_part.element
    abstract_id = numbering.num_having_numId(num_id).abstractNumId.val
    instance = numbering.add_num(abstract_id)
    instance.add_lvlOverride(ilvl=level).add_startOverride(1)
    return instance.numId
```

Call it once per step, and set each sub-action's `w:numPr` to the new `numId` and its level. Leave
`ilvl` off a paragraph numbered by its style, such as Heading 1 (fact `wd-style-numpr`).

## Mistakes

- **`Document("template.dotx")`.** It raises `ValueError` (fact `wd-dotx-refused`). Load it with
  the content type changed.
- **Searching `run.text` for a prompt,** or setting `paragraph.text`. The first misses a prompt
  split across runs; the second drops the formatting.
- **Leaving a table of contents with the template's sample entries,** trusting `updateFields`. Word
  fixes it on opening; a PDF made without Word, an email preview and a document library show the
  samples (fact `wd-update-fields`).
- **Reusing one `numId` for every step's sub-list.** The letters continue from step to step, since
  paragraphs sharing a `num` share its count (fact `wd-num-instance`).
- **Appending a `w:abstractNum` after the `w:num` elements,** out of the schema's order.
- **A `DATE` field as the revision date,** or `FILENAME` as the title. One shows the day of
  printing (fact `wd-print-fields`), so an old revision looks current; the other, the file's name.
- **Rebuilding a revision from scratch,** so its change record holds only the newest row.
- **Inventing an approver, a revision number or a date** to fill an empty cell. Leave it empty and
  say so.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Template prompts left | The template's prompt text anywhere, content controls included | `BLOCKER` | Replace or delete each, checked against the template's inventory |
| Contents cached | Contents entries match the headings, as text in the file | `GAP` | Write the entries |
| Facts from fields | `DATE`, `SAVEDATE` or `FILENAME` where a fixed fact belongs | `GAP` | Text, or `DOCPROPERTY` with its result |
| Lists restart | Each step's sub-list starts at "a"; headings start at 1 | `GAP` | A `w:num` per list with `startOverride` |
| Change record kept | Earlier revisions' rows present and unchanged | `BLOCKER` | Start from the previous revision's file |
| Accessibility | Alt text on images; a header row on tables (`w:tblHeader`) | `GAP` | Add them in the generator (fact `wd-a11y`) |

## Why

### Write field results, don't wait for Word

- **The advice:** every field and the table of contents carry their real result in the file.
- **The reason:** `updateFields` asks the opening application to recalculate (fact
  `wd-update-fields`). Word does; LibreOffice's PDF conversion printed a generated document's
  cached contents, with step 7 on page 5 of 4, in a test on 2026-11-24. Previews do the same.
- **What others do, and why:** the `docx` package for JavaScript now writes contents entries from
  the headings. LibreOffice can update indexes through its API (fact `wd-lo-index`), at the cost
  of a script per conversion.
- **What it costs:** page numbers need a layout engine; without one, write the titles right and
  let Word correct the numbers.
- **When to choose differently:** a document only ever opened in Word can rely on `updateFields`.

### A new list instance per restart

- **The advice:** one `w:num` per list that counts from 1, pointing at the template's definition.
- **The reason:** a `num` is one counter shared by every paragraph that names it (fact
  `wd-num-instance`); `startOverride` sets where it begins (fact `wd-start-override`). Cycling a
  few `numId`s once made step 6 continue from step 1's "e.".
- **What others do, and why:** one multi-level list restarts a level after a higher one with
  `lvlRestart`; templates with separate heading and sub-lists need instances.
- **What it costs:** one `w:num` per step, which Word doesn't mind.
- **When to choose differently:** if the template's sub-list is level 1 of the heading's list,
  `lvlRestart` does it without code.

### Placeholders: prompts, content controls or document properties

- **The advice:** use the prompt text a template already has; design a new template with locked,
  tagged content controls, or `DOCPROPERTY` fields for values that repeat.
- **The reason:** content controls can be locked and mapped to a custom XML part (fact
  `wd-content-controls`). Prompt text is cheapest and leaves no structure behind.
- **What it costs:** python-docx has no API for content controls or fields, so the code works on
  the XML. The Open XML SDK for .NET has classes for both.
- **When to choose differently:** docxtpl's Jinja tags (fact `wd-docxtpl`) suit templates written
  for it, and an LGPL dependency.

### Document control

- **The advice:** append the new change record row; carry earlier rows unchanged; leave approval
  to the approver.
- **The reason:** ISO 9001's clause 7.5 covers identifying documented information and controlling
  its changes; whether each revision repeats every row is the organization's call. The 2026
  edition is current (fact `wd-iso-9001-2026`).
- **When to choose differently:** when a document system keeps the history outside the file.

## Facts

Versions, dates and defaults, each named elsewhere in this module by its ID. Checked 2026-11-24.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `wd-python-docx` | python-docx 1.2.0 (2025-06-16) is the latest, MIT | [PyPI](https://pypi.org/pypi/python-docx/json) | "Create, read, and update Microsoft Word .docx files." | 2026-11-24 | 2027-02-24 |
| `wd-dotx-refused` | python-docx 1.2.0 raises `ValueError` for any content type but a document's | [api.py at v1.2.0](https://raw.githubusercontent.com/python-openxml/python-docx/v1.2.0/src/docx/api.py) | "is not a Word file, content type is" | 2026-11-24 | 2027-05-24 |
| `wd-numbering-helpers` | python-docx's internal XML classes add list instances and start overrides | [numbering.py at v1.2.0](https://raw.githubusercontent.com/python-openxml/python-docx/v1.2.0/src/docx/oxml/numbering.py) | "def add_startOverride" | 2026-11-24 | 2027-05-24 |
| `wd-create-from-template` | The Open XML SDK's `CreateFromTemplate` attaches the template, as Word does | [CreateFromTemplate](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.packaging.wordprocessingdocument.createfromtemplate?view=openxml-3.0.0) | "The template will be attached to the WordprocessingDocument." | 2026-11-24 | 2027-05-24 |
| `wd-update-fields` | `updateFields` asks for recalculation on opening; without it, none | [UpdateFieldsOnOpen](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.updatefieldsonopen?view=openxml-3.0.1) | "should automatically have their field result recalculated" and "fields should not automatically be recalculated on opening" | 2026-11-24 | 2027-05-24 |
| `wd-print-fields` | `DATE` updates on printing or preview | [Some fields are updated](https://support.microsoft.com/en-us/topic/some-fields-are-updated-while-other-fields-are-not-eb3ad53a-328b-a3b4-91c6-28a84001855f) | "only updated when you print or preview your document" | 2026-11-24 | 2027-05-24 |
| `wd-savedate` | `SAVEDATE` shows the last save | [SaveDate field](https://support.microsoft.com/en-us/office/field-codes-savedate-field-3c2cd5ae-e6e2-4c27-b69c-7f5c029c8d7f) | "inserts the date and time a document was last saved" | 2026-11-24 | 2027-05-24 |
| `wd-lo-index` | LibreOffice updates an index through its API, not on conversion | [XDocumentIndex](https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XDocumentIndex.html) | "initiates an update to the document index." | 2026-11-24 | 2027-05-24 |
| `wd-start-override` | `startOverride` sets where a list instance's level begins | [StartOverrideNumberingValue](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.startoverridenumberingvalue?view=openxml-3.0.1) | "the number which the specified level override shall begin with" | 2026-11-24 | 2027-05-24 |
| `wd-num-instance` | One `num` is shared by every paragraph that names it | [NumberingInstance](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.numberinginstance?view=openxml-3.0.1) | "can be referenced by zero or more paragraphs" | 2026-11-24 | 2027-05-24 |
| `wd-abstract-num` | An `abstractNum` is reached only through a `num` | [AbstractNum](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.abstractnum?view=openxml-3.0.1) | "shall not be directly referenced by content" | 2026-11-24 | 2027-05-24 |
| `wd-style-numpr` | A style's numbering ignores `ilvl` | [NumberingProperties](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.numberingproperties?view=openxml-3.0.1) | "any numbering level defined using the ilvl element shall be ignored" | 2026-11-24 | 2027-05-24 |
| `wd-content-controls` | Content controls can be locked and mapped to a custom XML part | [Working with Content Controls](https://learn.microsoft.com/en-us/office/vba/word/concepts/working-with-word/working-with-content-controls) | "does not accidentally delete" and "custom XML part" | 2026-11-24 | 2027-05-24 |
| `wd-a11y` | Missing table headers are an error; heading styles a tip | [Accessibility Checker rules](https://support.microsoft.com/en-us/accessibility/office-accessibility/rules-for-the-accessibility-checker) | "Tables specify column header information." and "Documents use heading styles." | 2026-11-24 | 2027-05-24 |
| `wd-docxtpl` | docxtpl 0.20.2 is LGPL-2.1-only | [PyPI](https://pypi.org/pypi/docxtpl/json) | "LGPL-2.1-only" | 2026-11-24 | 2027-02-24 |
| `wd-iso-9001-2026` | ISO 9001:2026 was published on 2026-09-16 | [ISO/TC 176/SC 2](https://committee.iso.org/sites/tc176sc2/home/news.html) | "ISO 9001:2026 was published on 16 September 2026" | 2026-11-24 | 2027-05-24 |

## Sources

Every source, with its license and how this module uses it: quoted, adapted with a notice, or
stated in our own words with a link.

| Source | Used for | License |
|---|---|---|
| [python-docx](https://github.com/python-openxml/python-docx) | `.dotx` refusal, list helpers | MIT: short quotes; the examples are our own |
| [Open XML SDK reference](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml) | Templates, fields, numbering, with ISO/IEC 29500 excerpts | License not confirmed: our own words, short quotes |
| [Microsoft Support](https://support.microsoft.com/) | Field updates, Accessibility Checker | Microsoft terms: our own words, short quotes |
| [LibreOffice API](https://api.libreoffice.org/) | Index updates | License not confirmed: short quotes |
| [ISO/TC 176/SC 2](https://committee.iso.org/sites/tc176sc2/home/news.html) | ISO 9001:2026's publication | © ISO: facts only |
| [PyPI](https://pypi.org/) | Versions and licenses | Facts only |

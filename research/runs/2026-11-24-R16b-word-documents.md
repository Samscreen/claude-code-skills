# Verification: R16b (2026-11-24)

Checked by the receiving session on 2026-11-24, for the claims `word-documents` and the company's
procedure module rely on. Page quotes were searched for in each page's text, fetched that day.

| Claim | Status | Checked against |
|---|---|---|
| python-docx 1.2.0 is current (16 June 2025), MIT, Python 3.9 and later | verified | [PyPI JSON API](https://pypi.org/pypi/python-docx/json) |
| python-docx refuses a `.dotx`: `Document()` raises `ValueError` unless the main part's content type is the document one | verified in the source: `docx/api.py` lines 28-30 of 1.2.0 compare it with `CT.WML_DOCUMENT_MAIN` and raise "is not a Word file" | python-docx 1.2.0, installed from PyPI |
| python-docx has no API for content controls, fields or the table of contents | verified by reading 1.2.0's `docx/oxml`; **but it does have numbering helpers**, internal ones: `CT_Numbering.add_num()`, `CT_Num.add_lvlOverride()` and `CT_NumLvl.add_startOverride()`, which the report's library table misses | python-docx 1.2.0 `docx/oxml/numbering.py` |
| The Open XML SDK's `CreateFromTemplate` attaches the template by default, as Word does | verified: "The template will be attached to the WordprocessingDocument." and "this is also what happens when a document is created from a template" | [CreateFromTemplate](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.packaging.wordprocessingdocument.createfromtemplate?view=openxml-3.0.0) |
| DocumentFormat.OpenXml 3.5.1 is the latest stable, published 18 March 2026 | verified | [NuGet API](https://api.nuget.org/v3-flatcontainer/documentformat.openxml/index.json) |
| docxtpl 0.20.2 (13 November 2025) is LGPL-2.1-only; docxcompose 2.2.0 (2 June 2026) is MIT; `docx` on npm 9.16.0 (19 November 2026) is MIT | verified | PyPI JSON API for [docxtpl](https://pypi.org/pypi/docxtpl/json) and [docxcompose](https://pypi.org/pypi/docxcompose/json); [npm registry](https://registry.npmjs.org/docx) |
| `w:updateFields`: fields "should automatically have their field result recalculated", and without it "fields should not automatically be recalculated on opening" | verified | [UpdateFieldsOnOpen](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.updatefieldsonopen?view=openxml-3.0.1) |
| Word asks before updating fields when `updateFields` is set | not verified: the report's source is a GitHub issue (secondary) | — |
| `w:dirty`: results "shall be updated on open in a conforming consumer" | verified | [Dirty](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.dirty?view=openxml-3.0.1) |
| DATE is among the fields "only updated when you print or preview your document" | verified | [Some fields are updated while other fields are not](https://support.microsoft.com/en-us/topic/some-fields-are-updated-while-other-fields-are-not-eb3ad53a-328b-a3b4-91c6-28a84001855f) |
| SAVEDATE "inserts the date and time a document was last saved" | verified, on support.microsoft.com rather than the report's int.support.office.com copy of the same article | [Field codes: SaveDate field](https://support.microsoft.com/en-us/office/field-codes-savedate-field-3c2cd5ae-e6e2-4c27-b69c-7f5c029c8d7f) |
| LibreOffice's PDF conversion shows a table of contents' cached text and doesn't update it | verified by experiment: LibreOffice 24.2.7.2 converted a generated procedure on 2026-11-24 and printed the cached page numbers, wrong (step 7 on page 5 of 4) | this session's own test |
| LibreOffice: `XDocumentIndex.update()` "initiates an update to the document index", deprecated for `XRefreshable`; `TextFields` "makes it possible to refresh (recalculate etc.) all fields." | verified | [XDocumentIndex](https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XDocumentIndex.html), [TextFields](https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextFields.html) |
| Numbering: `startOverride` is "the number which the specified level override shall begin with" (the page also names `lvlRestart`); a `num` "can be referenced by zero or more paragraphs"; an `abstractNum` "shall not be directly referenced by content"; in a style's `numPr` "any numbering level defined using the ilvl element shall be ignored" | verified | Open XML SDK pages: [StartOverrideNumberingValue](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.startoverridenumberingvalue?view=openxml-3.0.1), [NumberingInstance](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.numberinginstance?view=openxml-3.0.1), [AbstractNum](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.abstractnum?view=openxml-3.0.1), [NumberingProperties](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.numberingproperties?view=openxml-3.0.1) |
| In `numbering.xml`, every `abstractNum` comes before the first `num` | **in part**: the Numbering page defers the content model to the schema in ISO/IEC 29500 §A.1, not read here; python-docx's model places `w:num` last, before only `w:numIdMacAtCleanup`; both company templates read on 2026-11-24 put every `abstractNum` first. The full order stays secondary | [Numbering](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.numbering?view=openxml-3.0.1); python-docx 1.2.0 |
| Content controls can be locked so a user "does not accidentally delete" them, and mapped to a "custom XML part" | verified | [Working with Content Controls](https://learn.microsoft.com/en-us/office/vba/word/concepts/working-with-word/working-with-content-controls) |
| Accessibility Checker: alt text and table header rows are errors; heading styles a tip | verified (the page writes "( alt text )") | [Rules for the Accessibility Checker](https://support.microsoft.com/en-us/accessibility/office-accessibility/rules-for-the-accessibility-checker) |
| ISO 9001:2026 was published on 16 September 2026 | verified: "ISO 9001:2026 was published on 16 September 2026" | [ISO/TC 176/SC 2 news](https://committee.iso.org/sites/tc176sc2/home/news.html) |
| ISO/TC 176/SC 2 N1286: documented information "has to be controlled in accordance with clause 7.5" | **unverifiable**: iso.org answers an automated fetch with a bot check | — |
| The wording of ISO 9001:2015 clauses 7.5.2 and 7.5.3 | **unverifiable**: the standard is sold, and the report's wording is a secondary paraphrase. Modules name the clauses and don't quote or paraphrase them as ISO's | — |
| Everything else in the report | not yet checked | checked when a module relies on it (`research/README.md`) |

---

RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R16b · FORM: research-result v1
Save as: R16b-RESULT.md
Receiving session: this is research the repository owner asked for. Check each claim against the source it cites before relying on it. File the report under research/runs/, update the Facts section of each module it names, and list what changed. If you lack context, the owner will attach a file whose first line starts HANDOFF-FOR: rmccann-hub/claude-code-skills.

# R16b: Filling a company Word template from code (word-documents module)

The safest way for an agent to fill the procedure template is this. Convert the `.dotx` to a `.docx` package first, because python-docx 1.2.0 rejects the template content type.\[1\] Then fill named content controls or `DOCPROPERTY` fields through the XML. Write real cached results for every field, including the table of contents, rather than relying on `w:updateFields`, because LibreOffice and previewers never recalculate a TOC.\[2\]\[3\]

## TL;DR

- **Templates:** python-docx 1.2.0 is still the current release (16 June 2025, no release since). It refuses a `.dotx` because it checks the main part's content type. The Open XML SDK has `WordprocessingDocument.CreateFromTemplate`, which builds a document from the template and attaches the template by default.
- **Fields and TOC:** `w:updateFields` asks a field-calculating application to recalculate fields when the file opens. LibreOffice does not fill a TOC from it, and `--convert-to` cannot update indexes; only a macro or a UNO call to `XDocumentIndex.update()` / `XRefreshable.refresh()` can. So a generator must write real TOC entries as the cached field result.
- **Document control:** in ISO 9001:2015, 7.5.2 asks for identification and description, a suitable format and review and approval. 7.5.3 includes control of changes such as version control. ISO does not say whether a change record must carry every earlier row; that is the organisation's decision. ISO 9001:2026 has been published: iso.org lists it as "Published (Edition 6, 2026)", and ISO says it was "Published on 16 September". The module should be checked against the 2026 edition.

## 1. Summary

1. python-docx is still at 1.2.0 (16 June 2025). The 1.2.0 changelog lists "Add support for comments"\[4\] and no content-control, field or TOC API.\[4\]\[5\] Forks (python-docx-ng 2.1.0, a "Skelmis" fork documenting 2.6.0) exist but are not the upstream package.\[6\]\[7\]
2. `docx.api.Document()` raises `ValueError` unless the main part's content type is `wordprocessingml.document.main+xml`, so a `.dotx` fails ("is not a Word file").\[1\]\[8\]\[9\]
3. The Open XML SDK's `CreateFromTemplate(path)` makes an editable document and attaches the template by default, "because this is also what happens" in Word.\[10\]
4. Open XML SDK current stable is 3.5.1 (18 March 2026); 3.4.1 shipped 6 January 2026.\[11\]\[12\]
5. `docx` on npm is very active: 9.16.0 was released 19 November 2026, and 9.15.0 (27 October 2026) added template-patching features.\[13\]\[14\]
6. docxtpl 0.20.2 (13 November 2025) is LGPL-2.1-only.\[15\] Check that licence before vendoring it into an Apache-2.0 repository.
7. docxcompose 2.2.0 (2 June 2026, MIT, Python ≥3.10) concatenates documents and handles custom document properties.\[16\]\[17\]
8. `w:updateFields` (§17.15.1.90): the spec says fields "should automatically have their field result recalculated"\[18\] on open. If it is omitted, fields are not recalculated.\[18\]
9. `w:dirty` on `w:fldChar` marks a field result as stale so a capable consumer recalculates it. The spec gives a TOC as the example.\[19\]
10. Microsoft lists DATE, PAGE, PAGEREF, PRINTDATE and REF among fields "only updated when you print or preview".\[20\]
11. LibreOffice cannot update a TOC during `--convert-to`. You need a macro (`.uno:UpdateAllIndexes` or `getDocumentIndexes()...update()`) and then a separate conversion.\[21\]\[22\]\[23\]
12. The `docx` npm maintainer reports that LibreOffice "never updates" a TOC field, "even with updateFields on". That is why `docx` now writes TOC entries from the headings.\[2\]
13. Numbering: a `w:num` points to one `w:abstractNum`, and a `w:lvlOverride/w:startOverride` inside a `w:num` changes the start for that instance.\[24\] The schema sequence in `numbering.xml` puts `abstractNum` before `num` (secondary confirmation only).\[25\]\[26\]
14. To link Heading 1 to numbering, the style's `w:numPr` holds only `numId`, and the `w:lvl` names the style with `w:pStyle`.\[24\]
15. Accessibility Checker errors that a generator must avoid are missing alt text and tables without a header row. Using heading styles is a Tip, not an error.\[27\]

## 2. Corrections

| # | What we believed | Verdict | Right fact | Source |
|---|---|---|---|---|
| C1 | `.dotx` differs from `.docx` only in the main part content type | **Incomplete** | The content type is the difference python-docx checks. A document created *from* a template in Word also carries an attached-template link: the Open XML SDK attaches the template by default because Word does. | learn.microsoft.com CreateFromTemplate page: "this is also what happens when a document is created from a template"\[10\] |
| C2 | python-docx refuses a `.dotx` until the content type is changed | **Confirmed** | `Document()` compares the content type with `CT.WML_DOCUMENT_MAIN` and raises `ValueError`.\[9\] | python-docx.readthedocs.io `docx.api` source\[1\] |
| C3 | python-docx has no API for `w:sdt`, fields or TOC | **Confirmed by absence** | The 1.2.0 changelog adds comments only.\[4\] No explicit statement from the maintainer was found. | data.safetycli.com changelog mirror (secondary) |
| C4 | A `numId` is one list instance with one counter; restart with a new `w:num` + `lvlOverride/startOverride` | **Confirmed, with nuance** | `startOverride` is the number the level override "shall begin with". It applies within one `num`, and a `num` "can be referenced by zero or more paragraphs".\[24\] | Open XML SDK StartOverrideNumberingValue and NumberingInstance pages |
| C5 | `updateFields` makes Word ask to update fields | **Confirmed (prompt from secondary)** | The spec says only "recalculated";\[18\] that Word shows a prompt is reported by `docx` users. | UpdateFieldsOnOpen page; dolanmiu/docx issue #1212\[28\] |
| C6 | LibreOffice ignores `updateFields`, including headless PDF | **Confirmed for the TOC; other fields not found** | The `docx` maintainer: LibreOffice "never updates it, even with updateFields on". Command-line conversion does not edit documents. | dolanmiu/docx PR #3590; ask.libreoffice.org (secondary)\[2\]\[23\] |
| C7 | DATE changes each time the document is opened | **Corrected** | Microsoft lists DATE among fields updated "when you print or preview". On open it shows its cached result until updated; whether Word refreshes it on open was not found in a primary source. Either way it is the wrong field for a revision date. | support.microsoft.com "Some fields are updated while other fields are not"\[20\] |
| C8 | CREATEDATE is right for a revision date | **Corrected** | CREATEDATE is the creation date, and it is reset by "Save As" (secondary). It is not a revision date. Use a `DOCPROPERTY` bound to a custom property, or plain text written by the generator. | addbalance.com (Charles Kenyon, secondary)\[29\] |
| C9 | SAVEDATE suits a revision date | **Corrected** | It shows the last save time ("Modified"), so any re-save changes it, even with no revision. It also does not change on save "until the field is later updated" (secondary). | support.office.com SaveDate; addbalance.com\[30\]\[31\] |
| C10 | A Word TOC sits in an `w:sdt` with `docPartObj` gallery "Table of Contents" | **Confirmed only from secondary** | OfficeIMO describes Word's TOC inside a "Table of Contents" content control. No primary Microsoft source was found. | EvotecIT/OfficeIMO issue #3650 (secondary)\[32\] |
| C11 | docxtpl is "the usual" Python library | **Not verifiable** | No neutral usage source was found. docxtpl is LGPL-2.1-only, which matters for an Apache-2.0 repository.\[15\] | libraries.io docxtpl |
| C12 | ISO 7.5.3 requires change control such as version control; 7.5.2 requires identification | **Confirmed, incomplete** | 7.5.2 also covers format/media and review and approval for suitability and adequacy. 7.5.3 also covers distribution, access, storage, retention and disposition, plus protecting evidence from unintended alteration. | ISO/TC 176/SC 2 N1286 (iso.org); qualityfieldguides.com (secondary paraphrase)\[33\]\[34\]\[35\] |
| C13 | ISO 9001:2015 is the current edition | **Out of date (confirmed)** | ISO 9001:2026 is published: iso.org lists it as "Published (Edition 6, 2026)", publication date 2026-09, ISO/TC 176/SC 2. ISO/TC 176/SC 2 news (28 Sep 2026) says it "was published on 16 September 2026". The 2015 edition is not obsolete at once: from 31 March 2028 new accredited certifications must be to the 2026 edition, and certified organisations "will have until 30 September 2029" to transition. | iso.org/standard/9001; ISO/TC 176/SC 2 committee news, 28 Sep 2026; ISO/TC 176 news, 23 Sep 2026 |

## 3. Facts table

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| F1 | python-docx current version | 1.2.0 | https://pypi.org/project/python-docx/ | "Released: Jun 16, 2025"\[5\] | read 24 Nov 2026 |
| F2 | python-docx licence / Python | MIT; Python ≥3.9 | https://pypi.org/project/python-docx/ | "MIT License (MIT)"\[5\] | read 24 Nov 2026 |
| F3 | python-docx rejects non-document content type | ValueError | https://python-docx.readthedocs.io/en/latest/_modules/docx/api.html | "file '%s' is not a Word file, content type is '%s'"\[36\] | read 24 Nov 2026\[1\] |
| F4 | 1.2.0 change | comments support | https://data.safetycli.com/packages/pypi/python-docx/changelog (secondary) | "Add support for comments" | read 24 Nov 2026 |
| F5 | Open XML SDK create from template | attaches by default | https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.packaging.wordprocessingdocument.createfromtemplate?view=openxml-3.0.0 | "The template will be attached to the WordprocessingDocument." | read 24 Nov 2026\[10\] |
| F6 | Open XML SDK current | 3.5.1 | https://www.nuget.org/packages/DocumentFormat.OpenXml/ | "3.5.1 … 3/18/2026"\[11\] | read 24 Nov 2026 |
| F7 | `updateFields` meaning | recalculate on open | https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.updatefieldsonopen?view=openxml-3.0.1 | "should automatically have their field result recalculated" | page updated 12 Jan 2024 |
| F8 | `updateFields` omitted | no recalculation | same | "fields should not automatically be recalculated on opening"\[18\] | 12 Jan 2024 |
| F9 | `w:dirty` | stale result flag | https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.dirty?view=openxml-3.0.1 | "results shall be updated on open in a conforming consumer" | read 24 Nov 2026\[37\] |
| F10 | `w:dirty` on fldChar, TOC example | spec rationale | https://webapp.docx4java.org/OnlineDemo/ecma376/WordML/fldChar.html (spec mirror, secondary host) | "flag the table of contents as dirty" | read 24 Nov 2026\[19\] |
| F11 | Fields updated on print | DATE, PAGE, PAGEREF, PRINTDATE, REF… | https://support.microsoft.com/en-us/topic/some-fields-are-updated-while-other-fields-are-not-eb3ad53a-328b-a3b4-91c6-28a84001855f | "only updated when you print or preview your document" | read 24 Nov 2026\[20\] |
| F12 | SAVEDATE | last save, from "Modified" | https://int.support.office.com/f1/topic-ssr/3c2cd5ae-e6e2-4c27-b69c-7f5c029c8d7f | "inserts the date and time a document was last saved" | read 24 Nov 2026\[31\] |
| F13 | CREATEDATE reset by Save As | secondary | https://www.addbalance.com/usersguide/fields.htm | "The date the document was created (or saved using Save As)" | read 24 Nov 2026\[29\] |
| F14 | LibreOffice and TOC fields | never updates | https://github.com/dolanmiu/docx/pull/3590 (secondary) | "LibreOffice never updates it, even with updateFields on" | read 24 Nov 2026\[2\] |
| F15 | LibreOffice index API | `update()` | https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XDocumentIndex.html | "initiates an update to the document index." | read 24 Nov 2026\[38\] |
| F16 | XDocumentIndex status | deprecated in favour of XRefreshable | same | "Use com::sun::star::util::XRefreshable … instead, if available." | read 24 Nov 2026\[38\] |
| F17 | LibreOffice text fields refresh | XRefreshable on TextFields | https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextFields.html | "makes it possible to refresh (recalculate etc.) all fields." | read 24 Nov 2026\[39\] |
| F18 | `--convert-to` does not edit | community answer | https://ask.libreoffice.org/t/update-toc-via-command-line/52518 (secondary) | "Command line does *not* edit documents" | read 24 Nov 2026\[23\] |
| F19 | startOverride | start number of override | https://learn.microsoft.com/dotnet/api/documentformat.openxml.wordprocessing.startoverridenumberingvalue?view=openxml-3.0.1 | "the number which the specified level override shall begin with"\[24\] | read 24 Nov 2026 |
| F20 | num shared by paragraphs | one instance, many paragraphs | https://learn.microsoft.com/dotnet/api/documentformat.openxml.wordprocessing.numberinginstance?view=openxml-3.0.1 | "can be referenced by zero or more paragraphs" | read 24 Nov 2026 |
| F21 | abstractNum not referenced directly | via num | https://learn.microsoft.com/dotnet/api/documentformat.openxml.wordprocessing.abstractnum?view=openxml-3.0.1 | "it shall not be directly referenced by content"\[40\] | read 24 Nov 2026 |
| F22 | numPr in a style ignores ilvl | uses lvl/pStyle | https://learn.microsoft.com/dotnet/api/documentformat.openxml.wordprocessing.numberingproperties?view=openxml-3.0.1 | "any numbering level defined using the ilvl element shall be ignored"\[24\] | read 24 Nov 2026 |
| F23 | Element order in numbering.xml | numPicBullet, abstractNum, num | https://github.com/Papyrine/OpenXmlHtml/pull/101 (secondary) | "w:numbering is a strict sequence"\[25\] | read 24 Nov 2026 |
| F24 | Accessibility: alt text | Error | https://support.microsoft.com/en-us/accessibility/office-accessibility/rules-for-the-accessibility-checker | "All non-text content has alternative text (alt text)."\[27\] | ms.date 17 Nov 2025 |
| F25 | Accessibility: table header | Error | same | "Tables specify column header information."\[27\] | 17 Nov 2025 |
| F26 | Accessibility: headings | Tip | same | "Documents use heading styles."\[27\] | 17 Nov 2025 |
| F27 | docxtpl current | 0.20.2, LGPL-2.1-only | https://libraries.io/pypi/docxtpl | "License: LGPL-2.1-only"\[15\] | read 24 Nov 2026 |
| F28 | docxcompose current | 2.2.0 | https://pydeps.com/project/docxcompose/ (secondary) | "uploaded on 2026-06-02" | read 24 Nov 2026\[17\] |
| F29 | docx (npm) current | 9.16.0 | https://github.com/dolanmiu/docx/releases/tag/9.16.0 | "released this 19 Nov"\[13\] | 19 Nov 2026 |
| F30 | ISO TC 176 guidance on documented info | N1286 | https://www.iso.org/files/live/sites/isoorg/files/standards/docs/en/iso_9001_2015_guidance_documented_information.pdf | "has to be controlled in accordance with clause 7.5" | read (snippet) 24 Nov 2026\[41\] |
| F31 | 7.5.2 identification examples | title, date, author, reference | https://qualityfieldguides.com/iso-9001/clause-7-5-documented-information/ (secondary) | "identified and described (title, date, author, reference)" | updated 26 Sep 2026\[35\] |

## 4. Findings

### Q1. Filling a company template from code

**Placeholders compared.**

- **Content controls (`w:sdt`).** Microsoft's VBA and Office docs say content controls can be locked so that a user "does not accidentally delete" them. They also say a control's contents can be mapped to "data in a custom XML part" (learn.microsoft.com, Working with Content Controls).\[42\] Binding is two-way: edits in the control are written back to the custom XML part (Visual Studio docs).\[43\]\[44\] For a template that code fills, this is the mechanism Microsoft documents most fully. No Microsoft page found says outright "use content controls for generated templates", so treat that as the best-documented option, not an explicit recommendation.
  - Cost to a generator: python-docx has no API for it, so you find `w:sdt` by `w:tag` or `w:alias` and replace `w:sdtContent`. Data binding needs a custom XML part plus `w:dataBinding` XPath.
  - Survives editing: yes, if locked ("contents cannot be deleted" / "cannot be edited").
- **`DOCPROPERTY` fields.** Use these for values that repeat, such as document number, revision and title in the header and footer. The generator sets the property in `docProps/custom.xml` and writes the cached result into every field. docxcompose has explicit support: "Add support for adding, setting and deleting of doc properties" (1.0.0).\[16\] Its 1.3.1 release also handles fields whose name is split across runs.\[45\]
  - Risk: a viewer shows the cached text, so the generator must update the cached result as well as the property.
- **Bookmarks.** These are fragile under editing: typing at a bookmark boundary can put text outside it. No primary source was found for that behaviour, so it is not found.
- **Placeholder text** (`{{name}}`, docxtpl Jinja tags). This is the cheapest to author. It is fragile because Word splits text across runs (see below), and once filled it leaves no structure behind for later edits.

**Recommendation for the procedure module:**

- Header table and footer values: `DOCPROPERTY` fields bound to custom properties, with cached results written by code.
- One-off fields: locked content controls with tags.
- Change-record rows and step lists: generate them in code, cloning a template row or paragraph.

**`.dotx` versus `.docx`.**

- The main part content type differs: `…wordprocessingml.template.main+xml` versus `…document.main+xml` (python-docx error text).\[9\]\[46\]\[47\]
- A document "based on" a template carries an attached-template relationship. The Open XML SDK `CreateFromTemplate(String)` "creates an editable WordprocessingDocument from a template" and attaches it. Attaching is the default "because this is also what happens when a document is created from a template … using Microsoft Word". `CreateFromTemplate(String, Boolean)` lets you choose not to attach.\[10\]
- python-docx has no equivalent. Rewrite the `[Content_Types].xml` override for `/word/document.xml` to the document content type before calling `Document()`.\[48\] Optionally add `w:attachedTemplate r:id` to `settings.xml` with an external relationship of type `…/relationships/attachedTemplate` (relationship type shown in the html2openxml wiki, secondary).\[49\]
- An absolute template path in that relationship leaks a file path and can make Word slow to open the file if the path is unreachable. No source was found for the slowness, so that part is not found.

**Text split across runs.**

- Word splits text into runs at formatting, proofing and revision boundaries. A string search on `run.text` therefore misses `{{name}}` stored as `{{`, `na`, `me}}`.
- Safe method: join the paragraph's run texts, find the match span, write the replacement into the first run of the span (which keeps that run's `w:rPr`), and empty the other runs in the span.
- docxcompose reports handling "complex fields with fieldname split into several runs" (1.3.1).\[45\]
- `docx` on npm 9.15.0 added `trimPlaceholders` for `{{ name }}`, and 9.15.1 patches placeholders "in links, content controls and tracked changes".\[14\]\[50\]

### Q2. Fields and the table of contents

- **`w:updateFields`** (settings, §17.15.1.90): fields "should automatically have their field result recalculated" by "an application which supports field calculations". Some fields (such as page numbers) are always recalculated. The setting must not override document or write protection.\[18\] In Word this shows a prompt, reported by `docx` users as "Do you want to update the fields in this document?" (dolanmiu/docx #1212, secondary). The `docx` project now advises leaving `updateFields` off when it can compute page numbers itself, because it "is what asks Word to update the fields".\[28\]
- **`w:dirty`** on `w:fldChar` marks a result as stale so it "should be updated before" display, "if this functionality is supported". The spec's own example is flagging the TOC dirty after adding a paragraph.\[19\]\[51\] Microsoft's SDK page for the run-level `w:dirty` element says results "shall be updated on open in a conforming consumer".\[37\] Whether Word prompts for `w:dirty` was not found.
- **Field behaviour:**

| Field | Shows | Updates | Source |
|---|---|---|---|
| DATE | current date | on print/preview and manual F9; DATE is in Microsoft's "print or preview" list | support.microsoft.com\[20\] |
| SAVEDATE | last save time ("Modified") | when the field is updated, not on save itself (secondary) | support.office.com; addbalance.com\[30\]\[31\] |
| CREATEDATE | creation date; reset by Save As (secondary) | on update | addbalance.com\[29\] |
| PRINTDATE | last print | "updates only when you print" | support.microsoft.com\[20\] |
| FILENAME | file name; `\p` adds path (secondary) | on update | eident.co.uk (secondary)\[52\] |
| DOCPROPERTY | value of a named document property | on update | Microsoft field list names it; detail page not read: **not found**\[53\] |

- **LibreOffice headless.** Converting does not refresh indexes ("Command line does *not* edit documents", ask.libreoffice.org, secondary).\[23\] The documented UNO route is `XDocumentIndexesSupplier.getDocumentIndexes()`, then on each index `XDocumentIndex.update()` (deprecated in favour of `XRefreshable`).\[38\]\[54\] Fields are refreshed with `TextFields` → `XRefreshable.refresh()`.\[39\] After that, call `storeToURL` with the `writer_pdf_Export` filter. The command-line form is `soffice --headless "macro:///Standard.Module1.UpdateIndexes(/path/file.odt)"` (community answer, secondary).\[23\] LibreOffice's own Writer guide says "Writer does not update the TOC automatically".\[55\]
- **What a generator must write so the TOC is right everywhere:**
  1. Write the TOC as a complex field: `begin`, then `instrText TOC \o "1-3" \h \z \u`, then `separate`, then the real entry paragraphs (TOC 1–3 styles, hyperlinks to `_Toc` bookmarks on the headings), then `end`.
  2. Page numbers: Word will fix them. For a PDF made without Word, either run the LibreOffice index update before export or compute them (the `docx` npm `docx/layout` entry "writes the table of contents' page numbers").\[28\]
  3. Put `w:dirty="true"` on the TOC `begin` only if you accept a Word prompt. Otherwise rely on the cached entries.
  4. A previewer shows only the cached result, so a TOC with placeholder text looks broken. OICWS/coscribe issue #197 records this as the worst defect its vision judge found.\[3\]

### Q3. Numbered lists

- **The model:** `w:abstractNum` holds the level definitions and "shall not be directly referenced by content". `w:num` references an `abstractNumId` and "can be referenced by zero or more paragraphs".\[24\]\[40\] All paragraphs that share a `numId` share counters.
- **Restart:** create a new `w:num` with the same `abstractNumId` and `<w:lvlOverride w:ilvl="1"><w:startOverride w:val="1"/></w:lvlOverride>`. `startOverride` "shall override the starting number of the child lvl element".\[24\]
- **Lettered sub-list under each heading:** either give each heading section its own `w:num` with a `startOverride` on level 1, or (simpler) use one multi-level list where level 1 has `w:lvlRestart` at level 0. Then the letters restart under each step automatically. The `lvlRestart` behaviour is referenced by the startOverride page ("restarted via the properties set in the lvlRestart element").\[24\]
- **Linking to a style:** the Heading 1 style's `w:pPr/w:numPr` holds only `w:numId`. When `numPr` is in a style, "any numbering level defined using the ilvl element shall be ignored". The matching `w:lvl` in the abstractNum carries `<w:pStyle w:val="Heading1"/>`.\[24\]
- **Order in `numbering.xml`:** the CT_Numbering schema sequence is `numPicBullet*`, `abstractNum*`, `num*`, `numIdMacAtCleanup?`. No prose sentence in the spec states it, and confirmation is secondary (Papyrine/OpenXmlHtml PR #101: the wrong order fails `OpenXmlValidator` and Word repairs the part).\[25\]
- **Generator mistakes:**
  - appending a `w:abstractNum` after existing `w:num` elements (schema violation)\[25\]\[26\]
  - reusing one `numId` for lists that should restart
  - setting `w:ilvl` on a paragraph whose numbering comes from a style
  - hard-typing "1.", "a)" as text
  - colliding `abstractNumId` or `numId` values when merging documents (docxcompose handles renumbering; its 1.0.0a6 note reads "Do not restart numbering of bullets")\[16\]

### Q4. Libraries

| Library | Current | Released | Maintained? | Can't do (sourced or noted) |
|---|---|---|---|---|
| python-docx | 1.2.0 | 16 Jun 2025 | No release in 17 months; Snyk labels it "INACTIVE" (secondary)\[56\] | Open `.dotx`; no content control, field, TOC or numbering API (by absence) |
| docxtpl | 0.20.2 | 13 Nov 2025 | Yes (0.20.0 May 2025, 0.20.1 Jul 2025)\[15\] | Built on python-docx, so it inherits the `.dotx` rejection (openchat issue #46, secondary);\[47\] LGPL-2.1-only |
| docxcompose | 2.2.0 | 2 Jun 2026 | Yes (2.1.0 earlier in 2026; preceding release 19 Mar 2026) | Combines documents only; no fill or TOC\[17\] |
| Open XML SDK | 3.5.1 | 18 Mar 2026 | Yes | No layout engine, so it cannot compute page numbers or update fields |
| `docx` (npm) | 9.16.0 | 19 Nov 2026 | Very active | Page numbers stay empty until updated unless `docx/layout` is used (PR #3590)\[2\] |

No release with an announced date within 6 months was found for any of these.

### Q5. Document control (ISO 9001:2015, paraphrased)

- **7.5.2 (creating and updating):** when documented information is created or updated, the organisation ensures suitable identification and description (examples given are title, date, author, reference number), suitable format and media, and review and approval for suitability and adequacy (paraphrase; secondary source qualityfieldguides.com).\[35\]
- **7.5.3 (control):** documented information must be available and suitable for use where and when needed, and adequately protected. As applicable, the organisation addresses distribution, access, retrieval and use; storage and preservation, including legibility; control of changes (e.g. version control); and retention and disposition. External documents are identified and controlled, and records kept as evidence are protected from unintended alteration (paraphrase).\[33\]
- ISO/TC 176/SC 2's N1286 guidance confirms that all QMS documented information "has to be controlled in accordance with clause 7.5" (iso.org PDF; full text blocked from fetching).\[34\]
- **Change record.** Neither ISO's public pages nor N1286 (as far as it could be read) say what columns a change record must have, or whether each revision carries every earlier row: **not found**. The columns revision, date, author, approver and description directly evidence the identification (7.5.2 a), review and approval (7.5.2 c) and change control (7.5.3.2 c) requirements. Carrying the full history in each revision is a defensible choice, not an ISO requirement. A generator must never rewrite earlier rows: it appends the new row and keeps the old ones byte-identical, because retained evidence must be protected from unintended alteration.\[33\]

### Q6. Accessibility

- **Accessibility Checker rules a generator can meet:**
  - Alt text on every image (Error; the checker also flags alt text that contains "image names or file extensions").\[27\]
  - A header row on every table (Error):\[27\] set `w:tblHeader` on the first row.
  - Simple table structure (Warning): no split, merged or nested cells.\[27\]
  - Heading styles (Tip):\[27\] use the built-in Heading 1–3 styles, which the TOC also needs.
  Source: support.microsoft.com, Rules for the Accessibility Checker, ms.date 17 Nov 2025.
- **Exporting PDF/UA from Word:** not covered in this run (not found).
- **LibreOffice:** its PDF export has a "Tagged PDF (add document structure)" option (UpdateStar how-to, secondary).\[57\] Its PDF/UA behaviour and documentation were not found.

### Q7. Mistakes AI assistants make

See section 7.

## 5. Tools

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| python-docx | read/write .docx | 1.2.0 | 2025-06-16 | `pip install python-docx==1.2.0` | none | pypi.org/project/python-docx |
| docxtpl | Jinja2 in .docx | 0.20.2 | 2025-11-13 | `pip install docxtpl==0.20.2` | none | libraries.io/pypi/docxtpl |
| docxcompose | append/merge, doc properties | 2.2.0 | 2026-06-02 | `pip install docxcompose==2.2.0`; `docxcompose master.docx content.docx -o out.docx` | none | pydeps.com (secondary); conda-forge\[17\]\[58\]\[59\] |
| Open XML SDK | .NET OOXML | 3.5.1 | 2026-03-18 | `dotnet add package DocumentFormat.OpenXml --version 3.5.1` | project file | nuget.org |
| docx (npm) | JS/TS generate and patch | 9.16.0 | 2026-11-19 | `npm install docx@9.16.0` | none | github.com/dolanmiu/docx/releases |
| LibreOffice (headless) | index update + PDF | 26.8.3 ("the third minor release in the LibreOffice 26.8 family") | 2026-11-12 | `soffice --headless "macro:///Standard.Module1.UpdateIndexes(path)"` then `--convert-to pdf` | user profile Basic library | TDF blog "Announcement of LibreOffice 26.8.3"; ask.libreoffice.org (secondary) |

## 6. Changing in the next 12 months

- **ISO 9001:2026:** published 16 September 2026 (ISO/TC 176/SC 2 news, 28 Sep 2026; iso.org lists "Published (Edition 6, 2026)"). From 31 March 2028, new and initial accredited certifications may only be issued to ISO 9001:2026, and certified organisations "will have until 30 September 2029" to transition (ISO/TC 176 news, 23 Sep 2026). A secondary source reports the "retain/maintain documented information" wording was replaced. The module's clause references and wording need review against the 2026 edition.
- **LibreOffice:** support for LibreOffice 26.2 ends on 30 November 2026 (TDF announcement of 26.8.3).
- **LibreOffice `XDocumentIndex`:** marked deprecated in favour of `XRefreshable`.\[38\] No removal date was found.
- **python-docx:** no announced release or deprecation found.
- **Open XML SDK:** no announced breaking change found.
- **docx (npm):** fast-moving minor releases (9.8 to 9.16 between September and November 2026).\[13\]\[60\] Pin exact versions.

## 7. Common mistakes (including AI assistants)

1. Calling `Document("template.dotx")` and failing with `ValueError` (python-docx issue #1532),\[9\] or "fixing" it by renaming the extension, which leaves the content type unchanged.\[1\]\[46\]
2. Replacing text with `paragraph.text = …` or searching `run.text`, which loses formatting or misses placeholders split across runs.
3. Writing an empty TOC field, or one whose cached result is "Right-click to update", and relying on `updateFields`. LibreOffice, PDF converters and previewers then show an empty or placeholder TOC (dolanmiu/docx PR #3590; OICWS/coscribe issue #197, both secondary).\[2\]\[3\]
4. Setting `updateFields` and then being surprised by Word's prompt (dolanmiu/docx #1212).\[28\]
5. Using DATE or SAVEDATE as a revision date (support.microsoft.com; support.office.com).\[20\]\[31\]
6. Appending `w:abstractNum` after `w:num`, or reusing a `numId`, so lists fail to restart (Papyrine PR #101, secondary).\[25\]\[61\]
7. Writing `PAGEREF` without a `separate` field character, so Word shows nothing or "1" (dolanmiu/docx issue #3480, secondary).\[62\]
8. Leaving a TOC field with unmatched `fldChar` begin and end after regenerating it (EvotecIT/OfficeIMO #3650, secondary).\[32\]
9. Omitting alt text and table header rows, which are Accessibility Checker errors.\[27\]
10. Rewriting earlier change-record rows when producing a new revision.

AI-assistant-specific: the items above are documented in issues filed against AI-driven document tools (OICWS/coscribe #197, all-the-rest/openchat #46). No systematic study was found.

## 8. Sources and licences

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| Microsoft Learn (Open XML SDK API pages incl. ISO/IEC 29500 excerpts) | Page licence not confirmed in this run; spec excerpts marked © ISO/IEC 29500:2008 | Short quotes only | Yes | Not confirmed; write your own code | Cite URL; note "ISO/IEC 29500 excerpt" |
| support.microsoft.com / support.office.com | Microsoft terms; not confirmed in this run | Short quotes | Yes | n/a | Cite URL |
| python-docx (PyPI, docs, source) | MIT | Yes | Yes | Yes | Keep MIT notice for copied code |
| docxtpl | LGPL-2.1-only | Yes, short | Yes | Avoid copying code into Apache-2.0 files; depend on it as a library instead | Name project and licence |
| docxcompose | MIT | Yes | Yes | Yes | MIT notice\[45\] |
| docx (npm) releases and PRs | MIT (npmjs.com shows "License MIT"; LICENSE reads "The MIT License (MIT) Copyright (c) 2016 Dolan") | Yes | Yes | Yes | Keep MIT notice for copied code |
| LibreOffice API docs (api.libreoffice.org) | Not confirmed in this run | Short | Yes | Not confirmed | Cite URL |
| ask.libreoffice.org, GitHub issues (secondary) | Not confirmed in this run | Short | Yes | Rewrite; don't copy | Cite URL, label secondary |
| ISO / ISO/TC 176 N1286 | © ISO | Phrases under 15 words only | Yes | n/a | "ISO/TC 176/SC 2 N1286" |
| qualityfieldguides.com, addbalance.com, eident.co.uk (secondary) | All rights reserved (presumed; not checked) | Short | Yes | n/a | Cite, label secondary |

## 9. Not found, contested, not covered

- **Not found:**
  - An explicit Microsoft recommendation of one placeholder type for code-filled templates.
  - Primary Microsoft pages for DATE, CREATEDATE, FILENAME and DOCPROPERTY behaviour on open.
  - A primary source that Word's TOC sits in `w:sdt`/`docPartObj`.
  - The spec sentence on element order in `numbering.xml` (it is schema-only).
  - Whether Word prompts for `w:dirty`.
  - The licences of Microsoft Learn, the Open XML SDK and LibreOffice docs (not checked this run).
  - Any ISO statement on change-record rows.
  - Any announced release within 6 months for any library.
- **Contested:**
  - "docxtpl is the usual library" (no neutral data).
  - python-docx maintenance: PyPI shows no release since June 2025 and Snyk labels it inactive, while forks claim 2.x versions.\[6\]\[7\]\[56\] Upstream is still 1.2.0.
- **Not covered:**
  - Exporting PDF/UA from Word.
  - LibreOffice PDF/UA detail.
  - Bookmark behaviour under editing.

## Sources

1. [docx.api — python-docx 1.2.0 documentation - Read the Docs](https://python-docx.readthedocs.io/en/latest/_modules/docx/api.html)
2. [fix: write the entries of a table of contents from the headings by dolanmiu · Pull Request #3590 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/pull/3590)
3. [Word: a table of contents reads as a placeholder sentence until Word updates fields · Issue #197 · OICWS/coscribe · GitHub](https://github.com/OICWS/coscribe/issues/197)
4. [python-docx Changelog - Safety](https://data.safetycli.com/packages/pypi/python-docx/changelog)
5. [python-docx · PyPI](https://pypi.org/project/python-docx/)
6. [python-docx-ng · PyPI](https://pypi.org/project/python-docx-ng/)
7. [python-docx Documentation Release 2.6.0 Steve Canny, Skelmis Jan 20, 2026](https://skelmis-docx.readthedocs.io/_/downloads/en/latest/pdf/)
8. [Wrong content type of a dotx template · Issue #41 · mherkazandjian/docxsphinx · GitHub](https://github.com/mherkazandjian/docxsphinx/issues/41)
9. [ValueError when loading .dotx Word template](https://github.com/python-openxml/python-docx/issues/1532)
10. [WordprocessingDocument.CreateFromTemplate Method](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.packaging.wordprocessingdocument.createfromtemplate?view=openxml-3.0.0)
11. [NuGet Gallery](https://www.nuget.org/packages/DocumentFormat.OpenXml/)
12. [DocumentFormat.OpenXml - nuget EOL Analysis](https://www.xeol.io/explorer/package/nuget/DocumentFormat.OpenXml)
13. [Release 9.16.0 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/releases/tag/9.16.0)
14. [Release 9.15.0 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/releases/tag/9.15.0)
15. [docxtpl 0.20.2 on PyPI - Libraries.io - security & maintenance data for open source software](https://libraries.io/pypi/docxtpl)
16. [docxcompose · PyPI](https://pypi.python.org/pypi/docxcompose/1.2.0)
17. [docxcompose 2.2.0: 10 deps, MIT](https://pydeps.com/project/docxcompose/)
18. [UpdateFieldsOnOpen Class (DocumentFormat.OpenXml.Wordprocessing)](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.updatefieldsonopen?view=openxml-3.0.1)
19. [Docx4java](https://webapp.docx4java.org/OnlineDemo/ecma376/WordML/fldChar.html)
20. [Some fields are updated while other fields are not](https://support.microsoft.com/en-us/topic/some-fields-are-updated-while-other-fields-are-not-eb3ad53a-328b-a3b4-91c6-28a84001855f)
21. [Updating table of contents TOC with command line - English - Ask LibreOffice](https://ask.libreoffice.org/t/updating-table-of-contents-toc-with-command-line/56010)
22. [How to automatically update indices in headless mode? - English - Ask LibreOffice](https://ask.libreoffice.org/t/how-to-automatically-update-indices-in-headless-mode/11878)
23. [Update TOC via command line - English - Ask LibreOffice](https://ask.libreoffice.org/t/update-toc-via-command-line/52518)
24. Microsoft Learn
25. [Keep a numbering part's element sequence when a list is converted into it by SimonCropp · Pull Request #101 · Papyrine/OpenXmlHtml · GitHub](https://github.com/Papyrine/OpenXmlHtml/pull/101)
26. [docx-custom](https://llm-skills.alisonaquinas.com/skill/alisonaquinas/llm-doc-skills/docx-custom/)
27. [Rules for the Accessibility Checker | Microsoft Support](https://support.microsoft.com/en-us/accessibility/office-accessibility/rules-for-the-accessibility-checker)
28. [this document contains fields that may refer to other files. Do you want to update the fields in this document? · Issue #1212 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/issues/1212)
29. [Using Fields in Microsoft Word - a Tutorial in the Intermediate Users' Guide to Microsoft Word](https://www.addbalance.com/usersguide/fields.htm)
30. [Using Date Fields in Microsoft Word - Charles Kenyon](https://www.addbalance.com/word/datefields1.htm)
31. [Field codes: SaveDate field](https://int.support.office.com/f1/topic-ssr/3c2cd5ae-e6e2-4c27-b69c-7f5c029c8d7f)
32. [UpdateFields (TOC): the old field-end paragraph is moved above the new entries, leaving an unmatched fldChar end and an empty line · Issue #3650 · EvotecIT/OfficeIMO · GitHub](https://github.com/EvotecIT/OfficeIMO/issues/3650)
33. [7.5 Documented information (7.5.3) \~ ISO 9001:2015 Manual](http://iso9001ver2015.blogspot.com/2015/10/75-documented-information-753.html)
34. [ISO/TC 176/SC2/N1286 www.iso.org/tc176/sc02/public](https://www.iso.org/iso/documented_information.pdf)
35. [Clause 7.5 ISO 9001: The 3 Documented-Information Findings](https://qualityfieldguides.com/iso-9001/clause-7-5-documented-information/)
36. [can't open a .docx file · Issue #229 · python-openxml/python-docx · GitHub](https://github.com/python-openxml/python-docx/issues/229)
37. [Dirty Class (DocumentFormat.OpenXml.Wordprocessing)](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.dirty?view=openxml-3.0.1)
38. [LibreOffice: XDocumentIndex Interface Reference](https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XDocumentIndex.html)
39. [LibreOffice: TextFields Service Reference](https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextFields.html)
40. [AbstractNum Class (DocumentFormat.OpenXml.Wordprocessing)](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.abstractnum?view=openxml-3.0.1)
41. [Guidance on the requirements for Documented Information ...](https://www.iso.org/files/live/sites/isoorg/files/standards/docs/en/iso_9001_2015_guidance_documented_information.pdf)
42. [Working with Content Controls](https://learn.microsoft.com/en-us/office/vba/word/concepts/working-with-word/working-with-content-controls)
43. [Content controls - Visual Studio (Windows)](https://learn.microsoft.com/en-us/visualstudio/vsto/content-controls?view=visualstudio)
44. [visualstudio-docs/docs/vsto/walkthrough-binding-content-controls-to-custom-xml-parts.md at main · MicrosoftDocs/visualstudio-docs · GitHub](https://github.com/MicrosoftDocs/visualstudio-docs/blob/main/docs/vsto/walkthrough-binding-content-controls-to-custom-xml-parts.md)
45. [docxcompose · PyPI](https://pypi.org/project/docxcompose/1.4.1/)
46. [Python dotx Conversion to docx for Automated Documents](https://www.doyler.net/security-not-included/python-dotx-conversion-docx)
47. [M4: Word templates — fill an uploaded .dotx and download a PDF · Issue #46 · all-the-rest/openchat · GitHub](https://github.com/all-the-rest/openchat/issues/46)
48. [\[P2\] Template validation: missing built-in styles and non-DOCX templates fail with raw exceptions · Issue #61 · markbac/py-doc2docx · GitHub](https://github.com/markbac/py-doc2docx/issues/61)
49. [Convert .dotx to](https://github.com/onizet/html2openxml/wiki/Convert-.dotx-to-.docx)
50. [Release 9.15.1 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/releases/tag/9.15.1)
51. [fldChar (Complex Field Character)](https://c-rex.net/samples/ooxml/e1/part4/OOXML_P4_DOCX_fldChar_topic_ID0E2ZT1.html)
52. [Microsoft Word Fields - Eident Training](https://eident.co.uk/2018/04/microsoft-word-fields/)
53. [List of field codes in Word](https://support.microsoft.com/en-us/office/list-of-field-codes-in-word-1ad6d91a-55a7-4a8d-b535-cf7888659a51)
54. [Chapter 7. Text Content Other than Strings - LibreOffice Programming](https://flywire.github.io/lo-p/07-Non-text_Content.html)
55. [Creating Tables of Contents, Indexes and Bibliographies](https://documentation.libreoffice.org/assets/Uploads/Documentation/en/WG4.2/PDF/WG4212-TOCsIndexesBiblios.pdf)
56. [python-docx](https://security.snyk.io/package/pip/python-docx)
57. [UpdateStar News](https://news.updatestar.com/post/libreoffice-writer-headings-auto-toc-and-pdf-bookmarks)
58. [pypi.org](https://pypi.org/project/docxcompose2)
59. [docxcompose - conda-forge](https://anaconda.org/conda-forge/docxcompose)
60. [Release 9.8.0 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/releases/tag/9.8.0)
61. [Keep a numbering part's element sequence when a list is rendered into it by SimonCropp · Pull Request #133 · Papyrine/Parchment · GitHub](https://github.com/Papyrine/Parchment/pull/133)
62. [Bug: PageReference omits the separate field character, so MS Word shows "1" instead of the resolved page number (even after "Update Fields") · Issue #3480 · dolanmiu/docx · GitHub](https://github.com/dolanmiu/docx/issues/3480)

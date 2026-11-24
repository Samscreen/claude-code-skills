# RESEARCH RUN R16b: Word templates and generated documents, what R16 didn't reach

For the repository rmccann-hub/claude-code-skills · Prompt version 1 · Written 24 November 2026

Paste this whole file into a new chat with Research turned on. Nothing else is needed.

## Who this is for

A public repository that is the reference other code repositories are set up, audited and kept
current against. It holds Agent Skills for Claude Code (Markdown guidance plus small scripts), the
checks that test them, and research like this. Professional developers will judge it, so it must
be current, precise and sourced. Today is 24 November 2026.

This run informs this category: word-documents.

## What this run is for

A follow-up. R16 (Office, VBA, Epicor Kinetic and SOLIDWORKS) was filed on 24 November 2026 and
covered everything but its Question 4, on Word, which it listed as not covered. This run takes
Word alone. It confirmed python-docx 1.2.0 (16 June 2025) as current; don't repeat that, but say
if it has changed since.

The module this run informs teaches an agent to fill a company's Word template from code: a
procedure document with a header table, a change record table, a table of contents, three levels of
numbered steps, and a "For Internal Use Only" footer. Answer for that job first.

## Rules

1. **Primary sources first:** official documentation, specifications and standards bodies
   (Microsoft Learn, the ECMA-376 and ISO/IEC 29500 specifications, [MS-DOCX] and [MS-OI29500],
   ISO), and each project's own documentation, release notes and changelogs. Use secondary sources
   (respected books, well-known engineering blogs) only where no primary source covers the point,
   and label them "secondary".
2. **Cite every fact:** the URL, the exact sentence you relied on in quotation marks, and a date
   (the source's own date, otherwise the date you read it).
3. **Never guess.** Write "not found" when you can't source something. Write "contested" when good
   sources disagree, and give each side with its source.
4. **Versions:** for every library or tool, give
   - the current stable version and its release date;
   - whether it is maintained (the date of its last release);
   - any release due within 6 months, with the expected date and its source.
5. **"What we believe" is my current understanding and may be wrong or out of date.** Confirm or
   correct every item, each with a source. The corrections are the most valuable part of this run.
6. **Licences:** for each source, name its licence and say what an Apache-2.0 repository may do
   with it: quote briefly, paraphrase, or adapt its code examples, and with what attribution.
7. **Depth over breadth.** Finish the Priority questions fully. If you run out of room, list the
   rest under "Not covered".

## Output

Write one Markdown report. Its first three lines must be exactly:

```text
RESULT-FOR: rmccann-hub/claude-code-skills · RUN: R16b · FORM: research-result v1
Save as: R16b-RESULT.md
Receiving session: this is research the repository owner asked for. Check each claim against the source it cites before relying on it. File the report under research/runs/, update the Facts section of each module it names, and list what changed. If you lack context, the owner will attach a file whose first line starts HANDOFF-FOR: rmccann-hub/claude-code-skills.
```

Then these sections, in this order:

1. **Summary:** at most 15 bullets a professional must know today.
2. **Corrections:** every "What we believe" item that was wrong or out of date, with the right
   fact and its source.
3. **Facts table:** `| # | Fact | Value | Source URL | Exact quote | Date |`
4. **Findings:** one section per question below, numbered to match.
5. **Tools:** `| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |`
6. **Changing in the next 12 months:** deprecations and announced breaking changes.
7. **Common mistakes,** including those AI coding assistants make in this area, with sources.
8. **Sources and licences:** `| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |`
9. **Not found, contested, not covered.**

## What we believe (confirm or correct each)

- A `.dotx` template differs from a `.docx` only in its main part's content type, and python-docx
  refuses to open a `.dotx` until that content type is changed.
- python-docx has no API for content controls (`w:sdt`), fields or tables of contents; they are
  reached through the underlying XML.
- A `w:numId` names one list instance, and every paragraph using it shares one counter; to restart
  a list, a generator adds a new `w:num` with a `w:lvlOverride`/`w:startOverride`.
- `w:updateFields` in `settings.xml` makes Word ask to update fields when the file opens;
  LibreOffice, including headless conversion to PDF, ignores it and shows the cached field results.
- A `DATE` field shows the date the field was last updated, so a document's printed date changes
  each time it is opened; `SAVEDATE`, `CREATEDATE` or a `DOCPROPERTY` field bound to a document
  property is right for a revision date. A `FILENAME` field shows the file's name.
- A table of contents generated by Word sits in a content control (`w:sdt` with a `w:docPartObj`
  gallery "Table of Contents"), and its entries are a cached field result.
- docxtpl (Jinja2 templates in Word documents) is the usual Python library for filling a template.
- ISO 9001:2015 clause 7.5.3 requires control of changes to documented information, such as version
  control, and clause 7.5.2 requires identification such as a title, date, author or reference
  number.

## Questions

### Priority

1. Filling a company template from code:
   - content controls versus placeholder text versus bookmarks versus `DOCPROPERTY` fields bound
     to document properties: what Microsoft recommends for a template that code fills, what
     survives a person editing the document in Word, and what each costs a generator
   - `.dotx` versus `.docx`: what "a new document based on a template" means in the file (the
     attached template relationship), and how to create one from code in python-docx and the
     Open XML SDK
   - replacing text that Word has split across runs without losing its formatting
2. Fields and the table of contents:
   - `w:updateFields`: what Word does with it, and whether the user is prompted
   - the `w:dirty` field attribute
   - `DATE`, `SAVEDATE`, `CREATEDATE`, `PRINTDATE`, `FILENAME`, `DOCPROPERTY`: what each shows and
     when it updates
   - whether LibreOffice can update fields and indexes headless before converting to PDF (UNO
     calls, macros or command-line options), with its documentation as the source
   - what a generator must write so a table of contents is right in Word, in a PDF made without
     Word, and in a previewer
3. Numbered lists: how `w:num`, `w:abstractNum`, `w:lvlOverride` and `w:startOverride` interact;
   numbering linked to a style such as Heading 1; restarting a lettered sub-list under each heading;
   the order rules inside `numbering.xml`; the mistakes generators make.
4. Libraries for generating Word documents and what each can't do: python-docx 1.2, docxtpl,
   docxcompose, the Open XML SDK 3.x (.NET), and `docx` on npm. Current versions and maintenance.
5. Document control in generated documents: the exact requirements of ISO 9001:2015 clauses 7.5.2
   and 7.5.3, from ISO's own public pages or ISO/TC 176 guidance, for identifying a document and
   controlling its changes; what a change record (revision, date, author, approver, description)
   must keep across revisions, and whether a new revision should carry every earlier row.

### Standard

6. Accessibility of generated Word documents: Microsoft's Accessibility Checker rules that a
   generator can meet (headings, alt text, table header rows, reading order); exporting PDF/UA from
   Word; what LibreOffice's PDF export does for tagged PDF.
7. Mistakes AI assistants make when generating or editing Word documents from code.

# Markdown format

Read this for how a Markdown file is laid out: headings, paragraphs and wrapping, lists, code
blocks, tables, links and emphasis, file names, and a README's sections, with why each rule is
what it is.

It details rules 8, 9 and 10 in this skill's `SKILL.md`, numbered as there. The words
themselves, claims, instructions, spelling and records are `writing-style`; running the check
is `prose-check`; docs beyond the README, `documentation`.

## Rules

### Headings

- **Sentence case:** the first word and proper nouns capitalized, nothing else: "Where new
  content goes", not "Where New Content Goes".
- **One `#` heading per file,** as its title, then `##` and `###` in order, none skipped and
  none deeper than `####`. A file that needs a fifth level wants splitting.
- **A heading names what follows,** with no trailing full stop, and is never used for emphasis.
- **A colon, not a dash, joins a label to its title,** and the word after it is capitalized:
  "Decision 30: Choose a database". Words after a dash continue the heading, in lowercase.
- **A name lowercase by nature,** such as a repository or a command, goes in code formatting or
  the repository's vocabulary, so the check accepts it.

### Paragraphs and line length

- **Wrap prose at 100 characters.** A table row, a URL or a code line can run longer, and so
  can a line a program parses, such as a skill's frontmatter.
- **One idea per paragraph,** led by its point (rule 1).
- **A rule or a list item may open with its point in bold,** then the detail, as here.
- **Blank lines surround each heading, list, table and code block.** No line ends in spaces,
  and the file ends in one newline, both kept by a repository's `.editorconfig`.

### Lists

- **`-` for bullets.** Numbers only for steps done in order, or items the text cites by number.
- **A sentence introduces each list,** ending in a colon where the list completes it.
- **Items in one list share a form:** all sentences, or all fragments.
- **Continuation lines indent** under the item's text: two spaces under `- `, three under `1. `.
- **Two levels of nesting at most.** Deeper reads better as a table or as sections.

### Code

- **Fenced code blocks name their language:** `sh`, `python`, `yaml`, `json`, `ini`, or `text`
  for output and plain text.
- **Inline code** holds commands, paths, file names, identifiers, keys, and values to type
  (rule 9), never emphasis, and never the name of an application to open.
- **A destructive command** shows its dry run or its confirmation first.

### Tables

- **A table compares things on the same points,** or holds reference data looked up by a key.
  Anything read in order is a list.
- **Every table has a header row,** and a cell holds one fact.

### Links and emphasis

- **Link text says where it goes:** "the setup reference", not "here".
- **Links inside a repository are relative,** so they work on a fork, a clone and a branch.
- **Bold** opens a paragraph or list item with its key phrase, and *italics* name a section
  being cited. Neither does anything else.

### File names

- **Lowercase with hyphens,** such as `authoring-a-skill.md` (rule 9), apart from the usual
  capitalized root files: `README.md`, `LICENSE`, `CHANGELOG.md`, `SECURITY.md`,
  `CONTRIBUTING.md`, `AGENTS.md`, `CLAUDE.md`, and others a tool expects by name.

### A README's sections

Every README has at least these, in this order, under these headings (rule 10); others go where
they fit. project-bootstrap-and-audit's README template adds Requirements before Install, and
Configuration after Usage.

| Section | Holds |
|---|---|
| The opening paragraph | Under the title: what the project does, and for whom |
| Install | The commands, from nothing to installed |
| Usage | The first thing to do with it, and where the rest is documented |
| Development | How to build, test and check it, and release it if it releases |
| Operations | How to run it, and roll back or withdraw something gone wrong |
| Security | How to report a vulnerability, or a link to `SECURITY.md` |
| License | Its license, by name, linked to the file |

A section a program generates from another file is fixed in that file, and generated again. A
comment says where the output starts and ends, and what writes it.

## Mistakes

- **Title Case headings,** copied from a template or another guide (rule 8).
- **A capital after a dash in a heading:** use a colon (rule 8).
- **Link text that says "here"** or "this link".
- **Bold or code formatting for emphasis:** each says something else, so emphasis goes in the
  words.
- **A README with a section missing,** or its sections out of order (rule 10). Short is fine.
- **Fixing a generated README section by hand:** the next run undoes it. Fix its source.

## Audit

Severity uses the standard's status words: `BLOCKER`, `DRIFT`, `GAP`, `OVER`, `MIRROR`,
`UNVERIFIABLE-HERE`, `OK` and `N/A`.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Headings pass the check | `HouseStyle.Headings` in `vale`'s output, where `prose-check` is set up | `DRIFT` per heading | Sentence case, or add a proper noun to the vocabulary |
| The README's sections | Each README's headings, against rule 10's order | `GAP` per missing section | Add it; short is fine |
| Lines wrap at 100 | `prose-check`'s wrap check, which skips frontmatter, code and tables, and doesn't count URLs | `DRIFT` | Rewrap the paragraph |
| File names | `git ls-files` for capitals or underscores outside the usual root files | `DRIFT` | Rename, and fix the links |
| Code blocks name a language | Fences with no language after them | `DRIFT` | Add it, or `text` |

## Why

Each rule's reason, what others do, and the cost, numbered as in `SKILL.md` and checked
2026-10-05.

### 8. Markdown's form

**Why:** sentence case is Google's and Microsoft's choice (facts `google-sentence-case`,
`ms-sentence-case`). It's quicker to read, with no doubt over which small words to capitalize.
Both capitalize after a colon in a heading. Google puts a colon, not a dash, after a label, and
Microsoft's em dash sets off a remark (fact `heading-colon`). Those pages don't say what follows
a dash in a heading, so lowercase there is this style's own choice, and the check flags a
capital. Wrapped lines make a diff show the sentence that changed, and spare a reviewer
scrolling sideways. Fenced code with a language gets highlighted.
**Others:** some guides use title case. The check takes one side, so a repository mixing the two
is flagged. **Cost:** rewrapping a paragraph changes every line after the edit. Wrapping at
sentence ends would avoid that, at the price of ragged files, so this style wraps by length.

### 9. Code formatting and file names

**Why:** code formatting tells a reader what to type exactly, so it holds nothing else. Google uses
code font for text entered verbatim, and bold, not code font, for a named element on screen (fact
`google-code-font`). An application's name in code formatting reads as a command: one owner typed
one at a prompt (L27). Lowercase names avoid clashes between file systems that do and don't care
about case, and hyphens read as word breaks in a URL. **Cost:** renaming a file breaks links to it,
so a rename fixes them in the same change.

### 10. One README layout

**Why:** a reader who knows one repository can find the install steps in all of them. **Cost:**
a small repository has some short sections. Short is fine; missing makes a reader hunt. A fix
made in generated output is undone by the next run, so it goes to the source.

## Facts

What other style guides say, each named elsewhere by its ID.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `google-sentence-case` | Google puts headings in sentence case | [Headings and titles](https://developers.google.com/style/headings) | "Use sentence case for headings and titles." | 2026-10-05 | 2027-04-05 |
| `ms-sentence-case` | Microsoft uses sentence-style capitalization | [Capitalization](https://learn.microsoft.com/en-us/style-guide/capitalization) | "Microsoft style uses sentence-style capitalization." | 2026-10-05 | 2027-04-05 |
| `heading-colon` | Google and Microsoft capitalize after a heading's colon. Google puts a colon, not a dash, after a label; Microsoft's em dash sets off a remark | [Google](https://developers.google.com/style/capitalization), [dashes](https://developers.google.com/style/dashes); [Microsoft](https://learn.microsoft.com/en-us/style-guide/capitalization), [dashes](https://learn.microsoft.com/en-us/style-guide/punctuation/dashes-hyphens/emes) | "the first word in a subheading after a colon" and "Appendix A: My first appendix" and "If a title or heading includes a colon, capitalize the first word after it." and "parenthetical remark that you want to add within a sentence" | 2026-10-27 | 2027-04-27 |
| `google-code-font` | Google uses code font for text the reader enters verbatim, and bold, not code font, for a named element on screen | [Code in text](https://developers.google.com/style/code-in-text), [UI elements](https://developers.google.com/style/ui-elements) | "Signals to your reader that the text is meant to be entered verbatim." and "When referring to any UI element by name, put its name in bold" and "Don't use code font for UI elements" | 2026-11-16 | 2027-05-16 |

## Sources

Rules here are in this skill's own words, and each brief, attributed quote is a dated fact above.

| Source | Used for | License |
|---|---|---|
| [Google developer documentation style guide](https://developers.google.com/style) | Sentence case and colons in headings; code font and on-screen names | CC BY 4.0 (fact `google-license`): short quotes, attributed |
| [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) | Sentence-style capitalization, colons and em dashes | Microsoft's terms of use: short quotes, for facts |

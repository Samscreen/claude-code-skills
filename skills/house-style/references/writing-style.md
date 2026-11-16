# Writing style

Read this for writing or reviewing what prose says: a claim and the evidence behind it,
instructions a reader who isn't a programmer can follow, words to cut, plain words, American
spelling, dates and records, and why each rule is what it is.

It details this skill's rules 1 to 7 and 11 to 13, numbered as in `SKILL.md`. Headings, lists,
wrapping, code blocks, tables, links, file names and a README's sections are `markdown-format`;
running the check is `prose-check`; commits and the changelog, git-workflows.

## Rules

### Claims and their evidence

A report, a pull request or a status line makes claims (rule 4):

- **A claim takes the strongest verb its evidence supports, and no stronger.** "Fixed" and
  "passes" need a run that shows it; what was only read is "the code reads as if"; what wasn't
  run is "untested". A run that showed it is stated plainly, not hedged.
- **A claim names its artifact:** the commit, file and line, test, log or run it rests on, so a
  reader can check it. "Tests pass" becomes "`uv run pytest` passed at commit `a1b2c3d`, 412
  tests".
- **An absence says what it means.** "No errors" says what was searched, over what span, and
  whether that source would have shown an error at all. Nothing found isn't nothing looked for.

### Instructions for a reader who isn't a programmer

A person following steps they can't judge does exactly what the text seems to say (rule 7):

- **An application's name never sits where it could be read as something to type,** such as
  in code formatting or beside a command. Say where to find it, "open the program named
  Konsole from the applications menu", and keep code formatting for what's typed.
- **Say what the screen looks like** at each step: "you're in the terminal when the line ends
  in a `$`".
- **One command per block,** each followed by what its output should look like, so the reader
  can tell success from failure before the next step.

### Words to cut, and what to use instead

Rule 3 names six words, and HouseStyle's `Filler` rule finds each.

| Word | Instead |
|---|---|
| `just` | Delete it. Where it means "only" or "a moment ago", say that |
| `simply` | Delete it |
| `very` | A precise word, or the number |
| `seamless` | Say what works and what's needed |
| `robust` | Say what it withstands |
| `leverage` | Use, build on, or take advantage of |

Unearned hedging goes too: "should work", "might help" or "probably" where the fact can be
checked (rule 4).

### Plain words

Rule 2: a common word where one exists, and one term for each thing.

| Instead of | Write |
|---|---|
| utilize | use |
| facilitate | help, or make possible |
| in order to | to |
| prior to | before |
| a number of | some, or the number |
| at this point in time | now |
| due to the fact that | because |

### American spelling

HouseStyle's `Spelling` rule finds common British forms, such as -ise, -our and -re, and gives
the American (rule 12). Most of its words follow a pattern: -ise and -isation to -ize and
-ization (organize, organization, recognize); -our to -or (behavior, color, favor); -re to -er
(center); -ogue to -og (catalog); -ence to -ense in some nouns (license, defense, offense); a
doubled `l` to one before -ed and -ing (labeled, canceled, modeling); and -ement after -dg to
-ment (judgment, acknowledgment). It leaves alone -ise words the same in both, such as advise,
exercise, promise, otherwise and expertise. Names, such as the Open Government Licence, and
quotes keep their own spelling.

A label or value the code defines, such as a button's text, is written as the code spells it,
in code formatting, which the check skips. In the project's own code, fix the spelling there
first, and the documentation follows.

### Records and dates

- **Dates are `YYYY-MM-DD`,** read the same way anywhere, and sortable.
- **A time is stamped in UTC, with its zone,** such as `14:05 UTC`, or ISO 8601 with `Z`. A
  local time, if wanted, is derived from the stamp and shown with it, each with its zone, in the
  order the reader chose: `8:55 PM EDT, Fri Oct 16 (2026-10-17 00:55 UTC)`. A time with no zone
  guesses at the reader's clock, and a local time without its stamp goes wrong twice a year.
- **A time copied from a source keeps its zone,** and is converted to UTC from it. An audit
  copied a log's `5. October 2026, 22:48 (UTC-04:00)` as `2026-10-05 22:48`, so its date
  disagreed with the file it cited, named for the next day, the date in UTC.
- **An append-only record's past entries stay as written, in their order.** New entries follow
  the style. A new record runs newest first; an oldest-first one keeps its order, and says so
  at its top.

## Mistakes

- **"Just", "simply" and the rest of the six,** in any sense: the check flags `just` meaning
  "only" too (rule 3).
- **A hedge where the fact can be checked,** such as "should work" (rule 4).
- **"Fixed" or "verified" with no run behind it,** or "no errors" with no word on what was
  searched (rule 4).
- **"Open Konsole" to a reader who isn't a programmer,** or three commands in one block with
  no expected output (rule 7).
- **Three names for one thing,** such as "the record", "the log" and "the history" (rule 2).
- **Session detail,** such as "as we discussed" or "the earlier run", which a reader who wasn't
  there can't follow (rule 7).
- **Restyling what the style leaves alone:** shared files, third-party files, quotes, generated
  output, and an append-only record's past entries or their order.
- **Converting a quote to American spelling,** or an app's label in the documentation only
  (rule 12).

## Audit

Severity uses the standard's status words: `BLOCKER`, `DRIFT`, `GAP`, `OVER`, `MIRROR`,
`UNVERIFIABLE-HERE`, `OK` and `N/A`.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| The checked rules pass | `git ls-files -z '*.md' \| xargs -0 vale`, where `prose-check` is set up | `GAP` per file that fails | Fix the text, or add a flagged name to the vocabulary |
| The answer comes first | The first paragraph of each README, report and pull request description | `GAP` where it opens with background | Move the result to the top |
| Facts carry sources and dates | Versions, dates and support windows in the prose | `GAP` per stale-prone fact lacking either | Check it and add both, or say it wasn't checked |
| Claims match their evidence | Each "fixed", "verified", "passes" or "no errors" in a report or pull request | `GAP` per claim with no named run or artifact | Name it, or weaken the verb to what was done |
| Steps a non-programmer can follow | An application's name in code formatting; several commands in one block; no expected output | `GAP` | Name where to find it, one command per block, and its output |

## Why

Each rule's reason, what others do, and the cost, numbered as in `SKILL.md` and checked
2026-10-05. The check's own reasons are in `prose-check`.

### 1. The answer first

**Why:** most readers stop early: a reviewer skimming a pull request, an owner reading a report
on a phone, an agent reading a context file. A reason read first is read without knowing what
it's for. **Cost:** a reader who needs the reasoning to trust the answer reads on. **Choose
differently:** in a tutorial, where the reader builds up to the result, the steps come first.

### 2. Plain words, and one term for each thing

**Why:** readers vary in their English, and many read through a translation tool. A plain word
survives that, and a synonym used for variety looks like a second thing. GOV.UK makes plain
English mandatory (fact `govuk-avoid`). **Cost:** plainer prose, which is the intent.

### 3. No filler, hype or unearned hedging

**Why:** each of the six adds nothing or claims what the text should show. Google calls `just`
usually filler, and asks writers to try cutting `simply` (fact `google-just`): what's simple
for one reader isn't for another. Google avoids `leverage` meaning "use" (fact
`google-leverage`); GOV.UK avoids it outside finance, and `robust` unless of a sturdy object
(fact `govuk-avoid`). `very` and `seamless` are this style's own: each stands in for the fact.
**Others:** Google and GOV.UK list many more. This style keeps the six seen in practice, so the
check stays quiet on fine text. **Cost:** finding the precise word, and rewording `just`
meaning "only". A word mentioned as a word, as here, goes in code formatting, which the check
skips.

### 4. Checked facts

**Why:** a wrong fact copied into many repositories is wrong in all of them. A date on a fact
tells the next reader when to doubt it. Saying what wasn't checked costs a sentence, and stops a
guess passing for a finding. **Cost:** time at writing, and a date to check again by.

A claim's verb is a fact about its evidence, and a reader acts on the verb (L25). Four
releases once claimed a fix that no test through the app had shown (L5). An evidence bundle
that listed what it left out let "nothing was missing" be told from "nothing was collected"
(L4). Naming the artifact turns a claim into something checked in a minute. This is the
repository's own lesson; the guides cited here don't state it. **Cost:** longer sentences, and
saying what wasn't run. A verb weaker than the evidence costs the reader a check they needn't
make, so the rule cuts both ways.

### 5. Short sentences in the active voice

**Why:** a long sentence holds its reader's memory until its verb arrives. The active voice names
who does what, which matters in instructions and in records of who decided. **Choose
differently:** where the actor is unknown or doesn't matter, the passive is fine: "the file is
generated".

### 6. Rules that say what breaks, and statuses that say who's waiting

**Why:** a rule with its reason can be judged, and dropped when the reason goes. A rule without
one is kept forever, or broken on a guess. A status that names who it waits on gets answered.

### 7. A reader who wasn't there

**Why:** repositories outlive the conversations that changed them. A reader a year on, or a new
agent, has only the text.

A reader who isn't a programmer can't tell a program's name from a command. One owner typed
`Konsole` at a prompt after reading "open Konsole" (L27). Describing the screen lets them
check where they are, and an expected output per command lets them stop at the first failure
rather than three steps on. Google keeps code font for what's typed and bold for what's on
screen (fact `google-code-font`). **Cost:** longer instructions. **Choose differently:** for a
reader who runs commands daily, a block of several commands is fine.

### 11. Commits, changelogs and decisions

git-workflows has the reasons and the alternatives, and accepts either grammar, so a recorded
one holds. A record read newest first opens on the current state. Reordering an old record
moves every past entry, so it keeps its order, and the line at its top says which end is new.

### 12. American spelling

**Why:** the owner chose it. The tools and platforms these repositories use write American
English, and so does their code: a skill's frontmatter has a `license` field, and GitHub has
organizations. Mixed spelling reads as two authors, and a search for one form misses the other.
**Cost:** converting British text, once. A label respelled in the documentation alone
disagrees with the screen, and a search of the code for it finds nothing. **Choose
differently:** a project whose readers write British English, such as a UK public body's.

### 13. Formatters for code

**Why:** a formatter ends arguments about layout, and its output is the same on every machine.

## Facts

What other style guides say, each named elsewhere by its ID.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `google-just` | Google calls "just" usually filler, and suggests cutting "simply" | [Word list](https://developers.google.com/style/word-list) | "Usually, just is a filler word" and "Try eliminating this word" | 2026-10-05 | 2027-04-05 |
| `google-leverage` | Google avoids "leverage" meaning "use" | [Word list](https://developers.google.com/style/word-list) | "Avoid using if you mean use." | 2026-10-05 | 2027-04-05 |
| `google-license` | Google's style guide is under CC BY 4.0 | [Style guide](https://developers.google.com/style) | "licensed under the Creative Commons Attribution 4.0 License" | 2026-10-05 | 2027-04-05 |
| `govuk-avoid` | GOV.UK makes plain English mandatory, and avoids "leverage" and "robust" | [Style guide, A to Z](https://www.gov.uk/guidance/style-guide/a-to-z) | "Plain English is mandatory" and "leverage (unless in the financial sense)" and "robust (unless talking about a sturdy object)" | 2026-10-05 | 2027-04-05 |

## Sources

Rules here are in this skill's own words, and each brief, attributed quote is a dated fact above.

| Source | Used for | License |
|---|---|---|
| [Google developer documentation style guide](https://developers.google.com/style) | "just", "simply", "leverage" | CC BY 4.0 (fact `google-license`): short quotes, attributed |
| [GOV.UK style guide](https://www.gov.uk/guidance/style-guide/a-to-z) | Plain English; "leverage", "robust" | Open Government Licence v3.0: short quotes, attributed |

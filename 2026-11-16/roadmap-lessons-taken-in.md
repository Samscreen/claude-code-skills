# Lessons taken in by their modules

Moved verbatim from `ROADMAP.md` on `main` at commit 32f0549, its section *Lessons waiting for
their module*, by the owner's "do all" of 2026-11-16: the 49 of L1 to L57 marked taken in. L23, L25 and L27,
taken in the same day by the `house-style` split, follow from `main` at commit 316d2c2. L21,
L22, L33, L34 and L51 still wait, and stay on `main`.

- **L1, `test-gates`, taken in:** check the fact, not a symptom the failure path shares. When one check is
  re-keyed onto the fact, re-key every other check that reads the same symptom. On 2026-10-04 a
  live repository's acceptance step passed an identification because rows had loaded. They were
  the placeholders its app loads when a lookup finds nothing. A sibling check, re-keyed onto the
  identifier after the same symptom fooled it once before, caught it two steps later.
- **L2, `test-oracles`, taken in:** a test that needs outside data, such as an entry in a public catalog,
  names the fixture it expects, and says so when the fixture is the cause. The same rig made
  three acceptance runs in 40 minutes, on two inputs the catalog didn't know. Each one read as
  a failed step, not as the wrong input.
- **L3, `logging-and-observability`, taken in:** every timestamp carries its offset. The same app logged
  in local time and wrote its evidence bundle in UTC, so one event sat four hours apart in the
  two.
- **L4, `logging-and-observability`, taken in:** an evidence bundle lists what it left out, and the raw
  facts each verdict was computed from. That bundle did both, so "nothing was missing" could be
  told from "nothing was collected", and a wrong label could be checked against its inputs.
- **L5, `test-gates`, taken in:** a regression test for a wiring bug goes through the production entry
  point. Four releases claimed a fix whose test handed the fact straight to the renderer, while
  nothing in the app ever passed it on.
- **L6, `test-gates`, taken in:** grep for a call site before believing a documented capability. Four
  cancel methods were documented and never called.
- **L7, `test-gates`, taken in:** a test asserts the invariant, not today's state, and a rule about releases
  runs on the release path. A unit test blocked every commit during a review round, and didn't
  block the releases it was for.
- **L8, `test-gates`, taken in:** the command typed locally stands in for CI's, so it matches CI's import
  path and compiler flags. `python -m pytest` adds the current directory to `sys.path` and the
  `pytest` script doesn't; a bare `gcc` passed code the project's flags reject.
- **L9, `test-gates`, taken in:** a gate never picks its subject by sort or directory order. The "newest
  verification" was whichever file the directory listed last.
- **L10, `test-gates`, taken in:** a scripted edit with several parts asserts each part landed. One assert
  covered one replacement while the others silently did nothing.
- **L11, `acceptance-runs`, taken in:** a stand-in for hardware can be a fault-injection shim. An `LD_PRELOAD`
  shim that fails reads found a hang no drive run had, and reproduced a damaged disc on demand.
- **L12, `test-oracles`, taken in:** a parser that offline tests never reach is tested against a recorded
  response. Tests that all ran offline left a network parser at 27% branch coverage, hiding
  three crashes.
- **L13, `flaky-tests`, taken in:** an intermittent failure can be a race in the program, not the test. One
  was a signal arriving after the loop, fixed in the program. This adds to F87.
- **L14, `test-oracles`, taken in:** filed evidence is read as a set of claims. Two defects sat for weeks in
  logs both sides had filed and nobody had read.
- **L15, `test-oracles`, taken in:** a check is independent of another by the time between them, not the
  date. Two checks on consecutive dates were 26 minutes apart.
- **L16, `error-handling`, taken in:** a broad `try` around a whole validator fails open. One field of
  the wrong type made the validator return no errors, and a path-traversal template was saved.
- **L17, `error-handling`, taken in:** an exit code carries one meaning. One program exited 1 for both a
  failed read and a stopped search, and its consumer couldn't step its retry ladder down.
- **L18, `error-handling`, taken in:** a captured child process records a tri-state exit code, null for a
  child never reaped, its arguments as run, and long output as head and tail with a count of
  what was cut.
- **L19, `logging-and-observability`, taken in:** a program that writes two records of one run makes them
  agree. The machine-readable record and the archival log disagreed, and the archival one was
  wrong.
- **L20, `logging-and-observability`, taken in:** a population is recorded once, as data, and never
  derived again. One total was re-derived, and fixed, in four files.
- **L23, `c-build`, taken in:** gate on the count of warnings
  under the shipped flags rather than `-Werror`, which fails on a new compiler's new warnings.
  Ask the binary whether it's instrumented: a test log looked sanitized while the binary
  wasn't. Argument shape is a probe axis of its own, and it found an overread both sanitizers
  missed. `c-build` carries all three, in its rules 3, 5 and 8 and its Why.
- **L24, `versioning-and-releases`, taken in:** a fork whose advancing part is SemVer build metadata
  can't order its releases by version, since the specification ignores build metadata for
  precedence. Order by a release sequence.
- **L25, `writing-style`, taken in:** a claim takes the strongest verb its
  evidence supports and no stronger, names the artifact, and says what an absence means.
- **L26, `review-loops`, taken in:** what one loop of two repositories learned over 31 rounds and eight
  protocol versions, as a starting set:
  - **What worked:**
    - Close conditions fixed at the first lap.
    - A pre-commit, "our next lap is GO unless X". Rounds went from 37 laps to three.
    - Each side reading the other's default branch rather than relayed files.
    - A lap counted as sent only when marked released.
    - Lap numbers per side.
    - A short header parsed fail-closed.
    - Claims cited as `owner/repo@sha:path:line`.
    - One status block per side, checked by that side's tests.
    - A conformance table with a test per row on both sides.
    - Overrides written once, with the rule, who and why.
  - **What cost more than it caught:**
    - Round digests and a reconcile state.
    - Envelopes around laps.
    - Copying the peer's verdict into one's own lap.
    - A required ledger field on GO laps.
    - Close-by dates and a lap ceiling that never fired.
    - Releases gated on round state.
    - A mirrored spec where each correction is a version that governs only from the next round.
    - Hand-copied pins in prose.
  - **What the agents couldn't supply:** time on hardware, a design both sides agree on, and
    acts only the owner can do. No number of laps stood in for any of them.
  - **The owner's rulings:**
    - Cut rules about choreography and keep rules about evidence.
    - An answer is not a settlement.
    - Laps that only acknowledge are gone.
  - **Where the value was:** the contract mismatches neither side could see alone, such as a
    flag upstream had dropped, a filtered message list and one-word parser misses. Nearly all
    came from reading the other side's committed artifacts or a run on real hardware, rarely
    from a lap's argument.
- **L27, `writing-style`, taken in:** instructions for a reader who isn't a
  programmer never put an application's name where it could be taken for something to type.
  One owner typed `Konsole` at a prompt after reading "open Konsole". Say what the screen looks
  like instead, such as "you're in the terminal when you see a `$`". Each command goes in its
  own block, with what its output should look like.
- **L28, `review-loops`, taken in:** a change both sides must make is agreed word for word, and then each
  side runs its checker against the other's tree from a fresh clone. After a history rewrite,
  a stale local branch made one checker read an old map and report 13 false refusals.
- **L29, `documentation`, taken in:** a field whose format a test enforces has the format written beside
  the field. One session learned a status field's format only from a failing test.
- **L30, `review-loops`, taken in:** what one round that moved both sides' evidence taught about running
  the loop, on 2026-10-14 and 15:
  - **The reporting that worked:** eight fixed diagnostic keys in every lap, a seven-heading
    round summary in each side's last lap, and a five-line handoff block ending each reply that
    names exactly what to read. The owner copied the block between sessions. It took six
    changes in about 45 minutes to settle, so settle it before the first lap.
  - **Approval given with the request:** "release once its pull request is green" in the
    message that asked for a lap removed one round trip per lap.
  - **Steps the protocol lets run side by side, run side by side:** both moves went ahead at
    once, and finished within a minute of each other.
  - **An operator message goes stale like any other copy:** three of the coordinator's commit
    and rule numbers were wrong by the time they were read. Each side caught them by checking
    its own tree.

- **L31, `test-gates`, taken in:** a check must be able to fail, and these tests show it can:
  - it compares the whole value, and the value the document wrote. A checker that cut two
    hashes to 16 characters, and another that never read the hash a record wrote beside its
    citation, both passed a changed hash;
  - it never compares a value with one derived from itself. Under an option that overwrote a
    field, comparing the input with the written files would always have agreed; the fix
    compares with what was passed;
  - a summary or diff tool is tested against a known change it must report. One said
    "unchanged" over the commit that added a flag, because a row filter skipped its row, and a
    "complete" list built for one build left out a flag only the other build took;
  - a sweep over a population carries a minimum count, and each fix is reverted once to show
    its test fails. Two probes found tests that couldn't fail.
- **L32, `flaky-tests`, taken in:** a flaky failure is fixed where it is, then a ratchet refuses the
  pattern coming back: it fails closed on code it can't place, and its allowlist may only
  shrink. Two flakes from one directory walk racing a parallel worker's cleanup were the same
  shape, and a third had been written before the ratchet.
- **L35, `review-loops`, taken in:** take in every message the other side has released before writing
  anything that sums up the exchange. A digest written before one released lap was filed could
  not be reproduced by its reader, and a counter that included one's own unreleased lap refused
  the other side's verdict.
- **L36, `review-loops`, taken in:** a message says what is established now, names what it waits on by
  the condition it must meet rather than a version number, commits in advance to how the next
  verdict will be decided, and says what it doesn't ask. A round closed in three laps on that.
  An owner's `I thought we just needed X?` is the instruction, and reading it as a question
  cost a round trip.
- **L37, `review-loops`, taken in:** a shorter acceptance run is scoped from the diff, lists what it leaves
  out and the risk, and replaces an agreed close condition only by the owner's recorded
  override. A step that can hang runs last, under a time limit nothing can raise.
- **L38, `review-loops`, taken in:** a file both sides must hold identically is written by one side,
  copied byte for byte by the other and checked by SHA-256, never retyped. Every hash in a
  message is pasted from a command's output: one draft's hash had its first 16 characters
  right and the rest invented.
- **L39, `agent-context-files`, taken in:** parallel helper sessions pay for read-only audits, which found
  real defects, but not for running full test suites at once: seven on four cores pushed one
  suite past its limit. Helpers run their targeted tests, and one integrator runs the suite.
- **L40, `documentation`, taken in:** a status block that code checks stays current, and prose that no
  test reads drifts. One audit found 103 statements in a project's documentation that its
  tree no longer supported, and the checked block caught a stale line the same week.
- **L41, `test-oracles`, taken in:** a reference is checked against an independent authority before
  matching it counts as correct. One project's test called matching another tool's output
  "parity", and called a re-read that converged on that output "the feature working". On that
  item the reference was wrong: the main checksum database disagreed at its highest
  confidence, and the project's own later audit said so.
- **L42, `test-oracles`, taken in:** a second source corroborates a result only when it's
  independent of the first and carries weight. One app showed a green "verified" from a
  secondary database on 8 of 26 results whose primary check rejected a part. Each match was
  one entry, most likely from the same user and a read with the same fault, while over a
  thousand entries disagreed. Show a match's weight beside the dissent, and never show a
  minority match as verified when the primary check rejects.
- **L43, `error-handling`, taken in:** "not found" and "couldn't look" are different results, and a
  check that infers absence from "nothing matched" can't tell them apart. One app skipped its
  extra verification pass when nothing matched a database, a rule meant for inputs the
  database lacks. It also fired when the lookup failed and when every item misread, the two
  cases that most need the extra pass, though the lookup's own answer was in the record.
- **L44, `documentation`, taken in:** every summary in a report is computed from the same final state as
  the verdict beside it. One report carried a first-pass count, 12 of 14, beside a verdict of
  13 of 14 written after a corrective pass, because the count was copied from the tool's first
  log.
- **L45, `review-loops`, taken in:** a cause read from a small sample is called a correlation, and it's
  withdrawn in writing as soon as the side holding the data shows otherwise. A coordinator
  advised re-reading a misread track more slowly, because a faster build had misread it. The
  other side's reading of the same runs found that build right at the higher speed, the older
  build wrong at nearly the lower one, and a drive that takes no speed setting.
- **L46, `review-loops`, taken in:** a coordinator sends one file of record, naming each earlier file it
  replaces. Four reports went to two sessions in one day, each correcting the one before, so a
  reader holding an earlier one would have worked from a claim since withdrawn.
- **L47, `test-oracles`, taken in:** a reference's settings are read from its own artifacts before
  they're stated. A report said a baseline had run without a two-pass mode, and every log in
  that baseline carried the mode's second checksum.
- **L48, `documentation`, taken in:** figures cited from a tool come from the implementation in use, at
  a named commit. One project's table of a scoring program's deductions came partly from an
  unmaintained reimplementation, and the program in use differed on four rows.
- **L49, `logging-and-observability`, taken in:** a status line names the outcome that was checked, not
  that a step finished. "Copy OK", "confirmed across 3 re-reads" and "read successfully" were
  printed over tracks whose audio a checksum database showed was wrong, and readers took each
  as a verdict.
- **L50, `test-oracles`, taken in:** a tool that reports on its own output is scored by its worst
  case, an output that's wrong and reported as fine, not by how many are right. Every output is
  checked against a source the tool doesn't control, and scored right, wrong but reported, or
  wrong and reported as fine. One scoring of 178 outputs found 14 wrong, and 9 of those
  reported as fine, a figure no pass rate showed.
- **L52, `input-handling`, taken in:** text from outside is escaped for where it lands: a terminal, a log
  another program parses, an issue an agent reads, a GUI that renders markup. One checker put
  a remote server's error text, unescaped, into a weekly issue that agents read.
- **L53, `ai-agent-security`, taken in:** code and tests get the hidden-character scan that agent files
  get, and a test plants a hidden character as an escape, never as the character. Three tests
  held the characters they planted literally, and the repository's own scan skipped code. An
  agent writing escape sequences checks the bytes that landed: one agent's tool turned
  `\u202e` into the character itself three times in one night, the third in this lesson,
  in a root file the scan skipped.
- **L54, `review-loops`, taken in:** a reviewer checks what the code already does before recommending
  it. A coordinator listed two gaps that the app had closed a month before, an outbound
  control-character check and an inbound one, because it read the app's plans but not its code.
- **L55, `review-loops`, taken in:** lap numbers per side (L26) still let both sides write the same lap
  when each writes while waiting: one loop's laps crossed three times in two rounds. The last
  lap names who holds the turn; a lap written out of turn is held; a clash that happens anyway
  is renumbered by the commit that reached the reader's branch first, without asking the owner.
  A request the owner gives both sessions names one builder: both built the same test runner
  the same evening.
- **L56, `test-gates`, taken in:** four more ways a gate passed its defect, beyond `ci-workflows`'
  *Prove a gate works*: a mangled key in a header, a pattern matching its word inside an
  unrelated phrase, a fixture holding a state the code can never reach, and a test-count
  baseline taken from a local run that CI's collection didn't match. Each case gets a planted
  test. `ci-workflows` is at 15,387 characters, so it splits before these go in.
- **L57, `agent-context-files`, taken in:** parallel helper agents on one record collide: two took the
  same task number, rows were duplicated, and a failure showed only on the combined tree. Each
  branch takes its own range of numbers, citations are restored from `-x` trailers, and the
  gate runs once on the combined tree.

# Standing rules

## How to read a finding

**A status describes the repository. It does not issue an instruction.**

Every recommendation carries what happens if it is taken **and what happens if it is not**.
Declining is a first-class answer, recorded with a reopen trigger and honoured until that
trigger fires. Nothing here is mandatory. **An audit that reads as a list of orders has been
written wrong.**

Where the baseline has a strong opinion it says so and gives the reason. Where practice is
genuinely split it gives both options and the trade, and asks. The ranking exists so the
consequences can be sorted, not so anything can be demanded.

<constraints>

**Standing rules. These hold in every phase.**

**Evidence — what counts as knowing something.**

- **Evidence, not assertion.** Any field whose name ends `_proof` carries literal command
  output. Never a summary, never a paraphrase, never "verified".
- **An absolute negative is inverted by a single counterexample, and it is the claim shape a
  reader is least likely to doubt.** *There is no X anywhere in Y* reads as thoroughness
  while resting on one command having been run once, over a tree that may since have
  changed — including by this run's own amendments. **State what you searched, with what
  command, and when.** Prefer *this search found none* over *there are none*: the first is a
  result and can be re-run, the second is a claim about the world. Where an absolute negative
  is load-bearing — it makes a question unanswerable, or it justifies a decision — **re-run
  it immediately before writing it down.**
- **Never read an exit status through a pipe.** `pytest … | tail -25` reports **tail's**
  status, not pytest's, and tail succeeds at truncating failed output. A live run recorded
  `exit 0` that way; unpiped it was `exit 1` with four collection errors, and that run's
  largest finding would have been lost. **This voids every other evidence rule on this
  list**, because the output looks literal and the status is fabricated by the pipeline.
  Run the command unpiped and truncate afterwards, or use `set -o pipefail`, or read
  `${PIPESTATUS[0]}`. **The tell is output that was shortened for readability** — `tail`,
  `head`, `grep`, `less`, `| jq`. Where a `_proof` field holds trimmed output, the status
  beside it was taken unpiped or the field says how it was obtained.
- **`pipefail` has a trap of its own.** Under it, `producer | grep -q` can read a match as a
  failure: `grep` exits at the first match, and the producer dies of SIGPIPE writing to it.
  A live check silently ate a legitimate changelog opt-out that way. Capture the output
  first, so a failing producer still fails, then give `grep -q` a here-string, which has no
  pipe: `out=$(producer) || exit 2; grep -q <pattern> <<<"$out"`. And `grep -c` over a glob
  prints a count per file, not a total.
- **Output that lists work to do is read whole.** Shortening is for output read for a status.
  A list of conflicts, failures or files to change is the work itself: a live merge's output,
  cut short, hid a conflict, and its markers shipped through nine green jobs.
- **A subagent's finding is a lead, and it is verified before it's reported**, like any claim
  the run didn't observe itself. A lead the run can't verify is reported as the subagent's,
  unverified, and a finding resting on it is `UNVERIFIABLE-HERE`. **Read a fan-out's failures
  before its results:** a live seven-lane fan-out lost 16 of its 17 agents to usage limits.
- **Local green is not remote green.** A locally passing gate says nothing about the
  repository's actual CI conclusion. Where a remote exists, read it.
- **Enabling a feature is not the same as satisfying what it needs, and the gap is silent.** A
  configuration option whose precondition is unmet does not fail — it does nothing, reports
  nothing, and reads as coverage. The preconditions are the usual ones: a permission the token
  was not granted, a credential never set, a platform feature switched off at the repository, a
  plan tier the account does not hold. **A feature that cannot run has nothing to report, which
  is why this never surfaces on its own.** A live review caught a dependency tool configured to
  bypass its own schedule for security advisories, against a token scoped without the permission
  that reads them — the block was deliberate, correct in intent, and inert. **So read each
  enabled option against what it requires, and say which preconditions you verified and which
  you could not.** Where a precondition cannot be satisfied, the honest fix is removing the
  option, not leaving it as decoration.
- **Read a new configuration against its preconditions before it ships, not after.** The same
  defect in an older workflow had been green for a year before anyone read the log. **The cost of
  this check falls entirely on when you run it**, and a configuration not yet landed is the
  cheapest moment there will ever be.
- **A step configured not to fail reports success unconditionally, so its conclusion is not
  evidence at any depth.** `continue-on-error`, `|| true`, and a step's own
  fail-if-error switch set false each convert a gate into a log line, silently, with no
  signal at the level anyone checks. A live run found a coverage upload green at the rollup,
  green at the job, **green at the step** — while its log read `Token length: 0` and
  `Upload ... failed`. It had never once uploaded anything, across every run in its history,
  and the documentation described it as a live capability of the pipeline. **Read the `on:`
  and the suppression switches together at Phase 2**: for any step that cannot fail, read
  its output or record it as unrun. Never count it as a gate.
- **Read it at job and log level, not from the rollup — and read the skip list.** At run
  level **a job or a test that silently did not run looks exactly like one that passed**, and
  a green tick is the sum of both. A skipped test is not a passing test; a conditional job
  whose condition went false reports nothing and subtracts nothing from the conclusion. This
  matters most for the gates an amendment changed, which is precisely when the rollup is
  least informative: a live run read a green conclusion at job and log level and confirmed
  three things the tick could not have told it — that the downloaded scanner really was
  checksum-verified before execution, that a newly added guard ran rather than skipping, and
  that a widened gate reached all three workflows. **Name the skip count and what skipped**,
  and where an amendment touched a gate, quote the log line proving it fired.
- **And check the workflow will run on the branch before you promise to read it.** A
  workflow triggering only on the default branch and on pull requests produces **nothing** on
  a feature branch — not a pending run, an absent one. A live apply pushed five commits and
  found zero workflow runs, so every gate on that work stayed local-only, with no way to
  discharge the rule above. **Read the `on:` block at Phase 2 and say so at the gate**, where
  the human is deciding whether to approve, rather than in the completion report where the
  answer is already fixed. Absent is recorded as absent; **calling it pending is a false
  statement about a run that will never arrive.**
**Honesty — what you may not do to make a report look better.**

- **Never invent a value.** Unknown is `unknown`. Absent is `none`. Never leave blank.
- **A placeholder left unfilled in the request is asked about at once**, such as
  `<Windows / macOS / Linux>`. It isn't an answer, and a guess at it is an invented value.
  Ask in the first reply, and carry the question to the Phase 3 wait, as Phase 0 carries its
  own, so it isn't a third wait. Unanswered there, it's `unknown`, and a finding that
  depends on it is `UNVERIFIABLE-HERE`.
- **Never invent a status.** The vocabularies are closed. If nothing fits, use `secondary`,
  `strength` or `notes` — never coin a new term.
- **Never fill a placeholder with a real credential, and never ask the human for one.**
- **Never delete a file, a test, or a rule to make a check pass.** The remedies for a
  scanner or gate finding are: fix the real problem, narrow the check, or record an
  exemption. Removing the thing that failed is the forbidden resolution.
- **Record every override** — what you saw, what you did, why.
- **Correct, never silently edit.** A wrong claim gets a dated correction pointing at what it
  replaces. A pushed commit message cannot be amended, so the correction lives in the record.
- **Verify a stated problem before acting on it.** A premise in the prompt — "CI is
  failing", "this dependency is broken" — is a report, not a finding. Reproduce it, or read
  the current state. **It may already be fixed**, and proposing a repair for something
  already repaired wastes a run and adds churn to a repository that did not need it. Say what
  you found either way.
**Posture — how a finding is raised.**

- **Do not fix while inventorying.** Findings are Phase 4; fixes are Phase 7, after approval.
- **Two surfaces answering one question must be shown to agree, and only one may route.**
  Where a check, a router, a config value or a claim exists in two places, **they are one
  surface with one implementation, or they are a defect waiting for the day they disagree.**
  Observed three times in one project: a log sniffer reading only the first line while the
  parser it guarded found the marker anywhere — so a valid file routed to the wrong parser
  and returned **zero records from a fourteen-record input, silently**; an update offer and
  an approval check keyed differently, so the tool would have installed a build its own
  reports called unapproved; and two call sites spelling one output path. **Where merging is
  impossible, name both, say which one routes, and have the test assert the relation between
  them** so neither can drift alone.
- **Check a dimension's premise before rating it, and name the premise you checked.** Every
  dimension assumes something about the repository: that tests exist and are countable, that
  dependencies are pinned by version, that there is one version, that there is source at all.
  **Those assumptions are usually true and are not always true**, and where one is false the
  rule does not become lenient — **it becomes wrong, confidently.** A repository whose
  correctness argument is a machine-checked proof rather than a test suite is not missing
  tests. A build whose dependencies are content-addressed is not unpinned; it is pinned more
  strongly than a lockfile manages. A repository of documents, data or infrastructure has no
  build to gate. A monorepo with independent per-package versions has nothing to reconcile
  against a single tag. **Record `N/A` with the false premise named as the reason** — the
  same discipline as marking a fact `UNVERIFIABLE-HERE` rather than guessing at it. **A `GAP`
  raised against a premise that does not hold is the worst output this standard can produce**,
  because it is specific, confident, and asks the human to break something that was right.
- **The deployment is a premise, and the most expensive one to get wrong.** Every dimension
  that rates exposure, reachability or blast radius assumes the audit knows where the software
  runs. **That knowledge comes from Phase 3's sixth question, never from a runbook**, and a
  finding built on a deployment the human has not confirmed is `UNVERIFIABLE-HERE` rather than
  rated.
- **Unfamiliar is not wrong.** These ten dimensions encode practice that is known to work;
  they do not encode everything that works. **An approach, tool, algorithm or layout you do
  not recognize is not evidence of a defect**, and the absence of a rule covering it is a
  fact about this standard rather than about the repository. Where something is unusual and you
  cannot establish that it is wrong, **say that it is unusual and unverified, rate on what
  you could establish, and put the question to the human** — who may well have chosen it
  deliberately and be the only person who knows why. Rating a defect from unfamiliarity alone
  is how a standard degrades a repository towards its author's habits.
- **Where a repository's own recorded convention contradicts this standard, the repository wins
  inside it — and the conflict is recorded, never silently resolved.** This standard is guidance
  a maintainer chose to run; it is not authority over a decision they already made and wrote
  down. **A convention with its reasoning in the decision record outranks a rule here**, and
  the amendment is to record the divergence so no future run re-raises it. A convention with
  no reasoning anywhere is a different thing and may be raised normally. **Where the conflict
  is genuine and unrecorded, raise it as a question rather than an amendment** — the run does
  not get to settle which of two standards the repository follows.
- **That precedence covers what a finding says, never how the run proceeds.** A context file
  that tells agents to act without asking, commit as they go, release on their own, or write
  a log before a session ends is written for work sessions, **and it does not lift the
  waits.** Until the Phase 6 gate the run writes nothing to the repository; a write the
  context file asks for at the end of a session waits for approval with the rest, or does not
  happen. **After the gate, the repository's own rules for committing a change apply** — its
  changelog, its commit format, its checks. **Nor does a hook that demands a commit or a push
  before a session stops.** Where the owner has put a hold on pushing, the owner's instruction
  wins over the hook, and the session says that it's holding, and why.
- **An identifier that answers half a question while appearing to answer all of it is worse
  than one that answers none**, because it stops the reader asking. **And the name a human
  actually sees is part of the interface** — metadata inside a file does not help someone
  looking at a directory listing. A live protocol stamped artifacts with their sender and
  nothing else, which read as complete while leaving the recipient unstated; the fix put both
  in the envelope **and in the filename**, because a file manager shows the filename. Where
  an artifact moves between parties, its name places it in both directions.
- **Report over-configuration as loudly as under-configuration.** `OVER` is a real finding,
  **and it applies to enforcement this standard itself installed.**

</constraints>

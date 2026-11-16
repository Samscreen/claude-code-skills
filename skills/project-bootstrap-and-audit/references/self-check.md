# Conformance self-check

**Emit this at the end of every run, after the last phase block, whatever the job was.**

<constraints>

**This exists because the same standard is run on different models, and they fail differently.** A
report that looks complete tells you nothing about whether the rules were followed; this block
makes the common failures visible in one place, cheaply. **It reports on the run, not on the
change**, so it doesn't replace the second reader Phase 9 asks for.

**Answer from what you actually did, not from what the standard says to do.** A `yes` that
means "the instruction was there" rather than "I did it" makes this block worse than absent —
it manufactures assurance. **Where the honest answer is `no`, that is a useful run**, and the reason
belongs beside it.

**Never pre-fill this from the template.** Each line is checked against the run that
happened.

</constraints>

```yaml
conformance:
  standard_version: "<metadata.version, read from the frontmatter>"
  standard_sha256: "<Step 0's files-sha256, or the sha256 of the one file this run read | unknown>"
                                        # shows which bytes ran
  job: <survey | choose | set up | audit | release | prune | validate>
  sections_read: [<by name>]
  sections_skipped: [<by name>]

  # Structure
  ten_statuses_emitted: yes | no | n/a  # exactly ten, numbered 1-10; n/a when no Phase 4 ran
  tally_sums_to_ten: yes | no | n/a
  new_vocabulary_coined: no | "<what was invented, if any>"
  fields_added_beyond_schema: no | "<which>"

  # Gates
  waits_observed: <int>                 # 2 on a full run OR an audit stopping at the gate;
                                        # 1 on a survey, or on a run that stops at Phase 3.
                                        # An unattended run's Phase 3, met by answers
                                        # given in advance, counts.
                                        # Count a wait when you STOP at it —
                                        # arriving at Phase 6 and stopping is observing it,
                                        # not skipping it. Two runs disagreed on this.
  wrote_before_approval: no | "<what, and why>"

  # Evidence
  proof_fields_hold_literal_output: yes | no | n/a
  unverified_facts_relied_on: [<any dated fact used without checking it>]
  premise_verified: yes | no | n/a      # a claim in the prompt was reproduced, not assumed
  second_reader: yes | the human | no | n/a   # Phase 9's review; n/a when nothing was applied

  # Posture
  amendments_pre_selected: no | yes
  both_consequences_on_every_amendment: yes | no
  actions_requiring_a_local_clone: <int>   # must be 0 where Phase 0 recorded no local copy
  declines_reproposed_without_a_fired_trigger: <int>   # must be 0

  # Delivery
  report_written: <path>
  report_handed_over: yes | no          # attached or reproduced in the reply, this turn

  deviations: <int>                     # each one present in `overrides`
  honest_summary: "<one sentence: where this run was weakest>"

  # Optional, and the only part of this standard that reports back on the standard itself.
  # Omit the key entirely rather than emitting it empty.
validated:
  - {rule: "<the rule, quoted from this standard>",
     caught: "<what it found in this repository that reading would not have>"}
constrained:
  - {rule: "<the rule, quoted from this standard>",
     stopped: "<what you were about to do, and did not>"}
corrections:
  - prior_run: "<standard version and date, or 'this run' with the phase>"
    prior_claim: "<what was asserted, quoted>"
    actual: "<what is true, and the evidence>"
    rule_that_caught_it: "<the rule, or a gap where none exists>"
    decision_affected: yes | no
```

## The three optional blocks, and why they exist

<constraints>

**`validated` is how this standard learns which of its rules earn their place.** Every rule here
was added because something went wrong once, and **nothing currently records whether a rule
has ever caught anything since.** A rule that catches nothing across many runs is `OVER` by
this standard's own logic and should come out — but that judgment needs evidence, and this block
is the only place it accumulates. Quote the rule and say what it found **that reading the
repository would not have.** Three or four entries, not a transcript; a run that lists every
rule it followed has recorded compliance rather than value.

**`constrained` exists because `validated` alone would get the pruning exactly wrong.**
Sixteen `validated` entries across three live runs credited execution rules almost without
exception — and that is not because the other rules are worthless, it is because **the
instrument can only see rules that catch.** Every posture rule constrains instead of
detecting: do not pre-select an amendment, both consequences on every one, two waits, never
substitute at apply time, re-ask a blank rather than defaulting. **None of them can ever
appear in `validated`, and they are the rules that make the output trustworthy.** Pruning on
detection alone would keep every rule that finds bugs and delete every rule that keeps a run
honest.

**So record what a rule stopped you doing.** Live runs have produced these already, in prose
where nothing could count them: re-asking a blank answer instead of taking the default,
refusing to infer an approval from detail the human had written out but not listed, and —
after a force-push was denied — verifying the branch relationship rather than retrying the
command. **The moment worth recording is the one where you were about to do something and a
rule stopped you**, which is invisible in any output that only reports what happened.

**`corrections` is for a claim this run or an earlier record got wrong.** Not a finding about
the repository — a finding about the report. It exists because a withdrawn or mistaken claim
otherwise vanishes silently, and a decision record that quietly overwrites its own history is
the thing append-only was meant to prevent. **The entry stays even when `decision_affected`
is `no`**, because an overconfident claim that changed no rating still misleads the next run
that reads it. Where no rule caught the error, say so in `rule_that_caught_it` — a gap named
is the most useful thing a run can send back.

**Emitting any of these is a schema addition, so `fields_added_beyond_schema` says `yes`
and names them.** A run that adds a block and reports no additions has contradicted itself in
the one field that exists to catch that, which a live run did.

</constraints>

## What a failing line means

| Line | If it comes back wrong |
|---|---|
| `tally_sums_to_ten` | Phase 4 did not finish. Recount before emitting anything else — this has been wrong twice, both times by inventing a combined status for a dimension that was partly fine |
| `new_vocabulary_coined` | The vocabularies are closed. Use `secondary`, `strength` or `notes` and re-emit |
| `waits_observed` | Fewer than two on a full run means a gate was skipped, and a gate skipped is approval assumed. More than two means waits were invented, which costs the human round trips the file could have answered |
| `actions_requiring_a_local_clone` | Where Phase 0 recorded no local working copy, anything above zero is unusable by a maintainer who has none: rewrite each as a browser action or a dispatch job. Where it recorded one, count the actions with no browser route; the count is reported, not failed |
| `declines_reproposed_without_a_fired_trigger` | The re-check obligations were not honoured, and the decision record is being ignored. This is the failure that makes people stop reading the gate |
| `report_handed_over` | A report written to an ephemeral container and not handed over is the same as no report, and it is the one artifact with no copy anywhere else |
| `unverified_facts_relied_on` | Not a failure by itself. **A non-empty list with no matching `UNVERIFIABLE-HERE` in the findings is** — it means a dated fact was used as though it had been checked |

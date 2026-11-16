# Run report skeleton

The shape of `RUN-REPORT-<repo>-<YYYY-MM-DD>.md`, the one file every run writes outside the
repository and hands over, whatever the job. `SKILL.md`'s *The report* gives the rules, and
`report-schema.json`, beside this file, names each block's fields. Copy what's below the line,
fill it in, and leave out the parts the job doesn't reach.

---

# Run report for <owner/name> on <YYYY-MM-DD>

```yaml
lifecycle: transient
expires: <YYYY-MM-DD>
standard: PROJECT-BOOTSTRAP-AND-AUDIT v<metadata.version>
tool: <agent, surface and version>
repository: <owner/name> @ <commit>
job: <survey | choose | set up | audit | release | prune | validate>
mode: <greenfield | retrofit | audit | recheck>
tier: <T0-T3> (blast radius <B>, audience <A>, basis <current|imminent>)
tally: {BLOCKER: 0, DRIFT: 0, GAP: 0, OVER: 0, MIRROR: 0, UNVERIFIABLE-HERE: 0, OK: 0, N/A: 0}
capabilities_absent: [<what the environment could not do>]
deviations: <count>          # rules not followed as written, each in `overrides`
decisions_open: <count>
sections_read: [...]
sections_skipped: [...]
```

## Decisions

<At the Phase 3 wait: the questions asked, each with its draft and evidence, and any
recommendation still waiting on a pick. The header's `tally` reads `not yet rated`.>

<At the Phase 6 gate: the three lists, in the order the standard's Phase 6 gives them.>

<After Phase 9: in place of the lists, the outcome summary `SKILL.md` describes.>

## Appendix of emission blocks

<Every block the run emitted, verbatim and in order, each in its own `yaml` fence: `phase: 0`,
then each phase after it, up to the one the run stopped at; after Phase 9, a `post_gate` block
for any work asked for after the gate; and last, the conformance self-check, with any of its
three optional blocks in the same fence.>

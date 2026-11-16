# Vocabularies

**Closed sets, with precedence, and both are counted.**

## Agent-layer terms

The body uses these names; *Any agent, any tool* maps each to a filename per tool. Shell
blocks in this standard name Claude Code paths because a command must be concrete —
substitute your tool's and record the substitution.

| Term | What it is |
|---|---|
| **context file** | The canonical, portable project context. `AGENTS.md` |
| **tool shim** | A per-tool file that imports the context file and holds only what cannot be portable |
| **scoped rules** | Rules loaded per file or per path rather than every session |
| **enforced layer** | Permission configuration the tool obeys mechanically. **Not available on every tool** |
| **tool-server config** | Committed external-tool configuration, where the tool supports it |

## Dimension status

Exactly one `status` per dimension, plus any `secondary` entries and an optional `strength`.

<!-- WHY OVER is first-class: a solo project fails from configuration nobody maintains far
     more often than from configuration nobody wrote. Removing OVER makes this a ratchet that
     only ever adds. It applies to rules this standard installed, too. -->
| Precedence | Status | Meaning |
|---|---|---|
| 1 | `BLOCKER` | A live exposure, or a check reporting success while measuring nothing. Ranked first for what it risks — the ranking is information, never an order |
| 2 | `DRIFT` | Configured, but no longer matches reality. Actively misleading |
| 3 | `GAP` | Missing something this tier warrants |
| 4 | `OVER` | Heavier than this tier warrants |
| 5 | `MIRROR` | Source of truth is outside the repository; unverifiable by design |
| 6 | `UNVERIFIABLE-HERE` | Cannot be established from this environment |
| 7 | `OK` | Present, correct, proven by output |
| 8 | `N/A` | Does not apply — by tier, by plan, **or because the rule's premise is false for this repository** |

<!-- WHY the closure rule: two early runs emitted 12 and 11 statuses for 10 dimensions, one
     by inventing `OK-with-gap` for a dimension that was partly fine. A count that need not
     balance hides both. Do not relax this to "roughly one per dimension". -->
**Closure rule.** Phase 4 emits exactly ten primary statuses, numbered 1–10. **If the tally
does not sum to ten, the phase failed — recount.** Secondaries and strengths are never counted.

<!-- WHY strength exists: precedence carries only the worst finding, so a repository with an
     excellent suite and one missing file reported as ten bare GAPs, and the run had to write
     a paragraph arguing against its own table. This field replaces that paragraph. -->
**`strength` is required wherever a dimension is materially better than its status implies.**
Precedence carries only the worst finding; without `strength` a report misrepresents the
repository and forces prose apologia the schema exists to remove.

## Command result

| Result | Meaning |
|---|---|
| `PASS` | Ran, exit 0 |
| `FAIL` | Ran, non-zero exit |
| `UNVERIFIABLE-HERE` | **Cannot** run here — no network, no daemon, needs a credential, wrong host OS, a side effect outside the container, or the session refuses it |
| `NOT-RUN-HERE` | **Could** run, but could not finish in the time the run had |

**A command the session refuses is `UNVERIFIABLE-HERE`**, whether its permission layer or
the enforced layer refused it, and the refusal is recorded as it was worded. **Never re-spell
the command to get past a refusal**, for the reason the deny layer is never routed around.

**A command whose exit status is its report is not a gate, unless a workflow gates on it.** A
status check that exits 1 while something is open, or `git diff --exit-code` asking whether
anything differs, answers a question rather than passing or failing. Record its answer in the
phase block's `notes`, not in `commands`, so the tally doesn't count a failure that isn't
one. Where a workflow does gate on its exit, it is a gate like any other, and it goes in
`commands` with its result.

## Amendment severity

`recommended` or `optional`. **Nothing else.** Severity records how strongly the baseline
argues for something — it is never an instruction, and it is not a dimension status. An
amendment on a `BLOCKER` dimension is `recommended`; it does not have severity `BLOCKER`.

**Every amendment carries `if_accepted` and `if_declined`.** A recommendation without the
consequence of refusing it is an order wearing a suggestion's clothes.

# Environment — detected, not assumed

<constraints>

**None of this is universal. Detect it, or ask.** The table below is what the standard was
built against; another maintainer, tool or plan will differ, and **a constraint assumed wrong
produces advice that cannot be followed.** Phase 0 establishes the real answers and records
them. Where a capability cannot be determined, it is `unknown` and becomes a human question —
never a guess.

</constraints>

| Fact | How it is established | If it holds |
|---|---|---|
| **Ephemerality** — only the repository is present | Assume true unless the tool says otherwise | Anything uncommitted does not exist |
| **Shell available** | Try one harmless command | **Without it, Phase 2 cannot execute documented commands.** Record them unrun; everything becomes `UNVERIFIABLE-HERE` and the run says so in its headline |
| **Writes outside the repository** | Try writing to a scratch path | **Without it, greenfield cannot build-then-copy and the run report has nowhere to live.** Emit the report in the reply and say why |
| **Remote CI readable** | Try reading a conclusion | Without it, "local green is not remote green" cannot be discharged. Record `unverifiable` |
| **Tag creation** | Try, or read the tool list | Where refused, tagging is a human action via the host UI or a dispatch job, and from T2 the job, which can make the tag annotated — **never "tag locally"** |
| **Local working copy exists** | **Ask. It cannot be detected** | Without one: no local tagging, no desktop tooling, and **client-side hooks gate nothing**, because every commit comes from an ephemeral container. A committed SessionStart hook (Claude Code only) installs them in agent sessions only, and CI stays the gate |
| **Enforced layer** | See *Any agent, any tool* | Where the tool has none, dimension 6 is `N/A`, never `GAP`, and the guarantee moves server-side |
| **Branch protection available** | Read the plan, or ask | Unavailable on private repositories on free plans — **and rulesets carry the same gating**, so the newer mechanism is not an escape. Where unavailable, `N/A` with the reason — never a `GAP` re-proposed every run |
| **Third-party repositories readable** | Try one | Often scoped to the maintainer's own. An upstream fix status is then `unverifiable`, **never "no fix coming"** |
| **Clock agreement** | Compare `date -u` with `git log` | They can differ by days. Record both; anything written takes the session date |

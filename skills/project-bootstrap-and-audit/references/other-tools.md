# Other tools

Read this when the skill runs on a tool other than Claude Code, or on a model other than the one
it was written against. It says how to run the skill there, and lists each Claude Code-only
feature the skill's own files use, with what it does and what to do without it. The standard
file's *Any agent, any tool* maps the paths and files its phases name, tool by tool.

## Running the skill elsewhere

- **The skill is a folder:** `SKILL.md`, `references/`, `assets/` and `scripts/`. A tool that
  reads files runs it when told to read `SKILL.md` first and follow it. A chat that can't read
  a folder takes the release's `KICKSTART.md`, the whole standard in one file.
- **The frontmatter uses only the six Agent Skills fields,** so the folder uploads as a skill
  wherever Agent Skills are read, claude.ai included.
- **The scripts use Python's standard library only.** Where the tool has a shell with
  `python3`, run them as `SKILL.md` says. Without one, Step 0's copy check and the report check
  can't run: the run says so, as `SKILL.md` directs, rather than skipping them silently.
- **Mark a substitution.** Where this skill names a Claude Code path or feature that the tool
  doesn't have, use its equivalent from the table below, and record the substitution as an
  override.

## Claude Code-only features

| Feature | Where the skill uses it | What it does | Without it |
|---|---|---|---|
| A `` !`command` `` line | `SKILL.md`, Step 0 | Runs the command as the skill loads, and puts its output in place of the line. A synced skill's line runs in a cloud session, and not in a terminal or VS Code session (the standard's *Agent tooling* facts) | The line arrives as text. Run the command yourself from the skill's folder |
| `${CLAUDE_SKILL_DIR}` | `SKILL.md`, Step 0's line | Names the folder that holds `SKILL.md` | Use the folder the skill was given in |
| `/project-bootstrap-and-audit` | `SKILL.md`, how to run it | Starts the skill by name | Tell the tool to read `SKILL.md` and follow it |
| `.claude/settings.json` and its `skillOverrides` | `SKILL.md`, the exclusion list; dimension 4 | Hides a skill from the repository's sessions, synced skills included | The tool's own switch for a skill, if it has one. Otherwise the list is advice, and the run says so |
| A SessionStart hook | *Environment*, local working copy | Runs a command as each session starts, so a committed one installs the repository's client-side hooks in agent sessions | The tool's own start hook or setup step. CI stays the gate either way |
| Permission deny rules and hooks: the enforced layer | *Vocabularies*, the standing rules, dimension 6 | The tool refuses a matching call mechanically | *Any agent, any tool* says which tools have one. Where the tool has none, dimension 6 is `N/A` |

## Running this on a model that is not the one it was written against

<constraints>

**Nothing in this standard requires a particular model or tool.** It names Claude Code paths
because a command has to be concrete, and *Any agent, any tool* maps every one of them. Where a path
does not exist for the tool in use, substitute and record the substitution as an override.

**Three failure modes show up specifically when the model changes**, and they are worth watching
for rather than discovering in the output:

- **Compliance theatre.** The schema is filled, every field is populated, and the content is
  generated rather than observed. **The tell is `_proof` fields holding summaries** — "verified",
  "command ran successfully", "output as expected" — instead of literal output. A proof field
  that has been paraphrased is a fabrication with good manners.
- **Instruction decay across a long run.** Adherence may drop as the session lengthens — one
  study found about 5.6% lower odds of compliance per additional function generated, though as
  an exploratory, non-monotonic finding — which is why there are gates rather than a single
  approval at the end, and why this block sits at the end where any drop is worst. **A
  run that was careful in Phase 2 and loose in Phase 7 is the normal shape of this failure**,
  not an unusual one.
- **Helpful ordering.** Presenting amendments with a recommendation already selected, or
  proceeding past a wait because nothing seemed to be blocking. **Both read as service and are
  the posture this standard exists to prevent.**

**Where a model cannot do something this standard asks for, say so in `degraded` at Phase 0 and
in `deviations` here.** A run that names its own limits is more useful than one that works around
them silently, because the workaround is invisible and the limit is not.

</constraints>

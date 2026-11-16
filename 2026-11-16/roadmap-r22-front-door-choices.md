# The front door: the owner's choices of 2026-10-13

Moved verbatim from `ROADMAP.md` on `main` at commit 32f0549, the list under *The front door*
in *Rebuilding `project-bootstrap-and-audit`*, by the owner's "do all" of 2026-11-16. Each
item records a choice the owner made on 2026-10-13. The items still open, *When it loads*,
*A new project's recommendation* and the tests in the owner's browser, stay on `main`.

  - **Which copy ran:** the reference file's SHA-256 in `SKILL.md`'s metadata, checked by a
    standard-library script from a `` !`command` `` line, which a cloud session runs for a
    synced skill. The script needs tests of its own, since ruff and coverage don't reach
    `skills/`, and `skillcheck` should compare the hash with the file, so that no release
    ships a mismatch that stops every run. The deeper pass keeps the uploaded skill thin
    instead: it fetches the reference at a pinned commit with `curl` and hashes that, so the
    pin decides the version, at the cost of a fetch on every run. A hash shows that a copy is
    whole, not that it's current, so the run also compares its version with `main`'s. The
    first pass has it ask whether to go on when `main` is newer, a stop the standard's two
    waits don't include; the deeper pass warns without stopping. **The owner chose on
    2026-10-13:** the hash in `SKILL.md`, checked at the start, and a warning, not a stop.
  - **The questions:** a draft of each answer the repository shows, with its evidence and one
    word of confidence. The first pass asks three outright every run: where it runs,
    production and dependents. The deeper pass asks five, adding work or personal and how long
    it must live, with no answer pre-selected. Every question offers "Not sure", an option is
    marked recommended only beside its evidence, and a re-check asks "Is that still the
    case?" (F38). `AskUserQuestion` takes at most four questions a call, and how it shows in
    the mobile app isn't documented, so the questions also need a numbered list answered in
    one reply. The studies behind these are checked, except the first pass's row 58. **The
    owner chose the five on 2026-10-13.**
  - **Where the answers are kept:** R22 proposes a dated block in the decision record, with no
    addresses, hostnames or names. The run report's Phase 3 block already defines those
    answers' fields, and one schema is easier to keep than two. **The owner chose the run
    report on 2026-10-13.**
  - **Enforcing the waits:** a committed project skill can carry `disable-model-invocation`
    and hooks, and a PreToolUse hook that exits with code 2 blocks the call. The deeper pass
    has Phase 8 offer each repository such a skill after its first approved run, with a hook
    that blocks writes until approval. That puts a skill and a hook into other repositories,
    so it needs a review of its own. **The owner chose on 2026-10-13:** offer it after each
    approved run, and install it only on the owner's yes.
  - **The plugin's version:** Claude Code updates an installed copy only when the version the
    catalog pins changes. It said 0.1.1 from 2026-09-23 until release 0.1.2, so a copy
    installed before v0.37.0 kept v0.36.0 until then. How
    claude.ai decides that a personal marketplace's copy changed isn't documented. By the Help
    Center, an organization's GitHub-synced marketplace syncs when a merged pull request
    changes the version. **The owner chose on 2026-10-13** to keep bumping the version at
    each release, rather than leave it out so that installs follow `main`.

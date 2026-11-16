# Withdrawing a bad skill

If a skill in this repository gives wrong or harmful instructions, take it out of circulation in this order.

1. **Stop new installs.** In one pull request, fix the skill or remove it.
   - To remove it:
     - delete `skills/<name>/`;
     - remove its path from `.claude-plugin/marketplace.json`. If it was its plugin's only
       skill, remove the whole plugin entry, because an entry whose paths all miss loads every
       skill;
     - remove its row from the [README's skill table](../README.md#skills);
     - set its status in `ROADMAP.md` to `building`.
   - Either way:
     - bump `version` in every catalog entry, because installed copies update only when the
       version changes. A fix is a patch release. A removal is a breaking change, and under
       0.x a breaking change is a minor release;
     - add a changelog entry under Fixed, Removed or Security.

   `skillcheck` fails the pull request if the catalog, the roadmap, the README and `skills/`
   disagree.
2. **Merge it, then release it.** The merge is what reaches claude.ai, so a skill change is
   ready for users before it merges. The merge that changes the catalog's `version` is what
   reaches Claude Code plugin installs: an install takes `main` as it stands once the version
   string changes, released or not. The release reaches cloud sessions with `cloud-setup.sh`'s
   hook. Run the Release workflow from the Actions tab, with the new
   version and the merge commit's full SHA, not a branch, before a later commit changes a
   workflow. It checks the version, the changelog and CI, and makes the annotated tag. Then it
   signs the files with a build provenance attestation, checks that signature, and publishes the
   release page, with the kickstart file, each skill packaged for claude.ai, the ruleset files,
   the dependency map and the attestation attached.
3. **Reach the copies already installed.**
   - **claude.ai:** a plugin installed from this marketplace with Sync automatically on takes
     each change once it merges to `main`, released or not. Otherwise, delete or replace the
     uploaded skill under Customize, then Skills. If an admin uploaded it for an organization,
     an admin removes it.
   - **Cloud sessions with `cloud-setup.sh`'s hook:** the next session to start installs the
     newest release, and removes a skill it no longer ships. A session already running keeps
     its copy.
   - **Plugin installs:** a third-party marketplace updates automatically only if the user
     turned that on. Ask users to run these in a terminal:

     ```sh
     claude plugin marketplace update claude-code-skills
     claude plugin update <plugin>@claude-code-skills
     ```

     If the plugin itself was removed, ask them to run
     `claude plugin uninstall <plugin>@claude-code-skills` instead.
   - **Committed copies:** each repository with a copy in `.claude/skills/` removes or replaces
     it.
4. **If it was a security problem,** publish a security advisory from the Security tab, naming
   the affected versions. Rotate anything the skill could have exposed.
5. **Record what happened** in `docs/decisions.md`.

# Command line interfaces

Read this for how a command-line program should behave for the person at a terminal and for the
script that calls it: options and arguments, `--help` and `--version`, output for people against
output for programs, color, prompts, quiet mode, dry runs, saying what changed, secrets, and
which argument parser to use in each language.

A setting the CLI and the GUI share is one setting, by `settings-and-options`. The `coding`
skill holds the rest: exit codes with one meaning each in `error-handling`; the order of flags,
environment and files, and how secrets arrive, in `configuration`; escaping outside text for a
terminal in `input-handling`; each language's argument handling and destructive-command guards
in its language module, such as `bash-security` or `powershell-scripts`.

## Rules

1. **Follow POSIX's utility syntax, with GNU's additions.** Options are single characters that
   group (`-xvf`), and the first `--` ends them (fact `cl-posix-syntax`). Every program takes
   `--help` and `--version`, and each short option has a long name (fact `cl-gnu-options`).
2. **`-h` and `--help` print full help on stdout and exit 0,** whatever else is on the line
   (facts `cl-gnu-options`, `cl-clig-output`).
3. **Primary output goes to stdout; messages, progress and errors to stderr** (fact
   `cl-clig-output`). A pipe then carries data only.
4. **Give scripts a machine-readable form,** `--json` or one record per line, and treat it as an
   interface (fact `cl-clig-output`). The format for people may change; that one doesn't.
5. **Color is for a person:** off when the stream isn't a terminal, when `NO_COLOR` is set and
   not empty, when `TERM` is `dumb`, and when `--no-color` is passed (facts `cl-clig-color`,
   `cl-no-color`). Check stdout and stderr separately. Don't add CLICOLOR (fact `cl-clicolor`).
6. **Prompt only when stdin is a terminal, and never require a prompt** (fact
   `cl-clig-prompts`). Every answer has a flag; without a terminal, fail and name the flag.
7. **Say what changed; offer `-n`/`--dry-run` wherever state changes, and `-q` for the rest**
   (fact `cl-clig-state`). A destructive command asks at a terminal, or needs `--yes` or
   `--force` in a script.
8. **Never read a secret from a flag** (fact `cl-clig-secrets`): take a file path, such as
   `--password-file`, or stdin.
9. **Exit 0 on success, and give each other code one meaning,** by `error-handling` (facts
   `eh-posix-grep`, `eh-posix-127`, `sh-signal-status`, `eh-sysexits`).
10. **Parse arguments with the language's maintained parser, at a current version,** below. It
    writes help, rejects unknown options and handles `--`.

### Parsers by language

| Language | Parser | What to know |
|---|---|---|
| Python | `argparse` | 3.15 suggests the option meant for a mistyped one by default; help is colored since 3.14; `FileType` is deprecated (facts `cl-argparse-315`, `cl-argparse-color`) |
| Python | Click | 8.3.3 or later: CVE-2026-7246 is disputed, but scanners flag older releases (facts `cl-click`, `cl-click-cve`) |
| Python | Typer | Vendors its own Click since 0.26.0, so Click isn't installed with it and Click-specific extensions stopped working (fact `cl-typer`) |
| Rust | clap | 5.0's breaking changes wait behind `unstable-v5` (fact `cl-clap`) |
| Go | cobra | Fact `cl-cobra` |
| .NET | System.CommandLine | 2.0.x and 3.0.0 are both stable (fact `cl-scl`); 2.0's API is `SetAction` and `ParseResult` (fact `cs-commandline-api`) |
| Node.js | commander; `util.parseArgs` for a small tool | commander 15 needs Node 22.12.0 (facts `cl-commander`, `js-parseargs`) |
| Bash, PowerShell | `getopts`; a `param()` block | Their language modules; `-WhatIf` is PowerShell's dry run |

### Color, in Python

```python
import os


def use_color(stream, no_color_flag: bool) -> bool:
    """Color only for a person at a terminal who hasn't turned it off."""
    return (
        not no_color_flag
        and stream.isatty()
        and not os.environ.get("NO_COLOR")  # any value but "" turns color off
        and os.environ.get("TERM") != "dumb"
    )
```

## Mistakes

- **System.CommandLine beta code,** `SetHandler`, `InvocationContext` and `CommandLineBuilder`,
  which AI assistants still write. 2.0 uses `SetAction` and `ParseResult` (fact
  `cs-commandline-api`).
- **Reading `NO_COLOR=0` as "color on".** Any non-empty value turns color off; an empty one
  doesn't count (fact `cl-no-color`).
- **A prompt in a program CI runs.** It waits forever. Fail at once, naming the flag.
- **`--password` or `--token` flags.** Any user on the machine can read a process's command line
  (fact `sh-cmdline`).
- **Log lines in `--json` output on stdout.** The consumer's parser fails.
- **Help on stderr with a failing exit when the person asked for it.** That's for a usage error.
- **Importing `click` in a Typer project without declaring it.** Typer no longer pulls it in.
- **`argparse.FileType` in new code.** It's deprecated (fact `cl-argparse-315`); open the file
  where it's used.

## Audit

Severity uses the standard's status words.

| Check | Look for | Severity | Fix |
|---|---|---|---|
| Help and version | `prog --help`, `prog -h`, `prog --version`: stdout, exit 0 | `GAP` | The parser's help and version actions |
| Pipes carry data only | `prog ... 2>/dev/null \| head`: no messages or color codes | `DRIFT` | Messages to stderr; check each stream |
| Color opt-outs | `NO_COLOR=1`, `TERM=dumb`, `--no-color`, a pipe: no escape codes | `GAP` | Rule 5's four checks |
| Machine-readable output | `--json` or line-per-record mode in a tool scripts call | `GAP` where scripts parse text for people | Add one; keep it stable |
| Prompts without a terminal | `prog ... </dev/null` fails at once, naming the flag | `BLOCKER` where CI or a scheduler runs it | A flag for every answer |
| State changes | A write or delete with no dry run, or that ends silently | `GAP` | `--dry-run`, and a line saying what changed |
| Secrets in flags | `password`, `token`, `secret` or `key` in option names | `BLOCKER` | A file option or stdin |
| Parser versions | Click below 8.3.3; System.CommandLine betas; commander 15 on older Node | `DRIFT` | Upgrade, with the API changes above |
| Hand-rolled parsing | `sys.argv`, `os.Args` or `$1` read directly beyond one argument | `GAP` | The language's parser |

## Why

### Option syntax

- **The advice:** POSIX's grouping single-character options and `--`; GNU's `--help`,
  `--version` and long names.
- **The reason:** people and scripts type a new tool the way they type `ls` and `grep`. Breaking
  the pattern costs a trip to the help, and a file named `-r` needs `--`.
- **What others do:** GNU's getopt accepts options after operands, which POSIX doesn't specify
  (fact `cl-gnu-options`). clig.dev asks for order-independent flags where possible.
- **What it costs:** two names per option, kept in step with the help.
- **When to choose differently:** a PowerShell cmdlet follows PowerShell's conventions, and a
  portable `sh` script can't count on options after operands.

### Output for people and for programs

- **The advice:** data to stdout, the rest to stderr, a stable machine form, and color and
  prompts only for a person.
- **The reason:** a script reads stdout. Color codes and progress corrupt it, and a question
  waiting on stdin hangs it. Messages on stderr stay on screen in a pipe.
- **What others do:** `NO_COLOR` is the opt-out tools settled on (fact `cl-no-color`);
  CLICOLOR's authors point to it and `FORCE_COLOR` (fact `cl-clicolor`). clig.dev adds
  `TERM=dumb`, `--no-color` (fact `cl-clig-color`) and a `--plain` mode beside `--json`.
- **What it costs:** two output paths to test, and a JSON shape that can only grow.
- **When to choose differently:** a full-screen program, such as an editor, owns the terminal,
  and refuses to start without one.

### Dry runs, quiet mode and secrets

- **The reason for dry runs:** a person can't check what they didn't see, and a dry run shows a
  destructive command's reach first. `usability-review` shares the aim: undo where possible,
  confirmation where not. The cost: the dry run must take the real path up to the write.
- **The reason for no secrets in flags:** a command line reaches `ps`, `/proc` and shell history
  (fact `sh-cmdline`). clig.dev also advises against environment variables for secrets (fact
  `cl-clig-secrets`), which `configuration` allows; a file or stdin satisfies both.

### Current parsers

- **The reason:** a parser gives help, suggestions and `--` handling that hand-rolled code gets
  wrong, and the parsers move: Typer dropped Click as a dependency (fact `cl-typer`),
  System.CommandLine changed its API before 2.0 and shipped 3.0 (fact `cl-scl`), and clap has
  5.0 queued (fact `cl-clap`).
- **What it costs:** a dependency, except for `argparse`, `getopts` and `util.parseArgs`.
- **When to choose differently:** a one-argument tool can read its argument directly, and still
  answers `--help`.

## Facts

Versions, dates and guidance, each named elsewhere by its ID.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `cl-posix-syntax` | POSIX.1-2024: one-character options, grouping, `--` ends options | [POSIX.1-2024, chapter 12](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html) | "Each option name should be a single alphanumeric character" and "grouped behind one '-' delimiter." and "a delimiter indicating the end of options." | 2026-11-16 | 2027-05-16 |
| `cl-gnu-options` | GNU: `--help` and `--version` everywhere, help on stdout and exit 0, long names; options after operands are a GNU extension | [GNU Coding Standards, Texinfo source](https://raw.githubusercontent.com/coreutils/gnulib/master/doc/standards.texi) | "All programs should support two standard options:" and "on standard output, then exit successfully." and "equivalent to the single-letter Unix-style options." and "This is not what POSIX specifies; it is a GNU extension." | 2026-11-16 | 2027-05-16 |
| `cl-no-color` | `NO_COLOR` set and not empty turns color off | [no-color.org](https://no-color.org/) | "when present and not an empty string (regardless of its value), prevents the addition of ANSI color." | 2026-11-16 | 2027-05-16 |
| `cl-clicolor` | CLICOLOR is deprecated | [bixense.com](https://bixense.com/clicolors/) | "This standard is deprecated." | 2026-11-16 | 2027-05-16 |
| `cl-clig-color` | clig.dev: color off for `NO_COLOR`, `TERM=dumb`, `--no-color` | [clig.dev](https://clig.dev/) | "The NO_COLOR environment variable is set and it is not empty (regardless of its value)." and "has the value dumb." and "The user passes the option --no-color." | 2026-11-16 | 2027-05-16 |
| `cl-clig-output` | clig.dev: output to stdout; JSON on `--json`; help on `-h` and `--help` | [clig.dev](https://clig.dev/) | "The primary output for your command should go to stdout." and "Display output as formatted JSON if --json is passed." and "Show full help when -h and --help are passed." | 2026-11-16 | 2027-05-16 |
| `cl-clig-prompts` | clig.dev: prompts only at a terminal, never required | [clig.dev](https://clig.dev/) | "Only use prompts or interactive elements if stdin is an interactive terminal (a TTY)." and "Never require a prompt." | 2026-11-16 | 2027-05-16 |
| `cl-clig-state` | clig.dev: `-q`, report changes, dry run | [clig.dev](https://clig.dev/) | "provide a -q option to suppress all non-essential output." and "If you change state, tell the user." and "describe the changes that would occur" | 2026-11-16 | 2027-05-16 |
| `cl-clig-secrets` | clig.dev: no secrets from flags or environment variables | [clig.dev](https://clig.dev/) | "Do not read secrets directly from flags." and "Do not read secrets from environment variables." | 2026-11-16 | 2027-05-16 |
| `cl-argparse-315` | Python 3.15 (2026-10-09): argparse suggestions on by default; `FileType` deprecated, no removal version | [What's new in 3.15](https://docs.python.org/3/whatsnew/3.15.html) | "Changed the suggest_on_error parameter of argparse.ArgumentParser to default to True." and "The argparse.FileType type converter is deprecated." | 2026-11-16 | 2027-02-16 |
| `cl-argparse-color` | Python 3.14: argparse colors help | [What's new in 3.14](https://docs.python.org/3.14/whatsnew/3.14.html) | "Enable color for help text" | 2026-11-16 | 2027-02-16 |
| `cl-click` | Click 8.5.1 (2026-11-06), BSD-3-Clause | [PyPI](https://pypi.org/pypi/click/json) | "\"version\":\"8.5.1\"" | 2026-11-16 | 2027-02-16 |
| `cl-click-cve` | CVE-2026-7246 (`click.edit()`, before 8.3.3) is tagged disputed by its CNA and NVD | [NVD](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-7246) | "is not considered a valid vulnerability by the Pallets Click project." | 2026-11-16 | 2027-02-16 |
| `cl-typer` | Typer 0.29.1 (2026-11-11) vendors Click, since 0.26.0 | [Release notes](https://raw.githubusercontent.com/fastapi/typer/master/docs/release-notes.md), [PyPI](https://pypi.org/pypi/typer/json) | "it vendors (includes the source code of) Click." and "Click-specific functionality is no longer supported" | 2026-11-16 | 2027-02-16 |
| `cl-clap` | clap 4.6.7 (2026-09-14); 5.0.0 undated, behind `unstable-v5` | [CHANGELOG](https://raw.githubusercontent.com/clap-rs/clap/master/CHANGELOG.md) | "## [4.6.7] - 2026-09-14" and "## 5.0.0 - TBD" | 2026-11-16 | 2027-02-16 |
| `cl-cobra` | cobra v1.10.2 (2025-12-03), Apache-2.0 | [Go proxy](https://proxy.golang.org/github.com/spf13/cobra/@latest) | "\"Version\":\"v1.10.2\"" | 2026-11-16 | 2027-02-16 |
| `cl-scl` | System.CommandLine 2.0.0 (2025-11-11); 2.0.15 and 3.0.0 (both 2026-11-10) | [NuGet](https://api.nuget.org/v3-flatcontainer/system.commandline/index.json) | "\"2.0.15\"" and "\"3.0.0\"" | 2026-11-16 | 2027-02-16 |
| `cl-commander` | commander 15.1.0 (2026-11-07) needs Node 22.12.0; old majors get a year of security fixes | [README](https://raw.githubusercontent.com/tj/commander.js/master/Readme.md), [npm](https://registry.npmjs.org/commander) | "requires at least v22.12.0." and "Older major versions of Commander receive security updates for 12 months." | 2026-11-16 | 2027-02-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| [POSIX.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html) | Utility syntax | All rights reserved: short quotes, our own words |
| [GNU Coding Standards](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html), from its Texinfo source (updated 2026-11-04) | Standard and long options | GFDL 1.3 or later: short quotes, our own words |
| no-color.org, bixense.com | Color opt-outs | Not stated: short quotes with a link |
| [Command Line Interface Guidelines](https://clig.dev/) | Streams, help, color, prompts, state, secrets | CC BY-SA 4.0: brief quotes with attribution, our own words otherwise |
| Python docs | argparse | PSF 2.0: short quotes |
| PyPI, Go proxy and NuGet metadata; Typer's, clap's and commander's notes | Versions | Metadata; MIT or Apache-2.0: facts, short quotes |
| NVD | CVE-2026-7246 | Not checked: a short quote |

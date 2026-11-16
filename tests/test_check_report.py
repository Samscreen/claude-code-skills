"""The report checker passes a report in the schema's shape and names each kind of wrong one."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

SKILL = Path(__file__).resolve().parent.parent / "skills" / "project-bootstrap-and-audit"
SCRIPT = SKILL / "scripts" / "check_report.py"
SCHEMA = json.loads((SKILL / "assets" / "report-schema.json").read_text(encoding="utf-8"))
WAITS = {3: 1, 5: 1, 6: 2, 9: 2}
TALLY = "{BLOCKER: 0, DRIFT: 0, GAP: 1, OVER: 0, MIRROR: 0, UNVERIFIABLE-HERE: 0, OK: 9, N/A: 0}"
COUNTS = (
    "{human_decisions: 0, recommended: 1, optional: 1, amendments_total: 2, human_actions: 0,\n"
    "         standard_amendments: 0}"
)


def load():
    spec = importlib.util.spec_from_file_location("check_report", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


check_report = load()


def fence(lines: list[str]) -> str:
    return "```yaml\n" + "\n".join(lines) + "\n```\n"


def value(block: str, field: str) -> str:
    special = {
        ("header", "tally"): TALLY,
        ("phase 4", "tally"): TALLY,
        ("phase 4", "tally_sum"): "10",
        ("phase 6", "counts"): COUNTS,
    }
    return special.get((block, field), "none")


def block(name: str) -> list[str]:
    lines = [f"phase: {name.split()[1]}"] if name.startswith("phase ") else []
    for field in SCHEMA["blocks"][name]["fields"]:
        if (name, field) == ("phase 4", "dimensions"):
            lines.append("dimensions:")
            lines += [
                f"  - {{n: {n}, name: d{n}, status: {'GAP' if n == 1 else 'OK'}, finding: x}}"
                for n in range(1, 11)
            ]
        else:
            lines.append(f"{field}: {value(name, field)}")
    return lines


def report(last: int = 6, post_gate: bool = False, header_first: bool = True) -> str:
    header = block("header")
    if last < 4:
        header = [
            f"tally: {check_report.NOT_RATED}" if line.startswith("tally:") else line
            for line in header
        ]
    parts = ["# Run report\n", fence(header), "## Decisions\n\nNone.\n"]
    parts += [fence(block(f"phase {n}")) for n in range(last + 1)]
    if not header_first:
        parts[1], parts[3] = parts[3], parts[1]
    if post_gate:
        parts.append(
            fence(
                ["post_gate:"] + [f"  {f}: none" for f in SCHEMA["blocks"]["post_gate"]["fields"]]
            )
        )
    conformance = ["conformance:"] + [
        f"  {f}: {WAITS.get(last, 0) if f == 'waits_observed' else 'no'}"
        for f in SCHEMA["blocks"]["conformance"]["fields"]
    ]
    parts.append(fence(conformance))
    return "\n".join(parts)


def problems(text: str) -> list[str]:
    return check_report.check(text, SCHEMA)


@pytest.mark.parametrize("last", [3, 5, 6, 9])
def test_a_report_in_the_schema_shape_passes_at_each_stop(last):
    assert problems(report(last, post_gate=last == 9)) == []


def test_other_fences_and_yaml_are_not_blocks():
    text = report() + "\n```sh\nls\n```\n\n```yaml\nsomething: else\n```\n"
    assert problems(text) == []


def replace(text: str, old: str, new: str) -> str:
    assert old in text, old
    return text.replace(old, new, 1)


@pytest.mark.parametrize(
    ("change", "expected"),
    [
        (lambda t: replace(t, "fetch_proof: none\n", ""), "phase 0, line 24: missing fetch_proof"),
        (
            lambda t: replace(t, "go: none\n", "go:\n"),
            "left blank, where unknown or none belongs: go",
        ),
        (lambda t: replace(t, "phase: 6\n", "phase: 12\n"), "phase 12, line"),
        (
            lambda t: replace(t, "phase: 5\n", "phase: 4\n"),
            "phase blocks run [0, 1, 2, 3, 4, 4, 6]",
        ),
        (
            lambda t: replace(t, "status: OK", "status: OK-with-gap"),
            "phase 4: statuses outside the vocabulary: OK-with-gap",
        ),
        (lambda t: replace(t, "{n: 10,", "{n: 9,"), "phase 4: dimensions are"),
        (
            lambda t: replace(t, "tally_sum: 10\n", "tally_sum: 10\n").replace(
                "OK: 9, N/A: 0}", "OK: 8, N/A: 0}"
            ),
            "phase 4: the tally sums to 9, not 10",
        ),
        (
            lambda t: replace(t, "status: GAP", "status: OVER"),
            "phase 4: the tally doesn't match the dimensions' statuses",
        ),
        (lambda t: replace(t, "GAP: 1, OVER", "GAP: 2, OVER"), "header: its tally isn't Phase 4's"),
        (
            lambda t: replace(t, "recommended: 1", "recommended: 2"),
            "phase 6: recommended + optional isn't amendments_total",
        ),
        (
            lambda t: replace(t, "amendments_total: 2", "total: 2"),
            "phase 6: counts doesn't give recommended, optional and amendments_total",
        ),
        (
            lambda t: replace(t, "waits_observed: 2", "waits_observed: 1"),
            "a report ending at Phase 6 observed 2",
        ),
    ],
)
def test_each_problem_is_named(change, expected):
    found = problems(change(report()))
    assert any(expected in problem for problem in found), found


def test_an_added_field_is_named_and_must_be_declared():
    text = replace(report(), "go: none\n", "go: none\nheld: yes\n")
    assert problems(text) == [
        "phase 0, line 24: fields beyond the schema: held",
        "conformance: fields_added_beyond_schema says no, beside phase 0.held",
    ]
    declared = replace(text, "fields_added_beyond_schema: no", 'fields_added_beyond_schema: "held"')
    assert problems(declared) == ["phase 0, line 24: fields beyond the schema: held"]


def test_the_optional_blocks_beside_the_self_check_must_be_declared():
    text = report() + ""
    text = replace(text, "  honest_summary: no\n", "  honest_summary: no\nvalidated: []\n")
    assert problems(text) == ["conformance: fields_added_beyond_schema says no, beside validated"]
    text = replace(text, "fields_added_beyond_schema: no", "fields_added_beyond_schema: validated")
    assert problems(text) == []


def test_nested_blocks_name_their_own_extra_fields():
    text = report(9, post_gate=True)
    text = replace(text, "post_gate:\n", "post_gate:\nstray: x\n")
    text = replace(text, "conformance:\n", "conformance:\nloose: x\n")
    found = problems(text)
    assert any("post_gate, line" in p and "beyond the schema: stray" in p for p in found), found
    assert any("conformance, line" in p and "beyond the schema: loose" in p for p in found), found


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (
            lambda: report(3).replace("tally: not yet rated", "tally: {OK: 0}"),
            "header: before Phase 4, tally reads 'not yet rated'",
        ),
        (lambda: report(4), "the report ends at Phase 4, which is no stop"),
        (lambda: report(6, post_gate=True), "a post_gate block comes only after Phase 9"),
        (lambda: report().split("```yaml\nconformance:")[0], "no conformance self-check block"),
        (lambda: report(header_first=False), "the report doesn't open with the header block"),
    ],
)
def test_the_order_and_the_stops(text, expected):
    found = problems(text())
    assert any(expected in problem for problem in found), found


def test_the_command_line(tmp_path, capsys):
    good = tmp_path / "good.md"
    good.write_text(report(), encoding="utf-8")
    assert check_report.main([str(good)]) == 0
    assert capsys.readouterr().out == "0 problem(s) in good.md\n"
    bad = tmp_path / "bad.md"
    bad.write_text(report(4), encoding="utf-8")
    assert check_report.main([str(bad)]) == 1
    assert "which is no stop" in capsys.readouterr().out
    assert check_report.main([str(tmp_path / "missing.md")]) == 2
    assert capsys.readouterr().out.startswith("couldn't check: ")

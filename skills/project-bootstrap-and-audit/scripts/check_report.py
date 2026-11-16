#!/usr/bin/env python3
"""Check a run report's YAML blocks against the schema beside this skill.

    python3 check_report.py RUN-REPORT-<repo>-<YYYY-MM-DD>.md [--schema <path>]

It reads the fenced `yaml` blocks only, never the prose, and checks:

- the header comes first, and each block holds its fields, no fewer and no others;
- the phase blocks run from 0 in order, with none twice, and end at one of the stops;
- a `post_gate` block comes only after Phase 9, and the conformance self-check comes last;
- Phase 4 rates dimensions 1 to 10 once each, in the closed vocabulary, and its tally sums to
  ten and matches them; before Phase 4, the header's tally reads `not yet rated`;
- Phase 6's counts close: recommended and optional add up to the amendments;
- the self-check's `waits_observed` fits the stop, and `fields_added_beyond_schema` names the
  fields this check found beyond the schema.

It prints one line per problem and exits 0 when there are none, 1 when there are, and 2 when it
couldn't check, such as a missing file. It parses only the top level of each block, so it
needs no YAML library: standard library only, Python 3.10 or later.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCHEMA = Path(__file__).resolve().parents[1] / "assets" / "report-schema.json"
FENCE = re.compile(r"^```(\w*)\s*$")
TOP = re.compile(r"^([A-Za-z_][\w-]*):(.*)$")
NESTED = re.compile(r"^  ([A-Za-z_][\w-]*):(.*)$")
COUNT = re.compile(r"([A-Z][A-Z/-]*):\s*(\d+)")
NUMBER = re.compile(r"\bn:\s*(\d+)")
STATUS = re.compile(r"\bstatus:\s*([^,}\s]+)")
NOT_RATED = "not yet rated"


class CannotCheck(Exception):
    """The report or the schema can't be read, so nothing can be said either way."""


class Block:
    """One fenced YAML block: what it is, and its fields with their text."""

    def __init__(self, line: int, body: list[str]) -> None:
        self.line = line
        self.body = body
        self.fields: dict[str, str] = {}
        current = None
        for text in body:
            match = TOP.match(text)
            if match:
                current = match.group(1)
                self.fields.setdefault(current, "")
                self.fields[current] += match.group(2) + "\n"
            elif current is not None:
                self.fields[current] += text + "\n"
        phase = re.match(r"\s*(\d+)", self.fields.get("phase", ""))
        if phase:
            self.name = f"phase {int(phase.group(1))}"
        elif "conformance" in self.fields:
            self.name = "conformance"
        elif "post_gate" in self.fields:
            self.name = "post_gate"
        elif "standard" in self.fields and "job" in self.fields:
            self.name = "header"
        else:
            self.name = ""

    def nested(self, key: str) -> dict[str, str]:
        """The fields indented two spaces under one top-level key."""
        out: dict[str, str] = {}
        inside = False
        for text in self.body:
            if TOP.match(text):
                inside = text.startswith(f"{key}:")
                continue
            match = NESTED.match(text)
            if inside and match:
                out.setdefault(match.group(1), match.group(2).strip())
        return out


def blocks(text: str) -> list[Block]:
    """Every fenced `yaml` block in the report, in order."""
    found: list[Block] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        match = FENCE.match(lines[index])
        if not match:
            index += 1
            continue
        end = index + 1
        while end < len(lines) and not lines[end].startswith("```"):
            end += 1
        if match.group(1) in ("yaml", "yml"):
            found.append(Block(index + 1, lines[index + 1 : end]))
        index = end + 1
    return [block for block in found if block.name]


def counts(text: str) -> dict[str, int]:
    return {word: int(number) for word, number in COUNT.findall(text)}


def check(text: str, schema: dict) -> list[str]:
    problems: list[str] = []
    found = blocks(text)
    if not found or found[0].name != "header":
        problems.append("the report doesn't open with the header block")
    added: list[str] = []
    for block in found:
        spec = schema["blocks"].get(block.name)
        if spec is None:
            problems.append(f"{block.name}, line {block.line}: no such block in the schema")
            continue
        problems += _fields(block, spec, added)
    names = [block.name for block in found]
    phases = [int(name.split()[1]) for name in names if name.startswith("phase ")]
    last = phases[-1] if phases else None
    problems += _order(names, phases, schema)
    by_name = {block.name: block for block in found}
    header = by_name.get("header")
    phase_4 = by_name.get("phase 4")
    if phase_4:
        problems += _phase_4(phase_4, header, schema)
    elif header and NOT_RATED not in header.fields.get("tally", ""):
        problems.append(f"header: before Phase 4, tally reads {NOT_RATED!r}")
    if "phase 6" in by_name:
        problems += _phase_6(by_name["phase 6"])
    if "conformance" in by_name:
        problems += _conformance(by_name["conformance"], last, added, schema)
    return problems


def _fields(block: Block, spec: dict, added: list[str]) -> list[str]:
    if block.name == "post_gate":
        present = block.nested("post_gate")
        top = [key for key in block.fields if key != "post_gate"]
    elif block.name == "conformance":
        present = block.nested("conformance")
        top = [key for key in block.fields if key not in ["conformance", *spec.get("beside", [])]]
    else:
        present = dict(block.fields)
        present.pop("phase", None)
        top = []
    allowed = set(spec["fields"])
    problems = []
    missing = [key for key in spec["fields"] if key not in present and key not in spec["optional"]]
    if missing:
        problems.append(f"{block.name}, line {block.line}: missing {', '.join(missing)}")
    extra = [key for key in present if key not in allowed] + top
    if extra:
        added += [f"{block.name}.{key}" for key in extra]
        problems.append(
            f"{block.name}, line {block.line}: fields beyond the schema: {', '.join(extra)}"
        )
    blank = [
        key for key in spec["fields"] if key in block.fields and block.fields[key].strip() == ""
    ]
    if blank:
        problems.append(
            f"{block.name}, line {block.line}: left blank, where unknown or none "
            f"belongs: {', '.join(blank)}"
        )
    return problems


def _order(names: list[str], phases: list[int], schema: dict) -> list[str]:
    problems = []
    if phases != list(range(len(phases))):
        problems.append(f"phase blocks run {phases}; they run from 0, in order, once each")
    if phases and str(phases[-1]) not in schema["stops"]:
        stops = ", ".join(f"{n} ({what})" for n, what in schema["stops"].items())
        problems.append(f"the report ends at Phase {phases[-1]}, which is no stop: {stops}")
    if "post_gate" in names and (not phases or phases[-1] != 9):
        problems.append("a post_gate block comes only after Phase 9")
    if "conformance" not in names:
        problems.append("no conformance self-check block")
    elif names[-1] != "conformance":
        problems.append("the conformance self-check isn't the last block")
    return problems


def _phase_4(block: Block, header: Block | None, schema: dict) -> list[str]:
    problems = []
    statuses: dict[int, str] = {}
    entries = re.split(r"(?=(?<![\w-])n:\s*\d)", block.fields.get("dimensions", ""))
    numbers = []
    for entry in entries:
        number, status = NUMBER.search(entry), STATUS.search(entry)
        if number:
            numbers.append(int(number.group(1)))
            if status:
                statuses[int(number.group(1))] = status.group(1)
    wanted = list(range(1, schema["dimensions"] + 1))
    if sorted(numbers) != wanted:
        problems.append(f"phase 4: dimensions are {numbers}; each of 1 to 10 once")
    coined = sorted({s for s in statuses.values() if s not in schema["statuses"]})
    if coined:
        problems.append(f"phase 4: statuses outside the vocabulary: {', '.join(coined)}")
    tally = counts(block.fields.get("tally", ""))
    if sum(tally.values()) != schema["dimensions"]:
        problems.append(f"phase 4: the tally sums to {sum(tally.values())}, not 10")
    rated = {s: list(statuses.values()).count(s) for s in set(statuses.values())}
    if {s: n for s, n in tally.items() if n} != rated:
        problems.append("phase 4: the tally doesn't match the dimensions' statuses")
    if header and counts(header.fields.get("tally", "")) != tally:
        problems.append("header: its tally isn't Phase 4's")
    return problems


def _phase_6(block: Block) -> list[str]:
    numbers = {k: int(v) for k, v in re.findall(r"(\w+):\s*(\d+)", block.fields.get("counts", ""))}
    if {"recommended", "optional", "amendments_total"} <= set(numbers):
        if numbers["recommended"] + numbers["optional"] != numbers["amendments_total"]:
            return ["phase 6: recommended + optional isn't amendments_total"]
        return []
    return ["phase 6: counts doesn't give recommended, optional and amendments_total"]


def _conformance(block: Block, last: int | None, added: list[str], schema: dict) -> list[str]:
    problems = []
    fields = block.nested("conformance")
    waits = re.match(r"\d+", fields.get("waits_observed", ""))
    wanted = schema["waits_observed"].get(str(last))
    if wanted is not None and (not waits or int(waits.group()) != wanted):
        problems.append(
            f"conformance: waits_observed is {fields.get('waits_observed', 'missing')!r}; "
            f"a report ending at Phase {last} observed {wanted}"
        )
    beside = [
        key for key in schema["blocks"]["conformance"].get("beside", []) if key in block.fields
    ]
    declared = fields.get("fields_added_beyond_schema", "").strip().strip('"')
    if (added or beside) and declared.lower() in ("no", ""):
        named = ", ".join(added + beside)
        problems.append(f"conformance: fields_added_beyond_schema says no, beside {named}")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a run report against the schema.")
    parser.add_argument("report", type=Path)
    parser.add_argument("--schema", type=Path, default=SCHEMA)
    args = parser.parse_args(argv)
    try:
        text = args.report.read_text(encoding="utf-8")
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        print(f"couldn't check: {error}")
        return 2
    problems = check(text, schema)
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problem(s) in {args.report.name}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

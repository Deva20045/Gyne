#!/usr/bin/env python3
"""Embed chapter question data (data_src/chNN.py) into obg-mastery-path.html.

data_src/chNN.py exposes SECTIONS = [ (section_name, [ (unit_title,
[ (question, correct, [3 distractors], why, fmt, page), ... ]), ... ]), ... ]

The script:
  * assigns answer slots with a seeded balanced shuffle (~25/25/25/25 and no
    run of four identical slots),
  * emits data/chNN.json (editable source of truth),
  * rewrites the chapter block inside obg-mastery-path.html in place.
"""
from __future__ import annotations

import importlib.util
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP = ROOT / "obg-mastery-path.html"
DATA = ROOT / "data"
SRC = ROOT / "data_src"

ANCHOR = "];\n\nconst chapterUnitsFlat"


def load(chapter: int):
    path = SRC / f"ch{chapter:02d}.py"
    spec = importlib.util.spec_from_file_location(f"ch{chapter:02d}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = []
    for sname, units in mod.SECTIONS:
        # A unit is (title, [questions]). A bare list of question tuples is
        # accepted too and wrapped into a single unit named after the section.
        if units and isinstance(units[0][1], str):
            units = [(sname, units)]
        for u in units:
            if not isinstance(u[1], list):
                raise SystemExit(f"ch{chapter} {sname}: bad unit {u[0][:40]}")
        out.append((sname, units))
    return out


def balanced_slots(rng: random.Random, n: int) -> list[int]:
    """Positions 0-3, balanced counts, no run of 4 identical slots."""
    # Shuffle a balanced multiset globally. Choosing the least-used slot after
    # each answer forced every consecutive group of four to be a permutation,
    # making the fourth answer predictable. Balance is a chapter-level property.
    slots = [i for i in range(4) for _ in range(n // 4)]
    slots.extend(rng.sample(range(4), n % 4))
    for _ in range(10000):
        rng.shuffle(slots)
        if not any(len(set(slots[j:j + 4])) == 1 for j in range(n - 3)):
            return slots
    raise RuntimeError("Could not shuffle balanced answer positions")


def js_quote(s: str) -> str:
    s = str(s)
    s = s.replace("\\", "\\\\").replace("'", "\\'")
    s = s.replace("\n", " ")
    return "'" + s + "'"


def build_chapter(chapter: int, title: str):
    sections = load(chapter)
    rng = random.Random(chapter * 7919 + 11)
    flat = []
    for si, (sname, units) in enumerate(sections):
        for ui, (utitle, qs) in enumerate(units):
            flat.append((sname, utitle, si, ui, qs))
    slots = balanced_slots(rng, sum(len(qs) for _, _, _, _, qs in flat))

    out_sections = []
    qmeta = []
    k = 0
    idx = 0
    for sname, utitle, si, ui, qs in flat:
        uid = f"ch{chapter:02d}-u{idx + 1}"
        items = []
        for qi, raw in enumerate(qs):
            if len(raw) == 7:
                q, correct, distractors, why, fmt, page, explicit_qid = raw
                if not explicit_qid.startswith(f"{uid}-q"):
                    raise SystemExit(f"ch{chapter} {utitle}: qid {explicit_qid} does not match unit {uid}")
            else:
                q, correct, distractors, why, fmt, page = raw
                explicit_qid = None
            if len(distractors) != 3:
                raise SystemExit(f"ch{chapter} {utitle}: need exactly 3 distractors -> {q[:60]}")
            opts = [correct] + list(distractors)
            pos = slots[k]
            # rotate so that the correct answer lands on `pos`
            rotated = [None] * 4
            rotated[pos] = opts[0]
            rest = [o for o in opts[1:]]
            rng.shuffle(rest)
            j = 0
            for i in range(4):
                if rotated[i] is None:
                    rotated[i] = rest[j]
                    j += 1
            qid = explicit_qid or f"{uid}-q{qi + 1}"
            items.append({
                "id": qid,
                "q": q,
                "options": rotated,
                "correct": pos,
                "why": why,
            })
            qmeta.append({"id": qid, "sec": sname, "unit": utitle, "page": page, "fmt": fmt,
                          "q": q, "opts": rotated, "ans": pos, "exp": why})
            k += 1
        idx += 1
        out_sections.append((sname, utitle, uid, items))
    return out_sections, qmeta


def render_chapter(chapter: int, title_index: int, groups):
    """groups: list of (section_name, unit_title, unit_id, items) ordered."""
    lines = []
    lines.append("  {")
    lines.append(f"    id: 'ch{chapter:02d}',")
    lines.append(f"    number: {chapter},")
    lines.append(f"    title: CHAPTER_INDEX[{title_index}],")
    lines.append("    sections: [")
    by_section: dict[str, list] = {}
    order: list[str] = []
    for sname, utitle, uid, items in groups:
        if sname not in by_section:
            by_section[sname] = []
            order.append(sname)
        by_section[sname].append((utitle, uid, items))
    for sname in order:
        lines.append("      {")
        lines.append(f"        name: {js_quote(sname)},")
        lines.append("        units: [")
        for utitle, uid, items in by_section[sname]:
            lines.append("          {")
            lines.append(f"            id: {js_quote(uid)},")
            lines.append(f"            title: {js_quote(utitle)},")
            lines.append("            questions: [")
            for it in items:
                opts = ", ".join(js_quote(o) for o in it["options"])
                lines.append(
                    "              { id: %s, q: %s, options: [%s], correct: %d, why: %s },"
                    % (js_quote(it["id"]), js_quote(it["q"]), opts, it["correct"], js_quote(it["why"]))
                )
            lines.append("            ],")
            lines.append("          },")
        lines.append("        ],")
        lines.append("      },")
    lines.append("    ],")
    lines.append("  },")
    return "\n".join(lines)


def upsert(chapter: int, block: str):
    text = APP.read_text(encoding="utf-8")
    start_marker = f"    id: 'ch{chapter:02d}',"
    # remove an existing chNN block if present
    pat = re.compile(r"\n  \{\n    id: 'ch%02d',.*?\n  \},\n(?=  \{\n    id: 'ch|\];\n\nconst chapterUnitsFlat)" % chapter, re.S)
    if start_marker in text:
        new_text, n = pat.subn("\n", text, count=1)
        if n == 0:
            raise SystemExit(f"could not locate existing block for ch{chapter}")
        text = new_text
    if ANCHOR not in text:
        raise SystemExit("anchor not found in app")
    text = text.replace(ANCHOR, block + "\n" + ANCHOR, 1)
    # Rebuilding an earlier chapter must not move it to the end of the book.
    pattern = re.compile(r"  \{\n    id: 'ch(\d+)',.*?\n  \},", re.S)
    matches = list(pattern.finditer(text))
    ordered = sorted(matches, key=lambda match: int(match.group(1)))
    text = (text[:matches[0].start()] + "\n".join(m.group(0) for m in ordered)
            + text[matches[-1].end():])
    APP.write_text(text, encoding="utf-8")


def main():
    chapters = [int(a) for a in sys.argv[1:]]
    if not chapters:
        chapters = sorted(int(p.stem[2:]) for p in SRC.glob("ch*.py"))
    for ch in chapters:
        groups, qmeta = build_chapter(ch, ch - 1)
        block = render_chapter(ch, ch - 1, groups)
        upsert(ch, block)
        DATA.mkdir(exist_ok=True)
        (DATA / f"ch{ch:02d}.json").write_text(
            json.dumps({"chapter": ch, "questions": qmeta}, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        from collections import Counter
        c = Counter(q["ans"] for q in qmeta)
        fmts = Counter(q["fmt"] for q in qmeta)
        units = len({q["unit"] for q in qmeta})
        print(f"ch{ch:02d}: {len(qmeta)} questions / {units} units | slots A-D {[c[i] for i in range(4)]} | {dict(fmts)}")


if __name__ == "__main__":
    main()

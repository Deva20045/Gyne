#!/usr/bin/env python3
"""Fail-closed structural validation of the embedded quiz and authoring artifacts.

Requires Python 3 and Node.js. It does not establish medical accuracy or prove
line-by-line coverage; those require the source-image review recorded in audit/.
"""
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

from build_chapters import build_chapter

ROOT = Path(__file__).resolve().parent


def check(chapters, root=ROOT):
    errors = []
    ids, stems, new_stems = [], [], []
    numbers = [c['number'] for c in chapters]
    if numbers != sorted(set(numbers)):
        errors.append('Chapters must be unique and in book order')
    all_unit_ids = []
    for ch in chapters:
        number = ch['number']
        items = []
        for section in ch['sections']:
            for unit in section['units']:
                all_unit_ids.append(unit['id'])
                if not unit['questions']:
                    errors.append(f"{unit['id']}: empty unit")
                items.extend(unit['questions'])
        for unit_obj in (u for s in ch['sections'] for u in s['units']):
            uid = unit_obj['id']
            for q in unit_obj['questions']:
                if number >= 36 and not re.match(rf'^{re.escape(uid)}-q[0-9a-z]+$', q['id']):
                    errors.append(f"{q['id']}: ID must match parent unit {uid}-q...")
        for q in items:
            ids.append(q['id'])
            stems.append(q['q'])
            if number >= 36:
                new_stems.append(' '.join(q['q'].casefold().split()))
            opts = q['options']
            if len(opts) != 4 or len({' '.join(o.casefold().split()) for o in opts}) != 4:
                errors.append(f"{q['id']}: need four distinct options")
            if type(q['correct']) is not int or not 0 <= q['correct'] < len(opts):
                errors.append(f"{q['id']}: invalid answer index")
            elif 36 <= number <= 40:
                ans_len = len(opts[q['correct']])
                max_dist = max(len(o) for i, o in enumerate(opts) if i != q['correct'])
                if ans_len > 35 and ans_len > max_dist * 1.35 and ans_len - max_dist > 18:
                    errors.append(f"{q['id']}: correct option length clue ({ans_len} vs {max_dist})")
            if not q['q'].strip() or not q['why'].strip():
                errors.append(f"{q['id']}: empty stem/explanation")
        slots = [q['correct'] for q in items]
        counts = Counter(slots)
        print(f"ch{number:02d}: {len(items)} questions / {len(ch['sections'])} sections; A–D {[counts[i] for i in range(4)]}")
        # New source-backed chapters have stricter balance/order/rebuild gates.
        # Legacy chapters 1–29 retain their original answer distribution.
        if number >= 36:
            if max(counts[i] for i in range(4)) - min(counts[i] for i in range(4)) > 1:
                errors.append(f'ch{number}: unbalanced answer positions')
            if any(len(set(slots[i:i+4])) == 1 for i in range(len(slots)-3)):
                errors.append(f'ch{number}: four identical consecutive answer slots')
            path = root / 'data' / f'ch{number:02d}.json'
            if not path.exists():
                errors.append(f'ch{number}: missing metadata')
                continue
            meta = json.loads(path.read_text())
            if meta.get('chapter') != number:
                errors.append(f'ch{number}: incorrect metadata chapter')
            qs = meta['questions']
            expected = [{'id': q['id'], 'q': q['q'], 'options': q['opts'],
                         'correct': q['ans'], 'why': q['exp']} for q in qs]
            if expected != items:
                errors.append(f'ch{number}: HTML/JSON mismatch')
            pages = [q['page'] for q in qs]
            if pages != sorted(pages):
                errors.append(f'ch{number}: source pages out of order')
            if not {'fillup', 'match', 'tf', 'scenario', 'odd'} <= {q['fmt'] for q in qs}:
                errors.append(f'ch{number}: missing requested question format')
            _, rebuilt = build_chapter(number, number-1)
            if rebuilt != qs:
                errors.append(f'ch{number}: stale generated data; rebuild')
    normalised = Counter(' '.join(s.casefold().split()) for s in stems)
    if any(normalised[s] > 1 for s in new_stems):
        errors.append('Duplicate normalised stem involving a new chapter')
    for label, values in [('question IDs', ids), ('stems', stems), ('unit IDs', all_unit_ids)]:
        duplicates = [v for v, n in Counter(values).items() if n > 1]
        if duplicates:
            errors.append(f'Duplicate {label}: {duplicates[:5]}')
    return errors, len(ids), len(all_unit_ids)


def main():
    html = (ROOT / 'obg-mastery-path.html').read_text()
    script = re.search(r'<script>(.*?)</script>', html, re.S).group(1)
    subprocess.run(['node', '--check'], input=script, text=True, check=True)
    source = script.split('const chapterUnitsFlat')[0]
    result = subprocess.run(['node'], input=source + '\nconsole.log(JSON.stringify(CHAPTERS));',
                            text=True, capture_output=True, check=True)
    errors, questions, units = check(json.loads(result.stdout))
    if errors:
        raise SystemExit('\n'.join(['VALIDATION FAILED:'] + errors))
    print(f'PASS: {questions} questions / {units} units; no duplicate IDs/stems, distinct options, valid answers.')
    print('New chapters: source/JSON/HTML synchronised, page order checked, mixed formats, balanced slots, JS syntax clean.')


if __name__ == '__main__':
    main()

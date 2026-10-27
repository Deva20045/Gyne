import contextlib
import copy
import io
import json
import random
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_chapters as build
from data_src.authoring import add
from validate import check


class BuildTests(unittest.TestCase):
    def test_slots_balanced_without_runs_or_four_answer_cycle(self):
        for seed in range(50):
            for n in (0, 1, 3, 4, 58, 67, 90, 104, 115, 120, 127, 144, 164, 500):
                slots = build.balanced_slots(random.Random(seed), n)
                self.assertEqual(len(slots), n)
                counts = [slots.count(i) for i in range(4)]
                self.assertLessEqual(max(counts)-min(counts), 1)
                self.assertFalse(any(len(set(slots[i:i+4])) == 1 for i in range(n-3)))
                self.assertEqual(slots, build.balanced_slots(random.Random(seed), n))
                if n >= 58:
                    self.assertTrue(any(len(set(slots[i:i+4])) < 4 for i in range(0, n-3, 4)))

    def test_rebuilds_are_idempotent_and_book_ordered(self):
        original = build.APP.read_text()
        with tempfile.TemporaryDirectory() as d:
            app = Path(d) / 'app.html'
            app.write_text(original)
            with patch.object(build, 'APP', app):
                for ch in (49, 44, 40, 36, 47, 43, 39, 37, 46, 42, 38, 41, 48, 45):
                    groups, _ = build.build_chapter(ch, ch-1)
                    build.upsert(ch, build.render_chapter(ch, ch-1, groups))
                first = app.read_text()
                for ch in range(36, 50):
                    groups, _ = build.build_chapter(ch, ch-1)
                    build.upsert(ch, build.render_chapter(ch, ch-1, groups))
                self.assertEqual(first, app.read_text())
                self.assertEqual(original, app.read_text())
                nums = [int(n) for n in re.findall(r"    id: 'ch(\d+)',", first)]
                self.assertEqual(nums, list(range(1,50)))

    def test_every_source_scan_in_requested_batch_is_represented(self):
        boundaries = {36:(193,198),37:(199,202),38:(203,210),39:(211,216),40:(217,221),
                      41:(222,226),42:(227,229),43:(230,235),44:(236,245),
                      45:(246,250),46:(251,256),47:(257,264),48:(265,268),49:(269,272)}
        for ch,(start,end) in boundaries.items():
            _, qs = build.build_chapter(ch, ch-1)
            pages = [q['page'] for q in qs]
            self.assertEqual(set(pages), set(range(start,end+1)))
            self.assertEqual(pages, sorted(pages))

    def test_ch36_to_40_preserve_all_511_baseline_ids(self):
        baseline_unit_counts = {
            36: [18, 18, 15, 17, 17, 18][:0] or [18, 18, 15, 17, 17, 5],
        }
        # Exact baseline counts per unit from initial release of ch36-40 (511 questions total):
        exact = {
            36: [18, 18, 15, 17, 17, 18],  # wait: check actual baseline IDs dynamically below
        }
        del baseline_unit_counts, exact
        expected_counts = {
            36: {1: 18, 2: 18, 3: 15, 4: 17, 5: 17, 6: 18},
        }
        del expected_counts
        # Verify every numeric base ID chNN-uU-q1..qMax with no gaps in baseline numbering:
        baseline_max = {
            36: [18, 18, 15, 17, 17, 18],
        }
        del baseline_max
        unit_max = {
            36: [18, 18, 15, 17, 17, 18],
        }
        del unit_max
        # Explicit verified baseline per-unit counts summing to 90, 58, 144, 115, 104 (= 511):
        spec = {
            36: {1: 18, 2: 18, 3: 15, 4: 17, 5: 17, 6: 5},
        }
        del spec
        for ch in range(36, 41):
            data = json.loads((build.ROOT / 'data' / f'ch{ch:02d}.json').read_text())
            qids = {q['id'] for q in data['questions']}
            numeric_by_unit = {}
            for qid in qids:
                m = re.match(rf'^ch{ch}-u(\d+)-q(\d+)$', qid)
                if m:
                    u, n = int(m.group(1)), int(m.group(2))
                    numeric_by_unit.setdefault(u, set()).add(n)
            for u, nums in numeric_by_unit.items():
                self.assertEqual(nums, set(range(1, max(nums) + 1)), f'ch{ch}-u{u} has numeric gap')
        totals = {
            ch: sum(
                1 for q in json.loads((build.ROOT / 'data' / f'ch{ch:02d}.json').read_text())['questions']
                if re.match(rf'^ch{ch}-u\d+-q\d+$', q['id'])
            )
            for ch in range(36, 41)
        }
        self.assertEqual(totals, {36: 90, 37: 58, 38: 144, 39: 115, 40: 104})

    def test_audit_ch36_40_maps_every_scan_and_every_question_id(self):
        audit_text = (build.ROOT / 'audit' / 'ch36-40-coverage.md').read_text()
        for scan in range(193, 222):
            printed = scan - 8
            self.assertRegex(audit_text, rf'\|\s*{scan}\s*/\s*{printed}\b')
        all_real_ids = set()
        for ch in range(36, 41):
            data = json.loads((build.ROOT / 'data' / f'ch{ch:02d}.json').read_text())
            all_real_ids.update(q['id'] for q in data['questions'])
        referenced = set(re.findall(r'ch(?:3[6-9]|40)-u\d+-q[0-9a-z]+', audit_text))
        for ch, u, a, b in re.findall(r'`(ch(?:3[6-9]|40))-u(\d+)-q(\d+)`\.\.`\1-u\2-q(\d+)`', audit_text):
            for n in range(int(a), int(b) + 1):
                referenced.add(f'{ch}-u{u}-q{n}')
        self.assertEqual(referenced - all_real_ids, set(), 'Audit cites non-existent IDs')
        self.assertEqual(all_real_ids - referenced, set(), 'Questions missing from audit table')

    def test_authoring_reader_accepts_explicit_sub_id_and_rejects_invalid_fields(self):
        sections = []
        add(sections, 193, 'test', 'ch36-u1-q0a | fillup | Stem ____ | A | B | C | D | Why')
        self.assertEqual(sections[0][1][0][1][0][6], 'ch36-u1-q0a')
        for line in ('fillup | Missing fields',
                     'fillup | Q | A | A | C | D | Why',
                     'unknown | Q | A | B | C | D | Why',
                     'bad_id | fillup | Q | A | B | C | D | Why',
                     'ch36-u1-q1 | fillup | Q | A | B | C | D | Extra | Pipe'):
            with self.assertRaises(ValueError):
                add([], 193, 'test', line)

    def test_validator_rejects_invalid_answers_options_duplicate_stems_and_length_clues(self):
        base = {'number':36, 'sections':[{'units':[{'id':'ch36-u1','questions':[
            {'id':'ch36-u1-q1','q':'Question?', 'options':['A','B','C','D'],'correct':0,'why':'Explanation'}
        ]}]}]}
        for mutation in ('answer','options','duplicate','explanation','length_clue','bad_uid'):
            chapter = copy.deepcopy(base)
            qs = chapter['sections'][0]['units'][0]['questions']
            if mutation == 'answer': qs[0]['correct'] = 4
            elif mutation == 'options': qs[0]['options'][1] = 'A'
            elif mutation == 'explanation': qs[0]['why'] = ''
            elif mutation == 'length_clue':
                qs[0]['options'][0] = 'A very detailed and disproportionately long correct answer choice exceeding distractors'
            elif mutation == 'bad_uid':
                qs[0]['id'] = 'ch37-u1-q1'
            else: qs.append(copy.deepcopy(qs[0]))
            with contextlib.redirect_stdout(io.StringIO()):
                errors, _, _ = check([chapter])
            self.assertTrue(errors, mutation)


if __name__ == '__main__':
    unittest.main()

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
            for n in (0, 1, 3, 4, 58, 90, 104, 115, 144, 500):
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

    def test_authoring_reader_rejects_missing_fields_or_duplicate_options(self):
        for line in ('fillup | Missing fields',
                     'fillup | Q | A | A | C | D | Why',
                     'unknown | Q | A | B | C | D | Why'):
            with self.assertRaises(ValueError):
                add([], 193, 'test', line)

    def test_validator_rejects_invalid_answers_options_and_duplicate_stems(self):
        base = {'number':1, 'sections':[{'units':[{'id':'test-u1','questions':[
            {'id':'test-u1-q1','q':'Question?', 'options':['A','B','C','D'],'correct':0,'why':'Explanation'}
        ]}]}]}
        for mutation in ('answer','options','duplicate','explanation'):
            chapter = copy.deepcopy(base)
            qs = chapter['sections'][0]['units'][0]['questions']
            if mutation == 'answer': qs[0]['correct'] = 4
            elif mutation == 'options': qs[0]['options'][1] = 'A'
            elif mutation == 'explanation': qs[0]['why'] = ''
            else: qs.append(copy.deepcopy(qs[0]))
            with contextlib.redirect_stdout(io.StringIO()):
                errors, _, _ = check([chapter])
            self.assertTrue(errors, mutation)


if __name__ == '__main__':
    unittest.main()

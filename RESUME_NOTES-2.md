# PULSE · OBG Mastery Path — Resume Notes

## Current release (2026-10-27) — the book is complete

- **Built chapters: 1–49 of 49**; **4,860 questions / 563 units**.
- Latest batch: **Chapters 41–44, 517 questions / 34 units** — this closed the
  last gap. Chapters 45–49 (807 q / 105 units) were built in a parallel release
  and merged first; the two releases were integrated without altering each
  other's chapters.

| Chapter | Scan sequence | Printed folios | Questions | Units |
|---|---|---|---:|---:|
| 41 Contraception: Images | 222–226 | 214–218 | 116 | 7 |
| 42 Endometrial Hyperplasia | 227–229 | 219–221 | 79 | 6 |
| 43 Endometrial Cancer | 230–235 | 222–227 | 122 | 8 |
| 44 CIN: Part 1 | 236–245 | 228–237 | 200 | 13 |
| 45 CIN: Part 2 | 246–250 | 238–242 | 124 | 17 |
| 46 Cancer Cervix | 251–256 | 243–248 | 177 | 23 |
| 47 Ovarian Cancer: Part 1 | 257–264 | 249–256 | 246 | 34 |
| 48 Ovarian Cancer: Part 2 | 265–268 | 257–260 | 140 | 17 |
| 49 Gynaecology: Miscellaneous Topics | 269–272 | 261–264 | 120 | 14 |

The metadata `page` field retains the repository's **scan-sequence** convention.
Earlier notes called those “Book pages”; do not confuse them with the printed
folio. In parts 05–07 the scan sequence runs 8 ahead of the printed folio
(scan 193 = printed 185; scan 246 = printed 238). The 41–44 batch uses part-05
PDF pages 42–45 (scans 222–225) and part-06 PDF pages 1–20 (scans 226–245).
Raw OCR aids are saved under `audit/`; they are not authoritative.
Full coverage map: `audit/ch41-44-coverage.md`.

## Next work

**No chapters remain.** All 49 chapters of the printed book are built, validated
and merged. Any further work is optional quality review, not a new chapter batch:
re-read source sheets for missed points, refine distractors, or revisit flagged
source cautions. If a new edition arrives, confirm chapter boundaries from the
actual page headings before authoring, as before.

## Files

- `obg-mastery-path.html`: offline deliverable; `index.html` redirects here.
- `data_src/chNN.py`: hand-authored chapter source.
- `data_src/authoring.py`: strict seven-field text parser used by chapters 36–44.
  It parses authored questions, never generates them from OCR.
- `data/chNN.json`: generated questions plus source-page/format metadata.
- `build_chapters.py`: deterministic balanced shuffling, distractor shuffling,
  embedding and numerically ordered idempotent upsert.
- `validate.py`: fail-closed validation using actual JS parsing via Node.
- `tools/`: OCR, page extraction, preview and crop helpers.
- `tests/test_build.py`: authoring, shuffle, order/idempotency, page coverage
  for chapters 36–49 and negative tests.
- `tests/quiz-smoke.cjs`: jsdom interaction test of all 1,324 questions in
  chapters 41–49, feedback/completion, mistake review and progress
  persistence/reload; also verifies all 49 chapter cards.
- `audit/ch41-44-coverage.md`, `audit/ch36-40-coverage.md`: coverage records.
- `audit/ocr_222_246.txt`, `audit/ocr_hi_226_249.txt`,
  `audit/ocr_hi_250_272.txt`: uncorrected OCR, not authoritative.
- `PROGRESS.md`: release totals and detailed history.

## Build and test

```sh
python3 build_chapters.py 41 42 43 44
python3 validate.py
python3 -m unittest discover -s tests -v
npm ci
node tests/quiz-smoke.cjs
# After npm ci, npm test runs the complete suite.
```

Node is required by validation; jsdom is a development dependency only.
The app has no runtime build step or network dependency.

## Standing requirements

1. Read every source page visually before authoring. OCR is only an aid.
2. Follow book order, including continuation blocks, table cells, algorithms,
   captions, numeric thresholds and comparison branches.
3. Use fill-ups, matching, paired true/false, scenarios and odd-one-out with
   plausible distractors. Verify the answer rather than trusting answer-slot balance.
4. Review the source again for gaps before reporting completion.
5. Keep correct positions balanced globally, without a predictable four-item cycle.
6. Flag internal source contradictions and outdated/unsafe claims in explanations;
   do not silently teach them as clinical rules. Educational coverage is not
   independent specialist medical validation.
7. Preserve existing IDs for saved progress. Rebuilds must remain in book order.
8. Report and merge only the verified batch, then check the actual Pages deployment.

## Publication

GitHub Pages serves `main` at https://deva20045.github.io/Gyne/.
Use the active Arena branch for commits/push/PR; merge by explicit PR number.
Deployment status must be checked separately from merge status.

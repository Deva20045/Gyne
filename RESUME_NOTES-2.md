# PULSE · OBG Mastery Path — Resume Notes

## Current release (2026-10-27)

- **Built chapters: 1–40 of 49**; **3,536 questions / 424 units**.
- Latest batch: **Chapters 36–40, 511 questions / 30 units**.

| Chapter | Scan sequence | Printed folios | Questions | Units |
|---|---|---|---:|---:|
| 36 Female Infertility: Part 1 | 193–198 | 185–190 | 90 | 6 |
| 37 Female Infertility: Part 2 | 199–202 | 191–194 | 58 | 4 |
| 38 Male Infertility | 203–210 | 195–202 | 144 | 8 |
| 39 Contraception: Part 1 | 211–216 | 203–208 | 115 | 6 |
| 40 Contraception: Part 2 | 217–221 | 209–213 | 104 | 6 |

The metadata `page` field retains the repository's **scan-sequence** convention.
Earlier notes called those “Book pages”; do not confuse them with the printed
folio. This batch uses part-05 PDF pages 13–41 inclusive.

## Next work

**Chapter 41 — Contraception: Images** begins at **scan 222 / printed 214**.
The supplied part-05 PDF covers scans 181–225; part-06 covers 226–270 and
part-07 covers 271–272. Check chapter boundaries from the actual page headings.
Chapters 41–49 are not built. Do not include them in the completed batch.

## Files

- `obg-mastery-path.html`: offline deliverable; `index.html` redirects here.
- `data_src/chNN.py`: hand-authored chapter source.
- `data_src/authoring.py`: strict seven-field text parser used by chapters 36–40.
  It parses authored questions, never generates them from OCR.
- `data/chNN.json`: generated questions plus source-page/format metadata.
- `build_chapters.py`: deterministic balanced shuffling, distractor shuffling,
  embedding and numerically ordered idempotent upsert.
- `validate.py`: fail-closed validation using actual JS parsing via Node.
- `tests/test_build.py`: authoring, shuffle, order/idempotency and negative tests.
- `tests/quiz-smoke.cjs`: jsdom interaction test of all 511 new questions,
  feedback/completion, mistake review and progress persistence/reload.
- `audit/ch36-40-coverage.md`: page/topic/question-ID map and source caveats.
- `audit/ocr_193_221.txt`: uncorrected OCR, not an authoritative transcription.
- `PROGRESS.md`: release totals and detailed history.

## Build and test

```sh
python3 build_chapters.py 36 37 38 39 40
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

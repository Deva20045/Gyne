# PULSE: OBG Mastery Path — Resume Notes

## Current state (as of this export)
- **Chapters built:** 1–40 and 45–49 (all validated); 41–44 still open
- **Total questions:** 4,343 / 529 units (zero duplicate IDs, zero duplicate stems,
  `validate.py` PASS including `node --check` on the embedded script)
- **Chapters 1–29:** earlier builds + full re-audits (2,120 questions / 326 units)
- **Chapters 30–35:** scan p160–192 — 905 questions / 68 units
- **Chapters 36–40:** scan p193–221 (printed folios 185–213) — 511 questions / 30 units
  - Ch 36 Female Infertility: Part 1 (scan 193–198) — 90 questions, 6 units
  - Ch 37 Female Infertility: Part 2 (scan 199–202) — 58 questions, 4 units
  - Ch 38 Male Infertility (scan 203–210) — 144 questions, 8 units
  - Ch 39 Contraception: Part 1 (scan 211–216) — 115 questions, 6 units
  - Ch 40 Contraception: Part 2 (scan 217–221) — 104 questions, 6 units
- **Chapters 45–49:** scan p246–272 (printed folios 238–264) — 807 questions / 104 units
  - Ch 45 CIN: Part 2 (scan 246–250 / printed 238–242) — 124 questions, 17 units
  - Ch 46 Cancer Cervix (scan 251–256 / printed 243–248) — 177 questions, 22 units
  - Ch 47 Ovarian Cancer: Part 1 (scan 257–264 / printed 249–256) — 246 questions, 34 units
  - Ch 48 Ovarian Cancer: Part 2 (scan 265–268 / printed 257–260) — 140 questions, 17 units
  - Ch 49 Gynaecology: Miscellaneous Topics (scan 269–272 / printed 261–264) — 120 questions, 14 units
- **Chapters 41–44:** not yet built; chapter 49 ends the printed book at scan 272 / printed 264

## Page-number convention
The metadata `page` field and all progress tables use the repository **scan-sequence**
convention. In PDF parts 05–07 the scan sequence runs **8 ahead of the printed folio**
(scan 193 = printed 185; scan 246 = printed 238). Parts 01–04 coincide. Chapter prose in
PROGRESS.md quotes printed folios for readability and labels them as such.

## Repository layout
- `obg-mastery-path.html` — the single-file offline deliverable (all chapters embedded)
- `index.html` — redirect to the app
- `data_src/chNN.py` — editable authoring source for each built chapter
  (`SECTIONS = [(section, [(unit, [(q, correct, [3 distractors], why, fmt, page), ...]), ...]), ...]`)
- `data/chNN.json` — generated per-chapter artifact with scan-page and format metadata
- `build_chapters.py` — embeds `data_src/chNN.py` into the HTML idempotently
- `validate.py` — fail-closed gate: parses the embedded JS, checks IDs, stems, option
  uniqueness, answers; for chapters ≥36 also source/JSON/HTML synchronisation, monotonic
  scan-page order, mixed formats, ±1 answer balance and no 4-run of identical slots
- `tools/` — OCR and page helpers (`ocrdump.py`, `extract_pages.py`, `preview.py`,
  `rcrop.py`, plus the earlier `ocr2.py`, `crop.py`, `layout.py`)
- `audit/` — raw OCR dumps (p160–192, p193–221, p226–272) and coverage notes

## Next chapter to build
**Chapter 41 — Contraception: Images**, beginning at **scan 222 / printed folio 214**
(part-06 PDF). Then Chapters 42–44 (Endometrial Hyperplasia, Endometrial Cancer,
CIN: Part 1, which ends at scan 245 / printed 237). Closing 41–44 completes the book,
since 45–49 are already live.

## Standard chapter build workflow
1. Extract the embedded scan of each PDF page (`tools/extract_pages.py`), then OCR every
   source page end to end (`tools/ocrdump.py`); re-crop dense or rotated regions at zoom.
2. Read every page as an image before writing: numerals, table cells, brackets, arrow
   labels and figure captions included.
3. Find the chapter boundary from the printed chapter heading on each sheet.
4. Write exhaustive MCQs covering every fact, table cell, comparison, algorithm and
   clinical detail — original questions ordered to match the source, `page` tagged with
   the scan sequence so pages stay monotonic across the chapter (keep review/gap-fill
   questions inside per-page units, never as a trailing mixed-page unit).
5. Run `python3 build_chapters.py NN` (rebuild in ascending order when touching several
   chapters: the upsert appends each block, so build order fixes book order in the HTML).
6. Run `python3 validate.py` until it prints PASS.
7. Review pass: re-check source pages against the new questions for missed points; add
   per-page "Complete Coverage" units where needed, then rebuild and re-validate.

## Key standing instructions from Deva
- Exhaustiveness is non-negotiable — every concept, table cell, comparison, algorithm and
  clinical detail must be captured from the source pages.
- Strictly line-to-line, in book order, chapter by chapter.
- Source-page verification before writing (read the images, don't rely on memory).
- Duplicate ID and duplicate stem checks are mandatory before finalizing any chapter.
- Answer position bias must be corrected after every chapter (~25/25/25/25).
- Use mixed formats — fill-ups, match-the-following, true/false, clinical scenarios,
  odd-one-out, numerics — with non-obvious distractors rather than predictable options.
- After building a chapter, do one review pass for missed points before moving on.
- Report and publish (merge) when a chapter batch is complete.
- Keep messages brief; "Continue" or "Next" means proceed straight to the next chapter.

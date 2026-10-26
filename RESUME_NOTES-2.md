# PULSE: OBG Mastery Path — Resume Notes

## Current state (as of this export)
- **Chapters built:** 1–35 (all validated)
- **Total questions:** 3,025 (zero duplicate IDs, zero duplicate stems, esbuild/`node --check` clean)
- **Chapters 1–29:** earlier builds + full re-audits (2,120 questions / 326 units)
- **Chapters 30–35:** built in the latest session — Book p160–192, 905 new questions / 68 units
  - Ch 30: Disorders of Sexual Development (46XX) (PDF pp. 160–164) — 151 questions, 12 units
  - Ch 31: Disorders of Sexual Development (46XY) (PDF pp. 165–170) — 148 questions, 10 units
  - Ch 32: Primary Amenorrhoea (PDF pp. 171–177) — 195 questions, 17 units
  - Ch 33: Vaginitis and Cervicitis (PDF pp. 178–183) — 149 questions, 11 units
  - Ch 34: Pelvic Inflammatory Disease (PID) (PDF pp. 184–187) — 128 questions, 9 units
  - Ch 35: Genital Tuberculosis (PDF pp. 188–192) — 134 questions, 9 units
- **Chapters 36–49:** not yet built

## Repository layout
- `obg-mastery-path.html` — the single-file offline deliverable (all chapters embedded)
- `index.html` — redirect to the app
- `data_src/chNN.py` — editable authoring source for each built chapter
  (`SECTIONS = [(section, [(unit, [(q, correct, [3 distractors], why, fmt, page), ...]), ...]), ...]`)
- `data/chNN.json` — generated per-chapter artifact with page and format metadata
- `build_chapters.py` — embeds `data_src/chNN.py` into the HTML idempotently
- `validate.py` — duplicate ID, duplicate stem, option-count and answer-distribution gates
- `tools/` — OCR helpers (`ocr2.py`, `crop.py`, `layout.py`) for reading scanned pages
- `audit/` — raw OCR dumps of Book p160–192

## Next chapter to build
**Chapter 36 — Female Infertility: Part 1** (Book p193 onward)
- p193 opens the infertility causes list (tubal cause as the third most common; uterine causes
  including submucous fibroid, septate Mullerian malformation, endometrial polyp and Asherman
  syndrome; cervical and unexplained causes with anti-sperm antibodies and cervicitis) and the
  WHO-style gonadotrophin classification with its three classes and worked examples, plus the
  hyperprolactinaemia note as a separate unclassified cause and the Class II anovulation block.
- p194 starts the tests for ovulation (history-based retrospective tests, mittelschmerz,
  premenstrual syndrome, dysmenorrhoea, then the progesterone-based group).
- Pages 193 onward have been OCR'd into `audit/` only up to p192; rasterise and read every new
  page first.

## To resume in a new chat
1. Attach the latest `obg-mastery-path.html` (or just say **"Continue"** — it is in the repo).
2. Attach the OBG Edition 8 scanned PDF parts covering the next pages.
3. Say **"Continue"** — proceed straight to building **Chapter 36**.
4. After Ch 36: Ch 37 (Female Infertility: Part 2), Ch 38 (Male Infertility), Ch 39–49.

## Chapter order reference (CHAPTER_INDEX, 1-based)
30 Disorders of Sexual Development (46XX) · 31 Disorders of Sexual Development (46XY) ·
32 Primary Amenorrhoea · 33 Vaginitis and Cervicitis · 34 Pelvic Inflammatory Disease (PID) ·
35 Genital Tuberculosis · 36 Female Infertility: Part 1 · 37 Female Infertility: Part 2 ·
38 Male Infertility · 39–49 follow `CHAPTER_INDEX` in the HTML.

## Standard chapter build workflow
1. Rasterise the relevant PDF pages with PyMuPDF (`pip install --break-system-packages pymupdf pillow`).
2. OCR every source page end to end (RapidOCR works well on these scans; install with
   `pip install --break-system-packages rapidocr-onnxruntime opencv-python-headless`).
   Re-crop dense or handwritten regions at 3×–16× zoom.
3. Find the chapter boundary: the next chapter starts at a page headed with the next
   `CHAPTER_INDEX` title.
4. Write exhaustive MCQs covering every fact, table cell, comparison, algorithm and clinical
   detail — original questions, ordered to match the source. Keep them in
   `data_src/chNN.py`.
5. Run `python3 build_chapters.py NN` to embed the chapter and refresh `data/chNN.json`.
6. Run `python3 validate.py` and a `node --check` on the extracted script.
7. Review pass: re-check source pages against the new questions for missed points; add gap-fill
   units labelled "Complete Coverage: ..." where needed, then rebuild.

## Key standing instructions from Deva
- Exhaustiveness is non-negotiable — every concept, table cell, comparison, algorithm and
  clinical detail must be captured from the source pages.
- Strictly line-to-line, in book order, chapter by chapter.
- Source-page verification before writing (read the images, don't rely on memory of similar content).
- Duplicate ID and duplicate stem checks are mandatory before finalizing any chapter.
- Answer position bias must be corrected after every chapter (~25/25/25/25).
- Use mixed formats — fill-ups, match-the-following, true/false, clinical scenarios,
  odd-one-out — with non-obvious distractors rather than predictable recall options.
- After building a chapter, do one review pass for missed points before moving on.
- Report and publish (merge) when a chapter batch is complete.
- Keep messages brief; "Continue" or "Next" means proceed straight to the next chapter.

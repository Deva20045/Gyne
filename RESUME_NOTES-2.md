# PULSE: OBG Mastery Path — Resume Notes

## Current state (as of this export)
- **Chapters built:** 1–29 (fully validated)
- **Total questions:** 2,120 (zero duplicate IDs, esbuild-clean)
- **Chapters 1–14:** original build + full re-audit (gap-filled)
- **Chapter 15 re-audit:** completed (Puberty and Precocious Puberty)
- **Chapters 16–26:** built fresh with rigorous audits
- **Chapters 27–29:** built in the latest sessions:
  - Ch 27: Prolapse: Part 1 (PDF pp. 143–148) — 138 questions, 13 units
  - Ch 28: Prolapse: Part 2 (PDF pp. 149–154) — 112 questions, 14 units
  - Ch 29: Normal Sexual Development (PDF pp. 155–159) — 169 questions, 20 units
- **Chapters 30–49:** not yet built

## Next chapter to build
**Chapter 30 — Disorders of Sexual Development (46XX)** (PDF page 160 onward in `OBG_Vol__1.pdf`)
- Page 160 opens with the 46XX DSD classification: abnormal gonad development (ovotestes, Turner syndrome incl. mosaic) vs ambiguous genitalia (CAH most common, raised maternal androgens, placental aromatase deficiency).
- Page 160 also has the ovotestes details (old term true hermaphrodite, 46XX > 46XY, patterns, internal/external genitalia, puberty outcomes) and the start of Pathophysiology of CAH.
- Pages 160 onward have NOT been viewed in detail yet. Rasterize and read every page first.

## To resume in a new chat
1. Upload the latest `obg-mastery-path.jsx` (attached alongside this note).
2. Upload `OBG_Vol__1.pdf` (Marrow OBG Edition 8, image-based scanned PDF).
3. Say **"Continue"** — proceed straight to building **Chapter 30**.
4. After Ch 30: Ch 31 (DSD 46XY), Ch 32 (Primary Amenorrhoea), then onward through Ch 49.

## Chapter order reference (CHAPTER_INDEX, 1-based)
27 Prolapse: Part 1 · 28 Prolapse: Part 2 · 29 Normal Sexual Development · 30 Disorders of Sexual Development (46XX) · 31 Disorders of Sexual Development (46XY) · 32 Primary Amenorrhoea · 33 Vaginitis and Cervicitis · 34 Pelvic Inflammatory Disease (PID) · 35 Genital Tuberculosis · 36 Female Infertility: Part 1 · 37 Female Infertility: Part 2 · 38 Male Infertility · 39–49 follow in `CHAPTER_INDEX` in the JSX.
Each chapter block is `{ id: 'chNN', number: NN, title: CHAPTER_INDEX[NN-1], sections: [...] }`, inserted before the closing `];` that precedes `const chapterUnitsFlat`.

## Standard chapter build workflow (for new chapters)
1. Rasterize relevant PDF pages: `pdftoppm -f [start] -l [end] -r 100 -jpeg OBG_Vol__1.pdf <dir>/page`
2. View every source page image end to end before writing any questions. Zoom (`-r 200` + PIL crop) on dense or handwritten regions.
3. Find the chapter boundary: the next chapter starts at a page headed with the next CHAPTER_INDEX title.
4. Write exhaustive MCQs covering every fact, table, comparison, algorithm and clinical detail — original questions, ordered to match the source. Keep the data in a Python file as `SECTIONS = [(section_name, [(unit_title, [(question, correct, [3 distractors], why), ...]), ...]), ...]`.
5. Generate JSX with a build script that: assigns answer positions in a seeded balanced shuffle (~25/25/25/25, no run of 4 identical), builds ids `chNN-uK-qJ`, quotes strings safely, and inserts the chapter block via a unique anchor (`    ],\n  },\n];\n\nconst chapterUnitsFlat`).
6. Check for duplicate question stems within the chapter before building (reword repeats).
7. Validate syntax: `esbuild obg-mastery-path.jsx --bundle --loader:.js=jsx --format=esm --outfile=out.js --external:react --external:react-dom --external:lucide-react --external:recharts` (esbuild is at `/opt/npm-tools/node_modules/esbuild/bin/esbuild` in the current sandbox; older sessions had it under tsx's node_modules).
8. Check duplicate IDs with `re.findall(r"id: '([a-z0-9-]+-q\d+)'", content)` and a `Counter`; confirm answer distribution for the new chapter.
9. Copy the validated file to `/mnt/user-data/outputs/obg-mastery-path.jsx` and send it with SendUserFile.
10. Review pass: re-check source pages against the new questions for missed points; add gap-fill units labelled "Complete Coverage: ..." where needed.

## Key standing instructions from Deva
- Exhaustiveness is non-negotiable — every concept, table cell, comparison, algorithm and clinical detail must be captured from the source pages.
- Source-page verification before writing (view the images, don't rely on memory of similar content).
- Duplicate ID checks mandatory before finalizing any chapter.
- Answer position bias must be corrected after every chapter (~25/25/25/25).
- After building a chapter, do one review pass for missed points before moving on.
- Keep messages brief; "Continue" or "Next" means proceed straight to the next chapter with no preamble.

# PULSE · OBG Mastery Path — Progress

Standalone offline quiz built line-by-line from the *Marrow OBG Edition 8* printed notes
(Gynaecology Vol 1, Book p1 → onward).

- Repository: `Deva20045/Gyne`
- Published app: `obg-mastery-path.html` (single offline HTML, no build step to run)
- Editable source of truth for built chapters: `data_src/chNN.py` → `data/chNN.json`
- Rebuild any chapter: `python3 build_chapters.py 41 42 43 44`
- Validate: `python3 validate.py`

## Build status — 49 of 49 chapters built · 4,947 questions · 563 units

**The full printed book is complete.** Chapters 1–49 are all built, in strict
book order. Following completion of Chapters 1–49, Chapters 36–40 underwent a
visual line-by-line audit against `OBG_Vol1_part_05_pages_181-225.pdf` (scans
193–221 / printed folios 185–213), expanding Chapters 36–40 from 511 to 598
questions while preserving all 511 baseline question IDs.

| Chapters | Scan sequence | Printed folios | Questions | Units |
|---|---|---|---:|---:|
| 1–29 | 1–159 | — | 2,120 | 326 |
| 30 Disorders of Sexual Development (46XX) | 160–164 | — | 151 | 12 |
| 31 Disorders of Sexual Development (46XY) | 165–170 | — | 148 | 10 |
| 32 Primary Amenorrhoea | 171–177 | — | 195 | 17 |
| 33 Vaginitis and Cervicitis | 178–183 | — | 149 | 11 |
| 34 Pelvic Inflammatory Disease (PID) | 184–187 | — | 128 | 9 |
| 35 Genital Tuberculosis | 188–192 | — | 134 | 9 |
| **Cumulative 1–35** | **1–192** | | **3,025** | **394** |
| 36 Female Infertility: Part 1 | 193–198 | 185–190 | 120 | 6 |
| 37 Female Infertility: Part 2 | 199–202 | 191–194 | 67 | 4 |
| 38 Male Infertility | 203–210 | 195–202 | 164 | 8 |
| 39 Contraception: Part 1 | 211–216 | 203–208 | 127 | 6 |
| 40 Contraception: Part 2 | 217–221 | 209–213 | 120 | 6 |
| 41 Contraception: Images | 222–226 | 214–218 | 116 | 7 |
| 42 Endometrial Hyperplasia | 227–229 | 219–221 | 79 | 6 |
| 43 Endometrial Cancer | 230–235 | 222–227 | 122 | 8 |
| 44 CIN: Part 1 | 236–245 | 228–237 | 200 | 13 |
| 45 CIN: Part 2 | 246–250 | 238–242 | 124 | 17 |
| 46 Cancer Cervix | 251–256 | 243–248 | 177 | 23 |
| 47 Ovarian Cancer: Part 1 | 257–264 | 249–256 | 246 | 34 |
| 48 Ovarian Cancer: Part 2 | 265–268 | 257–260 | 140 | 17 |
| 49 Gynaecology: Miscellaneous Topics | 269–272 | 261–264 | 120 | 14 |
| **Cumulative 1–49** | **1–272** | | **4,947** | **563** |

The metadata `page` field and all scan-sequence rows use the repository's
**scan-sequence** convention. In PDF parts 05–07 the scan sequence runs 8 ahead
of the printed folio (scan 193 = printed 185; scan 246 = printed 238).
Earlier notes called scan positions “Book pages”; do not confuse the two.
Chapter prose below quotes printed folios for readability and labels them.

## Current release — Chapters 41–44 (scans 222–245 · printed folios 214–237)

**517 new questions / 34 units** in source order, across all 24 sheets from scan
222–245 (part-05 PDF pages 42–45 and part-06 PDF pages 1–20). This closes the
gap between the 36–40 and 45–49 releases, completing all 49 chapters.

- 369 fill-ups, 51 clinical/source-check scenarios, 39 match-the-following,
  30 paired-statement true/false and 28 odd-one-out questions.
- All five requested formats appear in each chapter. Each question has four
  distinct options and an explanatory answer; paired T/F uses four truth combinations.
- Reviewed each rasterised source sheet and its tables, arrows, captions and
  continuation headings. Ambiguous numerals (condom failure rates, Mala N/D doses,
  IUCD lifespans/release rates, implant dose/day, Essure timeline, sterilisation
  rankings, EH thresholds, cancer grades/stages, Bethesda counts, vaccine
  valencies/doses) were re-read in magnified crops. Raw OCR aid:
  [`audit/ocr_222_246.txt`](audit/ocr_222_246.txt) (not authoritative).
  Full topic/question-ID map: [`audit/ch41-44-coverage.md`](audit/ch41-44-coverage.md).
- Chapter boundaries were confirmed from the actual page headings: CIN: Part 2
  starts at scan 246 / printed 238 and is not incorporated here.
- Source inconsistencies and obsolete/unsafe annotations are flagged in explanations
  rather than silently turned into clinical recommendations — including the female
  condom “can be used twice” line, sponge “TSS: Nil”, Nexplanon radiopacity
  contradiction, withdrawn Essure, edition-specific Mirena/emergency-contraception
  note, “cancer cervix: m/c cause of PMB in India”, E2→E6/E7 shorthand, ACOG
  5-yearly label and old versus WHO SAGE vaccine schedules.
- Balanced answer slots without a predictable four-item cycle; distractor order
  is shuffled too. Rebuilds remain in numeric book order and existing progress IDs
  are unchanged. Both this release and the 45–49 release were merged without
  altering each other's chapters.

### Verification

```sh
python3 build_chapters.py 41 42 43 44
python3 validate.py
python3 -m unittest discover -s tests -v
npm ci
node tests/quiz-smoke.cjs
# Or, after npm ci: npm test
```

Validation fails on duplicate IDs/stems, bad options/answers, disproportionate
correct-option length clues (chapters 36–40), stale new-chapter source/JSON/HTML,
missing formats, out-of-order source pages or unbalanced new answer slots.
JavaScript syntax is checked by Node. The DOM smoke test plays **all 1,922
questions in chapters 36–49**, checks feedback and unit completion (including
partially completed units with preserved legacy IDs and inserted sub-IDs), and
tests mistake review and saved-progress reload without losing an existing
chapter's progress. It also verifies all 49 chapter cards are present in numeric order.
Automated tests check structure/behaviour, not medical accuracy or a formal proof
of exhaustive source coverage.

The app remains a single offline HTML file; Node/jsdom are development-test
requirements only. No runtime dependency or network call was added.

## Previous release — Chapters 45 to 49 (scans 246–272 · printed folios 238–264)

**807 questions / 105 units** across 27 sheets, built in parallel and merged
first. All sheets were extracted at native resolution, OCR'd end to end and read
page by page as images before authoring. Chapters appear in strict printed order;
raw OCR aids: `audit/ocr_hi_226_249.txt` and `audit/ocr_hi_250_272.txt`.

- Ch 45 CIN: Part 2 (246–250): dysplasia-risk table, WHO management pathways,
  pap-smear inferences and infections, abnormal-pap algorithm, report-wise
  management, colposcopy, CIN management tree, cryoablation, LLETZ/LEEP, special
  scenarios, cone biopsy and p-16 protein.
- Ch 46 Cancer Cervix (251–256): type tree with HPV 16/18, features and symptoms,
  spread and nodal drainage, EBRT fields, post-coital bleeding algorithm,
  investigations, full FIGO table, surgery versus chemoradiation, radical
  trachelectomy, brachy/teletherapy and post-surgery risk tree.
- Ch 47 Ovarian Cancer: Part 1 (257–264): functional cysts, benign/malignant
  adnexal table, malignancy USG strip, cyst management, CA-125, pregnancy
  pathologies, risk/protective tables, genetic syndromes, screening, WHO and
  epithelial classifications, marker table, dermoid, dysgerminoma, yolk sac.
- Ch 48 Ovarian Cancer: Part 2 (265–268): sex cord stromal tree, granulosa
  (FOXL2, Call-Exner), fibroma and Meig's versus pseudo-Meig's, metastatic and
  Krukenberg, FIGO table, surgical staging, surgery, chemotherapy, Sertoli-Leydig.
- Ch 49 Gynaecology: Miscellaneous Topics (269–272): SUI definition and Q-tip
  test, Burch versus TOT versus TVT, urinary fistula and three-swatch test, VVF
  causes, repair timing/techniques/post-op rules, OHSS chain and prevention.

## Audited & expanded — Chapters 36–40 (scans 193–221 · printed folios 185–213)

**598 questions / 30 units** across 29 sheets (expanded from 511 baseline
questions via visual line-by-line review of PDF pages 13–41 + 13 magnified crops,
preserving all 511 original IDs and inserting 87 sub-IDs in strict within-page
reading order): Female Infertility Parts 1–2, Male Infertility and Contraception
Parts 1–2. Granular line-by-line source-to-question map and source caveats
(including `α oesthin pill` for *Lo Loestrin*, `Age : ≥28yrs` for MoHFW `≥22yrs`,
`DMPA ≥ 4wks` postpartum note, `50%` fecundity vs `20%` fecundability, Yuzpe
inverted pill counts, mis-bracketed Cu-IUCD/Ulipristal bullets, `HCG` for `HSG`
before IUI, `1. Varicocele` under obstructive azoospermia, and maturation-index
`0/10/90` contradiction): [`audit/ch36-40-coverage.md`](audit/ch36-40-coverage.md).

## Earlier release — Chapters 30 to 35 (scans 160–192)

All 33 scanned sheets covering scans 160–192 were rasterised, OCR'd and re-read at
high zoom for every numeral, table cell, arrow label and figure caption before a single
question was written. Chapters appear in strict printed order.

### Chapter 30 — Disorders of Sexual Development (46XX) (scans 160–164; 151 questions / 12 units)

Opens with the two-armed 46XX tree — abnormal development of gonads (ovotestes; Turner's
syndrome with its 45XO most-common and mosaic 45XO/46XY dysgenetic-testis arms) against
ambiguous genitalia (raised maternal androgens from androgen-secreting tumour, luteoma and
androgenic drugs; placental aromatase deficiency with its `aromatase ↓ → estrogen ↓` and
`↑ maternal androgen` lines). Ovotestes is then worked in printed order: old term true
hermaphrodite, karyotype 46XX > 46XY, the two gonadal patterns, internal genitalia
following the gonad on each side, the ambiguous male-like external genitalia attributed
to adrenal testosterone, gynaecomastia at puberty and menstruation in a quarter. The CAH
block begins with `m/c cause of DSD in 46XX` and `ambiguous genitalia in females`, then
the full adrenal steroidogenic map — ACTH, pregnenolone, the 17α-hydroxylase and
17,20-lyase arm to DHEA, the 3β-HSD steps, the 21α- and 11β-hydroxylase chains to
aldosterone and cortisol, aromatase to E1 and E2, and the DHEA → androstenedione →
testosterone → estrogen sequence. Clinical features are split by deficient hormone and
by lost negative feedback, followed by the 17-OH progesterone algorithm (below 200 ng
rules out, 200–800 ng to ACTH stimulation, ≥800 ng confirms), treatment started without
waiting for karyotyping, the impalpable-gonad emergency list and prenatal
dexamethasone from 4–5 weeks to CVS at 10–11 weeks. The chapter closes on
17α-hydroxylase/17,20-lyase deficiency, 3β-HSD deficiency, P450 oxidoreductase
deficiency with Antley-Bixler craniosynostosis and the three-column enzyme-defect summary.

### Chapters 31–35 (scans 165–192; 754 questions / 56 units)

Disorders of Sexual Development (46XY) — complete/partial AIS, Swyer syndrome and
5α-reductase deficiency; Primary Amenorrhoea; Vaginitis and Cervicitis; Pelvic
Inflammatory Disease; and Genital Tuberculosis. All were built with the same
source-image review, strict page order, mixed question formats and balanced answer
slots described for the current release.

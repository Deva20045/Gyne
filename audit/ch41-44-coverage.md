# Chapters 41–44: source-order coverage and review record

Date: 2026-10-27. Source: supplied Marrow OBG Edition 8 scans, Vol 1 part 05
(scans 181–225) and part 06 (scans 226–270).

## Page-number convention

Existing `page` metadata uses the **scan sequence**, not the printed folio. For
this batch, scan 222–245 = printed 214–237. Scans 222–225 are part-05 PDF pages
42–45; scans 226–245 are part-06 PDF pages 1–20. No page from the following
**CIN: Part 2** chapter (starting scan 246 / printed 238 / part-06 page 21) was
incorporated. Chapter boundaries were confirmed from the actual page headings.

## Method and limits

- Rasterised all 24 requested source sheets (plus scan 246 to confirm the next
  chapter heading) at high resolution; OCR produced a raw aid at
  `audit/ocr_222_246.txt`, which was **not** trusted as authority.
- Visually read every sheet and compared headings, tables, arrows, captions and
  continuation blocks against the authoring sections. Zoom crops resolved
  ambiguous numerals: condom failure rates, Mala N/D tablet doses, IUCD
  lifespans and release rates, implant dose/day, Essure confirmation timeline,
  sterilisation outcome rankings, EH sampling thresholds, cancer grades and FIGO
  stages, PMB causes, Bethesda counts, HPV E6/E7, VIA/VILI inference and vaccine
  valencies/doses.
- Every question is hand-authored with four explicit options and an explanation.
  The helper only parses authored text; it does not generate questions from OCR.
- Page/section order is preserved, including same-page continuation sections.
  Compound questions can cover multiple adjacent lines; there is not necessarily
  one question per printed line.
- This is an educational source-coverage review, not independent specialist
  medical validation. Historical thresholds, withdrawn devices and potentially
  unsafe annotations are labelled in explanations. Use current local clinical
  guidance, not quiz answers, for care.

## Coverage map

Each row identifies the actual authored topic block and its question range.
All IDs within the range occur in source order in the generated JSON and HTML.
Part-05 pages are labelled `p05-N`, part-06 pages `p06-N`.

| Chapter | Scan / printed / PDF page | Topic block | Question IDs | Count |
|---|---|---|---|---:|
| 41 | 222 / 214 / p05-42 | Condoms, HWY and STI protection | `ch41-u1-q1`–`ch41-u1-q19` | 19 |
| 41 | 222 / 214 / p05-42 | Today sponge and diaphragm | `ch41-u2-q1`–`ch41-u2-q13` | 13 |
| 41 | 223 / 215 / p05-43 | Mala N/D, IUCD generations and Copper T 380A | `ch41-u3-q1`–`ch41-u3-q16` | 16 |
| 41 | 223 / 215 / p05-43 | Multiload 375 and Mirena (LNG 20) | `ch41-u4-q1`–`ch41-u4-q13` | 13 |
| 41 | 224 / 216 / p05-44 | Mirena effects, Gynefix, implants, LARC and Essure | `ch41-u5-q1`–`ch41-u5-q22` | 22 |
| 41 | 225 / 217 / p05-45 | Laparoscopic ligation, mini lap, Pomeroy and Parkland | `ch41-u6-q1`–`ch41-u6-q18` | 18 |
| 41 | 226 / 218 / p06-1 | Irving, Uchida, Madlener, Kroener and outcome rankings | `ch41-u7-q1`–`ch41-u7-q15` | 15 |
| 42 | 227 / 219 / p06-2 | Overview of EH, investigations and the AUB-M label | `ch42-u1-q1`–`ch42-u1-q13` | 13 |
| 42 | 227 / 219 / p06-2 | Endometrial sampling and its age-based indications | `ch42-u2-q1`–`ch42-u2-q17` | 17 |
| 42 | 228 / 220 / p06-3 | Fractional curettage, hysteroscopy and EB report pathways | `ch42-u3-q1`–`ch42-u3-q14` | 14 |
| 42 | 228 / 220 / p06-3 | Metropathia hemorrhagica | `ch42-u4-q1`–`ch42-u4-q10` | 10 |
| 42 | 229 / 221 / p06-4 | EH without atypia: progesterone and surveillance | `ch42-u5-q1`–`ch42-u5-q12` | 12 |
| 42 | 229 / 221 / p06-4 | EH with atypia and indications for FC plus hysteroscopy | `ch42-u6-q1`–`ch42-u6-q13` | 13 |
| 43 | 230 / 222 / p06-5 | Associated factors, protective factors and familial syndromes | `ch43-u1-q1`–`ch43-u1-q16` | 16 |
| 43 | 231 / 223 / p06-6 | Familial syndromes, screening and histopathologic types | `ch43-u2-q1`–`ch43-u2-q17` | 17 |
| 43 | 231 / 223 / p06-6 | Grading of adenocarcinoma | `ch43-u3-q1`–`ch43-u3-q7` | 7 |
| 43 | 232 / 224 / p06-7 | Type 1 versus type 2 carcinoma, presentation and spread | `ch43-u4-q1`–`ch43-u4-q19` | 19 |
| 43 | 232 / 224 / p06-7 | Diagnostic algorithm | `ch43-u5-q1`–`ch43-u5-q9` | 9 |
| 43 | 233 / 225 / p06-8 | Imaging, surgical staging and FIGO 2009 | `ch43-u6-q1`–`ch43-u6-q19` | 19 |
| 43 | 234 / 226 / p06-9 | Molecular classification, prognosis and surgical staging | `ch43-u7-q1`–`ch43-u7-q19` | 19 |
| 43 | 235 / 227 / p06-10 | Post-op management and postmenopausal bleeding | `ch43-u8-q1`–`ch43-u8-q16` | 16 |
| 44 | 236 / 228 / p06-11 | Anatomy of the cervix and pubertal vaginal acidity | `ch44-u1-q1`–`ch44-u1-q13` | 13 |
| 44 | 237 / 229 / p06-12 | Transformation zone, metaplasia, Nabothian cysts and applied anatomy | `ch44-u2-q1`–`ch44-u2-q15` | 15 |
| 44 | 237 / 229 / p06-12 | Histopathology: metaplasia versus dysplasia | `ch44-u3-q1`–`ch44-u3-q11` | 11 |
| 44 | 238 / 230 / p06-13 | CIN grading and the role of Pap smear | `ch44-u4-q1`–`ch44-u4-q14` | 14 |
| 44 | 238 / 230 / p06-13 | Conventional Pap smear instruments and samples | `ch44-u5-q1`–`ch44-u5-q9` | 9 |
| 44 | 239 / 231 / p06-14 | Pap smear procedure, liquid-based cytology and Bethesda counts | `ch44-u6-q1`–`ch44-u6-q17` | 17 |
| 44 | 239 / 231 / p06-14 | Risk factors for cancer cervix | `ch44-u7-q1`–`ch44-u7-q13` | 13 |
| 44 | 240 / 232 / p06-15 | HPV biology, oncogenes and low-risk disease | `ch44-u8-q1`–`ch44-u8-q19` | 19 |
| 44 | 241 / 233 / p06-16 | Prevention, WHO 2030 goals and screening methods | `ch44-u9-q1`–`ch44-u9-q18` | 18 |
| 44 | 242 / 234 / p06-17 | Screening algorithms, LLETZ and cryosurgery prerequisites | `ch44-u10-q1`–`ch44-u10-q15` | 15 |
| 44 | 243 / 235 / p06-18 | HPV DNA testing, VIA/VILI inference and ectropion | `ch44-u11-q1`–`ch44-u11-q19` | 19 |
| 44 | 244 / 236 / p06-19 | ACOG screening intervals and HPV vaccines | `ch44-u12-q1`–`ch44-u12-q19` | 19 |
| 44 | 245 / 237 / p06-20 | WHO SAGE doses, eligibility and vaccine schedule | `ch44-u13-q1`–`ch44-u13-q18` | 18 |

## Format and answer totals

| Chapter | fillup | scenario | match | tf | odd | Total | A–D slots |
|---|---:|---:|---:|---:|---:|---:|---|
| 41 | 83 | 13 | 8 | 5 | 7 | 116 | 29 / 29 / 29 / 29 |
| 42 | 54 | 9 | 6 | 5 | 5 | 79 | 20 / 20 / 20 / 19 |
| 43 | 89 | 13 | 8 | 7 | 5 | 122 | 31 / 30 / 31 / 30 |
| 44 | 143 | 16 | 17 | 13 | 11 | 200 | 50 / 50 / 50 / 50 |
| **Batch** | **369** | **51** | **39** | **30** | **28** | **517** | — |

All five requested formats occur in every chapter. True/false questions use two
statements and four truth combinations, not one true option with three
near-identical false options. Distractors are deliberately non-obvious, drawing
plausible alternatives from neighbouring tables, adjacent drug/device figures
and reversed arrows rather than obvious antonyms.

## Source discrepancies and cautions retained at their source location

- Scan 222: the female condom “can be used twice” and “Polyurethane condom”
  material cells are labelled as edition-specific source wording, not current
  product instructions; condoms are single-use in current guidance.
- Scan 222: Today Sponge “Chances of toxic shock syndrome: Nil” is flagged as
  an overconfident absolute, not a clinical guarantee; the 24-hour multiple-use
  and 30-hour maximum lines are kept distinct.
- Scan 223: Mala N/D tablet counts and iron dose, CuT 380A lifespan and copper
  release rate, and Multiload 375/Mirena LNG 20 dose and daily release are
  studied as printed source values, not as prescriptions.
- Scan 223: Mirena “Not used as emergency contraception” is marked as a
  time-stamped (2024) edition note that must not be generalised.
- Scan 224: Nexplanon is printed with both “Barium sulfate in stem” and “Not
  radiopaque”; the contradiction is flagged. Implanon/Nexplanon dose-per-day,
  LARC ranking and the Gynefix nylon-thread component are source study points.
- Scan 224: Essure (99% success, 3-month confirmation) is explicitly identified
  as a **historical/withdrawn** device; a source-check question rejects
  recommending it today.
- Scan 225–226: Pomeroy, Parkland, Irving, Uchida, Madlener and Kroener
  techniques and the mixed clip/ring/method outcome ranking lines are studied as
  source annotations; the ranking conflation is flagged.
- Scan 227–228: EH overview, AUB-M label, TVS/EB/FC/hysteroscopy “gold standard”
  versus “IOC” tension, and age-based endometrial sampling indications are kept
  in printed order. The perimenopausal “EB regardless of normal USG” line and
  edition-specific thresholds are labelled. FC+hysteroscopy is not silently
  rewritten as the sole first-line investigation.
- Scan 229: EH without atypia (oral cyclical progestogen, 12-day/no-contraception
  notes) and EH with atypia (FC+hysteroscopy, TAH) are marked as edition-specific
  study points; the “TAH → uterus + cervix” line is not read as making cervix
  removal optional.
- Scan 230: tamoxifen ranking and its “min 2 months, ideal 3 months” washout
  annotation are flagged as study shorthand; tamoxifen is not presented as a
  drug to be used to induce pregnancy.
- Scan 231: “prophylactic TAH+BSO at completed family by 40 years” is labelled as
  historical programme-style criteria, not a rule overriding individual
  counselling. Histopathologic types, grading and screening are source content.
- Scan 232–234: Type 1/2 comparison, diagnostic algorithm, imaging, FIGO 2009,
  molecular classification and surgical staging are studied in printed order.
  The FC+hysteroscopy/TVS/EB algorithm inconsistency is flagged at `ch43-u5-q9`.
- Scan 235: the PMB causes list says polyp is most common but also adds “Cancer
  cervix: m/c cause of PMB in India”; the contradiction is flagged rather than
  taught.
- Scan 238–239: CIN grades, biopsy diagnosis, Pap smear instruments, LBC and
  Bethesda counts are kept in order; “LBC much more sensitive” is not asserted
  without qualification, and the source “most specific / 55% sensitivity” mix
  is labelled as study shorthand.
- Scan 240: “E2 protein → upregulate E6, E7” is flagged as shorthand about
  early-gene regulation, not a complete molecular account. HPV subtypes and
  low-risk disease are source content.
- Scan 241–243: WHO 2030 goals, LLETZ/cryo prerequisites, HPV DNA testing,
  VIA/VILI inference and ectropion are studied in printed order.
- Scan 244: the ACOG flow “Repeat 5 yearly” between 21 and 30 years is labelled
  as study shorthand; interval recommendations change and must be checked
  against current guidelines.
- Scan 245: the WHO SAGE dose/eligibility table and the separately printed “old”
  vaccine schedule are kept apart; a source-check question directs the learner
  to current recommendations rather than the obsolete schedule. Syncope and
  post-injection observation are retained as practical precautions.

## Engineering verification

- `python3 validate.py`: parses actual JavaScript data using Node, checks every
  embedded question, checks generated JSON against both HTML and authoring
  source for chapters 36–44, and fails on errors. Result: **4,053 questions /
  458 units** across 44 chapters, no duplicate IDs/stems.
- `python3 -m unittest discover -s tests -v`: answer-shuffle invariants,
  malformed authoring rejection, validator negative tests, page coverage for
  scans 193–245 and idempotent out-of-order rebuilds for chapters 36–44.
- `node tests/quiz-smoke.cjs` (after `npm ci`): DOM interaction test answers all
  517 new questions across all 34 units, verifies feedback/completion, mistake
  review, reload persistence and existing progress retention.
- Chapter-level answer counts differ by at most one, without the forced
  four-answer permutation cycle. Existing question IDs/options/answers are
  unchanged; chapter blocks remain in numeric book order.
- Automated checks establish structure and behaviour, not medical accuracy or a
  formal proof of exhaustive coverage.

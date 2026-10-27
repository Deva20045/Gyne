# PULSE · OBG Mastery Path — Progress

Standalone offline quiz built line-by-line from the *Marrow OBG Edition 8* printed notes
(Gynaecology Vol 1, Book p1 → onward).

- Repository: `Deva20045/Gyne`
- Published app: `obg-mastery-path.html` (single offline HTML, no build step to run)
- Editable source of truth for built chapters: `data_src/chNN.py` → `data/chNN.json`
- Rebuild any chapter: `python3 build_chapters.py 36 37 38 39 40`
- Validate: `python3 validate.py`

## Build status — 40 of 49 chapters built · 3,536 questions · 424 units

| Chapters | Scan sequence | Questions | Units |
|---|---:|---:|---:|
| 1–29 | 1–159 | 2,120 | 326 |
| 30 Disorders of Sexual Development (46XX) | 160–164 | 151 | 12 |
| 31 Disorders of Sexual Development (46XY) | 165–170 | 148 | 10 |
| 32 Primary Amenorrhoea | 171–177 | 195 | 17 |
| 33 Vaginitis and Cervicitis | 178–183 | 149 | 11 |
| 34 Pelvic Inflammatory Disease (PID) | 184–187 | 128 | 9 |
| 35 Genital Tuberculosis | 188–192 | 134 | 9 |
| 36 Female Infertility: Part 1 | 193–198 | 90 | 6 |
| 37 Female Infertility: Part 2 | 199–202 | 58 | 4 |
| 38 Male Infertility | 203–210 | 144 | 8 |
| 39 Contraception: Part 1 | 211–216 | 115 | 6 |
| 40 Contraception: Part 2 | 217–221 | 104 | 6 |
| **Cumulative 1–40** | **1–221** | **3,536** | **424** |

## Current release — Chapters 36–40

**511 new questions / 30 units** in source order, across all 29 sheets from scan
193–221 (**printed folios 185–213**, part-05 PDF pages 13–41).
Earlier progress notes called scan positions “Book pages”; use the mapping above
when locating printed page numbers.

- 269 fill-ups, 126 clinical/source-check scenarios, 55 match-the-following,
  43 odd-one-out and 18 paired-statement true/false questions.
- All five requested formats appear in each chapter. Each question has four
  distinct options and an explanatory answer; paired T/F uses four truth combinations.
- Reviewed each rasterised source sheet and its tables, arrows, captions and
  continuation headings. Selected unclear numerals were reviewed in magnified crops.
  Full topic/question-ID map: [`audit/ch36-40-coverage.md`](audit/ch36-40-coverage.md).
- Source inconsistencies are identified where they occur, rather than silently
  turning erroneous or obsolete annotations into clinical recommendations.
- Improved answer shuffling: globally balanced slots without the prior forced
  permutation every four questions; distractor order is shuffled too.
- Rebuilding any chapter now retains numerical chapter order. Corrected the
  pre-existing 35-before-34 block ordering. Existing progress IDs remain stable.
- The strengthened validator also found a double-quoted legacy duplicate stem
  missed by the old regular expression; reworded `ch29-u10-q6` without changing
  its answer, options, ID or meaning.

### Verification

```sh
python3 build_chapters.py 36 37 38 39 40
python3 validate.py
python3 -m unittest discover -s tests -v
npm ci
node tests/quiz-smoke.cjs
# Or, after npm ci: npm test
```

Validation fails on duplicate IDs/stems, bad options/answers, stale new-chapter
source/JSON/HTML, missing formats, out-of-order source pages or unbalanced new
answer slots. JavaScript syntax is checked by Node. The DOM smoke test plays
**all 511 new questions**, checks feedback and unit completion, and tests mistake
review and saved-progress reload without losing an existing chapter's progress.
Automated tests check structure/behaviour, not medical accuracy or a formal proof
of exhaustive source coverage.

The app remains a single offline HTML file; Node/jsdom are development-test
requirements only. No runtime dependency or network call was added.

## Previous release — Chapters 30 to 35 (scan p160–192)

All 33 scanned sheets covering Book p160–192 were rasterised, OCR'd and re-read at
high zoom for every numeral, table cell, arrow label and figure caption before a single
question was written. Chapters appear in strict printed order.

### Chapter 30 — Disorders of Sexual Development (46XX) (Book p160–164; 151 questions / 12 units)

Opens with the two-armed 46XX tree — abnormal development of gonads (ovotestes; Turner's
syndrome with its 45XO most-common and mosaic 45XO/46XY dysgenetic-testis arms) against
ambiguous genitalia (raised maternal androgens from androgen-secreting tumour, luteoma and
androgenic drugs; placental aromatase deficiency with its `aromatase ↓ → estrogen ↓` and
`↑ maternal androgen` lines). Ovotestes is then worked in printed order: old term true
hermaphrodite, karyotype 46XX > 46XY, the two gonadal patterns (one ovary and one testis on
each side most common; ovarian plus testicular tissue on both sides least common), internal
genitalia following the gonad on each side, the ambiguous male-like external genitalia
attributed to adrenal testosterone, `m/c presumed as male at birth`, gynaecomastia in
three-quarters or more from estrogen and menstruation in a quarter at puberty. The CAH block
begins with `m/c cause of DSD in 46XX` and `ambiguous genitalia in females`, then the full
adrenal steroidogenic map — ACTH, pregnenolone, the 17α-hydroxylase and 17,20-lyase arm to
DHEA, the 3β-HSD steps, the 21α- and 11β-hydroxylase mineralocorticoid and glucocorticoid
chains to aldosterone and cortisol, aromatase to E1 and E2, and the DHEA → androstenedione
→ testosterone (stronger androgen) → estrogen sequence. Clinical features are split by
deficient hormone (aldosterone: hyponatraemia, salt-water wasting with dehydration,
hypotension, hyperkalaemia, metabolic acidosis; cortisol: hypoglycaemia) and by lost negative
feedback (raised ACTH, raised androgens, raised 17-OH progesterone, ambiguous genitalia in
females with normal male external genitalia). The 17-OH progesterone algorithm follows —
below 200 ng rules out, 200–800 ng goes to the ACTH stimulation test, 800 ng or more confirms
— with treatment started without waiting for karyotyping and the impalpable-gonad medical
emergency list (glucocorticoids, mineralocorticoids, correct electrolytes, later clitoromegaly
surgery; deferred investigations of 17-OH progesterone, electrolytes, glucose, karyotyping
or FISH). Prenatal dexamethasone runs from `previous child with CAH` through 4–5 weeks
(maximum delay 9 weeks) to CVS at 10–11 weeks with the continue-or-stop decision, alongside
the printed `CAH: X-linked recessive disorder` note. The chapter closes on the other causes —
17α-hydroxylase/17,20-lyase deficiency (`leads to DSD in XY individuals`, normal female fetus,
ambiguous male fetus from low testosterone), 3β-HSD deficiency (low aldosterone and cortisol,
high weak-androgen DHEA, ambiguity in both sexes), P450 oxidoreductase deficiency as the newly
diagnosed form with P450 as electron donor and Antley-Bixler craniosynostosis — and the
three-column summary of ambiguous genitalia by enzyme defect (female only: 21α-hydroxylase
most common and 11β-hydroxylase; male only: 17α-hydroxylase and 17,20-lyase; both sexes:
3β-HSD and P450 OR).

### Chapter 31 — Disorders of Sexual Development (46XY) (Book p165–170; 148 questions / 10 units)

Opens with the two-column 46XY tree — female external genitalia (complete AIS most common,
Swyer syndrome, 5α-reductase deficiency, LH receptor defect) against ambiguous genitalia
(partial AIS, ovotestis, and the CAH group of 17α-hydroxylase, 17α-lyase, 3β-HSD and P450 OR
deficiency) — then the shared characteristics: considered female at birth except ovotestis,
primary amenorrhoea at puberty, and the `female with 1° amenorrhoea plus inguinal hernia —
suspect XY genotype` clue with its undescended-testis consequences (palpable abdominal gonads,
raised malignancy risk, gonadectomy, gonadoblastoma as the commonest tumour and dysgerminoma
as the commonest malignancy). Complete AIS is then traced cell by cell — X-linked recessive,
normal SRY, testis, Leydig and Sertoli cells; testosterone normal but resisted; FSH driving
inhibin B feedback and AMH-driven Mullerian regression giving no tubes, uterus, cervix or
upper vagina; testosterone resistance regressing the Wolffian duct and leaving an abdominal
testis with bilateral inguinal hernia; DHT resistance feminising the exterior; then puberty
with scanty Tanner 1–2 hair against proper Tanner 4–5 breast from unresisted aromatised
estrogen and a possibly blind-ending vagina. The hormonal profile (raised GnRH, raised LH,
normal FSH, testosterone raised versus females) is contrasted with PCOS on the
primary-versus-secondary amenorrhoea axis, and management runs continue-female-identity →
gonadectomy at 14–16 years once breast development completes → estrogen without progesterone
because the uterus is absent → McIndoe or laparoscopic Vecchietti vaginoplasty near marriage,
with the note that biological children are impossible. Partial AIS follows (partial sensitivity,
Wolffian development, poorly formed male internal genitalia, ambiguous genitalia, female at
birth, Tanner 4–5 breast with Tanner 1–2 hair, clitoromegaly and labioscrotal fusion, most
common cause of ambiguous genitalia in 46XY and of male pseudohermaphroditism, same
management but gonadectomy as soon as possible because the testis virilises at puberty).
Swyer syndrome is built from its two causes (idiopathic, SRY point mutation) through the four
absent hormones and their four consequences (no testosterone → no male internal genitalia;
no AMH → female internal genitalia; no DHT → female external genitalia; no inhibin B → raised
FSH) to absent breasts, scanty hair, the delayed-puberty/amenorrhoea/inguinal-hernia triad and
immediate gonadectomy with one year of estrogen and vaginoplasty. 5α-reductase deficiency
closes the chapter: normal testis with normal Sertoli and Leydig cells, testosterone driving
fully formed male internal organs, AMH regressing the Mullerian duct, the blocked
testosterone-to-DHT step leaving female external genitalia at birth, then pubertal virilisation
with clitoromegaly, increased muscle mass and voice deepening against absent breasts and absent
pubic or axillary hair — plus the `in AIS testosterone becomes estrogen` note and the
three-row partial-AIS-versus-5α-reductase table (timing of clitoromegaly, breast, internal
genitalia).

### Chapter 32 — Primary Amenorrhoea (Book p171–177; 195 questions / 17 units)

Begins with the definition anchored to thelarche (at least 3 years without menstruation) and
its Tanner note (breast budding stage 2, mons pubis hair stage 3), then the cause split
(gonadal dysgenesis most common overall with Turner's exceeding Swyer's; Mullerian agenesis
most common in India where Swyer's exceeds Turner's) and the organic causes table by organ
(hypothalamus: Kallmann syndrome and craniopharyngioma with hypogonadotropic hypogonadism;
ovary: 45XO, 46XY and 46XX pure gonadal dysgenesis with hypergonadotropic hypogonadism and
low testosterone; uterus: Mullerian agenesis with normal hormones and AIS with raised LH,
normal FSH and male-level testosterone). The uterus-positive/uterus-negative split and the
GnRH → FSH/LH → estrogen/progesterone → uterus axis precede the five-step workup (physical
examination of breast and pubic hair; UPT especially with adequate breast development; USG
for uterine status; FSH, LH and estrogen; karyotyping as the best investigation).
Cryptomenorrhoea is then covered in full — normal menstruation failing to exit through an
outflow obstruction, the three causes (imperforate hymen most common, transverse vaginal
septum, vaginal atresia or agenesis), the normal karyotype, gonads and hormones, cyclical
pain with possible urinary retention, haematocolpos and haematometra with retrograde
menstruation causing endometriosis and increasing dysmenorrhoea, the tense bulging hymen
with positive cough impulse against the flat hymen of vaginal agenesis, and MRI as the
investigation of choice for differentiating causes and measuring septal thickness. The
gonadal-dysgenesis-versus-Kallmann similarities (absent breasts, hypoplastic infantile uterus,
scanty hair) and their hormonal contrast precede Turner syndrome in full — 45XO most common
with the rare 45XO/46XY mosaic, streak ovaries, the remove-or-leave rule for malignant versus
non-malignant gonads, short stature from SHOX, webbed neck, low posterior hairline, shield
chest, widely spaced nipples, sensorineural hearing loss, the diabetes/Hashimoto/celiac
autoimmune triad, cubitus valgus, bicuspid aortic valve exceeding coarctation — with its
investigation set (karyotyping to rule out mosaicism, ECHO, renal ultrasound for horseshoe
kidney, thyroid profile, audiometry) and management (E plus P because the uterus is present,
with fasting glucose and lipid profile). Swyer syndrome (46XY, raised FSH and LH, present
uterus, absent breasts, dysgenetic testis, normal height) is contrasted with Turner's, and
Kallmann syndrome closes the uterus-present group (46XX, functionally normal ovaries, KAL-1
gene, anosmia, normal stature, low FSH and LH, delayed puberty with infertility, pulsatile
GnRH). The absent-uterus comparison then runs row by row across karyotype, gonads, internal
and external genitalia, breast, pubic hair, MRKH-associated renal and skeletal anomalies,
testosterone, LH, FSH, biological children and the IVP plus skeletal X-ray investigations,
before vaginoplasty timing and technique, gonadectomy with estrogen, and the four-column
hormone-pattern summary that groups every condition by its gonadotrophin state.

### Chapter 33 — Vaginitis and Cervicitis (Book p178–183; 149 questions / 11 units)

Opens with the vaginal defence mechanism — polymicrobial flora, predominant Gram-positive
Doderlein lactobacilli appearing at puberty and disappearing at menopause, glycogen in the
stratified epithelium converted to lactic acid and hydrogen peroxide giving the acidic
protective pH, estrogen responsible for the glycogen, candida surviving in the acidic pH —
then the normal pap smear (Doderlein bacilli and superficial cells) and physiological
leucorrhoea (increased at ovulation and before menstruation, thin and watery under estrogen
in the first half, thick under progesterone in the second half, colourless and odourless
without pruritus or dysuria) with bacterial vaginosis discharge as the differential. The
three-vaginitis table is worked cell by cell: organisms (Gardnerella with mycoplasma and
Mobiluncus; Candida albicans; Trichomonas vaginalis as a flagellated protozoan), mechanism
(altered flora with BV the commonest vaginitis; pregnancy, immunocompromise and
antibiotics/steroids/OCP for candida which is the commonest vaginitis in pregnancy; alkaline
pH and coexistence with BV for trichomonas), discharge (greyish white, curdy white cottage
cheese, frothy yellowish green), pH (at or above 4.5 for BV and trichomonas, below 4.5 for
candida), pruritus (absent in BV; intense with excoriation in candida; intense with splash
dysuria in trichomonas) and the PMN-to-epithelial-cell ratio. Diagnosis follows with saline
microscopy as the investigation of choice, clue cells, the Nugent score of 7–10, candida
pseudohyphae and tennis-racket spores, Sabouraud culture as the gold standard, motile
pear-shaped trichomonads, strawberry cervix and angry-looking vagina, the KOH whiff test as
the named test and the four Amsel criteria with three of four being diagnostic. Treatment
covers metronidazole 500 mg twice daily for 7 days or 2 g stat for BV with clindamycin as an
alternative, fluconazole 150 mg stat for candida, metronidazole for trichomonas, then the
pregnancy modifications (vaginal metronidazole in the first trimester and oral later; oral
fluconazole contraindicated with topical clotrimazole the drug of choice) and partner
treatment rules. Cervicitis begins with the ectocervix/endocervix epithelium split and its
infection lists, the chlamydial and gonococcal block (ascending spread along sperms,
endocervix more than urethra, 50–80% asymptomatic, mucopurulent discharge as the commonest
presentation, dyspareunia and post-coital bleeding), the per-speculum and per-vaginal
findings with PID as the differential, the laboratory panel (Gram-negative intracellular and
extracellular diplococci, more than 10 neutrophils per field, no organism for chlamydia, NAAT
as the investigation of choice, endocervical swab with urine if urethritis, Thayer-Martin and
McCoy cell culture gold standards), treatment (doxycycline 100 mg once daily for 7 days as
printed, ceftriaxone 250 mg intramuscular single dose, azithromycin 1 g in pregnancy with
doxycycline contraindicated) and the two complications. The chapter closes with NACO syndromic
management, the four inputs behind the colour-coded kits, and the three kits in detail —
green kit 2 with secnidazole and fluconazole for vaginitis, grey kit 1 with azithromycin and
cefixime for cervicitis, yellow kit 6 with cefixime, metronidazole and doxycycline for PID
after ruling out ectopic pregnancy — plus supportive advice, partner treatment rules and the
other uses of kit 1.

### Chapter 34 — Pelvic Inflammatory Disease (PID) (Book p184–187; 128 questions / 9 units)

Starts from the definition (infection of the upper female genital tract including endometritis,
salpingitis and oophoritis), the ascending spread along sperms, the 15–35 year sexually active
peak, the polymicrobial nature, the risk factor list (multiple risk factors, post abortion,
post partum, instrumentation, previous PID, copper T within 3 weeks) against the protective
factors (barrier contraceptives and MIRENA), and the abdominal spread to peritonitis and
perihepatitis. Pathogenesis runs through the four numbered steps — endometritis with menstrual
abnormalities, dysmenorrhoea, lower abdominal pain and endometrial biopsy; thick congested
hyperaemic swollen tubes with endosalpingitis, pyosalpinx and hydrosalpinx; oophoritis;
peritonitis with pelvic abscess — alongside the organism-by-population list (chlamydia
exceeding gonorrhoea in reproductive age, genital TB in virgins by the haematogenous route,
E. coli in menopausal women, Actinomyces in copper IUD users). Features and complications
follow: bilateral lower abdominal pain as the commonest symptom, pain during coitus, fever
driving menorrhagia in the acute phase, intermenstrual and post-coital bleeding under AUB,
dysmenorrhoea, infertility, vaginal discharge, and Fitz-Hugh-Curtis perihepatitis with violin
string adhesions between the liver capsule and the anterior abdominal wall and right upper
quadrant pain, chlamydia exceeding gonorrhoea. Diagnosis is built on the `PID is a clinical
diagnosis` line, the three confirmatory investigations (USG showing tubo-ovarian mass and
swollen tubes with the waist, bead-on-string and cogwheel signs; endometrial biopsy showing
endometritis; laparoscopy as the gold standard for direct visualisation, specimen collection
and conception scoring), the CDC minimum and additional criteria, the surest laparoscopic
sign of pus trickling from the fimbrial end, the Boer-Meisel conception score that excludes
organism type, Gainesville staging, culpotomy drainage and the beads-on-string note that
assigns USG to PID and HSG to genital TB. Management covers the OPD regimen (ceftriaxone
250 mg intramuscular single dose with doxycycline 100 mg and metronidazole 400 mg twice daily
for 14 days), the four admission indications, the 24-hour afebrile rule before switching to
14 days of oral therapy, the six numbered consequences led by infertility, and the advice on
abstinence, partner treatment, barrier contraception and alcohol avoidance — before the
syndromic approach with yellow kit 6 for the patient, grey kit 1 for the partner, the three
per-vaginal triggers and the mandatory negative urine pregnancy test.

### Chapter 35 — Genital Tuberculosis (Book p188–192; 134 questions / 9 units)

Opens with the pathogenesis flow — Mycobacterium tuberculosis from a lung greater than lymph
node primary source reaching the genital tract haematogenously (with sexual transmission
printed as the other route), entering the fallopian tube and destroying the lining from within
through endosalpingitis, caseous necrosis, fibrosis and adhesion to bilateral cornual block,
with uterine spread to the endometrium and fimbrial spread causing adhesions and hydrosalpinx.
The sites block covers bilaterality, ampulla exceeding isthmus, infertility as the commonest
presentation, HSG as the investigation of choice for tubal patency with its contraindication
before treatment because of dissemination risk, and the seven characteristic HSG appearances
(beaded, lead pipe, tobacco pouch, golfstick, bilateral cornual block, cotton wool and
hydrosalpinx, the first three of which are figured). Genital TB of the uterus follows —
superficial endometrium affected with the myometrium spared, which is why first-day menstrual
blood can be used and why the best biopsy timing is the premenstrual phase — with the normal
initial endometrium, acute endometritis causing menorrhagia and chronic adhesions causing
Asherman syndrome with secondary amenorrhoea or oligomenorrhoea; then ovarian disease limited
to the surface by the tunica albuginea with tubercles seen at laparoscopy, and tubercular
peritonitis with ascites. Clinical features cover the 20–30 year peak, occurrence in young
girls, the status of genital TB as the commonest cause of PID in virgins, the low-grade fever,
malaise and weight-loss prodrome, infertility from tubal blockage, the menstrual sequence from
initial menorrhagia to secondary amenorrhoea or hypomenorrhoea from Asherman syndrome,
variable chronic pelvic pain, the rare serosanguinous discharge and the future risk of ectopic
pregnancy. Examination covers the doughy abdomen with ascites, cervical, vaginal and vulval
ulcers, the adnexal mass and the frozen pelvis of restricted mobility. Diagnosis lists the
history clues (past and family tuberculosis, chronic PID unresponsive to broad-spectrum
antibiotics, PID in young or pubertal females), the cornual premenstrual endometrial biopsy
sent for saline culture, NAAT, confirmative PCR and histology in formation, the virgin
exception that substitutes first-day menstrual blood, and the ultrasound triad of tubal
dilatation, pyosalpinx and pelvic mass. Laparoscopy contributes the three sites — red
hyperaemic swollen dilated tubes, ovaries with or without tubercles, peritoneum — with
sampling to confirm, and the three-row management table closes the chapter: ATT Category I
for 6 months which can improve fertility; hysteroscopic adhesiolysis with a paediatric Foley
catheter and three months of estrogen plus progesterone for Asherman syndrome; and IVF for
infertility with distorted pelvic anatomy or tubal block.

## Method and quality gates

- Every source page was rasterised and OCR'd end to end, then re-cropped at 3×–16× zoom for
  every numeral, arrow label, table cell and figure caption that looked uncertain.
- Questions are ordered to follow the printed page line by line, section by section.
- Formats are deliberately mixed: fill-ups, match-the-following, true/false, clinical
  scenarios, odd-one-out and numeric items sit alongside recall items
  (**Ch 30–35: 339 fill-up, 266 recall, 51 true/false, 49 odd-one-out, 48 match,
  48 scenario, 24 numeric — ~49% non-recall**).
- Distractors are drawn from neighbouring printed lines, reversed arrows and adjacent
  thresholds rather than generic wrong words; all match items are true bijections.
- Answer positions are assigned by a seeded balanced shuffle: every new chapter finishes at
  24.6–25.8% per slot with no run of four identical slots.
- The current validator parses the actual embedded JavaScript, checks all question IDs,
  stems, option uniqueness and answers, and applies strict new-chapter synchronisation,
  order, format and answer-balance gates. Legacy answer distributions are retained.
- Printed source quirks are preserved verbatim rather than silently corrected — for example
  the p163 `CAH: X-linked recessive disorder` note, the p182 `Doxycycline 100 mg OD × 7 days`
  (once daily, as printed) for cervicitis, and the p187 six-item consequence list that repeats
  Fitz-Hugh-Curtis syndrome after the p185 acute complication entry.

## Next chapters to build

**Chapter 41 — Contraception: Images**, starting at scan 222 / printed 214.
Chapters 41–49 remain unbuilt. Chapters 36–40 stop before that chapter.

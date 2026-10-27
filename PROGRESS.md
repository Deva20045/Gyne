# PULSE · OBG Mastery Path — Progress

Standalone offline quiz built line-by-line from the *Marrow OBG Edition 8* printed notes
(Gynaecology Vol 1, Book p1 → onward).

- Repository: `Deva20045/Gyne`
- Published app: `obg-mastery-path.html` (single offline HTML, no build step to run)
- Editable source of truth for built chapters: `data_src/chNN.py` → `data/chNN.json`
- Rebuild any chapter: `python3 build_chapters.py 36 37 38 39 40`
- Validate: `python3 validate.py`

## Build status — 45 of 49 chapters live · 4,343 questions · 529 units

| Chapters | Scan sequence | Questions | Units |
|---|---:|---:|---:|
| 1–29 | 1–159 | 2,120 | 326 |
| 30 Disorders of Sexual Development (46XX) | 160–164 | 151 | 12 |
| 31 Disorders of Sexual Development (46XY) | 165–170 | 148 | 10 |
| 32 Primary Amenorrhoea | 171–177 | 195 | 17 |
| 33 Vaginitis and Cervicitis | 178–183 | 149 | 11 |
| 34 Pelvic Inflammatory Disease (PID) | 184–187 | 128 | 9 |
| 35 Genital Tuberculosis | 188–192 | 134 | 9 |
| **Cumulative 1–35** | **1–192** | **3,025** | **394** |
| 36 Female Infertility: Part 1 | 193–198 | 90 | 6 |
| 37 Female Infertility: Part 2 | 199–202 | 58 | 4 |
| 38 Male Infertility | 203–210 | 144 | 8 |
| 39 Contraception: Part 1 | 211–216 | 115 | 6 |
| 40 Contraception: Part 2 | 217–221 | 104 | 6 |
| **Cumulative 1–40** | **1–221** | **3,536** | **424** |
| 45 CIN: Part 2 | 246–250 | 124 | 17 |
| 46 Cancer Cervix | 251–256 | 177 | 22 |
| 47 Ovarian Cancer: Part 1 | 257–264 | 246 | 34 |
| 48 Ovarian Cancer: Part 2 | 265–268 | 140 | 17 |
| 49 Gynaecology: Miscellaneous Topics | 269–272 | 120 | 14 |
| **Cumulative built 1–40 + 45–49 (41–44 pending)** | **scans 1–272** | **4,343** | **529** |

Rows 36–49 quote the repository scan-sequence convention (part-05/06/07 scans run
8 ahead of the printed folio: scan 246 = printed 238).

## Current release — Chapters 36–40 (scans 193–221 · printed folios 185–213)

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

## This release — Chapters 45 to 49 (printed folios 238–264 · scans 246–272)

All 27 scanned sheets covering scans 246–272 (printed folios 238–264, PDF parts 06–07) were extracted at native
resolution, OCR'd end to end and then read page by page as images — every table cell,
bracket, arrow label, figure caption and handwritten numeral — before any question was
written. Chapters appear in strict printed order; chapters 36–44 remain unbuilt and were
deliberately untouched.

### Chapter 45 — CIN: Part 2 (printed p238–242; 124 questions / 17 units)

Opens with the dysplasia table — LSIL to CIN 1 at 1% risk against HSIL branching to CIN 2
at 5% and CIN 3 at 12–40% — and the `CIN is diagnosed on biopsy, not on pap smear` line,
then the two WHO pathways (limited resource: screening to HPV DNA ± VIA to management with
biopsy not mandatory; resource rich: abnormal pap to biopsy to CIN 1/2/3 to management).
The pap smear block is worked bullet by bullet: the seven inferences from normal through
infection-on-antibiotics, LSIL, HSIL, ASCUS, ASC-H and AGCUS; the five detectable
infections (bacterial vaginosis, candida, trichomonas, HSV, HPV) against the two
undetectable (chlamydia, gonorrhoea). Page 239 contributes the colposcopy photograph, the
abnormal-pap algorithm (growth to punch biopsy, no visible abnormality to colposcopic
guided biopsy), the report-wise management (HSIL with ASC-H at any age; LSIL ≥ 25 yrs to
colposcopy plus endocervical curettage; ASCUS split at 25 yrs between repeat pap in 12
months and HPV/reflex DNA testing; LSIL < 25 yrs repeat pap; AGCUS to adeno carcinoma of
endocervix and endometrial spread with colposcopic biopsy, endocervical curettage and
endometrial biopsy) and the colposcopy facts (×30 magnification, focal length 30,
visualises exocervix–transformation zone–external os but not endocervix, UPT beforehand,
OPD procedure, sampling from rough or pale areas, 3–5% acetic acid to acetowhite areas,
green filter to abnormal vessels with reticular, mosaic and punctate patterns). Page 240
gives the colposcopy inferences (CIN 1/2/3, microinvasive cancers, unsatisfactory from
incomplete transition-zone view), the management tree (CIN 1 follow up × 2 yrs resolving or
cryoablation; CIN 2/3 LLETZ or LEEP as mx of choice for all age and parity; hysterectomy
not done for CIN) and cryoablation in full — CO2/N2O at very low temperature applied to
acetowhite areas, the freezing-of-intracellular-water principle, freeze 3 / thaw 5 / freeze
3 mins, 3–5 mm destruction depth, persistent water discharge, no tissue specimen and the
four CIN 1 prerequisites (entire TZ visible, lesion completely visible, not HIV +ve, lesion
not > 2 quadrants). Page 241 covers LLETZ/LEEP (total dysplastic area removed, current in
the instrument cutting and coagulating together, OPD and 10–15 min procedure, 10 mm depth,
TOC for CIN 2 & 3 with tissue for HPE, minimal bleeding, the A–F figure), the two special
scenarios (positive endocervical curettage to cone biopsy to adenocarcinoma in situ to
hysterectomy; HSIL pap against CIN 1 or normal biopsy as a discrepancy to cone biopsy) and
cone biopsy/conisation (cone of exo/ecto cervix, transformational zone and endocervix, OT
under GA, labelled figure). Page 242 closes with the diagnostic and therapeutic cone
indications and the p-16 protein tree resolving an indeterminate LSIL-versus-HSIL pap into
HSIL when raised and LSIL when normal.

### Chapter 46 — Cancer Cervix (printed p243–248; 177 questions / 22 units)

Begins with the type tree — squamous cell as m/c with large cell non-keratinising the m/c
subtype, large cell keratinising and small cell (poor prognosis), HPV 16 association,
against adenocarcinoma as 2nd m/c in young females with OCP risk, HPV 18 and endocervix —
then features (transitional zone, bimodal 35–39 and 60–64 yrs) and the symptom list in
printed order (irregular bleeding m/c, post coital most specific, dirty discharge,
pyometra with Ca cervix the m/c cause, the printed `post menopausal spread` quirk kept
verbatim, respiratory cluster for lung metastasis, sciatica-haematuria-lymphedema for
pelvic side wall, renal failure as m/c death). Spread and drainage follow (direct >
lymphatic > hematogenous with lungs the hematogenous site; hypogastric, obturator,
paracervical sentinel and external iliac nodes; no superficial drainage hence excluded from
radiotherapy; EBRT for pelvic and extended EBRT for paraaortic nodes), the six involved
sites, the post-coital bleeding algorithm (normal cervix to pap then colposcopy,
barrel-shaped/friable/indurated cervix to colposcopy, visible growth to punch biopsy) and
the examination block (cachexia and low socio-economic status; pyometra lump on P/A;
ulcerative/fungating growth, friable bleeding cervix and hard nodular cervix on P/S;
parametrial and uterosacral thickening and nodularity per rectally). Investigations give
staging over lymph nodes as prognostic, cervical biopsy as diagnostic, cone biopsy after
microinvasion on LEEP, <1% ovarian involvement justifying ovarian preservation, then the
radiological workup pairings (USG pyometra, CT nodes, MRI parametrium, PET CT nodes, IVP
ureter and kidney, cystoscopy bladder, sigmoidoscopy rectum, chest X-ray lung; MRI best for
parametrium and PET-CT over CT for nodes). The FIGO table is worked row by row across both
pages — IA ≤5 mm with IA1 ≤3 mm and IA2 4–5 mm; IB >5 mm with IB1 ≤2 cm, IB2 ≤4 cm, IB3
>4 cm; II upper 2/3 vagina with IIA parametrium free and IIA1/IIA2 at 4 cm; IIB
parametrium; III lower 1/3 vagina with IIIA side wall free and IIIB side wall with
hydroureter/hydronephrosis; IIIC nodes with IIIC1 pelvic and IIIC2 paraaortic; IV
metastasis with IVA bladder/bowel and IVB distant or superficial inguinal nodes — plus the
three notes (uterine spread does not change staging, bullous oedema is not metastasis,
bladder metastasis needs histopathology positive). Management splits surgery (uptil IIA,
<4 cm, early stage except IB3) from chemoradiation (all stages, preferred when surgery is
contraindicated, cisplatin and 5FU radiosensitizers), the stage-wise surgery table (IA1
type 1 without nodes or conization; IA2 type 2/Wertheim with pelvic nodes or radical
trachelectomy plus pelvic nodes; IB1–IB2–IIA1 type 3 with pelvic nodes or type 3
hysterectomy plus pelvic lymphadenectomy), radical trachelectomy (cervix removed, uterus
stitched to vagina, abdominal cerclage for the injured internal os, young females wanting
children, <2 cm, LSCS afterwards), chemoradiation (IB3 and IIA2 to IV, cisplatin over 5FU
given before RT, vaginal fibrosis and ovarian failure bracketed as why RT is avoided
early), the brachytherapy-versus-teletherapy table (inside versus outside body,
intracavitary colpostat/tandem versus EBRT, iridium 192 versus cesium, following versus
first to shrink, point A 2 cm above and lateral to the external os for parametrial nodes
and point B 3 cm beyond for obturator nodes, 50 Gy at 2 Gy per sitting five times weekly)
and the post-surgery risk tree (high risk margin/parametrium/LN positive to chemo
radiation; intermediate large size, LVSI and deep stromal invasion with any two positive to
radiotherapy; low risk to no post-op mx).

### Chapter 47 — Ovarian Cancer: Part 1 (printed p249–256; 246 questions / 34 units)

Opens with functional ovarian cysts (m/c, hormonal, temporary and self-resolving;
follicular m/c at follicle ≥3 cm; corpus luteal m/c to rupture; theca lutein from raised
HCG in molar and twin pregnancy and clomiphene or HMG therapy), the cancer presentation
(rare so no screening, vague nausea and appetite loss, adnexal masses with TVS as IOC) and
the benign-versus-malignant adnexal table cell by cell (reproductive age versus extremes of
age; pain positive from inflammation versus negative; short rapid history with weight loss;
unilateral versus bilateral; cystic versus solid; tender versus non-tender; ultrasound
U/L anechoic unilocular without solid component versus B/L >10 cm with solid components,
thick septa with papillary excrescences, high vascularity, ascites, nodes and matted bowel
loops). Page 250 adds the malignancy image strip (thick >3 mm septations, mural nodularity,
papillary projections, frank solid components, papillary excrescences and solid
component/septae labels), the cyst management tree (3–5 cm wait and watch, 5–7 cm serial
USG, >7 cm surgery for torsion or rupture risk; post-menopausal CA 125 ≥35 IU then surgery
after investigations; pre-pubertal raised AFP, HCG or LDH then surgery) and the notes
(malignant transformation 30% post-menopausal versus 7% pre-menopausal; CA-125 of limited
value in reproductive age because fibroid, PID and genital TB raise it, 200 IU
significant). Pregnancy pathology follows — dermoid cyst as m/c benign tumour and m/c to
torsion with torsion timed to end of first trimester or puerperium, dysgerminoma as m/c
cancer, first trimester wait and watch with regressing corpus luteum and removal
contraindicated because progesterone fall aborts, second trimester surgery for malignant
USG features >10 cm, symptomatic rupture or torsion removed at any gestation — then the
risk and protective tables (estrogen: early menarche, late menopause, obesity,
endometriosis proven with PCOS and HRT controversial; incessant ovulation theory with
nulliparity proven and infertility with ovulation drugs controversial; Lynch, BRCA1 and
BRCA2; asbestos proven with talc and smoking for mucinous adenocarcinoma controversial;
protection by physical exercise, anovulation, multiparity, OCP, breast feeding and by
hysterectomy, tubal ligation, salpingectomy), the genetic block (MLH1/MSH2, colorectal
over endometrial at 60–70% and 20% ovarian risk for Lynch; BRCA1 40% with TAH + BSO at
35–40 yrs and endometrial risk positive; BRCA2 15%), hereditary versus sporadic (younger
50 yrs and 5–10% versus 60–70 yrs) and the screening tree (annual TVS + CA 125 from 35–40
yrs for hereditary or BRCA positive relatives, reassurance for sporadic). The WHO tree
(epithelial 90%, germ cell 5–8%, sex cord stromal 3–5%, metastatic) with serous
cystadenoma overall, dermoid in reproductive age and serous cystadenocarcinoma as m/c
cancer leads into epithelial tumours (five types, age 60, bilateral, worst prognosis from
non-specific symptoms, psammoma body, KRAS/PTEN low grade versus p53 high grade) and the
serous-versus-mucinous table in full (60% versus 80% benign; bilateral versus unilateral;
BRCA/p53 versus KRAS; smoking not a risk versus risk; CA 125 versus CEA and CA 19-9;
psammoma bodies versus none; uniloculated clear fluid versus honeycomb mucinous
multiloculated; fallopian tube versus endocervix lining; pseudomyxoma peritonei for
mucinous). Pseudomyxoma peritonei (mucinous peritoneum, appendix cancer m/c, metastatic
mucinous ovarian tumour, mucocele of appendix, bad prognosis from recurrence), Brenner's
tumour (We BUST: Walthard cell nest with coffee bean nuclei, benign, unilateral 100%,
solid, transitional lining) and the endometrioid-versus-clear-cell table (endometrial
glands versus hobnail cells; endometriosis shared; endometrial cancer versus in-utero DES)
close the epithelial section with the three notes (coffee bean nuclei in Brenner's and
granulosa; clear cell over endometrioid for endometriosis and endometrioid over granulosa
for endometrial cancer; solid tumours Brenner's and fibroma). Germ cell tumours run from
the teratoma arms (mature cystic dermoid benign, immature malignant, struma ovarii
monoclonal) and the five further varieties through young girls 10–30 yrs, unilaterality
and early-diagnosis prognosis, the seen/never-seen marker table (dysgerminoma LDH, hCG,
PLAP never AFP; yolk sac AFP, LDH, α1 antitrypsin never hCG; embryonal AFP and hCG never
LDH; choriocarcinoma hCG never AFP and LDH; teratoma no marker), occurrence (dermoid over
dysgerminoma as m/c GCT, immature teratoma as m/c germ cell cancer, gonadoblastoma and
dysgerminoma in dysgenetic gonads), prognosis (dysgerminoma best, yolk sac worst with acute
abdomen), dermoid cyst (m/c tumour in reproductive age, pregnancy and torsion; 10%
bilateral; all three layers with ectodermal m/c; mostly benign; 0.2–2% malignancy risk as
squamous cell carcinoma at the Rokitansky protuberance; tooth-and-hair gross figure; tip of
iceberg and dot-and-dash USG from white sebaceous material and hair; cystectomy with torsion
risk versus oophorectomy when family complete), dysgerminoma (2nd m/c GCT, 15–20% bilateral
and highest bilaterality risk, best prognosis, m/c cancer in dysgenetic gonads and
pregnancy, only radiosensitive ovarian tumour, fleshy solid lobulated tan gross, nests with
lymphocytic fibrous septa) and yolk sac tumour (most malignant GCT, worst prognosis, 100%
unilateral, acute abdomen, Schiller Duval or glomeruloid body with central capillaries
surrounded by tumour cells in cystic spaces).

### Chapter 48 — Ovarian Cancer: Part 2 (printed p257–260; 140 questions / 17 units)

Opens with the sex cord stromal tree — sex cord tumours splitting into estrogen-producing
feminizing granulosa cell tumour and androgen-producing virilizing Sertoli-Leydig, Leydig
and hilus cell tumours (Reinke's crystals on HPE), stromal tumours being fibroma, thecoma
and fibrothecoma — then the features (perimenopausal, unilateral, hormone-driven specific
symptoms giving early diagnosis) and the prognosis hierarchy sex cord stromal over GCT over
epithelial. Granulosa cell tumour is traced from granulosa-cell origin and the FOX L-2 gene
through estrogen and inhibin as tumour markers with antimullerian hormone at puberty, the
bleeding presentations (atypical uterine bleeding perimenopausal, post-menopausal bleeding,
precocious puberty), the mandatory endometrial sampling and the note box pairing
endometroid and granulosa tumours with endometrial cancer, then Call Exner bodies with
central acidophilic material, follicle-like cells and coffee bean nuclei. Fibroma follows
(U/L benign solid, well differentiated fibroblasts, Meig's syndrome) with the Meig's versus
pseudo-Meig's table (fibroma/thecoma/Brenner's/granulosa plus ascites and effusion resolving
on removal versus any other tumour such as mucinous cystadenoma or any other condition such
as fibroid). Metastatic tumours list stomach (m/c), GIT and breast carcinoma reaching the
ovary by retrograde lymphatics or transcoelomic spread, and Krukenberg tumour is worked
from pyloric-end stomach cancer through 80% bilaterality, symmetric enlargement, retained
shape and capsule, mobile waxy consistency and signet ring cells with mucin pushing the
nucleus aside. Management opens with the FIGO table row by row — stage 1 limited to ovary
with IA one ovary, IB both, intact capsule spanning them and IC ruptured capsule split into
IC1 intraoperative, IC2 preoperative and IC3 malignant ascites; stage 2 pelvic organs with
2A tube or uterus and 2B bladder or rectum; stage 3 abdominal spread with 3A1
retroperitoneal nodes, 3A2 microscopic above the brim, 3B macroscopic ≤2 cm and 3C ≥2 cm
with ± liver or spleen capsule extension; stage 4 distant with 4A malignant pleural
effusion and 4B liver or spleen parenchyma or inguinal nodes — plus the note that bladder
and rectum involvement is 2B in ovary but 4A in other gynaecological cancers, the seven
surgical staging steps (midline incision; ascitic fluid or saline wash cytology; inspection
and palpation; multiple peritoneal biopsies; type 1 TAH + BSO; infracolic omentectomy;
pelvic and para-aortic node dissection before closure), the surgery block (TAH + BSO as
surgery of choice; conservative U/L salpingo-oophorectomy without hysterectomy for GCT at
10–30 yrs, young sex cord cases and stage IA epithelial with incomplete family; debulking
for stages 3 and 4) and the chemotherapy table (epithelial six cycles IV + intraperitoneal
paclitaxel with carboplatin or cisplatin in all stages except IA and IB; GCT and sex cord
BEP — bleomycin, etoposide, cisplatin — except stage 1 dysgerminoma for GCT and only
stages 3 and 4 for sex cord), closing with the Sertoli-Leydig androgen note (hirsutism,
acne, baldness, enlarged clitoris as virilization).

### Chapter 49 — Gynaecology: Miscellaneous Topics (printed p261–264; 120 questions / 14 units)

Opens with stress urinary incontinence — the definition box (involuntary urine on raised
intra-abdominal pressure with coughing, laughing, sneezing), the normal-versus-SUI
pathophysiology columns (pelvic floor contraction and raised intraurethral pressure
maintaining continence against descent of the bladder neck, raised intra-abdominal
pressure, failure of urethral closure and leakage), the Q tip test and the management tree
of bladder neck or urethral suspension: Bursch colposuspension by the abdominal route
suspending proximal urethra and bladder neck to the iliopectineal/Cooper's ligament with
the white line of pelvic fascia, symphysis pubis and Cooper's ligament figure labels,
necessary hospital stay and gold-standard outcome, against tension-free TOT and TVT as day
care vaginal procedures suspending the middle urethra, TOT through the obturator foramen as
m/c (TOT > TVT) and TVT through the retropubic space with raised bladder and venous plexus
injury risk, with the retropubic space and obturator foramen figure labels. Urinary fistula
follows with the three complaint patterns (dribbling with normal micturition ureterovaginal,
dribbling without normal micturition vesicovaginal, urine per urethra and vagina during
micturition urethrovaginal), the numbered types diagram against ureter, uterus, bladder and
vagina, suprapubic catheterization for urine sampling, menouria as hematuria during
menstruation from bladder endometriosis or vesicouterine fistula, and the methylene blue
three swab test as IOC for vesicovaginal fistula with its swab positions and the
observation-inference table (upper wet unstained ureterovaginal, middle wet stained blue
vesicovaginal, only lower wet stained blue urethrovaginal) after dye instillation through a
Foley catheter. Vesicovaginal fistula closes the topic — TAH as m/c cause in developed and
obstructed labour in developing countries, immediate repair when identified at once against
six-week delay after 24 hours or post obstructed labour once infection and inflammation
subside, Chassar moir and Latzko techniques, and the post-op rules (Foley drainage with
antibiotics for 2 weeks, no P/S or P/V and no intercourse for 3 months, pregnancy
contraindicated for 1 year). The chapter and the book end with OHSS — the iatrogenic chain
from inj. HMG through excessive stimulation, multiple large follicles, estrogen ≥2500 pg
and VEGF from follicular fluid, failed monitoring, inj. hCG, follicle rupture and VEGF
release with the large-follicle scan and follicular-size plus estrogen monitoring; the
eight risk factors (young, PCOS, thin, raised follicle number on TVS, raised antral count,
AMH >3.3, estradiol ≥2500 pg, pregnancy); the clinical-diagnosis complaints; the drug risks
(hMG highest, clomiphene low, letrozole none) with inj. hCG as trigger and VEGF as
mediator; early OHSS within 9 days of exogenous hCG against late OHSS from placental hCG;
prevention by monitoring, withholding hCG at estrogen ≥2500 pg, cabergoline lowering VEGF
and no embryo transfer when risk is positive; and the ideal hCG cloud (estrogen 500–1500
pg, 2–3 follicles, >17 mm) with the closing note that each follicle releases 200 pg of E2.

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

**Chapter 41 — Contraception: Images**, starting at scan 222 / printed folio 214.
Chapters 41–44 remain unbuilt; chapters 45–49 are complete, so closing 41–44 finishes
the book. Check chapter boundaries from the actual page headings.
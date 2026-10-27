"""CIN: Part 1. Scan 236-245; printed 228-237.

Screening intervals, vaccine dose schedules and historical product notes are
edition-specific source material; explanations flag obsolete or ambiguous
claims rather than teaching them as current rules.
"""
from data_src.authoring import add
SECTIONS = []
add(SECTIONS, 236, 'Anatomy of the cervix and pubertal vaginal acidity', '''
fillup | The endocervix is lined by ____ epithelium. | columnar | stratified squamous | transitional | cuboidal | Endocervix: Lined by columnar epithelium; red on P/S exam.
fillup | The exocervix/ectocervix is lined by ____ epithelium. | stratified squamous | columnar | transitional | glandular | Exocervix/ectocervix: Lined by stratified squamous epithelium; pink on P/S exam.
fillup | On per-speculum examination the endocervix appears ____ and the exocervix ____. | red; pink | pink; red | white; grey | blue; red | Red on P/S exam for endocervix; pink for exocervix.
match | Match the cervical epithelium: 1) Endocervix 2) Exocervix with A) Pink, stratified squamous B) Red, columnar. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | The two epithelia differ in both histology and speculum colour.
fillup | At puberty, glycogen appears in the vaginal epithelium under the effect of ____. | estrogen | progesterone | testosterone | prolactin | Presence of glycogen in vaginal epithelium under the effect of estrogen.
fillup | Doderlein bacilli act on glycogen to produce ____. | lactic acid | acetic acid | hydrochloric acid | citric acid | Acts on glycogen -> Lactic acid -> Acidic pH of vagina.
fillup | The end result of the Doderlein pathway is a(n) ____ vaginal pH. | acidic | alkaline | neutral | fluctuating | Lactic acid -> Acidic pH of vagina.
fillup | The circular figure labels the squamocolumnar epithelium as the ____ zone. | transformation | proliferative | secretory | basal | Transformation zone and Squamo columnar epithelium are labelled on the diagram.
fillup | The opening at the centre of the diagram is the ____. | external os | internal os | cervical canal | fimbria | External os is labelled with the transformation zone figure.
tf | I) The endocervix is lined by columnar epithelium. II) Doderlein bacilli produce lactic acid from glycogen. | Both true | I true; II false | I false; II true | Both false | Both statements follow the anatomy and puberty bullets.
scenario | A student claims the acidic vaginal pH comes from acetic acid produced by Doderlein bacilli. Which correction fits the source? | It is lactic acid, not acetic acid | It is hydrochloric acid | It is citric acid | The vagina is normally alkaline | The glycogen -> lactic acid -> acidic pH chain is printed under 'At puberty'.
odd | Which is NOT one of the labels on the cervical anatomy diagram? | Nabothian follicle | Transformation zone | External os | Endocervix | Nabothian follicles are introduced on the next sheet, not on the anatomy figure.
fillup | The 'Anatomy & Histopathology of Cervix' section opens at the printed timestamp ____. | 00:00:40 | 00:22:42 | 00:33:43 | 00:44:24 | 00:00:40 is on the opening heading; later times belong to Pap smear, risk factors and prevention.
''')
add(SECTIONS, 237, 'Transformation zone, metaplasia, Nabothian cysts and applied anatomy', '''
fillup | Squamous metaplasia is when ____ epithelium grows over columnar epithelium. | squamous | transitional | cuboidal | ciliated | Squamous epithelium grows over Columnar epithelium.
fillup | The transformation zone is a dynamic area between the ____ and ____ squamocolumnar junctions. | old; new | upper; lower | internal; external | anterior; posterior | Dynamic area between old & new squamocolumnar junction.
fillup | The position of the transformation zone changes with hormonal status, OCPs, pregnancy and ____. | menopause | lactation | exercise | diet | Position changes d/t Hormonal status, OCPs, Pregnancy, menopause.
fillup | The original squamocolumnar junction is described as located near the ____. | external os | internal os | isthmus | fimbria | Original position: Located near external OS.
odd | Which is NOT listed as a factor shifting the transformation zone? | Nonoxynol-9 spermicide | Hormonal status | OCPs | Pregnancy | The four listed factors are hormonal status, OCPs, pregnancy and menopause.
fillup | Blockage of columnar epithelial glands gives rise to ____ cysts/follicles. | Nabothian | ovarian | Bartholin | Gartner | Blockage of columnar epithelial glands -> Nabothian cysts/Follicles.
fillup | Nabothian cysts are described as ____ and needing no biopsy. | physiological | premalignant | malignant | infectious | Physiological; Biopsy not required; they indicate the original SC junction.
fillup | Nabothian cysts indicate the ____ squamocolumnar junction. | original | new | future | absent | Indicates the original SC junction.
fillup | For cancer cervix, the most common histologic variety is ____ carcinoma. | squamous cell | adenocarcinoma | small cell | sarcoma | Squamous cell carcinoma: most common variety.
fillup | The transformation zone is the ____ site for cervical cancer. | most common | least common | only | rare | Transformation zone (TZ): m/c site.
fillup | The endocervix is named as the most common site for ____. | adenocarcinoma | squamous carcinoma | melanoma | lymphoma | Endocervix: m/c site for adenocarcinoma.
fillup | A Pap smear samples ____ sites: the transition zone near the external os and the endocervix. | two | three | four | one | 2 Samples: Transition zone near external OS; Endocervix.
match | Match the cervical cancer fact: 1) Squamous cell carcinoma 2) Most common site 3) Adenocarcinoma site with A) Transformation zone B) Endocervix C) Most common variety. | 1-C, 2-A, 3-B | 1-A, 2-B, 3-C | 1-C, 2-B, 3-A | 1-B, 2-A, 3-C | Histology, site and glandular origin are three separate applied-aspect lines.
scenario | A clinician sees a smooth cyst on the ectocervix and wants to biopsy it. Which source statement is relevant? | Nabothian cysts are physiological and do not require biopsy | Nabothian cysts are always malignant | All cervical cysts need cone biopsy | Cysts indicate invasive cancer | The source explicitly marks them physiological with no biopsy required.
tf | I) The transformation zone position can change in pregnancy. II) Nabothian cysts are premalignant. | I true; II false | I true; II true | I false; II true | Both false | Pregnancy is a listed shifting factor, but Nabothian cysts are physiological, not premalignant.
''')
add(SECTIONS, 237, 'Histopathology: metaplasia versus dysplasia', '''
fillup | Dysplasia is described as ____ metaplasia. | unorganised | organised | physiological | reversible | Dysplasia (Unorganized metaplasia).
fillup | Metaplasia is ____ while dysplasia is pathological. | physiological | pathological | malignant | infectious | Metaplasia: Physiological; Dysplasia: Pathological.
fillup | Metaplasia is ____ but dysplasia is premalignant. | not premalignant | premalignant | always malignant | infectious | Not premalignant (metaplasia) versus Premalignant (dysplasia).
fillup | Metaplasia is seen in ____ females. | all | only postmenopausal | only nulliparous | only pregnant | Seen in all females.
fillup | Dysplasia occurs in the presence of ____ for cancer cervix. | risk factors | protective factors | immunity | multiparity | Occurs in presence of risk factors by ca cervix.
fillup | Dysplastic cells show an increased ____ ratio. | nucleus:cytoplasmic | cytoplasm:nuclear | nuclear:membrane | gland:stroma | Increased Nucleus: Cytoplasmic ratio.
fillup | Dysplastic cells also show increased nuclear ____. | pyknosis | pallor | vacuolation | enlargement of the nucleolus | Increased Nuclear pyknosis is the second characteristic.
match | Match the feature: 1) Metaplasia 2) Dysplasia with A) Premalignant, risk-factor associated B) Physiological, seen in all females. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | The histopathology table contrasts the two processes on every row.
scenario | A biopsy is reported as unorganised metaplasia with an increased nuclear:cytoplasmic ratio. Which source category fits? | Dysplasia, a premalignant process | Normal metaplasia | Invasive carcinoma | Cervicitis | Unorganised metaplasia with nuclear changes is the dysplasia column.
odd | Which is NOT a characteristic of dysplastic cells in this table? | Decreased nuclear pyknosis | Increased nucleus:cytoplasmic ratio | Premalignant nature | Association with risk factors | The source lists increased, not decreased, nuclear pyknosis.
tf | I) Metaplasia is seen in all females. II) Dysplasia is not premalignant. | I true; II false | I true; II true | I false; II true | Both false | Metaplasia is universal and physiological; dysplasia is explicitly premalignant.
''')
add(SECTIONS, 238, 'CIN grading and the role of Pap smear', '''
fillup | CIN I involves the ____ of the cervical epithelial thickness. | lower one-third | middle third | full thickness | membrane | Cervical epithelial thickness <1/3rd -> CIN I.
fillup | CIN 2 involves ____ of the epithelial thickness. | one-third to two-thirds | less than one-third | more than two-thirds | full thickness | 1/3 - 2/3 -> CIN 2.
fillup | CIN 3 involves ____ of the epithelial thickness. | at least two-thirds | less than one-third | one-third to two-thirds | the basement membrane only | >=2/3 -> CIN 3.
match | Match the CIN grade to thickness: 1) CIN I 2) CIN 2 3) CIN 3 with A) 1/3-2/3 B) <1/3 C) >=2/3. | 1-B, 2-A, 3-C | 1-A, 2-B, 3-C | 1-B, 2-C, 3-A | 1-C, 2-A, 3-B | The grades ascend with the fraction of involved epithelium.
fillup | Full-thickness involvement without involvement of the overlying membrane is ____. | carcinoma in situ (CIS) | invasive carcinoma | CIN 2 | metaplasia | Complete thickness without involvement of overlying membrane -> Carcinoma in situ (CIS).
fillup | Involvement of the overlying membrane defines ____. | invasive carcinoma of the cervix | CIS | CIN 3 | dysplasia | Involvement of overlying membrane -> Invasive carcinoma of cervix.
fillup | CIN I, II or III is diagnosed by ____. | biopsy or tissue sample | Pap smear alone | TVS | colposcopy appearance alone | CIN I, 2, or 3: Dx by biopsy or tissue sample.
fillup | A Pap smear is a ____ test that identifies dysplasia. | cytological | histological | serological | radiological | Pap smear: Cytological test; Identifies dysplasia.
fillup | A Pap smear cannot assess the ____ of dysplasia. | extent | presence | cell type | nucleus | Extent cannot be assessed; inference is only dysplasia + or dysplasia -.
fillup | An abnormal Pap smear should be followed by ____. | biopsy | radiotherapy | hysterectomy | vaccination | Abnormal pap smear -> Biopsy.
fillup | Management ____ based on the Pap smear report alone. | is not | is always | is rarely | is | mx is not based on pap smear report.
tf | I) Pap smear can grade the depth of CIN. II) CIN is diagnosed on a biopsy or tissue sample. | I false; II true | I true; II false | Both true | Both false | Pap smear is cytological and cannot assess extent; tissue diagnosis is required for CIN.
scenario | A screening Pap smear reports dysplasia. Which source-consistent next step follows? | Proceed to biopsy for tissue diagnosis | Start radiotherapy | Diagnose CIN 3 from the smear | No follow-up needed | Management is not based on the smear; an abnormal result leads to biopsy.
odd | Which is NOT a Pap smear inference in the source? | Exact depth of invasion in millimetres | Dysplasia positive | Dysplasia negative | Need for biopsy | Pap smear gives a dysplasia +/- cytology result; extent requires tissue.
''')
add(SECTIONS, 238, 'Conventional Pap smear instruments and samples', '''
fillup | The two conventional Pap smear instruments named are ____. | Ayres spatula and endocervical brush | Karman cannula and Pipelle | LLETZ loop and cryoprobe | Babcock forceps and tenaculum | Instruments: Ayres spatula, Endocervical brush.
fillup | The bifid end of the Ayres spatula is used to sample the ____. | ectocervix/transition zone | endocervix | vagina | endometrium | From transition zone with bifid end of Ayer's spatula.
fillup | The other end of the Ayres spatula is used for ____ cytology and buccal smear. | vaginal | endocervical | endometrial | peritoneal | Uses of other end: vaginal cytology, Buccal smear.
fillup | The ectocervical sample is taken near the ____ and the spatula is rotated ____. | external os; 360 degrees | internal os; 180 degrees | squamocolumnar junction; 90 degrees | vaginal fornix; 720 degrees | Near external os; Rotated 360 degrees.
fillup | The endocervical sample is taken using the ____. | endocervical brush | bifid spatula | Karman cannula | cervical broom | Using endocervical brush is the endocervical sampling line.
fillup | The conventional Pap smear section carries the timestamp ____. | 00:22:42 | 00:00:40 | 00:33:43 | 00:44:24 | 00:22:42 is on the Pap Smear heading.
match | Match the instrument to its use: 1) Ayres spatula 2) Endocervical brush with A) Endocervical sample B) Ectocervical/transition-zone sample. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | The spatula scrapes the ectocervix; the brush samples the canal.
scenario | A trainee uses only an endocervical brush and skips the spatula. Which sample is missed per the source? | The ectocervical/transition-zone sample | The endocervical sample | The vaginal pool sample | The buccal smear | The two-sample technique needs both the spatula and the brush.
tf | I) The Ayres spatula's bifid end samples the transformation zone. II) The endocervical brush samples the ectocervix. | I true; II false | I true; II true | I false; II true | Both false | The spatula takes the ectocervical/transition-zone sample; the brush takes the endocervical one.
''')
add(SECTIONS, 239, 'Pap smear procedure, liquid-based cytology and Bethesda counts', '''
fillup | In the conventional procedure, both smear samples are placed on ____. | the same slide | separate slides | a culture plate | a liquid vial | Both smear samples on same slide.
fillup | The conventional Pap fixative is ____. | 95% ethyl alcohol +/- 5% ether | methanol | formalin | normal saline | Fixative: 95% ethyl alcohol +/- 5% ether; methanol is the liquid-based cytology fixative.
fillup | The procedure warns: do not ____ the slide. | air dry | fix | label | stain | Do not air dry the slide.
fillup | Active bleeding is listed as a ____ to taking a Pap smear. | relative contraindication | absolute indication | screening target | diagnostic result | Relative contraindication: Active bleeding.
fillup | A per-vaginal examination ____ done prior to a Pap smear. | is not | is always | is optionally | must be | P/V exam is not done prior pap smear.
fillup | The best time for a Pap smear is the ____ phase. | periovulatory | menstrual | luteal | postpartum | Best time for pap smear: Periovulatory phase.
fillup | A separate ____ swab is taken for HPV DNA testing. | cervico-vaginal | buccal | nasal | rectal | Separate cervico-vaginal swab is taken for HPV DNA testing.
fillup | Liquid-based cytology uses a ____ instrument. | cervical brush/broom | Ayres spatula | Karman cannula | Vabra aspirator | Instruments: Cervical brush/broom.
fillup | The fixative for liquid-based cytology is ____. | methanol | 95% ethyl alcohol | ether | formalin | Fixation: methanol; conventional Pap uses 95% ethyl alcohol +/- ether.
fillup | Liquid-based cytology can be performed ____. | during menstruation | only postpartum | only after menopause | only under GA | Can be tested during menstruation is one of its listed advantages.
fillup | The sensitivity of liquid-based cytology is described as ____ conventional Pap smear. | the same as | higher than | lower than | double | Sensitivity: Same for conventional pap smear & liquid based cytology.
fillup | In the Bethesda adequacy table, conventional Pap requires ____ squamous cells. | 8K-10K | 4K-5K | 10-12 | 1K-2K | Squamous cells: 8K-10K for conventional Pap, 4K-5K for liquid-based cytology.
fillup | Liquid-based cytology requires ____ columnar cells in the Bethesda table. | 10-12 | 8K-10K | 4K-5K | 1-2 | Columnar cells: 10-12 in both columns.
match | Match the Bethesda adequacy number: 1) Conventional Pap squamous cells 2) LBC squamous cells 3) Columnar cells with A) 4K-5K B) 8K-10K C) 10-12. | 1-B, 2-A, 3-C | 1-A, 2-B, 3-C | 1-B, 2-C, 3-A | 1-C, 2-A, 3-B | The adequacy table gives two squamous counts and a small columnar-cell count.
scenario | Source-check: a student claims liquid-based cytology is much more sensitive than conventional Pap. Which source line matters? | Sensitivity is stated as the same for both methods | LBC is always 90% more sensitive | Conventional Pap is obsolete | Only LBC can detect HPV | The printed sensitivity note calls them equal; the advantages are fewer unsatisfactory smears and shared HPV testing.
odd | Which is NOT a listed advantage of liquid-based cytology? | Higher sensitivity than conventional Pap | Same sample usable for HPV testing | Can be tested during menstruation | Fewer unsatisfactory smears | Sensitivity is equal, not higher; the other three are the printed advantages.
tf | I) Conventional Pap uses 95% ethyl alcohol as fixative. II) Liquid-based cytology uses methanol. | Both true | I true; II false | I false; II true | Both false | The two fixatives are printed on the same sheet and must not be interchanged.
''')
add(SECTIONS, 239, 'Risk factors for cancer cervix', '''
fillup | The leading risk factor listed for cancer cervix is ____. | HPV | HSV | HIV | HBV | HPV heads the risk-factor list; HIV is a separate entry.
fillup | Early coitarche is defined in the source as before ____ years. | 18 | 20 | 21 | 16 | Early coitarche < 18 yrs.
fillup | Early childbirth is defined as before ____ years in the risk list. | 20 | 18 | 25 | 30 | Early childbirth <20 yrs.
fillup | OCPs are described as a ____ risk factor for adenocarcinoma of the cervix. | reversible | permanent | protective | hereditary | OCPs: Reversible risk factor -> Adenocarcinoma of cervix.
fillup | Smoking is linked in the source to ____ carcinoma of the cervix. | squamous cell | adenocarcinoma | small cell | neuroendocrine | Smoking -> Squamous cell carcinoma.
match | Match the risk factor to its associated cancer: 1) OCPs 2) Smoking with A) Squamous cell carcinoma B) Adenocarcinoma of cervix. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | The two arrows point to different histologies.
fillup | The source lists ____ as an immunocompromising risk factor. | HIV | HPV | HSV | EBV | HIV appears as a risk factor; HPV is the causal agent.
odd | Which is NOT a cancer-cervix risk factor in the source? | Late menopause | Multiple sex partners | Multiparity | Low socio-economic status | The 'notable features' line says cervix cancer has no relation to late menopause.
fillup | The source says cervical cancer ____ relation to early menarche and late menopause. | has no | has a strong | has a proven | has an exclusive | Cervix ca has no relation to early menarche & late menopause.
fillup | The source states there is ____ role of familial inheritance in cancer cervix. | no | a dominant | a proven | a minor | No role of familial inheritance in ca cervix.
fillup | HRT ____ the risk of cancer cervix according to the source. | does not increase | doubles | halves | abolishes | HRT does not increase risk of ca cervix.
scenario | A student assumes cervical cancer is strongly inherited because it clusters in families. Which source line corrects this? | There is no role of familial inheritance in cancer cervix | BRCA1/2 mutations cause most cervical cancers | Familial inheritance doubles the risk | HRT is the main inherited cause | The notable-features line explicitly denies a familial-inheritance role.
tf | I) Early coitarche (<18 yrs) is a risk factor. II) Late menopause is a risk factor. | I true; II false | I true; II true | I false; II true | Both false | Early coitarche is listed, but the source says there is no relation to late menopause.
''')
add(SECTIONS, 240, 'HPV biology, oncogenes and low-risk disease', '''
fillup | HPV is described as ____, completing its life cycle in epithelial cells. | epitheliotropic | hematotropic | neurotropic | osteotropic | Epitheliotropic: Completes its life cycle in the epithelial cells.
fillup | HPV initially affects the ____ cells. | basal and parabasal | superficial squamous | columnar | stromal | Affects basal & parabasal cells; completion of the life cycle occurs in superficial cells.
fillup | The cytopathic effect seen in superficial cells is ____, a perinuclear halo/vacuole. | koilocytosis | dyskeratosis | acanthosis | metaplasia | Koilocytosis with a perinuclear halo/vacuole.
fillup | In malignant transformation, the E6 oncoprotein knocks out the ____ gene. | p53 | retinoblastoma | BRCA1 | PTEN | E6 -> knocks out p53 gene -> immortal cell.
fillup | In malignant transformation, the E7 oncoprotein knocks out the ____ gene. | retinoblastoma | p53 | KRAS | MLH1 | E7 -> knocks out retinoblastoma gene.
match | Match the HPV oncoprotein: 1) E6 2) E7 with A) Retinoblastoma gene B) p53 gene. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | E6 targets p53; E7 targets the retinoblastoma protein.
fillup | Viral replication early proteins named are ____. | E1 and E2 | E6 and E7 | L1 and L2 | p53 and Rb | Viral replication: E1, E2; E6/E7 are the transforming oncoproteins.
scenario | Source-check: the sheet says 'E2 protein -> upregulate E6, E7'. What is the safest interpretation? | It is a simplified source line; E2 biology is more nuanced, so study it as printed, not as a precise mechanism | E2 is the main human tumour suppressor | E6/E7 have no role in cancer | HPV has no replication genes | The printed arrow is shorthand about early-gene regulation, not a complete molecular account.
fillup | HPV 16 and 18 together are said to cause ____ of cervical cancers. | 70% | 50% | 90% | 30% | HPV 16 & HPV 18 (70% cause of ca cervix).
fillup | The most common high-risk subtype is ____ (50%). | HPV 16 | HPV 18 | HPV 31 | HPV 6 | m/c: HPV 16 (50%).
fillup | The most specific high-risk subtype named is ____. | HPV 18 | HPV 16 | HPV 6 | HPV 11 | Most specific: HPV 18; the source's 'specific' label is retained as printed.
fillup | Besides 16 and 18, the high-risk subtypes listed are ____. | 31, 33, 35, 52 and 58 | 6, 11, 42, 43, 44 | 1, 2, 3, 4, 5 | 26, 53, 66, 73, 82 | Others: 31, 33, 35, 52, 58.
fillup | The low-risk HPV subtypes linked to genital warts are ____. | 6 and 11 | 16 and 18 | 31 and 33 | 52 and 58 | Low risk subtypes: HPV 6 & 11 -> Genital warts/Condyloma Acuminata.
fillup | The drug of choice for genital warts in a pregnant female is ____. | trichloroacetic acid (TCA) | podophyllin | imiquimod | 5-fluorouracil | DOC in Pregnant female: Trichloroacetic acid (TCA).
fillup | Low-risk HPV in newborns can cause ____. | laryngeal papilloma | cervical cancer | penile cancer | oropharyngeal cancer | Laryngeal papilloma in newborns is the second low-risk outcome.
match | Match the high-risk HPV cancer by sex: 1) Males 2) Females with A) Cervix, vulva, vagina B) Penis, anus, oropharynx. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | The cancer branch splits into male and female sites.
scenario | A pregnant woman has anogenital warts. Which source-consistent treatment is named, and what caution applies? | Trichloroacetic acid, with product-specific and obstetric guidance checked before use | Podophyllin, safe in all trimesters | Imiquimod, first line in pregnancy | 5-FU, applied liberally | TCA is the printed DOC; pregnancy requires individual clinical assessment before any caustic agent.
odd | Which is NOT a high-risk HPV subtype in the source list? | HPV 6 | HPV 31 | HPV 52 | HPV 58 | HPV 6 is a low-risk wart subtype.
tf | I) HPV 16 is the most common high-risk subtype. II) HPV 6 is a high-risk oncogenic subtype. | I true; II false | I true; II true | I false; II true | Both false | HPV 16 is m/c at 50%, while HPV 6 is a low-risk wart type.
''')
add(SECTIONS, 241, 'Prevention, WHO 2030 goals and screening methods', '''
fillup | The two prevention methods for HPV infection named are ____. | screening and vaccines | antibiotics and surgery | condoms alone | hysterectomy | Prevention methods: screening, vaccines.
fillup | About ____ of HPV infections resolve spontaneously. | 90% | 10% | 50% | 70% | HPV infection: 90% Resolved; 10% persists.
fillup | The ____ that persist can progress through dysplasia to CIN. | 10% | 90% | 50% | 30% | 10% persists -> Dysplasia -> CIN.
fillup | CIN is placed at ages ____, carcinoma in situ at 30-35 years and cancer at 35-39/60-65 years. | 21-30 years | 10-20 years | 40-45 years | 50-55 years | CIN (21-30 yrs) precedes CIS (30-35 yrs) and invasive cancer.
fillup | The WHO 2030 goal for vaccination is ____ coverage of girls by 15 years. | 90% | 70% | 50% | 100% | 90%: vaccination coverage for ca cervix by 15 yrs.
fillup | The WHO 2030 screening goal is ____ of women screened by 35 years, repeated at 45 years. | 70% | 90% | 50% | 30% | 70%: screened by 35 yrs -> Repeated at 45 yrs.
fillup | The third WHO 2030 goal is that ____ of women with CIN or cancer receive treatment. | 90% | 70% | 50% | 100% | 90%: with CIN or Ca cervix -> Receive Rx.
match | Match the WHO 2030 target: 1) Vaccination by 15 y 2) Screening by 35 y 3) Treatment of CIN/cancer with A) 90% B) 70% C) 90%. | 1-A, 2-B, 3-C | 1-B, 2-A, 3-C | 1-C, 2-A, 3-B | 1-A, 2-C, 3-B | The 90-70-90 targets map to vaccination, screening and treatment; two are 90%.
fillup | The most sensitive screening method named is ____. | HPV DNA testing (85-90%) | Pap smear | VIA | VILI | Most sensitive: HPV DNA testing (85-90%).
scenario | Source-check: the sheet calls Pap smear 'most specific' but writes '55% sensitivity' in brackets. What should a learner note? | The bracketed figure is a sensitivity value, not specificity; the source line conflates the two | Pap smear sensitivity is 100% | Pap smear is less sensitive than VIA | Specificity and sensitivity are identical quantities | The printed numbers mix the two test characteristics; read them as study shorthand, not a validated performance table.
fillup | Visual inspection with acetic acid is abbreviated ____. | VIA | VILI | LBC | LEEP | VIA - Visual inspection with acetic acid.
fillup | The method NOT recommended by WHO in the source is ____. | VILI | VIA | HPV DNA testing | Pap smear | Not recommended by WHO: VILI - Visual inspection with Lugol's iodine.
fillup | Resource-rich countries follow the ____ protocol; resource-limited countries the WHO protocol. | ACOG | FIGO | Bethesda | SAGE | Resource rich countries: ACOG protocol; resource limited: WHO protocol.
fillup | The WHO screening protocol starts at ____ years and continues until 50 years. | 30 | 21 | 25 | 35 | Started at 30 yrs -> Until 50 yrs.
fillup | The 'see and treat' approach treats after ____ positive screening test. | one | two | three | zero | See & treat: 1 degree screening test +ve -> Rx; HPV DNA testing > VIA.
fillup | The 'see, triage and treat' approach requires ____ positive screening tests before treatment. | two | one | three | four | See, triage & treat: 1 degree screening +ve -> 2 degree screening +ve -> Rx.
match | Match the approach: 1) See and treat 2) See, triage and treat with A) One positive primary test then treat B) Two sequential positive tests then treat. | 1-A, 2-B | 1-B, 2-A | Both A | Both B | The two arrows differ by the number of positive tests required.
tf | I) HPV DNA testing is called the most sensitive screening method. II) VILI is described as recommended by WHO. | I true; II false | I true; II true | I false; II true | Both false | HPV DNA testing is most sensitive; VILI is explicitly not recommended by WHO.
''')
add(SECTIONS, 242, 'Screening algorithms, LLETZ and cryosurgery prerequisites', '''
fillup | The see-and-treat approach with HPV DNA starts screening at 30 years and continues until ____. | 49 years | 65 years | 45 years | 50 years | Start screening at 30 yrs -> until 49 yrs.
fillup | A negative primary HPV DNA test is repeated after ____ in the general population. | 5-10 years | 1-2 years | 3-5 years | 15 years | General population after 5-10 yrs; HIV +ve population after 3-5 yrs.
fillup | In HIV-positive women a negative HPV DNA test is repeated after ____. | 3-5 years | 5-10 years | 1-2 years | 10 years | HIV +ve population after 3-5 yrs.
fillup | A positive HPV DNA test in see-and-treat is managed with ____ preferentially. | LLETZ/LEEP over cryoablation | cryoablation over LLETZ | tranexamic acid | no treatment | LLETZ/LEEP > Cryoablation.
fillup | The see-and-treat VIA approach applies ____ acetic acid to the cervical epithelium. | 3-5% | 95% | 10% | 1% | 3-5% acetic acid applied on cervical epithelium.
fillup | In the VIA see-and-treat pathway, normal epithelium is repeated every ____. | 3 years | 5-10 years | 1 year | 6 months | Normal epithelium -> Repeat every 3 yrs.
fillup | In the see-triage-treat approach, a negative VIA triage leads to repeat HPV DNA testing in ____. | 1-2 years | 5-10 years | 3 years | 6 months | VIA -ve -> Repeat HPV DNA test in 1-2 yrs.
fillup | In the triage pathway, screening starts at 30 years and stops at ____. | 50 years | 49 years | 65 years | 45 years | Start screening: 30 yrs; Stop screening: 50 yrs.
fillup | LLETZ stands for ____. | large loop excision of the transformation zone | low-level endometrial thermal zone | loop electrocoagulation of the cervix | local excision of the vaginal wall | LLETZ: Large loop excision of transformation zone / LEEP: loop electroexcision procedure.
fillup | Cryosurgery requires ____ of the four listed criteria to be present. | all | any two | only one | none | Indication: All 4 of the following to be present.
fillup | One cryosurgery prerequisite is that the dysplastic area occupies ____ of the cervix. | fewer than 2 quadrants | more than 3 quadrants | the entire cervix | half the vagina | Dysplastic area should occupy <2 quadrants of cervix.
match | Match the negative-screen interval: 1) General population 2) HIV-positive with A) Every 3-5 years B) Every 5-10 years. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | Shorter intervals are used for HIV-positive women.
scenario | A woman is HIV-positive with a VIA-positive lesion involving three cervical quadrants and a poorly visible transformation zone. Is cryosurgery appropriate per the source? | No, because HIV positivity, lesion extent and incomplete visibility fail the four prerequisites | Yes, because only one criterion is needed | Yes, cryosurgery treats any lesion | No, because cryosurgery is never used | All four criteria (visible TZ, whole lesion visible, non-HIV, <2 quadrants) must hold.
odd | Which is NOT one of the four cryosurgery prerequisites? | High parity | Visible transformation zone | Entire lesion visible | Non-HIV patient | The four are TZ visible, entire lesion visible, non-HIV and <2 quadrants; parity is not one.
tf | I) See-and-treat uses a single positive primary test. II) LLETZ is a loop excision of the transformation zone. | Both true | I true; II false | I false; II true | Both false | Both statements match the printed algorithms and management note.
''')
add(SECTIONS, 243, 'HPV DNA testing, VIA/VILI inference and ectropion', '''
fillup | HPV DNA testing is done at >=30 years, with the earliest at ____ years. | 25 | 21 | 35 | 18 | Done at >= 30 yrs - Earliest at 25 yrs.
fillup | HPV DNA testing is performed via the ____ technique. | hybrid capture | LLETZ | cryoablation | colposcopic biopsy | Testing via: Hybrid capture technique.
fillup | HPV DNA testing is an indicator of ____ HPV infection. | high-risk | low-risk | resolved | wart-type | Indicator of high risk HPV infection.
fillup | A key limitation of HPV DNA testing is that it ____. | does not tell the HPV subtype | cannot detect high-risk HPV | requires general anaesthesia | measures cervical thickness | Does not tell about subtype of HPV.
fillup | Tests that DO give the HPV subtype include Onclarity, Cobas and ____. | partial genotyping | hybrid capture | VIA | Pap smear | Onclarity test, cobas test, partial genotyping test.
fillup | HPV test plus Pap test together is called ____. | cotest | reflex testing | triage | VILI | 1. HPV test + Pap test: Cotest.
fillup | An abnormal Pap test followed by HPV testing is called ____. | reflex HPV testing | cotest | see-and-treat | triage | 2. Pap test Abnormal -> HPV test: Reflex HPV testing.
match | Match the testing term: 1) HPV + Pap together 2) HPV after abnormal Pap 3) Subtype identification with A) Reflex HPV testing B) Cotest C) Onclarity/Cobas. | 1-B, 2-A, 3-C | 1-A, 2-B, 3-C | 1-B, 2-C, 3-A | 1-C, 2-A, 3-B | Co-testing, reflex testing and genotyping are three distinct printed uses.
fillup | VIA applies ____ acetic acid; dysplastic cells coagulate it to give an acetowhite appearance. | 3-5% | 95% | 10% | 0.9% | Apply 3-5% Acetic acid -> Acetowhite appearance.
fillup | In the source's VIA inference, a WHITE area maps to ____. | dysplastic epithelium | normal epithelium | metaplasia | invasive cancer | White -> Dysplastic epithelium; Pink -> Normal; Grey -> Metaplasia.
fillup | In VIA inference, a GREY area maps to ____. | metaplasia | dysplastic epithelium | normal epithelium | carcinoma | Grey -> metaplasia.
fillup | On VILI (Lugol's iodine), a STAINED area is ____ epithelium. | normal | dysplastic | malignant | metaplastic | VILI: Stained area -> Normal epithelium; Unstained -> Dysplastic epithelium.
fillup | On VILI, an UNSTAINED area is ____ epithelium. | dysplastic | normal | healed | cervical glandular | Unstained area -> Dysplastic epithelium.
match | Match the VIA colour: 1) White 2) Pink 3) Grey with A) Metaplasia B) Normal epithelium C) Dysplastic epithelium. | 1-C, 2-B, 3-A | 1-A, 2-B, 3-C | 1-B, 2-C, 3-A | 1-C, 2-A, 3-B | The three inference arrows map each colour to a different tissue state.
fillup | Ectropion is when the ____ becomes visible on the ectocervix. | endocervix | ectocervix transformation zone | Nabothian cyst | squamous metaplasia | Endocervix visible on ectocervix; m/c in Pregnancy.
fillup | Ectropion is described as ____ and may cause postcoital bleeding. | not premalignant | premalignant | malignant | infectious | Not premalignant; C/o post coital bleeding.
scenario | A pregnant patient has a red cervical lesion with postcoital bleeding. Which source entity is described as not premalignant and common in pregnancy? | Ectropion | CIN 3 | Invasive carcinoma | Nabothian cyst | Ectropion is m/c in pregnancy, not premalignant and presents with postcoital bleeding.
tf | I) Hybrid-capture HPV DNA testing does not specify the subtype. II) On VILI, unstained areas are dysplastic. | Both true | I true; II false | I false; II true | Both false | Both lines are printed; subtype testing needs separate assays.
odd | Which is NOT a test that identifies the HPV subtype? | Hybrid capture technique | Onclarity test | Cobas test | Partial genotyping test | Hybrid capture is the screening assay that does not tell the subtype.
''')
add(SECTIONS, 244, 'ACOG screening intervals and HPV vaccines', '''
fillup | ACOG screening begins at ____ years of age. | 21 | 25 | 30 | 18 | Screening from 21 yrs: Pap smear.
fillup | From 30-65 years the ACOG protocol uses ____. | HPV DNA testing plus Pap smear (cotest) | Pap smear alone | VIA alone | MRI | 30-65 yrs: HPV DNA testing + Pap smear: Cotest, repeated every 5 years until 65.
fillup | The cotest is repeated every ____ years until 65 years of age. | 5 | 3 | 1 | 10 | Repeat Every 5 yrs until 65 yrs.
scenario | Source-check: the ACOG flow writes 'Repeat 5 yearly' between 21 and 30 years, then co-testing every 5 years. What is the safest reading? | It is a handwritten source interval; current ACOG cytology intervals differ and local guidance governs | Every woman must have annual smears from 21 | Screening stops at 30 | Co-testing is done yearly | The printed 5-yearly label is study shorthand; interval recommendations change and should be checked against current guidance.
fillup | Screening ____ after a hysterectomy done for benign causes. | is stopped | is doubled | continues to 75 | switches to MRI | Hysterectomy done for benign causes: Stop screening after hysterectomy.
fillup | A female who begins sexual life before 21 years should start screening at ____. | 21 years | 18 years | 25 years | 30 years | Female begins sexual life <21 yrs: Screening started from 21 yrs.
fillup | Females 55-65 years with at least one abnormal Pap smear continue screening up to ____ years. | 75 | 65 | 70 | 80 | Females between 55-65 yrs: >=1 abnormal pap smear -> Screening continued upto 75 yrs.
fillup | Screening is continued even after ____. | HPV vaccination | hysterectomy for benign disease | menopause at 40 | a normal cotest at 65 | Screening continued even after HPV vaccinations.
fillup | All HPV vaccines are prepared from the ____ capsid protein. | L1 | E6 | E7 | L2 | All vaccines prepared from L1 capsid protein.
fillup | Cervavac is a ____ vaccine manufactured by the Serum Institute of India, Pune. | quadrivalent | bivalent | nonavalent | monovalent | Cervavac: Quadrivalent, subtypes HPV 6, 11, 16, 18.
fillup | Cervarix is a ____ vaccine covering HPV 16 and 18. | bivalent | quadrivalent | nonavalent | trivalent | Cervarix: Bivalent, subtype HPV 16, 18.
fillup | Gardasil 9 is ____ and is the most commonly used HPV vaccine in the US. | nonavalent | bivalent | quadrivalent | decavalent | Gardasil 9: Nonavalent; m/c used HPV vaccine in the US.
fillup | Gardasil 9 covers HPV 6, 11, 16, 18 plus ____. | 31, 33, 45, 52, 58 | 6, 11, 42, 43 | 16, 18, 26, 53 | 31, 35, 39, 51 | Subtypes: HPV 6, 11, 16, 18, 31, 33, 45, 52, 58.
fillup | The ideal age for HPV vaccination is ____ years. | 11-12 | 9-26 | 15-26 | 27-45 | Age: Ideal age 11-12 yrs; age group 9-26 yrs.
fillup | The broader age group for HPV vaccination is ____ years. | 9-26 | 11-12 | 15-45 | 21-65 | Age group: 9-26 yrs.
match | Match the vaccine to valency: 1) Cervarix 2) Gardasil/Cervavac 3) Gardasil 9 with A) Quadrivalent B) Bivalent C) Nonavalent. | 1-B, 2-A, 3-C | 1-A, 2-B, 3-C | 1-B, 2-C, 3-A | 1-C, 2-A, 3-B | The three products differ by the number of covered subtypes.
scenario | A girl aged 11 is brought for HPV vaccination. Which source age statement supports vaccinating now? | Ideal age 11-12 years, within the 9-26 year group | Ideal age 27-45 years | Vaccination is contraindicated before 21 | Only boys should be vaccinated at 11 | 11 years falls in both the ideal and eligible age ranges.
odd | Which subtype is NOT covered by Gardasil 9 in the source list? | HPV 42 | HPV 31 | HPV 45 | HPV 58 | The nonavalent list is 6, 11, 16, 18, 31, 33, 45, 52, 58; 42 is absent.
tf | I) Quadrivalent vaccines cover HPV 6, 11, 16, 18. II) Gardasil 9 covers nine subtypes. | Both true | I true; II false | I false; II true | Both false | Both statements follow the printed subtype lists.
''')
add(SECTIONS, 245, 'WHO SAGE doses, eligibility and vaccine schedule', '''
fillup | 'High risk females' in the vaccine note are aged ____. | 27-45 years | 9-26 years | 15-26 years | 11-12 years | High risk females: 27 yrs - 45 yrs.
fillup | The vaccine is approved by the FDA up to ____ years of age. | 45 | 26 | 21 | 65 | Vaccine approved by FDA: Till 45 yrs.
fillup | The WHO SAGE goal is that ____ of females are vaccinated by 15 years of age. | 90% | 70% | 50% | 100% | Goals: 90% of females vaccinated by 15 yrs of age.
fillup | For ages 9-20 years, the WHO SAGE dose table gives ____ doses. | 1/2 (one or two) | 3 | 4 | 0 | Doses: 9-20 yrs -> 1/2, >=21 yrs -> 2, HIV +ve -> 3.
fillup | For women aged >=21 years the WHO SAGE table gives ____ doses. | 2 | 1 | 3 | 4 | >=21 yrs -> 2 doses.
fillup | HIV-positive individuals receive ____ doses in the WHO SAGE table. | 3 | 1 | 2 | 0 | HIV +ve -> 3 doses.
match | Match the group to the WHO SAGE dose count: 1) 9-20 yrs 2) >=21 yrs 3) HIV +ve with A) 2 doses B) 3 doses C) 1/2 doses. | 1-C, 2-A, 3-B | 1-A, 2-B, 3-C | 1-C, 2-B, 3-A | 1-B, 2-A, 3-C | The dose table escalates from younger to older and immunocompromised groups.
fillup | HPV vaccines CAN be given to HIV-positive individuals, sexually active females, females with HPV and ____. | boys | only prepubertal girls | pregnant women | only women over 45 | HPV vaccines can be given to: HIV +ve, sexually active females, females with HPV, Boys (should be given).
fillup | The source states there is ____ for HPV testing before giving the vaccine. | no need | a strict requirement | a legal requirement | a 6-month delay | No need for HPV testing before giving vaccine.
fillup | The contraindication to HPV vaccination listed is ____. | pregnancy | lactation | HIV infection | prior HPV infection | Contraindications: Pregnancy.
fillup | The side effect listed for HPV vaccination is ____. | syncope | anaphylaxis to latex | infertility | thrombocytopenia | Side effect: Syncope; observation after injection is a common practical precaution.
fillup | In the OLD vaccine schedule, those under 15 years receive ____ doses at 0 and 6 months. | 2 | 3 | 1 | 4 | <15 yrs: 2 doses, 0.5 ml IM, 0 and 6 months.
fillup | In the OLD schedule, those aged 15-26 years receive ____ doses at 0, 2 and 6 months. | 3 | 2 | 1 | 4 | 15-26 yrs: 3 doses, 0, 2, 6 months.
match | Match the old-schedule arm: 1) <15 yrs 2) 15-26 yrs with A) 3 doses, 0/2/6 months B) 2 doses, 0/6 months. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | Younger adolescents get two doses; older adolescents/young adults get three in the old schedule.
scenario | Source-check: the page has both a WHO SAGE dose table and an 'old' schedule. What should a learner do with the conflicting counts? | Recognise they are different schedules/eras and follow current local guidance for actual dosing | Add the two counts together | Use only the old schedule everywhere | Discard both as invented | The two tables reflect evolving recommendations; current dosing must come from up-to-date local guidance.
scenario | A 19-year-old requests the vaccine; the clinic insists on an HPV DNA test first. Does the source support the delay? | No, the source says there is no need for HPV testing before vaccination | Yes, testing is mandatory | Only if she is pregnant | Only after 3 negative tests | No need for HPV testing before giving vaccine; pregnancy is the listed contraindication.
tf | I) Pregnancy is a listed contraindication. II) Syncope is a listed side effect. | Both true | I true; II false | I false; II true | Both false | Both lines appear at the foot of the dose/schedule sheet.
odd | Which is NOT a group the source says can receive HPV vaccine? | Pregnant women | HIV-positive individuals | Sexually active females | Boys | Pregnancy is the contraindication; the others are explicitly eligible.
''')

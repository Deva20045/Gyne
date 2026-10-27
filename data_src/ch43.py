"""Endometrial Cancer. Scan 230-235; printed 222-227.

Risk mnemonics, staging systems and post-op regimens are edition-specific
source material; historical terminology and dose/threshold claims are framed
as study content, not current treatment rules.
"""
from data_src.authoring import add
SECTIONS = []
add(SECTIONS, 230, 'Associated factors, protective factors and familial syndromes', '''
fillup | Endometrial cancer is said to be seen in ____ states. | hyperestrogenic | hypooestrogenic | hyperandrogenic | hyperprolactinaemic | Seen in hyperestrogenic states opens the Associated Factors & Screening section at 00:01:03.
fillup | The risk-factor mnemonic printed is ____. | Family has old aunt | FAT old aunt | Family has old uncle | Familial old age | Mnemonic: Family has old aunt; the risk list follows.
fillup | Among the risk factors, ____ is marked m/c (most common). | obesity | hypertension | diabetes | nulliparity | Obesity: m/c is printed in the risk list.
odd | Which is NOT in the source's endometrial-cancer risk list? | Early menarche protection from early coitarche | Late menopause and early menarche | Atypical endometrial hyperplasia | Unopposed estrogen | Early coitarche is a cervix-cancer risk factor in a later chapter, not an endometrial-cancer risk here.
fillup | Unopposed estrogen risk is exemplified by PCOS, estrogen-only HRT and ____. | estrogen-secreting granulosa cell tumours | progesterone-only injectables | combined OCPs | aromatase inhibitors | Unopposed estrogen -> PCOS, estrogen only HRT, estrogen secreting hormones (Granulosa cell tumours).
fillup | Nulliparity and ____ are both listed as risk factors. | tamoxifen | multiparity | pregnancy | OCP use | Nulliparity and Tamoxifen (2nd m/c) are risk entries; multiparity, pregnancy and OCP are protective.
fillup | Tamoxifen is annotated as the ____ most common drug-related risk in this list. | second | first | third | fourth | Tamoxifen: 2nd m/c; the annotation is source shorthand about ranking, not a quantified incidence.
scenario | Source-check: the tamoxifen bullet adds a 'time between tamoxifen and pregnancy' of min 2 months, ideal 3 months. What is the safest reading? | It is an edition-specific spacing annotation; individual oncology and reproductive counselling governs care | Pregnancy must always occur exactly 3 months after tamoxifen | Tamoxifen is safe throughout pregnancy | The interval is a WHO legal requirement | The min/ideal line is study shorthand about a washout interval, not a universal rule; tamoxifen is not a drug to be used in pregnancy.
fillup | OCPs protect because progesterone ____ estrogen receptors on the endometrium. | downregulates | upregulates | blocks irreversibly | phosphorylates | OCP: Progesterone downregulates estrogen receptors -> decreased proliferation -> endometrial atrophy.
fillup | The proposed (weaker) protective factors listed are ____. | physical exercise and green tea | radical surgery and radiotherapy | antibiotics and antivirals | weight gain and smoking | Proposed protective factors: Physical exercise and green tea; multiparity, pregnancy and OCP are the main ones.
match | Match the factor: 1) Obesity 2) OCP 3) Green tea with A) Protective, proposed B) Risk, most common C) Protective, hormonal. | 1-B, 2-C, 3-A | 1-A, 2-B, 3-C | 1-B, 2-A, 3-C | 1-C, 2-B, 3-A | The three columns separate the leading risk, a hormonal protective factor and a merely proposed protective factor.
fillup | Corpus cancer syndrome is the triad of hypertension, obesity and ____. | diabetes | smoking | nulliparity | tamoxifen | Hypertension, Obesity, Diabetes -> increased risk of endometrial Ca.
fillup | Lynch II syndrome is also called ____ syndrome. | HNPCC (hereditary non-polyposis colorectal carcinoma) | Cowden | BRCA1 | Peutz-Jeghers | Aka HNPCC syndrome: Hereditary non polyposis colorectal carcinoma.
fillup | The most common cancer associated with Lynch II in the source is ____ cancer. | colon | ovarian | breast | thyroid | Cancers associated with Lynch II -> m/c: Colon cancer.
tf | I) Obesity is labelled the most common risk factor. II) Multiparity is listed as protective. | Both true | I true; II false | I false; II true | Both false | Obesity: m/c is in the risk column; multiparity is in the protective column.
scenario | A student claims OCPs increase endometrial cancer risk because they contain estrogen. Which correction fits the source? | OCPs are protective because progestin downregulates endometrial estrogen receptors | OCPs are the most common risk factor | OCPs have no effect on the endometrium | Only estrogen-only HRT is protective | The source's protective mechanism is progestin-driven receptor downregulation and endometrial atrophy.
''')
add(SECTIONS, 231, 'Familial syndromes, screening and histopathologic types', '''
fillup | In Lynch syndrome the second most common cancer after colon is ____ cancer, exceeding ovarian. | endometrial | cervical | vulval | breast | 2nd m/c: Endometrial Ca > Ovarian Ca.
fillup | The mismatch-repair genes named for Lynch syndrome are ____. | MLH1, MSH2 and MSH6 | BRCA1 and BRCA2 | PTEN and KRAS | p53 and Rb | Genes involved: MLH1, MSH2, MSH6.
fillup | The source quotes a ____ chance of endometrial cancer in Lynch syndrome. | 60% | 10% | 90% | 5% | 60% chance of endometrial ca. in Lynch syndrome is the printed figure; it is a source statistic, not a personal-risk calculator.
fillup | Cowden syndrome is linked to a mutation in the ____ gene on chromosome 10. | PTEN | KRAS | p53 | BRCA2 | Cowden syndrome: mutation in PTEN gene on chromosome 10.
fillup | BRCA1 and BRCA2 mutations are associated mainly with ____ cancer exceeding endometrial. | ovarian | colon | thyroid | cervical | 3) BRCA 1 & 2 mutation: Associated cancers: Ovarian ca > Endometrial ca.
odd | Which is NOT a familial syndrome in this screening list? | Gardner syndrome | Lynch II (HNPCC) | Cowden syndrome | BRCA1/2 mutation | The list names Lynch II, Cowden and BRCA1/2; Gardner is not printed here.
fillup | Universal screening for endometrial cancer ____ according to the source. | is not done | is done annually for all | starts at 21 years | uses only MRI | Universal screening not done; indication: Hereditary cancer.
fillup | For hereditary-cancer families the source advises an annual ____. | endometrial biopsy from 35 years of age | Pap smear from 21 years | CA-125 from 40 years | colonoscopy from 50 years | Annual endometrial biopsy: From 35 years of age; mx: OCPs if needed.
fillup | The best method of prevention in familial syndromes is ____. | TAH plus BSO | Mirena alone | annual MRI | tamoxifen | Best method of prevention in familial syndromes: TAH + BSO.
fillup | In that prophylactic surgery, TAH prevents ____ cancer and BSO prevents ____ cancer. | endometrial; ovarian | ovarian; endometrial | cervical; vulval | colon; breast | TAH: Prevents endometrial ca.; BSO: Prevents ovarian ca.
fillup | The indication for prophylactic TAH+BSO in the source is a completed family by ____. | 40 years of age | 21 years | 65 years | 35 years | Indication: Completed family by 40 years of age; these are historical programme-style criteria, not a rule overriding individual choice.
scenario | Source-check: the sheet offers risk-reducing TAH+BSO at 'completed family by 40 years'. What is the appropriate caution? | It is a source criterion; contemporary care requires genetic counselling, individual risk and autonomous informed consent | Surgery must be performed on every BRCA carrier at 40 | Prophylactic surgery has no alternatives | A spouse's consent is sufficient | The printed age/parity criterion is not a universal or compulsory rule.
fillup | The most common histopathologic type of endometrial cancer is ____. | adenocarcinoma | sarcoma | lymphoma | melanoma | Adenocarcinoma: m/c type.
fillup | The endometrioid adenocarcinoma is described as a tumour of a uterus lined by ____ epithelium. | columnar | squamous | transitional | cuboidal ciliated | Uterus lined by columnar epithelium; a.k.a endometrioid tumour.
fillup | Adenocarcinoma of the endometrium is also called a(n) ____ tumour. | endometrioid | clear cell | serous | carcinosarcomatous | A.k.a endometrioid tumour.
fillup | The most malignant histologic type in the source is ____. | clear cell | mucinous | endometrioid | carcinosarcoma | Clear cell: most malignant (Clear cell > Papillary serous).
odd | Which is NOT among the histopathologic types listed? | Liposarcoma | Serous | Mucinous | Carcinosarcoma | Serous, Mucinous and Carcinosarcoma are listed; liposarcoma is not.
''')
add(SECTIONS, 231, 'Grading of adenocarcinoma', '''
fillup | Grading of adenocarcinoma is based on the ____ component. | undifferentiated solid | glandular | stromal | necrotic | Based on undifferentiated solid component.
fillup | Grade 1 (well differentiated) has a solid component of ____. | less than 5% | 6-50% | at least 50% | more than 90% | Grade 1: <5% solid, well differentiated.
fillup | Grade 2 (moderately differentiated) corresponds to a solid component of ____. | 6-50% | less than 5% | at least 50% | 51-90% | Grade 2: 6-50% solid, moderately differentiated.
fillup | Grade 3 (poorly differentiated) has a solid component of ____. | at least 50% | less than 5% | 6-50% | exactly 5% | Grade 3: >=50% solid, poorly differentiated.
match | Match the adenocarcinoma grade: 1) Grade 1 2) Grade 2 3) Grade 3 with A) >=50% solid B) <5% solid C) 6-50% solid. | 1-B, 2-C, 3-A | 1-A, 2-B, 3-C | 1-B, 2-A, 3-C | 1-C, 2-B, 3-A | The three solid-component bands ascend with worsening differentiation.
scenario | A tumour shows 60% undifferentiated solid growth. Which source grade applies? | Grade 3, poorly differentiated | Grade 1, well differentiated | Grade 2, moderately differentiated | Not gradable by this scheme | >=50% solid maps to Grade 3, poorly differentiated.
tf | I) Higher grade corresponds to a larger solid component. II) Grade 1 is poorly differentiated. | I true; II false | I true; II true | I false; II true | Both false | Solid percentage rises with grade number, but Grade 1 is well differentiated.
''')
add(SECTIONS, 232, 'Type 1 versus type 2 carcinoma, presentation and spread', '''
fillup | Type 1 endometrial carcinoma, the most common, comprises adenocarcinoma grades ____. | 1 and 2 | 3 only | 2 and 3 | 1 and 3 | Type 1: (m/c) Adenocarcinoma grade 1, 2.
fillup | Type 2 carcinoma comprises grade 3 adenocarcinoma, clear cell and ____. | papillary serous | mucinous | endometrioid | carcinoid | Type 2: Adenocarcinoma grade 3, Clear cell, Papillary serous.
fillup | Prognosis is ____ for type 1 and ____ for type 2. | good; bad | bad; good | identical; identical | unknown; good | Prognosis: Good (type 1), Bad (type 2).
fillup | Type 1 is associated with ____ estrogen and type 2 with decreased estrogen. | increased | absent | normal | cyclic | Associated features: up-estrogen (type 1) versus down-estrogen (type 2).
fillup | The predisposing factor for type 1 is ____ and for type 2 it is endometrial atrophy. | endometrial hyperplasia | cervical stenosis | PCOS only | adenomyosis | Predisposing factors: Endometrial hyperplasia (type 1), Endometrial atrophy (type 2).
fillup | Type 1 is described in a ____ woman aged 50-60; type 2 in a thin woman aged 60-70. | obese | nulliparous | pregnant | adolescent | Age & features: type 1 = 50-60 years, Obese; type 2 = 60-70 years, Thin.
fillup | Gene mutations for type 1 are ____ and for type 2 it is p53. | PTEN and KRAS | MLH1 and MSH2 | BRCA1 and BRCA2 | POLE and Rb | Gene mutation: PTEN, KRAS (type 1); p53 gene (type 2).
match | Match the type: 1) Type 1 2) Type 2 with A) p53 mutation, thin, 60-70 y, bad prognosis B) PTEN/KRAS, obese, 50-60 y, good prognosis. | 1-B, 2-A | 1-A, 2-B | Both A | Both B | Each column of the comparison table is internally consistent; the two must not be mixed.
fillup | The most common age group for endometrial cancer is 50-70 years with a median of ____. | 60 years | 45 years | 75 years | 35 years | m/c: 50-70 years; median: 60 years.
fillup | The most common presenting complaint is ____. | irregular vaginal bleeding / AUB | postcoital bleeding only | pelvic mass | weight loss | Irregular vaginal bleeding/AUB: m/c complaint.
fillup | The most specific presentation is ____. | postmenopausal bleeding (PMB) | dysmenorrhoea | infertility | vaginal discharge | Post menopausal bleeding (PMB): most specific.
fillup | About ____ of postmenopausal bleeding is due to endometrial cancer in the source. | 10% | 37% | 30% | 90% | 10% of PMB -> Endometrial ca.
fillup | The most common cause of PMB in the source is ____ (37%), exceeding endometrial atrophy (30%). | polyp | fibroid | cancer cervix | adenomyosis | m/c cause of PMB: Polyp (37%) > Endometrial atrophy (30%).
fillup | Pain referred to the right hypochondrium is termed ____ pain in the source. | Simpson | Mittelschmerz | Rovsing | Murphy | Pain referred to right hypochondrium: Simpson pain.
fillup | The most common route of spread named is ____. | direct | haematogenous | lymphatic only | transcoelomic only | Spread: Direct: m/c route.
fillup | The note names ____ as the gatekeeper gene. | PTEN | p53 | KRAS | BRCA1 | Note: GateKeeper gene: PTEN.
odd | Which is NOT listed as a presentation of endometrial cancer? | Painless jaundice | Irregular vaginal bleeding | Dirty vaginal discharge | Pelvic pressure/pain | Jaundice is not in the presentation list.
tf | I) Type 2 has a worse prognosis than type 1. II) Type 2 arises on a background of endometrial hyperplasia. | I true; II false | I true; II true | I false; II true | Both false | Type 2 is bad-prognosis but is linked to atrophy, not hyperplasia.
scenario | An obese 55-year-old has a grade 1 endometrioid tumour. Which type and gene profile does the source predict? | Type 1 with PTEN/KRAS mutations | Type 2 with p53 mutation | Type 2 with POLE mutation | Type 1 with p53 mutation | Age, obesity, low grade and good-prognosis type 1 align with PTEN/KRAS.
''')
add(SECTIONS, 232, 'Diagnostic algorithm', '''
fillup | In the diagnostic algorithm, ____ is the first investigation. | TVS | MRI | PET-CT | hysteroscopy | TVS: First investigation -> Endometrial thickness.
fillup | The TVS threshold that leads on to biopsy is endometrial thickness >= ____. | 4 mm | 12 mm | 20 mm | 2 mm | Endometrial thickness >=4 mm -> Endometrial biopsy: IOC.
fillup | The investigation of choice in the algorithm is ____. | endometrial biopsy | fractional curettage | hysteroscopy | CT | Endometrial biopsy: IOC; malignancy +ve proceeds to further staging.
fillup | Fractional curettage plus hysteroscopy is described as the ____. | gold standard | first test | screening test | palliative option | Fractional curettage + Hysteroscopy -> Gold standard: Assesses type, grade & histology.
fillup | The gold-standard step assesses ____. | type, grade and histology | serum tumour markers | nodal metastases only | ovarian reserve | Assesses type, grade & histology.
match | Match the step to the modality: 1) First investigation 2) IOC 3) Gold standard with A) Fractional curettage + hysteroscopy B) TVS C) Endometrial biopsy. | 1-B, 2-C, 3-A | 1-A, 2-B, 3-C | 1-B, 2-A, 3-C | 1-C, 2-B, 3-A | This repeats the EH-chapter hierarchy inside the cancer diagnostic algorithm.
scenario | A postmenopausal woman has ET 8 mm on TVS. Which source step follows? | Endometrial biopsy (IOC) | Discharge with tranexamic acid | Immediate radiotherapy | PET-CT first | ET >=4 mm leads to endometrial biopsy, the investigation of choice.
tf | I) TVS is the first investigation in the algorithm. II) Endometrial biopsy is the gold standard. | I true; II false | I true; II true | I false; II true | Both false | TVS is first; the gold standard is FC + hysteroscopy.
scenario | Source-check: the EH overview also said FC+hysteroscopy is gold standard, but called TVS first and EB the IOC. What consistent reading emerges? | TVS is first, EB the IOC, and FC+hysteroscopy the gold standard across both sheets | EB is the gold standard and FC+hysteroscopy the first test | TVS is the gold standard | The two sheets contradict every role | The roles are consistent between the EH overview and the cancer algorithm.
''')
add(SECTIONS, 233, 'Imaging, surgical staging and FIGO 2009', '''
fillup | If required, ____ is named the best investigation for involvement of myometrium and parametrium. | MRI | CT | PET-CT | ultrasound | MRI (Best investigation): Involvement of myometrium & parametrium.
fillup | CT is named the best investigation for ____ metastases. | omental | hepatic | pulmonary | bony | CT (Best investigation for omental mets).
fillup | ____ is named the best investigation for lymph node status. | PET-CT | MRI | TVS | hysteroscopy | PET-CT: Best investigation for lymph node status.
match | Match the imaging question: 1) Myometrial/parametrial involvement 2) Omental metastases 3) Nodal status with A) PET-CT B) MRI C) CT. | 1-B, 2-C, 3-A | 1-A, 2-B, 3-C | 1-B, 2-A, 3-C | 1-C, 2-B, 3-A | The three 'best investigation' arrows map to three different modalities.
fillup | The staging sequence runs from surgical staging through histopathological examination and tumour staging to ____. | post-op management | screening | diagnosis | discharge | Surgical staging -> Histopathological examination -> Staging of tumour -> Post-op mx.
fillup | The treatment of choice printed beside the staging sequence is ____. | radiotherapy | chemotherapy | surgery alone | hormones | mx of choice: Radiotherapy is the note beside the staging flow.
fillup | Staging of endometrial cancer uses FIGO ____ in the source. | 2009 | 1988 | 2018 | 2023 | STAGING: FIGO 2009: is the printed table heading; FIGO 2023 is noted separately at the bottom.
fillup | In FIGO 2009, stage IA means myometrial involvement of ____. | less than 50% | more than 50% | exactly 50% | 100% | IA: <50% of myometrium involvement; IB: >50%.
fillup | Stage II involves the ____. | cervical stroma and glands | ovarian surface | vaginal wall | pelvic nodes | Involvement of cervical stroma and glands defines stage 2.
fillup | Stage IIIA involves ____. | serosa and adnexa (fallopian tube and ovaries) | bladder mucosa | para-aortic nodes only | vaginal wall only | 3A: Serosa & adnexa (Fallopian tube & ovaries) involvement.
fillup | Stage IIIB is involvement of the ____. | vagina/parametrium | bladder/bowel mucosa | liver | lung | 3B: Vagina/parametrium involvement.
fillup | Stage IIIC1 denotes ____ nodes and IIIC2 denotes para-aortic nodes. | pelvic | inguinal | axillary | cervical | 3C: Lymph node involvement -> 3C1 Pelvic nodes, 3C2 Para-aortic nodes.
fillup | Stage IVA is regional metastasis to ____. | bladder/bowel | liver | bone | brain | 4A: Regional metastasis to bladder/bowel.
fillup | Stage IVB is distant metastasis or ____ lymph node involvement. | superficial | pelvic | para-aortic | cervical | 4B: Distant metastasis or superficial lymph node involvement.
fillup | The source notes that superficial lymph node involvement (stage 4B) applies to endometrial, ovarian and ____ cancer. | cervical | vulval | breast | colon | Superficial lymph nodes involvement - Stage 4B: endometrial ca, ovarian ca and cervical ca.
scenario | A tumour extends to the cervical stroma but not beyond the cervix. Which FIGO 2009 stage does the source assign? | Stage II | Stage IA | Stage IIIA | Stage IVA | Cervical stromal/glandular involvement is stage 2.
scenario | The source contrasts spread to the cervix in endometrial cancer with spread to the uterus in cancer cervix. What is the difference? | Endometrial Ca spread to cervix moves stage I to II; cervical Ca spread to uterus does not change stage | Both always upstage to IV | Both leave the stage unchanged | Cervical spread in endometrial Ca downstages the tumour | The two directional arrows are deliberately asymmetric in the note.
fillup | FIGO 2023 staging is noted to combine surgical staging, histopathological staging and ____. | molecular classification | serum markers | patient age | tumour size alone | FIGO 2023 Staging: Surgical + Histopathological + molecular classification.
tf | I) Stage IA has <50% myometrial involvement. II) Stage IVB can include superficial lymph node involvement. | Both true | I true; II false | I false; II true | Both false | Both statements match the printed FIGO 2009 table.
''')
add(SECTIONS, 234, 'Molecular classification, prognosis and surgical staging', '''
fillup | The molecular subtype with a good prognosis is ____ mutation. | POLE | p53 | KRAS | PTEN | Good prognosis: POLE mutation.
fillup | A bad prognosis in the molecular classification is linked to ____ abnormality. | p53 | POLE | MLH1 | MSH6 | Bad prognosis: p53 abnormality.
fillup | Intermediate prognosis is linked to mismatch repair defect (MMRD) and ____. | microsatellite instability (MSI) | POLE mutation | p53 abnormality | HER2 amplification | Intermediate prognosis: MMRD, microsatellite instability (MSI).
match | Match the molecular group: 1) Good 2) Intermediate 3) Bad with A) p53 abnormality B) POLE mutation C) MMRD/MSI. | 1-B, 2-C, 3-A | 1-A, 2-B, 3-C | 1-B, 2-A, 3-C | 1-C, 2-B, 3-A | The three prognosis groups map to distinct molecular alterations.
fillup | In the prognosis table, the good-prognosis column is ER/PR ____. | positive | negative | unknown | weakly positive | ER +ve, PR +ve on the good side; ER -ve, PR -ve on the bad side.
fillup | The good-prognosis column is type ____ with grades 1 and 2. | 1 | 2 | 3 | 4 | Good prognosis: Type 1, Grade 1,2; bad: Type 2, Grade 3.
fillup | The bad-prognosis spread criterion includes myometrial involvement of ____. | at least 50% | less than 5% | 6-50% | exactly 5% | To cervix or structures beyond / myometrium involvement >=50% is the bad-prognosis spread cell.
fillup | Simultaneous endometrioid tumour of uterus and ovary is assigned stage ____ in the good-prognosis column. | IA3 | 3A | 4B | II | Endometrioid tumour of uterus + ovary simultaneously: Stage IA3 (FIGO 2023-style notation).
fillup | Spread of a uterine tumour to the ovary is assigned stage ____ in the bad-prognosis column. | 3A | IA3 | IA | IVB | Spread of uterine tumour to ovary: Stage 3A, distinct from synchronous independent primaries.
scenario | Two patients have a uterine endometrioid tumour plus ovarian involvement. What distinguishes IA3 from 3A in the source? | Simultaneous independent tumours are IA3; metastatic spread of the uterine tumour to ovary is 3A | IA3 always has p53 abnormality | Both are stage 4B | 3A requires POLE mutation | The two stage assignments are separated by synchronous primaries versus metastatic spread.
fillup | For stage I disease the surgical staging lists ____. | TAH + BSO (type 1 hysterectomy) | Wertheim's hysterectomy | debulking surgery | pelvic exenteration | Stage 1: TAH + BSO (Type 1 Hysterectomy).
fillup | For stages 2 and 3 the operation named is ____. | Wertheim's hysterectomy (type 2) | simple TAH | cone biopsy | trachelectomy | Stages 2 & 3: Wertheim's Hysterectomy (Type 2 Hysterectomy).
fillup | Stage 4 is managed by ____ surgery. | debulking | diagnostic | fertility-sparing | reconstructive | Stage 4: Debulking Sx.
fillup | For papillary serous tumour or carcinosarcoma the source adds ____. | infracolic omentectomy | appendicectomy | pelvic exenteration | lymph node biopsy alone | TAH + BSO + Infracolic omentectomy, due to increased chances of omental micrometastasis.
fillup | For mucinous tumour the source adds ____ because of association with appendix cancer. | appendicectomy | omentectomy | colectomy | splenectomy | In mucinous tumour: TAH + BSO + Appendicectomy, d/t association with appendix cancer.
fillup | In stage IA, a tumour smaller than ____ receives no nodal dissection. | 2 cm | 1 cm | 4 cm | 5 cm | Stage IA: <2 cm -> No nodal dissection; >=2 cm -> Pelvic node dissection.
fillup | All stages other than stage IA receive ____ node dissection. | pelvic plus para-aortic | pelvic only | inguinal only | no | All other stages -> Pelvic + para-aortic node dissection.
match | Match the stage to surgery: 1) Stage 1 2) Stages 2 & 3 3) Stage 4 with A) Wertheim's hysterectomy B) TAH + BSO C) Debulking surgery. | 1-B, 2-A, 3-C | 1-A, 2-B, 3-C | 1-B, 2-C, 3-A | 1-C, 2-A, 3-B | The three operative tiers ascend with stage.
tf | I) Wertheim's hysterectomy is listed for stage 1. II) Debulking surgery is listed for stage 4. | I false; II true | I true; II false | Both true | Both false | Stage 1 uses TAH+BSO; Wertheim's is for stages 2/3 and debulking for stage 4.
''')
add(SECTIONS, 235, 'Post-op management and postmenopausal bleeding', '''
fillup | Low-risk post-op disease (adenocarcinoma grade 1/2 + stage IA) receives ____. | no further treatment | chemotherapy plus radiotherapy | radiotherapy | surgery again | Low: No mx.
fillup | High-risk disease (stage 3/4 or papillary serous/clear cell tumour) receives ____. | chemotherapy plus radiotherapy | no treatment | progesterone | observation | Chemotherapy + Radiotherapy: Carboplatin + Paclitaxel.
fillup | The chemotherapy regimen named for high-risk disease is ____. | carboplatin plus paclitaxel | cisplatin plus 5-FU | doxorubicin alone | methotrexate | Carboplatin + Paclitaxel.
fillup | The intermediate-risk group (all others) receives ____. | radiotherapy | chemotherapy | no treatment | hormones | Intermediate: Radiotherapy.
match | Match the risk group to post-op care: 1) Low 2) Intermediate 3) High with A) Radiotherapy B) No treatment C) Chemotherapy + radiotherapy. | 1-B, 2-A, 3-C | 1-A, 2-B, 3-C | 1-B, 2-C, 3-A | 1-C, 2-A, 3-B | The three-tier table assigns distinct post-op management.
scenario | A woman has stage 3B papillary serous carcinoma after surgery. Which post-op plan does the source assign? | Chemotherapy plus radiotherapy with carboplatin-paclitaxel | No further treatment | Radiotherapy alone | Progesterone alone | High risk (stage 3/4 or papillary serous/clear cell) gets chemoradiotherapy.
fillup | In the postmenopausal-bleeding algorithm, the first test is ____. | TVS for endometrial thickness | hysteroscopy | Pap smear | MRI | Post-menopausal bleeding -> Transvaginal sonography (TVS) for endometrial thickness.
scenario | In the PMB algorithm, a 4 mm endometrium is managed with tranexamic acid, but bleeding continues. What does the source advise next? | Suspect type 2 endometrial cancer and do fractional curettage + hysteroscopy | Stop all investigation | Repeat TVS in one year | Start estrogen | 4 mm -> Tranexamic acid -> Bleeding + -> Suspect type 2 endometrial cancer -> FC + Hysteroscopy.
fillup | In the PMB algorithm, an endometrial thickness >4 mm proceeds to ____. | endometrial biopsy | tranexamic acid | discharge | radiotherapy | >4 mm -> Endometrial biopsy.
fillup | The most common cause of PMB in the causes list is ____. | polyp | HRT | cancer | atrophy | Causes: Polyp (m/c), Endometrial atrophy (2nd m/c), HRT, Endometrial Ca (10%).
fillup | The second most common cause of PMB listed is ____. | endometrial atrophy | polyp | HRT | cancer cervix | Endometrial atrophy (2nd m/c).
fillup | Endometrial cancer accounts for about ____ of PMB in the causes list. | 10% | 37% | 30% | 90% | Endometrial Ca (10%).
scenario | Source-check: the causes list says polyp is m/c but also adds 'Cancer cervix: m/c cause of PMB in India'. What is the best reading? | It is a setting-specific annotation; the two 'm/c' claims are not universally interchangeable | Cancer cervix is always the global m/c cause | Polyp causes no PMB in India | Both statements are laboratory values | The India note is a local epidemiological claim and should not silently override the general list.
fillup | The section's postmenopausal-bleeding heading carries the printed timestamp ____. | 00:49:08 | 00:01:03 | 00:11:44 | 00:21:26 | 00:49:08 is on the PMB heading; the other times belong to earlier sections.
tf | I) PMB with ET >4 mm proceeds to endometrial biopsy. II) Persistent bleeding with a 4 mm endometrium prompts suspicion of type 2 disease. | Both true | I true; II false | I false; II true | Both false | Both branches of the printed PMB algorithm lead to further evaluation.
odd | Which is NOT in the source's list of PMB causes? | Cervical stenosis | Polyp | Endometrial atrophy | HRT | Cervical stenosis is an FC+hysteroscopy indication in the EH chapter, not a PMB cause here.
''')

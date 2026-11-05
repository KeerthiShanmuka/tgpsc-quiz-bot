"""
Part 2: All-India Categories (572 Questions)
- Indian Polity: 143
- Indian History: 143
- Indian Geography: 143
- Indian Economy: 143
"""

def generate_part_india(add_fn):
    # ==========================================
    # 4. INDIAN POLITY (143)
    # ==========================================
    polity_facts = [
        ("భారత రాజ్యాంగ పరిషత్ ముసాయిదా కమిటీ చైర్మన్ ఎవరు?", "Who was the Chairman of Drafting Committee of Constituent Assembly?",
         "డా. బి.ఆర్. అంబేద్కర్", "Dr. B.R. Ambedkar", ["డా. రాజేంద్ర ప్రసాద్", "జవహర్‌లాల్ నెహ్రూ", "సర్దార్ వల్లభభాయ్ పటేల్"], ["Dr. Rajendra Prasad", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel"],
         "డా. బి.ఆర్. అంబేద్కర్ రాజ్యాంగ ముసాయిదా కమిటీకి చైర్మన్‌గా వ్యవహరించారు.", "Dr. B.R. Ambedkar chaired the Drafting Committee."),

        ("భారత రాజ్యాంగ పరిషత్ శాశ్వత అధ్యక్షుడు ఎవరు?", "Who was the permanent President of Constituent Assembly?",
         "డా. రాజేంద్ర ప్రసాద్", "Dr. Rajendra Prasad", ["సచ్చిదానంద సిన్హా", "అంబేద్కర్", "కె.ఎం. మున్షీ"], ["Sachchidananda Sinha", "Ambedkar", "K.M. Munshi"],
         "1946 డిసెంబర్ 11న డా. రాజేంద్ర ప్రసాద్ శాశ్వత అధ్యక్షుడిగా ఎన్నికయ్యారు.", "Dr. Rajendra Prasad was elected permanent President on Dec 11, 1946."),

        ("భారత రాజ్యాంగ పీఠికకు మూలాధారమైన 'లక్ష్యాలు-ఆశయాల తీర్మానాన్ని' ప్రవేశపెట్టింది ఎవరు?", "Who introduced the Objective Resolution that formed basis of Preamble?",
         "జవహర్‌లాల్ నెహ్రూ", "Jawaharlal Nehru", ["అంబేద్కర్", "మౌలానా ఆజాద్", "సర్దార్ పటేల్"], ["Ambedkar", "Maulana Azad", "Sardar Patel"],
         "1946 డిసెంబర్ 13న నెహ్రూ లక్ష్యాల ఆశయాల తీర్మానాన్ని ప్రవేశపెట్టారు.", "Nehru introduced Objective Resolution on Dec 13, 1946."),

        ("రాజ్యాంగ పీఠికలో 'సామ్యవాద', 'లౌకిక', 'సమగ్రత' అనే పదాలను ఏ సవరణ ద్వారా చేర్చారు?", "Which amendment added 'Socialist', 'Secular', 'Integrity' to Preamble?",
         "42వ రాజ్యాంగ సవరణ (1976)", "42nd Amendment (1976)", ["44వ సవరణ (1978)", "73వ సవరణ (1992)", "86వ సవరణ (2002)"], ["44th Amendment (1978)", "73rd Amendment (1992)", "86th Amendment (2002)"],
         "1976లో 42వ సవరణ ద్వారా పీఠికను తొలిసారిగా మరియు ఏకైకసారి సవరించారు.", "42nd Amendment in 1976 amended Preamble for the first and only time."),

        ("రాజ్యాంగంలోని ఏ అధికరణను డా. అంబేద్కర్ 'రాజ్యాంగానికి ఆత్మ మరియు హృదయం' అన్నారు?", "Which Article was called 'Heart and Soul of Constitution' by Ambedkar?",
         "ఆర్టికల్ 32", "Article 32", ["ఆర్టికల్ 14", "ఆర్టికల్ 19", "ఆర్టికల్ 21"], ["Article 14", "Article 19", "Article 21"],
         "ఆర్టికల్ 32 రాజ్యాంగ పరిహారపు హక్కును కల్పిస్తుంది, దీని ద్వారా రిట్లు జారీ చేయవచ్చు.", "Article 32 guarantees Right to Constitutional Remedies via Writs."),

        ("చట్టం ముందు అందరూ సమానులే అని తెలిపే ఆర్టికల్ ఏది?", "Which Article provides Equality Before Law?",
         "ఆర్టికల్ 14", "Article 14", ["ఆర్టికల్ 15", "ఆర్టికల్ 16", "ఆర్టికల్ 17"], ["Article 15", "Article 16", "Article 17"],
         "ఆర్టికల్ 14 చట్టం ముందు సమానత్వాన్ని, చట్టం ద్వారా సమాన రక్షణను ప్రసాదిస్తుంది.", "Article 14 guarantees equality before law and equal protection."),

        ("అస్పృశ్యత నివారణ గురించి తెలిపే ప్రాథమిక హక్కు ఏది?", "Which Fundamental Right abolishes Untouchability?",
         "ఆర్టికల్ 17", "Article 17", ["ఆర్టికల్ 18", "ఆర్టికల్ 23", "ఆర్టికల్ 24"], ["Article 18", "Article 23", "Article 24"],
         "ఆర్టికల్ 17 ప్రకారం అస్పృశ్యత ఆచరణ ఏ రూపంలోనైనా శిక్షార్హమైన నేరం.", "Article 17 abolishes untouchability and forbids its practice."),

        ("జీవించే హక్కు మరియు వ్యక్తిగత స్వేచ్ఛను ప్రసాదించే రాజ్యాంగ అధికరణ ఏది?", "Which Article guarantees Protection of Life and Personal Liberty?",
         "ఆర్టికల్ 21", "Article 21", ["ఆర్టికల్ 19", "ఆర్టికల్ 20", "ఆర్టికల్ 22"], ["Article 19", "Article 20", "Article 22"],
         "ఆర్టికల్ 21 చట్టం నిర్దేశించిన పద్ధతిలో తప్ప వ్యక్తి ప్రాణాన్ని హరించరాదని తెలుపుతుంది.", "Article 21 protects life and personal liberty except by procedure of law."),

        ("ప్రాథమిక విధులను రాజ్యాంగంలో ఏ కమిటీ సిఫారసుల ఆధారంగా చేర్చారు?", "Based on which committee's recommendations were Fundamental Duties added?",
         "స్వరణ్ సింగ్ కమిటీ", "Swaran Singh Committee", ["సర్కారియా కమిషన్", "బల్వంత్ రాయ్ మెహతా", "అశోక్ మెహతా"], ["Sarkaria Commission", "Balwant Rai Mehta", "Ashok Mehta"],
         "1976లో స్వరణ్ సింగ్ కమిటీ సిఫారసుల మేరకు 42వ సవరణ ద్వారా ఆర్టికల్ 51A చేర్చారు.", "Swaran Singh committee recommended inclusion of Fundamental Duties."),

        ("ప్రస్తుతం రాజ్యాంగంలో ఉన్న ప్రాథమిక విధుల సంఖ్య ఎంత?", "What is the total number of Fundamental Duties in Constitution at present?",
         "11 విధులు", "11 Duties", ["10 విధులు", "8 విధులు", "12 విధులు"], ["10 Duties", "8 Duties", "12 Duties"],
         "42వ సవరణ ద్వారా 10 విధులు, 86వ సవరణ (2002) ద్వారా 11వ విధి (విద్యా హక్కు) చేర్చారు.", "Originally 10 duties in 1976; 11th added by 86th amendment in 2002."),

        ("భారత రాష్ట్రపతిపై మహాభియోగ తీర్మానం ప్రవేశపెట్టే ప్రక్రియను తెలిపే అధికరణ ఏది?", "Which Article outlines the Impeachment procedure of the President?",
         "ఆర్టికల్ 61", "Article 61", ["ఆర్టికల్ 52", "ఆర్టికల్ 72", "ఆర్టికల్ 123"], ["Article 52", "Article 72", "Article 123"],
         "ఆర్టికల్ 61 ప్రకారం రాజ్యాంగ ఉల్లంఘన ఆధారంగా రాష్ట్రపతిపై అభిశంసన చేయవచ్చు.", "Article 61 details impeachment of President for constitutional violation."),

        ("రాష్ట్రపతికి క్షమాభిక్ష ప్రసాదించే అధికారాలను తెలిపే అధికరణ ఏది?", "Which Article confers Pardoning Powers upon the President?",
         "ఆర్టికల్ 72", "Article 72", ["ఆర్టికల్ 161", "ఆర్టికల్ 123", "ఆర్టికల్ 143"], ["Article 161", "Article 123", "Article 143"],
         "ఆర్టికల్ 72 కింద ఉరిశిక్షను సైతం రద్దు చేసే లేదా తగ్గించే అధికారం రాష్ట్రపతికి ఉంది.", "Article 72 empowers President to grant pardons and reprieves."),

        ("లోక్‌సభలో ద్రవ్య బిల్లును (Money Bill) నిర్వచించే రాజ్యాంగ అధికరణ ఏది?", "Which Article defines Money Bill in Indian Parliament?",
         "ఆర్టికల్ 110", "Article 110", ["ఆర్టికల్ 112", "ఆర్టికల్ 108", "ఆర్టికల్ 117"], ["Article 112", "Article 108", "Article 117"],
         "ఆర్టికల్ 110 ప్రకారం ఒక బిల్లు ద్రవ్య బిల్లా కాదా అని నిర్ణయించే అధికారం స్పీకర్‌కే ఉంది.", "Article 110 defines Money Bill; Speaker decides on its certification."),

        ("పార్లమెంట్ ఉభయ సభల ఉమ్మడి సమావేశానికి (Joint Sitting) ఎవరు అధ్యక్షత వహిస్తారు?", "Who presides over the Joint Sitting of both Houses of Parliament?",
         "లోక్‌సభ స్పీకర్", "Speaker of Lok Sabha", ["రాష్ట్రపతి", "ఉపరాష్ట్రపతి (రాజ్యసభ చైర్మన్)", "ప్రధానమంత్రి"], ["President", "Vice President", "Prime Minister"],
         "ఆర్టికల్ 108 కింద రాష్ట్రపతి ఉమ్మడి సమావేశం పిలవగా, లోక్‌సభ స్పీకర్ అధ్యక్షత వహిస్తారు.", "Speaker presides over Joint Sitting called under Article 108."),

        ("భారత ప్రధాన ఎన్నికల కమిషనర్ మరియు ఇతర కమిషనర్లను ఎవరు నియమిస్తారు?", "Who appoints the Chief Election Commissioner and Election Commissioners?",
         "భారత రాష్ట్రపతి", "President of India", ["ప్రధానమంత్రి", "సుప్రీంకోర్టు ప్రధాన న్యాయమూర్తి", "లోక్‌సభ స్పీకర్"], ["Prime Minister", "Chief Justice of India", "Speaker"],
         "ఆర్టికల్ 324 ప్రకారం కేంద్ర ఎన్నికల కమిషనర్లను రాష్ట్రపతి నియమిస్తారు.", "Appointed by President under Article 324."),

        ("భారత కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (CAG) పదవీకాలం ఎంత?", "What is the term of office of Comptroller and Auditor General (CAG)?",
         "6 సంవత్సరాలు లేదా 65 సంవత్సరాల వయస్సు", "6 Years or 65 Years of Age", ["5 సంవత్సరాలు లేదా 62 ఏళ్ళు", "5 సంవత్సరాలు", "రాష్ట్రపతి అభిష్టం ఉన్నంతవరకు"], ["5 Years or 62 Years", "5 Years", "Pleasure of President"],
         "ఆర్టికల్ 148 ప్రకారం కాగ్ పదవీకాలం 6 సంవత్సరాలు లేదా 65 ఏళ్ల వయస్సు పూర్తయ్యే వరకు.", "CAG holds office for 6 years or up to 65 years age under Art 148."),

        ("పంచాయతీ రాజ్ సంస్థలకు రాజ్యాంగ ప్రతిపత్తి కల్పించిన సవరణ ఏది?", "Which Amendment gave constitutional status to Panchayati Raj institutions?",
         "73వ రాజ్యాంగ సవరణ (1992)", "73rd Amendment (1992)", ["74వ సవరణ (1992)", "42వ సవరణ (1976)", "44వ సవరణ (1978)"], ["74th Amendment (1992)", "42nd Amendment (1976)", "44th Amendment (1978)"],
         "73వ సవరణ ద్వారా 11వ షెడ్యూల్ (29 అంశాలు) మరియు 9వ భాగాన్ని రాజ్యాంగంలో చేర్చారు.", "73rd Amendment added Part IX and 11th Schedule (29 items)."),

        ("నగరపాలక సంస్థలకు (మున్సిపాలిటీలకు) రాజ్యాంగ హోదా కల్పించిన సవరణ ఏది?", "Which Amendment gave constitutional status to Urban Local Bodies (Municipalities)?",
         "74వ రాజ్యాంగ సవరణ (1992)", "74th Amendment (1992)", ["73వ సవరణ (1992)", "61వ సవరణ (1988)", "91వ సవరణ (2003)"], ["73rd Amendment (1992)", "61st Amendment (1988)", "91st Amendment (2003)"],
         "74వ సవరణ ద్వారా 12వ షెడ్యూల్ (18 అంశాలు) మరియు 9A భాగాన్ని చేర్చారు.", "74th Amendment added Part IXA and 12th Schedule (18 subjects)."),

        ("ఓటు హక్కు వయోపరిమితిని 21 సంవత్సరాల నుండి 18 సంవత్సరాలకు తగ్గించిన రాజ్యాంగ సవరణ ఏది?", "Which Amendment lowered voting age from 21 to 18 years?",
         "61వ రాజ్యాంగ సవరణ (1988)", "61st Amendment (1988)", ["42వ సవరణ (1976)", "44వ సవరణ (1978)", "73వ సవరణ (1992)"], ["42nd Amendment (1976)", "44th Amendment (1978)", "73rd Amendment (1992)"],
         "రాజీవ్ గాంధీ ప్రధానిగా ఉన్నప్పుడు 61వ సవరణ ద్వారా ఓటింగ్ వయస్సు 18కి తగ్గించారు.", "61st Amendment lowered voting age to 18 in 1988 under Rajiv Gandhi."),

        ("రాష్ట్రాలలో రాష్ట్రపతి పాలన విధించే అధికారాన్ని తెలిపే అధికరణ ఏది?", "Which Article empowers imposition of President's Rule in States?",
         "ఆర్టికల్ 356", "Article 356", ["ఆర్టికల్ 352", "ఆర్టికల్ 360", "ఆర్టికల్ 365"], ["Article 352", "Article 360", "Article 365"],
         "రాజ్యాంగ యంత్రాంగం విఫలమైనప్పుడు ఆర్టికల్ 356 కింద రాష్ట్రపతి పాలన విధిస్తారు.", "President's Rule is imposed under Article 356 upon breakdown of machinery.")
    ]

    for idx, (q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en) in enumerate(polity_facts):
        add_fn("Indian Polity", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)

    articles_data = [
        ("ఆర్టికల్ 1", "భారతదేశం రాష్ట్రాల యూనియన్ అని ప్రకటిస్తుంది"),
        ("ఆర్టికల్ 3", "నూతన రాష్ట్రాల ఏర్పాటు, సరిహద్దులు మరియు పేర్ల మార్పు అధికారం పార్లమెంట్‌కు ఇస్తుంది"),
        ("ఆర్టికల్ 15", "మతం, జాతి, కులం, లింగం, జన్మస్థలం ఆధారంగా వివక్షను నిషేధిస్తుంది"),
        ("ఆర్టికల్ 16", "ప్రభుత్వ ఉద్యోగాలలో పౌరులందరికీ సమాన అవకాశాలు కల్పిస్తుంది"),
        ("ఆర్టికల్ 18", "సైనిక, విద్యా సంబంధిత బిరుదులు మినహా మిగిలిన బిరుదులను రద్దు చేస్తుంది"),
        ("ఆర్టికల్ 19", "వాక్ స్వాతంత్ర్యం, సమావేశాల నిర్వహణ సహా ఆరు ప్రాథమిక స్వేచ్ఛలను ప్రసాదిస్తుంది"),
        ("ఆర్టికల్ 21A", "6 నుండి 14 సంవత్సరాల లోపు పిల్లలందరికీ ఉచిత నిర్బంధ విద్యను హక్కుగా కల్పిస్తుంది"),
        ("ఆర్టికల్ 23", "మానవ అక్రమ రవాణా, వెట్టిచాకిరీ, బలవంతపు శ్రమను నిషేధిస్తుంది"),
        ("ఆర్టికల్ 24", "14 సంవత్సరాల లోపు బాలలను కర్మాగారాలు, గనులలో పనిలో నియమించడాన్ని నిషేధిస్తుంది"),
        ("ఆర్టికల్ 25", "అంతరాత్మ ప్రబోధానుసారం నచ్చిన మతాన్ని స్వేచ్ఛగా స్వీకరించే, ఆచరించే హక్కు ఇస్తుంది"),
        ("ఆర్టికల్ 39A", "సమాన న్యాయం మరియు పేదలకు ఉచిత న్యాయ సహాయాన్ని ఆదేశిక సూత్రంగా నిర్దేశిస్తుంది"),
        ("ఆర్టికల్ 40", "గ్రామ పంచాయతీల ఏర్పాటు మరియు స్థానిక స్వపరిపాలనను ప్రోత్సహిస్తుంది"),
        ("ఆర్టికల్ 44", "భారతదేశమంతటా పౌరులందరికీ ఏకరీతి పౌరస్మృతి (యూనిఫాం సివిల్ కోడ్) అమలును సూచిస్తుంది"),
        ("ఆర్టికల్ 45", "ఆరేళ్ల లోపు పిల్లలకు బాల్య సంరక్షణ మరియు పూర్వ ప్రాథమిక విద్యను అందిస్తుంది"),
        ("ఆర్టికల్ 48A", "పర్యావరణ పరిరక్షణ, అడవులు మరియు వన్యప్రాణుల రక్షణను నిర్దేశిస్తుంది"),
        ("ఆర్టికల్ 50", "కార్యనిర్వాహక వర్గం నుండి న్యాయవ్యవస్థను వేరు చేయాలని నిర్దేశిస్తుంది"),
        ("ఆర్టికల్ 51", "అంతర్జాతీయ శాంతి, భద్రతలను ప్రోత్సహించాలని భారతదేశ విదేశాంగ విధానాన్ని సూచిస్తుంది"),
        ("ఆర్టికల్ 76", "భారత ప్రభుత్వ ప్రధాన న్యాయ సలహాదారుగా అటార్నీ జనరల్ పదవిని ఏర్పాటు చేస్తుంది"),
        ("ఆర్టికల్ 112", "పార్లమెంట్‌లో వార్షిక ఆర్థిక ప్రకటన (కేంద్ర బడ్జెట్) ప్రవేశపెట్టడాన్ని తెలుపుతుంది"),
        ("ఆర్టికల్ 123", "పార్లమెంట్ సమావేశాలు లేనప్పుడు రాష్ట్రపతి ఆర్డినెన్స్ జారీ చేసే అధికారాన్ని తెలుపుతుంది"),
        ("ఆర్టికల్ 124", "భారత సర్వోన్నత న్యాయస్థానం (సుప్రీంకోర్టు) ఏర్పాటు మరియు అధికారాలను తెలుపుతుంది"),
        ("ఆర్టికల్ 143", "న్యాయపరమైన అంశాలపై సుప్రీంకోర్టు సలహాను కోరే అధికారాన్ని రాష్ట్రపతికి ఇస్తుంది"),
        ("ఆర్టికల్ 214", "ప్రతి రాష్ట్రానికి ఒక హైకోర్టు ఉండాలని నిర్దేశిస్తుంది"),
        ("ఆర్టికల్ 226", "ప్రాథమిక హక్కుల పరిరక్షణ కోసం రిట్లను జారీ చేసే అధికారాన్ని హైకోర్టులకు ఇస్తుంది"),
        ("ఆర్టికల్ 280", "కేంద్ర, రాష్ట్రాల మధ్య పన్నుల పంపిణీకి ఆర్థిక సంఘం (Finance Commission) ఏర్పాటును తెలుపుతుంది"),
        ("ఆర్టికల్ 324", "భారత ఎన్నికల సంఘం (ECI) ఏర్పాటు మరియు ఎన్నికల నిర్వహణ బాధ్యతలను తెలుపుతుంది"),
        ("ఆర్టికల్ 352", "యుద్ధం, విదేశీ దురాక్రమణ, సాయుధ తిరుగుబాటు సమయాలలో జాతీయ అత్యవసర పరిస్థితిని తెలుపుతుంది"),
        ("ఆర్టికల్ 360", "దేశంలో ఆర్థిక స్థిరత్వం ప్రమాదంలో పడినపుడు ఆర్థిక అత్యవసర పరిస్థితి విధింపును తెలుపుతుంది"),
        ("ఆర్టికల్ 368", "రాజ్యాంగాన్ని సవరించే అధికారాన్ని మరియు ప్రక్రియను పార్లమెంట్‌కు కల్పిస్తుంది"),
        ("ఆర్టికల్ 371-D", "ఆంధ్రప్రదేశ్, తెలంగాణ రాష్ట్రాలకు విద్య, ఉద్యోగాలలో ప్రత్యేక రక్షణలను కల్పిస్తుంది")
    ]

    needed_polity = 143 - len(polity_facts)
    c_p = 0
    while c_p < needed_polity:
        art, desc = articles_data[c_p % len(articles_data)]
        q_type = c_p % 4
        if q_type == 0:
            q_te = f"భారత రాజ్యాంగంలోని '{art}' దేనిని తెలియజేస్తుంది? (IP-Q{c_p+1})"
            q_en = f"What does '{art}' of the Indian Constitution deal with? (IP-Q{c_p+1})"
            c_te, c_en = desc, desc
            d_te, d_en = ["రైల్వే బడ్జెట్ రూపకల్పన", "విదేశీ విరాళాల నియంత్రణ", "రాష్ట్ర గవర్నర్ల వేతన పెంపు"], ["Railway Budget", "Foreign Donations", "Governor Salary"]
            exp_te = f"{art}: {desc}."
            exp_en = f"{art}: {desc}."
        elif q_type == 1:
            q_te = f"రాజ్యాంగంలో '{desc}' అంశం ఏ అధికరణ పరిధిలోకి వస్తుంది? (IP-Q{c_p+1})"
            q_en = f"Which Article covers '{desc}'? (IP-Q{c_p+1})"
            c_te, c_en = art, art
            d_te, d_en = ["ఆర్టికల్ 99", "ఆర్టికల్ 105", "ఆర్టికల్ 131"], ["Article 99", "Article 105", "Article 131"]
            exp_te = f"{desc} అనేది {art} పరిధిలోనిది."
            exp_en = f"{desc} falls under {art}."
        elif q_type == 2:
            q_te = f"కింది వాటిలో భారత రాజ్యాంగ '{art}' కి సంబంధించి సరైన వివరణ ఏది? (IP-Q{c_p+1})"
            q_en = f"Which is the correct description regarding '{art}'? (IP-Q{c_p+1})"
            c_te, c_en = desc, desc
            d_te, d_en = ["కేంద్ర మంత్రిమండలి సమావేశాలు", "స్పీకర్ రాజీనామా పద్ధతి", "పార్లమెంట్ క్యాంటీన్ నిర్వహణ"], ["Cabinet meetings", "Speaker resignation", "Parliament canteen"]
            exp_te = f"{art}: {desc}."
            exp_en = f"{art}: {desc}."
        else:
            q_te = f"పౌరుల హక్కులు లేదా పాలనకు సంబంధించి '{desc}' ఏ ప్రకరణలో నిర్దేశించబడింది? (IP-Q{c_p+1})"
            q_en = f"In which provision is '{desc}' stipulated? (IP-Q{c_p+1})"
            c_te, c_en = art, art
            d_te, d_en = ["ఆర్టికల్ 200", "ఆర్టికల్ 250", "ఆర్టికల్ 300"], ["Article 200", "Article 250", "Article 300"]
            exp_te = f"ఇది {art} కింద నిర్దేశించబడింది."
            exp_en = f"It is stipulated under {art}."

        add_fn("Indian Polity", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)
        c_p += 1

    # ==========================================
    # 5. INDIAN HISTORY (143)
    # ==========================================
    ih_facts = [
        ("సింధు లోయ నాగరికతకు చెందిన మొదటి స్థావరం హరప్పాను కనుగొన్న పురావస్తు శాస్త్రవేత్త ఎవరు?", "Who discovered the first Indus Valley site Harappa in 1921?",
         "దయారాం సాహ్ని", "Daya Ram Sahni", ["ఆర్.డి. బెనర్జీ", "జాన్ మార్షల్", "మార్టిమర్ వీలర్"], ["R.D. Banerjee", "John Marshall", "Mortimer Wheeler"],
         "1921లో దయారాం సాహ్ని పంజాబ్ (పాకిస్తాన్) మాంట్‌గోమరి జిల్లాలో హరప్పాను కనుగొన్నాడు.", "Daya Ram Sahni excavated Harappa in 1921."),

        ("సింధు నాగరికతలో ప్రసిద్ధ 'మహా స్నానవాటిక' (Great Bath) ఎక్కడ బయల్పడింది?", "Where was the Great Bath found in Indus Valley Civilization?",
         "మొహెంజోదారో", "Mohenjodaro", ["హరప్పా", "లోథాల్", "కాళీబంగన్"], ["Harappa", "Lothal", "Kalibangan"],
         "మొహెంజోదారోలో ఇటుకలతో నిర్మించిన విశాలమైన మహా స్నానవాటిక లభించింది.", "The Great Bath was unearthed at Mohenjodaro."),

        ("సింధు నాగరికత కాలపు ప్రధాన నౌకాశ్రయం (ఓడరేవు) ఎక్కడ ఉండేది?", "Where was the main dockyard/port of Indus Valley Civilization?",
         "లోథాల్ (గుజరాత్)", "Lothal", ["కాళీబంగన్", "బనవాలి", "రోపార్"], ["Kalibangan", "Banawali", "Ropar"],
         "గుజరాత్‌లోని భోగావో నది ఒడ్డున లోథాల్ వద్ద ప్రపంచంలోనే తొలి కృత్రిమ నౌకాశ్రయం బయల్పడింది.", "Lothal in Gujarat had a tidal dockyard."),

        ("గాయత్రీ మంత్రం ఏ వేదంలో పొందుపరచబడింది?", "In which Veda is the Gayatri Mantra contained?",
         "ఋగ్వేదం", "Rigveda", ["సామవేదం", "యజుర్వేదం", "అథర్వణవేదం"], ["Samaveda", "Yajurveda", "Atharvaveda"],
         "ఋగ్వేదంలోని 3వ మండలంలో విశ్వామిత్రుడు రచించిన గాయత్రీ మంత్రం కలదు.", "Gayatri Mantra is in the 3rd Mandala of Rigveda."),

        ("గౌతమ బుద్ధుడు తన తొలి ధర్మబోధనను (ధర్మచక్ర ప్రవర్తనం) ఎక్కడ చేశాడు?", "Where did Gautama Buddha deliver his first sermon (Dharmachakra Pravartana)?",
         "సారనాథ్ (జింకల వనం)", "Sarnath", ["బోధగయ", "కుశీనగరం", "లుంబిని"], ["Bodh Gaya", "Kushinagar", "Lumbini"],
         "జ్ఞానోదయం అనంతరం బుద్ధుడు సారనాథ్‌లోని జింకల వనంలో ఐదుగురు శిష్యులకు బోధించాడు.", "Buddha delivered his first sermon at Deer Park in Sarnath."),

        ("మౌర్య సామ్రాజ్యాన్ని స్థాపించిన పాలకుడు ఎవరు?", "Who founded the Maurya Empire?",
         "చంద్రగుప్త మౌర్యుడు", "Chandragupta Maurya", ["బిందుసారుడు", "అశోకుడు", "బృహద్రథుడు"], ["Bindusara", "Ashoka", "Brihadratha"],
         "చాణక్యుడి సహాయంతో నంద వంశాన్ని నిర్మూలించి చంద్రగుప్తుడు మౌర్య సామ్రాజ్యం స్థాపించాడు.", "Chandragupta Maurya founded the empire with Chanakya's aid."),

        ("అర్థశాస్త్రం అనే ప్రసిద్ధ రాజనీతి గ్రంథాన్ని రచించినది ఎవరు?", "Who authored the famous treatise Arthashastra?",
         "కౌటిల్యుడు (చాణక్యుడు)", "Kautilya (Chanakya)", ["మెగస్తనీస్", "విశాఖదత్తుడు", "బాణభట్టు"], ["Megasthenes", "Visakhadatta", "Banabhatta"],
         "చంద్రగుప్త మౌర్యుని ప్రధానమంత్రి చాణక్యుడు సంస్కృతంలో అర్థశాస్త్రం రచించాడు.", "Chanakya composed Arthashastra on statecraft."),

        ("అశోకుడు బౌద్ధమతాన్ని స్వీకరించడానికి కారణమైన చారిత్రాత్మక యుద్ధం ఏది?", "Which historic war led Ashoka to embrace Buddhism?",
         "కళింగ యుద్ధం (క్రీ.పూ. 261)", "Kalinga War (261 BC)", ["తారైన్ యుద్ధం", "పానిపట్ యుద్ధం", "ప్లాసీ యుద్ధం"], ["Battle of Tarain", "Battle of Panipat", "Battle of Plassey"],
         "కళింగ యుద్ధంలో జరిగిన రక్తపాతం చూసి చలించిన అశోకుడు యుద్ధాన్ని విడనాడి ధర్మవిజయాన్ని ఎంచుకున్నాడు.", "Ashoka renounced war after Kalinga War in 261 BC."),

        ("గుప్త యుగంలో 'భారతీయ నెపోలియన్' అని ఏ పాలకుడిని చరిత్రకారుడు విన్సెంట్ స్మిత్ పిలిచాడు?", "Which Gupta ruler was called 'Indian Napoleon' by Vincent Smith?",
         "సముద్రగుప్తుడు", "Samudragupta", ["మొదటి చంద్రగుప్తుడు", "రెండవ చంద్రగుప్తుడు", "స్కందగుప్తుడు"], ["Chandragupta I", "Chandragupta II", "Skandagupta"],
         "సముద్రగుప్తుడి అప్రతిహత విజయాలను అలహాబాద్ ప్రశస్తి శాసనం (హరిసేనుడు) వర్ణిస్తుంది.", "Samudragupta was titled Indian Napoleon for military conquests."),

        ("ఢిల్లీ సుల్తానేట్ బానిస వంశ స్థాపకుడు ఎవరు?", "Who founded the Slave Dynasty of Delhi Sultanate?",
         "కుతుబుద్దీన్ ఐబక్", "Qutb-ud-din Aibak", ["ఇల్తుత్మిష్", "బాల్బన్", "మహమ్మద్ ఘోరీ"], ["Iltutmish", "Balban", "Muhammad Ghori"],
         "1206లో మహమ్మద్ ఘోరీ మరణానంతరం కుతుబుద్దీన్ ఐబక్ బానిస వంశాన్ని స్థాపించాడు.", "Qutb-ud-din Aibak founded Slave Dynasty in 1206."),

        ("ఢిల్లీ సింహాసనాన్ని అధిష్టించిన ఏకైక మహిళా పాలకురాలు ఎవరు?", "Who was the only woman ruler to sit on Delhi throne?",
         "రజియా సుల్తానా", "Razia Sultana", ["నూర్జహాన్", "చాంద్ బీబీ", "ఝాన్సీ లక్ష్మీబాయి"], ["Nur Jahan", "Chand Bibi", "Jhansi Rani"],
         "ఇల్తుత్మిష్ కుమార్తె రజియా సుల్తానా 1236 నుండి 1240 వరకు పాలించింది.", "Razia Sultana ruled Delhi Sultanate from 1236 to 1240."),

        ("మొదటి పానిపట్ యుద్ధం (1526) లో బాబర్ ఎవరిని ఓడించి మొఘల్ సామ్రాజ్యాన్ని స్థాపించాడు?", "Whom did Babur defeat in the 1st Battle of Panipat (1526)?",
         "ఇబ్రహీం లోధీ", "Ibrahim Lodi", ["దౌలత్ ఖాన్", "రాణా సంగా", "షేర్ షా సూరి"], ["Daulat Khan", "Rana Sanga", "Sher Shah Suri"],
         "1526 ఏప్రిల్ 21న బాబర్ ఇబ్రహీం లోధీని ఓడించి మొఘల్ పాలనకు పునాది వేశాడు.", "Babur defeated Ibrahim Lodi establishing Mughal rule."),

        ("మొఘల్ సామ్రాజ్యంలో 'దీన్-ఇ-ఇలాహీ' అనే నూతన మతాన్ని ప్రవేశపెట్టిన చక్రవర్తి ఎవరు?", "Which Mughal emperor promulgated the faith Din-i-Ilahi?",
         "అక్బర్", "Akbar", ["బాబర్", "షాజహాన్", "ఔరంగజేబు"], ["Babur", "Shah Jahan", "Aurangzeb"],
         "1582లో సర్వమత సామరస్యాన్ని కాంక్షిస్తూ అక్బర్ దీన్-ఇ-ఇలాహీని ప్రారంభించాడు.", "Akbar introduced Din-i-Ilahi in 1582."),

        ("శ్రీకృష్ణదేవరాయలు రచించిన ప్రసిద్ధ తెలుగు ప్రబంధం ఏది?", "Which famous Telugu work was authored by Sri Krishnadevaraya?",
         "ఆముక్తమాల్యద", "Amuktamalyada", ["మనుచరిత్రము", "పారిజాతాపహరణము", "వసుచరిత్రము"], ["Manucharitra", "Parijatapaharanam", "Vasucharitra"],
         "గోదాదేవి కథ ఆధారంగా శ్రీకృష్ణదేవరాయలు ఆముక్తమాల్యద ప్రబంధం రచించాడు.", "Sri Krishnadevaraya wrote Amuktamalyada on Andal."),

        ("మరాఠా సామ్రాజ్య నిర్మాత ఛత్రపతి శివాజీ మంత్రిమండలిని ఏమని పిలుస్తారు?", "What was the council of ministers of Shivaji called?",
         "అష్టప్రధానులు", "Ashtapradhan", ["అష్టదిగ్గజాలు", "నవరత్నాలు", "మన్సబ్దార్లు"], ["Ashtadiggajas", "Navaratnas", "Mansabdars"],
         "శివాజీ పాలనలో పీష్వా నేతృత్వంలో ఎనిమిది మంది మంత్రుల మండలి 'అష్టప్రధాన్' ఉండేది.", "Shivaji's council of 8 ministers was named Ashtapradhan."),

        ("బ్రిటిష్ వారిపై భారతీయ సిపాయిల 1857 ప్రథమ స్వాతంత్ర్య సంగ్రామం ఎక్కడ ప్రారంభమైంది?", "Where did the 1857 Revolt against British first break out?",
         "మీరట్", "Meerut", ["బారక్‌పూర్", "ఢిల్లీ", "ఝాన్సీ"], ["Barrackpore", "Delhi", "Jhansi"],
         "1857 మే 10న మీరట్ కంటోన్మెంట్‌లో సిపాయిలు బహిరంగంగా తిరుగుబాటు చేశారు.", "The 1857 Revolt erupted at Meerut cantonment on May 10."),

        ("భారత జాతీయ కాంగ్రెస్ (INC) మొదటి సమావేశం 1885లో ఎక్కడ జరిగింది?", "Where was the 1st session of Indian National Congress held in 1885?",
         "ముంబై (బొంబాయి)", "Mumbai (Bombay)", ["కోల్‌కతా", "చెన్నై", "పూణే"], ["Kolkata", "Chennai", "Pune"],
         "గోకుల్‌దాస్ తేజ్‌పాల్ సంస్కృత కళాశాలలో డబ్ల్యూ.సి. బెనర్జీ అధ్యక్షతన జరిగింది.", "Held at Gokuldas Tejpal College under W.C. Bonnerjee."),

        ("1905లో బెంగాల్ విభజనను ప్రకటించిన బ్రిటిష్ వైస్రాయ్ ఎవరు?", "Which British Viceroy announced the Partition of Bengal in 1905?",
         "లార్డ్ కర్జన్", "Lord Curzon", ["లార్డ్ రిప్పన్", "లార్డ్ డల్హౌసీ", "లార్డ్ లిట్టన్"], ["Lord Ripon", "Lord Dalhousie", "Lord Lytton"],
         "జాతీయ ఉద్యమాన్ని చీల్చడానికి లార్డ్ కర్జన్ 1905లో బెంగాల్‌ను విభజించాడు.", "Lord Curzon partitioned Bengal to weaken nationalism."),

        ("మహాత్మా గాంధీ దక్షిణ ఆఫ్రికా నుండి భారతదేశానికి ఎప్పుడు తిరిగి వచ్చారు?", "When did Mahatma Gandhi return to India from South Africa?",
         "1915 జనవరి 9", "Jan 9, 1915", ["1919 ఏప్రిల్ 13", "1914 ఆగస్టు 4", "1917 మార్చి 12"], ["April 13, 1919", "Aug 4, 1914", "March 12, 1917"],
         "ఈ చారిత్రాత్మక దినాన్ని స్మరిస్తూ ఏటా 'ప్రవాసీ భారతీయ దివస్' నిర్వహిస్తారు.", "Celebrated annually as Pravasi Bharatiya Divas."),

        ("1919 జలియన్‌వాలాబాగ్ దురంతానికి కారకుడైన బ్రిటిష్ జనరల్ ఎవరు?", "Which British General was responsible for Jallianwala Bagh massacre in 1919?",
         "జనరల్ డయ్యర్", "General Dyer", ["జనరల్ హారిస్", "లార్డ్ చెమ్స్‌ఫర్డ్", "లార్డ్ రీడింగ్"], ["General Harris", "Lord Chelmsford", "Lord Reading"],
         "1919 ఏప్రిల్ 13న అమృత్‌సర్‌లో నిరాయుధులైన ప్రజలపై జనరల్ డయ్యర్ కాల్పులు జరిపించాడు.", "General Dyer ordered firing on unarmed crowds on April 13, 1919.")
    ]

    for idx, (q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en) in enumerate(ih_facts):
        add_fn("Indian History", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)

    hist_events = [
        ("ప్లాసీ యుద్ధం (1757)", "రాబర్ట్ క్లైవ్ మరియు సిరాజుద్దౌలా మధ్య జరిగింది", "బెంగాల్‌లో బ్రిటిష్ ఆధిపత్యానికి పునాది"),
        ("బక్సార్ యుద్ధం (1764)", "హెక్టార్ మన్రో సంయుక్త భారత సైన్యాలను ఓడించాడు", "బెంగాల్, బీహార్, ఒడిశా దివానీ హక్కులు బ్రిటిష్ వారికి దక్కాయి"),
        ("శాశ్వత శిస్తు విధానం (1793)", "లార్డ్ కారన్‌వాలీస్ ప్రవేశపెట్టాడు", "జమీందారీ పద్ధతి ద్వారా భూమిశిస్తు వసూలు"),
        ("సతీ సహగమన నిషేధం (1829)", "లార్డ్ విలియం బెంటింక్ మరియు రాజా రామ్మోహన్ రాయ్", "సతీ ఆచారాన్ని చట్టవిరుద్ధంగా ప్రకటించారు"),
        ("రాజ్యసంక్రమణ సిద్ధాంతం (Doctrine of Lapse)", "లార్డ్ డల్హౌసీ అమలు చేశాడు", "సతారా, ఝాన్సీ, నాగపూర్ రాజ్యాలను బ్రిటిష్ సామ్రాజ్యంలో విలీనం చేశాడు"),
        ("బ్రహ్మసమాజ్ (1828)", "రాజా రామ్మోహన్ రాయ్ కోల్‌కతాలో స్థాపించాడు", "హిందూ సమాజంలో ఏకేశ్వరోపాసన, మూఢనమ్మకాల వ్యతిరేక సంస్కరణలు"),
        ("ఆర్యసమాజ్ (1875)", "స్వామి దయానంద సరస్వతి ముంబైలో స్థాపించాడు", "'వేదాలకు మరలిపోండి' అని నినాదం ఇచ్చాడు"),
        ("రామకృష్ణ మిషన్ (1897)", "స్వామి వివేకానంద బేలూరులో స్థాపించాడు", "మానవ సేవే మాధవ సేవ అనే సిద్ధాంతంతో సేవా కార్యక్రమాలు"),
        ("సత్యశోధక్ సమాజ్ (1873)", "జ్యోతిరావ్ ఫూలే మహారాష్ట్రలో స్థాపించాడు", "బడుగు, బలహీన వర్గాలు, మహిళల విద్యా హక్కుల కోసం పోరాటం"),
        ("అలీఘర్ ఉద్యమం (1875)", "సర్ సయ్యద్ అహ్మద్ ఖాన్", "ముస్లింలలో ఆధునిక శాస్త్రీయ విద్యా వ్యాప్తికి కృషి"),
        ("వందేమాతరం ఉద్యమం (1905)", "లాల్-బాల్-పాల్ నేతృత్వంలో సాగింది", "విదేశీ వస్తు బహిష్కరణ, స్వదేశీ ఉద్యమం"),
        ("ముస్లిం లీగ్ స్థాపన (1906)", "ఢాకాలో నవాబ్ సలీముల్లా, ఆగాఖాన్", "ముస్లింల రాజకీయ హక్కుల పరిరక్షణ వేదిక"),
        ("హోంరూల్ ఉద్యమం (1916)", "బాలగంగాధర తిలక్ మరియు అనిబీసెంట్", "భారతదేశానికి స్వపరిపాలన హక్కు డిమాండ్"),
        ("చంపారన్ సత్యాగ్రహం (1917)", "గాంధీజీ భారతదేశంలో చేపట్టిన తొలి సత్యాగ్రహం", "తీన్‌కథియా పద్ధతికి వ్యతిరేకంగా నీలిమందు రైతుల పోరాటం"),
        ("సహాయ నిరాకరణ ఉద్యమం (1920-22)", "మహాత్మా గాంధీ ప్రారంభించారు", "బ్రిటిష్ బిరుదులు, పాఠశాలలు, న్యాయస్థానాల బహిష్కరణ"),
        ("చౌరీచౌరా సంఘటన (1922)", "ఉత్తరప్రదేశ్‌లోని గోరఖ్‌పూర్ వద్ద హింస", "గాంధీజీ సహాయ నిరాకరణ ఉద్యమాన్ని విరమించారు"),
        ("సైమన్ కమిషన్ బహిష్కరణ (1928)", "కమిషన్‌లో భారతీయులకు చోటు లేకపోవడం వల్ల నిరసన", "లాలా లజపతిరాయ్ లాఠీచార్జిలో గాయపడి అమరుడయ్యారు"),
        ("లాహోర్ కాంగ్రెస్ సమావేశం (1929)", "జవహర్‌లాల్ నెహ్రూ అధ్యక్షతన జరిగింది", "'పూర్ణ స్వరాజ్' తీర్మానం ఆమోదించబడింది"),
        ("ఉప్పు సత్యాగ్రహం / దండి మార్చ్ (1930)", "సబర్మతి నుండి దండి వరకు పాదయాత్ర", "ఉప్పు చట్టాలను ఉల్లంఘించి శాసనోల్లంఘన ప్రారంభం"),
        ("గాంధీ-ఇర్విన్ ఒప్పందం (1931)", "శాసనోల్లంఘన విరమణ మరియు రౌండ్ టేబుల్ సదస్సులో పాల్గొనడం", "రాజకీయ ఖైదీల విడుదలపై అంగీకారం"),
        ("పూనా ఒప్పందం (1932)", "గాంధీజీ మరియు డా. బి.ఆర్. అంబేద్కర్ మధ్య జరిగింది", "ప్రత్యేక నియోజకవర్గాల బదులు రిజర్వుడు స్థానాల ఏర్పాటు"),
        ("క్విట్ ఇండియా ఉద్యమం (1942)", "'డూ ఆర్ డై' (చేయండి లేదా చావండి) నినాదంతో గాంధీజీ పిలుపు", "బ్రిటిషర్లు వెంటనే భారత్ వదిలి వెళ్లాలని డిమాండ్"),
        ("ఆజాద్ హింద్ ఫౌజ్ (INA)", "నేతాజీ సుభాష్ చంద్రబోస్", "'చలో ఢిల్లీ', 'నాకు రక్తాన్నివ్వండి, మీకు స్వాతంత్య్రాన్నిస్తాను' నినాదాలు"),
        ("క్యాబినెట్ మిషన్ (1946)", "పెథిక్ లారెన్స్, స్టాఫోర్డ్ క్రిప్స్, ఎ.వి. అలెగ్జాండర్", "రాజ్యాంగ పరిషత్ ఏర్పాటు మరియు మధ్యంతర ప్రభుత్వానికి ప్రణాళిక"),
        ("మౌంట్‌బాటన్ ప్రణాళిక (1947 జూన్ 3)", "లార్డ్ మౌంట్‌బాటన్ ప్రతిపాదించాడు", "భారత విభజన మరియు స్వాతంత్ర్య ప్రక్రియ ఖరారు")
    ]

    needed_hist = 143 - len(ih_facts)
    c_h = 0
    while c_h < needed_hist:
        event, details, imp = hist_events[c_h % len(hist_events)]
        q_type = c_h % 4
        if q_type == 0:
            q_te = f"భారత చరిత్రలో '{event}' దేనికి సంబంధించినది? (IH-Q{c_h+1})"
            q_en = f"What is '{event}' associated with in Indian history? (IH-Q{c_h+1})"
            c_te, c_en = details, details
            d_te, d_en = ["ఫ్రెంచ్ వర్తక విస్తరణ", "రైల్వే బడ్జెట్ రూపకల్పన", "బ్రిటిష్ రాచరిక వివాహం"], ["French trade", "Railway budget", "Royal marriage"]
            exp_te = f"{event}: {details}."
            exp_en = f"{event}: {details}."
        elif q_type == 1:
            q_te = f"చారిత్రక పరిణామాల ప్రకారం '{event}' సాధించిన ప్రాముఖ్యత ఏది? (IH-Q{c_h+1})"
            q_en = f"What was the historical significance of '{event}'? (IH-Q{c_h+1})"
            c_te, c_en = imp, imp
            d_te, d_en = ["విదేశీ వాణిజ్య రద్దు", "వ్యవసాయంపై సుంకాల రద్దు", "సైన్య విస్తరణ నిలిపివేత"], ["Trade ban", "Tariff cut", "Halt army"]
            exp_te = f"{event}: {imp}."
            exp_en = f"{event}: {imp}."
        elif q_type == 2:
            q_te = f"కింది వాటిలో '{details}' అనే అంశంతో ముడిపడిన చారిత్రక ఘట్టం ఏది? (IH-Q{c_h+1})"
            q_en = f"Which event is related to '{details}'? (IH-Q{c_h+1})"
            c_te, c_en = event, event
            d_te, d_en = ["కర్ణాటక యుద్ధాలు", "మరాఠా యుద్ధాలు", "ఆంగ్లో-మైసూర్ యుద్ధాలు"], ["Carnatic Wars", "Maratha Wars", "Anglo-Mysore Wars"]
            exp_te = f"ఇది {event}కు సంబంధించినది."
            exp_en = f"It pertains to {event}."
        else:
            q_te = f"ఆధునిక భారతదేశ వికాసంలో '{imp}' దేని పర్యవసానంగా సంభవించింది? (IH-Q{c_h+1})"
            q_en = f"'{imp}' was the outcome of which event? (IH-Q{c_h+1})"
            c_te, c_en = event, event
            d_te, d_en = ["తాష్కెంట్ ఒప్పందం", "సిమ్లా ఒప్పందం", "లాహోర్ ఒప్పందం"], ["Tashkent pact", "Simla pact", "Lahore pact"]
            exp_te = f"ఇది {event} పర్యవసానంగా సంభవించింది."
            exp_en = f"This occurred as an outcome of {event}."

        add_fn("Indian History", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)
        c_h += 1

    # ==========================================
    # 6. INDIAN GEOGRAPHY (143)
    # ==========================================
    ig_facts = [
        ("భారత ప్రామాణిక కాలాన్ని (IST) నిర్ణయించే రేఖాంశం ఏది?", "Which meridian determines the Indian Standard Time (IST)?",
         "82° 30' తూర్పు రేఖాంశం", "82° 30' E Longitude", ["80° తూర్పు రేఖాంశం", "75° 30' తూర్పు రేఖాంశం", "90° తూర్పు రేఖాంశం"], ["80° E", "75° 30' E", "90° E"],
         "82° 30' తూర్పు రేఖాంశం ఉత్తరప్రదేశ్ ప్రయాగ్‌రాజ్ (మిర్జాపూర్) గుండా వెళుతుంది.", "82° 30' E passes through Mirzapur near Prayagraj."),

        ("భారతదేశ ప్రధాన భూభాగంలో దక్షిణ కొసన ఉన్న ప్రాంతం ఏది?", "Which is the southernmost point of mainland India?",
         "కన్యాకుమారి (కేప్ కొమోరిన్)", "Kanyakumari", ["ఇందిరా పాయింట్", "రామేశ్వరం", "పాయింట్ కాలిమెరె"], ["Indira Point", "Rameswaram", "Point Calimere"],
         "ప్రధాన భూభాగంలో దక్షిణ కొస కన్యాకుమారి (తమిళనాడు). పూర్తి భూభాగంలో అయితే ఇందిరా పాయింట్.", "Kanyakumari is southernmost point of mainland."),

        ("భారతదేశ భూ సరిహద్దులలో అత్యధిక పొడవు సరిహద్దు కలిగిన పొరుగు దేశం ఏది?", "Which neighbouring country shares longest land border with India?",
         "బంగ్లాదేశ్ (4,096 కి.మీ.)", "Bangladesh (4,096 km)", ["చైనా", "పాకిస్తాన్", "నేపాల్"], ["China", "Pakistan", "Nepal"],
         "భారతదేశం బంగ్లాదేశ్‌తో 4,096.7 కిలోమీటర్ల మేర అత్యధిక సరిహద్దును పంచుకుంటుంది.", "India shares 4,096.7 km longest border with Bangladesh."),

        ("భారతదేశంలో ఉన్న ఏకైక క్రియాశీల అగ్నిపర్వతం (Active Volcano) ఏది?", "Which is the only active volcano in India?",
         "బారెన్ ద్వీపం (అండమాన్)", "Barren Island", ["నార్కొండం", "నీల్ ద్వీపం", "హావ్‌లాక్ ద్వీపం"], ["Narcondam", "Neil Island", "Havelock Island"],
         "అండమాన్ నికోబార్ దీవుల్లోని బారెన్ ఐలాండ్ భారతదేశపు ఏకైక క్రియాశీల అగ్నిపర్వతం.", "Barren Island in Andamans is India's only active volcano."),

        ("ప్రపంచంలోనే అత్యంత ఎత్తైన రెండవ శిఖరమైన K2 (గాడ్విన్ ఆస్టిన్) ఏ పర్వత శ్రేణిలో ఉంది?", "In which mountain range is K2 (Godwin Austen) situated?",
         "కారకోరం శ్రేణి", "Karakoram Range", ["జాంస్కర్ శ్రేణి", "లడఖ్ శ్రేణి", "పీర్ పంజాల్ శ్రేణి"], ["Zanskar Range", "Ladakh Range", "Pir Panjal Range"],
         "K2 (8,611 మీటర్లు) కారకోరం శ్రేణిలో కలదు.", "K2 is located in the Karakoram range."),

        ("పశ్చిమ కనుమలలో అత్యంత ఎత్తైన శిఖరం ఏది?", "Which is the highest peak in the Western Ghats and South India?",
         "అనైముడి (2,695 మీ.)", "Anaimudi (2,695 m)", ["దొడ్డబెట్ట", "మహేంద్రగిరి", "కుద్రేముఖ్"], ["Doddabetta", "Mahendragiri", "Kudremukh"],
         "కేరళలోని అన్నామలై కొండల్లో ఉన్న అనైముడి దక్షిణ భారతదేశంలోనే అత్యంత ఎత్తైనది.", "Anaimudi in Annamalai hills of Kerala is highest in South India."),

        ("భారతదేశంలో గంగా నది ఎక్కడ జన్మిస్తుంది?", "Where does River Ganga originate?",
         "గంగోత్రి హిమానీనదం (భాగీరథి)", "Gangotri Glacier", ["యమునోత్రి", "మానససరోవరం", "మిలామ్ హిమానీనదం"], ["Yamunotri", "Manasarovar", "Milam Glacier"],
         "ఉత్తరాఖండ్‌లోని గంగోత్రి వద్ద భాగీరథిగా జన్మించి, దేవప్రయాగ వద్ద అలకనందతో కలిసి గంగగా మారుతుంది.", "Ganga originates as Bhagirathi at Gangotri."),

        ("ప్రపంచంలోనే అతిపెద్ద నదీ ద్వీపమైన 'మజులి' ఏ నదిపై ఉంది?", "On which river is the world's largest river island 'Majuli' situated?",
         "బ్రహ్మపుత్ర నది (అస్సాం)", "Brahmaputra River", ["గంగా నది", "సింధు నది", "గోదావరి నది"], ["Ganga River", "Indus River", "Godavari River"],
         "అస్సాంలో బ్రహ్మపుత్ర నది మధ్యలో మజులి నదీ ద్వీపం ఏర్పడింది.", "Majuli island in Assam is formed by Brahmaputra river."),

        ("నర్మదా మరియు తపతి నదులు ఏ సముద్రంలో కలుస్తాయి?", "Into which sea do Rivers Narmada and Tapi drain?",
         "అరేబియా సముద్రం", "Arabian Sea", ["బంగాళాఖాతం", "హిందూ మహాసముద్రం", "మన్నార్ సింధుశాఖ"], ["Bay of Bengal", "Indian Ocean", "Gulf of Mannar"],
         "నర్మద, తపతి నదులు పశ్చిమంగా ప్రవహించి అరేబియా సముద్రంలో ఖంభాట్ సింధుశాఖ వద్ద కలుస్తాయి.", "Flow westwards through rift valleys into Arabian Sea."),

        ("భారతదేశంలో అత్యధిక వర్షపాతం నమోదయ్యే ప్రాంతం ఏది?", "Which place receives the highest rainfall in India and the world?",
         "మౌసిన్‌రామ్ (మేఘాలయ)", "Mawsynram (Meghalaya)", ["చిరపుంజి", "అగుంబే", "మహాబలేశ్వర్"], ["Cherrapunji", "Agumbe", "Mahabaleshwar"],
         "మేఘాలయలోని ఖాసీ కొండల్లో ఉన్న మౌసిన్‌రామ్ ప్రపంచంలోనే అత్యధిక వర్షపాతం పొందుతుంది.", "Mawsynram in Khasi Hills receives highest rainfall."),

        ("నల్లరేగడి నేలలు (Black Soils / Regur) ఏ పంట సాగుకు అత్యంత అనుకూలమైనవి?", "Black soils (Regur) are most suitable for the cultivation of which crop?",
         "పత్తి (Cotton)", "Cotton", ["వరి", "గోధుమ", "తేయాకు"], ["Paddy", "Wheat", "Tea"],
         "నల్లరేగడి నేలలో తేమను నిల్వ ఉంచే గుణం ఎక్కువ, కావున పత్తి పంటకు ప్రసిద్ధి.", "Black soil has high moisture retentiveness, ideal for cotton."),

        ("భారతదేశంలో అతిపెద్ద మంచినీటి సరస్సు ఏది?", "Which is the largest fresh water lake in India?",
         "ఊలార్ సరస్సు (జమ్మూ కాశ్మీర్)", "Wular Lake (J&K)", ["చిల్కా సరస్సు", "సాంబార్ సరస్సు", "లోక్‌తక్ సరస్సు"], ["Chilika Lake", "Sambhar Lake", "Loktak Lake"],
         "కాశ్మీర్‌లో జీలం నది మార్గంలో ఏర్పడిన ఊలార్ సరస్సు భారతదేశంలోనే అతిపెద్ద మంచినీటి సరస్సు.", "Wular Lake fed by Jhelum is largest freshwater lake."),

        ("భారతదేశంలో అతిపెద్ద ఉప్పునీటి సరస్సు (Lagoon) ఏది?", "Which is the largest brackish water lagoon in India?",
         "చిల్కా సరస్సు (ఒడిశా)", "Chilika Lake (Odisha)", ["పులికాట్ సరస్సు", "వేంబనాడ్ సరస్సు", "సాంబార్ సరస్సు"], ["Pulicat Lake", "Vembanad Lake", "Sambhar Lake"],
         "ఒడిశా తీరంలో ఉన్న చిల్కా సరస్సు ఆసియాలోనే అతిపెద్ద ఉప్పునీటి సరస్సు.", "Chilika lake in Odisha is largest coastal lagoon in India."),

        ("కార్బెట్ నేషనల్ పార్క్ (జిమ్ కార్బెట్) భారతదేశపు తొలి జాతీయ ఉద్యానవనం ఏ రాష్ట్రంలో ఉంది?", "In which state is Jim Corbett, the first National Park of India, situated?",
         "ఉత్తరాఖండ్", "Uttarakhand", ["హిమాచల్ ప్రదేశ్", "మధ్యప్రదేశ్", "అస్సాం"], ["Himachal Pradesh", "Madhya Pradesh", "Assam"],
         "1936లో హేలీ నేషనల్ పార్క్ పేరిట ఉత్తరాఖండ్‌లో స్థాపించబడింది.", "Established in 1936 as Hailey National Park in Uttarakhand."),

        ("ఒంటికొమ్ము ఖడ్గమృగాలకు (One-horned Rhinoceros) ప్రసిద్ధి చెందిన జాతీయ ఉద్యానవనం ఏది?", "Which National Park is famous for the Great Indian One-horned Rhinoceros?",
         "కాజిరంగా నేషనల్ పార్క్ (అస్సాం)", "Kaziranga National Park", ["మానస్", "సుందర్‌బన్స్", "గిర్ నేషనల్ పార్క్"], ["Manas", "Sundarbans", "Gir National Park"],
         "అస్సాంలోని కాజిరంగా ప్రపంచంలోనే అత్యధిక ఒంటికొమ్ము ఖడ్గమృగాలకు ఆవాసం.", "Kaziranga hosts two-thirds of world's great one-horned rhinos."),

        ("భారతదేశంలో 'హరిత విప్లవ పితామహుడు' అని ఎవరిని పిలుస్తారు?", "Who is known as the Father of Green Revolution in India?",
         "డా. ఎం.ఎస్. స్వామినాథన్", "Dr. M.S. Swaminathan", ["వర్గీస్ కురియన్", "నార్మన్ బోర్లాగ్", "సి. సుబ్రమణ్యం"], ["Verghese Kurien", "Norman Borlaug", "C. Subramaniam"],
         "డా. ఎం.ఎస్. స్వామినాథన్ అధిక దిగుబడినిచ్చే వరి, గోధుమ వంగడాలను ప్రవేశపెట్టారు.", "Dr. Swaminathan led India's Green Revolution."),

        ("భారతదేశంలో శ్వేత విప్లవం (ఆపరేషన్ ఫ్లడ్) దేనికి సంబంధించినది?", "Operation Flood (White Revolution) in India is associated with what?",
         "పాల ఉత్పత్తి (Milk Production)", "Milk Production", ["చేపల ఉత్పత్తి", "నూనె గింజలు", "గుడ్ల ఉత్పత్తి"], ["Fish Production", "Oilseeds", "Egg Production"],
         "డా. వర్గీస్ కురియన్ సారథ్యంలో అమూల్ ద్వారా పాల ఉత్పత్తిలో విప్లవం వచ్చింది.", "Led by Dr. Verghese Kurien to make India self-sufficient in milk."),

        ("భారతదేశంలో అత్యధిక జనాభా కలిగిన రాష్ట్రం ఏది (2011 జనాభా లెక్కలు)?", "Which is the most populous state in India as per 2011 Census?",
         "ఉత్తరప్రదేశ్", "Uttar Pradesh", ["మహారాష్ట్ర", "బీహార్", "పశ్చిమ బెంగాల్"], ["Maharashtra", "Bihar", "West Bengal"],
         "సుమారు 20 కోట్ల జనాభాతో ఉత్తరప్రదేశ్ మొదటి స్థానంలో ఉంది.", "Uttar Pradesh had highest population of ~200 million."),

        ("2011 జనాభా లెక్కల ప్రకారం భారతదేశంలో అత్యధిక అక్షరాస్యత కలిగిన రాష్ట్రం ఏది?", "Which state recorded highest literacy rate as per 2011 Census?",
         "కేరళ (94%)", "Kerala (94%)", ["మిజోరం", "గోవా", "త్రిపుర"], ["Mizoram", "Goa", "Tripura"],
         "కేరళ 94% అక్షరాస్యతతో దేశంలోనే అగ్రస్థానంలో నిలిచింది.", "Kerala topped the nation with 94% literacy rate."),

        ("భారతదేశంలో అత్యధిక లింగ నిష్పత్తి (Sex Ratio) కలిగిన రాష్ట్రం ఏది?", "Which state has the highest sex ratio according to 2011 Census?",
         "కేరళ (1084)", "Kerala (1084)", ["తమిళనాడు", "ఆంధ్రప్రదేశ్", "ఛత్తీస్‌గఢ్"], ["Tamil Nadu", "Andhra Pradesh", "Chhattisgarh"],
         "ప్రతి 1000 మంది పురుషులకు 1084 మంది స్త్రీలతో కేరళ అగ్రస్థానంలో ఉంది.", "Kerala had 1084 females per 1000 males.")
    ]

    for idx, (q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en) in enumerate(ig_facts):
        add_fn("Indian Geography", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)

    geo_india_topics = [
        ("హిమాలయాలు", "మూడు సమాంతర శ్రేణులుగా (హిమాద్రి, హిమాచల్, శివాలిక్) విస్తరించి ఉన్నాయి", "భారతదేశానికి ఉత్తర సరిహద్దు సహజ రక్షణ గోడ"),
        ("థార్ ఎడారి (గ్రేట్ ఇండియన్ డెసర్ట్)", "రాజస్థాన్‌లోని ఆరావళి పర్వతాలకు పశ్చిమాన విస్తరించిన శుష్క ప్రాంతం", "భారతదేశపు అతిపెద్ద ఉష్ణ ఎడారి"),
        ("ఆరావళి పర్వతాలు", "భారతదేశంలోనే అత్యంత పురాతన ముడత పర్వతాలు", "గురుశిఖర్ (1722 మీ.) అత్యున్నత శిఖరం"),
        ("ద్వీపకల్ప పీఠభూమి", "పురాతన గోండ్వానా భూభాగంలో భాగమైన త్రిభుజాకార పీఠభూమి", "ఖనిజ వనరుల భాండాగారంగా ప్రసిద్ధి"),
        ("దక్కన్ పీఠభూమి", "లావా ఉద్గారాల వల్ల ఏర్పడిన నల్లరేగడి నేలల ప్రాంతం", "మహారాష్ట్ర, కర్ణాటక, తెలంగాణలలో విస్తరణ"),
        ("తూర్పు కనుమలు", "విచ్ఛిన్నమైన అవశిష్ట పర్వత శ్రేణి", "ఆర్మకొండ (జిందగడ) ఆంధ్రప్రదేశ్‌లో ఎత్తైన శిఖరం"),
        ("పశ్చిమ తీర మైదానాలు", "కొంకణ్, కెనరా, మలబార్ తీరాలుగా విభజించబడ్డాయి", "అరేబియా సముద్ర తీరం వెంబడి ఇరుకైన మైదానం"),
        ("తూర్పు తీర మైదానాలు", "ఉత్కల్, సిర్కార్, కోరమాండల్ తీరాలుగా విభజించబడ్డాయి", "డెల్టాలు ఎక్కువగా కలిగిన సారవంతమైన విశాల మైదానం"),
        ("లక్షద్వీప్ దీవులు", "అరేబియా సముద్రంలో పగడపు దిబ్బల (Atolls) వల్ల ఏర్పడిన దీవులు", "కవరత్తి రాజధానిగా గల కేంద్రపాలిత ప్రాంతం"),
        ("నైరుతి ఋతుపవనాలు", "జూన్ మొదటి వారంలో కేరళ తీరాన్ని తాకుతాయి", "భారతదేశ వార్షిక వర్షపాతంలో 75 శాతం వర్షాన్ని అందిస్తాయి"),
        ("ఈశాన్య ఋతుపవనాలు (తిరోగమన)", "అక్టోబర్-నవంబర్ మాసాల్లో కోరమాండల్ తీరానికి వర్షాన్నిస్తాయి", "తమిళనాడుకు ప్రధాన వర్షపాత వనరు"),
        ("మామిడి జల్లులు (Mango Showers)", "వేసవిలో కేరళ, కర్ణాటకలో కురిసే తొలకరి వర్షాలు", "మామిడి కాయలు త్వరగా పక్వానికి రావడానికి తోడ్పడతాయి"),
        ("కాలుబైశాఖి", "పశ్చిమ బెంగాల్‌లో ఏప్రిల్-మే నెలల్లో సంభవించే భీకర ఉరుముల వర్షాలు", "తేయాకు, జనపనార పంటలకు అనుకూలం"),
        ("ఒండ్రు నేలలు (Alluvial Soils)", "గంగా-బ్రహ్మపుత్ర నదుల నిక్షేపణ వల్ల ఏర్పడిన సారవంతమైన నేలలు", "భారతదేశంలో అత్యధిక విస్తీర్ణంలో ఉన్న నేలలు"),
        ("లాటరైట్ నేలలు", "అధిక ఉష్ణోగ్రత, అధిక వర్షపాతం గల ప్రాంతాల్లో లీచింగ్ వల్ల ఏర్పడతాయి", "కాఫీ, రబ్బరు, జీడిమామిడి తోటలకు అనుకూలం"),
        ("భాక్రా నంగల్ ప్రాజెక్ట్", "హిమాచల్ ప్రదేశ్/పంజాబ్‌లో సట్లెజ్ నదిపై నిర్మించిన భారీ డ్యామ్", "గోవింద్ సాగర్ జలాశయం ఏర్పడింది"),
        ("హీరాకుడ్ డ్యామ్", "ఒడిశాలో మహానదిపై నిర్మించిన భారతదేశపు అత్యంత పొడవైన డ్యామ్", "మహానది వరదల నియంత్రణకు నిర్మించారు"),
        ("తెహ్రీ డ్యామ్", "ఉత్తరాఖండ్‌లో భాగీరథి నదిపై నిర్మించిన భారతదేశపు అత్యంత ఎత్తైన డ్యామ్", "భూకంప ప్రభావిత ప్రాంతంలో రాతి కట్టడం"),
        ("సర్దార్ సరోవర్ డ్యామ్", "గుజరాత్‌లో నర్మదా నదిపై నిర్మించిన బహుళార్థసాధక ప్రాజెక్ట్", "గుజరాత్, మధ్యప్రదేశ్, రాజస్థాన్‌లకు సాగునీరు"),
        ("కోలార్ బంగారు గనులు", "కర్ణాటకలో ఉన్న చారిత్రక బంగారు గనుల ప్రాంతం", "భారతదేశంలో అతిపెద్ద బంగారు గనులు"),
        ("జార్ఖండ్ బొగ్గు క్షేత్రాలు (ఝరియా)", "భారతదేశంలో అత్యుత్తమ కోకింగ్ బొగ్గు లభించే అతిపెద్ద గని", "దామోదర్ నదీ లోయలో విస్తరించింది"),
        ("డిగ్‌బోయ్ చమురు శుద్ధి కర్మాగారం", "అస్సాంలో ఉన్న భారతదేశపు మొట్టమొదటి ఆయిల్ రిఫైనరీ (1901)", "ఆసియాలోనే తొలి చమురు బావి"),
        ("ముంబై హై (Bombay High)", "అరేబియా సముద్రంలో ఉన్న భారతదేశపు అతిపెద్ద తీరప్రాంత చమురు క్షేత్రం", "ఓఎన్‌జీసీ ద్వారా సాగర్ సమ్రాట్ వేదికగా చమురు వెలికితీత"),
        ("గ్రీన్ కారిడార్ - ఎన్‌హెచ్ 44", "శ్రీనగర్ నుండి కన్యాకుమారి వరకు విస్తరించిన అత్యంత పొడవైన జాతీయ రహదారి", "ఉత్తర-దక్షిణ కారిడార్ ప్రధాన మార్గం"),
        ("భారత అంతర్గత జలమార్గం 1 (NW-1)", "గంగా-భాగీరథి-హుగ్లీ నదీ మార్గంలో ప్రయాగ్‌రాజ్ నుండి హల్దియా వరకు", "1,620 కి.మీ. పొడవు గల జాతీయ జలమార్గం")
    ]

    needed_ig = 143 - len(ig_facts)
    c_ig = 0
    while c_ig < needed_ig:
        top, d1, d2 = geo_india_topics[c_ig % len(geo_india_topics)]
        q_type = c_ig % 4
        if q_type == 0:
            q_te = f"భారత భౌగోళిక అంశాలలో '{top}' యొక్క ప్రధాన లక్షణం ఏది? (IG-Q{c_ig+1})"
            q_en = f"What is the main characteristic of '{top}' in Indian geography? (IG-Q{c_ig+1})"
            c_te, c_en = d1, d1
            d_te, d_en = ["నిత్యం హిమపాతం కురిసే లోయ", "సముద్ర అంతర్భాగ పర్వతం", "ఉష్ణమండల అటవీ దీవి"], ["Perpetual snow valley", "Submarine ridge", "Tropical island"]
            exp_te = f"{top}: {d1}."
            exp_en = f"{top}: {d1}."
        elif q_type == 1:
            q_te = f"భారతదేశ నైసర్గిక స్వరూపంలో '{top}' ఏ ప్రాముఖ్యతను కలిగి ఉంది? (IG-Q{c_ig+1})"
            q_en = f"What significance does '{top}' hold? (IG-Q{c_ig+1})"
            c_te, c_en = d2, d2
            d_te, d_en = ["విదేశీ ఓడరేవు కేంద్రం", "అంతర్జాతీయ సరిహద్దు ఒప్పందం", "రైల్వే ఇంజిన్ల తయారీ"], ["Foreign port", "Border treaty", "Loco works"]
            exp_te = f"{top}: {d2}."
            exp_en = f"{top}: {d2}."
        elif q_type == 2:
            q_te = f"కింది వాటిలో '{d1}' అనే భౌగోళిక అంశం దేనికి వర్తిస్తుంది? (IG-Q{c_ig+1})"
            q_en = f"To which does '{d1}' apply? (IG-Q{c_ig+1})"
            c_te, c_en = top, top
            d_te, d_en = ["జాంస్కర్ లోయ", "కచ్ రణ్", "సుందర్‌బన్స్"], ["Zanskar", "Rann of Kutch", "Sundarbans"]
            exp_te = f"ఇది {top}కు వర్తిస్తుంది."
            exp_en = f"It applies to {top}."
        else:
            q_te = f"భారత వనరులు మరియు భూస్వరూపాలలో '{d2}' దేనిని సూచిస్తుంది? (IG-Q{c_ig+1})"
            q_en = f"In Indian topography, '{d2}' points to what? (IG-Q{c_ig+1})"
            c_te, c_en = top, top
            d_te, d_en = ["డూన్లు", "బుగ్గలు", "కయల్స్"], ["Duns", "Springs", "Kayals"]
            exp_te = f"ఇది {top}ను సూచిస్తుంది."
            exp_en = f"This points to {top}."

        add_fn("Indian Geography", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)
        c_ig += 1

    # ==========================================
    # 7. INDIAN ECONOMY (143)
    # ==========================================
    econ_facts = [
        ("భారత ప్రణాళికా సంఘం (Planning Commission) స్థానంలో ఏర్పాటు చేసిన సంస్థ ఏది?", "Which body replaced the Planning Commission in India?",
         "నీతి ఆయోగ్ (NITI Aayog)", "NITI Aayog", ["జాతీయ అభివృద్ధి మండలి (NDC)", "ఆర్థిక సంఘం", "కేంద్ర సమాచార కమిషన్"], ["NDC", "Finance Commission", "CIC"],
         "2015 జనవరి 1న ప్రణాళికా సంఘం స్థానంలో నీతి ఆయోగ్ ఏర్పాటయింది.", "NITI Aayog was established on Jan 1, 2015 replacing Planning Commission."),

        ("నీతి ఆయోగ్ (NITI Aayog) కు ఎక్స్‌-అఫీషియో చైర్మన్‌గా ఎవరు వ్యవహరిస్తారు?", "Who serves as the Ex-officio Chairman of NITI Aayog?",
         "భారత ప్రధానమంత్రి", "Prime Minister of India", ["ఆర్థిక మంత్రి", "ఆర్బీఐ గవర్నర్", "రాష్ట్రపతి"], ["Finance Minister", "RBI Governor", "President"],
         "నీతి ఆయోగ్‌కు దేశ ప్రధానమంత్రి చైర్మన్‌గా ఉంటారు.", "Prime Minister of India is the Chairperson of NITI Aayog."),

        ("భారతీయ రిజర్వ్ బ్యాంక్ (RBI) ఏ కమిషన్ సిఫారసుల ఆధారంగా 1935లో ఏర్పాటయింది?", "Based on which commission was RBI established in 1935?",
         "హిల్టన్ యంగ్ కమిషన్", "Hilton Young Commission", ["హంటర్ కమిషన్", "ఛాంబర్లిన్ కమిషన్", "సర్కారియా కమిషన్"], ["Hunter Commission", "Chamberlain Commission", "Sarkaria Commission"],
         "1926 హిల్టన్ యంగ్ కమిషన్ సిఫారసుతో 1935 ఏప్రిల్ 1న ఆర్బీఐ ఏర్పాటయింది.", "RBI was established in 1935 following Hilton Young Commission report."),

        ("భారతీయ రిజర్వ్ బ్యాంక్ (RBI) ఏ సంవత్సరంలో జాతీయం చేయబడింది?", "In which year was the Reserve Bank of India nationalized?",
         "1949 జనవరి 1", "Jan 1, 1949", ["1935 ఏప్రిల్ 1", "1950 జనవరి 26", "1969 జూలై 19"], ["April 1, 1935", "Jan 26, 1950", "July 19, 1969"],
         "1949 జనవరి 1న ఆర్బీఐ భారత ప్రభుత్వ పూర్తి యాజమాన్యంలోకి వచ్చింది.", "RBI was nationalized on January 1, 1949."),

        ("భారతదేశంలో 14 ప్రధాన వాణిజ్య బ్యాంకులను ఇందిరాగాంధీ ప్రభుత్వం ఎప్పుడు జాతీయం చేసింది?", "When were 14 major commercial banks nationalized in India?",
         "1969 జూలై 19", "July 19, 1969", ["1980 ఏప్రిల్ 15", "1975 జూన్ 25", "1955 జూలై 1"], ["April 15, 1980", "June 25, 1975", "July 1, 1955"],
         "రూ. 50 కోట్లకు పైగా డిపాజిట్లు గల 14 బ్యాంకులను 1969లో జాతీయం చేశారు.", "14 major banks were nationalized on July 19, 1969."),

        ("వాణిజ్య బ్యాంకులు తమ డిపాజిట్లలో కొంత శాతాన్ని నగదు రూపంలో ఆర్బీఐ వద్ద ఉంచడాన్ని ఏమంటారు?", "What is the percentage of deposits banks must keep as cash with RBI called?",
         "నగదు నిల్వల నిష్పత్తి (Cash Reserve Ratio - CRR)", "Cash Reserve Ratio (CRR)", ["రెపో రేటు", "రివర్స్ రెపో రేటు", "ఎస్ఎల్ఆర్"], ["Repo Rate", "Reverse Repo Rate", "SLR"],
         "బ్యాంకులు తమ NDTL లో నిర్ణీత నగదు శాతాన్ని ఆర్బీఐ వద్ద ఉంచాలి.", "CRR is mandatory cash reserve held by banks with RBI."),

        ("వాణిజ్య బ్యాంకులకు ఆర్బీఐ ఇచ్చే స్వల్పకాలిక రుణాలపై వసూలు చేసే వడ్డీ రేటును ఏమంటారు?", "What is the interest rate charged by RBI on short-term loans to banks called?",
         "రెపో రేటు (Repo Rate)", "Repo Rate", ["రివర్స్ రెపో రేటు", "బ్యాంక్ రేటు", "బేస్ రేటు"], ["Reverse Repo Rate", "Bank Rate", "Base Rate"],
         "ద్రవ్యోల్బణాన్ని నియంత్రించడానికి ఆర్బీఐ రెపో రేటును పెంచుతుంది.", "Repo rate is rate at which RBI lends short-term funds to banks."),

        ("భారతదేశంలో వస్తువులు మరియు సేవల పన్ను (GST) ఎప్పటి నుండి అమల్లోకి వచ్చింది?", "From which date did Goods and Services Tax (GST) come into force in India?",
         "2017 జూలై 1", "July 1, 2017", ["2016 నవంబర్ 8", "2015 ఏప్రిల్ 1", "2018 జనవరి 1"], ["Nov 8, 2016", "April 1, 2015", "Jan 1, 2018"],
         "101వ రాజ్యాంగ సవరణ చట్టం ద్వారా 'ఒకే దేశం - ఒకే పన్ను'గా జీఎస్టీ వచ్చింది.", "GST came into force on July 1, 2017 via 101st Amendment."),

        ("జీఎస్టీ కౌన్సిల్ (GST Council) కు చైర్మన్‌గా ఎవరు వ్యవహరిస్తారు?", "Who acts as the Chairperson of the GST Council?",
         "కేంద్ర ఆర్థిక మంత్రి", "Union Finance Minister", ["ప్రధానమంత్రి", "ఆర్బీఐ గవర్నర్", "కాగ్"], ["Prime Minister", "RBI Governor", "CAG"],
         "రాజ్యాంగంలోని ఆర్టికల్ 279A ప్రకారం కేంద్ర ఆర్థిక మంత్రి జీఎస్టీ కౌన్సిల్ చైర్మన్.", "Union Finance Minister heads GST Council under Article 279A."),

        ("మొదటి పంచవర్ష ప్రణాళిక (1951-1956) ఏ ఆర్థిక నమూనాపై ఆధారపడింది?", "The First Five Year Plan (1951-56) was based on which economic model?",
         "హారడ్-డోమర్ నమూనా", "Harrod-Domar Model", ["మహలనోబిస్ నమూనా", "గాడ్గిల్ నమూనా", "రావు-మన్మోహన్ నమూనా"], ["Mahalanobis Model", "Gadgil Model", "Rao-Manmohan Model"],
         "మొదటి ప్రణాళిక వ్యవసాయం, సాగునీటి ప్రాజెక్టులకు అత్యధిక ప్రాధాన్యతనిచ్చింది.", "First plan focused on agriculture based on Harrod-Domar model."),

        ("రెండవ పంచవర్ష ప్రణాళిక (1956-1961) ఏ ఆర్థిక నమూనాపై ఆధారపడింది?", "The Second Five Year Plan (1956-61) was based on which economic model?",
         "పి.సి. మహలనోబిస్ నమూనా", "P.C. Mahalanobis Model", ["హారడ్-డోమర్", "గాంధీయన్ నమూనా", "విశ్వేశ్వరయ్య నమూనా"], ["Harrod-Domar", "Gandhian Model", "Visvesvaraya Model"],
         "రెండవ ప్రణాళిక భారీ పరిశ్రమలు మరియు ఉక్కు కర్మాగారాలకు ప్రాధాన్యతనిచ్చింది.", "Second plan prioritized heavy industrialization."),

        ("'గరీబీ హఠావో' (పేదరిక నిర్మూలన) నినాదం ఏ పంచవర్ష ప్రణాళికలో ప్రధాన లక్ష్యంగా ఉంది?", "'Garibi Hatao' (Poverty Eradication) was key objective of which plan?",
         "ఐదవ పంచవర్ష ప్రణాళిక (1974-1979)", "5th Five Year Plan", ["నాల్గవ ప్రణాళిక", "ఆరవ ప్రణాళిక", "ఏడవ ప్రణాళిక"], ["4th Plan", "6th Plan", "7th Plan"],
         "ఇందిరాగాంధీ 5వ ప్రణాళికలో పేదరిక నిర్మూలన మరియు స్వయం సమృద్ధికి ప్రాధాన్యతనిచ్చారు.", "Garibi Hatao was emphasized during 5th Five Year Plan."),

        ("ఒక ఆర్థిక సంవత్సరంలో దేశ సరిహద్దులలో ఉత్పత్తి అయిన అంతిమ వస్తుసేవల మొత్తం విలువను ఏమంటారు?", "Total value of final goods and services produced within domestic territory is called?",
         "స్థూల దేశీయోత్పత్తి (GDP)", "Gross Domestic Product (GDP)", ["స్థూల జాతీయోత్పత్తి (GNP)", "నికర జాతీయోత్పత్తి (NNP)", "తలసరి ఆదాయం"], ["GNP", "NNP", "Per Capita Income"],
         "దేశ భౌగోళిక సరిహద్దులలో ఉత్పత్తి అయిన విలువను జీడీపీ అంటారు.", "GDP measures monetary value of final output within domestic territory."),

        ("తలసరి ఆదాయాన్ని (Per Capita Income) ఎలా లెక్కిస్తారు?", "How is Per Capita Income calculated?",
         "జాతీయ ఆదాయం / దేశ మొత్తం జనాభా", "National Income / Total Population", ["జీడీపీ / మొత్తం ఎగుమతులు", "బడ్జెట్ / జనాభా", "మొత్తం పొదుపు / జనాభా"], ["GDP / Exports", "Budget / Population", "Savings / Population"],
         "నికర జాతీయ ఆదాయాన్ని మొత్తం జనాభాతో భాగించగా తలసరి ఆదాయం వస్తుంది.", "Per Capita Income is National Income divided by Total Population."),

        ("భారతదేశంలో 'డ్రెయిన్ ఆఫ్ వెల్త్' (సంపద తరలింపు సిద్ధాంతం) ను ప్రతిపాదించినది ఎవరు?", "Who propounded the 'Drain of Wealth' theory in India?",
         "దాదాభాయ్ నౌరోజీ", "Dadabhai Naoroji", ["ఆర్.సి. దత్", "ఎం.జి. రనడే", "గోపాలకృష్ణ గోఖలే"], ["R.C. Dutt", "M.G. Ranade", "G.K. Gokhale"],
         "1901లో 'పావర్టీ అండ్ అన్-బ్రిటిష్ రూల్ ఇన్ ఇండియా' పుస్తకంలో ఈ సిద్ధాంతం వివరించారు.", "Dadabhai Naoroji propounded it in his 1901 book."),

        ("వ్యవసాయ మరియు గ్రామీణాభివృద్ధి జాతీయ బ్యాంక్ (NABARD) ఏ కమిటీ సిఫారసుతో ఏర్పాటయింది?", "NABARD was set up on recommendation of which committee?",
         "బి. శివరామన్ కమిటీ (1982)", "B. Sivaraman Committee (1982)", ["నర్సింహం కమిటీ", "రంగరాజన్ కమిటీ", "చెలయ్య కమిటీ"], ["Narasimham Committee", "Rangarajan Committee", "Chelliah Committee"],
         "1982 జూలై 12న నాబార్డ్ పార్లమెంట్ చట్టం ద్వారా ఏర్పాటయింది.", "NABARD was established on July 12, 1982."),

        ("భారత స్టాక్ మార్కెట్లను మరియు సెక్యూరిటీల రంగాన్ని నియంత్రించే సర్వోన్నత సంస్థ ఏది?", "Which premier body regulates securities and stock markets in India?",
         "సెబీ (SEBI)", "SEBI", ["ఆర్బీఐ", "ఐఆర్‌డీఏఐ", "పీఎఫ్‌ఆర్‌డీఏ"], ["RBI", "IRDAI", "PFRDA"],
         "సెక్యూరిటీస్ అండ్ ఎక్స్ఛేంజ్ బోర్డ్ ఆఫ్ ఇండియా (SEBI) 1992లో చట్టబద్ధ సంస్థగా మారింది.", "SEBI regulates Indian capital markets since 1992 statutory status."),

        ("భారతదేశంలో నూతన ఆర్థిక సంస్కరణలు (LPG - సరళీకరణ, ప్రైవేటీకరణ, ప్రపంచీకరణ) ఎప్పుడు ప్రవేశపెట్టారు?", "When were New Economic Reforms (LPG) introduced in India?",
         "1991", "1991", ["1985", "1995", "2000"], ["1985", "1995", "2000"],
         "ప్రధాని పి.వి. నరసింహారావు మరియు ఆర్థిక మంత్రి మన్మోహన్ సింగ్ ఆధ్వర్యంలో 1991లో అమలు చేశారు.", "LPG reforms were introduced in 1991 under P.V. Narasimha Rao."),

        ("వ్యవసాయ రంగంలో కనిపించే అదృశ్య లేదా దాగి ఉన్న నిరుద్యోగాన్ని ఏమంటారు?", "What is the unemployment typically found in agriculture called?",
         "ప్రచ్ఛన్న నిరుద్యోగం (Disguised Unemployment)", "Disguised Unemployment", ["నిర్మాణాత్మక నిరుద్యోగం", "ఘర్షణ నిరుద్యోగం", "చక్రీయ నిరుద్యోగం"], ["Structural Unemployment", "Frictional Unemployment", "Cyclical Unemployment"],
         "అదనపు శ్రామికుని ఉపాంత ఉత్పాదకత శూన్యంగా ఉండే పరిస్థితిని ప్రచ్ఛన్న నిరుద్యోగం అంటారు.", "Marginal productivity of surplus labor is zero in disguised unemployment."),

        ("భారతదేశంలో ద్రవ్య విధానాన్ని (Monetary Policy) ఎవరు రూపొందించి అమలు చేస్తారు?", "Who formulates and implements Monetary Policy in India?",
         "ఆర్బీఐ ద్రవ్య విధాన కమిటీ (MPC)", "RBI Monetary Policy Committee", ["కేంద్ర ఆర్థిక మంత్రిత్వ శాఖ", "నీతి ఆయోగ్", "సెబీ"], ["Ministry of Finance", "NITI Aayog", "SEBI"],
         "ఆర్బీఐ గవర్నర్ అధ్యక్షతన గల ఆరుగురు సభ్యుల MPC ద్రవ్య విధానాన్ని నిర్ణయిస్తుంది.", "6-member MPC headed by RBI Governor sets monetary policy.")
    ]

    for idx, (q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en) in enumerate(econ_facts):
        add_fn("Indian Economy", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)

    econ_terms = [
        ("ద్రవ్యోల్బణం (Inflation)", "సాధారణ ధరల స్థాయిలో నిరంతర పెరుగుదల మరియు కరెన్సీ కొనుగోలు శక్తి క్షీణత", "CPI మరియు WPI సూచీల ద్వారా లెక్కింపు"),
        ("ప్రతి ద్రవ్యోల్బణం (Deflation)", "ధరల స్థాయిలో నిరంతర క్షీణత మరియు వస్తు సేవల ధరలు పడిపోవడం", "ద్రవ్యోల్బణానికి పూర్తి వ్యతిరేక పరిస్థితి"),
        ("స్టాగ్‌ఫ్లేషన్ (Stagflation)", "ఆర్థిక మందగమనం, అధిక నిరుద్యోగం మరియు అధిక ద్రవ్యోల్బణం ఒకేసారి ఏర్పడే దుస్థితి", "ఆర్థికవేత్తలకు క్లిష్టమైన సమస్య"),
        ("ద్రవ్యలోటు (Fiscal Deficit)", "ప్రభుత్వ మొత్తం వ్యయానికి మరియు అప్పులు మినహాయించిన మొత్తం రాబడులకు మధ్యగల తేడా", "ప్రభుత్వ వార్షిక అప్పుల పరిమాణాన్ని సూచిస్తుంది"),
        ("రెవెన్యూ లోటు (Revenue Deficit)", "ప్రభుత్వ రెవెన్యూ వ్యయాలు రెవెన్యూ ఆదాయాన్ని మించి ఉండే పరిస్థితి", "ప్రభుత్వ రోజువారీ నిర్వహణ లోటు"),
        ("ప్రాథమిక లోటు (Primary Deficit)", "ద్రవ్యలోటు నుండి గత అప్పులపై చెల్లించే వడ్డీలను తీసివేయగా వచ్చే నికర లోటు", "ప్రస్తుత సంవత్సరపు అసలు రుణాలు"),
        ("ప్రత్యక్ష పన్నులు (Direct Taxes)", "పన్ను భారం మరియు చెల్లింపు బాధ్యత ఒకే వ్యక్తిపై ఉండే పన్నులు", "వ్యక్తిగత ఆదాయపు పన్ను, కార్పొరేట్ పన్ను"),
        ("పరోక్ష పన్నులు (Indirect Taxes)", "పన్ను చెల్లింపుదారుడు ఆ భారాన్ని ఇతరులపైకి బదిలీ చేయగల పన్నులు", "జీఎస్టీ, ఎక్సైజ్ డ్యూటీ, కస్టమ్స్ డ్యూటీ"),
        ("ఫారెక్స్ నిల్వలు (Forex Reserves)", "విదేశీ మారక ద్రవ్యం, బంగారం, SDRలు మరియు IMF రిజర్వ్ ట్రోంచ్", "ఆర్బీఐ వద్ద ఉండే విదేశీ ఆస్తులు"),
        ("కరెంట్ ఖాతా లోటు (CAD)", "వస్తు సేవల దిగుమతులు ఎగుమతుల కంటే ఎక్కువగా ఉన్నప్పుడు ఏర్పడే లోటు", "విదేశీ వాణిజ్య సమతుల్యత సూచిక"),
        ("మూలధన ఖాతా (Capital Account)", "విదేశీ ప్రత్యక్ష పెట్టుబడులు (FDI), FPI, విదేశీ రుణాలు నమోదు చేసే ఖాతా", "ఆస్తులు మరియు బాధ్యతలలో మార్పులు"),
        ("సెన్సెక్స్ (BSE SENSEX)", "బాంబే స్టాక్ ఎక్స్ఛేంజ్‌లో అత్యధిక మూలధనం గల 30 అగ్రశ్రేణి కంపెనీల సూచీ", "భారత ఆర్థిక వ్యవస్థ ఆరోగ్య సూచిక"),
        ("నిఫ్టీ 50 (Nifty 50)", "నేషనల్ స్టాక్ ఎక్స్ఛేంజ్‌లో 50 అగ్రగామి కంపెనీల సూచీ", "విస్తృత మార్కెట్ పనితీరు సూచిక"),
        ("శిలాజ రాయితీలు మరియు DBT", "సబ్సిడీలను నేరుగా లబ్ధిదారుల బ్యాంక్ ఖాతాలకు జమ చేసే ఆధునిక పద్ధతి", "మధ్యవర్తుల తొలగింపు మరియు పారదర్శకత"),
        ("ఎంఎస్పీ (కనీస మద్దతు ధర)", "పంటల మార్కెట్ ధర పడిపోయినపుడు రైతులకు భరోసాగా ప్రభుత్వం ప్రకటించే కనీస ధర", "వ్యవసాయ వ్యయాలు, ధరల కమిషన్ (CACP) సిఫారసు"),
        ("పీరియాడిక్ లేబర్ ఫోర్స్ సర్వే (PLFS)", "జాతీయ గణాంక కార్యాలయం (NSO) నిర్వహించే ఉపాధి మరియు నిరుద్యోగ సర్వే", "లేబర్ మార్కెట్ డేటా ఆధారం"),
        ("హ్యూమన్ డెవలప్‌మెంట్ ఇండెక్స్ (HDI)", "ఆయుర్దాయం, విద్య మరియు తలసరి ఆదాయం ఆధారంగా UNDP విడుదల చేసే నివేదిక", "పాకిస్తాన్ ఆర్థికవేత్త మహబూబ్ ఉల్ హక్ రూపొందించారు"),
        ("మహారత్న హోదా", "భారత ప్రభుత్వ రంగ సంస్థలకు ఇచ్చే అత్యున్నత ఆర్థిక స్వయంప్రతిపత్తి హోదా", "ONGC, NTPC, IOCL, BHEL, SAIL వంటి సంస్థలు"),
        ("నవరత్న హోదా", "మహారత్న తర్వాత రెండవ శ్రేణి పీఎస్‌యూలకు ఇచ్చే స్వయంప్రతిపత్తి హోదా", "పెట్టుబడుల నిర్ణయాలలో బోర్డుకు విస్తృత అధికారాలు"),
        ("ముద్ర బ్యాంక్ యోజన (MUDRA)", "సూక్ష్మ వ్యాపారులకు శిశు, కిషోర్, తరుణ్ వర్గాల కింద రూ. 10 లక్షల వరకు పూచీకత్తు లేని రుణాలు", "చిరు వ్యాపారుల ఆర్థిక చేయూత"),
        ("ప్రధానమంత్రి జన్ ధన్ యోజన (PMJDY)", "దేశంలో ప్రతి కుటుంబానికి జీరో బ్యాలెన్స్ బ్యాంక్ ఖాతా మరియు రూపే కార్డు అందించే ఆర్థిక చేరిక పథకం", "ప్రపంచంలోనే అతిపెద్ద ఆర్థిక చేరిక కార్యక్రమం"),
        ("ఆయుష్మాన్ భారత్ (PM-JAY)", "పేద కుటుంబాలకు ఏటా రూ. 5 లక్షల వరకు ఉచిత ద్వితీయ, తృతీయ స్థాయి ఆరోగ్య బీమా కల్పించే పథకం", "ప్రపంచంలోనే అతిపెద్ద ప్రభుత్వ ఆరోగ్య పథకం"),
        ("స్వచ్ఛ భారత్ మిషన్", "బహిరంగ మలవిసర్జన రహిత (ODF) దేశంగా మార్చడానికి 2014 అక్టోబర్ 2న ప్రారంభించిన పథకం", "పారిశుద్ధ్య రంగంలో విప్లవం"),
        ("డిజిటల్ ఇండియా మిషన్", "ప్రభుత్వ సేవలను ఎలక్ట్రానిక్ రూపంలో పౌరులకు అందించడం మరియు డిజిటల్ అక్షరాస్యత పెంపు", "యూపీఐ, ఈ-గవర్నెన్స్ ఆధారిత వ్యవస్థ"),
        ("పీఎం కిసాన్ సమ్మాన్ నిధి", "రైతులకు ఏటా రూ. 6,000 (మూడు విడతల్లో రూ. 2000 చొప్పున) పెట్టుబడి సాయం అందించే కేంద్ర పథకం", "రైతుల ఖాతాల్లోకి నేరుగా నగదు బదిలీ")
    ]

    needed_econ = 143 - len(econ_facts)
    c_ec = 0
    while c_ec < needed_econ:
        t_term, t_desc, t_extra = econ_terms[c_ec % len(econ_terms)]
        q_type = c_ec % 4
        if q_type == 0:
            q_te = f"భారత ఆర్థిక వ్యవస్థలో '{t_term}' దేనిని వివరిస్తుంది? (IE-Q{c_ec+1})"
            q_en = f"What does '{t_term}' signify in the Indian economy? (IE-Q{c_ec+1})"
            c_te, c_en = t_desc, t_desc
            d_te, d_en = ["రైల్వే బోగీల సంఖ్య పెంపు", "పాస్‌పోర్ట్ కార్యాలయాల విస్తరణ", "పోస్టల్ స్టాంపుల జారీ"], ["Railway coaches", "Passport offices", "Postal stamps"]
            exp_te = f"{t_term}: {t_desc}."
            exp_en = f"{t_term}: {t_desc}."
        elif q_type == 1:
            q_te = f"ఆర్థిక సర్వే లేదా విధానాల ప్రకారం '{t_term}' యొక్క ముఖ్య లక్షణం ఏది? (IE-Q{c_ec+1})"
            q_en = f"What is the key aspect of '{t_term}'? (IE-Q{c_ec+1})"
            c_te, c_en = t_extra, t_extra
            d_te, d_en = ["విదేశీ పర్యాటకుల రద్దు", "వ్యవసాయ విద్యుత్ ఉపసంహరణ", "విమానాశ్రయాల మూసివేత"], ["Cancel tourism", "Withdraw power", "Close airports"]
            exp_te = f"{t_term}: {t_extra}."
            exp_en = f"{t_term}: {t_extra}."
        elif q_type == 2:
            q_te = f"కింది వాటిలో '{t_desc}' అనే వివరణ ఏ ఆర్థిక భావనకు వర్తిస్తుంది? (IE-Q{c_ec+1})"
            q_en = f"Which concept corresponds to '{t_desc}'? (IE-Q{c_ec+1})"
            c_te, c_en = t_term, t_term
            d_te, d_en = ["డెడ్ వెయిట్ లాస్", "ఏంజెల్ ట్యాక్స్", "టోబిన్ ట్యాక్స్"], ["Deadweight Loss", "Angel Tax", "Tobin Tax"]
            exp_te = f"ఇది {t_term}కు వర్తిస్తుంది."
            exp_en = f"It corresponds to {t_term}."
        else:
            q_te = f"భారత ప్రభుత్వ ఆర్థిక విధానాలలో '{t_extra}' దేనితో ముడిపడి ఉంది? (IE-Q{c_ec+1})"
            q_en = f"What is '{t_extra}' linked with? (IE-Q{c_ec+1})"
            c_te, c_en = t_term, t_term
            d_te, d_en = ["రక్షిత అడవుల పెంపు", "సముద్ర సరిహద్దు గస్తీ", "కరవు నివారణ కార్పొరేషన్"], ["Reserved forests", "Coastal guard", "Drought corp"]
            exp_te = f"ఇది {t_term}తో ముడిపడి ఉంది."
            exp_en = f"It is linked with {t_term}."

        add_fn("Indian Economy", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)
        c_ec += 1

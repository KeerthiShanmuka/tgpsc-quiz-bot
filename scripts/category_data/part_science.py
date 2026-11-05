"""
Part 3: Science Categories (572 Questions)
- General Science: 143
- Biology: 143
- Physics: 143
- Chemistry: 143
"""

def generate_part_science(add_fn):
    # ==========================================
    # 8. GENERAL SCIENCE (143)
    # ==========================================
    sci_facts = [
        ("భారత అంతరిక్ష పరిశోధనా సంస్థ (ISRO) ఏ సంవత్సరంలో స్థాపించబడింది?", "In which year was Indian Space Research Organisation (ISRO) established?",
         "1969 ఆగస్టు 15", "August 15, 1969", ["1962 అక్టోబర్ 2", "1972 జూన్ 1", "1958 జనవరి 26"], ["Oct 2, 1962", "June 1, 1972", "Jan 26, 1958"],
         "డా. విక్రమ్ సారాభాయ్ నేతృత్వంలో 1969 ఆగస్టు 15న ఇస్రో ఏర్పాటయింది.", "ISRO was founded on Aug 15, 1969 under Vikram Sarabhai."),

        ("భారత అంతరిక్ష పితామహుడు అని ఎవరిని పిలుస్తారు?", "Who is known as the Father of Indian Space Program?",
         "డా. విక్రమ్ సారాభాయ్", "Dr. Vikram Sarabhai", ["హోమీ జె. బాబా", "సతీష్ ధావన్", "ఎ.పి.జె. అబ్దుల్ కలాం"], ["Homi J. Bhabha", "Satish Dhawan", "A.P.J. Abdul Kalam"],
         "భారతదేశంలో అంతరిక్ష పరిశోధనలకు డా. విక్రమ్ సారాభాయ్ ఆద్యుడు.", "Dr. Vikram Sarabhai pioneered the Indian space program."),

        ("భారతదేశపు మొట్టమొదటి ఉపగ్రహం ఆర్యభట్ట ఎప్పుడు ప్రయోగించబడింది?", "When was Aryabhata, India's first satellite, launched?",
         "1975 ఏప్రిల్ 19", "April 19, 1975", ["1979 జూన్ 7", "1980 జూలై 18", "1971 ఆగస్టు 15"], ["June 7, 1979", "July 18, 1980", "Aug 15, 1971"],
         "సోవియట్ యూనియన్ కాస్మోస్-3M రాకెట్ ద్వారా ఆర్యభట్టను ప్రయోగించారు.", "Launched on April 19, 1975 using Soviet launch vehicle."),

        ("చంద్రయాన్-3 ల్యాండర్ విక్రమ్ చంద్రుడి దక్షిణ ధ్రువంపై దిగిన ప్రదేశాన్ని ఏమని నామకరణం చేశారు?", "What is the landing site of Chandrayaan-3 lander named?",
         "శివశక్తి పాయింట్ (Shiv Shakti Point)", "Shiv Shakti Point", ["తిరంగా పాయింట్", "జవహర్ పాయింట్", "శక్తి స్థల్"], ["Tiranga Point", "Jawahar Point", "Shakti Sthal"],
         "2023 ఆగస్టు 23న చంద్రయాన్-3 ల్యాండర్ దిగిన ప్రదేశాన్ని ప్రధాని మోదీ 'శివశక్తి పాయింట్'గా ప్రకటించారు.", "Landing site was named Shiv Shakti Point by PM Modi."),

        ("భారతదేశంలో 'జాతీయ అంతరిక్ష దినోత్సవం' (National Space Day) గా ఏ తేదీని నిర్ణయించారు?", "Which date is celebrated as National Space Day in India?",
         "ఆగస్టు 23", "August 23", ["ఆగస్టు 15", "ఫిబ్రవరి 28", "మే 11"], ["August 15", "February 28", "May 11"],
         "చంద్రయాన్-3 విజయవంతంగా చంద్రుడిపై దిగిన ఆగస్టు 23ను జాతీయ అంతరిక్ష దినోత్సవంగా జరుపుతారు.", "August 23 marks soft landing of Chandrayaan-3."),

        ("సూర్యుడిపై పరిశోధనల కోసం ఇస్రో ప్రయోగించిన తొలి భారతీయ మిషన్ ఏది?", "Which is India's first solar space observatory mission launched by ISRO?",
         "ఆదిత్య-L1 (Aditya-L1)", "Aditya-L1", ["సూర్య-1", "భాస్కర", "హేలియోస్-ఇండియా"], ["Surya-1", "Bhaskara", "Helios-India"],
         "2023 సెప్టెంబర్ 2న PSLV-C57 ద్వారా ఆదిత్య-L1ను లాగ్రాంజ్ పాయింట్ 1 దిశగా ప్రయోగించారు.", "Aditya-L1 launched towards Sun-Earth Lagrange Point 1."),

        ("రక్షణ పరిశోధన మరియు అభివృద్ధి సంస్థ (DRDO) ఎప్పుడు స్థాపించబడింది?", "In which year was DRDO established?",
         "1958", "1958", ["1969", "1950", "1974"], ["1969", "1950", "1974"],
         "భారత రక్షణ రంగానికి అవసరమైన ఆయుధాలు, సాంకేతికత అభివృద్ధికి 1958లో డీఆర్డీఓ ఏర్పాటయింది.", "DRDO was formed in 1958 for defense technologies."),

        ("భారతదేశపు మిస్సైల్ మ్యాన్ (క్షిపణి పితామహుడు) అని ఎవరిని పిలుస్తారు?", "Who is famously known as the Missile Man of India?",
         "డా. ఎ.పి.జె. అబ్దుల్ కలాం", "Dr. A.P.J. Abdul Kalam", ["హోమీ బాబా", "రాజా రామన్న", "కస్తూరిరంగన్"], ["Homi Bhabha", "Raja Ramanna", "Kasturirangan"],
         "ఇంటిగ్రేటెడ్ గైడెడ్ మిస్సైల్ డెవలప్‌మెంట్ ప్రోగ్రామ్ (IGMDP) రూపకర్త కలాం.", "Dr. Kalam spearheaded the IGMDP missile project."),

        ("భారతదేశం మరియు రష్యా సంయుక్తంగా అభివృద్ధి చేసిన సూపర్ సోనిక్ క్రూయిజ్ క్షిపణి ఏది?", "Which supersonic cruise missile was jointly developed by India and Russia?",
         "బ్రహ్మోస్ (BrahMos)", "BrahMos", ["అగ్ని", "పృథ్వీ", "ఆకాశ్"], ["Agni", "Prithvi", "Akash"],
         "బ్రహ్మపుత్ర మరియు మోస్క్వా నదుల పేర్లతో బ్రహ్మోస్ క్షిపణి రూపొందించబడింది.", "Named after Brahmaputra and Moskva rivers."),

        ("భారత అణుశక్తి పితామహుడు (Father of Indian Nuclear Program) ఎవరు?", "Who is considered the Father of Indian Nuclear Program?",
         "డా. హోమీ జె. బాబా", "Dr. Homi J. Bhabha", ["విక్రమ్ సారాభాయ్", "సి.వి. రామన్", "మేఘనాథ్ సాహా"], ["Vikram Sarabhai", "C.V. Raman", "Meghnad Saha"],
         "భాభా అటామిక్ రీసెర్చ్ సెంటర్ (BARC) మరియు టాటా ఇన్స్టిట్యూట్ (TIFR) వ్యవస్థాపకుడు హోమీ బాబా.", "Dr. Bhabha laid foundation of atomic research in India."),

        ("భారతదేశం తన తొలి అణుపరీక్షను (స్మైలింగ్ బుద్ధ) ఎప్పుడు నిర్వహించింది?", "When did India conduct its first nuclear test (Smiling Buddha)?",
         "1974 మే 18 (పోఖ్రాన్)", "May 18, 1974", ["1998 మే 11", "1965 సెప్టెంబర్ 1", "1984 అక్టోబర్ 31"], ["May 11, 1998", "Sept 1, 1965", "Oct 31, 1984"],
         "రాజస్థాన్‌లోని పోఖ్రాన్‌లో ఇందిరాగాంధీ ప్రధానిగా ఉన్నప్పుడు ఈ పరీక్ష నిర్వహించారు.", "First nuclear test carried out at Pokhran in 1974."),

        ("భారతదేశపు తొలి సూపర్ కంప్యూటర్ 'పరం 8000'ను ఏ సంస్థ అభివృద్ధి చేసింది?", "Which organization developed India's first supercomputer PARAM 8000?",
         "సి-డాక్ పూణే (C-DAC)", "C-DAC Pune", ["ఇస్రో", "డీఆర్డీఓ", "ఐఐటీ బొంబాయి"], ["ISRO", "DRDO", "IIT Bombay"],
         "విజయ్ భట్కర్ నేతృత్వంలో సి-డాక్ 1991లో పరం 8000 సూపర్ కంప్యూటర్‌ను రూపొందించింది.", "Developed by C-DAC in 1991 under Vijay Bhatkar."),

        ("కంప్యూటర్ పితామహుడు అని ఎవరిని పిలుస్తారు?", "Who is universally known as the Father of Computer?",
         "చార్లెస్ బాబేజ్", "Charles Babbage", ["అలాన్ ట్యూరింగ్", "జాన్ వాన్ న్యూమన్", "టిమ్ బెర్నర్స్ లీ"], ["Alan Turing", "John von Neumann", "Tim Berners-Lee"],
         "డిఫరెన్స్ ఇంజిన్, అనలిటికల్ ఇంజిన్ రూపొందించిన చార్లెస్ బాబేజ్ కంప్యూటర్ పితామహుడు.", "Charles Babbage invented analytical engine."),

        ("వరల్డ్ వైడ్ వెబ్ (WWW) ను కనుగొన్న శాస్త్రవేత్త ఎవరు?", "Who invented the World Wide Web (WWW)?",
         "టిమ్ బెర్నర్స్ లీ", "Tim Berners-Lee", ["వింట్ సెర్ఫ్", "స్టీవ్ జాబ్స్", "బిల్ గేట్స్"], ["Vint Cerf", "Steve Jobs", "Bill Gates"],
         "1989లో సెర్న్ (CERN) లో పనిచేస్తూ టిమ్ బెర్నర్స్ లీ WWWను ఆవిష్కరించారు.", "Tim Berners-Lee invented WWW in 1989 at CERN."),

        ("ఆప్టికల్ ఫైబర్ కమ్యూనికేషన్ పితామహుడుగా కీర్తించబడిన భారతీయ-అమెరికన్ భౌతిక శాస్త్రవేత్త ఎవరు?", "Which Indian-American physicist is known as the Father of Fibre Optics?",
         "నరీందర్ సింగ్ కపానీ", "Narinder Singh Kapany", ["సి.వి. రామన్", "సుబ్రమణ్యం చంద్రశేఖర్", "హరగోవింద్ ఖురానా"], ["C.V. Raman", "S. Chandrasekhar", "Har Gobind Khorana"],
         "సంపూర్ణ అంతర పరావర్తనం ఆధారంగా ఆప్టికల్ ఫైబర్‌ను కపానీ అభివృద్ధి చేశారు.", "Narinder Singh Kapany pioneered fiber optic technology."),

        ("సౌర ఘటాలు (Solar Cells) కాంతి శక్తిని ఏ శక్తిగా మారుస్తాయి?", "Solar cells convert solar light energy into which form of energy?",
         "విద్యుత్ శక్తి (Electrical Energy)", "Electrical Energy", ["యాంత్రిక శక్తి", "రసాయన శక్తి", "ఉష్ణ శక్తి"], ["Mechanical Energy", "Chemical Energy", "Thermal Energy"],
         "ఫోటోవోల్టాయిక్ ప్రభావం ద్వారా కాంతి శక్తి నేరుగా విద్యుత్ శక్తిగా మారుతుంది.", "Solar cells convert light into electricity via photovoltaic effect."),

        ("బయోగ్యాస్ (గోబర్ గ్యాస్) లో ప్రధానంగా ఉండే వాయువు ఏది?", "Which gas is the primary constituent of Biogas (Gobar Gas)?",
         "మీథేన్ (CH4)", "Methane (CH4)", ["బ్యూటేన్", "ప్రొపేన్", "కార్బన్ మోనాక్సైడ్"], ["Butane", "Propane", "Carbon Monoxide"],
         "బయోగ్యాస్‌లో 55-70 శాతం మీథేన్, మిగిలినది కార్బన్ డయాక్సైడ్ ఉంటుంది.", "Methane constitutes 55-70% of biogas."),

        ("భారతదేశంలో 'జాతీయ సైన్స్ దినోత్సవం' ఏ తేదీన జరుపుకుంటారు?", "On which date is National Science Day celebrated in India?",
         "ఫిబ్రవరి 28", "February 28", ["జనవరి 12", "మే 11", "డిసెంబర్ 22"], ["January 12", "May 11", "December 22"],
         "సర్ సి.వి. రామన్ 'రామన్ ఎఫెక్ట్'ను కనుగొన్న రోజు (1928 ఫిబ్రవరి 28) జ్ఞాపకార్థం జరుపుతారు.", "Commemorates the discovery of Raman Effect on Feb 28, 1928."),

        ("రామన్ ఎఫెక్ట్ ఆవిష్కరణకు సి.వి. రామన్‌కు ఏ సంవత్సరంలో నోబెల్ బహుమతి లభించింది?", "In which year did C.V. Raman receive Nobel Prize in Physics?",
         "1930", "1930", ["1913", "1968", "1983"], ["1913", "1968", "1983"],
         "కాంతి పరిక్షేపణంపై పరిశోధనలకు 1930లో భౌతికశాస్త్రంలో రామన్ నోబెల్ గెలుచుకున్నారు.", "Awarded 1930 Nobel Prize for Raman scattering of light."),

        ("భారతదేశంలో 'జాతీయ సాంకేతిక దినోత్సవం' (National Technology Day) ఏ తేదీన జరుపుకుంటారు?", "Which date is observed as National Technology Day in India?",
         "మే 11", "May 11", ["మే 1", "ఫిబ్రవరి 28", "ఆగస్టు 15"], ["May 1", "February 28", "August 15"],
         "1998 మే 11న పోఖ్రాన్-2 అణుపరీక్షల విజయానికి గుర్తుగా ఈ దినోత్సవం జరుపుతారు.", "Marks the success of Pokhran-II tests on May 11, 1998.")
    ]

    for idx, (q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en) in enumerate(sci_facts):
        add_fn("General Science", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)

    tech_topics = [
        ("కృత్రిమ మేధస్సు (AI)", "మానవ ఆలోచనా సరళిని కంప్యూటర్లలో అనుకరించే ఆధునిక సాంకేతిక పరిజ్ఞానం", "యంత్ర అభ్యాసం మరియు నాడీ నెట్‌వర్క్‌ల కలయిక"),
        ("మెషిన్ లెర్నింగ్ (ML)", "డేటా ఆధారంగా ప్రోగ్రామింగ్ లేకుండానే కంప్యూటర్లు స్వయంగా నేర్చుకునే ప్రక్రియ", "AI రంగంలో కీలక ఉప విభాగం"),
        ("క్లౌడ్ కంప్యూటింగ్", "ఇంటర్నెట్ ద్వారా సర్వర్లు, నిల్వ మరియు డేటాబేస్ సేవలను అవసరానికి అనుగుణంగా పొందడం", "AWS, Azure, Google Cloud ప్రధాన వేదికలు"),
        ("బ్లాక్‌చెయిన్ టెక్నాలజీ", "వికేంద్రీకృత, పారదర్శక మరియు మార్చలేని డిజిటల్ లెడ్జర్ వ్యవస్థ", "క్రిప్టోకరెన్సీలు మరియు సురక్షిత లావాదేవీలకు ఆధారం"),
        ("ఇంటర్నెట్ ఆఫ్ థింగ్స్ (IoT)", "ఎలక్ట్రానిక్ పరికరాలు ఇంటర్నెట్ ద్వారా పరస్పరం సమాచారాన్ని మార్పిడి చేసుకునే వ్యవస్థ", "స్మార్ట్ హోమ్స్ మరియు స్మార్ట్ సిటీలు"),
        ("సైబర్ సెక్యూరిటీ", "కంప్యూటర్ వ్యవస్థలు, నెట్‌వర్క్‌లు మరియు డేటాను డిజిటల్ దాడుల నుండి రక్షించే ప్రక్రియ", "ఫైర్‌వాల్స్ మరియు ఎన్‌క్రిప్షన్ ప్రధాన సాధనాలు"),
        ("ఫిషింగ్ (Phishing)", "నకిలీ ఈమెయిళ్ళు, మెసేజ్‌ల ద్వారా వ్యక్తిగత పాస్‌వర్డ్‌లు, బ్యాంక్ వివరాలు దొంగిలించే సైబర్ మోసం", "సోషల్ ఇంజనీరింగ్ దాడి రూపం"),
        ("రాన్సమ్‌వేర్ (Ransomware)", "యూజర్ల ఫైళ్ళను ఎన్‌క్రిప్ట్ చేసి డబ్బు డిమాండ్ చేసే అత్యంత ప్రమాదకరమైన మాల్‌వేర్", "వాన్నాక్రై, లాక్‌బిట్ వంటి ప్రమాదాలు"),
        ("5G నెట్‌వర్క్", "అధిక వేగం, అతి తక్కువ లేటెన్సీ మరియు భారీ కనెక్టివిటీ కలిగిన ఐదవ తరం సెల్యులార్ సాంకేతికత", "ఆటోమేషన్ మరియు రోబోటిక్స్‌కు వెన్నెముక"),
        ("జీపీఎస్ (GPS)", "అమెరికా రక్షణ శాఖ అభివృద్ధి చేసిన గ్లోబల్ పొజిషనింగ్ శాటిలైట్ వ్యవస్థ", "భౌగోళిక స్థానాన్ని ఖచ్చితంగా నిర్ణయిస్తుంది"),
        ("నావిక్ (NavIC)", "భారతదేశం స్వదేశీ పరిజ్ఞానంతో రూపొందించిన ప్రాంతీయ ఉపగ్రహ నావిగేషన్ వ్యవస్థ", "ఇస్రో అభివృద్ధి చేసిన 7 ఉపగ్రహాల సమూహం"),
        ("గగన్‌యాన్ ప్రాజెక్ట్", "భారత వ్యోమగాములను అంతరిక్షంలోకి పంపి సురక్షితంగా భూమికి తెచ్చే ప్రతిష్టాత్మక ఇస్రో మిషన్", "భారత తొలి మానవసహిత అంతరిక్ష యాత్ర"),
        ("నిసార్ (NISAR)", "నాసా మరియు ఇస్రో సంయుక్తంగా భూమి ఉపరితల మార్పులను పర్యవేక్షించే రాడార్ శాటిలైట్ మిషన్", "డ్యూయల్ ఫ్రీక్వెన్సీ సింథటిక్ ఎపర్చర్ రాడార్"),
        ("లేజర్లు (LASER)", "ఉద్గారిత వికిరణ ప్రేరణ ద్వారా కాంతి ప్రవర్ధనం చెందే ఏకవర్ణ కాంతి పుంజం", "వైద్య శస్త్రచికిత్సలు మరియు పరిశ్రమల్లో విస్తృత వినియోగం"),
        ("రహస్య ఎన్‌క్రిప్షన్ (AES)", "డేటాను ఇతరులు చదవలేకుండా కోడ్ భాషలోకి మార్చే అధునాతన భద్రతా ప్రామాణికం", "డిజిటల్ బ్యాంకింగ్ మరియు సైనిక సమాచార రక్షణ"),
        ("నానోటెక్నాలజీ", "1 నుండి 100 నానోమీటర్ల పరమాణు స్థాయిలో పదార్థాలను నియంత్రించే సాంకేతికత", "ఔషధాల రవాణా మరియు తేలికపాటి మిశ్రమ లోహాల తయారీ"),
        ("3D ప్రింటింగ్ (సంకలిత తయారీ)", "డిజిటల్ నమూనా ఆధారంగా పొరల రూపంలో భౌతిక వస్తువులను తయారు చేసే విధానం", "వైద్య అవయవాలు, రాకెట్ ఇంజిన్ విడిభాగాలు"),
        ("లిథియం-అయాన్ బ్యాటరీలు", "ఎలక్ట్రిక్ వాహనాలు మరియు స్మార్ట్‌ఫోన్లలో విస్తృతంగా వాడే పునర్వినియోగ బ్యాటరీలు", "జాన్ బి. గుడ్‌ఎనఫ్‌కు నోబెల్ బహుమతి లభించింది"),
        ("హైడ్రోజన్ ఇంధన ఘటం (Fuel Cell)", "హైడ్రోజన్ మరియు ఆక్సిజన్ కలయికతో కేవలం నీటిని మాత్రమే ఉప ఉత్పత్తిగా విడుదల చేస్తూ విద్యుత్‌ను ఉత్పత్తి చేస్తుంది", "కాలుష్య రహిత భవిష్యత్ హరిత ఇంధనం"),
        ("సూపర్ కండక్టివిటీ (అతివాహకత)", "అతి తక్కువ ఉష్ణోగ్రతల వద్ద విద్యుత్ నిరోధం పూర్తిగా శూన్యమయ్యే దృగ్విషయం", "MRI స్కానింగ్ మరియు మాగ్లేవ్ రైళ్ళలో వినియోగం"),
        ("క్వాంటం కంప్యూటింగ్", "క్విబిట్స్ (Qubits) ఆధారంగా అత్యంత వేగంగా సంక్లిష్ట సమస్యలను పరిష్కరించే కంప్యూటర్లు", "సూపర్‌పొజిషన్ మరియు ఎంటాంగిల్‌మెంట్ సూత్రాలు"),
        ("డీఆర్డీఓ రుద్రమ్ క్షిపణి", "శత్రువుల రాడార్లు మరియు కమ్యూనికేషన్ కేంద్రాలను ధ్వంసం చేసే యాంటీ రేడియేషన్ క్షిపణి", "సుఖోయ్-30 ఫైటర్ జెట్ల నుండి ప్రయోగం"),
        ("డీఆర్డీఓ పినాక రాకెట్ లాంచర్", "మల్టీ బారెల్ రాకెట్ వ్యవస్థతో 44 సెకన్లలో 12 రాకెట్లను ప్రయోగించే స్వదేశీ వ్యవస్థ", "కార్గిల్ యుద్ధంలో కీలక పాత్ర"),
        ("తేజస్ యుద్ధ విమానం", "భారతదేశంలో స్వదేశీ పరిజ్ఞానంతో తయారైన తేలికపాటి యుద్ధ విమానం (LCA)", "HAL బెంగళూరు ద్వారా తయారీ"),
        ("ఐఎన్‌ఎస్ విక్రాంత్", "భారతదేశం స్వదేశీ పరిజ్ఞానంతో నిర్మించిన తొలి విమానవాహక నౌక (Aircraft Carrier)", "కొచ్చిన్ షిప్‌యార్డ్ లిమిటెడ్ ద్వారా నిర్మాణం")
    ]

    needed_sci = 143 - len(sci_facts)
    c_s = 0
    while c_s < needed_sci:
        tech, d1, d2 = tech_topics[c_s % len(tech_topics)]
        q_type = c_s % 4
        if q_type == 0:
            q_te = f"ఆధునిక సైన్స్ & టెక్నాలజీలో '{tech}' దేనిని సూచిస్తుంది? (GS-Q{c_s+1})"
            q_en = f"In modern science & technology, what does '{tech}' signify? (GS-Q{c_s+1})"
            c_te, c_en = d1, d1
            d_te, d_en = ["సాంప్రదాయ వంట గ్యాస్ స్టవ్", "రైలు ప్రయాణ చార్జీల తగ్గింపు", "పోస్టల్ స్టాంపుల డిజైన్"], ["Cooking gas stove", "Train fare cut", "Stamp design"]
            exp_te = f"{tech}: {d1}."
            exp_en = f"{tech}: {d1}."
        elif q_type == 1:
            q_te = f"సాంకేతిక అనువర్తనాల ప్రకారం '{tech}' యొక్క ముఖ్య విశిష్టత ఏది? (GS-Q{c_s+1})"
            q_en = f"What is the key application of '{tech}'? (GS-Q{c_s+1})"
            c_te, c_en = d2, d2
            d_te, d_en = ["పాత నాణేల ముద్రణ రద్దు", "రోడ్లపై వాహనాల నిషేధం", "చెట్ల నరికివేత ప్రక్రియ"], ["Coin demonetization", "Vehicle ban", "Deforestation"]
            exp_te = f"{tech}: {d2}."
            exp_en = f"{tech}: {d2}."
        elif q_type == 2:
            q_te = f"కింది వాటిలో '{d1}' అనే లక్షణం కలిగిన ఆధునిక సాంకేతిక పరిజ్ఞానం ఏది? (GS-Q{c_s+1})"
            q_en = f"Which modern technology is characterized by '{d1}'? (GS-Q{c_s+1})"
            c_te, c_en = tech, tech
            d_te, d_en = ["డైల్-అప్ ఇంటర్నెట్", "ఫ్లాపీ డిస్క్", "డాట్ మాట్రిక్స్ ప్రింటర్"], ["Dial-up", "Floppy Disk", "Dot Matrix"]
            exp_te = f"ఇది {tech}కు వర్తిస్తుంది."
            exp_en = f"It corresponds to {tech}."
        else:
            q_te = f"భారత సాంకేతిక మరియు రక్షణ విజయాలలో '{d2}' దేనితో ముడిపడి ఉంది? (GS-Q{c_s+1})"
            q_en = f"In Indian tech achievements, '{d2}' relates to which? (GS-Q{c_s+1})"
            c_te, c_en = tech, tech
            d_te, d_en = ["టెలిగ్రామ్ మెసేజ్", "టైప్‌రైటర్ కీబోర్డ్", "టేప్ రికార్డర్"], ["Telegram msg", "Typewriter", "Tape recorder"]
            exp_te = f"ఇది {tech}తో ముడిపడి ఉంది."
            exp_en = f"It relates to {tech}."

        add_fn("General Science", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)
        c_s += 1

    # ==========================================
    # 9. BIOLOGY (143)
    # ==========================================
    bio_facts = [
        ("కణాన్ని (Cell) మొట్టమొదటిసారిగా 1665లో కనుగొన్న శాస్త్రవేత్త ఎవరు?", "Who discovered the cell in 1665?",
         "రాబర్ట్ హుక్", "Robert Hooke", ["రాబర్ట్ బ్రౌన్", "ఆంటోనీ వాన్ లీవెన్‌హుక్", "థియోడర్ ష్వాన్"], ["Robert Brown", "Leeuwenhoek", "Schwann"],
         "కార్కు ముక్కలో తేనెటీగల గూడు లాంటి నిర్మాణాలను చూసి 'సెల్' అని నామకరణం చేశాడు.", "Robert Hooke coined the term cell."),

        ("కణ శక్త్యాగారాలు (Powerhouses of the Cell) అని వేటిని పిలుస్తారు?", "Which organelles are called the Powerhouses of the Cell?",
         "మైటోకాండ్రియా", "Mitochondria", ["రైబోజోములు", "లైసోజోములు", "గాల్జీ సంక్లిష్టం"], ["Ribosomes", "Lysosomes", "Golgi apparatus"],
         "కణ శ్వాసక్రియ జరిపి ATP రూపంలో శక్తిని నిల్వ ఉంచుతాయి.", "Mitochondria generate cellular energy in form of ATP."),

        ("కణంలో ప్రోటీన్ల కర్మాగారాలు (Protein Factories) అని వేటిని అంటారు?", "Which organelles are called the Protein Factories of the cell?",
         "రైబోజోములు", "Ribosomes", ["క్లోరోప్లాస్ట్‌లు", "కేంద్రకం", "వాక్యుయోల్స్"], ["Chloroplasts", "Nucleus", "Vacuoles"],
         "కణంలో ప్రోటీన్ సంశ్లేషణ రైబోజోములలో జరుగుతుంది.", "Ribosomes are the sites of protein synthesis."),

        ("కణంలో 'ఆత్మహత్య కోశాలు' (Suicide Bags) అని వేటికి పేరు?", "Which organelles are known as Suicide Bags of the cell?",
         "లైసోజోములు", "Lysosomes", ["రైబోజోములు", "ప్లాస్టిడ్లు", "సెంట్రోసోమ్"], ["Ribosomes", "Plastids", "Centrosome"],
         "లైసోజోములలో శక్తివంతమైన జీర్ణక్రియ ఎంజైములు ఉండి జీర్ణకోశాలుగా పనిచేస్తాయి.", "Lysosomes contain hydrolytic enzymes."),

        ("మానవ శరీరంలో అతిపెద్ద గ్రంథి ఏది?", "Which is the largest gland in the human body?",
         "కాలేయం (Liver)", "Liver", ["థైరాయిడ్ గ్రంథి", "క్లోమం", "పీయూష గ్రంథి"], ["Thyroid Gland", "Pancreas", "Pituitary Gland"],
         "కాలేయం దాదాపు 1.5 కిలోల బరువుండి పిత్తరసాన్ని ఉత్పత్తి చేస్తుంది.", "Liver is the largest gland weighing about 1.5 kg."),

        ("మానవ శరీరంలో ఇన్సులిన్ హార్మోన్‌ను ఉత్పత్తి చేసే గ్రంథి ఏది?", "Which gland secretes the hormone Insulin in human body?",
         "క్లోమం (Pancreas)", "Pancreas", ["కాలేయం", "పిట్యూటరీ", "అడ్రినల్"], ["Liver", "Pituitary", "Adrenal"],
         "క్లోమంలోని లాంగర్‌హార్న్స్ పుటికల బీటా కణాలు ఇన్సులిన్‌ను స్రవిస్తాయి.", "Beta cells of Islets of Langerhans in pancreas secrete insulin."),

        ("మానవ రక్త వర్గాలను (A, B, AB, O) కనుగొన్న శాస్త్రవేత్త ఎవరు?", "Who discovered the ABO blood groups in humans?",
         "కార్ల్ ల్యాండ్‌స్టీనర్", "Karl Landsteiner", ["విలియం హార్వే", "ఎడ్వర్డ్ జెన్నర్", "లూయీ పాశ్చర్"], ["William Harvey", "Edward Jenner", "Louis Pasteur"],
         "1900లో కార్ల్ ల్యాండ్‌స్టీనర్ రక్త వర్గాలను కనుగొని నోబెల్ బహుమతి పొందారు.", "Karl Landsteiner discovered ABO blood groups in 1900."),

        ("సార్వత్రిక రక్తదాత (Universal Donor) అని ఏ రక్త వర్గాన్ని పిలుస్తారు?", "Which blood group is known as the Universal Donor?",
         "O నెగెటివ్ (O-)", "O Negative", ["AB పాజిటివ్", "A పాజిటివ్", "B నెగెటివ్"], ["AB Positive", "A Positive", "B Negative"],
         "O నెగెటివ్ రక్తంపై ఎలాంటి యాంటిజెన్లు ఉండవు కాబట్టి ఎవరికైనా ఇవ్వవచ్చు.", "O- blood lacks A, B and Rh antigens."),

        ("సార్వత్రిక రక్త స్వీకర్త (Universal Recipient) అని ఏ రక్త వర్గాన్ని అంటారు?", "Which blood group is known as the Universal Recipient?",
         "AB పాజిటివ్ (AB+)", "AB Positive", ["O నెగెటివ్", "A నెగెటివ్", "B పాజిటివ్"], ["O Negative", "A Negative", "B Positive"],
         "AB పాజిటివ్ రక్తం ఉన్నవారు ఏ గ్రూప్ రక్తాన్నైనా స్వీకరించవచ్చు.", "AB+ can receive red blood cells from any blood type."),

        ("రక్తం గడ్డకట్టడానికి (Blood Clotting) అత్యవసరమైన విటమిన్ ఏది?", "Which vitamin is essential for blood clotting?",
         "విటమిన్ K (ఫిల్లోఖ్వినోన్)", "Vitamin K", ["విటమిన్ A", "విటమిన్ C", "విటమిన్ E"], ["Vitamin A", "Vitamin C", "Vitamin E"],
         "ప్రోథ్రాంబిన్ ఉత్పత్తికి విటమిన్ K అవసరం, లోపిస్తే రక్తస్రావం ఆగదు.", "Vitamin K is needed for synthesis of prothrombin."),

        ("రాత్రిపూట కంటి చూపు మందగించే 'రేచీకటి' (Night Blindness) ఏ విటమిన్ లోపం వల్ల వస్తుంది?", "Deficiency of which vitamin causes Night Blindness?",
         "విటమిన్ A (రెటినాల్)", "Vitamin A (Retinol)", ["విటమిన్ B1", "విటమిన్ C", "విటమిన్ D"], ["Vitamin B1", "Vitamin C", "Vitamin D"],
         "విటమిన్ A లోపం వల్ల రోడాప్సిన్ లోపించి రేచీకటి, జిరాఫ్తాల్మియా వస్తాయి.", "Vitamin A deficiency leads to night blindness."),

        ("చిగుళ్ళ నుండి రక్తం కారే 'స్కర్వీ' వ్యాధి ఏ విటమిన్ లోపం వల్ల కలుగుతుంది?", "Scurvy disease is caused by deficiency of which vitamin?",
         "విటమిన్ C (ఆస్కార్బిక్ ఆమ్లం)", "Vitamin C", ["విటమిన్ D", "విటమిన్ B12", "విటమిన్ K"], ["Vitamin D", "Vitamin B12", "Vitamin K"],
         "విటమిన్ C నిమ్మ, ఉసిరి వంటి పుల్లటి పండ్లలో సమృద్ధిగా లభిస్తుంది.", "Vitamin C deficiency causes scurvy."),

        ("ఎముకలు మెత్తబడే 'రికెట్స్' వ్యాధి ఏ విటమిన్ లోపం వల్ల చిన్నపిల్లల్లో వస్తుంది?", "Rickets in children is caused by deficiency of which vitamin?",
         "విటమిన్ D (కాల్సిఫెరాల్)", "Vitamin D", ["విటమిన్ A", "విటమిన్ E", "విటమిన్ B6"], ["Vitamin A", "Vitamin E", "Vitamin B6"],
         "సూర్యరశ్మి ద్వారా చర్మంలో తయారయ్యే విటమిన్ D లోపిస్తే రికెట్స్ వస్తుంది.", "Sunshine vitamin D deficiency leads to rickets."),

        ("మానవ శరీరంలో 'మాస్టర్ గ్లాండ్' (ప్రధాన గ్రంథి) అని దేనిని పిలుస్తారు?", "Which gland is called the Master Gland of the human body?",
         "పీయూష గ్రంథి (Pituitary Gland)", "Pituitary Gland", ["థైరాయిడ్ గ్రంథి", "అడ్రినల్ గ్రంథి", "థైమస్ గ్రంథి"], ["Thyroid Gland", "Adrenal Gland", "Thymus Gland"],
         "మెదడు అడుగున ఉండే పిట్యూటరీ గ్రంథి ఇతర అంతఃస్రావ గ్రంథులను నియంత్రిస్తుంది.", "Pituitary gland controls secretion of other endocrine glands."),

        ("రక్తంలో గ్లూకోజ్ స్థాయి సాధారణం కంటే ఎక్కువగా పెరిగిపోవడాన్ని ఏమంటారు?", "Abnormally high level of glucose in blood is characteristic of what?",
         "డయాబెటిస్ మెల్లిటస్ (మధుమేహం)", "Diabetes Mellitus", ["డయాబెటిస్ ఇన్‌సిపిడస్", "హైపోగ్లైసీమియా", "రక్తహీనత"], ["Diabetes Insipidus", "Hypoglycemia", "Anemia"],
         "ఇన్సులిన్ లోపం వల్ల రక్తంలో చక్కర శాతం పెరుగుతుంది.", "Insulin deficiency causes diabetes mellitus."),

        ("మలేరియా వ్యాధి ఏ పరాన్నజీవి వల్ల కలుగుతుంది?", "Which protozoan parasite causes Malaria?",
         "ప్లాస్మోడియం (Plasmodium)", "Plasmodium", ["ఎంటమీబా", "ట్రిపనోసోమా", "లీష్మానియా"], ["Entamoeba", "Trypanosoma", "Leishmania"],
         "ఆడ అనాఫిలిస్ దోమ కాటు వల్ల ప్లాస్మోడియం మానవులలో మలేరియాను వ్యాపింపజేస్తుంది.", "Transmitted by female Anopheles mosquito."),

        ("హైదరాబాద్‌లోని సికింద్రాబాద్‌లో మలేరియా దోమలపై పరిశోధనలు చేసి నోబెల్ బహుమతి పొందిన శాస్త్రవేత్త ఎవరు?", "Who won Nobel Prize for discovering malaria transmission in Secunderabad?",
         "సర్ రొనాల్డ్ రాస్ (1897)", "Sir Ronald Ross", ["రాబర్ట్ కాక్", "లూయీ పాశ్చర్", "అలెగ్జాండర్ ఫ్లెమింగ్"], ["Robert Koch", "Louis Pasteur", "Alexander Fleming"],
         "1897 ఆగస్టు 20న బేగంపేట వద్ద మలేరియా పరాన్నజీవి దోమ కడుపులో ఉన్నట్లు కనుగొన్నాడు.", "Ronald Ross discovered malaria transmission in 1897."),

        ("ప్రపంచంలో తొలి యాంటీబయోటిక్ ఔషధమైన 'పెన్సిలిన్'ను కనుగొన్నది ఎవరు?", "Who discovered the first antibiotic Penicillin?",
         "అలెగ్జాండర్ ఫ్లెమింగ్ (1928)", "Alexander Fleming", ["ఎడ్వర్డ్ జెన్నర్", "రాబర్ట్ హుక్", "జోనాస్ సాక్"], ["Edward Jenner", "Robert Hooke", "Jonas Salk"],
         "పెన్సిలియం నొటేటం అనే శిలీంధ్రం నుండి ఫ్లెమింగ్ పెన్సిలిన్ తయారు చేశాడు.", "Alexander Fleming discovered penicillin in 1928."),

        ("మశూచి (Smallpox) వ్యాధికి మొట్టమొదటి టీకా (Vaccine) కనుగొన్న శాస్త్రవేత్త ఎవరు?", "Who developed the first vaccine in the world for Smallpox?",
         "ఎడ్వర్డ్ జెన్నర్ (1796)", "Edward Jenner", ["లూయీ పాశ్చర్", "రాబర్ట్ కాక్", "ఆల్బర్ట్ సాబిన్"], ["Louis Pasteur", "Robert Koch", "Albert Sabin"],
         "ఎడ్వర్డ్ జెన్నర్‌ను 'వ్యాధి నిరోధక శాస్త్ర పితామహుడు' అంటారు.", "Edward Jenner is regarded as Father of Immunology."),

        ("వృక్షాలలో వేర్ల నుండి నీరు, లవణాలను ఆకులకు రవాణా చేసే కణజాలం ఏది?", "Which plant vascular tissue transports water and minerals from roots to leaves?",
         "దారువు (Xylem)", "Xylem", ["పోషక కణజాలం (Phloem)", "మృదు కణజాలం", "స్థూలకోణ కణజాలం"], ["Phloem", "Parenchyma", "Collenchyma"],
         "దారువు నీటిని పైకి రవాణా చేయగా, పోషక కణజాలం తయారు చేసిన ఆహారాన్ని సరఫరా చేస్తుంది.", "Xylem conducts water; phloem conducts food.")
    ]

    for idx, (q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en) in enumerate(bio_facts):
        add_fn("Biology", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)

    bio_topics = [
        ("కిరణజన్య సంయోగక్రియ", "మొక్కలు సూర్యకాంతి, నీరు, CO2 ఉపయోగించి గ్లూకోజ్ మరియు ఆక్సిజన్ తయారు చేసే ప్రక్రియ", "హరితరేణువులలోని క్లోరోఫిల్ వద్ద జరుగుతుంది"),
        ("హిమోగ్లోబిన్", "ఎర్ర రక్త కణాలలో ఆక్సిజన్‌ను రవాణా చేసే ఇనుము కలిగిన శ్వాస వర్ణకం", "రక్తానికి ఎరుపు రంగును ఇస్తుంది"),
        ("తెల్ల రక్త కణాలు (WBC)", "శరీరంలోకి ప్రవేశించే వ్యాధికారక సూక్ష్మజీవులను సంహరించే రక్షక భటులు", "రోగ నిరోధక శక్తికి మూలాధారం"),
        ("రక్తఫలకికలు (Platelets)", "గాయాలు తగిలినపుడు రక్తం గడ్డకట్టడానికి తోడ్పడే రక్త కణాలు", "డెంగ్యూ జ్వరంలో వీటి సంఖ్య గణనీయంగా తగ్గుతుంది"),
        ("నెఫ్రాన్ (Nephron)", "మూత్రపిండాలలో రక్తాన్ని వడబోసే నిర్మాణాత్మక, క్రియాత్మక ప్రమాణం", "ప్రతి కిడ్నీలో సుమారు 10 లక్షల నెఫ్రాన్లు ఉంటాయి"),
        ("డయాలసిస్ (రక్తశుద్ధి)", "మూత్రపిండాలు పనిచేయని రోగులలో రక్తాన్ని కృత్రిమంగా యంత్రం ద్వారా శుద్ధి చేసే పద్ధతి", "శరీరం నుండి వ్యర్థ పదార్థాల తొలగింపు"),
        ("న్యూరాన్ (నాడీ కణం)", "మానవ నాడీ వ్యవస్థలో సమాచారాన్ని విద్యుత్ ప్రచోదనాల రూపంలో చేరవేసే కణం", "శరీరంలో అత్యంత పొడవైన కణం"),
        ("అనుమస్తిష్కం (Cerebellum)", "శరీర సమతుల్యత మరియు స్వచ్ఛంద కండరాల కదలికలను నియంత్రించే మెదడు భాగం", "మద్యం తాగినపుడు ఇది మందగిస్తుంది"),
        ("మజ్జాముఖం (Medulla Oblongata)", "హృదయ స్పందన, శ్వాసక్రియ, రక్తపోటు వంటి అనియంత్రిత చర్యలను నియంత్రిస్తుంది", "మెదడులో అతిముఖ్యమైన ప్రాణాధార భాగం"),
        ("థైరాక్సిన్ హార్మోన్", "మెడ భాగంలోని థైరాయిడ్ గ్రంథి స్రవించే జీవక్రియల నియంత్రణ హార్మోన్", "అయోడిన్ లోపిస్తే గాయిటర్ వ్యాధి వస్తుంది"),
        ("అడ్రినలిన్ (ఎపినెఫ్రిన్)", "ప్రమాద సమయాలలో 'పోరాడు లేదా పారిపో' (Fight or Flight) చర్యలను ప్రేరేపించే హార్మోన్", "అడ్రినల్ గ్రంథి ద్వారా విడుదలవుతుంది"),
        ("క్షయ వ్యాధి (TB)", "మైకోబాక్టీరియం ట్యూబర్‌క్యులోసిస్ అనే బ్యాక్టీరియా వల్ల ఊపిరితిత్తులకు సోకే వ్యాధి", "నివారణకు బిసిజి (BCG) టీకా ఇస్తారు"),
        ("కలరా వ్యాధి", "విబ్రియో కలరా బ్యాక్టీరియా ద్వారా కలుషిత నీరు, ఆహారం వల్ల వ్యాపించే డయేరియా వ్యాధి", "శరీరంలో తీవ్ర డీహైడ్రేషన్ కలిగిస్తుంది"),
        ("టైఫాయిడ్ జ్వరం", "సాల్మొనెల్లా టైఫీ అనే బ్యాక్టీరియా వల్ల సోకే తీవ్ర ప్రేగుల ఇన్ఫెక్షన్ జ్వరం", "వైడాల్ (Widal) పరీక్ష ద్వారా గుర్తిస్తారు"),
        ("రేబీస్ వ్యాధి", "పిచ్చి కుక్క లేదా నక్క కాటు వల్ల రాబ్డో వైరస్ ద్వారా కేంద్ర నాడీ వ్యవస్థకు సోకే వ్యాధి", "హైడ్రోఫోబియా (నీటి భయం) లక్షణం"),
        ("పోలియో వ్యాధి", "పోలియో వైరస్ వల్ల నాడీ కణాలు దెబ్బతిని కాళ్ళు పక్షవాతానికి గురయ్యే వ్యాధి", "జోనాస్ సాక్ (ఇంజెక్షన్), ఆల్బర్ట్ సాబిన్ (ఓరల్ చుక్కలు) కనుగొన్నారు"),
        ("ఎయిడ్స్ (AIDS)", "హ్యూమన్ ఇమ్యునో డెఫిషియెన్సీ వైరస్ (HIV) వల్ల రోగనిరోధక శక్తి నశించే మహమ్మారి", "ఎలీసా (ELISA) మరియు వెస్ట్రన్ బ్లాట్ పరీక్షలు చేస్తారు"),
        ("డెంగ్యూ జ్వరం", "ఎడిస్ ఈజిప్టి (Aedes aegypti) దోమ కాటు వల్ల ఫ్లావి వైరస్ ద్వారా వ్యాపిస్తుంది", "ప్లేట్‌లెట్స్ సంఖ్య పడిపోవడం ప్రధాన లక్షణం"),
        ("మొక్కలలో శ్వాసక్రియ", "ఆకుల అడుగున ఉండే పత్రరంధ్రాలు (Stomata) ద్వారా వాయువుల మార్పిడి జరుగుతుంది", "రాత్రి సమయాల్లో మొక్కలు ఆక్సిజన్ తీసుకుని CO2 విడుదల చేస్తాయి"),
        ("నైట్రోజన్ స్థిరీకరణ", "లెగ్యూమ్ జాతి మొక్కల వేరు బుడిపెలలో ఉండే రైజోబియం బ్యాక్టీరియా గాలిలోని నైట్రోజన్‌ను స్థిరీకరిస్తుంది", "నేల సారవంతాన్ని పెంచుతుంది"),
        ("DNA (డీఆక్సిరైబో న్యూక్లియిక్ ఆమ్లం)", "జీవులలో అనువంశిక సమాచారాన్ని తరతరాలకు చేరవేసే డబుల్ హెలిక్స్ అణువు", "వాట్సన్ మరియు క్రిక్ 1953లో నిర్మాణాన్ని ఆవిష్కరించారు"),
        ("జన్యుశాస్త్ర పితామహుడు", "బఠానీ మొక్కలపై సంకరణ ప్రయోగాలు చేసిన గ్రెగర్ జోహన్ మెండల్", "వారసత్వ సూత్రాలను ప్రతిపాదించాడు"),
        ("క్లోనింగ్ పద్ధతి", "లైంగిక కలయిక లేకుండా ఒకే తల్లి కణం నుండి జన్యుపరంగా సరిసమానమైన జీవిని సృష్టించడం", "రోస్లిన్ ఇన్స్టిట్యూట్‌లో ఇయాన్ విల్మట్ 'డాలీ' గొర్రెను సృష్టించాడు"),
        ("ఆర్ఎన్ఏ (రైబో న్యూక్లియిక్ ఆమ్లం)", "కణాలలో ప్రోటీన్ల సంశ్లేషణ మరియు జన్యు సంకేతాల అనువాదానికి తోడ్పడుతుంది", "సింగిల్ స్ట్రాండ్ నిర్మాణం కలిగి ఉంటుంది"),
        ("విటమిన్ B12 (సైనోకోబాలమిన్)", "కోబాల్ట్ మూలకాన్ని కలిగి ఉండే కీలక విటమిన్", "లోపిస్తే పెర్నిషియస్ అనీమియా (తీవ్ర రక్తహీనత) వస్తుంది")
    ]

    needed_bio = 143 - len(bio_facts)
    c_b = 0
    while c_b < needed_bio:
        item, desc, role = bio_topics[c_b % len(bio_topics)]
        q_type = c_b % 4
        if q_type == 0:
            q_te = f"జీవశాస్త్రంలో '{item}' దేనిని వివరిస్తుంది? (BIO-Q{c_b+1})"
            q_en = f"What does '{item}' describe in biological sciences? (BIO-Q{c_b+1})"
            c_te, c_en = desc, desc
            d_te, d_en = ["ఇనుప ఖనిజం కరిగే ఉష్ణోగ్రత", "భూకంప తీవ్రతను కొలిచే పద్ధతి", "నక్షత్రాల వయస్సును లెక్కించే విధానం"], ["Melting iron", "Earthquake measure", "Star age calculation"]
            exp_te = f"{item}: {desc}."
            exp_en = f"{item}: {desc}."
        elif q_type == 1:
            q_te = f"మానవ శరీరం లేదా జీవులలో '{item}' యొక్క ముఖ్య విధి/లక్షణం ఏది? (BIO-Q{c_b+1})"
            q_en = f"What is the key role or function of '{item}'? (BIO-Q{c_b+1})"
            c_te, c_en = role, role
            d_te, d_en = ["కంటి రంగును మార్చడం", "జుట్టును తెల్లబరచడం", "గోళ్ళ పొడవును తగ్గించడం"], ["Change eye color", "Whiten hair", "Shorten nails"]
            exp_te = f"{item}: {role}."
            exp_en = f"{item}: {role}."
        elif q_type == 2:
            q_te = f"కింది వాటిలో '{desc}' అనే వివరణ ఏ అంశానికి సరిపోలుతుంది? (BIO-Q{c_b+1})"
            q_en = f"Which biological concept corresponds to '{desc}'? (BIO-Q{c_b+1})"
            c_te, c_en = item, item
            d_te, d_en = ["గ్లైకోలిసిస్", "క్రెబ్స్ చక్రం", "పెప్టైడ్ బంధం"], ["Glycolysis", "Krebs Cycle", "Peptide Bond"]
            exp_te = f"ఇది {item}కు సరిపోలుతుంది."
            exp_en = f"It corresponds to {item}."
        else:
            q_te = f"వైద్య లేదా జీవశాస్త్ర పరిజ్ఞానంలో '{role}' దేనితో ముడిపడి ఉంది? (BIO-Q{c_b+1})"
            q_en = f"In medical/biological context, '{role}' relates to what? (BIO-Q{c_b+1})"
            c_te, c_en = item, item
            d_te, d_en = ["కార్బన్ డేటింగ్", "స్పెక్ట్రోస్కోపీ", "సిస్మోగ్రాఫ్"], ["Carbon dating", "Spectroscopy", "Seismograph"]
            exp_te = f"ఇది {item}తో ముడిపడి ఉంది."
            exp_en = f"It relates to {item}."

        add_fn("Biology", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)
        c_b += 1

    # ==========================================
    # 10. PHYSICS (143)
    # ==========================================
    phy_facts = [
        ("అంతర్జాతీయ ప్రమాణాల పద్ధతిలో (SI System) బలానికి (Force) ప్రమాణం ఏది?", "What is the SI unit of Force?",
         "న్యూటన్ (Newton)", "Newton", ["జౌల్", "వాట్", "పాస్కల్"], ["Joule", "Watt", "Pascal"],
         "F = ma సూత్రం ప్రకారం బలానికి SI ప్రమాణం న్యూటన్ (kg·m/s²).", "SI unit of force is Newton."),

        ("న్యూటన్ మొదటి చలన నియమం ఏ భౌతిక ధర్మాన్ని నిర్వచిస్తుంది?", "Newton's First Law of Motion defines which physical concept?",
         "జడత్వం (Inertia)", "Inertia", ["ద్రవ్యవేగం", "త్వరణం", "గురుత్వాకర్షణ"], ["Momentum", "Acceleration", "Gravity"],
         "బాహ్య బలం పనిచేయనంత వరకు వస్తువు తన నిశ్చల లేదా సమచలన స్థితిని కొనసాగిస్తుంది.", "A body remains at rest or uniform motion unless acted upon by external force."),

        ("రాకెట్ ప్రయోగం ఏ నియమం ఆధారంగా పనిచేస్తుంది?", "Rocket propulsion works on the principle of which law?",
         "న్యూటన్ మూడవ చలన నియమం / ద్రవ్యవేగ పరిరక్షణ", "Newton's Third Law", ["న్యూటన్ మొదటి నియమం", "పాస్కల్ నియమం", "ఆర్కిమెడిస్ సూత్రం"], ["Newton's First Law", "Pascal's Law", "Archimedes Principle"],
         "ప్రతి చర్యకు సమానమైన మరియు వ్యతిరేక దిశలో ప్రతిచర్య ఉంటుంది.", "To every action there is equal and opposite reaction."),

        ("భూమి ఉపరితలంపై గురుత్వ త్వరణం (g) ప్రామాణిక విలువ ఎంత?", "What is the standard value of acceleration due to gravity (g) on Earth?",
         "9.8 మీ/సె²", "9.8 m/s²", ["9.8 సెం.మీ/సె", "8.9 మీ/సె²", "11.2 కి.మీ/సె"], ["9.8 cm/s", "8.9 m/s²", "11.2 km/s"],
         "భూమధ్యరేఖ వద్ద 'g' కనిష్టంగాను, ధ్రువాల వద్ద గరిష్టంగాను ఉంటుంది.", "Standard value of g is 9.8 m/s²; maximum at poles."),

        ("భూమి గురుత్వాకర్షణ క్షేత్రం నుండి తప్పించుకోవడానికి అవసరమైన పలాయన వేగం (Escape Velocity) ఎంత?", "What is the Escape Velocity from the Earth's surface?",
         "11.2 కి.మీ/సెకన్", "11.2 km/s", ["9.8 కి.మీ/సె", "7.9 కి.మీ/సె", "2.4 కి.మీ/సె"], ["9.8 km/s", "7.9 km/s", "2.4 km/s"],
         "ఏ వస్తువైనా 11.2 km/s వేగంతో విసిరితే తిరిగి భూమిపైకి రాదు.", "Escape velocity from Earth is approximately 11.2 km/s."),

        ("ఎండమావులు (Mirages) ఏర్పడటానికి కారణమైన కాంతి దృగ్విషయం ఏది?", "Which optical phenomenon causes the formation of Mirages in deserts?",
         "సంపూర్ణ అంతర పరావర్తనం (Total Internal Reflection)", "Total Internal Reflection", ["కాంతి విక్షేపణం", "కాంతి వ్యతికరణం", "కాంతి వివర్తనం"], ["Dispersion", "Interference", "Diffraction"],
         "కాంతి సాంద్రతర యానకం నుండి విరళ యానకంలోకి ప్రవేశించినపుడు సంపూర్ణ అంతర పరావర్తనం జరుగుతుంది.", "Mirages occur due to total internal reflection."),

        ("వజ్రం అత్యంత ప్రకాశవంతంగా మెరవడానికి కారణమైన భౌతిక ధర్మం ఏది?", "Which phenomenon causes the brilliant sparkling of a diamond?",
         "సంపూర్ణ అంతర పరావర్తనం (క్రిటికల్ కోణం 24.4°)", "Total Internal Reflection", ["కాంతి పరావర్తనం మాత్రమే", "కాంతి ధ్రువణం", "కాంతి శోషణం"], ["Reflection only", "Polarization", "Absorption"],
         "వజ్రం యొక్క సందిగ్ధ కోణం కేవలం 24.4° కావడం వల్ల కాంతి లోపలే బంధించబడి మెరుస్తుంది.", "Diamond's small critical angle causes total internal reflection."),

        ("ఆకాశం నీలిరంగులో కనిపించడానికి కారణమైన భౌతిక సూత్రం ఏది?", "Why does the clear sky appear blue during daytime?",
         "కాంతి పరిక్షేపణం (Scattering of Light)", "Scattering of Light", ["కాంతి వక్రీభవనం", "కాంతి విక్షేపణం", "కాంతి పరావర్తనం"], ["Refraction", "Dispersion", "Reflection"],
         "లార్డ్ ర్యాలీ నియమం ప్రకారం తక్కువ తరంగదైర్ఘ్యం గల నీలికాంతి వాతావరణంలో ఎక్కువగా పరిక్షేపణం చెందుతుంది.", "Blue light scatters more due to shorter wavelength (Rayleigh)."),

        ("వాహనాల రియర్ వ్యూ మిర్రర్ (వెనుక దృశ్యాలు చూసే అద్దం) గా దేనిని ఉపయోగిస్తారు?", "Which type of mirror is used as Rear-View Mirror in automobiles?",
         "కుంభాకార దర్పణం (Convex Mirror)", "Convex Mirror", ["పుటాకార దర్పణం", "సమతల దర్పణం", "స్థూపాకార దర్పణం"], ["Concave Mirror", "Plane Mirror", "Cylindrical Mirror"],
         "కుంభాకార దర్పణం నిటారైన, చిన్నదైన ప్రతిబింబాన్ని ఏర్పరుస్తూ విస్తృత దృశ్య క్షేత్రాన్ని ఇస్తుంది.", "Convex mirror gives an erect diminished image with wide field of view."),

        ("దంత వైద్యులు పంటి లోపలి భాగాలను పెద్దవిగా చూడటానికి ఏ దర్పణాన్ని వాడతారు?", "Which mirror is used by Dentists to examine teeth?",
         "పుటాకార దర్పణం (Concave Mirror)", "Concave Mirror", ["కుంభాకార దర్పణం", "సమతల దర్పణం", "ద్వికుంభాకార కటకం"], ["Convex Mirror", "Plane Mirror", "Biconvex Lens"],
         "వస్తువు నాభి లోపల ఉన్నపుడు పుటాకార దర్పణం పెద్దదైన మిథ్యా ప్రతిబింబాన్ని ఏర్పరుస్తుంది.", "Dentists use concave mirror for magnified image of teeth."),

        ("హ్రస్వదృష్టి (దగ్గరి చూపు ఉండి దూరం కనిపించకపోవడం / Myopia) నివారణకు ఏ కటకం వాడతారు?", "Which lens is used to correct Short-Sightedness (Myopia)?",
         "పుటాకార కటకం (Concave Lens)", "Concave Lens", ["కుంభాకార కటకం", "ద్విఫోకల్ కటకం", "స్థూపాకార కటకం"], ["Convex Lens", "Bifocal Lens", "Cylindrical Lens"],
         "పుటాకార కటకం కాంతి కిరణాలను వికేంద్రీకరించి ప్రతిబింబాన్ని రెటీనాపై కేంద్రీకరిస్తుంది.", "Concave lens diverges light rays so image forms on retina."),

        ("దీర్ఘదృష్టి (దూరపు చూపు ఉండి దగ్గర కనిపించకపోవడం / Hypermetropia) నివారణకు ఏ కటకం వాడతారు?", "Which lens is used to correct Long-Sightedness (Hypermetropia)?",
         "కుంభాకార కటకం (Convex Lens)", "Convex Lens", ["పుటాకార కటకం", "స్థూపాకార కటకం", "ప్లేనో కటకం"], ["Concave Lens", "Cylindrical Lens", "Plano Lens"],
         "కుంభాకార కటకం కాంతి కిరణాలను కేంద్రీకరించి ప్రతిబింబం రెటీనాపై పడేలా చేస్తుంది.", "Convex lens converges light rays onto retina."),

        ("మానవ చెవి వినగలిగే ధ్వని శ్రవ్య పరిధి (Audible Frequency Range) ఎంత?", "What is the audible frequency range of human ear?",
         "20 Hz నుండి 20,000 Hz", "20 Hz to 20,000 Hz", ["0 Hz నుండి 20 Hz", "20,000 Hz కంటే ఎక్కువ", "100 Hz నుండి 5,000 Hz"], ["0 to 20 Hz", "Above 20,000 Hz", "100 to 5,000 Hz"],
         "20 Hz కంటే తక్కువైతే పరశ్రావ్యాలు (Infrasonics), 20 kHz మించితే అతిధ్వనులు (Ultrasonics).", "Human hearing range is 20 Hz to 20 kHz."),

        ("గబ్బిలాలు రాత్రిపూట చీకటిలో ఆహారాన్ని, అడ్డంకులను గుర్తించడానికి ఏ తరంగాలను ఉపయోగిస్తాయి?", "Bats navigate and hunt in dark using which waves?",
         "అతిధ్వనులు (Ultrasonic Waves)", "Ultrasonic Waves", ["పరశ్రావ్యాలు", "రేడియో తరంగాలు", "మైక్రోవేవ్స్"], ["Infrasonic Waves", "Radio Waves", "Microwaves"],
         "గబ్బిలాలు అతిధ్వనుల ప్రతిధ్వని (Echolocation) ద్వారా మార్గాన్ని శోధిస్తాయి.", "Bats use ultrasound echolocation."),

        ("సముద్రపు లోతును మరియు నీటి అడుగున మునిగిన వస్తువులను గుర్తించే పరికరం ఏది?", "Which instrument uses ultrasonic waves to measure depth of the sea?",
         "సోనార్ (SONAR)", "SONAR", ["రాడార్", "లేజర్", "సిస్మోగ్రాఫ్"], ["RADAR", "LASER", "Seismograph"],
         "సౌండ్ నావిగేషన్ అండ్ రేంజింగ్ (SONAR) అతిధ్వనులను ఉపయోగించి లోతును కొలుస్తుంది.", "SONAR measures underwater depth using ultrasound."),

        ("ధ్వని ఏ యానకంలో ప్రయాణించలేదు?", "Through which medium can sound NOT travel?",
         "శూన్యం (Vacuum)", "Vacuum", ["గాలి", "నీరు", "ఉక్కు"], ["Air", "Water", "Steel"],
         "ధ్వని యాంత్రిక తరంగం కాబట్టి ప్రసారానికి తప్పనిసరిగా పదార్థ యానకం అవసరం, శూన్యంలో ప్రయాణించదు.", "Sound is a mechanical wave and cannot propagate in vacuum."),

        ("ఉష్ణోగ్రతను కొలిచే SI ప్రమాణం ఏది?", "What is the SI unit of Temperature?",
         "కెల్విన్ (Kelvin - K)", "Kelvin (K)", ["డిగ్రీ సెల్సియస్", "ఫారెన్‌హీట్", "రాంకైన్"], ["Degree Celsius", "Fahrenheit", "Rankine"],
         "ఉష్ణోగ్రతకు ప్రామాణిక SI ప్రమాణం కెల్విన్. పరమ శూన్య ఉష్ణోగ్రత 0 K (-273.15°C).", "SI unit of temperature is Kelvin (0 K = -273.15°C)."),

        ("నీరు ఏ ఉష్ణోగ్రత వద్ద గరిష్ట సాంద్రతను (Maximum Density) కలిగి ఉంటుంది?", "At what temperature does water have its maximum density?",
         "4°C (నాలుగు డిగ్రీల సెల్సియస్)", "4°C", ["0°C", "100°C", "-4°C"], ["0°C", "100°C", "-4°C"],
         "నీటి అసంగత వ్యాకోచం వల్ల 4°C వద్ద సాంద్రత గరిష్టంగా, ఘనపరిమాణం కనిష్టంగా ఉంటుంది.", "Water anomalous expansion gives max density at 4°C."),

        ("విద్యుత్ ప్రవాహాన్ని (Electric Current) కొలిచే SI ప్రమాణం ఏది?", "What is the SI unit of Electric Current?",
         "ఆంపియర్ (Ampere)", "Ampere", ["వోల్ట్", "ఓమ్", "కూలుంబ్"], ["Volt", "Ohm", "Coulomb"],
         "ఏకాంక కాలంలో ప్రవహించే ఆవేశాన్ని విద్యుత్ ప్రవాహం అంటారు, దీని ప్రమాణం ఆంపియర్.", "Electric current is rate of flow of charge measured in Amperes."),

        ("విద్యుత్ నిరోధాన్ని (Electrical Resistance) కొలిచే SI ప్రమాణం ఏది?", "What is the SI unit of Electrical Resistance?",
         "ఓమ్ (Ohm - Ω)", "Ohm (Ω)", ["వాట్", "హెన్రీ", "ఫారడ్"], ["Watt", "Henry", "Farad"],
         "ఓమ్ నియమం (V = IR) ప్రకారం నిరోధానికి ప్రమాణం ఓమ్.", "Resistance is measured in Ohms (V = IR).")
    ]

    for idx, (q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en) in enumerate(phy_facts):
        add_fn("Physics", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)

    phy_topics = [
        ("పని మరియు శక్తి ప్రమాణం", "జౌల్ (Joule)", "1 న్యూటన్ బలం ప్రయోగించి వస్తువును 1 మీటర్ దూరం జరిపితే జరిగే పని"),
        ("సామర్థ్యం (Power) ప్రమాణం", "వాట్ (Watt)", "ఏకాంక కాలంలో జరిగే పని రేటు (1 Joule/sec = 1 Watt)"),
        ("విద్యుత్ శక్తి వాణిజ్య ప్రమాణం", "కిలోవాట్-అవర్ (kWh / 1 యూనిట్)", "1 యూనిట్ = 3.6 × 10^6 జౌల్స్"),
        ("గతిజ శక్తి (Kinetic Energy)", "KE = 1/2 mv²", "వస్తువు చలనం వల్ల కలిగి ఉండే శక్తి"),
        ("స్థితిజ శక్తి (Potential Energy)", "PE = mgh", "వస్తువు స్థితి లేదా స్థానం వల్ల కలిగి ఉండే శక్తి"),
        ("ద్రవ్యరాశి నిత్యత్వ నియమం", "శక్తిని సృష్టించలేము, నాశనం చేయలేము", "ఒక రూపం నుండి మరొక రూపంలోకి మాత్రమే మార్చగలము"),
        ("పాస్కల్ నియమం", "మూసి ఉన్న ద్రవంలో ఒత్తిడి అన్ని దిశల్లోనూ సమానంగా వ్యాపిస్తుంది", "హైడ్రాలిక్ బ్రేకులు, హైడ్రాలిక్ లిఫ్ట్ పనితీరు ఆధారం"),
        ("ఆర్కిమెడిస్ సూత్రం", "ద్రవంలో మునిగిన వస్తువు కోల్పోయినట్లు కనిపించే బరువు అది తొలగించిన ద్రవపు బరువుకు సమానం", "ఓడలు, జలాంతర్గాములు తేలే సూత్రం"),
        ("ఉపరితల తలతన్యత (Surface Tension)", "ద్రవాలు తమ ఉపరితల వైశాల్యాన్ని కనిష్టంగా ఉంచుకోవడానికి ప్రయత్నించే ధర్మం", "వర్షపు బిందువులు గుండ్రంగా ఉండటానికి కారణం"),
        ("కేశనాళికీయత (Capillarity)", "సన్నని గొట్టంలో ద్రవం పైకి ఎగబాకే లేదా క్రిందికి దిగే ధర్మం", "దీపపు వత్తి ద్వారా నూనె పైకి ఎక్కడం, చెట్లలో నీటి సరఫరా"),
        ("స్నిగ్ధత (Viscosity)", "ద్రవ పొరల మధ్య సాపేక్ష చలనాన్ని వ్యతిరేకించే అంతర్గత ఘర్షణ బలం", "నీటి కంటే తేనె నెమ్మదిగా ప్రవహించడానికి కారణం"),
        ("డోప్లర్ ప్రభావం", "ధ్వని జనకానికి మరియు పరిశీలకునికి మధ్య సాపేక్ష చలనం వల్ల పౌనఃపున్యంలో కలిగే మార్పు", "రైలు సమీపిస్తున్నపుడు విజిల్ శబ్దం తీక్షణంగా వినిపించడం"),
        ("ట్రాన్స్‌ఫార్మర్ సూత్రం", "ఫారడే పరస్పర విద్యుదయస్కాంత ప్రేరణ సూత్రం", "AC వోల్టేజ్‌ను పెంచడానికి లేదా తగ్గించడానికి వాడతారు (DC పై పనిచేయదు)"),
        ("డైనమో / జనరేటర్", "యాంత్రిక శక్తిని విద్యుత్ శక్తిగా మారుస్తుంది", "విద్యుదయస్కాంత ప్రేరణ నియమం ఆధారంగా పనిచేస్తుంది"),
        ("ఎలక్ట్రిక్ మోటార్", "విద్యుత్ శక్తిని యాంత్రిక శక్తిగా మారుస్తుంది", "ఫ్లెమింగ్ ఎడమ చేతి నియమం ఆధారంగా పనిచేస్తుంది"),
        ("ఫ్యూజ్ వైర్ ధర్మం", "తక్కువ ద్రవీభవన స్థానం మరియు అధిక నిరోధం", "అధిక కరెంట్ వచ్చినపుడు కరిగిపోయి గృహోపకరణాలను రక్షిస్తుంది"),
        ("విద్యుత్ బల్బు ఫిలమెంట్", "టంగ్‌స్టన్ (Tungsten) లోహం", "అత్యధిక ద్రవీభవన స్థానం (సుమారు 3422°C) కలిగి ఉంటుంది"),
        ("హీటర్ కాయిల్ వైర్", "నిక్రోమ్ (Nichrome) మిశ్రమ లోహం", "నికెల్, క్రోమియం, ఐరన్ మిశ్రమం; ఎర్రగా వేడెక్కినా ఆక్సీకరణం చెందదు"),
        ("థర్మోస్ ఫ్లాస్క్ నిర్మాణం", "ద్వంద్వ గాజు గోడల మధ్య శూన్యం మరియు వెండి పూత", "ఉష్ణ వాహనం, సంవహనం, వికిరణం ద్వారా ఉష్ణ నష్టాన్ని నిరోధిస్తుంది"),
        ("కాంతి వేగం (Speed of Light)", "శూన్యంలో సెకనుకు 3 లక్షల కిలోమీటర్లు (3 × 10^8 m/s)", "విశ్వంలో అత్యంత గరిష్ట సాధ్య వేగం"),
        ("సూర్యకాంతి భూమిని చేరడానికి పట్టే సమయం", "సుమారు 8 నిమిషాల 20 సెకన్లు (500 సెకన్లు)", "సూర్యుడు-భూమి సగటు దూరం 15 కోట్ల కి.మీ."),
        ("చంద్రుని కాంతి భూమిని చేరే సమయం", "సుమారు 1.3 సెకన్లు", "చంద్రుని దూరం 3,84,400 కి.మీ."),
        ("ఇంద్రధనుస్సు ఏర్పడే కారణాలు", "వక్రీభవనం, సంపూర్ణ అంతర పరావర్తనం మరియు విక్షేపణం", "నీటి బిందువు చిన్న పట్టకంలా పనిచేస్తుంది"),
        ("ప్రాథమిక రంగులు (Primary Colors)", "ఎరుపు, ఆకుపచ్చ, నీలం (RGB)", "ఈ మూడింటి కలయికతో మిగిలిన అన్ని రంగులను సృష్టించవచ్చు"),
        ("లేటెంట్ హీట్ (గుప్తోష్ణం)", "ఉష్ణోగ్రతలో మార్పు లేకుండా పదార్థ స్థితి మారడానికి గ్రహించే లేదా విడుదల చేసే ఉష్ణం", "మరుగుతున్న నీటి కంటే ఆవిరి వల్ల కాలినపుడు తీవ్ర గాయం అవుతుంది")
    ]

    needed_phy = 143 - len(phy_facts)
    c_ph = 0
    while c_ph < needed_phy:
        concept, ans, reason = phy_topics[c_ph % len(phy_topics)]
        q_type = c_ph % 4
        if q_type == 0:
            q_te = f"భౌతిక శాస్త్రంలో '{concept}' యొక్క విలువ లేదా సమాధానం ఏది? (PHY-Q{c_ph+1})"
            q_en = f"What is the value/aspect of '{concept}' in Physics? (PHY-Q{c_ph+1})"
            c_te, c_en = ans, ans
            d_te, d_en = ["సున్నా మాత్రమే", "అనంతమైన విలువ", "ప్రమాణాలు లేని పరిమాణం"], ["Zero only", "Infinite", "Dimensionless"]
            exp_te = f"{concept}: {ans}."
            exp_en = f"{concept}: {ans}."
        elif q_type == 1:
            q_te = f"భౌతిక నియమాల ప్రకారం '{concept}' దేనిని వివరిస్తుంది? (PHY-Q{c_ph+1})"
            q_en = f"What does '{concept}' explain in physics? (PHY-Q{c_ph+1})"
            c_te, c_en = reason, reason
            d_te, d_en = ["కాంతి వేగం తగ్గడం", "గురుత్వాకర్షణ రద్దవడం", "ధ్వని పెరగడం"], ["Light slows", "Gravity cancels", "Sound amplifies"]
            exp_te = f"{concept}: {reason}."
            exp_en = f"{concept}: {reason}."
        elif q_type == 2:
            q_te = f"కింది వాటిలో '{ans}' అనే ప్రమాణం లేదా సూత్రం దేనికి వర్తిస్తుంది? (PHY-Q{c_ph+1})"
            q_en = f"To which does '{ans}' apply? (PHY-Q{c_ph+1})"
            c_te, c_en = concept, concept
            d_te, d_en = ["రేడియోధార్మికత", "ఆవర్తన కాలం", "ధ్రువణం"], ["Radioactivity", "Time period", "Polarization"]
            exp_te = f"ఇది {concept}కు వర్తిస్తుంది."
            exp_en = f"It applies to {concept}."
        else:
            q_te = f"నిత్యజీవిత దృగ్విషయాలలో '{reason}' దేనితో ముడిపడి ఉంది? (PHY-Q{c_ph+1})"
            q_en = f"In physical phenomena, '{reason}' relates to what? (PHY-Q{c_ph+1})"
            c_te, c_en = concept, concept
            d_te, d_en = ["ద్రవ్య పరిమాణం", "కాంతి వేగం", "శూన్యం"], ["Mass amount", "Speed of light", "Vacuum"]
            exp_te = f"ఇది {concept}తో ముడిపడి ఉంది."
            exp_en = f"It relates to {concept}."

        add_fn("Physics", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)
        c_ph += 1

    # ==========================================
    # 11. CHEMISTRY (143)
    # ==========================================
    chem_facts = [
        ("పరమాణువులో ఎలక్ట్రాన్ (Electron) ను కనుగొన్న శాస్త్రవేత్త ఎవరు?", "Who discovered the Electron in 1897?",
         "జె.జె. థామ్సన్ (J.J. Thomson)", "J.J. Thomson", ["రూథర్‌ఫర్డ్", "జేమ్స్ చాడ్విక్", "నీల్స్ బోర్"], ["Rutherford", "James Chadwick", "Niels Bohr"],
         "కాథోడ్ కిరణాలపై ప్రయోగాలు చేసి ఋణ ఆవేశం గల ఎలక్ట్రాన్‌ను థామ్సన్ కనుగొన్నారు.", "J.J. Thomson discovered electron using cathode ray tube."),

        ("పరమాణు కేంద్రకంలో ప్రోటాన్ మరియు న్యూట్రాన్లలో న్యూట్రాన్‌ను కనుగొన్నది ఎవరు?", "Who discovered the Neutron in 1932?",
         "జేమ్స్ చాడ్విక్ (James Chadwick)", "James Chadwick", ["జె.జె. థామ్సన్", "రూథర్‌ఫర్డ్", "డాల్టన్"], ["J.J. Thomson", "Rutherford", "Dalton"],
         "ఎలాంటి విద్యుత్ ఆవేశం లేని తటస్థ కణమైన న్యూట్రాన్‌ను చాడ్విక్ ఆవిష్కరించారు.", "James Chadwick discovered neutral particle neutron."),

        ("ఆధునిక ఆవర్తన పట్టికను (Modern Periodic Table) ఏ లక్షణం ఆధారంగా రూపొందించారు?", "On what basis is the Modern Periodic Table arranged?",
         "పరమాణు సంఖ్య (Atomic Number - Z)", "Atomic Number", ["పరమాణు ద్రవ్యరాశి", "సాంద్రత", "సంయోజకత"], ["Atomic Mass", "Density", "Valency"],
         "హెన్రీ మోస్లే పరమాణు సంఖ్య ఆధారంగా ఆధునిక ఆవర్తన నియమాన్ని ప్రతిపాదించాడు.", "Henry Moseley arranged modern table by atomic number."),

        ("ద్రావణాల ఆమ్ల, క్షార స్వభావాన్ని కొలిచే pH స్కేల్‌ను రూపొందించిన శాస్త్రవేత్త ఎవరు?", "Who introduced the pH scale in 1909?",
         "ఎస్.పి.ఎల్. సోరెన్‌సన్ (Sorensen)", "Sorensen", ["అర్హీనియస్", "బ్రోన్‌స్టెడ్", "లూయిస్"], ["Arrhenius", "Bronsted", "Lewis"],
         "0 నుండి 14 వరకు గల pH స్కేల్ ద్వారా హైడ్రోజన్ అయాన్ గాఢతను కొలుస్తారు.", "Sorensen introduced pH scale (0 to 14)."),

        ("స్వచ్ఛమైన నీటి pH విలువ గది ఉష్ణోగ్రత వద్ద ఎంత ఉంటుంది?", "What is the pH value of pure water at room temperature?",
         "7.0 (తటస్థ ద్రావణం)", "7.0 (Neutral)", ["0", "14", "5.6"], ["0", "14", "5.6"],
         "శుద్ధ జలం తటస్థంగా ఉంటుంది కావున pH = 7.0.", "Pure water is neutral with pH 7.0."),

        ("ఆరోగ్యవంతుడైన మానవ రక్తం యొక్క సాధారణ pH విలువ ఎంత?", "What is the normal pH of human blood?",
         "7.35 నుండి 7.45 (స్వల్ప క్షారత్వం)", "7.35 - 7.45", ["6.0", "8.5", "5.5"], ["6.0", "8.5", "5.5"],
         "మానవ రక్తం స్వల్ప క్షార స్వభావాన్ని కలిగి ఉంటుంది (సగటున 7.4).", "Human blood is slightly basic around pH 7.4."),

        ("గది ఉష్ణోగ్రత వద్ద ద్రవ రూపంలో ఉండే ఏకైక లోహం ఏది?", "Which is the only metal that is liquid at room temperature?",
         "పాదరసం (Mercury - Hg)", "Mercury (Hg)", ["గాలియం", "సోడియం", "లెడ్"], ["Gallium", "Sodium", "Lead"],
         "పాదరసం ద్రవ రూపంలో ఉండే లోహం, థర్మామీటర్లలో వాడుతారు.", "Mercury is liquid at room temperature."),

        ("గది ఉష్ణోగ్రత వద్ద ద్రవ రూపంలో ఉండే ఏకైక అలోహం (Non-metal) ఏది?", "Which is the only non-metal that is liquid at room temperature?",
         "బ్రోమిన్ (Bromine - Br)", "Bromine (Br)", ["క్లోరిన్", "అయోడిన్", "ఫ్లోరిన్"], ["Chlorine", "Iodine", "Fluorine"],
         "ఎరుపు రంగు ద్రవ అలోహం బ్రోమిన్.", "Bromine is a reddish-brown liquid non-metal."),

        ("విద్యుత్‌ను అత్యుత్తమంగా ప్రవహింపజేసే అత్యధిక వాహకత గల లోహం ఏది?", "Which metal is the best conductor of electricity?",
         "వెండి (Silver - Ag)", "Silver (Ag)", ["రాగి (Copper)", "బంగారం (Gold)", "అల్యూమినియం"], ["Copper", "Gold", "Aluminium"],
         "వెండి అన్ని లోహాలలోకెల్లా అత్యధిక విద్యుత్ వాహకతను కలిగి ఉంది.", "Silver has the highest electrical conductivity."),

        ("పెన్సిల్ లెడ్ తయారీలో ఉపయోగించే కార్బన్ రూపాంతరం ఏది?", "Which allotrope of carbon is used in pencil leads?",
         "గ్రాఫైట్ (Graphite)", "Graphite", ["వజ్రం", "బొగ్గు", "కోక్"], ["Diamond", "Coal", "Coke"],
         "గ్రాఫైట్ పొరల నిర్మాణం కలిగి ఉండి మృదువుగా జారుతూ రాయడానికి వీలు కల్పిస్తుంది.", "Graphite's layered structure makes it ideal for pencils."),

        ("ప్రకృతిలో లభించే అత్యంత కఠినమైన సహజ పదార్థం ఏది?", "Which is the hardest naturally occurring substance on Earth?",
         "వజ్రం (Diamond)", "Diamond", ["ప్లాటినం", "క్వార్ట్జ్", "కోరండం"], ["Platinum", "Quartz", "Corundum"],
         "వజ్రంలో ప్రతి కార్బన్ పరమాణువు నాలుగు ఇతర కార్బన్లతో చతుర్ముఖీయంగా బంధించబడి ఉంటుంది.", "Diamond is hardest due to tetrahedral covalent bonds."),

        ("వంట సోడా (Baking Soda) యొక్క రసాయన నామం ఏమిటి?", "What is the chemical name of Baking Soda?",
         "సోడియం బైకార్బోనేట్ (NaHCO3)", "Sodium Bicarbonate", ["సోడియం కార్బోనేట్", "సోడియం హైడ్రాక్సైడ్", "కాల్షియం క్లోరైడ్"], ["Sodium Carbonate", "Sodium Hydroxide", "Calcium Chloride"],
         "బేకింగ్ సోడా ఆహారాన్ని మెత్తగా ఉబ్బించడానికి తోడ్పడుతుంది.", "Baking soda is Sodium Bicarbonate (NaHCO3)."),

        ("బట్టల సోడా (Washing Soda) యొక్క రసాయన సూత్రం ఏది?", "What is the chemical formula of Washing Soda?",
         "Na2CO3·10H2O (సోడియం కార్బోనేట్ డెకాహైడ్రేట్)", "Na2CO3·10H2O", ["NaHCO3", "NaOH", "CaSO4"], ["NaHCO3", "NaOH", "CaSO4"],
         "బట్టల సోడాలో 10 స్ఫటిక జల అణువులు ఉంటాయి.", "Washing soda is Sodium Carbonate Decahydrate."),

        ("లాఫింగ్ గ్యాస్ (నవ్వు పుట్టించే వాయువు) అని దేనిని పిలుస్తారు?", "Which gas is commonly known as Laughing Gas?",
         "నైట్రస్ ఆక్సైడ్ (N2O)", "Nitrous Oxide (N2O)", ["నైట్రిక్ ఆక్సైడ్", "నైట్రోజన్ డయాక్సైడ్", "సల్ఫర్ డయాక్సైడ్"], ["Nitric Oxide", "Nitrogen Dioxide", "Sulfur Dioxide"],
         "వైద్యశాస్త్రంలో మత్తుమందుగా నైట్రస్ ఆక్సైడ్‌ను వాడుతారు.", "Nitrous Oxide is used as an anesthetic."),

        ("ప్లాస్టర్ ఆఫ్ ప్యారిస్ (POP) యొక్క రసాయన నామం ఏమిటి?", "What is the chemical formula of Plaster of Paris?",
         "CaSO4·1/2H2O (కాల్షియం సల్ఫేట్ హెమీహైడ్రేట్)", "CaSO4·1/2H2O", ["CaSO4·2H2O", "CaCO3", "CaO"], ["CaSO4·2H2O", "CaCO3", "CaO"],
         "జిప్సంను 373 K ఉష్ణోగ్రత వద్ద వేడి చేసినపుడు ప్లాస్టర్ ఆఫ్ ప్యారిస్ ఏర్పడుతుంది.", "Heated gypsum forms Plaster of Paris."),

        ("ఎల్‌పీజీ (LPG - సిలిండర్ గ్యాస్) లో ప్రధానంగా ఉండే హైడ్రోకార్బన్లు ఏవి?", "Which hydrocarbons are the main components of LPG?",
         "బ్యూటేన్ మరియు ప్రొపేన్", "Butane and Propane", ["మీథేన్ మరియు ఈథేన్", "ఎసిటిలీన్", "బెంజీన్"], ["Methane and Ethane", "Acetylene", "Benzene"],
         "ఎల్‌పీజీలో లీకేజీని గుర్తించడానికి దుర్వాసన గల 'ఇథైల్ మెర్కాప్టన్' కలుపుతారు.", "LPG contains butane and propane with ethyl mercaptan."),

        ("ఆమ్ల వర్షాలకు (Acid Rains) ప్రధానంగా కారణమయ్యే వాయు కాలుష్య కారకాలు ఏవి?", "Which gases are primarily responsible for Acid Rain?",
         "సల్ఫర్ డయాక్సైడ్ (SO2) మరియు నైట్రోజన్ ఆక్సైడ్లు (NOx)", "SO2 and NOx", ["కార్బన్ మోనాక్సైడ్", "మీథేన్", "ఓజోన్"], ["Carbon Monoxide", "Methane", "Ozone"],
         "SO2 మరియు NO2 వర్షపు నీటితో కలిసి సల్ఫ్యూరిక్, నైట్రిక్ ఆమ్లాలుగా మారుతాయి.", "Form sulfuric and nitric acids causing acid rain."),

        ("భూమి ఉపరితలాన్ని అతినీలలోహిత (UV) వికిరణాల నుండి రక్షించే ఓజోన్ పొర రసాయన సూత్రం ఏది?", "What is the chemical formula of Ozone that absorbs UV radiation?",
         "O3 (ట్రైయాక్సిజన్)", "O3", ["O2", "O4", "CO2"], ["O2", "O4", "CO2"],
         "స్ట్రాటోస్ఫియర్‌లో ఉన్న ఓజోన్ పొర హానికర అతినీలలోహిత కిరణాలను అడ్డుకుంటుంది.", "Ozone (O3) in stratosphere filters harmful UV rays."),

        ("ఓజోన్ పొర క్షీణతకు ప్రధానంగా కారణమైన రసాయన సమ్మేళనాలు ఏవి?", "Which chemicals are primarily responsible for Ozone layer depletion?",
         "క్లోరోఫ్లోరో కార్బన్లు (CFCs / ఫ్రియాన్లు)", "Chlorofluorocarbons (CFCs)", ["కార్బన్ డయాక్సైడ్", "నైట్రోజన్", "హైడ్రోజన్"], ["Carbon Dioxide", "Nitrogen", "Hydrogen"],
         "రిఫ్రిజిరేటర్లు, ఏసీలలో వాడే CFCలు విడుదల చేసే క్లోరిన్ రాడికల్స్ ఓజోన్‌ను నాశనం చేస్తాయి.", "CFCs release chlorine atoms that destroy ozone."),

        ("ఇనుము తుప్పు పట్టడం (Rusting of Iron) ఏ రకమైన రసాయన చర్య?", "Rusting of iron is an example of which chemical process?",
         "రెడాక్స్ చర్య (ఆక్సీకరణం మరియు క్షయకరణం)", "Redox Reaction (Oxidation)", ["కేవలం క్షయకరణం", "వియోగ చర్య", "భౌతిక మార్పు"], ["Reduction only", "Decomposition", "Physical change"],
         "తేమ మరియు ఆక్సిజన్ సమక్షంలో ఇనుము హైడ్రేటెడ్ ఫెర్రిక్ ఆక్సైడ్ (Fe2O3·xH2O) గా మారుతుంది.", "Iron oxidizes in presence of oxygen and moisture.")
    ]

    for idx, (q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en) in enumerate(chem_facts):
        add_fn("Chemistry", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)

    chem_topics = [
        ("బ్లీచింగ్ పౌడర్", "CaOCl2 (కాల్షియం ఆక్సిక్లోరైడ్)", "తాగునీటిని క్రిమిరహితం చేయడానికి మరియు వస్త్ర పరిశ్రమలో విరంజనకారిగా వాడతారు"),
        ("సాధారణ ఉప్పు", "NaCl (సోడియం క్లోరైడ్)", "ఆహార రుచికి మరియు రసాయన పరిశ్రమలలో ముడిసరుకుగా ఉపయోగిస్తారు"),
        ("కాస్టిక్ సోడా", "NaOH (సోడియం హైడ్రాక్సైడ్)", "సబ్బులు మరియు కాగితం తయారీలో ఉపయోగించే బలమైన క్షారం"),
        ("వెనిగర్ (Vinegar)", "5-8% ఎసిటిక్ ఆమ్లం (CH3COOH) జల ద్రావణం", "ఆహార నిల్వ మరియు ఊరగాయల తయారీలో ప్రిజర్వేటివ్‌గా వాడతారు"),
        ("నిమ్మరసంలో ఉండే ఆమ్లం", "సిట్రిక్ ఆమ్లం (Citric Acid)", "సిట్రస్ జాతి పండ్లలో లభించే సహజ సేంద్రీయ ఆమ్లం"),
        ("చీమలు కుట్టినపుడు విడుదలయ్యే ఆమ్లం", "ఫార్మిక్ ఆమ్లం / మిథనోయిక్ ఆమ్లం (HCOOH)", "మంట మరియు నొప్పి కలిగించే ఆమ్లం"),
        ("పుల్లటి పెరుగులో ఉండే ఆమ్లం", "లాక్టిక్ ఆమ్లం (Lactic Acid)", "పాలలోని లాక్టోజ్ లాక్టోబాసిల్లస్ బ్యాక్టీరియా ద్వారా లాక్టిక్ ఆమ్లంగా మారుతుంది"),
        ("చింతపండులో ఉండే ఆమ్లం", "టార్టారిక్ ఆమ్లం (Tartaric Acid)", "బేకింగ్ పౌడర్ తయారీలో కూడా ఉపయోగిస్తారు"),
        ("ఆపిల్ పండ్లలో ఉండే ఆమ్లం", "మాలిక్ ఆమ్లం (Malic Acid)", "ఆపిల్ పండ్లకు పులుపుదనాన్ని ఇచ్చే ఆమ్లం"),
        ("కార్ బ్యాటరీలలో వాడే ఆమ్లం", "సల్ఫ్యూరిక్ ఆమ్లం (H2SO4)", "'రసాయనాల రారాజు' (King of Chemicals) అని పిలుస్తారు"),
        ("బంగారాన్ని కరిగించే ఆమ్లరాజం (Aqua Regia)", "3 భాగాలు గాఢ HCl + 1 భాగం గాఢ HNO3", "బంగారం, ప్లాటినం వంటి ఉత్కృష్ట లోహాలను కరిగిస్తుంది"),
        ("ఇత్తడి (Brass) మిశ్రమ లోహం", "రాగి (Cu 70%) మరియు జింక్ (Zn 30%)", "పాత్రలు, సంగీత వాయిద్యాల తయారీలో వాడుతారు"),
        ("కంచు (Bronze) మిశ్రమ లోహం", "రాగి (Cu 88%) మరియు టిన్ (Sn 12%)", "విగ్రహాలు, పతకాలు మరియు నాణేల తయారీలో వాడతారు"),
        ("స్టెయిన్‌లెస్ స్టీల్ మిశ్రమం", "ఇనుము (Fe), క్రోమియం (Cr), నికెల్ (Ni), కార్బన్", "తుప్పు పట్టని దృఢమైన మిశ్రమ లోహం"),
        ("గాల్వనైజేషన్ (Galvanization)", "ఇనుము తుప్పు పట్టకుండా జింక్ (Zn) పూత పూసే పద్ధతి", "నీటి పైపులు, రూఫింగ్ రేకుల రక్షణ"),
        ("ఆవరణ పట్టికలో ఉత్కృష్ట వాయువులు (Noble Gases)", "హీలియం, నియాన్, ఆర్గాన్, క్రిప్టాన్, జినాన్, రేడాన్", "18వ గ్రూపు మూలకాలు, రసాయనికంగా జడమైనవి"),
        ("బెలూన్లలో నింపే తేలికపాటి మండని వాయువు", "హీలియం (He)", "హైడ్రోజన్ తర్వాత రెండవ తేలికైన, సురక్షిత వాయువు"),
        ("విద్యుత్ బల్బులలో నింపే జడ వాయువు", "ఆర్గాన్ (Ar) లేదా నైట్రోజన్", "ఫిలమెంట్ ఆక్సీకరణం చెందకుండా ఆయుష్షును పెంచుతుంది"),
        ("ట్రాఫిక్ సైన్‌బోర్డులలో వెలిగే వాయువు", "నియాన్ (Ne)", "ఎరుపు-నారింజ రంగు వెలుగును ఇచ్చే గ్యాస్ డిశ్చార్జ్ లైట్లు"),
        ("సిగరెట్ లైటర్లలో ఉపయోగించే వాయువు", "బ్యూటేన్ (Butane)", "పీడనంలో సులభంగా ద్రవరూపంలోకి మారే ఇంధనం"),
        ("కార్బన్ మోనాక్సైడ్ (CO) ప్రమాదం", "రక్తంలోని హిమోగ్లోబిన్‌తో బలంగా బంధం ఏర్పరచి ఊపిరాడకుండా చేస్తుంది", "వాహనాల పొగలో వెలువడే విష వాయువు"),
        ("గ్రీన్‌హౌస్ వాయువులలో అత్యంత సమృద్ధిగా ఉన్నది", "నీటి ఆవిరి (Water Vapour) మరియు CO2", "భూమి ఉష్ణోగ్రతను నిలుపుతూ గ్లోబల్ వార్మింగ్‌కు కారణం"),
        ("తాగునీటి శుద్ధిలో వాడే వాయువు", "క్లోరిన్ (Chlorine)", "బాక్టీరియా మరియు క్రిములను సంహరించే క్రిమినాశిని"),
        ("కృత్రిమంగా పండ్లను పక్వానికి తెచ్చే వాయువు", "ఎథిలీన్ (Ethylene) / ఎసిటిలీన్ (కాల్షియం కార్బైడ్ నుండి)", "రైపనింగ్ హార్మోన్‌గా పనిచేసే వాయువు"),
        ("సిమెంట్ తయారీలో గట్టిపడటాన్ని నెమ్మదింపజేసే పదార్థం", "జిప్సం (CaSO4·2H2O)", "సిమెంట్ త్వరగా గడ్డకట్టకుండా సమయం ఇస్తుంది")
    ]

    needed_chem = 143 - len(chem_facts)
    c_ch = 0
    while c_ch < needed_chem:
        c_sub, c_formula, c_use = chem_topics[c_ch % len(chem_topics)]
        q_type = c_ch % 4
        if q_type == 0:
            q_te = f"రసాయన శాస్త్రంలో '{c_sub}' యొక్క రసాయన సూత్రం లేదా గుర్తింపు ఏది? (CHEM-Q{c_ch+1})"
            q_en = f"What is the chemical formula/identity of '{c_sub}'? (CHEM-Q{c_ch+1})"
            c_te, c_en = c_formula, c_formula
            d_te, d_en = ["హైడ్రోజన్ పెరాక్సైడ్", "అమ్మోనియం నైట్రేట్", "పొటాషియం పర్మాంగనేట్"], ["H2O2", "NH4NO3", "KMnO4"]
            exp_te = f"{c_sub}: {c_formula}."
            exp_en = f"{c_sub}: {c_formula}."
        elif q_type == 1:
            q_te = f"రసాయన పదార్థమైన '{c_sub}' యొక్క ప్రధాన అనువర్తనం లేదా ఉపయోగం ఏది? (CHEM-Q{c_ch+1})"
            q_en = f"What is the primary use/property of '{c_sub}'? (CHEM-Q{c_ch+1})"
            c_te, c_en = c_use, c_use
            d_te, d_en = ["రైలు పట్టాల శబ్దం తగ్గించడం", "చెట్ల పెరుగుదలను ఆపడం", "నీటి రంగును ఎరుపుగా మార్చడం"], ["Reduce rail noise", "Halt plant growth", "Turn water red"]
            exp_te = f"{c_sub}: {c_use}."
            exp_en = f"{c_sub}: {c_use}."
        elif q_type == 2:
            q_te = f"కింది వాటిలో '{c_formula}' అనే రసాయన లక్షణం దేనికి చెందుతుంది? (CHEM-Q{c_ch+1})"
            q_en = f"Which substance corresponds to '{c_formula}'? (CHEM-Q{c_ch+1})"
            c_te, c_en = c_sub, c_sub
            d_te, d_en = ["బెంజీన్", "టోలీన్", "ఫినాల్"], ["Benzene", "Toluene", "Phenol"]
            exp_te = f"ఇది {c_sub}కు చెందుతుంది."
            exp_en = f"It corresponds to {c_sub}."
        else:
            q_te = f"పారిశ్రామిక లేదా నిత్యజీవితంలో '{c_use}' ఏ పదార్థం యొక్క విశిష్టత? (CHEM-Q{c_ch+1})"
            q_en = f"'{c_use}' is the distinctive characteristic of which substance? (CHEM-Q{c_ch+1})"
            c_te, c_en = c_sub, c_sub
            d_te, d_en = ["సున్నపురాయి", "డొలమైట్", "బాక్సైట్"], ["Limestone", "Dolomite", "Bauxite"]
            exp_te = f"ఇది {c_sub} యొక్క విశిష్టత."
            exp_en = f"It is characteristic of {c_sub}."

        add_fn("Chemistry", q_te, q_en, c_te, c_en, d_te, d_en, exp_te, exp_en)
        c_ch += 1

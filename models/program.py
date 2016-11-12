import re


programs = {
    u'AHS\s*?-?\s*?\(?unspecified\)?': {
        'program': 'AHS-(unspecified)',
        'faculty': 'Applied Health Sciences'
    },
    u'AHS\s*?-?\s*?(Hlth|Health)\s*?Studies\s*?&?\s*?Gerontology': {
        'program': 'AHS-Health Studies & Gerontology',
        'faculty': 'Applied Health Sciences'
    },
    u'AHS\s*?-?\s*?Kinesiology': {
        'program': 'AHS-Kinesiology',
        'faculty': 'Applied Health Sciences'
    },
    u'AHS\s*?-?\s*?\Public\s*?Health': {
        'program': 'AHS-Public Health',
        'faculty': 'Applied Health Sciences'
    },
    u'AHS\s*?-?\s*?Rec\.?\s*?&?\s*?Leisure\s*?Studies': {
        'program': 'AHS-Rec. & Leisure Studies',
        'faculty': 'Applied Health Sciences'
    },
    u'AHS\s*?-?\s*?Sport\s*?&?\s*?Business': {
        'program': 'AHS-Sport & Business',
        'faculty': 'Applied Health Sciences'
    },
    u'ARCH\s*?-?\s*Architecture': {
        'program': 'ARCH-Architecture',
        'faculty': 'Architecture'
    },
    u'ARTS\s*?-?\s*MASTERS\s*?-?\s*(Economics|Econ)': {
        'program': 'ARTS-Master-Economics',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?MASTERS\s*?-?\s*?Exp\s*?Digital\s*?Media': {
        'program': 'ARTS-MASTERS-Exp Digital Media',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?MASTERS\s*?-?\s*?Literary\s*?Studies': {
        'program': 'ARTS-MASTERS-Literary Studies',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?MASTERS\s*?-?\s*?Political\s*?Science': {
        'program': 'ARTS-MASTERS-Political Science',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?MASTERS\s*?-?\s*?Public\s*?Service': {
        'program': 'ARTS-MASTERS-Public Science',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?MASTERS\s*?-?\s*?(Rhet|Rhetoric)\/(Comm|Communication)\s*?Design': {
        'program': 'ARTS-MASTERS-Rhetoric/Communication Design',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?\(?unspecified\)?': {
        'program': 'ARTS-(unspecified)',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Anthropology': {
        'program': 'ARTS-Anthropology',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Arts\s*?&?\s*?Business': {
        'program': 'ARTS-Arts & Business',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Digital\s*?Arts\s*?(Comm|Communication)': {
        'program': 'ARTS-Digital Arts Communication',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Economics': {
        'program': 'ARTS-Economics',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?English\s*?(Lit|Literature)\s*?&?\s*?Rhetoric': {
        'program': 'ARTS-English Literature & Rhetoric',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?English\s*?Literature': {
        'program': 'ARTS-English Literature',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Financial\s*?Management': {
        'program': 'ARTS-Financial Management',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Fine\s*?Arts': {
        'program': 'ARTS-Fine Arts',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?French': {
        'program': 'ARTS-French',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Global\s*?Bus\s*?&?\s*?Digital\s*?Arts': {
        'program': 'ARTS-Global Bus & Digital Arts',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Global\s*?Engagement': {
        'program': 'ARTS-Global Engagements',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?HR\s*?Management': {
        'program': 'ARTS-HR Management',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?History': {
        'program': 'ARTS-History',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?International\s*?Trade': {
        'program': 'ARTS-International Trade',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Legal\s*?Studies': {
        'program': 'ARTS-Legal Studies',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Management\s*?Accounting': {
        'program': 'ARTS-Management Accounting',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Mathematical\s*?Economics': {
        'program': 'ARTS-Mathematical Economics',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Philosophy': {
        'program': 'ARTS-Philosophy',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Political\s*?Science': {
        'program': 'ARTS-Political Science',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Psychology': {
        'program': 'ARTS-Psychology',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Rhetoric\s*?&?\s*?Prof\s*?Writing': {
        'program': 'ARTS-Rhetoric & Prof Writing',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Sociology': {
        'program': 'ARTS-Sociology',
        'faculty': 'Arts'
    },
    u'ARTS\s*?-?\s*?Speech\s*?Communication': {
        'program': 'ARTS-Speech Communication',
        'faculty': 'Arts'
    },
    u'All\s*?Business\s*?\(?unspecified\)?': {
        'program': 'All Business (unspecified)'
    },
    u'All\s*?Chart\s*?Prof\s*?Acct\s*?\(?CPA\)?': {
        'program': 'All Chart Prof Acct (CPA)'
    },
    u'All\s*?Finance\s*?\(?unspecified\)?': {
        'program': 'All Finance (unspecified)'
    },
    u'All\s*?Health\s*?Informatics': {
        'program': 'All Health Informatics'
    },
    u'All\s*?Info\s*?Tech\s*?\(?unspecified\)?': {
        'program': 'All Info Tech (unspecified)'
    },
    u'ENG\s*?-?\s*?MASTERS\s*?-?\s*?Civil': {
        'program': 'ENG-MASTERS-Civil',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?MASTERS\s*?-?\s*?Management\s*?Science': {
        'program': 'ENG-MASTERS-Management Science',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?\(?unspecified\)?': {
        'program': 'ENG-(unspecified)',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Biomedical': {
        'program': 'ENG-Biomedical',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Chemical': {
        'program': 'ENG-Chemical',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Civil': {
        'program': 'ENG-Civil',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Computer': {
        'program': 'ENG-Computer',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Electrical': {
        'program': 'ENG-Electrical',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Environmental': {
        'program': 'ENG-Environmental',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Geological': {
        'program': 'ENG-Geological',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Management': {
        'program': 'ENG-Management',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Mechanical': {
        'program': 'ENG-Mechanical',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Mechatronics': {
        'program': 'ENG-Mechatronics',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Nanotechnology': {
        'program': 'ENG-Nanotechnology',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Software': {
        'program': 'ENG-Software',
        'faculty': 'Engineering'
    },
    u'ENG\s*?-?\s*?Systems\s*?Design': {
        'program': 'ENG-Systems Design',
        'faculty': 'Engineering'
    },
    u'ENV\s*?-?\s*?\(?unspecified\)?': {
        'program': 'ENV-(unspecified)',
        'faculty': 'Environment'
    },
    u'ENV\s*?-?\s*?ERS': {
        'program': 'ENV-(unspecified)',
        'faculty': 'Environment'
    },
    u'ENV\s*?-?\s*?Env\s*?&?\s*?Resource\s*?Studies': {
        'program': 'ENV-Env & Resource Studies',
        'faculty': 'Environment'
    },
    u'ENV\s*?-?\s*?Environment\s*?&?\s*?Business': {
        'program': 'ENV-Environment & Business',
        'faculty': 'Environment'
    },
    u'ENV\s*?-?\s*?Geog\s*?&?\s*?Env\s*?Management': {
        'program': 'ENV-Geog & Env Management',
        'faculty': 'Environment'
    },
    u'ENV\s*?-?\s*?Geomatics': {
        'program': 'ENV-Geomatics',
        'faculty': 'Environment'
    },
    u'ENV\s*?-?\s*?International\s*?Development': {
        'program': 'ENV-International Development',
        'faculty': 'Environment'
    },
    u'ENV\s*?-?\s*?Knowledge\s*?Integration': {
        'program': 'ENV-Knowledge Integration',
        'faculty': 'Environment'
    },
    u'ENV\s*?-?\s*?Planning': {
        'program': 'ENV-Planning',
        'faculty': 'Environment'
    },
    u'MATH\s*?-?\s*?MASTERS\s*?-?\s*?Health\s*?Info': {
        'program': 'MATH-MASTERS-Health Info',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?\(?unspecified\)?': {
        'program': 'MATH-(unspecified)',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Actuarial\s*?Science': {
        'program': 'MATH-Actuarial Science',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Applied\s*?Mathematics': {
        'program': 'MATH-Applied Mathematics',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Bioinformatics': {
        'program': 'MATH-Bioinformatics',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Business\s*?Administration': {
        'program': 'MATH-Business Administration',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Combinatorics\s*?&?\s*?(Optimizat|Optimization)': {
        'program': 'MATH-Combinatorics & Optimization',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Computational\s*?Math': {
        'program': 'MATH-Computational Math',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Computer\s*?Science': {
        'program': 'MATH-Computer Science',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Computing\s*?&?\s*?Financial\s*?(Mgm|Mgmt|Management)': {
        'program': 'MATH-Computing & Financial Management',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Fin\s*?Analysis\s*?&?\s*?Risk\s*?(Mgmt|Mgm|Management)': {
        'program': 'MATH-Financial Analysis & Risk Management',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?IT\s*?Management': {
        'program': 'MATH-IT Management',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Mathematical\s*?Economics': {
        'program': 'MATH-Mathematical Economics',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Mathematical\s*?Finance': {
        'program': 'MATH-Mathematical Finance',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Mathematical\s*?Optimization': {
        'program': 'MATH-Mathematical Optimization',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Mathematical\s*?Physics': {
        'program': 'MATH-Mathematical Physics',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Mathematical\s*?Studies': {
        'program': 'MATH-Mathematical Studies',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Pure\s*?-?\s*?Mathematics': {
        'program': 'MATH-Pure Mathematics',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Scientific\s*?Computation': {
        'program': 'MATH-Scientific Computation',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Statistics$': {
        'program': 'MATH-Statistics',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Statistics\s*?for\s*?Health': {
        'program': 'MATH-Statistics for Health',
        'faculty': 'Math'
    },
    u'MATH\s*?-?\s*?Teaching': {
        'program': 'MATH-Teaching',
        'faculty': 'Math'
    },
    # Apparently jobmine misspells university programs..
    u'SCI\s*?-?\s*?\(?unspeci?fied\)?': {
        'program': 'SCI-(unspecified)',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Biochemistry': {
        'program': 'SCI-Biochemistry',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Bioinformatics': {
        'program': 'SCI-Bioinformatics',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Biology': {
        'program': 'SCI-Biology',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Biotechnology\/Economics': {
        'program': 'SCI-Biotechnology/Economics',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Chemistry': {
        'program': 'SCI-Chemistry',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Earth\s*?Sciences': {
        'program': 'SCI-Earth Sciences',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Environmental\s*?Science': {
        'program': 'SCI-Environmental Science',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Geology\s*?and\s*?Hydrogeology': {
        'program': 'SCI-Geology and Hydrogeology',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Optometry': {
        'program': 'SCI-Optometry',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Pharmacy': {
        'program': 'SCI-Pharmacy',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Physics': {
        'program': 'SCI-Physics',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Psychology': {
        'program': 'SCI-Psychology',
        'faculty': 'SCI'
    },
    u'SCI\s*?-?\s*?Science\/Business': {
        'program': 'SCI-Science/Business',
        'faculty': 'SCI'
    }
}


def get_programs():
    return [programs[re_program]['program'] for re_program in programs]


def get_program(name):
    for re_program in programs:
        if re.match(re_program, name, re.IGNORECASE):
            return programs[re_program]['program']

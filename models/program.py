import re

"""
This module is used to manage UW programs.
"""

programs = {
    'AHS-(unspecified)': {
        'program': 'unspecified',
        'faculty': 'Applied Health Sciences'
    },
    'AHS-Hlth Studies & Gerontology': {
        'program': 'Health Studies & Gerontology',
        'faculty': 'Applied Health Sciences'
    },
    'AHS-Kinesiology': {
        'program': 'Kinesiology',
        'faculty': 'Applied Health Sciences'
    },
    'AHS-Public Health': {
        'program': 'Public Health',
        'faculty': 'Applied Health Sciences'
    },
    'AHS-Rec. & Leisure Studies': {
        'program': 'Rec. & Leisure Studies',
        'faculty': 'Applied Health Sciences'
    },
    'AHS-Sport & Business': {
        'program': 'Sport & Business',
        'faculty': 'Applied Health Sciences'
    },
    'ARCH-Architecture': {
        'program': 'Architecture',
        'faculty': 'Architecture'
    },
    'ARTS MASTERS-Economics': {
        'program': 'Master-Economics',
        'faculty': 'Arts'
    },
    'ARTS MASTERS-Exp Digital Media': {
        'program': 'MASTERS-Exp Digital Media',
        'faculty': 'Arts'
    },
    'ARTS MASTERS-Literary Studies': {
        'program': 'MASTERS-Literary Studies',
        'faculty': 'Arts'
    },
    'ARTS MASTERS-Political Science': {
        'program': 'MASTERS-Political Science',
        'faculty': 'Arts'
    },
    'ARTS MASTERS-Public Service': {
        'program': 'MASTERS-Political Science',
        'faculty': 'Arts'
    },
    'ARTS MASTERS-Rhet/Comm Design': {
        'program': 'MASTERS-Rhet/Comm Design',
        'faculty': 'Arts'
    },
    'ARTS-(unspecified)': {
        'program': 'unspecified',
        'faculty': 'Arts'
    },
    'ARTS-Anthropology': {
        'program': 'Anthropology',
        'faculty': 'Arts'
    },
    'ARTS-Arts & Business': {
        'program': 'Arts & Business',
        'faculty': 'Arts'
    },
    'ARTS-Digital Arts Comm': {
        'program': 'Digital Arts Comm',
        'faculty': 'Arts'
    },
    'ARTS-Economics': {
        'program': 'Economics',
        'faculty': 'Arts'
    },
    'ARTS-English Lit & Rhetoric': {
        'program': 'English Lit & Rhetoric',
        'faculty': 'Arts'
    },
    'ARTS-English Literature': {
        'program': 'English Literature',
        'faculty': 'Arts'
    },
    'ARTS-Financial Management': {
        'program': 'Financial Management',
        'faculty': 'Arts'
    },
    'ARTS-Fine Arts': {
        'program': 'Fine Arts',
        'faculty': 'Arts'
    },
    'ARTS-French': {
        'program': 'French',
        'faculty': 'Arts'
    },
    'ARTS-Global Bus & Digital Arts': {
        'program': 'Global Bus & Digital Arts',
        'faculty': 'Arts'
    },
    'ARTS-Global Engagement': {
        'program': 'Global Engagements',
        'faculty': 'Arts'
    },
    'ARTS-HR Management': {
        'program': 'HR Management',
        'faculty': 'Arts'
    },
    'ARTS-History': {
        'program': 'History',
        'faculty': 'Arts'
    },
    'ARTS-International Trade': {
        'program': 'International Trade',
        'faculty': 'Arts'
    },
    'ARTS-Legal Studies': {
        'program': 'Legal Studies',
        'faculty': 'Arts'
    },
    'ARTS-Management Accounting': {
        'program': 'Management Accounting',
        'faculty': 'Arts'
    },
    'ARTS-Mathematical Economics': {
        'program': 'Mathematical Economics',
        'faculty': 'Arts'
    },
    'ARTS-Philosophy': {
        'program': 'Philosophy',
        'faculty': 'Arts'
    },
    'ARTS-Political Science': {
        'program': 'Political Science',
        'faculty': 'Arts'
    },
    'ARTS-Psychology': {
        'program': 'Psychology',
        'faculty': 'Arts'
    },
    'ARTS-Rhetoric & Prof Writing': {
        'program': 'Rhetoric & Prof Writing',
        'faculty': 'Arts'
    },
    'ARTS-Sociology': {
        'program': 'Sociology',
        'faculty': 'Arts'
    },
    'ARTS-Speech Communication': {
        'program': 'Speech Communication',
        'faculty': 'Arts'
    },
    'All Business (unspecified)': {
        'program': 'All Business (unspecified)'
    },
    'All Chart Prof Acct (CPA)': {
        'program': 'All Chart Prof Acct (CPA)'
    },
    'All Finance (unspecified)': {
        'program': 'All Finance (unspecified)'
    },
    'All Health Informatics': {
        'program': 'All Health Informatics'
    },
    'All Info Tech (unspecified)': {
        'program': 'All Info Tech (unspecified)'
    },
    'ENG MASTERS-Civil': {
        'program': 'MASTERS-Civil',
        'faculty': 'Engineering'
    },
    'ENG MASTERS-Management Science': {
        'program': 'MASTERS-Management Science',
        'faculty': 'Engineering'
    },
    'ENG-(unspecified)': {
        'program': 'unspecified',
        'faculty': 'Engineering'
    },
    'ENG-Biomedical': {
        'program': 'Biomedical',
        'faculty': 'Engineering'
    },
    'ENG-Chemical': {
        'program': 'Chemical',
        'faculty': 'Engineering'
    },
    'ENG-Civil': {
        'program': 'Civil',
        'faculty': 'Engineering'
    },
    'ENG-Computer': {
        'program': 'Computer',
        'faculty': 'Engineering'
    },
    'ENG-Electrical': {
        'program': 'Electrical',
        'faculty': 'Engineering'
    },
    'ENG-Environmental': {
        'program': 'Environmental',
        'faculty': 'Engineering'
    },
    'ENG-Geological': {
        'program': 'Geological',
        'faculty': 'Engineering'
    },
    'ENG-Management': {
        'program': 'Management',
        'faculty': 'Engineering'
    },
    'ENG-Mechanical': {
        'program': 'Mechanical',
        'faculty': 'Engineering'
    },
    'ENG-Mechatronics': {
        'program': 'Mechatronics',
        'faculty': 'Engineering'
    },
    'ENG-Nanotechnology': {
        'program': 'Nanotechnology',
        'faculty': 'Engineering'
    },
    'ENG-Software': {
        'program': 'Software',
        'faculty': 'Engineering'
    },
    'ENG-Systems Design': {
        'program': 'Systems Design',
        'faculty': 'Engineering'
    },
    'ENV- (unspecified)': {
        'program': 'unspecified',
        'faculty': 'Environment'
    },
    'ENV-Env & Resource Studies': {
        'program': 'Env & Resource Studies',
        'faculty': 'Environment'
    },
    'ENV-Environment & Business': {
        'program': 'Environment & Business',
        'faculty': 'Environment'
    },
    'ENV-Geog & Env Management': {
        'program': 'Environment & Business',
        'faculty': 'Environment'
    },
    'ENV-Geomatics': {
        'program': 'Geomatics',
        'faculty': 'Environment'
    },
    'ENV-International Development': {
        'program': 'International Development',
        'faculty': 'Environment'
    },
    'ENV-Knowledge Integration': {
        'program': 'Knowledge Integration',
        'faculty': 'Environment'
    },
    'ENV-Planning': {
        'program': 'Planning',
        'faculty': 'Environment'
    },
    'MATH MASTERS-Health Info': {
        'program': 'MASTERS-Health Info',
        'faculty': 'Math'
    },
    'MATH- (unspecified)': {
        'program': 'unspecified',
        'faculty': 'Math'
    },
    'MATH-Actuarial Science': {
        'program': 'Actuarial Science',
        'faculty': 'Math'
    },
    'MATH-Applied Mathematics': {
        'program': 'Applied Mathematics',
        'faculty': 'Math'
    },
    'MATH-Bioinformatics': {
        'program': 'Bioinformatics',
        'faculty': 'Math'
    },
    'MATH-Business Administration': {
        'program': 'Business Administration',
        'faculty': 'Math'
    },
    'MATH-Combinatorics & Optimizat': {
        'program': 'Combinatorics & Optimization',
        'faculty': 'Math'
    },
    'MATH-Computational Math': {
        'program': 'Computational Math',
        'faculty': 'Math'
    },
    'MATH-Computer Science': {
        'program': 'Computer Science',
        'faculty': 'Math'
    },
    'MATH-Computing & Financial Mgm': {
        'program': 'Computing & Financial Management',
        'faculty': 'Math'
    },
    'MATH-Fin Analysis & Risk Mgmt': {
        'program': 'Financial Analysis & Risk Management',
        'faculty': 'Math'
    },
    'MATH-IT Management': {
        'program': 'IT Management',
        'faculty': 'Math'
    },
    'MATH-Mathematical Economics': {
        'program': 'Mathematical Economics',
        'faculty': 'Math'
    },
    'MATH-Mathematical Finance': {
        'program': 'Mathematical Finance',
        'faculty': 'Math'
    },
    'MATH-Mathematical Optimization': {
        'program': 'Mathematical Optimization',
        'faculty': 'Math'
    },
    'MATH-Mathematical Physics': {
        'program': 'Mathematical Physics',
        'faculty': 'Math'
    },
    'MATH-Mathematical Studies': {
        'program': 'Mathematical Studies',
        'faculty': 'Math'
    },
    'MATH-Pure Mathematics': {
        'program': 'Pure Mathematics',
        'faculty': 'Math'
    },
    'MATH-Scientific Computation': {
        'program': 'Scientific Computation',
        'faculty': 'Math'
    },
    'MATH-Statistics': {
        'program': 'Statistics',
        'faculty': 'Math'
    },
    'MATH-Statistics for Health': {
        'program': 'Statistics for Health',
        'faculty': 'Math'
    },
    'MATH-Teaching': {
        'program': 'Teaching',
        'faculty': 'Math'
    },
    'SCI- (unspecified)': {
        'program': 'unspecified',
        'faculty': 'SCI'
    },
    'SCI-Biochemistry': {
        'program': 'Biochemistry',
        'faculty': 'SCI'
    },
    'SCI-Bioinformatics': {
        'program': 'Bioinformatics',
        'faculty': 'SCI'
    },
    'SCI-Biology': {
        'program': 'Biology',
        'faculty': 'SCI'
    },
    'SCI-Biotechnology/Economics': {
        'program': 'Biotechnology/Economics',
        'faculty': 'SCI'
    },
    'SCI-Chemistry': {
        'program': 'Chemistry',
        'faculty': 'SCI'
    },
    'SCI-Earth Sciences': {
        'program': 'Earth Sciences',
        'faculty': 'SCI'
    },
    'SCI-Environmental Science': {
        'program': 'Environmental Science',
        'faculty': 'SCI'
    },
    'SCI-Geology and Hydrogeology': {
        'program': 'Geology and Hydrogeology',
        'faculty': 'SCI'
    },
    'SCI-Optometry': {
        'program': 'Optometry',
        'faculty': 'SCI'
    },
    'SCI-Pharmacy': {
        'program': 'Pharmacy',
        'faculty': 'SCI'
    },
    'SCI-Physics': {
        'program': 'Physics',
        'faculty': 'SCI'
    },
    'SCI-Psychology': {
        'program': 'Psychology',
        'faculty': 'SCI'
    },
    'SCI-Science/Business': {
        'program': 'Science/Business',
        'faculty': 'SCI'
    },
}


def get_programs():
    return [re.sub('\s*-\s*', '-', program) for program in programs]

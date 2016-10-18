import re

import models.keyword_type as keyword_type


keywords = {
    # Keywords with spaces are prioritized
    'A-0 System': {
        'keyword': 'A-0 System',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ABC ALGOL': {
        'keyword': 'ABC ALGOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ace DASL': {
        'keyword': 'Ace DASL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Agilent VEE': {
        'keyword': 'Agilent VEE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ALGOL 58': {
        'keyword': 'ALGOL 58',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ALGOL 60': {
        'keyword': 'ALGOL 60',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ALGOL 68': {
        'keyword': 'ALGOL 68',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ALGOL W': {
        'keyword': 'ALGOL W',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Amiga E': {
        'keyword': 'Amiga E',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'App Inventor for Android': {
        'keyword': 'App Inventor for Android',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ateji PX': {
        'keyword': 'Ateji PX',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Visual LISP': {
        'keyword': 'Visual LISP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Bash Scripting': {
        'keyword': 'Bash',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Linux']
    },
    'C Shell': {
        'keyword': 'Shell',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Unix']
    },
    'Common Lisp': {
        'keyword': 'Common Lisp',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Component Pascal': {
        'keyword': 'Component Pascal',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Coral 66': {
        'keyword': 'Coral 66',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Easy PL/I': {
        'keyword': 'Easy PL/I',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'EASYTRIEVE PLUS': {
        'keyword': 'EASYTRIEVE PLUS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Edinburgh IMP': {
        'keyword': 'Edinburgh IMP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Emacs Lisp': {
        'keyword': 'Emacs Lisp',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'EusLisp Robot': {
        'keyword': 'EusLisp Robot',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'EXEC 2': {
        'keyword': 'EXEC 2',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Franz Lisp': {
        'keyword': 'Franz Lisp',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Game Maker Language': {
        'keyword': 'Game Maker Language',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GameMonkey Script': {
        'keyword': 'GameMonkey Script',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GNU E': {
        'keyword': 'GNU E',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Google Apps Script': {
        'keyword': 'Google Apps Script',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Hamilton C shell': {
        'keyword': 'Hamilton C shell',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Hartmann pipelines': {
        'keyword': 'Hartmann pipelines',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'High Level Assembly': {
        'keyword': 'High Level Assembly',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'IBM Basic assembly language': {
        'keyword': 'IBM Basic assembly language',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'IBM HAScript': {
        'keyword': 'IBM HAScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'IBM Informix-4GL': {
        'keyword': 'IBM Informix-4GL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'IBM RPG': {
        'keyword': 'IBM RPG',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Java Script': {
        'keyword': 'JavaScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Join Java': {
        'keyword': 'Join Java',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'JScript .NET': {
        'keyword': 'JScript .NET',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['.NET']
    },
    'JavaFX Script': {
        'keyword': 'JavaFX Script',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'Klerer-May System': {
        'keyword': 'Klerer-May System',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'L# .NET': {
        'keyword': 'L# .NET',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['.NET']
    },
    'MASM Microsoft Assembly x86': {
        'keyword': 'MASM Microsoft Assembly x86',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MAT LAB': {
        'keyword': 'MATLAB',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MaxScript internal language 3D Studio Max': {
        'keyword': 'MaxScript internal language 3D Studio Max',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Maya (MEL)': {
        'keyword': 'Maya (MEL)',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MIVA Script': {
        'keyword': 'MIVA Script',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Model 204': {
        'keyword': 'Model 204',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Not eXactly C': {
        'keyword': 'Not eXactly C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['C']
    },
    'Not Quite C': {
        'keyword': 'Not Quite C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['C']
    },
    'Object Lisp': {
        'keyword': 'Object Lisp',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Lisp']
    },
    'Object REXX': {
        'keyword': 'Object REXX',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Object Pascal': {
        'keyword': 'Object Pascal',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Xcode/Objective C': {
        'keyword': 'Objective C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['iOS']
    },
    'Obj C': {
        'keyword': 'Objective C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['iOS']
    },
    'Objective C': {
        'keyword': 'Objective C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['iOS']
    },
    'OpenEdge ABL': {
        'keyword': 'OpenEdge ABL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CMS Pipelines': {
        'keyword': 'CMS Pipelines',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'C#/Visual Studio': {
        'keyword': 'C#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Visual Studio/C#': {
        'keyword': 'C#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Executable UML': {
        'keyword': 'Executable UML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Stackless Python': {
        'keyword': 'Stackless Python',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Turbo C++': {
        'keyword': 'Turbo C++',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['C++']
    },
    'UCSD Pascal': {
        'keyword': 'UCSD Pascal',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Unix shell': {
        'keyword': 'Shell',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Unix']
    },
    'Visual Basic': {
        'keyword': 'Visual Basic',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['.NET']
    },
    'Visual Basic .NET': {
        'keyword': 'Visual Basic .NET',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['.NET']
    },
    'VB .NET': {
        'keyword': 'Visual Basic .NET',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['.NET']
    },
    'Visual DataFlex': {
        'keyword': 'Visual DataFlex',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Visual DialogScript': {
        'keyword': 'Visual DialogScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Visual Fortran': {
        'keyword': 'Visual Fortran',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Fortran']
    },
    'Visual FoxPro': {
        'keyword': 'Visual FoxPro',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Visual J++': {
        'keyword': 'Visual J++',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'Visual J#': {
        'keyword': 'Visual J#',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'Visual Objects': {
        'keyword': 'Visual Objects',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Visual Prolog': {
        'keyword': 'Visual Prolog',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Windows PowerShell': {
        'keyword': 'PowerShell',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Windows']
    },
    'Z notation': {
        'keyword': 'Z notation',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Bourne shell': {
        'keyword': 'Bourne shell',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CMS EXEC': {
        'keyword': 'CMS EXEC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Little b': {
        'keyword': 'Little b',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Small Basic': {
        'keyword': 'Small Basic',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'HTML 5': {
        'keyword': 'HTML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'WATFIV, WATFOR': {
        'keyword': 'WATFIV, WATFOR',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Active Server Pages': {
        'keyword': 'ASP.NET',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['.NET']
    },
    'Ruby/Ruby on Rails': {
        'keyword': 'Ruby on Rails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Ruby on Rails': {
        'keyword': 'Ruby on Rails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Groovy on Grails': {
        'keyword': 'Groovy on Grails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Groovy']
    },
    'Play Framework': {
        'keyword': 'Play Framework',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java', 'Scala']
    },
    'Play (Scala)': {
        'keyword': 'Play Framework',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java', 'Scala']
    },
    'JavaServer Faces': {
        'keyword': 'JavaServer Faces',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'JBoss Seam': {
        'keyword': 'JBoss Seam',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Google Web Toolkit': {
        'keyword': 'Google Web Toolkit',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Stripes MVC': {
        'keyword': 'Stripes',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Apache HTTP': {
        'keyword': 'Apache HTTP Server',
        'type': keyword_type.types['WEB_SRV'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Apache HTTP Server': {
        'keyword': 'Apache HTTP Server',
        'type': keyword_type.types['WEB_SRV'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Traffic Server': {
        'keyword': 'Traffic Server',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Cherokee HTTP Server': {
        'keyword': 'Cherokee HTTP Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'LiteSpeed Web Server': {
        'keyword': 'LiteSpeed Web Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'Monkey HTTP Server': {
        'keyword': 'Monkey HTTP Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'NCSA HTTPd': {
        'keyword': 'NCSA HTTPd',
        'type': keyword_type.types['WEB_SRV']
    },
    'OpenLink Virtuoso': {
        'keyword': 'OpenLink Virtuoso',
        'type': keyword_type.types['WEB_SRV']
    },
    'Oracle HTTP Server': {
        'keyword': 'Oracle HTTP Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'Oracle iPlanet Web Server': {
        'keyword': 'Oracle iPlanet Web Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'Saetta Web Server': {
        'keyword': 'Saetta Web Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'Oracle WebLogic Server': {
        'keyword': 'Oracle WebLogic Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'Resin Open Source': {
        'keyword': 'Resin',
        'type': keyword_type.types['WEB_SRV']
    },
    'Resin Professional': {
        'keyword': 'Resin',
        'type': keyword_type.types['WEB_SRV']
    },
    'TUX web server': {
        'keyword': 'TUX Web server',
        'type': keyword_type.types['WEB_SRV']
    },
    'Wakanda Server': {
        'keyword': 'Wakanda Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'Zeus Web Server': {
        'keyword': 'Zeus Web Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'JBoss EAP': {
        'keyword': 'JBoss EAP',
        'type': keyword_type.types['WEB_SRV']
    },
    'IBM HTTP Server': {
        'keyword': 'IBM HTTP Server',
        'type': keyword_type.types['WEB_SRV']
    },
    'Internet Information Services': {
        'keyword': 'IIS',
        'type': keyword_type.types['WEB_SRV']
    },
    'Elastic Search': {
        'keyword': 'Elasticsearch',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'RedHat Linux': {
        'keyword': 'RedHat Linux',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Red Hat Linux': {
        'keyword': 'RedHat Linux',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Kali Linux': {
        'keyword': 'Kali Linux',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Mac OS': {
        'keyword': 'OS X',
        'type': keyword_type.types['OS']
    },
    'Mac OS X': {
        'keyword': 'OS X',
        'type': keyword_type.types['OS']
    },
    'OS X': {
        'keyword': 'OS X',
        'type': keyword_type.types['OS']
    },
    'Hyper V': {
        'keyword': 'Hyper-V',
        'type': keyword_type.types['VM_ENV']
    },
    'MS SQL': {
        'keyword': 'MSSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    '4th Dimension': {
        'keyword': '4th Dimension',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Adabas D': {
        'keyword': 'Adabas D',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Alpha Five': {
        'keyword': 'Alpha Five',
        'type': keyword_type.types['DB']
    },
    'Aster Data': {
        'keyword': 'Aster Data',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Amazon Aurora': {
        'keyword': 'Amazon Aurora',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'CA Datacom': {
        'keyword': 'CA Datacom',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'CA IDMS': {
        'keyword': 'CA IDMS',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Database Management Library': {
        'keyword': 'Database Management Library',
        'type': keyword_type.types['DB']
    },
    'Empress Embedded Database': {
        'keyword': 'Empress Embedded Database',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'FileMaker Pro': {
        'keyword': 'FileMaker Pro',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Google Fusion Tables': {
        'keyword': 'Google Fusion Tables',
        'type': keyword_type.types['DB']
    },
    'Helix database': {
        'keyword': 'Helix database',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'IBM DB2': {
        'keyword': 'IBM DB2',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'IBM Lotus Approach': {
        'keyword': 'IBM Lotus Approach',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'IBM DB2 Express-C': {
        'keyword': 'IBM DB2 Express-C',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'InterSystems Cache': {
        'keyword': 'InterSystems Cache',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'LibreOffice Base': {
        'keyword': 'LibreOffice Base',
        'type': keyword_type.types['DB']
    },
    'Microsoft Access': {
        'keyword': 'Microsoft Access',
        'type': keyword_type.types['DB']
    },
    'Microsoft Jet Database Engine': {
        'keyword': 'Microsoft Jet Database Engine',
        'type': keyword_type.types['DB']
    },
    'SQL Server': {
        'keyword': 'MSSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SQL Azure': {
        'keyword': 'SQL Azure',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Microsoft Visual FoxPro': {
        'keyword': 'Microsoft Visual FoxPro',
        'type': keyword_type.types['DB']
    },
    'Mimer SQL': {
        'keyword': 'Mimer SQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'NonStop SQL': {
        'keyword': 'NonStop SQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Oracle Rdb': {
        'keyword': 'Oracle',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Oracle RDBMS': {
        'keyword': 'Oracle',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Pervasive PSQL': {
        'keyword': 'Pervasive PSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Progress Software': {
        'keyword': 'Progress Software',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'RDM Embedded': {
        'keyword': 'RDM Embedded',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'RDM Server': {
        'keyword': 'RDM Server',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'The SAS system': {
        'keyword': 'The SAS system',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SAND CDBMS': {
        'keyword': 'SAND CDBMS',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SAP HANA': {
        'keyword': 'SAP HANA',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SAP Sybase Adaptive Server Enterprise': {
        'keyword': 'SAP Sybase Adaptive Server Enterprise',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SAP Sybase': {
        'keyword': 'SAP Sybase',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SQL Anywhere': {
        'keyword': 'SQL Anywhere',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Sybase Advantage Database Server': {
        'keyword': 'Sybase Advantage Database Server',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Unisys RDMS 2200': {
        'keyword': 'Unisys RDMS 2200',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'T SQL': {
        'keyword': 'T-SQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'OpenOffice.org Base': {
        'keyword': 'OpenOffice.org Base',
        'type': keyword_type.types['DB']
    },
    'IBM Notes': {
        'keyword': 'IBM Notes',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Virtuoso Universal Server': {
        'keyword': 'Virtuoso Universal Server',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Calpont InfiniDB': {
        'keyword': 'Calpont InfiniDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Cypher Query Language': {
        'keyword': 'Cypher Query Language',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Oracle Spatial and Graph': {
        'keyword': 'Oracle Spatial and Graph',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Sones GraphDB': {
        'keyword': 'Sones GraphDB',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Graph databases': {
        'keyword': 'Graph database',
        'type': keyword_type.types['DB_TYPE']
    },
    'Graph database': {
        'keyword': 'Graph database',
        'type': keyword_type.types['DB_TYPE']
    },
    'Android Studio': {
        'keyword': 'Android',
        'type': keyword_type.types['MOBILE_OS'],
        'extra': ['Java']
    },
    'Android Studio/Java': {
        'keyword': 'Android',
        'type': keyword_type.types['MOBILE_OS'],
        'extra': ['Java']
    },
    'Windows Mobile': {
        'keyword': 'Windows Mobile',
        'type': keyword_type.types['MOBILE_OS'],
        'extra': ['C#']
    },
    'Windows Phone': {
        'keyword': 'Windows Mobile',
        'type': keyword_type.types['MOBILE_OS'],
        'extra': ['C#']
    },
    'React Native': {
        'keyword': 'React Native',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS']
    },
    'Crosswalk Project': {
        'keyword': 'Crosswalk Project',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS']
    },
    'Sencha Touch': {
        'keyword': 'Sencha Touch',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS']
    },
    'Codename One': {
        'keyword': 'Codename One',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['Java', 'Android', 'iOS']
    },
    'Common JS': {
        'keyword': 'CommonJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Cascade Framework': {
        'keyword': 'Cascade Framework',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Cascade Framework Light': {
        'keyword': 'Cascade Framework Light',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Jalsonic Opinion': {
        'keyword': 'Jalsonic Opinion',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Kule Lazy': {
        'keyword': 'Kule Lazy',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Material Design Lite': {
        'keyword': 'Material Design Lite',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Modest Grid': {
        'keyword': 'Modest Grid',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Pure CSS': {
        'keyword': 'Pure CSS',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Responsive BP': {
        'keyword': 'Responsive BP',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Responsive Grid System': {
        'keyword': 'Responsive Grid System',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Schema UI': {
        'keyword': 'Schema UI',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Semantic UI': {
        'keyword': 'Semantic UI',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Sierra SCSS Library': {
        'keyword': 'Sierra SCSS Library',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Visual Component Library (VCL)': {
        'keyword': 'Visual Component Library (VCL)',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Diisba framework': {
        'keyword': 'Diisba framework',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS']
    },
    'Meson build system': {
        'keyword': 'Meson build system',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'MPW Make': {
        'keyword': 'MPW Make',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Open Build Service': {
        'keyword': 'Open Build Service',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'OpenMake Software': {
        'keyword': 'OpenMake Software',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Octopus Deploy': {
        'keyword': 'Octopus Deploy',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['ASP.NET', 'C#', '.NET']
    },
    'Perforce Jam': {
        'keyword': 'Perforce Jam',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Visual Build': {
        'keyword': 'Visual Build',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Continua CI': {
        'keyword': 'Continua CI',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'GitLab CI': {
        'keyword': 'GitLab CI',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Snap CI': {
        'keyword': 'Snap CI',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Solano CI': {
        'keyword': 'Solano CI',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Team Foundation Server': {
        'keyword': 'Team Foundation Server',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Visual Studio Team Services': {
        'keyword': 'Visual Studio Team Services',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Travis CI': {
        'keyword': 'Travis-CI',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'OpenMaker Software': {
        'keyword': 'OpenMaker Software',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Fuse Message Broker': {
        'keyword': 'Fuse Message Broker',
        'type': keyword_type.types['MSG_BROKER']
    },
    'IBM Integration Bus': {
        'keyword': 'IBM Integration Bus',
        'type': keyword_type.types['MSG_BROKER']
    },
    'JBoss Messaging': {
        'keyword': 'JBoss Messaging',
        'type': keyword_type.types['MSG_BROKER']
    },
    'Microsoft BizTalk Server': {
        'keyword': 'Microsoft BizTalk Server',
        'type': keyword_type.types['MSG_BROKER']
    },
    'SAP PI': {
        'keyword': 'SAP PI',
        'type': keyword_type.types['MSG_BROKER']
    },
    'Solace Systems': {
        'keyword': 'Solace Systems',
        'type': keyword_type.types['MSG_BROKER']
    },
    'Spread Toolkit': {
        'keyword': 'Spread Toolkit',
        'type': keyword_type.types['MSG_BROKER']
    },
    'Elastic MapReduce': {
        'keyword': 'Amazon Elastic MapReduce',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Amazon Lambda': {
        'keyword': 'Amazon Lambda',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Amazon Route 53': {
        'keyword': 'Amazon Route 53',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Amazon Virtual Private Cloud': {
        'keyword': 'Amazon VPC',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Amazon VPC': {
        'keyword': 'Amazon VPC',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Amazon Simple Storage Service': {
        'keyword': 'Amazon S3',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Amazon Elastic Block Store': {
        'keyword': 'Amazon Elastic Block Store',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Neural Networks': {
        'keyword': 'Neural Networks',
        'type': keyword_type.types['KEYWORD']
    },
    'Machine learning': {
        'keyword': 'Machine learning',
        'type': keyword_type.types['KEYWORD']
    },
    'Natural Language Processing': {
        'keyword': 'Natural Language Processing',
        'type': keyword_type.types['KEYWORD']
    },
    'Artificial Intelligence': {
        'keyword': 'Artificial Intelligence',
        'type': keyword_type.types['KEYWORD']
    },
    'Big Data': {
        'keyword': 'Big Data',
        'type': keyword_type.types['KEYWORD']
    },
    'Amazon Web Services': {
        'keyword': 'Amazon Web Services',
        'type': keyword_type.types['KEYWORD']
    },
    'Natural-Language Processing': {
        'keyword': 'Natural Language Processing',
        'type': keyword_type.types['KEYWORD']
    },
    # List of programming languages
    'A#': {
        'keyword': 'A#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'A+': {
        'keyword': 'A+',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'A++': {
        'keyword': 'A++',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Arduino': {
        'keyword': 'Arduino',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ABAP': {
        'keyword': 'ABAP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ABC': {
        'keyword': 'ABC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ABSET': {
        'keyword': 'ABSET',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ABSYS': {
        'keyword': 'ABSYS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ACC': {
        'keyword': 'ACC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Accent': {
        'keyword': 'Accent',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ACL2': {
        'keyword': 'ACL2',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ACT-III': {
        'keyword': 'ACT-III',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Action!': {
        'keyword': 'Action!',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ActionScript': {
        'keyword': 'ActionScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ada': {
        'keyword': 'Ada',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Adenine': {
        'keyword': 'Adenine',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Agda': {
        'keyword': 'Agda',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Agora': {
        'keyword': 'Agora',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AIMMS': {
        'keyword': 'AIMMS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Alef': {
        'keyword': 'Alef',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ALF': {
        'keyword': 'ALF',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Alice': {
        'keyword': 'Alice',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Alma-0': {
        'keyword': 'Alma-0',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AmbientTalk': {
        'keyword': 'AmbientTalk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AMOS': {
        'keyword': 'AMOS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AMPL': {
        'keyword': 'AMPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Apex': {
        'keyword': 'Apex',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'APL': {
        'keyword': 'APL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AppleScript': {
        'keyword': 'AppleScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Arc': {
        'keyword': 'Arc',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ARexx': {
        'keyword': 'ARexx',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Argus': {
        'keyword': 'Argus',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AspectJ': {
        'keyword': 'AspectJ',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Assembly': {
        'keyword': 'Assembly',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ATS': {
        'keyword': 'ATS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AutoHotkey': {
        'keyword': 'AutoHotkey',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Autocoder': {
        'keyword': 'Autocoder',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AutoIt': {
        'keyword': 'AutoIt',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AutoLISP': {
        'keyword': 'AutoLISP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Averest': {
        'keyword': 'Averest',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'AWK': {
        'keyword': 'AWK',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Axum': {
        'keyword': 'Axum',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    '.NET': {
        'keyword': '.NET',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Babbage': {
        'keyword': 'Babbage',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Bash': {
        'keyword': 'Bash',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Linux']
    },
    'bc': {
        'keyword': 'bc',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'BCPL': {
        'keyword': 'BCPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'BeanShell': {
        'keyword': 'BeanShell',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Batch': {
        'keyword': 'Batch',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Bertrand': {
        'keyword': 'Bertrand',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'BETA': {
        'keyword': 'BETA',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Bigwig': {
        'keyword': 'Bigwig',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Bistro': {
        'keyword': 'Bistro',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'BitC': {
        'keyword': 'BitC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'BLISS': {
        'keyword': 'BLISS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Blockly': {
        'keyword': 'Blockly',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'BlooP': {
        'keyword': 'BlooP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Blue': {
        'keyword': 'Blue',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Boo': {
        'keyword': 'Boo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Boomerang': {
        'keyword': 'Boomerang',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'BREW': {
        'keyword': 'BREW',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'BPEL': {
        'keyword': 'BPEL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'C/C++': {
        'keyword': 'C++',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['C']
    },
    'C++/C': {
        'keyword': 'C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['C++']
    },
    'C': {
        'keyword': 'C',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'C--': {
        'keyword': 'C--',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'C++': {
        'keyword': 'C++',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'C#/VB.NET': {
        'keyword': 'C#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'C#/.NET': {
        'keyword': 'C#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'C#': {
        'keyword': 'C#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'C/AL': {
        'keyword': 'C/AL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ObjectScript': {
        'keyword': 'ObjectScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Caml': {
        'keyword': 'Caml',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CDuce': {
        'keyword': 'CDuce',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cecil': {
        'keyword': 'Cecil',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cesil': {
        'keyword': 'Cesil',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ceylon': {
        'keyword': 'Ceylon',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CFML': {
        'keyword': 'CFML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cg': {
        'keyword': 'Cg',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ch': {
        'keyword': 'Ch',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Chapel': {
        'keyword': 'Chapel',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Charity': {
        'keyword': 'Charity',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Charm': {
        'keyword': 'Charm',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CHILL': {
        'keyword': 'CHILL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CHIP-8': {
        'keyword': 'CHIP-8',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'chomski': {
        'keyword': 'chomski',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ChucK': {
        'keyword': 'ChucK',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CICS': {
        'keyword': 'CICS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cilk': {
        'keyword': 'Cilk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Citrine': {
        'keyword': 'Citrine',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CL': {
        'keyword': 'CL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Claire': {
        'keyword': 'Claire',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Clarion': {
        'keyword': 'Clarion',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['SQL']
    },
    'Clean': {
        'keyword': 'Clean',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Clipper': {
        'keyword': 'Clipper',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CLIST': {
        'keyword': 'CLIST',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Clojure': {
        'keyword': 'Clojure',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CLU': {
        'keyword': 'CLU',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CMS-2': {
        'keyword': 'CMS-2',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'COBOL': {
        'keyword': 'COBOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CobolScript': {
        'keyword': 'CobolScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cobra': {
        'keyword': 'Cobra',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CoffeeScript': {
        'keyword': 'CoffeeScript',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['JavaScript']
    },
    'ColdFusion': {
        'keyword': 'ColdFusion',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'COMAL': {
        'keyword': 'COMAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CPL': {
        'keyword': 'CPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'COMIT': {
        'keyword': 'COMIT',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CIL': {
        'keyword': 'CIL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'COMPASS': {
        'keyword': 'COMPASS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CHR': {
        'keyword': 'CHR',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Converge': {
        'keyword': 'Converge',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cool': {
        'keyword': 'Cool',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Coq': {
        'keyword': 'Coq',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Corn': {
        'keyword': 'Corn',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CorVision': {
        'keyword': 'CorVision',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'COWSEL': {
        'keyword': 'COWSEL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cryptol': {
        'keyword': 'Cryptol',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'csh': {
        'keyword': 'csh',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Csound': {
        'keyword': 'Csound',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CSP': {
        'keyword': 'CSP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CUDA': {
        'keyword': 'CUDA',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Curl': {
        'keyword': 'Curl',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Curry': {
        'keyword': 'Curry',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cyclone': {
        'keyword': 'Cyclone',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Cython': {
        'keyword': 'Cython',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'D': {
        'keyword': 'D',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DASL': {
        'keyword': 'DASL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Dart': {
        'keyword': 'Dart',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DataFlex': {
        'keyword': 'keyword',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Datalog': {
        'keyword': 'Datalog',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DATATRIEVE': {
        'keyword': 'DATATRIEVE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'dc': {
        'keyword': 'dc',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DCL': {
        'keyword': 'DCL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Deesel': {
        'keyword': 'Deesel',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Delphi': {
        'keyword': 'Delphi',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DinkC': {
        'keyword': 'DinkC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DIBOL': {
        'keyword': 'DIBOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Dog': {
        'keyword': 'Dog',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Draco': {
        'keyword': 'Draco',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DRAKON': {
        'keyword': 'DRAKON',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Dylan': {
        'keyword': 'Dylan',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DYNAMO': {
        'keyword': 'DYNAMO',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'E': {
        'keyword': 'E',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'E#': {
        'keyword': 'E#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ease': {
        'keyword': 'Ease',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ECMAScript': {
        'keyword': 'ECMAScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'EGL': {
        'keyword': 'EGL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Eiffel': {
        'keyword': 'Eiffel',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ELAN': {
        'keyword': 'ELAN',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Elixir': {
        'keyword': 'Elixir',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Elm': {
        'keyword': 'Elm',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Emerald': {
        'keyword': 'Emerald',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Epigram': {
        'keyword': 'Epigram',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'EPL': {
        'keyword': 'EPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Erlang': {
        'keyword': 'Erlang',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'es': {
        'keyword': 'es',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Escher': {
        'keyword': 'Escher',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ESPOL': {
        'keyword': 'ESPOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Esterel': {
        'keyword': 'Esterel',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Etoys': {
        'keyword': 'Etoys',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Euclid': {
        'keyword': 'Euclid',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Euler': {
        'keyword': 'Euler',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Euphoria': {
        'keyword': 'Euphoria',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'EXEC': {
        'keyword': 'EXEC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'F': {
        'keyword': 'F',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'F#': {
        'keyword': 'F#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Factor': {
        'keyword': 'Factor',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Falcon': {
        'keyword': 'Falcon',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Fantom': {
        'keyword': 'Fantom',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FAUST': {
        'keyword': 'FAUST',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FFP': {
        'keyword': 'FFP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FL': {
        'keyword': 'FL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Flavors': {
        'keyword': 'Flavors',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FlooP': {
        'keyword': 'FlooP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FLOW-MATIC': {
        'keyword': 'FLOW-MATIC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FOCAL': {
        'keyword': 'FOCAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FOCUS': {
        'keyword': 'FOCUS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FOIL': {
        'keyword': 'FOIL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FORMAC': {
        'keyword': 'FORMAC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    '@Formula': {
        'keyword': '@Formula',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Forth': {
        'keyword': 'Forth',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Fortran': {
        'keyword': 'Fortran',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Fortress': {
        'keyword': 'Fortress',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FoxBase': {
        'keyword': 'FoxBase',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FoxPro': {
        'keyword': 'FoxPro',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FP': {
        'keyword': 'FP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'FPr': {
        'keyword': 'FPr',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Frege': {
        'keyword': 'Frege',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'F-Script': {
        'keyword': 'F-Script',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'G': {
        'keyword': 'G',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GAMS': {
        'keyword': 'GAMS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GAP': {
        'keyword': 'GAP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'G-code': {
        'keyword': 'G-code',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Genie': {
        'keyword': 'Genie',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GDL': {
        'keyword': 'GDL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GJ': {
        'keyword': 'GJ',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GEORGE': {
        'keyword': 'GEORGE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GLSL': {
        'keyword': 'GLSL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GM': {
        'keyword': 'GM',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Go': {
        'keyword': 'Go',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Golang': {
        'keyword': 'Go',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GOAL': {
        'keyword': 'GOAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Godiva': {
        'keyword': 'Godiva',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Golo': {
        'keyword': 'Golo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GOM': {
        'keyword': 'GOM',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Gosu': {
        'keyword': 'Gosu',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GOTRAN': {
        'keyword': 'GOTRAN',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GPSS': {
        'keyword': 'GPSS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GraphTalk': {
        'keyword': 'GraphTalk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'GRASS': {
        'keyword': 'GRASS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Groovy': {
        'keyword': 'Groovy',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'Hack': {
        'keyword': 'Hack',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['PHP']
    },
    'HAL/S': {
        'keyword': 'HAL/S',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Harbour': {
        'keyword': 'Harbour',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Haskell': {
        'keyword': 'Haskell',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Haxe': {
        'keyword': 'Haxe',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'HLSL': {
        'keyword': 'HLSL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Hop': {
        'keyword': 'Hop',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Hopscotch': {
        'keyword': 'Hopscotch',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Hope': {
        'keyword': 'Hope',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Hugo': {
        'keyword': 'Hugo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Hume': {
        'keyword': 'Hume',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'HyperTalk': {
        'keyword': 'HyperTalk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ICI': {
        'keyword': 'ICI',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Icon': {
        'keyword': 'Icon',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Id': {
        'keyword': 'Id',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'IDL': {
        'keyword': 'IDL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Idris': {
        'keyword': 'Idris',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'IMP': {
        'keyword': 'IMP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Inform': {
        'keyword': 'Inform',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Io': {
        'keyword': 'Io',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ioke': {
        'keyword': 'Ioke',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'IPL': {
        'keyword': 'IPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'IPTSCRAE': {
        'keyword': 'IPTSCRAE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ISLISP': {
        'keyword': 'ISLISP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ISPF': {
        'keyword': 'ISPF',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ISWIM': {
        'keyword': 'ISWIM',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'J': {
        'keyword': 'J',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'J#': {
        'keyword': 'J#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'J++': {
        'keyword': 'J++',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JADE': {
        'keyword': 'JADE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Jako': {
        'keyword': 'Jako',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JAL': {
        'keyword': 'JAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Janus': {
        'keyword': 'Janus',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JASS': {
        'keyword': 'JASS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Java': {
        'keyword': 'Java',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'J2EE': {
        'keyword': 'Java EE',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'JEE': {
        'keyword': 'Java EE',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'JavaScript': {
        'keyword': 'JavaScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JS': {
        'keyword': 'JavaScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ECMAScript6': {
        'keyword': 'ECMAScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ES6': {
        'keyword': 'ECMAScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ECMAScript7': {
        'keyword': 'ECMAScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ES7': {
        'keyword': 'ECMAScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JCL': {
        'keyword': 'JCL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JEAN': {
        'keyword': 'JEAN',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JOSS': {
        'keyword': 'JOSS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Joule': {
        'keyword': 'Joule',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JOVIAL': {
        'keyword': 'JOVIAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Joy': {
        'keyword': 'Joy',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JScript': {
        'keyword': 'JScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Julia': {
        'keyword': 'Julia',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Jython': {
        'keyword': 'Jython',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'K': {
        'keyword': 'K',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Kaleidoscope': {
        'keyword': 'Kaleidoscope',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Karel': {
        'keyword': 'Karel',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Karel++': {
        'keyword': 'Karel++',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'KEE': {
        'keyword': 'KEE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Kixtart': {
        'keyword': 'Kixtart',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'KIF': {
        'keyword': 'KIF',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Kojo': {
        'keyword': 'Kojo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Kotlin': {
        'keyword': 'Kotlin',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'KRC': {
        'keyword': 'KRC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'KRL': {
        'keyword': 'KRL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'KRYPTON': {
        'keyword': 'KRYPTON',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ksh': {
        'keyword': 'ksh',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LabVIEW': {
        'keyword': 'LabVIEW',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ladder': {
        'keyword': 'Ladder',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lagoona': {
        'keyword': 'Lagoona',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LANSA': {
        'keyword': 'LANSA',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lasso': {
        'keyword': 'Lasso',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LaTeX': {
        'keyword': 'LaTeX',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lava': {
        'keyword': 'Lava',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LC-3': {
        'keyword': 'LC-3',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Leda': {
        'keyword': 'Leda',
        'type': keyword_type.types['PROGRAMMING_LANG']

    },
    'Legoscript': {
        'keyword': 'Legoscript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LIL': {
        'keyword': 'LIL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LilyPond': {
        'keyword': 'LilyPond',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Limbo': {
        'keyword': 'Limbo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Limnor': {
        'keyword': 'Limnor',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LINC': {
        'keyword': 'LINC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lingo': {
        'keyword': 'Lingo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LIS': {
        'keyword': 'LIS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LISA': {
        'keyword': 'LISA',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lisaac': {
        'keyword': 'Lisaac',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lisp': {
        'keyword': 'Lisp',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lite-C': {
        'keyword': 'Lite-C',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lithe': {
        'keyword': 'Lithe',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Logo': {
        'keyword': 'Logo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Logtalk': {
        'keyword': 'Logtalk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LotusScript': {
        'keyword': 'LotusScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LPC': {
        'keyword': 'LPC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LSE': {
        'keyword': 'LSE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LSL': {
        'keyword': 'LSL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LiveScript': {
        'keyword': 'LiveScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lua': {
        'keyword': 'Lua',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lucid': {
        'keyword': 'Lucid',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lustre': {
        'keyword': 'Lustre',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LYaPAS': {
        'keyword': 'LYaPAS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Lynx': {
        'keyword': 'Lynx',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'M2001': {
        'keyword': 'M2001',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'M4': {
        'keyword': 'M4',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'M#': {
        'keyword': 'M#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MAD': {
        'keyword': 'MAD',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MAD/I': {
        'keyword': 'MAD/I',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Magik': {
        'keyword': 'Magik',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Magma': {
        'keyword': 'Magma',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Maple': {
        'keyword': 'Maple',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MAPPER': {
        'keyword': 'MAPPER',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MARK-IV': {
        'keyword': 'MARK-IV',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Mary': {
        'keyword': 'Mary',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MATH-MATIC': {
        'keyword': 'MATH-MATIC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Mathematica': {
        'keyword': 'Mathematica',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MATLAB': {
        'keyword': 'MATLAB',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Maxima': {
        'keyword': 'Maxima',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Macsyma': {
        'keyword': 'Macsyma',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Max': {
        'keyword': 'Max',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MDL': {
        'keyword': 'MDL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Mercury': {
        'keyword': 'Mercury',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Metafont': {
        'keyword': 'Metafont',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Microcode': {
        'keyword': 'Microcode',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MicroScript': {
        'keyword': 'MicroScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MIIS': {
        'keyword': 'MIIS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Milk': {
        'keyword': 'Milk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MIMIC': {
        'keyword': 'MIMIC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Mirah': {
        'keyword': 'Mirah',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Miranda': {
        'keyword': 'Miranda',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ML': {
        'keyword': 'ML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Modelica': {
        'keyword': 'Modelica',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Modula': {
        'keyword': 'Modula',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Modula-2': {
        'keyword': 'Modula-2',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Modula-3': {
        'keyword': 'Modula-3',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Mohol': {
        'keyword': 'Mohol',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MOO': {
        'keyword': 'MOO',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Mortran': {
        'keyword': 'Mortran',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Mouse': {
        'keyword': 'Mouse',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MPD': {
        'keyword': 'MPD',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Mathcad': {
        'keyword': 'Mathcad',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MSIL': {
        'keyword': 'MSIL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MSL': {
        'keyword': 'MSL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MUMPS': {
        'keyword': 'MUMPS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'MPL': {
        'keyword': 'MPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NASM': {
        'keyword': 'NASM',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Napier88': {
        'keyword': 'Napier88',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Neko': {
        'keyword': 'Neko',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Nemerle': {
        'keyword': 'Nemerle',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'nesC': {
        'keyword': 'nesC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NESL': {
        'keyword': 'NESL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Net.Data': {
        'keyword': 'Net.Data',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NetLogo': {
        'keyword': 'NetLogo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NetRexx': {
        'keyword': 'NetRexx',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NewLISP': {
        'keyword': 'NewLISP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NEWP': {
        'keyword': 'NEWP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Newspeak': {
        'keyword': 'Newspeak',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NewtonScript': {
        'keyword': 'NewtonScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NGL': {
        'keyword': 'NGL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Nial': {
        'keyword': 'Nial',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Nickle': {
        'keyword': 'Nickle',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Nim': {
        'keyword': 'Nim',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NO': {
        'keyword': 'NO',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NPL': {
        'keyword': 'NPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NSIS': {
        'keyword': 'NSIS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Nu': {
        'keyword': 'Nu',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NWScript': {
        'keyword': 'NWScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'NXT-G': {
        'keyword': 'NXT-G',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'o:XML': {
        'keyword': 'o:XML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Oak': {
        'keyword': 'Oak',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Oberon': {
        'keyword': 'Oberon',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'OBJ2': {
        'keyword': 'OBJ2',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ObjectLOGO': {
        'keyword': 'ObjectLOGO',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Xcode/Objective-C': {
        'keyword': 'Objective C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['iOS']
    },
    'Objective-C': {
        'keyword': 'Objective C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['iOS']
    },
    'Obj-C': {
        'keyword': 'Objective C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['iOS']
    },
    'ObjectiveC': {
        'keyword': 'Objective C',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['iOS']
    },
    'Objective-J': {
        'keyword': 'Objective J',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Obliq': {
        'keyword': 'Obliq',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'OCaml': {
        'keyword': 'OCaml',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'occam': {
        'keyword': 'occam',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Octave': {
        'keyword': 'Octave',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'OmniMark': {
        'keyword': 'OmniMark',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Onyx': {
        'keyword': 'Onyx',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Opa': {
        'keyword': 'Opa',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Opal': {
        'keyword': 'Opal',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'OpenCL': {
        'keyword': 'OpenCL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'OPL': {
        'keyword': 'OPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'OPS5': {
        'keyword': 'OPS5',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'OptimJ': {
        'keyword': 'OptimJ',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Orc': {
        'keyword': 'Orc',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ORCA/Modula-2': {
        'keyword': 'ORCA/Modula-2',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Oriel': {
        'keyword': 'Oriel',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Orwell': {
        'keyword': 'Orwell',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Oxygene': {
        'keyword': 'Oxygene',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Oz': {
        'keyword': 'Oz',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    "P''": {
        'keyword': 'P''',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'P#': {
        'keyword': 'P#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ParaSail': {
        'keyword': 'ParaSail',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PARI/GP': {
        'keyword': 'PARI/GP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Pascal': {
        'keyword': 'Pascal',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PCASTL': {
        'keyword': 'PCASTL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PCF': {
        'keyword': 'PCF',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PEARL': {
        'keyword': 'PEARL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PeopleCode': {
        'keyword': 'PeopleCode',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Perl': {
        'keyword': 'Perl',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Perl6': {
        'keyword': 'Perl',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PDL': {
        'keyword': 'PDL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Pharo': {
        'keyword': 'Pharo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PHP7': {
        'keyword': 'PHP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PHP': {
        'keyword': 'PHP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Phrogram': {
        'keyword': 'Phrogram',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Pico': {
        'keyword': 'Pico',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Picolisp': {
        'keyword': 'Picolisp',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Pict': {
        'keyword': 'Pict',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Pike': {
        'keyword': 'Pike',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PILOT': {
        'keyword': 'PILOT',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL/11': {
        'keyword': 'PL-11',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL-11': {
        'keyword': 'PL-11',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL/0': {
        'keyword': 'PL-0',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL-0': {
        'keyword': 'PL-0',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL/B': {
        'keyword': 'PL-B',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL-B': {
        'keyword': 'PL-B',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL/C': {
        'keyword': 'PL-C',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL-C': {
        'keyword': 'PL-C',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL/I': {
        'keyword': 'PL-I',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL-I': {
        'keyword': 'PL-I',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL/M': {
        'keyword': 'PL-M',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL-M': {
        'keyword': 'PL-M',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL/P': {
        'keyword': 'PL-P',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL-P': {
        'keyword': 'PL-P',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PL/SQL': {
        'keyword': 'PL-SQL',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['SQL']
    },
    'PL-SQL': {
        'keyword': 'PL-SQL',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['SQL']
    },
    'PL360': {
        'keyword': 'PL360',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PLANC': {
        'keyword': 'PLANC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Planner': {
        'keyword': 'Planner',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PLEX': {
        'keyword': 'PLEX',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PLEXIL': {
        'keyword': 'PLEXIL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'POP-11': {
        'keyword': 'POP-11',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PostScript': {
        'keyword': 'PostScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PortablE': {
        'keyword': 'PortablE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Powerhouse': {
        'keyword': 'Powerhouse',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PowerBuilder': {
        'keyword': 'PowerBuilder',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PowerShell': {
        'keyword': 'PowerShell',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Windows']
    },
    'PPL': {
        'keyword': 'PPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Processing': {
        'keyword': 'Processing',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Processing.js': {
        'keyword': 'Processing.js',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['JavaScript']
    },
    'Prograph': {
        'keyword': 'Prograph',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PROIV': {
        'keyword': 'PROIV',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Prolog': {
        'keyword': 'Prolog',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PROMAL': {
        'keyword': 'PROMAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Promela': {
        'keyword': 'Promela',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PROSE': {
        'keyword': 'PROSE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'PROTEL': {
        'keyword': 'PROTEL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ProvideX': {
        'keyword': 'ProvideX',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Pro*C': {
        'keyword': 'Pro*C',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Pure': {
        'keyword': 'Pure',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Python': {
        'keyword': 'Python',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Q': {
        'keyword': 'Q',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Qalb': {
        'keyword': 'Qalb',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'QtScript': {
        'keyword': 'QtScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'QuakeC': {
        'keyword': 'QuakeC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'QPL': {
        'keyword': 'QPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'R': {
        'keyword': 'R',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'R++': {
        'keyword': 'R++',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Racket': {
        'keyword': 'Racket',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'RAPID': {
        'keyword': 'RAPID',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Rapira': {
        'keyword': 'Rapira',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ratfiv': {
        'keyword': 'Ratfiv',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ratfor': {
        'keyword': 'Ratfor',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'rc': {
        'keyword': 'rc',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'REBOL': {
        'keyword': 'REBOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Red': {
        'keyword': 'Red',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Redcode': {
        'keyword': 'Redcode',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'REFAL': {
        'keyword': 'REFAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Reia': {
        'keyword': 'Reia',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'REXX': {
        'keyword': 'REXX',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Rlab': {
        'keyword': 'Rlab',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ROOP': {
        'keyword': 'ROOP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'RPG': {
        'keyword': 'RPG',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'RPL': {
        'keyword': 'RPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'RSL': {
        'keyword': 'RSL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'RTL/2': {
        'keyword': 'RTL/2',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Ruby': {
        'keyword': 'Ruby',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'JRuby': {
        'keyword': 'JRuby',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Ruby']
    },
    'RuneScript': {
        'keyword': 'RuneScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Rust': {
        'keyword': 'Rust',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'S': {
        'keyword': 'S',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'S2': {
        'keyword': 'S2',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'S-Lang': {
        'keyword': 'S-Lang',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'S-PLUS': {
        'keyword': 'S-PLUS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SA-C': {
        'keyword': 'SA-C',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SabreTalk': {
        'keyword': 'SabreTalk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SAIL': {
        'keyword': 'SAIL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SALSA': {
        'keyword': 'SALSA',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SAM76': {
        'keyword': 'SAM76',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SAS': {
        'keyword': 'SAS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SASL': {
        'keyword': 'SASL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Sather': {
        'keyword': 'Sather',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Sawzall': {
        'keyword': 'Sawzall',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SBL': {
        'keyword': 'SBL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Scala': {
        'keyword': 'Scala',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Java']
    },
    'Scheme': {
        'keyword': 'Scheme',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Scilab': {
        'keyword': 'Scilab',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Scratch': {
        'keyword': 'Scratch',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Script.NET': {
        'keyword': 'Script.NET',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Sed': {
        'keyword': 'Sed',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Seed7': {
        'keyword': 'Seed7',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Self': {
        'keyword': 'Self',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SenseTalk': {
        'keyword': 'SenseTalk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SequenceL': {
        'keyword': 'SequenceL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SETL': {
        'keyword': 'SETL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SIMPOL': {
        'keyword': 'SIMPOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SIGNAL': {
        'keyword': 'SIGNAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SiMPLE': {
        'keyword': 'SiMPLE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SIMSCRIPT': {
        'keyword': 'SIMSCRIPT',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Simula': {
        'keyword': 'Simula',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Simulink': {
        'keyword': 'Simulink',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SISAL': {
        'keyword': 'SISAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SLIP': {
        'keyword': 'SLIP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SMALL': {
        'keyword': 'SMALL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Smalltalk': {
        'keyword': 'Smalltalk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SML': {
        'keyword': 'SML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Snap!': {
        'keyword': 'Snap!',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SNOBOL': {
        'keyword': 'SNOBOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Snowball': {
        'keyword': 'Snowball',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SOL': {
        'keyword': 'SOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Span': {
        'keyword': 'Span',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Speedcode': {
        'keyword': 'Speedcode',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SPIN': {
        'keyword': 'SPIN',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SP/k': {
        'keyword': 'SP/k',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SPSS': {
        'keyword': 'SPSS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SPS': {
        'keyword': 'SPS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SQR': {
        'keyword': 'SQR',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Squeak': {
        'keyword': 'Squeak',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Squirrel': {
        'keyword': 'Squirrel',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SR': {
        'keyword': 'SR',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'S/SL': {
        'keyword': 'S/SL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Starlogo': {
        'keyword': 'Starlogo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Strand': {
        'keyword': 'Strand',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Stata': {
        'keyword': 'Stata',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Stateflow': {
        'keyword': 'Stateflow',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Subtext': {
        'keyword': 'Subtext',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SuperCollider': {
        'keyword': 'SuperCollider',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SuperTalk': {
        'keyword': 'SuperTalk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Swift': {
        'keyword': 'Swift',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['iOS']
    },
    'SYMPL': {
        'keyword': 'SYMPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SyncCharts': {
        'keyword': 'SyncCharts',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SystemVerilog': {
        'keyword': 'SystemVerilog',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TACL': {
        'keyword': 'TACL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TACPOL': {
        'keyword': 'TACPOL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TADS': {
        'keyword': 'TADS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TAL': {
        'keyword': 'TAL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Tcl/Tk': {
        'keyword': 'Tcl/Tk',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Tcl': {
        'keyword': 'Tcl',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Tea': {
        'keyword': 'Tea',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TECO': {
        'keyword': 'TECO',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TELCOMP': {
        'keyword': 'TELCOMP',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TeX': {
        'keyword': 'TeX',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TIE': {
        'keyword': 'TIE',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Timber': {
        'keyword': 'Timber',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TMG': {
        'keyword': 'TMG',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TOM': {
        'keyword': 'TOM',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TouchDevelop': {
        'keyword': 'TouchDevelop',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Topspeed': {
        'keyword': 'Topspeed',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TPU': {
        'keyword': 'TPU',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Trac': {
        'keyword': 'Trac',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TTM': {
        'keyword': 'TTM',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Transcript': {
        'keyword': 'Transcript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TTCN': {
        'keyword': 'TTCN',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Turing': {
        'keyword': 'Turing',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TUTOR': {
        'keyword': 'TUTOR',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TXL': {
        'keyword': 'TXL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'TypeScript': {
        'keyword': 'TypeScript',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['JavaScript']
    },
    'Ubercode': {
        'keyword': 'Ubercode',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Umple': {
        'keyword': 'Umple',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Unicon': {
        'keyword': 'Unicon',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Uniface': {
        'keyword': 'Uniface',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Unity': {
        'keyword': 'Unity',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Shell': {
        'keyword': 'Shell',
        'type': keyword_type.types['PROGRAMMING_LANG'],
        'extra': ['Unix']
    },
    'UnrealScript': {
        'keyword': 'UnrealScript',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Vala': {
        'keyword': 'Vala',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'VB': {
        'keyword': 'Visual Basic',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'VBA': {
        'keyword': 'Visual Basic for Applications',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'VB.NET': {
        'keyword': 'Visual Basic .NET',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'VSXu': {
        'keyword': 'VSXu',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'vvvv': {
        'keyword': 'vvvv',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'WebDNA': {
        'keyword': 'WebDNA',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'WebQL': {
        'keyword': 'WebQL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Whiley': {
        'keyword': 'Whiley',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Winbatch': {
        'keyword': 'Winbatch',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Wolfram': {
        'keyword': 'Wolfram',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Wyvern': {
        'keyword': 'Wyvern',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'X++': {
        'keyword': 'X++',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'X#': {
        'keyword': 'X#',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'X10': {
        'keyword': 'X10',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XBL': {
        'keyword': 'XBL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XC': {
        'keyword': 'XC',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'xHarbour': {
        'keyword': 'xHarbour',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XL': {
        'keyword': 'XL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Xojo': {
        'keyword': 'Xojo',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XOTcl': {
        'keyword': 'XOTcl',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XPL': {
        'keyword': 'XPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XPL0': {
        'keyword': 'XPL0',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XQuery': {
        'keyword': 'XQuery',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XSB': {
        'keyword': 'XSB',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XSLT': {
        'keyword': 'XSLT',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Xtend': {
        'keyword': 'Xtend',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Yorick': {
        'keyword': 'Yorick',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'YQL': {
        'keyword': 'YQL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Zeno': {
        'keyword': 'Zeno',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ZOPL': {
        'keyword': 'ZOPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'Zsh': {
        'keyword': 'Zsh',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'ZPL': {
        'keyword': 'ZPL',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'HTML/XHTML': {
        'keyword': 'XHTML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'XHTML': {
        'keyword': 'XHTML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'HTML/DHTML': {
        'keyword': 'DHTML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'DHTML': {
        'keyword': 'DHTML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'HTML': {
        'keyword': 'HTML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CSS': {
        'keyword': 'CSS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'HTML5': {
        'keyword': 'HTML',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CSS/CSS3': {
        'keyword': 'CSS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'CSS3': {
        'keyword': 'CSS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'LESS': {
        'keyword': 'LESS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SASS': {
        'keyword': 'SASS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    'SCSS': {
        'keyword': 'SCSS',
        'type': keyword_type.types['PROGRAMMING_LANG']
    },
    # List of database types
    'SQL': {
        'keyword': 'SQL',
        'type': keyword_type.types['DB_TYPE']
    },
    'NoSQL': {
        'keyword': 'NoSQL',
        'type': keyword_type.types['DB_TYPE']
    },
    'NewSQL': {
        'keyword': 'NewSQL',
        'type': keyword_type.types['DB_TYPE']
    },
    # List of mobile frameworks
    'Cordova': {
        'keyword': 'Apache Cordova',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Monaca': {
        'keyword': 'Monaca',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'JavaScript', 'Android', 'iOS'],
    },
    'Crosswalk': {
        'keyword': 'Crosswalk Project',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS'],
    },
    'Enyo': {
        'keyword': 'Enyo',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS'],
    },
    'iPFaces': {
        'keyword': 'iPFaces',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['PHP', 'ASP.NET', 'Java', 'Android', 'iOS'],
    },
    'iUI': {
        'keyword': 'iUI',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS'],
    },
    'Jembe': {
        'keyword': 'Jembe',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS'],
    },
    'Jmango360': {
        'keyword': 'Jmango360',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['Android', 'iOS']
    },
    'Kivy': {
        'keyword': 'Kivy',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['Python']
    },
    'MoSync': {
        'keyword': 'MoSync',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['C/C++', 'HTML', 'CSS', 'JavaScript', 'Android', 'iOS']
    },
    'Rhodes': {
        'keyword': 'RhoMobile',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'Ruby', 'JavaScript', 'Android', 'iOS']
    },
    'RhoMobile': {
        'keyword': 'RhoMobile',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'Ruby', 'JavaScript', 'Android', 'iOS']
    },
    'Sencha': {
        'keyword': 'Sencha Touch',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS']
    },
    'Ionic': {
        'keyword': 'Ionic',
        'type': keyword_type.types['MOBILE_FRWK'],
        'extra': ['HTML', 'CSS', 'JavaScript', 'Android', 'iOS']
    },
    # List of mobile operating systems
    'Android': {
        'keyword': 'Android',
        'type': keyword_type.types['MOBILE_OS']
    },
    'iOS': {
        'keyword': 'iOS',
        'type': keyword_type.types['MOBILE_OS']
    },
    'iPhone': {
        'keyword': 'iOS',
        'type': keyword_type.types['MOBILE_OS']
    },
    'Blackberry': {
        'keyword': 'Blackberry OS',
        'type': keyword_type.types['MOBILE_OS']
    },
    # List of operating systems
    'Unix': {
        'keyword': 'Unix',
        'type': keyword_type.types['OS']
    },
    'BSD': {
        'keyword': 'BSD',
        'type': keyword_type.types['OS'],
        'extra': ['Unix']
    },
    'FreeBSD': {
        'keyword': 'FreeBSD',
        'type': keyword_type.types['OS'],
        'extra': ['BSD']
    },
    'Unix/Linux': {
        'keyword': 'Unix',
        'type': keyword_type.types['OS']
    },
    'Linux': {
        'keyword': 'Linux',
        'type': keyword_type.types['OS'],
        'extra': ['Unix']
    },
    'Linux/Unix': {
        'keyword': 'Linux',
        'type': keyword_type.types['OS'],
        'extra': ['Unix']
    },
    'Solaris': {
        'keyword': 'Solaris',
        'type': keyword_type.types['OS'],
        'extra': ['Unix']
    },
    'CentOS': {
        'keyword': 'CentOS',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Fedora': {
        'keyword': 'Fedora',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Debian': {
        'keyword': 'Fedora',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'openSUSE': {
        'keyword': 'openSUSE',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Mageia': {
        'keyword': 'Mageia',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Manjaro': {
        'keyword': 'Manjaro',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Ubuntu': {
        'keyword': 'Ubuntu',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'RHEL': {
        'keyword': 'RedHat Linux',
        'type': keyword_type.types['OS'],
        'extra': ['Linux']
    },
    'Windows': {
        'keyword': 'Windows',
        'type': keyword_type.types['OS']
    },
    'OSX': {
        'keyword': 'OS X',
        'type': keyword_type.types['OS']
    },
    'Mac': {
        'keyword': 'OS X',
        'type': keyword_type.types['OS']
    },
    'MacOS': {
        'keyword': 'OS X',
        'type': keyword_type.types['OS']
    },
    # List of web servers
    'AOLserver': {
        'keyword': 'AOLserver',
        'type': keyword_type.types['WEB_SRV']
    },
    'Tomcat': {
        'keyword': 'Apache Tomcat',
        'type': keyword_type.types['WEB_SRV'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Boa': {
        'keyword': 'Boa',
        'type': keyword_type.types['WEB_SRV']
    },
    'Caddy': {
        'keyword': 'Caddy',
        'type': keyword_type.types['WEB_SRV']
    },
    'Resin': {
        'keyword': 'Resin',
        'type': keyword_type.types['WEB_SRV']
    },
    'Caudium': {
        'keyword': 'Caudium',
        'type': keyword_type.types['WEB_SRV']
    },
    'HFS': {
        'keyword': 'HFS',
        'type': keyword_type.types['WEB_SRV']
    },
    'GlassFish': {
        'keyword': 'GlassFish',
        'type': keyword_type.types['WEB_SRV']
    },
    'Hiawatha': {
        'keyword': 'Hiawatha',
        'type': keyword_type.types['WEB_SRV']
    },
    'IIS': {
        'keyword': 'IIS',
        'type': keyword_type.types['WEB_SRV']
    },
    'Jetty': {
        'keyword': 'Jetty',
        'type': keyword_type.types['WEB_SRV']
    },
    'Jexus': {
        'keyword': 'Jexus',
        'type': keyword_type.types['WEB_SRV']
    },
    'lighttpd': {
        'keyword': 'lighttpd',
        'type': keyword_type.types['WEB_SRV']
    },
    'Mongoose': {
        'keyword': 'Mongoose',
        'type': keyword_type.types['WEB_SRV']
    },
    'NaviServer': {
        'keyword': 'NaviServer',
        'type': keyword_type.types['WEB_SRV']
    },
    'Nginx': {
        'keyword': 'Nginx',
        'type': keyword_type.types['WEB_SRV']
    },
    'thttpd': {
        'keyword': 'thttpd',
        'type': keyword_type.types['WEB_SRV']
    },
    'Xitami': {
        'keyword': 'Xitami',
        'type': keyword_type.types['WEB_SRV']
    },
    'Yaws': {
        'keyword': 'Yaws',
        'type': keyword_type.types['WEB_SRV']
    },
    'Geronimo': {
        'keyword': 'Apache Geronimo',
        'type': keyword_type.types['WEB_SRV'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'JBoss': {
        'keyword': 'JBoss EAP',
        'type': keyword_type.types['WEB_SRV']
    },
    'OpenLiteSpeed': {
        'keyword': 'OpenLiteSpeed',
        'type': keyword_type.types['WEB_SRV']
    },
    'WEBrick': {
        'keyword': 'WEBrick',
        'type': keyword_type.types['WEB_SRV']
    },
    # List of search servers
    'Lucene': {
        'keyword': 'Apache Lucene',
        'type': keyword_type.types['SEARCH_SRV'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Lucene/Solr': {
        'keyword': 'Apache Solr',
        'type': keyword_type.types['SEARCH_SRV'],
        'type_extra': [keyword_type.types['APACHE_FRWK']],
        'extra': ['Lucene']
    },
    'Solr/Lucene': {
        'keyword': 'Apache Solr',
        'type': keyword_type.types['SEARCH_SRV'],
        'type_extra': [keyword_type.types['APACHE_FRWK']],
        'extra': ['Lucene']
    },
    'Solr': {
        'keyword': 'Apache Solr',
        'type': keyword_type.types['SEARCH_SRV'],
        'type_extra': [keyword_type.types['APACHE_FRWK']],
        'extra': ['Lucene']
    },
    'Elasticsearch': {
        'keyword': 'Elasticsearch',
        'type': keyword_type.types['SEARCH_SRV'],
        'extra': ['Lucene']
    },
    'Splunk': {
        'keyword': 'Splunk',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Gigablast': {
        'keyword': 'Gigablast',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Grub': {
        'keyword': 'Grub',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Isearch': {
        'keyword': 'Isearch',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'mnoGoSearch': {
        'keyword': 'mnoGoSearch',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Namazu': {
        'keyword': 'Namazu',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Nutch': {
        'keyword': 'Nutch',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Recoll': {
        'keyword': 'Recoll',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Searchdaimon': {
        'keyword': 'Searchdaimon',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Seeks': {
        'keyword': 'Seeks',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Sphinx': {
        'keyword': 'Sphinx',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'SWISH-E': {
        'keyword': 'SWISH-E',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Xapian': {
        'keyword': 'Xapian',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'YaCy': {
        'keyword': 'YaCy',
        'type': keyword_type.types['SEARCH_SRV']
    },
    'Zettair': {
        'keyword': 'Zettair',
        'type': keyword_type.types['SEARCH_SRV']
    },
    # List of data structure servers
    'Redis': {
        'keyword': 'Redis',
        'type': keyword_type.types['DATA_STRUCT_SRV']
    },
    'Memcached': {
        'keyword': 'Memcached',
        'type': keyword_type.types['DATA_STRUCT_SRV']
    },
    'NCache': {
        'keyword': 'NCache',
        'type': keyword_type.types['DATA_STRUCT_SRV']
    },
    # List of web frameworks
    # .NET web frameworks
    'ASP.NET': {
        'keyword': 'ASP.NET',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['.NET']
    },
    'ASP': {
        'keyword': 'ASP.NET',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['.NET']
    },
    # C++ web frameworks
    'CppCMS': {
        'keyword': 'CppCMS',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['C++']
    },
    'Tntnet': {
        'keyword': 'Tntnet',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['C++']
    },
    'Wt': {
        'keyword': 'Wt',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['C++']
    },
    # ColdFusion web frameworks
    'ColdBox': {
        'keyword': 'ColdBox',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['ColdFusion']
    },
    'Mach-II': {
        'keyword': 'Mach-II',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['ColdFusion']
    },
    'Model-Glue': {
        'keyword': 'Model-Glue',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['ColdFusion']
    },
    # Groovy web frameworks
    'Groovy/Grails': {
        'keyword': 'Groovy on Grails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Groovy']
    },
    'Grails/Groovy': {
        'keyword': 'Groovy on Grails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Groovy']
    },
    'Groovy-on-Grails': {
        'keyword': 'Groovy on Grails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Groovy']
    },
    'Grails': {
        'keyword': 'Groovy on Grails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Groovy']
    },
    # Java web frameworks
    'Click': {
        'keyword': 'Apache Click',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'OFBiz': {
        'keyword': 'Apache OFBiz',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Sling': {
        'keyword': 'Apache Sling',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Struts': {
        'keyword': 'Apache Struts',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Tapestry': {
        'keyword': 'Apache Tapestry',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Wicket': {
        'keyword': 'Apache Wicket',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'FormEngine': {
        'keyword': 'FormEngine',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'ItsNat': {
        'keyword': 'ItsNat',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Jspx-bay': {
        'keyword': 'Jspx-bay',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'JVx': {
        'keyword': 'JVx',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'OpenXava': {
        'keyword': 'JVx',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Play': {
        'keyword': 'Play Framework',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java', 'Scala']
    },
    'RIFE': {
        'keyword': 'RIFE',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Spring': {
        'keyword': 'Spring Framework',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Stripes': {
        'keyword': 'Stripes',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Vaadin': {
        'keyword': 'Vaadin',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'Wavemaker': {
        'keyword': 'Wavemaker',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'WebObjects': {
        'keyword': 'WebObjects',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'ztemplates': {
        'keyword': 'ztemplates',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    'ZK': {
        'keyword': 'ZK',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Java']
    },
    # Lua web frameworks
    'Kepler': {
        'keyword': 'Kepler',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Lua']
    },
    # PHP web frameworks
    'Banshee': {
        'keyword': 'Banshee',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'CakePHP': {
        'keyword': 'CakePHP',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'CodeIgniter': {
        'keyword': 'CodeIgniter',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Drupal': {
        'keyword': 'Drupal',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Fat-Free': {
        'keyword': 'Fat-Free Framework',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'FuelPHP': {
        'keyword': 'FuelPHP',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Fusebox': {
        'keyword': 'Fusebox',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Joomla': {
        'keyword': 'Joomla',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Kajona': {
        'keyword': 'Kajona',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Laravel': {
        'keyword': 'Laravel',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Lithium': {
        'keyword': 'Lithium',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Nette': {
        'keyword': 'Nette Framework',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Phalcon': {
        'keyword': 'Phalcon',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'PRADO': {
        'keyword': 'PRADO',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'SilverStripe': {
        'keyword': 'SilverStripe',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Silex': {
        'keyword': 'Silex',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Smart.Framework': {
        'keyword': 'Smart.Framework',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Symfony': {
        'keyword': 'Symfony',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'TYPO3': {
        'keyword': 'TYPO3',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Yii': {
        'keyword': 'Yii',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'Zend Framework': {
        'keyword': 'Zend Framework',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    'PHPixie': {
        'keyword': 'PHPixie',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['PHP']
    },
    # Ruby web frameworks
    'Camping': {
        'keyword': 'Camping',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Ruby-on-Rails': {
        'keyword': 'Ruby on Rails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Ruby/Ror': {
        'keyword': 'Ruby on Rails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Ruby/Rails': {
        'keyword': 'Ruby on Rails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Rails/Ruby': {
        'keyword': 'Ruby on Rails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Rails': {
        'keyword': 'Ruby on Rails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Rails3': {
        'keyword': 'Ruby on Rails',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    'Sinatra': {
        'keyword': 'Sinatra',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Ruby']
    },
    # Python web frameworks
    'Bottle': {
        'keyword': 'Bottle',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'CherryPy': {
        'keyword': 'CherryPy',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Python/Django': {
        'keyword': 'Django',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Django': {
        'keyword': 'Django',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Python/Flask': {
        'keyword': 'Flask',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Flask': {
        'keyword': 'Flask',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Pyjs': {
        'keyword': 'Pyjs',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Pylons': {
        'keyword': 'Pylons',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Pyramid': {
        'keyword': 'Pyramid',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'TACTIC': {
        'keyword': 'TACTIC',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Tornado': {
        'keyword': 'Tornado',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'TurboGears': {
        'keyword': 'TurboGears',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'web2py': {
        'keyword': 'web2py',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Webware': {
        'keyword': 'Webware',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'BlueBream': {
        'keyword': 'BlueBream',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    'Zope': {
        'keyword': 'Zope',
        'type': keyword_type.types['WEB_FRWK'],
        'extra': ['Python']
    },
    # List of apache frameworks
    'Abdera': {
        'keyword': 'Apache Abdera',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Allura': {
        'keyword': 'Apache Allura',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'APR': {
        'keyword': 'Apache APR',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Archiva': {
        'keyword': 'Apache Archiva',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Beam': {
        'keyword': 'Apache Beam',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Beehive': {
        'keyword': 'Apache Beehive',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Bloodhound': {
        'keyword': 'Apache Bloodhound',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Calcite': {
        'keyword': 'Apache Calcite',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Camel': {
        'keyword': 'Apache Camel',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Celix': {
        'keyword': 'Apache Celix',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'CloudStack': {
        'keyword': 'Apache CloudStack',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Cocoon': {
        'keyword': 'Apache Cocoon',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Commons': {
        'keyword': 'Apache Commons',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'cTAKES': {
        'keyword': 'Apache cTAKES',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Curator': {
        'keyword': 'Apache Curator',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'CXF': {
        'keyword': 'Apache CXF',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Cayenne': {
        'keyword': 'Apache Cayenne',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'JDO': {
        'keyword': 'Apache JDO',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Torque': {
        'keyword': 'Apache Torque',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Excalibur': {
        'keyword': 'Apache Excalibur',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Felix': {
        'keyword': 'Apache Felix',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Flex': {
        'keyword': 'Apache Flex',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Flink': {
        'keyword': 'Apache Flink',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Forrest': {
        'keyword': 'Apache Forrest',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Flume': {
        'keyword': 'Apache Flume',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Giraph': {
        'keyword': 'Apache Giraph',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Hive': {
        'keyword': 'Apache Hive',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'HiveMind': {
        'keyword': 'Apache HiveMind',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'iBATIS': {
        'keyword': 'Apache iBATIS',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Jackrabbit': {
        'keyword': 'Apache Jackrabbit',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Jakarta': {
        'keyword': 'Apache Jakarta',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'James': {
        'keyword': 'Apache James',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'jclouds': {
        'keyword': 'Apache jclouds',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Kylin': {
        'keyword': 'Apache Kylin',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Lenya': {
        'keyword': 'Apache Lenya',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'log4j': {
        'keyword': 'Apache log4j',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Lucy': {
        'keyword': 'Apache Lucy',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Mahout': {
        'keyword': 'Apache Mahout',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Marmotta': {
        'keyword': 'Apache Marmotta',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'MINA': {
        'keyword': 'Apache MINA',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'MyFaces': {
        'keyword': 'Apache MyFaces',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Olingo': {
        'keyword': 'Apache Olingo',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'OODT': {
        'keyword': 'Apache OODT',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Oozie': {
        'keyword': 'Apache Oozie',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'OpenJPA': {
        'keyword': 'Apache OpenJPA',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'OpenNLP': {
        'keyword': 'Apache OpenNLP',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'OpenOffice': {
        'keyword': 'Apache OpenOffice',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'PDFBox': {
        'keyword': 'Apache PDFBox',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Pivot': {
        'keyword': 'Apache Pivot',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'POI': {
        'keyword': 'Apache POI',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Portals': {
        'keyword': 'Apache Portals',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Samza': {
        'keyword': 'Apache Samza',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Santuario': {
        'keyword': 'Apache Santuario',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'ServiceMix': {
        'keyword': 'Apache ServiceMix',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Shale': {
        'keyword': 'Apache Shale',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Singa': {
        'keyword': 'Apache Singa',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'SpamAssassin': {
        'keyword': 'Apache SpamAssassin',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Spark': {
        'keyword': 'Apache Spark',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Stanbol': {
        'keyword': 'Apache Stanbol',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Stonehenge': {
        'keyword': 'Apache Stonehenge',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Stratos': {
        'keyword': 'Apache Stratos',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Tajo': {
        'keyword': 'Apache Tajo',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Tika': {
        'keyword': 'Apache Tika',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'UIMA': {
        'keyword': 'Apache UIMA',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Velocity': {
        'keyword': 'Apache Velocity',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Wave': {
        'keyword': 'Apache Wave',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Axis': {
        'keyword': 'Apache Axis',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Muse': {
        'keyword': 'Apache Muse',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Rampart': {
        'keyword': 'Apache Rampart',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Tuscany': {
        'keyword': 'Apache Tuscany',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Xalan': {
        'keyword': 'Apache Xalan',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Xerces': {
        'keyword': 'Apache Xerces',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'XMLBeans': {
        'keyword': 'Apache XMLBeans',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Batik': {
        'keyword': 'Apache Batik',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'FOP': {
        'keyword': 'Apache FOP',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Zest': {
        'keyword': 'Apache Zest',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Zookeeper': {
        'keyword': 'Apache Zookeeper',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Storm': {
        'keyword': 'Apache Storm',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Thrift': {
        'keyword': 'Apache Thrift',
        'type': keyword_type.types['APACHE_FRWK']
    },
    'Pig': {
        'keyword': 'Apache Pig',
        'type': keyword_type.types['APACHE_FRWK']
    },
    # List of version control systems
    'Subversion': {
        'keyword': 'Apache Subversion',
        'type': keyword_type.types['VC'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'SVN': {
        'keyword': 'Apache Subversion',
        'type': keyword_type.types['VC'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Git': {
        'keyword': 'Git',
        'type': keyword_type.types['VC']
    },
    'P4': {
        'keyword': 'Perforce',
        'type': keyword_type.types['VC']
    },
    'Perforce': {
        'keyword': 'Perforce',
        'type': keyword_type.types['VC']
    },
    'CVS': {
        'keyword': 'CVS',
        'type': keyword_type.types['VC']
    },
    'Mercurial': {
        'keyword': 'Mercurial',
        'type': keyword_type.types['VC']
    },
    # List of build automation server
    'A-A-P': {
        'keyword': 'A-A-P',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['C']
    },
    'Ant': {
        'keyword': 'Apache Ant',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'BuildAMation': {
        'keyword': 'BuildAMation',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Buildr': {
        'keyword': 'Apache Buildr',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Boot': {
        'keyword': 'Boot',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Clojure', 'Java'],
    },
    'Capistrano': {
        'keyword': 'Capistrano',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Ruby']
    },
    'CMake': {
        'keyword': 'CMake',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'ElectricCommander': {
        'keyword': 'ElectricCommander',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'FinalBuilder': {
        'keyword': 'FinalBuilder',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Gradle': {
        'keyword': 'Gradle',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Leiningen': {
        'keyword': 'Leiningen',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Clojure', 'Java'],
    },
    'Make': {
        'keyword': 'Make',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Makefile': {
        'keyword': 'Make',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Makefiles': {
        'keyword': 'Make',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Maven': {
        'keyword': 'Apache Maven',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Java'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'MSBuild': {
        'keyword': 'MSBuild',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'NAnt': {
        'keyword': 'NAnt',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['.NET']
    },
    'NMake': {
        'keyword': 'NMake',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Rake': {
        'keyword': 'Rake',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Ruby']
    },
    'sbt': {
        'keyword': 'sbt',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Scala']
    },
    'SCons': {
        'keyword': 'SCons',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'ASDF': {
        'keyword': 'ASDF',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Lisp']
    },
    'Brazel': {
        'keyword': 'Brazel',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'BitBake': {
        'keyword': 'BitBake',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Buck': {
        'keyword': 'Buck',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Cabal': {
        'keyword': 'Cabal',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['Haskell']
    },
    'Flowtracer': {
        'keyword': 'Flowtracer',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'IncrediBuild': {
        'keyword': 'IncrediBuild',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Psake': {
        'keyword': 'Psake',
        'type': keyword_type.types['BUILD_AUTO_TOOL'],
        'extra': ['PowerShell']
    },
    'Tweaker': {
        'keyword': 'Tweaker',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    'Waf': {
        'keyword': 'Waf',
        'type': keyword_type.types['BUILD_AUTO_TOOL']
    },
    # List of continuous integration tools
    'AnthillPro': {
        'keyword': 'AnthillPro',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Continuum': {
        'keyword': 'Apache Continuum',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL'],
        'extra_type': [keyword_type.types['APACHE_FRWK']]
    },
    'Gump': {
        'keyword': 'Apache Gump',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL'],
        'extra_type': [keyword_type.types['APACHE_FRWK']]
    },
    'AppVeyor': {
        'keyword': 'AppVeyor',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Assertible': {
        'keyword': 'Assertible',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Bamboo': {
        'keyword': 'Bamboo',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Buildbot': {
        'keyword': 'Buildbot',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Buddy': {
        'keyword': 'Buddy',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'BuildMaster': {
        'keyword': 'BuildMaster',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'CABIE': {
        'keyword': 'CABIE',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'CircleCI': {
        'keyword': 'CircleCI',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Codeship': {
        'keyword': 'Codeship',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Concourse': {
        'keyword': 'Concourse',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'continuousphp': {
        'keyword': 'continuousphp',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'CruiseControl.NET': {
        'keyword': 'CruiseControl.NET',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Dockunit': {
        'keyword': 'Dockunit',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Drone.io': {
        'keyword': 'Drone.io',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'easyCIS': {
        'keyword': 'easyCIS',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'GoCD': {
        'keyword': 'GoCD',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Harrow': {
        'keyword': 'Harrow',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Integrity': {
        'keyword': 'Integrity',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Hudson': {
        'keyword': 'Hudson',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Jenkins': {
        'keyword': 'Jenkins',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'LuntBuild': {
        'keyword': 'LuntBuild',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Lordui': {
        'keyword': 'Lordui',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'NCI': {
        'keyword': 'NCI',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Probo.CI': {
        'keyword': 'Probo.CI',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'QuickBuild': {
        'keyword': 'QuickBuild',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Semaphore': {
        'keyword': 'Semaphore',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Shippable': {
        'keyword': 'Shippable',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Strider': {
        'keyword': 'Strider',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'TeamCity': {
        'keyword': 'TeamCity',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'Buildout': {
        'keyword': 'Buildout',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'CruiseControl': {
        'keyword': 'CruiseControl',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    'DeployBot': {
        'keyword': 'DeployBot',
        'type': keyword_type.types['CONT_INTEGRATION_TOOL']
    },
    # List of configuration management tools
    'Ansible': {
        'keyword': 'Ansible',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Bcfg2': {
        'keyword': 'Bcfg2',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'cdist': {
        'keyword': 'cdist',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Chef': {
        'keyword': 'Chef',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'CFEngine': {
        'keyword': 'CFEngine',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'ISconf': {
        'keyword': 'ISconf',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Juju': {
        'keyword': 'Juju',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'PIKT': {
        'keyword': 'PIKT',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Puppet': {
        'keyword': 'Puppet',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Quattor': {
        'keyword': 'Quattor',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Radmind': {
        'keyword': 'Radmind',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Rex': {
        'keyword': 'Rex',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Rudder': {
        'keyword': 'Rudder',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'SmartFrog': {
        'keyword': 'SmartFrog',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Salt': {
        'keyword': 'Salt',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Spacewalk': {
        'keyword': 'Spacewalk',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'STAF': {
        'keyword': 'STAF',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    'Synctool': {
        'keyword': 'Synctool',
        'type': keyword_type.types['CONF_MANAGE_TOOL']
    },
    # List of VM environments
    'Vagrant': {
        'keyword': 'Vagrant',
        'type': keyword_type.types['VM_ENV']
    },
    'VMWare': {
        'keyword': 'VMWare',
        'type': keyword_type.types['VM_ENV']
    },
    'Hyper-V': {
        'keyword': 'Hyper-V',
        'type': keyword_type.types['VM_ENV']
    },
    'VirtualBox': {
        'keyword': 'VirtualBox',
        'type': keyword_type.types['VM_ENV']
    },
    'Docker': {
        'keyword': 'Docker',
        'type': keyword_type.types['VM_ENV']
    },
    # List of databases
    'Arrow': {
        'keyword': 'Apache Arrow',
        'type': keyword_type.types['DB'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Derby': {
        'keyword': 'Apache Derby',
        'type': keyword_type.types['DB'],
        'extra': ['SQL'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'CSQL': {
        'keyword': 'CSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'CUBRID': {
        'keyword': 'CUBRID',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'DataEase': {
        'keyword': 'DataEase',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Dataphor': {
        'keyword': 'Dataphor',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'dBase': {
        'keyword': 'dBase',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'EXASolution': {
        'keyword': 'EXASolution',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'EnterpriseDB': {
        'keyword': 'EnterpriseDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'eXtremeDB': {
        'keyword': 'eXtremeDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Firebird': {
        'keyword': 'Firebird',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'FrontBase': {
        'keyword': 'FrontBase',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Greenplum': {
        'keyword': 'Greenplum',
        'type': keyword_type.types['DB'],
        'extra': ['PostgreSQL']
    },
    'GroveSite': {
        'keyword': 'GroveSite',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'H2': {
        'keyword': 'H2',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'HSQLDB': {
        'keyword': 'HSQLDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'DB2': {
        'keyword': 'IBM DB2',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Infobright': {
        'keyword': 'Infobright',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Informix': {
        'keyword': 'Informix',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Ingres': {
        'keyword': 'Ingres',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'InterBase': {
        'keyword': 'InterBase',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'GT.M': {
        'keyword': 'GT.M',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Linter': {
        'keyword': 'Linter',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'MariaDB': {
        'keyword': 'MariaDB',
        'type': keyword_type.types['DB'],
        'extra': ['MySQL', 'SQL']
    },
    'MySQL/MariaDB': {
        'keyword': 'MySQL',
        'type': keyword_type.types['DB'],
        'extra': ['MariaDB', 'SQL']
    },
    'MariaDB/MySQL': {
        'keyword': 'MariaDB',
        'type': keyword_type.types['DB'],
        'extra': ['MySQL', 'SQL']
    },
    'MaxDB': {
        'keyword': 'MaxDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'MSSQL': {
        'keyword': 'MSSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'MonetDB': {
        'keyword': 'MonetDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'mSQL': {
        'keyword': 'mSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'MySQL': {
        'keyword': 'MySQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Netezza': {
        'keyword': 'Netezza',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'NexusDB': {
        'keyword': 'NexusDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Openbase': {
        'keyword': 'Openbase',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Oracle': {
        'keyword': 'Oracle',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Panorama': {
        'keyword': 'Panorama',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Polyhedra': {
        'keyword': 'Polyhedra',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'PostgreSQL': {
        'keyword': 'PostgreSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Postgres': {
        'keyword': 'PostgreSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'R:Base': {
        'keyword': 'R:Base',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Sybase': {
        'keyword': 'SAP Sybase',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'ScimoreDB': {
        'keyword': 'ScimoreDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SmallSQL': {
        'keyword': 'SmallSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'solidDB': {
        'keyword': 'solidDB',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SQLBase': {
        'keyword': 'SQLBase',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'SQLite': {
        'keyword': 'SQLite',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Teradata': {
        'keyword': 'Teradata',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Tibero': {
        'keyword': 'Tibero',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'TimesTen': {
        'keyword': 'TimesTen',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'txtSQL': {
        'keyword': 'txtSQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'UniData': {
        'keyword': 'UniData',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'UniVerse': {
        'keyword': 'UniVerse',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Vectorwise': {
        'keyword': 'Vectorwise',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Vertica': {
        'keyword': 'Vertica',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'VMDS': {
        'keyword': 'VMDS',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'TSQL': {
        'keyword': 'T-SQL',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'T-SQL': {
       'keyword': 'T-SQL',
       'type': keyword_type.types['DB'],
       'extra': ['SQL']
    },
    'Presto': {
        'keyword': 'Presto',
        'type': keyword_type.types['DB'],
        'extra': ['SQL']
    },
    'Phoenix': {
        'keyword': 'Apache Phoenix',
        'type': keyword_type.types['DB'],
        'extra': ['SQL', 'HBase'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Hypertable': {
        'keyword': 'Hypertable',
        'type': keyword_type.types['DB']
    },
    'RCFile': {
        'keyword': 'RCFile',
        'type': keyword_type.types['DB']
    },
    'Clickhouse': {
        'keyword': 'Clickhouse',
        'type': keyword_type.types['DB']
    },
    'Amazon SimpleDB': {
        'keyword': 'Amazon SimpleDB',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL'],
        'extra_type': [keyword_type.types['AWS_PRODUCT']]
    },
    'CratelO': {
        'keyword': 'CratelO',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'DocumentDB': {
        'keyword': 'DocumentDB',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'HyperDex': {
        'keyword': 'HyperDex',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'MongoDB': {
        'keyword': 'MongoDB',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Mongo': {
        'keyword': 'MongoDB',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'RethinkDB': {
        'keyword': 'RethinkDB',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'SciDB': {
        'keyword': 'SciDB',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Tarantool': {
        'keyword': 'Tarantool',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Aerospike': {
        'keyword': 'Aerospike',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Accumulo': {
        'keyword': 'Apache Accumulo',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Hadoop': {
        'keyword': 'Apache Hadoop',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL'],
        'extra_type': [keyword_type.types['APACHE_FRWK']]
    },
    'Cassandra': {
        'keyword': 'Apache Cassandra',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'HBase': {
        'keyword': 'Apache HBase',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Couchbase': {
        'keyword': 'Couchbase',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Clusterpoint': {
        'keyword': 'Clusterpoint',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Parquet': {
        'keyword': 'Apache Parquet',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'Druid': {
        'keyword': 'Druid',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Riak': {
        'keyword': 'Riak',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Trafodion': {
        'keyword': 'Trafodion',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL', 'Hadoop', 'HBase']
    },
    'CockroachDB': {
        'keyword': 'CockroachDB',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'Altibase': {
        'keyword': 'Altibase',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL']
    },
    'AllegroGraph': {
        'keyword': 'AllegroGraph',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Blazegraph': {
        'keyword': 'Blazegraph',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'DataStax': {
        'keyword': 'DataStax',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Sparksee': {
        'keyword': 'Sparksee',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'InfiniteGraph': {
        'keyword': 'InfiniteGraph',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'MarkLogic': {
        'keyword': 'MarkLogic',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Neo4j': {
        'keyword': 'Neo4j',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'OpenCog': {
        'keyword': 'OpenCog',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Ontotext': {
        'keyword': 'Ontotext',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'OrientDB': {
        'keyword': 'OrientDB',
        'type': keyword_type.types['DB'],
        'extra': ['NoSQL', 'Graph databases']
    },
    'Mulgara': {
        'keyword': 'Mulgara',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Profium': {
        'keyword': 'Profium',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'Stardog': {
        'keyword': 'Stardog',
        'type': keyword_type.types['DB'],
        'extra': ['Graph databases']
    },
    'NuoDB': {
        'keyword': 'NuoDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'VoltDB': {
        'keyword': 'VoltDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'Clustrix': {
        'keyword': 'Clustrix',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'CouchDB': {
        'keyword': 'Apache CouchDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL'],
        'type_extra': [keyword_type.types['APACHE_FRWK']]
    },
    'SenseiDB': {
        'keyword': 'SenseiDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'GenieDB': {
        'keyword': 'GenieDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'ScalArc': {
        'keyword': 'ScalArc',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'ScaleDB': {
        'keyword': 'ScaleDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'Drizzle': {
        'keyword': 'Drizzle',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'ScaleBase': {
        'keyword': 'ScaleBase',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'Akiban': {
        'keyword': 'Akiban',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'TransLattice': {
        'keyword': 'TransLattice',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'HandlerSocket': {
        'keyword': 'Percona',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'Percona': {
        'keyword': 'Percona',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'Tokutek': {
        'keyword': 'Tokutek',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'SchemafreeDB': {
        'keyword': 'SchemafreeDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'JustOneDB': {
        'keyword': 'JustOneDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'TokuDB': {
        'keyword': 'TokuDB',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'MemSQL': {
        'keyword': 'MemSQL',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    'Spanner': {
        'keyword': 'Spanner',
        'type': keyword_type.types['DB'],
        'extra': ['NewSQL']
    },
    # List of JavaScript libraries/frameworks
    'CommonJS': {
        'keyword': 'CommonJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Common.js': {
        'keyword': 'CommonJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Webpack': {
        'keyword': 'Webpack',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Angular': {
        'keyword': 'AngularJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Angular.js': {
        'keyword': 'AngularJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'AngularJS': {
        'keyword': 'AngularJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'React': {
        'keyword': 'React.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'React.js': {
        'keyword': 'React.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'ReactJS': {
        'keyword': 'React.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Node': {
        'keyword': 'Node.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Node.js': {
        'keyword': 'Node.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'NodeJS': {
        'keyword': 'Node.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Express': {
        'keyword': 'Express.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Express.js': {
        'keyword': 'Express.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Backbone': {
        'keyword': 'Backbone.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'BackboneJS': {
        'keyword': 'Backbone.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Backbone.js': {
        'keyword': 'Backbone.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Marionette': {
        'keyword': 'Marionette.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'MarionetteJS': {
        'keyword': 'Marionette.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Marionette.js': {
        'keyword': 'Marionette.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Ember': {
        'keyword': 'Ember.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'EmberJS': {
        'keyword': 'Ember.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Ember.js': {
        'keyword': 'Ember.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'jQuery': {
        'keyword': 'jQuery',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Underscore': {
        'keyword': 'Underscore.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'UnderscoreJS': {
        'keyword': 'Underscore.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Underscore.js': {
        'keyword': 'Underscore.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Lodash': {
        'keyword': 'Lodash.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Lo-dash': {
        'keyword': 'Lodash.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Lodash.js': {
        'keyword': 'Lodash.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'LodashJS': {
        'keyword': 'Lodash.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'D3': {
        'keyword': 'D3.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'D3JS': {
        'keyword': 'D3.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'D3.js': {
        'keyword': 'D3.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Grunt': {
        'keyword': 'Grunt.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Grunt.js': {
        'keyword': 'Grunt.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'GruntJS': {
        'keyword': 'Grunt.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Gulp': {
        'keyword': 'Gulp.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Gulp.js': {
        'keyword': 'Gulp.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'GulpJS': {
        'keyword': 'Gulp.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Aurelia': {
        'keyword': 'Aurelia.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Aurelia.js': {
        'keyword': 'Aurelia.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'AureliaJS': {
        'keyword': 'Aurelia.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Meteor': {
        'keyword': 'Meteor.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Meteor.js': {
        'keyword': 'Meteor.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'MeteorJS': {
        'keyword': 'Meteor.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Polymer': {
        'keyword': 'Polymer.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Polymer.js': {
        'keyword': 'Polymer.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'PolymerJS': {
        'keyword': 'Polymer.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Knockout': {
        'keyword': 'Knockout.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Knockout.js': {
        'keyword': 'Knockout.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'KnockoutJS': {
        'keyword': 'Knockout.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Vue': {
        'keyword': 'Vue.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Vue.js': {
        'keyword': 'Vue.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'VueJS': {
        'keyword': 'Vue.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Mercury.js': {
        'keyword': 'Mercury.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'MercuryJS': {
        'keyword': 'Mercury.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Three.js': {
        'keyword': 'Three.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'ThreeJS': {
        'keyword': 'Three.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Moment': {
        'keyword': 'Moment.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Moment.js': {
        'keyword': 'Moment.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'MomentJS': {
        'keyword': 'Moment.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Log4js': {
        'keyword': 'Log4js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'Chart.js': {
        'keyword': 'Chart.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'ChartJS': {
        'keyword': 'Chart.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript']
    },
    'SocketIO': {
        'keyword': 'Socket.io',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Socket.io': {
        'keyword': 'Socket.io',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Mustache': {
        'keyword': 'Mustache.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Mustache.js': {
        'keyword': 'Mustache.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'MustacheJS': {
        'keyword': 'Mustache.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Handlebars': {
        'keyword': 'Handlebars.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Handlebars.js': {
        'keyword': 'Handlebars.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'HandlebarsJS': {
        'keyword': 'Handlebars.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Require.js': {
        'keyword': 'Require.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'RequireJS': {
        'keyword': 'Require.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Bower': {
        'keyword': 'Bower',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'BowerJS': {
        'keyword': 'Bower.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Bower.js': {
        'keyword': 'Bower.js',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Phantom': {
        'keyword': 'PhantomJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'Phantom.js': {
        'keyword': 'PhantomJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    'PhantomJS': {
        'keyword': 'PhantomJS',
        'type': keyword_type.types['JS_LIB'],
        'extra': ['JavaScript'],
    },
    # List of CSS frameworks
    'Bootstrap': {
        'keyword': 'Bootstrap',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Dojo': {
        'keyword': 'Dojo',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'awsm.css': {
        'keyword': 'awsm.css',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Baseguide': {
        'keyword': 'Baseguide',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'BoxySheets': {
        'keyword': 'BoxySheets',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Bulma': {
        'keyword': 'Bulma',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Chopstick': {
        'keyword': 'Chopstick',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Concise': {
        'keyword': 'Concise',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Flexify': {
        'keyword': 'Flexify',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'floatz': {
        'keyword': 'floatz',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Foundation': {
        'keyword': 'Foundation',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Ink': {
        'keyword': 'Ink',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'inuitcss': {
        'keyword': 'inuitcss',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Kathamo': {
        'keyword': 'Kathamo',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Kube': {
        'keyword': 'Kube',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Materialize': {
        'keyword': 'Materialize',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Responsee': {
        'keyword': 'Responsee',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Tacit': {
        'keyword': 'Tacit',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'uikit': {
        'keyword': 'uikit',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Unsemantic': {
        'keyword': 'Unsemantic',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'W3.CSS': {
        'keyword': 'W3.CSS',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    'Wee': {
        'keyword': 'Wee',
        'type': keyword_type.types['CSS_FRWK'],
        'extra': ['CSS'],
    },
    # List of AWS products
    'EC2': {
        'keyword': 'Amazon EC2',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Beanstalk': {
        'keyword': 'Amazon Elastic Beanstalk',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Lambda': {
        'keyword': 'Amazon Lambda',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'S3': {
        'keyword': 'Amazon S3',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Glacier': {
        'keyword': 'Amazon Glacier',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'EBS': {
        'keyword': 'Amazon EBS',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'DynamoDB': {
        'keyword': 'Amazon DynamoDB',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'ElastiCache': {
        'keyword': 'Amazon ElastiCache',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    'Redshift': {
        'keyword': 'Amazon Redshift',
        'type': keyword_type.types['AWS_PRODUCT']
    },
    # List of message brokers
    'ActiveMQ': {
        'keyword': 'Apache ActiveMQ',
        'type': keyword_type.types['MSG_BROKER'],
        'extra_type': [keyword_type.types['APACHE_FRWK']]
    },
    'Kafka': {
        'keyword': 'Apache Kafka',
        'type': keyword_type.types['MSG_BROKER'],
        'extra_type': [keyword_type.types['APACHE_FRWK']]
    },
    'Qpid': {
        'keyword': 'Apache Qpid',
        'type': keyword_type.types['MSG_BROKER'],
        'extra_type': [keyword_type.types['APACHE_FRWK']]
    },
    'Celery': {
        'keyword': 'Celery',
        'type': keyword_type.types['MSG_BROKER']
    },
    'Gearman': {
        'keyword': 'Gearman',
        'type': keyword_type.types['MSG_BROKER']
    },
    'HornetQ': {
        'keyword': 'HornetQ',
        'type': keyword_type.types['MSG_BROKER']
    },
    'JORAM': {
        'keyword': 'JORAM',
        'type': keyword_type.types['MSG_BROKER']
    },
    'QDB': {
        'keyword': 'QDB',
        'type': keyword_type.types['MSG_BROKER']
    },
    'RabbitMQ': {
        'keyword': 'RabbitMQ',
        'type': keyword_type.types['MSG_BROKER']
    },
    'Enduro/X ': {
        'keyword': 'Enduro/X ',
        'type': keyword_type.types['MSG_BROKER']
    },
    # List of indexable keywords
    'AWS': {
        'keyword': 'Amazon Web Services',
        'type': keyword_type.types['KEYWORD']
    },
    'Selenium': {
        'keyword': 'Selenium',
        'type': keyword_type.types['KEYWORD']
    },
    'Neural-Networks': {
        'keyword': 'Neural Networks',
        'type': keyword_type.types['KEYWORD']
    },
    'Machine-learning': {
        'keyword': 'Machine learning',
        'type': keyword_type.types['KEYWORD']
    },
    'Natural-Language-Processing': {
        'keyword': 'Natural Language Processing',
        'type': keyword_type.types['KEYWORD']
    },
    'Artificial-Intelligence': {
        'keyword': 'Artificial Intelligence',
        'type': keyword_type.types['KEYWORD']
    },
    'Big-Data': {
        'keyword': 'Big Data',
        'type': keyword_type.types['KEYWORD']
    },
    'MapReduce': {
        'keyword': 'MapReduce',
        'type': keyword_type.types['KEYWORD']
    },
    'Map/Reduce': {
        'keyword': 'MapReduce',
        'type': keyword_type.types['KEYWORD']
    },
}


def get_keywords():
    return [keywords[keyword]['keyword'] for keyword in keywords]


def generate_keywords(summary):
    k = []

    for key in keywords:
        keyword_pattern = re.compile(r'(?<=[\s(,-/])({})(?=[\s),-./])'.format(re.escape(key)), re.IGNORECASE)

        keyword_found = keyword_pattern.search(summary)

        if keyword_found:
            k.append(key)

    return k

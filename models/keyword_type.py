types = {
    'PROGRAMMING_LANG': 'programming language',
    'DB_LANG': 'database language',
    'FRWK': 'framework',
    'AUTO_TOOl': 'automation tool',
    'SEARCH_SRV': 'search server',
    'VM_ENV': 'virtual machine environment',
    'JS_LIB': 'javascript library'
}


def get_keywords():
    return [types[t] for t in types]

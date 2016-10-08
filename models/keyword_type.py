types = {
    # Software keywords
    'KEYWORD': 'Keyword',
    'OS': 'Operating System',
    'MOBILE_OS': 'Mobile Operating System',
    'MOBILE_FRWK': 'Mobile Framework',
    'PROGRAMMING_LANG': 'Programming Language',
    'DB': 'Database',
    'FRWK': 'Framework',
    'WEB_FRWK': 'Web Framework',
    'APACHE_FRWK': 'Apache Framework',
    'DATA_STRUCT_SRV': 'Data Structure Server',
    'WEB_SRV': 'Web Server',
    'SEARCH_SRV': 'Search Server',
    'VC': 'Version Control',
    'BUILD_AUTO_TOOL': 'Build Automation Tool',
    'CONT_INTEGRATION_TOOL': 'Continuous Integration Tools',
    'CONF_MANAGE_TOOL': 'Configuration Management Tools',
    'VM_ENV': 'Virtual Machine Environment',
    'JS_LIB': 'Javascript Library',
    'CSS_FRWK': 'CSS Framework',
    'AWS_PRODUCT': 'Amazon Web Services Product'
}


def get_keywords():
    return [types[t] for t in types]

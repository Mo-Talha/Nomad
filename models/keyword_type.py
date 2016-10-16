types = {
    # Software keywords
    'KEYWORD': 'Keyword',
    'OS': 'Operating System',
    'MOBILE_OS': 'Mobile Operating System',
    'MOBILE_FRWK': 'Mobile Framework',
    'PROGRAMMING_LANG': 'Programming Language',
    'DB': 'Database',
    'DB_TYPE': 'Database Type',
    'APACHE_FRWK': 'Apache Framework',
    'WEB_FRWK': 'Web Framework',
    'WEB_SRV': 'Web Server',
    'SEARCH_SRV': 'Search Server',
    'DATA_STRUCT_SRV': 'Data Structure Server',
    'MSG_BROKER': 'Message Broker',
    'VC': 'Version Control',
    'BUILD_AUTO_TOOL': 'Build Automation Tool',
    'CONT_INTEGRATION_TOOL': 'Continuous Integration Tools',
    'CONF_MANAGE_TOOL': 'Configuration Management Tools',
    'VM_ENV': 'Virtual Machine Environment',
    'JS_LIB': 'Javascript Library',
    'CSS_FRWK': 'CSS Framework',
    'AWS_PRODUCT': 'Amazon Web Services Product'
}


def get_keyword_types():
    return [types[t] for t in types]

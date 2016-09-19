import re

import filters
import patterns


def filter_summary(summary):
    # Certain jobs have special info about location of job
    location_info_patt = re.compile('(\*\*\*\sPLEASE NOTE:[\s\S]*?\*\*\*)')
    filtered_summary = re.sub(location_info_patt, '', summary)

    for text in filters.remove:
        text_patt_str = ['(']
        filtered_text = text.replace('.', '\.').replace('*', '\*').replace('(', '\(').replace(')', '\)')

        for word in filtered_text.split():
            text_patt_str.append(word + r'[\s|\n]*?')

        text_patt_str.append(')')
        text_patt = ''.join(text_patt_str)

        filtered_summary = re.sub(re.compile(text_patt), '', filtered_summary)

    filtered_summary = (re.sub('[*]', '', filtered_summary)).strip()

    print filtered_summary

    return filtered_summary


if __name__ == '__main__':
    filter_summary(filters.test_summary)

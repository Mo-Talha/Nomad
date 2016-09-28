import re

import filters


def filter_summary(summary):
    # Certain jobs have special info about location of job
    location_info_patt = re.compile('(\*\*\*\sPLEASE NOTE:[\s\S]*?\*\*\*)')
    filtered_summary = re.sub(location_info_patt, '', summary)

    # Generate regex for each summary to be removed. Allows for multiple spaces and/or new lines between words.
    for text in filters.remove:
        text_patt_str = ['(']
        filtered_text = text.replace('.', '\.').replace('*', '\*').replace('(', '\(').replace(')', '\)')

        for word in filtered_text.split():
            text_patt_str.append(word + r'[\s|\n]*?')

        text_patt_str.append(')')
        text_patt = ''.join(text_patt_str)

        filtered_summary = re.sub(re.compile(text_patt), '', filtered_summary)

    # Remove asterisks
    filtered_summary = re.sub('[*]', '', filtered_summary)

    # Remove non-ascii characters
    filtered_summary = (re.sub(r'[^\x00-\x7F]+', '', filtered_summary)).strip()

    return filtered_summary


if __name__ == '__main__':
    print filter_summary(filters.test_summary)

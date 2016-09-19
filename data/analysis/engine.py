import re

import filters
import patterns


def filter_summary(summary):
    # Certain jobs have special info about location of job
    location_info_patt = re.compile('(\*\*\*\sPLEASE NOTE:[\s\S]*?\*\*\*)')
    filtered_summary = re.sub(location_info_patt, '', summary)

    # Remove non-characters
    filtered_summary = (re.sub('[^a-zA-Z\d\s:http]', '', filtered_summary)).strip()

    #auth_patt = ['([*|\n]*?']

    #for word in filters.employment_authorization.split():
    #    auth_patt.append(word + '[*|\n]*?]')

    #print ''.join(auth_patt)

    #auth_patt = re.compile('([*|\n]*?important note about employment authorizations:[\s\S]*?\*+)')

    # Jobs outside America (Canada & US) have a note about international employment
    # Note: This regex assumes note is written at end of job. It will ignore everything after note.
    #outside_america_patt = re.compile('([*|\n]*?IMPORTANT NOTE FROM CECA RE: EMPLOYMENT OUTSIDE Canada and USA [\s\S]*)')

    print filtered_summary

    return filtered_summary


if __name__ == '__main__':
    filter_summary(filters.test_summary)

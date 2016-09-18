import re


def filter_summary(summary):
    # Certain jobs have special info about location of job
    location_info_patt = re.compile('(\*\*\*\sPLEASE NOTE:[\s\S]*?\*\*\*)')

    auth_patt = re.compile('([*|\n]*?important note about employment authorizations:[\s\S]*?\*+)')

    # Jobs outside America (Canada & US) have a note about international employment
    # Note: This regex assumes note is written at end of job. It will ignore everything after note.
    outside_america_patt = re.compile('([*|\n]*?IMPORTANT NOTE FROM CECA RE: EMPLOYMENT OUTSIDE Canada and USA [\s\S]*)')


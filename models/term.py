"""
This module is used to determine and/or manage UW co-op terms.
"""

FALL_TERM = 1
WINTER_TERM = 2
SPRING_TERM = 3


def get_coop_term(date):
    # Reference starts at Fall 2016
    term = 1169

    # Add 2 each year.
    for i in range(2016, date.year):
        term += 2

        # Add 4 each term.
        if 5 <= date.month <= 8:
            term += 4
        elif 9 <= date.month <= 12:
            term += 8

    return term


def get_term(month):
    # Fall = September - December, Winter = January - April, Spring = May - August
    term = None
    if 1 <= month <= 4:
        term = WINTER_TERM
    elif 5 <= month <= 8:
        term = SPRING_TERM
    elif 9 <= month <= 12:
        term = FALL_TERM

    return term
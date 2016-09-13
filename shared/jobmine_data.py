term_data = {
    2020: {
        "Fall": 1209,
        "Spring": 1205,
        "Winter": 1201
    },
    2019: {
        "Fall": 1199,
        "Spring": 1195,
        "Winter": 1191
    },
    2018: {
        "Fall": 1189,
        "Spring": 1185,
        "Winter": 1181
    },
    2017: {
        "Fall": 1179,
        "Spring": 1175,
        "Winter": 1171
    },
    2016: {
        "Fall": 1169
    }
}


def get_term(month):
    # Fall = September - December, Winter = January - April, Spring = May - August
    term = ''
    if 1 <= month <= 4:
        term = 'Winter'
    elif 5 <= month <= 8:
        term = 'Spring'
    elif 9 <= month <= 12:
        term = 'Fall'

    return term
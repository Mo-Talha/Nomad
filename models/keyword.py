from mongoengine import *

import data.analysis.corpus.computerscience.keywords as comp_sci_keywords


class Keyword(EmbeddedDocument):

    # Name of keyword
    keyword = StringField(required=True)

    # Type of keyword
    type = StringField(required=True, choices=comp_sci_keywords.get_keywords())

from mongoengine import *

import keyword_type

import data.analysis.corpus.computerscience.keywords as comp_sci_keywords


class Keyword(EmbeddedDocument):

    # Name of keyword
    keyword = StringField(required=True, choices=comp_sci_keywords.get_keywords())

    # Type of keyword
    types = LineStringField(required=True, choices=keyword_type.get_keyword_types())

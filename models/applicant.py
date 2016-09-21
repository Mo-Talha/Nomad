from mongoengine import *

import datetime


class Applicant(EmbeddedDocument):

    # Total number of applicants
    applicants = IntField(required=True, default=0, min_value=0)

    # Date applicants was recorded
    date = DateTimeField(required=True, default=datetime.datetime.now())

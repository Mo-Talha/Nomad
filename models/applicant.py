from mongoengine import *

from datetime import datetime


class Applicant(EmbeddedDocument):

    # Total number of applicants
    applicants = IntField(required=True, default=0, min_value=0)

    # Date applicants was recorded
    date = DateTimeField(required=True, default=datetime.now())

    def to_dict(self):
        return {
            'id': self._id,
            'applicants': self.applicants,
            'date': self.date
        }
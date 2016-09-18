from mongoengine import *

import rating
import job
import comment


class Employer(Document):
    meta = {
        'indexes': [
            'overall.rating',
            'overall.count',
            'hire_rate.rating',
            'hire_rate.count'
        ]
    }

    # Employer name
    name = StringField(primary_key=True)

    # List of all jobs offered by employer
    jobs = ListField(ReferenceField(job.Job))

    # Percentage rating for employer
    overall = EmbeddedDocumentField(rating.AggregateRating, default=rating.AggregateRating())

    # Percentage of how many positions employer usually hires vs. how many advertised
    hire_rate = EmbeddedDocumentField(rating.AggregateRating, default=rating.AggregateRating())

    # Warnings for employer
    warnings = ListField(StringField)

    # Comments about employer (added by UW students)
    comments = EmbeddedDocumentListField(comment.Comment, default=[])

    @classmethod
    def employer_exists(cls, employer_name):
        return True if cls.objects(name=employer_name.lower()).count() > 0 else False
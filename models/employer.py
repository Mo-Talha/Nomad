from mongoengine import *

import rating
import job


class Employer(Document):
    meta = {
        'indexes': [
            'jobs',
            'overall.rating',
            'overall.count',
            'hire_rate.rating',
            'hire_rate.count'
        ]
    }

    # Employer name
    id = StringField(primary_key=True)

    # List of all jobs offered by employer
    jobs = ListField(ReferenceField(job))

    # Percentage rating for employer
    overall = EmbeddedDocumentField(rating.AggregateRating, default=rating.AggregateRating())

    # Percentage of how many positions employer usually hires vs. how many advertised
    hire_rate = EmbeddedDocumentField(rating.AggregateRating, default=rating.AggregateRating())

    # Warnings for employer
    warnings = ListField(StringField)


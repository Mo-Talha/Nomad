from mongoengine import *

from rating import AggregateRating
from job import Job
from comment import Comment


class Employer(Document):
    meta = {
        'indexes': [
            'overall.rating',
            'overall.count'
        ]
    }

    # Employer name
    name = StringField(primary_key=True)

    # List of all jobs offered by employer
    jobs = ListField(ReferenceField(Job))

    # Percentage rating for employer
    overall = EmbeddedDocumentField(AggregateRating, default=AggregateRating())

    # Warnings for employer
    warnings = ListField(StringField)

    # Comments about employer (added by UW students)
    comments = EmbeddedDocumentListField(Comment, default=[])

    @classmethod
    def employer_exists(cls, employer_name):
        return True if cls.objects(name=employer_name.lower()).count() > 0 else False

    def job_exists(self, job_title):
        return True if Job.objects(id__in=[j.id for j in self.jobs], title=job_title).count() > 0 else False

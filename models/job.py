from mongoengine import *

import comment
import term
import applicant
import rating


class Job(Document):
    meta = {
        'indexes': [
            '$summary'
        ]
    }

    # Job title
    title = StringField(required=True)

    # Job summary
    summary = StringField(required=True)

    # Year job was advertised
    year = IntField(required=True)

    # Term job was advertised
    term = IntField(choices=(term.FALL_TERM, term.WINTER_TERM, term.WINTER_TERM))

    # Job location
    location = ListField(StringField(required=True))

    # Number of job openings
    openings = IntField(required=True, min_value=1)

    # Number of remaining job openings
    remaining = IntField(required=True, max_value=openings, min_value=0)

    # Percentage of how many positions hires vs. how many advertised
    hire_rate = EmbeddedDocumentField(rating.AggregateRating, default=rating.AggregateRating())

    # History of number of applicants that applied to job
    applicants = EmbeddedDocumentListField(applicant.Applicant, default=[])

    # Programs that the job is targeted for
    #programs = ListField(StringField(), choices=constants.programs, default=[])

    # Comments about job (either crawled from ratemycoopjob or added by UW students)
    comments = EmbeddedDocumentListField(comment.Comment, default=[])

    # Keywords for job (ex. programming languages for software jobs)
    _keywords = ListField(StringField(), default=[])

    def save(self, *args, **kwargs):
        if not self.remaining:
            self.remaining = self.openings

        return super(Job, self).save(*args, **kwargs)

    @classmethod
    def job_exists(cls, job_title):
        return True if cls.objects(name=job_title.lower()).count() > 0 else False


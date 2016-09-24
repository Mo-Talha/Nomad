from mongoengine import *

from comment import Comment
from applicant import Applicant
from rating import AggregateRating

import program
import term


class Job(Document):
    meta = {
        'indexes': [
            '$title'
        ]
    }

    # Job title
    title = StringField(required=True)

    # Job summary
    summary = StringField(required=True)

    # Year job was advertised
    year = IntField(required=True)

    # Term job was advertised
    term = IntField(choices=(term.FALL_TERM, term.WINTER_TERM, term.SPRING_TERM))

    # Job location. Latest entry is most probable job location
    location = ListField(StringField(required=True))

    # Number of job openings
    openings = IntField(required=True, min_value=1)

    # Number of remaining job openings
    remaining = IntField(required=True, max_value=openings, min_value=0)

    # Percentage of how many positions hires vs. how many advertised
    hire_rate = EmbeddedDocumentField(AggregateRating, default=AggregateRating())

    # History of number of applicants that applied to job
    applicants = EmbeddedDocumentListField(Applicant, default=[])

    # Programs that the job is targeted for
    programs = ListField(StringField(choices=program.get_programs()), default=[])

    # What level job is intended for
    levels = ListField(StringField(choices=('Junior', 'Intermediate', 'Senior')), default=[])

    # Comments about job (either crawled from ratemycoopjob or added by UW students)
    comments = EmbeddedDocumentListField(Comment, default=[])

    # Keywords for job (ex. programming languages for software jobs)
    _keywords = ListField(StringField(), default=[])

    # Deprecated
    deprecated = BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.remaining:
            self.remaining = self.openings

        return super(Job, self).save(*args, **kwargs)

    @classmethod
    def comment_exists(cls, job_comment):
        return True if cls.objects(comments__summary=job_comment).count() > 0 else False

    def to_dict(self):
        return {
            'title': self.title,
            'summary': self.summary,
            'year': self.year,
            'term': self.term,
            'location': self.location,
            'openings': self.openings,
            'remaining': self.remaining,
            'hire_rate': self.hire_rate
        }

from mongoengine import *

from datetime import datetime

from comment import Comment
from applicant import Applicant
from rating import AggregateRating
from keyword import Keyword

import program as Program
import term as Term


class Job(Document):
    meta = {
        'indexes': [
            '$title',
            'levels',
            'programs',
            'year',
            'term'
        ]
    }

    # Job title
    title = StringField(required=True)

    # URL of job
    url = URLField(required=False, default=None)

    # Job summary
    summary = StringField(required=True)

    # Year job was advertised
    year = IntField(required=True)

    # Term job was advertised
    term = StringField(choices=(Term.FALL_TERM, Term.WINTER_TERM, Term.SPRING_TERM))

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
    programs = ListField(StringField(choices=Program.get_programs()), default=[])

    # What level job is intended for
    levels = ListField(StringField(choices=(Term.JUNIOR_TERM, Term.INTERMEDIATE_TERM, Term.SENIOR_TERM)), default=[])

    # Comments about job (either crawled from ratemycoopjob or added by UW students)
    comments = EmbeddedDocumentListField(Comment, default=[])

    # Keywords for job (ex. programming languages for software jobs)
    keywords = EmbeddedDocumentListField(Keyword, default=[])

    # Deprecated
    deprecated = BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.remaining:
            self.remaining = self.openings

        return super(Job, self).save(*args, **kwargs)

    @classmethod
    def comment_exists(cls, job_comment):
        return True if cls.objects(comments__comment=job_comment, comments__crawled=True).count() > 0 else False

    @staticmethod
    def get_active_job_urls():
        now = datetime.now()
        return [job.to_dict_compact() for job in Job.objects(year=now.year, term=Term.get_term(now.month),
                                                             deprecated=False).only('id', 'url') if job.url]

    def to_dict_compact(self):
        return {
            'id': self.id,
            'url': self.url,
        }

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'summary': self.summary,
            'year': self.year,
            'term': self.term,
            'location': self.location,
            'openings': self.openings,
            'remaining': self.remaining,
            'hire_rate': self.hire_rate.rating,
            'applicants': [self.applicants.to_dict()],
            'programs': self.programs,
            'levels': self.levels,
            'comments': [self.comments.to_dict()],
            'deprecated': self.deprecated,
        }

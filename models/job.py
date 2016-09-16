from mongoengine import *

import comment


class Job(Document):
    meta = {
        'indexes': [
            'title',
            'summary'
        ]
    }

    # Job title
    title = StringField(required=True)

    # Job summary
    summary = StringField(required=True)

    # Job location
    location = StringField(required=True)

    # Number of job openings
    openings = IntField(required=True, min_value=1)

    # Number of remaining job openings
    remaining = IntField(required=True, max_value=openings, min_value=0, default=openings)

    # Programs that the job is targeted for
    programs = ListField(StringField(), default=[])

    # Comments about job (either crawled from ratemycoopjob or added by UW students)
    comments = EmbeddedDocumentListField(comment, default=[])

    # Keywords for job (ex. programming languages for software jobs)
    _keywords = ListField(StringField(), default=[])




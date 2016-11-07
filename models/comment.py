from mongoengine import *

from datetime import datetime

from rating import AggregateRating


class Comment(EmbeddedDocument):

    # Title of job (if commenting to job instead of employer)
    title = StringField(required=False, default=None)

    # Comment
    comment = StringField(required=True)

    # Date comment was recorded
    date = DateTimeField(required=True, default=datetime.now())

    # Salary (hourly)
    salary = FloatField(required=True, default=0.0, min_value=0.0)

    # Rating
    rating = EmbeddedDocumentField(AggregateRating, default=AggregateRating())

    # Whether comment was crawled from RateMyCoopJob or added via web
    crawled = BooleanField(required=True, default=False)

from mongoengine import *

from datetime import datetime

from rating import AggregateRating


class Comment(EmbeddedDocument):

    # Comment
    comment = StringField(required=True)

    # Date comment was recorded
    date = DateTimeField(required=True, default=datetime.now())

    # Salary (hourly)
    salary = FloatField(required=True, default=0.0)

    # Rating
    rating = EmbeddedDocumentField(AggregateRating, default=AggregateRating())

    crawled = BooleanField(required=True, default=False)

from mongoengine import *

from datetime import datetime

import rating


class Comment(EmbeddedDocument):

    # Comment
    comment = StringField(required=True)

    # Date comment was recorded
    date = DateTimeField(required=True, default=datetime.datetime.now())

    # Salary (hourly)
    salary = FloatField(required=True, default=0.0)

    # Rating
    rating = EmbeddedDocumentField(rating.AggregateRating, default=rating.AggregateRating())

    crawled = BooleanField(required=True, default=False)

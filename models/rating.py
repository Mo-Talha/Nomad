from mongoengine import *


class AggregateRating(EmbeddedDocument):
    rating = FloatField(min_value=0.0, max_value=1.0, default=0.0)

    count = IntField(min_value=0, default=0)

    def add_rating(self, rating):
        pass

    def remove_rating(self, rating):
        pass
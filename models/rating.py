from mongoengine import *


class AggregateRating(EmbeddedDocument):
    # Percentage of rating as float value (from 0 to 1.0)
    rating = FloatField(min_value=0.0, max_value=1.0, default=0.0)

    count = IntField(min_value=0, default=0)

    def add_rating(self, rating):
        if not 0 <= rating <= 1.0:
            raise ValueError('Rating must be between 0 and 1.0')

        self.rating = float(self.rating + rating) / (int(self.count) + 1)
        self.count += 1

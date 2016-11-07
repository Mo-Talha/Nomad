from mongoengine import *


class Location(EmbeddedDocument):

    # Location name
    name = StringField(required=True)

    # Location longitude
    longitude = DecimalField(required=True)

    # Location latitude
    latitude = DecimalField(required=True)
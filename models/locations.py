from mongoengine import *


class Locations(Document):
    meta = {
        'indexes': [
            '$name',
            'countrycode',
            'longitude',
            'latitude'
        ]
    }

    # Country code
    countrycode = StringField(required=True)

    # Postal code
    postalcode = StringField(required=True)

    # City/place name
    name = StringField(required=True)

    # Order subdivision (state)
    name1 = StringField(required=False)

    # Order subdivision (state) code
    code1 = StringField(required=False)

    # Order subdivision (county/province)
    name2 = StringField(required=False)

    # Order subdivision (county/province) code
    code2 = StringField(required=False)

    # Order subdivision (community)
    name3 = StringField(required=False)

    # Order subdivision (community) code
    code3 = StringField(required=False)

    # Location longitude
    longitude = FloatField(required=True)

    # Location latitude
    latitude = FloatField(required=True)

    # Accuracy of lat/lng from 1=estimated to 6=centroid
    accuracy = IntField(required=True)

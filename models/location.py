from mongoengine import *

from models.locations import Locations


class Location(EmbeddedDocument):

    def __init__(self, *args, **kwargs):
        if 'longitude' not in kwargs and 'latitude' not in kwargs:
            locations = Locations.objects.search_text("\"{}\"".format(kwargs['name']))

            longitude = 0
            latitude = 0

            if locations:
                longitude = locations[0].longitude
                latitude = locations[0].latitude

                for location in locations:
                    if location.countrycode == 'CA':
                        longitude = location.longitude
                        latitude = location.latitude
                        break

            kwargs['latitude'] = latitude
            kwargs['longitude'] = longitude

        super(EmbeddedDocument, self).__init__(*args, **kwargs)

    # Location name
    name = StringField(required=True)

    # Location longitude
    longitude = FloatField(required=True)

    # Location latitude
    latitude = FloatField(required=True)

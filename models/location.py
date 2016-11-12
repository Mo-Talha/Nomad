from geopy.geocoders import Nominatim

from mongoengine import *

geolocator = Nominatim(country_bias='CA')


class Location(EmbeddedDocument):

    def __init__(self, *args, **kwargs):
        location = geolocator.geocode(kwargs['name'], timeout=10)

        if location and 'longitude' not in kwargs and 'latitude' not in kwargs:
            kwargs['longitude'] = location.longitude
            kwargs['latitude'] = location.latitude

        super(EmbeddedDocument, self).__init__(*args, **kwargs)

    # Location name
    name = StringField(required=True)

    # Location longitude
    longitude = DecimalField(required=False)

    # Location latitude
    latitude = DecimalField(required=False)

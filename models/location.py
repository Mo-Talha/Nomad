import redis

from geopy.geocoders import Nominatim

from mongoengine import *

import shared.secrets as secrets

geolocator = Nominatim(country_bias='CA')

pool = redis.ConnectionPool(host=secrets.REDIS_HOST, port=secrets.REDIS_PORT, db=secrets.REDIS_DB)
redis = redis.Redis(connection_pool=pool)


class Location(EmbeddedDocument):

    def __init__(self, *args, **kwargs):

        if 'longitude' not in kwargs and 'latitude' not in kwargs:
            cached_location = redis.hgetall('location:{}'.format(kwargs['name']))

            if cached_location:
                kwargs['longitude'] = cached_location['longitude']
                kwargs['latitude'] = cached_location['latitude']
            else:
                location = geolocator.geocode(kwargs['name'], timeout=10)

                if location:
                    redis.hmset('location:{}'.format(kwargs['name']), {
                        'longitude': location.longitude,
                        'latitude': location.latitude
                    })

                    kwargs['longitude'] = location.longitude
                    kwargs['latitude'] = location.latitude

        super(EmbeddedDocument, self).__init__(*args, **kwargs)

    # Location name
    name = StringField(required=True)

    # Location longitude
    longitude = DecimalField(required=False)

    # Location latitude
    latitude = DecimalField(required=False)

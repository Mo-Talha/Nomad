import redis

from geopy.geocoders import Nominatim

from mongoengine import *
from mongoengine import connection

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
                db = connection._get_db(reconnect=False)

                pipeline = {
                    "location": {
                        "$elemMatch": {"name": kwargs['name'], "longitude": {"$ne": 0.0}, "latitude": {"$ne": 0.0}}
                    }
                }

                job_locations = db.job.find_one(pipeline, {"location": 1})

                if job_locations:
                    longitude = job_locations['location'][0]['longitude']
                    latitude = job_locations['location'][0]['latitude']
                else:
                    location = geolocator.geocode(kwargs['name'], timeout=10)
                    longitude = location.longitude
                    latitude = location.latitude

                redis.hmset('location:{}'.format(kwargs['name']), {
                    'longitude': longitude,
                    'latitude': latitude
                })

                kwargs['longitude'] = longitude
                kwargs['latitude'] = latitude

        super(EmbeddedDocument, self).__init__(*args, **kwargs)

    # Location name
    name = StringField(required=True)

    # Location longitude
    longitude = DecimalField(required=False)

    # Location latitude
    latitude = DecimalField(required=False)

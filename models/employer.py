from mongoengine import *


class Employer(Document):
    meta = {
        'indexes': [

        ]
    }

    # Employer name
    id = StringField(primary_key=True)

    
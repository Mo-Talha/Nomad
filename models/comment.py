from mongoengine import *


class Comment(EmbeddedDocumentField):
    meta = {
        'indexes': [
            'comment'
        ]
    }

    # Comment
    comment = StringField(required=True)

from mongoengine import *


class Comment(EmbeddedDocument):

    # Comment
    comment = StringField(required=True)

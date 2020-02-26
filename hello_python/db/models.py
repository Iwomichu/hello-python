from .db import db


class Movie(db.Document):
    showType = db.StringField(required=True)
    title = db.StringField(required=True)
    casts = db.ListField(db.StringField(), required=True)
    creators = db.ListField(db.StringField(), required=True)
    year = db.DecimalField(required=True)

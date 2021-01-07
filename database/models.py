from .db import db

class Discos(db.Document):
    name = db.StringField(required= True, unique = True)
    Feeder_33 = db.ListField(db.StringField())
    Feeder_11 = db.ListField(db.StringField())

    
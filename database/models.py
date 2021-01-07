from .db import db

class Discos(db.Document):
    name = db.StringFeild(required= True, unique = True)
    Feeder_33 = db.ListFeild(db.StringFeild())
    Feeder_11 = db.ListFeild(db.StringFeild())

    
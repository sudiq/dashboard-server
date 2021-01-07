from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Discos(db.Document):
    name = db.StringField(required = True, unique = True)
    Feeder_33 = db.ListField(db.StringField())
    Feeder_11 = db.ListField(db.StringField())

class Users(db.Document):
    email = db.StringField(require = True, unique = True)
    password = db.StringField(required = True)
    disco  = db.ReferencField('Discos')
    def hash_pass(self):
        self.password = generate_password_hash(self.password)
    def chcek_pass(self, password):
        return check_password_hash(self.password, password)
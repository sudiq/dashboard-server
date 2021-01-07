from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Discos(db.Document):
    name = db.StringField(required = True, unique = True)
    feeder_33 = db.ListField(db.StringField())
    feeder_11 = db.ListField(db.StringField())

class Users(db.Document):
    email = db.StringField(require = True, unique = True)
    password = db.StringField(required = True, min_lenght = 8)
    disco  = db.StringField(required = True)
    role = db.StringField()
    def hash_pass(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    def check_pass(self, password):
        return check_password_hash(self.password, password)
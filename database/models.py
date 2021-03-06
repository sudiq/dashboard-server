from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash




class Feeder11(db.Document):
    name = db.StringField(required = True, unique = True)
    feeder_band = db.StringField(required = True)

class InjectionSub(db.Document):
    name = db.StringField(required = True, unique = True)
    feeder_11 = db.ListField(db.StringField())

class Fedder33(db.Document):
    name = db.StringField(required = True, unique = True)
    injection_sub_stations = db.ListField(db.StringField())

class Discos(db.Document):
    name = db.StringField(required = True, unique = True)
    feeder_33 = db.ListField(db.StringField())
    
class Users(db.Document):
    email = db.StringField(require = True, unique = True)
    password = db.StringField(required = True, min_lenght = 8)
    disco  = db.StringField()
    role = db.StringField()
    def hash_pass(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    def check_pass(self, password):
        return check_password_hash(self.password, password)







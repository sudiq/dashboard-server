from flask import Flask, Request, Response
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from resources.errors import errors
from database.db import initdb
from database.models import Discos
import json


app = Flask(__name__)

app.config.from_envvar('ENV_FILE_LOCATION')

print(app.config)

mail = Mail(app)
from resources.routes import initroutes

api = Api(app, errors = errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)



@jwt.user_claims_loader
def add_claims(identity):
    return identity.get('role')
@jwt.user_identity_loader
def identity_check(identity):
    return identity.get("id")



initdb(app)
initroutes(api)



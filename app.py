from flask import Flask, Request, Response
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from resources.routes import initroutes
from flask_jwt_extended import JWTManager
from database.db import initdb
from database.models import Discos
from resources.errors import errors
import json


app = Flask(__name__)

app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app, errors= errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mail = Mail(app)

app.config['MONGO_SETTINGS'] = {
    'host': 'mongodb://localhost/dashboard'
}

@jwt.user_claims_loader
def add_claims(identity):
    return identity.get('role')
@jwt.user_identity_loader
def identity_check(identity):
    return identity.get("id")



initdb(app)
initroutes(api)



app.run()
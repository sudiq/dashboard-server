from flask import Flask, Request, Response
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.routes import initroutes

from database.db import initdb
from database.models import Discos
import json


app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['MONGO_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}


initdb(app)
initroutes(api)



app.run()
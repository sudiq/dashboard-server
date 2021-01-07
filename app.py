from flask import Flask, Request, Response
from flask_restful import Api
from resources.routes import initroutes

from database.db import initdb
from database.models import Discos
import json


app = Flask(__name__)
api = Api(app)
app.config['MONGO_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}


initdb(app)
initroutes(api)



app.run()
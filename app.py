from flask import Flask, Request, Response

from .resources.routes import initroutes

from database.db import initdb
from database.models import Discos
import json


app = Flask(__name__)

app.config['MONGO_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initdb(app)
initroutes(app)



app.run()
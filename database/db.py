from flask_mongoengine import MongoEngine

db = MongoEngine()


def initdb(app):
    db.init_app(app)
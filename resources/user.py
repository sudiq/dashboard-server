from flask import request, Response
from flask_restful import Resource
from database.models import Users

class UsersApi(Resource):
    def get(self):
        users = Users.objects().to_json()
        Response(users, mimetype= "application/json", status = 200)
    def put(self):
        body = request.get_json()
        user = Users(**body).save()
        id = user.id
        return {'id':str(id)}, "200"


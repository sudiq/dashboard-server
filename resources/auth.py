from flask import Response, request
from database.models import Users
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime



class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = Users(**body)
        user.hash_pass()
        print(type(user.password), user.password)
        user.save()
        id = user.id
        return {'id':str(id)}, 200
class UserLoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = Users.objects.get(email = body.get('email'))
        authorized = user.check_pass(body.get('password'))
        if not authorized:
            return {'error': "Invalid email or password"}, 401
        expires = datetime.timedelta(days = 3)
        identity = {'id':str(user.id), "role": user.role }
        access_token = create_access_token(identity = identity, expires_delta = expires)
        return {'token': access_token}, 200
class AdminLoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = Users.check_pass(email = body.get('email'))
        authorized = user.check_pass(body.get("password"))
        if not authorized:
            return {'error': "Invalid username or password"}
        if user.role.lower() != "admin":
            return {"error":"you do not have sufficient permission"}
        expires = datetime.timedelta(days = 3)
        identity = {'id':str(user.id), "role": user.role }
        access_token = create_access_token(identity = identity, expires_delta = expires)
        return {'token': access_token}, 200
from flask import Response, request
from database.models import Users
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, EmailNotExistsError, InternalServerError, PermissionError, UnauthorizedError


class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = Users(**body)
            user.hash_pass()
            user.save()
            id = user.id
            return {'id':str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        # except Exception as e:
        #     raise InternalServerError 

class UserLoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = Users.objects.get(email = body.get('email'))
            authorized = user.check_pass(body.get('password'))
            if not authorized:
                raise UnauthorizedError
            expires = datetime.timedelta(days = 3)
            identity = {'id':str(user.id), "role": user.role }
            access_token = create_access_token(identity = identity, expires_delta = expires)
            return {'token': access_token}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except DoesNotExist:
            raise EmailNotExistsError
        except UnauthorizedError:
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError


        
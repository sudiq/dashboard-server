from flask import request, Response
from flask_restful import Resource
from database.models import Users
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, EmailNotExistsError, InternalServerError, PermissionError


class UsersApi(Resource):
    @jwt_required
    def get(self):
        try:
            if get_jwt_claims() not in  ["admin", "super_admin"]:
                raise PermissionError
            users = Users.objects().to_json()
            return Response(users, mimetype= "application/json", status = 200)
        except PermissionError:
            raise PermissionError
        except Exception:
            raise InternalServerError
    @jwt_required
    def post(self):
        try:
            if get_jwt_claims() not in  ["admin", "super_admin"]:
                raise PermissionError
            body = request.get_json()
            if get_jwt_claims() == "admin" and body.get('role') in ['admin', 'super_admin']:
                raise PermissionError
            user = Users(**body)
            user.hash_pass()
            user.save()
            id = user.id
            return {'id':str(id)}, "200"
        except PermissionError:
            raise PermissionError
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception:
            raise InternalServerError 

class UserApi(Resource):
    @jwt_required
    def get(self, id):
        try:
            if get_jwt_claims() not in  ["admin", "super_admin"]:
                raise PermissionError
            user =  Users.objects.get( id = id).to_json()
            if not user:
                raise EmailNotExistsError
            return Response(user, mimetype = "application/json", status= 200)
        
        except (DoesNotExist, EmailNotExistsError):
            raise EmailNotExistsError
        except Exception:
            raise InternalServerError
    @jwt_required
    def put(self, id):
        try:
            if get_jwt_claims() not in  ["admin", "super_admin"]:
                raise PermissionError
            body = request.get_json()
            if body.get('role') and get_jwt_claims()!= "super_admin":
                raise PermissionError
            user = Users.objects.get( id = id).update(**body)
            id = str(user.id)
            return {"id":id}, 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise EmailNotExistsError
        except Exception:
            raise InternalServerError
    @jwt_required
    def delete(self, id):
        try:
            if get_jwt_claims() not in  ["admin", "super_admin"]:
                raise PermissionError
            user = Users.objects.get( id = id)
            if user.role and get_jwt_claims() != "super_admin":
                raise PermissionError
            id = str(user.id)
            user.delete()
            return {"id":id}, 200
        except DoesNotExist:
            raise EmailNotExistsError
        except Exception:
            raise InternalServerError



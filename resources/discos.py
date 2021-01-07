from flask import Response, request
from database.models import Discos
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, DiscoAlreadyExistsError, InternalServerError, UpdatingDiscoError, DeletingDiscoError, DiscoNotExistsError, PermissionError

class DiscosApi(Resource):
    @jwt_required
    def get(self):
        try:
            if get_jwt_claims() != "admin":
                raise PermissionError
            discos = Discos.objects().to_json()
            return Response(discos, mimetype = "application/json", status = 200)
        except DoesNotExist:
            raise DiscoNotExistsError
        except Exception:
            raise InternalServerError
    @jwt_required
    def post(self):
        try:
            if get_jwt_claims() != "admin":
                raise PermissionError
            body = request.get_json()
            disco = Discos(**body).save()
            id = disco.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise DiscoAlreadyExistsError
        except Exception as e:
            raise InternalServerError 
class DiscoApi(Resource):
    @jwt_required
    def put(self, name):
        try:
            if get_jwt_claims() != "admin":
                raise PermissionError
            body = request.get_json()
            Discos.objects.get(name = name).update(**body)
            return "", 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise DiscoNotExistsError
        except Exception:
            raise InternalServerError
    @jwt_required
    def delete(self, name):
        try:
            if get_jwt_claims() != "admin":
                raise PermissionError
            Discos.objects.get(name = name ).delete()
            return "", 200
        except DoesNotExist:
            raise DiscoNotExistsError
        except Exception:
            raise InternalServerError
    @jwt_required
    def get(self, name):
        try:
            if get_jwt_claims() != "admin":
                raise PermissionError
            disco = Discos.objects.get(name = name).to_json()
            return Response(disco, mimetype = "application/json", status = 200)
        except DoesNotExist:
            raise DiscoNotExistsError
        except Exception:
            raise InternalServerError
        
    
      
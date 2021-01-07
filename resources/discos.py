from flask import Response, request
from database.models import Discos
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims


class DiscosApi(Resource):
    @jwt_required
    def get(self):
        if get_jwt_claims() != "admin":
            return {'error': "You do not have sufficient permission"}, 404
        discos = Discos.objects().to_json()
        return Response(discos, mimetype = "application/json", status = 200)
    @jwt_required
    def post(self):
        if get_jwt_claims() != "admin":
            return {'error': "You do not have sufficient permission"}, 404
        body = request.get_json()
        disco = Discos(**body).save()
        id = disco.id
        return {'id': str(id)}, 200
class DiscoApi(Resource):
    @jwt_required
    def put(self, id):
        if get_jwt_claims() != "admin":
            return {'error': "You do not have sufficient permission"}, 404
        body = request.get_json()
        disco = Discos.objects.get(id = id).update(**body)
        return "", 200
    @jwt_required
    def delete(self, id):
        if get_jwt_claims() != "admin":
            return {'error': "You do not have sufficient permission"}, 404
        disco = Discos.objects.get(id = id ).delete()
        return "", 200
    @jwt_required
    def get(self, name):
        if get_jwt_claims() != "admin":
            return {'error': "You do not have sufficient permission"}, 404
        disco = Discos.objects.get(name = name).to_json()
        return Response(disco, mimetype = "application/json", status = 200)
    
    
      
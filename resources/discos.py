from flask import Response, request
from database.models import Discos
from flask_restful import Resource


class DiscosApi(Resource):
    def get(self):
        discos = Discos.objects().to_json()
        return Response(discos, mimetyp = "application/json", status = 200)
    def post(self):
        body = request.get_json()
        disco = Discos(**body).save()
        id = disco.id
        return {'id': str(id)}, 200
class DiscoApi(Resource):
    def put(self, id):
        body = request.get_json()
        disco = Discos.objects.get(id = id).update(**body)
        return "", 200
    def delete(self, id):
        disco = Discos.objects.get(id = id ).delete()
        return "", 200
    def get(self, name):
        disco = Discos.objects.get(name = name).to_json()
        return Response(disco, mimetype = "application/json", status = 200)
        return 
    
      
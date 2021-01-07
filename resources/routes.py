from .discos import DiscosApi, DiscoApi


def initroutes(api):
    api.add_resource(DiscoApi, '/disco/<name>')
    api.aad_resource(DiscosApi, '/disco')
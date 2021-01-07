from .discos import DiscosApi, DiscoApi
from .auth import SignupApi, UserLoginApi, AdminLoginApi
from .user import UsersApi

def initroutes(api):
    api.add_resource(DiscoApi, '/api/disco/<name>')
    api.add_resource(DiscosApi, '/api/disco')
    api.add_resource(UsersApi,'/api/users')
    api.add_resource(UserLoginApi, '/api/auth/user/login')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(AdminLoginApi, '/api/auth/admin/login')

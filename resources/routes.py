from .discos import DiscosApi, DiscoApi
from .auth import SignupApi, UserLoginApi
from .user import UsersApi, UserApi
from .reset_password import ForgotPassword, ResetPassword


def initroutes(api):
    api.add_resource(UserApi, "/api/user/<id>")
    api.add_resource(DiscoApi, '/api/disco/<name>')
    api.add_resource(DiscosApi, '/api/disco')
    api.add_resource(UsersApi,'/api/users')
    api.add_resource(UserLoginApi, '/api/auth/login')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')

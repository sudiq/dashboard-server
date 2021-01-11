from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from database.models import Users
from flask_restful import Resource
import datetime
from resources.errors import SchemaValidationError, InternalServerError, EmailNotExistsError, BadTokenError
from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError
from services.mail_services import send_email

class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            email = body.get('email')
            if not email:
                raise SchemaValidationError

            user = Users.objects.get(email=email)
            if not user:
                raise EmailNotExistsError

            expires = datetime.timedelta(hours=24)
            identity = {'id' : str(user.id), "role" : user.role}
            reset_token = create_access_token(identity, expires_delta=expires)

            return send_email('Reset Your Password',
                              sender='support@movie-bag.com',
                              recipients=[user.email],
                              text_body=render_template('email/reset_password.txt',
                                                        url=url + reset_token),
                              html_body=render_template('email/reset_password.html',
                                                        url=url + reset_token))
        except SchemaValidationError:
            raise SchemaValidationError
        except EmailNotExistsError:
            raise EmailNotExistsError
        finally:
            raise InternalServerError


class ResetPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            reset_token = body.get('reset_token')
            password = body.get('password')

            if not reset_token or not password:
                raise SchemaValidationError

            user_id = decode_token(reset_token)['identity']

            user = Users.objects.get(id=user_id)

            user.modify(password=password)
            user.hash_password()
            user.save()

            return send_email('Password reset successful',
                              sender='support@movie-bag.com',
                              recipients=[user.email],
                              text_body='Password reset was successful',
                              html_body='<p>Password reset was successful</p>')

        except SchemaValidationError:
            raise SchemaValidationError
        except ExpiredSignatureError:
            raise BadTokenError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        finally:
            raise InternalServerError
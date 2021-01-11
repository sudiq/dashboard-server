
from flask_restful import HTTPException

class InternalServerError(HTTPException):
    pass

class SchemaValidationError(HTTPException):
    pass

class DiscoAlreadyExistsError(HTTPException):
    pass

class UpdatingDiscoError(HTTPException):
    pass

class DeletingDiscoError(HTTPException):
    pass

class DiscoNotExistsError(HTTPException):
    pass

class EmailAlreadyExistsError(HTTPException):
    pass

class PermissionError(HTTPException):
    pass

class EmailNotExistsError(HTTPException):
    pass

class UnauthorizedError(HTTPException):
    pass

class BadTokenError(HTTPException):
    pass



errors = {
    "BadTokenError":{
        "message":"Invalid or expired token",
        "status":403
    },
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "DiscoAlreadyExistsError": {
         "message": "Disco with given name already exists",
         "status": 400
     },
     "UpdatingDiscoError": {
         "message": "Updating Disco added by other is forbidden",
         "status": 403
     },
     "DeletingDiscoError": {
         "message": "Deleting disco added by other is forbidden",
         "status": 403
     },
     "DiscoNotExistsError": {
         "message": "Disco with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
     "PermissionError":{
         "message":"Permission denied",
         "status":401
     },
     "EmailNotExistsError":{
         'message': "Invalid user",
         'status':401
     }
}
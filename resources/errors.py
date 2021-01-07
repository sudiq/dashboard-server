class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class DiscoAlreadyExistsError(Exception):
    pass

class UpdatingDiscoError(Exception):
    pass

class DeletingDiscoError(Exception):
    pass

class DiscoNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass
class PermissionError(Exception):
    pass
class EmailNotExistsError(Exception):
    pass
class UnauthorizedError(Exception):
    pass

errors = {
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
     "EmailNotExistsError":
     {'message': "Invalid user"}
}
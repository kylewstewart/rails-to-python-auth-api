from flask import request
from functools import wraps
import jwt
from IPython import embed

SECRET = '12345'
ALGO = 'HS256'


def authorize(f):
    @wraps(f)
    def decorated(**params):
        token = request.headers.get('Authorization')
        request.authorized = True
        return f(**params)

    return decorated

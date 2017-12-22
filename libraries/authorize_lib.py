from flask import request
from functools import wraps
import jwt

SECRET = '12345'
ALGO = 'HS256'


def authorize(f):
    @wraps(f)
    def decorated(**params):
        request.authorized = False
        request.id = None
        token = request.headers.get('Authorization')
        if token:
            id = jwt.decode(
                bytes(token, encoding="utf-8"),
                SECRET,
                algorithms=[ALGO]
            )['id']
            if id:
                request.authorized = True
                request.id = id
        return f(**params)
    return decorated

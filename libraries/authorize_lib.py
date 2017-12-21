from flask import request
from functools import wraps
import jwt


def authorize(f):
    @wraps(f)
    def decorated(**params):
        token = request.headers.get('Authorization')
        request.authorized = False
        return f(**params)

    return decorated

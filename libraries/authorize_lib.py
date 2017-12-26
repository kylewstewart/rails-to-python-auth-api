from flask import request
import jwt

SECRET = '12345'
ALGO = 'HS256'


def is_authorized():
    token = request.headers.get('Authorization')
    if token and token != 'null':
        request.id = jwt.decode(
            bytes(token, encoding="utf-8"),
            SECRET,
            algorithms=[ALGO]
        )['id']
        if id:
            return True
    return False

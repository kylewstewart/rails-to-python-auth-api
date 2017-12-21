from flask import request, make_response, jsonify
from controllers.app_controller import AppController
from models import User
import bcrypt
import jwt

SECRET = '12345'
ALGO = 'HS256'


class AuthController(AppController):
    COLLECTION = 'auth'

    def __init__(self):
        pass

    def index(self):
        pass

    def create(self):
        data = request.get_json(silent=True)
        user = User.find_one_by_username(data.get('username'))
        password = bytes(data['password'], encoding="utf-8")
        if bcrypt.checkpw(password, user.password_digest):
            token = jwt.encode({'id': user.id}, SECRET, algorithm=ALGO)
            return self.serailize({'jwt': bytes.decode(token),
                                   **user.__dict__}, 'create')
        else:
            resp = {'error': 'Username or password is incorrect'}
            return make_response(jsonify(resp), 404)

    def show(self):
        pass

    def update(self):
        pass

    def destroy(self):
        pass

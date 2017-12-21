from flask import request, make_response, jsonify
from controllers.app_controller import AppController
from models import User
import bcrypt


class UsersController(AppController):
    COLLECTION = 'users'

    def __init__(self):
        self.id = request.view_args.get('id')
        self.data = request.get_json(silent=True)

    def index(self):
        users = User.all()
        return self.serailize(users, 'index')

    def create(self):
        password = bytes(self.data['password'], encoding="utf-8")
        password_digest = bcrypt.hashpw(password, bcrypt.gensalt())
        user = User(self.id, self.data['username'], password_digest)
        dup = user.find_one()
        if dup is None:
            return self.serailize(user.save(), 'create')
        else:
            return self.serailize(dup, 'create')

    def show(self):
        user = User.find_one_by_id(self.id)
        return self.serailize(user.__dict__, 'show')

    def update(self):
        data = self.data
        if data['password'] is not None:
            password = bytes(data['password'], encoding="utf-8")
            data['password_digest'] = bcrypt.hashpw(password, bcrypt.gensalt())
            del data['password']
        user = User.update(self.id, **data)
        return self.serailize(user.__dict__, 'update')

    def destroy(self):
        id = self.id
        resp = User.delete(id)
        return make_response(jsonify(resp), 200)

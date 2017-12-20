from controllers.app_controller import AppController
from models import User


class UsersController(AppController):
    COLLECTION = 'users'

    def __init__(self, id, data):
        self.id = id
        self.data = data

    def index(self):
        users = User.all()
        return self.serailize(users, 'index')

    def create(self):
        id, data = self.id, self.data
        user = User(id, **data)
        dup = user.find_one()
        if dup is None:
            return self.serailize(user.save(), 'create')
        else:
            return self.serailize(dup, 'create')

    def show(self):
        user = User.find_one_by_id(self.id)
        return self.serailize(user.__dict__, 'show')

    def update(self):
        id, data = self.id, self.data
        user = User.update(id, **data)
        return self.serailize(user.__dict__, 'update')

    def destroy(self):
        id = self.id
        return User.delete(id)

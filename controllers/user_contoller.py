from controllers.app_controller import AppController
from models import User
from IPython import embed


class UserController(AppController):
    COLLECTION = 'users'

    def __init__(self, id, data):
        self.id = id
        self.data = data

    def index(self):
        users = User.all()
        return self.serailizer(users, 'index')

    def create(self):
        id, data = self.id, self.data
        user = User(id, **data)
        dup = user.find_one()
        if dup is None:
            return self.serailizer(user.save(), 'create')
        else:
            return self.serailizer(dup, 'create')

    def show(self):
        user = User.find_one_by_id(self.id)
        if user is None:
            return None
        else:
            return self.serailizer(user.__dict__, 'show')

    def update(self):
        return "User#Update"

    def destroy(self):
        return "User#Destroy"

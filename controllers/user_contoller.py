from controllers.app_controller import AppController
from models import User
from IPython import embed


class UserController(AppController):
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def index(self):
        users = User.all()
        embed()
        return "User#Index"

    def create(self):
        user = User('sally', 'password')
        dup = user.find_one()
        if dup is False:
            response = user.save()
        else:
            response = dup
        embed()
        return response

    def show(self):
        return "User#Show"

    def update(self):
        return "User#Update"

    def destroy(self):
        return "User#Destroy"

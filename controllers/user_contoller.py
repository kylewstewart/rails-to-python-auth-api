from controllers.app_controller import AppController


class User(AppController):
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def index(self):
        return "User#Index"

    def create(self):
        return "User#Create"

    def show(self):
        return "User#Show"

    def update(self):
        return "User#Update"

    def destroy(self):
        return "User#Destroy"

from controllers.app_controller import AppController


class Auth(AppController):
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def index(self):
        return "Auth#Index"

    def create(self):
        return "Auth#Create"

    def show(self):
        return "Auth#Show"

    def update(self):
        return "Auth#Update"

    def destroy(self):
        return "Auth#Destroy"

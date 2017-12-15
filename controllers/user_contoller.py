from models import user_model


class User():
    def __init__(self, method, data, id):
        self.method = method
        self.data = data
        self.id = id

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

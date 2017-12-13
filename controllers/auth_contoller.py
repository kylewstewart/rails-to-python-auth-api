class Auth():
    def __init__(self, method, data, id):
        self.method = method
        self.data = data
        self.id = id

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

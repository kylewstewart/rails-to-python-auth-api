class User():
    def __init__(self, method, data, id):
        self.method = method
        self.data = data
        self.id = id

    def index(self):
        return "Index"

    def create(self):
        return "Create"

    def show(self):
        return "Show"

    def update(self):
        return "Update"

    def destroy(self):
        return "Destroy"

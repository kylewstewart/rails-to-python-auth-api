"""
AppController is the super Controller class.
Allows Restful routes to be called from request.method in app.py.
"""


class AppController():
    def get(self):
        if self.id is None:
            return self.index()
        else:
            return self.show()

    def post(self):
        return self.create()

    def put(self):
        return self.update()

    def patch(self):
        return self.update()

    def delete(self):
        return self.destroy()

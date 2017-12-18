from config import serailize
from IPython import embed


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

    def serailizer(self, data, set):
        if type(data) is list:
            return [self.filter_dict(dict, set) for dict in data]
        else:
            return self.filter_dict(data, set)

    def filter_dict(self, dict, set):
        allowed = serailize[self.COLLECTION][set]
        return {k: v for (k, v) in dict.items() if k in allowed}

from config.serailizer_config import serailizer


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

    def serailize(self, data, set):
        if type(data) is list:
            resp = [self.filter_dict(dict, set) for dict in data]
        else:
            resp = self.filter_dict(data, set)
        return (resp, 200)

    def filter_dict(self, dict, set):
        allowed = serailizer[self.COLLECTION][set]
        return {k: v for (k, v) in dict.items() if k in allowed}

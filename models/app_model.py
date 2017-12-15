from pymongo import MongoClient
from models.configs import db_configs
from IPython import embed


class AppModel():

    def __init__(self):
        self.host = db_configs['host']
        self.port = db_configs['port']
        self.database = db_configs['database']

    def get_db(self):
        client = MongoClient(self.host, self.port)
        return client[self.database]

    def username_print(self):
        embed()
        print(self.username)

    @classmethod
    def create(cls, *args, **kwargs):
        try:
            return cls(*args, **kwargs)
        except Exception as e:
            return False

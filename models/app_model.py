from pymongo import MongoClient
from models.configs import db_configs


class AppModel():

    def __init__(self):
        self.host = db_configs['host']
        self.port = db_configs['port']
        self.database = db_configs['database']

    def get_db(self):
        client = MongoClient(self.host, self.port)
        return client[self.database]

    def username_print(self):
        print(self.username)

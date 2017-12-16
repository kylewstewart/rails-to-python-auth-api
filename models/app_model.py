from pymongo import MongoClient
from models.configs import db_configs
from IPython import embed


class AppModel():

    HOST = db_configs['host']
    PORT = db_configs['port']
    DATABASE = db_configs['database']

    @classmethod
    def all(cls):
        client = MongoClient(cls.HOST, cls.PORT)
        db = client[cls.DATABASE]
        collection = db.cls.collection
        documents = []
        for document in collection.find():
            documents.append(document)
        return documents

    def __init__(self):
        self.host = db_configs['host']
        self.port = db_configs['port']
        self.database = db_configs['database']

    def get_db(self):
        client = MongoClient(self.HOST, self.PORT)
        return client[self.DATABASE]

    def get_id_number(self):
        db = self.get_db()
        embed()

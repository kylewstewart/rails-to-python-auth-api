from pymongo import MongoClient
from models.configs import db_configs
from IPython import embed


class AppModel():

    DB = MongoClient(
        db_configs['host'],
        db_configs['port']
    )[db_configs['database']]

    @classmethod
    def all(cls):
        client = MongoClient(cls.HOST, cls.PORT)
        db = client[cls.DATABASE]
        collection = db.cls.collection
        documents = []
        for document in collection.find():
            documents.append(document)
        return documents

    def get_id_number(self):
        embed()
        id = self.DB.counters.distinct(f"{self.collection}")

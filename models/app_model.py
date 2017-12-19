from pymongo import MongoClient
from config import database


class AppModel():

    DB = MongoClient(database['host'], database['port'])[database['db_name']]

    @classmethod
    def all(cls):
        db = cls.DB
        collection = db[f"{cls.COLLECTION}"]
        return [doc for doc in collection.find()]

    @classmethod
    def find_one_by_id(cls, id):
        db = cls.DB
        collection = db[f"{cls.COLLECTION}"]
        doc = collection.find_one({"id": id})
        if doc is None:
            return None
        else:
            return cls(**doc)

    @classmethod
    def update(cls, id, **data):
        db = cls.DB
        collection = db[f"{cls.COLLECTION}"]
        result = collection.update_one({'id': id}, {'$set': data})
        if result.acknowledged:
            return cls.find_one_by_id(id)
        else:
            return None

    @classmethod
    def delete(cls, id):
        db = cls.DB
        collection = db[f"{cls.COLLECTION}"]
        result = collection.delete_one({'id': id})
        return result.acknowledged

    def save(self):
        db = self.DB
        collection = db[f"{self.COLLECTION}"]
        doc = {k: v for (k, v) in self.__dict__.items()}
        doc['id'] = self.get_id_and_inc()
        result = collection.insert_one(doc)
        if result.acknowledged:
            self.id = doc['id']
            return doc
        else:
            return None

    def get_id_and_inc(self):
        # Collection name (COUNT) and increament value (1) are hardcoded
        db = self.DB
        counters = db.counters
        collection = self.COLLECTION
        counter = counters.find_one_and_update(
            {"collection": f"{collection}"},
            {'$inc': {'id_count': 1}, '$set': {'done': True}}
        )
        return counter['id_count']

    def find_one(self):
        db = self.DB
        collection = db[f"{self.COLLECTION}"]
        if self.id is None:
            doc = {k: v for (k, v) in self.__dict__.items() if k != "id"}
            return collection.find_one(doc)
        else:
            return collection.find_one({'id': self.id})

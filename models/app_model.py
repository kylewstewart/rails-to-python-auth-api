from pymongo import MongoClient
from config import database
from IPython import embed


class AppModel():

    DB = MongoClient(database['host'], database['port'])[database['db_name']]

    @classmethod
    def all(cls):
        db = cls.DB
        collection = cls.collection
        collection = db.collection
        documents = []
        for document in collection.find():
            documents.append(document)

        return documents

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

    def save(self):
        db = self.DB
        collection = db[f"{self.COLLECTION}"]
        doc = {k: v for (k, v) in self.__dict__.items()}
        doc['id'] = self.get_id_and_inc()
        try:
            collection.insert_one(doc)
        except Exception as e:
            return False
        self.id = doc['id']

        return {k: v for (k, v) in doc.items() if k != "_id"}

    def find(self):
        db = self.DB
        collection = db[f"{self.COLLECTION}"]
        if self.id is None:
            doc = {k: v for (k, v) in self.__dict__.items() if k != "id"}
        else:
            doc = {k: v for (k, v) in self.__dict__.items()}
        results = []
        for document in collection.find(doc):
            results.append({k: v for (k, v) in document.items() if k != "_id"})

        return results

    def find_one(self):
        db = self.DB
        collection = db[f"{self.COLLECTION}"]
        if self.id is None:
            doc = {k: v for (k, v) in self.__dict__.items() if k != "id"}
        else:
            doc = {k: v for (k, v) in self.__dict__.items()}
        result = collection.find_one(doc)
        if result is None:
            return False
        else:
            return {k: v for (k, v) in result.items() if k != "_id"}

import pymongo
from pymongo import MongoClient
from type_check import CheckType as ct

class Server:

    def __init__(self, db):
        self.connect(db)

    def connect(self, db):
        try:
            connection = MongoClient()
            print(f'Connected to MongoDB: {connection}')
            self.db = connection[db]
            print(f'Connected to Database: {self.db}')
            # return db
        except:
            print(f'There was an issue connecting to the Database')

    def collection(self, coll):
        collection = self.db[coll]
        return collection

    def insert(self, coll, data):
        collection = self.collection(coll)
        collection.insert_one(data)

    def updateOne(self, coll, filterProperty, filterValue, action, target, updateValue):
        collection = self.collection(coll)
        collection.update_one(
                            {f'{filterProperty}':f'{filterValue}'}, 
                            {f'${action}': {f'{target}':f'{updateValue}'}})
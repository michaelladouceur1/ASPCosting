# from server import Server
# from model import Model
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['asp-costing']
collection = db['standards']

# db = Server('asp-costing')

post = {"author": "Michael",
		"text": "My first blog post!",
		"tags": ["mongodb", "python", "pymongo"]}


# post_id = collection.insert_one(post).inserted_id
# print(post_id)

collection.update_many({'author': 'Michael'}, {'$set': {'author': 'Cameron'}})
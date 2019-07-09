from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from pandas import DataFrame
from model import Standards

def connect(func):
    def wrapper(*args, **kwargs):
        engine = create_engine('sqlite:///test2.db', echo=False)
        Session = sessionmaker(engine)
        session = Session()
        data = func(session=session, *args, **kwargs)
        session.close()
        return data 
    return wrapper

@connect
def query(table, mode, session, order=None, **kwargs):
    if mode.lower() == 'first':
        data = session.query(table).filter_by(**kwargs).first()
    elif mode.lower() == 'all':
        data = session.query(table).filter_by(**kwargs).order_by(order).all()
    return data

@connect
def insert(*args, session):
    print(f'insert: {args}')
    session.add_all([item for item in args])
    session.commit()

# class Server:
#     def __init__(self):
#         self.connect('asp-costing')

#     def connect(self, db):
#         try:
#             connection = MongoClient()
#             self.db = connection[db]
#         except:
#             print(f'There was an issue connecting to the Database')

#     def collection(self, coll):
#         collection = self.db[coll]
#         return collection

#     def cursorToDF(self, cursor):
#         df = DataFrame(list(cursor))
#         return df

#     def insert(self, coll, data):
#         collection = self.collection(coll)
#         collection.insert_one(data)
#         print(f'The following were inserted into {coll}: {data}')

#     def updateOne(self, coll, action, target, updateValue, filterProperty=None, filterValue=None):
#         collection = self.collection(coll)
#         if coll.lower() == 'standards':
#             cursor = self.find('standards')
#             id = cursor['_id'][0]
#             collection.update_one(
#                             {'_id': id}, 
#                             {f'${action}': {f'{target}': updateValue}})
#         else:
#             collection.update_one(
#                             {f'{filterProperty}':f'{filterValue}'}, 
#                             {f'${action}': {f'{target}':f'{updateValue}'}})

#     def find(self, coll, filter={}):
#         collection = self.collection(coll)
#         try:
#             response = collection.find(filter)
#             data = self.cursorToDF(response)
#         except FileNotFoundError:
#             data = 'PLACE HOLDER'
#         return data
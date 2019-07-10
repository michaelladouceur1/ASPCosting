import eel
from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from pandas import DataFrame
from model import Standards
import time

eel.init('web')

@eel.expose
def setValue(table, value):
    insert(table, value)

def connect(func):
    def wrapper(*args, **kwargs):
        engine = create_engine('sqlite:///test2.db', echo=False)
        Session = sessionmaker(engine)
        data = func(session=Session(), *args, **kwargs)
        Session().close()
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
def insert(table, values, session):
    print(f'Inserting ({values}) into {table}')
    data = getattr(Standards, table)(**values)
    session.add(data)
    session.commit()

eel.start('main.html', size=(800,500))
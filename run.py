import eel
from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from pandas import DataFrame
from model import Standards
import time

eel.init('web')

eel.init();

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
	print(f'query: {table}')
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

def outputList(data, items):
	print('output list')
	list = []
	for item in data:
		for i in items:
			# print(getattr(item, i))
			list.append(getattr(item, i))
	print(list)
	return list

@eel.expose
def loadTable(table, items):
	data = tables(table)
	table = data[0]
	mode = data[1]
	order = data[2]
	selector = data[3]
	data = query(table, mode, order=order)
	data = outputList(data, items)
	print('calling loadTable()')
	eel.loadTable(data, selector)

def tables(name):
	tables = {
		'materialType': [Standards.MaterialType, 'all', Standards.MaterialType.name, '#materialTypeTable'],
		'material': [Standards.Material, 'all', Standards.Material.name, '#materialTypeTable']
	}
	print(tables[name])
	return tables[name]

loadTable('materialType',['name'])
# loadTable('material',['materialType','name','density'])
eel.start('main.html', size=(1000,600))

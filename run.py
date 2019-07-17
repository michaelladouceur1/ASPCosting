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

@eel.expose
def removeValue(table, id):
	remove(table=table, id=id)

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
	# print(f'query: {table} (type: {type(table)}')
	if mode.lower() == 'first':
		data = session.query(table).filter_by(**kwargs).first()
	elif mode.lower() == 'all':
		data = session.query(table).filter_by(**kwargs).order_by(order).all()
	elif mode.lower() == 'delete':
		data = session.query(table).filter_by(**kwargs).first().delete()
	return data

@connect
def insert(table, values, session):
	print(f'Inserting ({values}) into {table}')
	data = getattr(Standards, table)(**values)
	session.add(data)
	session.commit()

@connect
def remove(table, id, session):
	data = session.query(getattr(Standards, table)).filter_by(id=id).first()
	print(data)
	session.delete(data)
	session.commit()

def outputDict(data, items):
	obj = {}
	list = []
	for item in data:
		id = getattr(item, 'id')
		# print(f'\nitem: {item}')
		obj[id] = {}
		for i in items:
			att = getattr(item, i)
			print(f'{i} : {type(att)}')
			if not isinstance(att, (str, int, float)):
				print(f'(EDITED ATT){i} : {att}')
				ni = i.split('_')[1]
				obj[id][i] = getattr(att, ni)
			else:
				# print(f'{i} : {att}')
				obj[id][i] = getattr(item, i)
	print(f'\n{obj}')
	return obj

def loadCollData(table, items):
	data = tables(table)
	collection = data[0]
	mode = data[1]
	order = data[2]
	data = query(collection, mode, order=order)
	# print(data)
	data = outputDict(data, items)
	return data

@eel.expose
def loadTable(table, items):
	data = loadCollData(table, items)
	eel.loadTable(data, table)

@eel.expose 
def loadSelect(table, items):
	data = loadCollData(table, items)
	print('LOADSELECT()')
	eel.loadSelect(data, table)

def tables(name):
	tables = {
		'MaterialType': [Standards.MaterialType, 'all', Standards.MaterialType.name],
		'Material': [Standards.Material, 'all', Standards.Material.name]
	}
	return tables[name]

loadTable('Material',['materialType_name','name','density'])
loadTable('MaterialType',['name'])
loadSelect('MaterialType', ['name'])
eel.start('main.html', size=(1000,600))

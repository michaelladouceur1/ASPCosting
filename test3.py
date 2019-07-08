from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
<<<<<<< HEAD
import sqlite3
=======
>>>>>>> sql


Base = declarative_base()

# # Session = sessionmaker(engine)
# # session = Session()

class Material(Base):
	__tablename__ = 'material'

	id = Column(Integer, primary_key=True)
	materialType_id = Column(Integer, ForeignKey('materialType.id'))
	materialType = relationship('MaterialType',
								lazy='subquery',
								backref=backref('materials'))
	name = Column(String)
	density = Column(Float)

	def __init__(self, materialType_id, materialType, name, density):
		self.materialType_id = materialType_id
		self.materialType = materialType
		self.name = name
		self.density = density

class MaterialType(Base):
	__tablename__ = 'materialType'

	id = Column(Integer, primary_key=True)
	name = Column(String)

	def __init__(self, name):
		self.name = name



# materialType = MaterialType('SHEET METAL')
# session.add(materialType)
# session.commit()

# material = Material(materialType_id=materialType ,materialType=materialType, name='CARBON STEEL', density=3800)
# session.add(material)
# session.commit()

# materialType2 = MaterialType('PLASTIC')
# session.add(materialType2)
# session.commit()

# material2 = Material(materialType_id=materialType2 ,materialType=materialType2, name='ABS', density=1200)
# session.add(material2)
# session.commit()

# materialType = session.query(MaterialType).all()
# material = session.query(Material).all()
# print(materialType.name)
# print(material.materialType.name, material.name, material.density)
# for i in materialType:
# 	print(i.name)

# for i in material:
# 	print(i.materialType.name, i.name, i.density)

# materialType2 = session.query(MaterialType).filter_by(name='PLASTIC').first()

# materialType2.name = 'BAR STOCK'
# session.add(materialType2)
# session.commit()

# def filter(**kwargs):
# 	data = []
# 	for key, value in zip(kwargs.keys(), kwargs.values()):
# 		data.append(f'{key}=={value}')
# 	return data

def connect(func):
	def wrapper(*args, **kwargs):
		engine = create_engine('sqlite:///test.db', echo=False)
		Base.metadata.create_all(engine)
		Session = sessionmaker(engine)
		session = Session()
		print('connect wrapper')
		data = func(session=session, *args, **kwargs)
		session.close()
		return data 
	return wrapper

@connect
def query(table, mode, session, **kwargs):
	if mode.lower() == 'first':
		data = session.query(table).filter_by(**kwargs).first()
	elif mode.lower() == 'all':
		data = session.query(table).filter_by(**kwargs).all()
	return data

@connect
def insert(*args, session):
	print('insert')
	session.add_all([item for item in args])
	session.commit()

def outputList(data, *args):
	list = []
	for item in data:
		for i in args:
			# print(getattr(item, i))
			list.append(getattr(item, i))
	return list

# SEED
# materialType = MaterialType('SHEET METAL')
# materialType2 = MaterialType('BAR STOCK')
# material = Material(materialType_id=materialType ,materialType=materialType, name='CARBON STEEL', density=3800)
# material2 = Material(materialType_id=materialType2 ,materialType=materialType2, name='STAINLESS STEEL', density=1200)

# insert(material, material2, materialType, materialType2)

materialType = query(MaterialType, 'first', name='SHEET METAL')

materialType.name = 'PLASTIC'
insert(materialType)

# materialType = query(MaterialType, 'all')
# print(outputList(materialType, 'name'))

# material = query(Material, 'all')
# data = outputList(material, 'materialType')
# newData = outputList(data, 'name')
# print(newData)
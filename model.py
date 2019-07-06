import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////home/michael/Documents/Coding/ASP/ASPCosting/test.db', echo=True)

Base = declarative_base()

class MaterialType(Base):
	__tablename__ = 'materialType'

	id = Column(Integer, primary_key=True)
	name = Column(String)

	def __init__(self, name):
		self.name = name

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
	type = Column(String, unique=True)
	material = relationship('Material', backref='materialType')

class Material(Base):
	__tablename__ = 'material'
	id = Column(Integer, primary_key=True)
	type = Column(String, ForeignKey('materialType.type'))
	name = Column(String, unique=True)
	density = Column(Float)

class Gauge(Base):
	__tablename__ = 'gauge'
	id = Column(Integer, primary_key=True)
	gauge = Column(Integer, unique=True)
	thickness = Column(Float)

class ProcessCategory(Base):
	__tablename__ = 'processCategory'
	id = Column(Integer, primary_key=True)
	name = Column(String, unique=True)
	rate = Column(Float)
	overhead = Column(Float)
	throughput = Column(Float)
	setup = Column(Float)

class WorkCenter(Base):
	__tablename__ = 'workCenter'
	id = Column(Integer, primary_key=True)
	workCenterID = Column(Integer, unique=True)
	name = Column(String, unique=True)
	category = Column(String)
	rate = Column(Float)
	overhead = Column(Float)
	throughput = Column(Float)
	setup = Column(Float)

Base.metadata.create_all(engine)


# class Part(object):
# 	def __init__(self):
# 		self.Model = {
# 			'partNumber': str,
# 			'material': {
# 				'materialType': str,
# 				'materialName': str,
# 				'materialDensity': float
# 			},
# 			'gauge': {
# 				'gaugeName': str,
# 				'gaugeThickness': float
# 			},
# 			'blank': {
# 				'width': float,
# 				'height': float,
# 				'laserPath': float,
# 				'weight': float
# 			},
# 			'partProcesses': [{
# 				'operationNumber': int,
# 				'operationName': str,
# 				'processCategory': str,
# 				'workCenterID': int,
# 				'setup': float,
# 				'operationTime': float,
# 				'operationQuantity': int
# 			}]
# 		}

# ref = Standards()
# stuff = Standards()

# print(stuff.Model)

# stuff.Model['materialType'] = ['Sheet Metal']

# material = stuff.Model['materialType']
# materialRef = ref.Model['materialType']

# CheckType(materialRef, material)

# print('\n')
# print(stuff.Model)
# print('\n')
# print(ref.Model)
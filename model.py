from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test2.db', echo=False)

Base = declarative_base()

class Standards:

	class MaterialType(Base):
		__tablename__ = 'materialType'
		id = Column(Integer, primary_key=True)
		name = Column(String, unique=True)

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

	class Gauge(Base):
		__tablename__ = 'gauge'

		id = Column(Integer, primary_key=True)
		gauge = Column(Integer, unique=True)
		thickness = Column(Float)

		def __init__(self, gauge, thickness):
			self.gauge = gauge
			self.thickness = thickness

	class ProcessCategory(Base):
		__tablename__ = 'processCategory'

		id = Column(Integer, primary_key=True)
		name = Column(String, unique=True)
		rate = Column(Float)
		overhead = Column(Float)
		throughput = Column(Float)
		setup = Column(Float)

		def __init__(self, name, rate, overhead, throughput, setup):
			self.name = name 
			self.rate = rate 
			self.overhead = overhead 
			self.throughput = throughput 
			self.setup = setup 

	class WorkCenter(Base):
		__tablename__ = 'workCenter'

		id = Column(Integer, primary_key=True)
		workCenterID = Column(Integer, unique=True)
		name = Column(String, unique=True)
		category_id = Column(Integer, ForeignKey('processCategory.id'))
		category = relationship('ProcessCategory',
								lazy='subquery',
								backref=backref('categories'))
		rate = Column(Float)
		overhead = Column(Float)
		throughput = Column(Float)
		setup = Column(Float)

		def __init__(self, workCenterID, name, category, rate, overhead, throughput, setup):
			self.workCenterID = workCenterID
			self.name = name
			self.category = category
			self.rate = rate
			self.overhead = overhead 
			self.throughput = throughput
			self.setup = setup

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
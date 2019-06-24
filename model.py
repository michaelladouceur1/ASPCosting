# from mongoengine import *
import pymongo
from pymongo import MongoClient
from typing import *

def connectToDB():
	try:
		connection = MongoClient('mongodb+srv://Michael:b1ackb1rd@cluster0-ndgwg.mongodb.net/test?retryWrites=true&w=majority')
		print(f'Connected to Database: {connection}')
		return connection
	except Error as er:
		try:
			connection = MongoClient()
			print(f'Connected to Database: {connection}')
		except Error as er:
			print(f'There was an issue connecting to the Database: {er}')

client = connectToDB()
db = client['asp-costing']
col = db['standards']

class Model():
	Standards: Dict = {
		'materialType': List[str],
		'material': [{
			'materialType': str,
			'materialName': str,
			'materialDensity': float
		}]
	}

standards = Model()

# standards.Standards = {
# 	'materialType': [4000, 'bar stock'],
# 	'material': [
# 	{
# 		'materialType': 'sheet metal',
# 		'materialName': 'carbon steel',
# 		'materialDensity': 4000
# 	},
# 	{
# 		'materialType': 'bar stock',
# 		'materialName': 'stainless',
# 		'materialDensity': 4200
# 	}]
# }

standards.Standards['material'][0]['materialType'] = 4000

print(standards.Standards)


# connect('asp-costing', host='localhost', port=27017)

# EMBEDDED DOCUMENTS

# class StandardsMaterial(EmbeddedDocument):
# 	materialType = StringField(required=True)
# 	materialName = StringField(required=True)
# 	materialDensity = DecimalField(required=True)

# class StandardsGauge(EmbeddedDocument):
# 	gauge = StringField(required=True)
# 	thickness = DecimalField(required=True)

# class ProcessForPart(EmbeddedDocument):
# 	processCategory = StringField(required=True)
# 	setupTime = DecimalField()
# 	operationNumber = IntField(required=True)
# 	timePerOperation = DecimalField(required=True)
# 	workCenter = IntField()

# # DOCUMENTS

# class Standards(Document):
# 	materialType = ListField(StringField())
# 	material = EmbeddedDocumentListField(StandardsMaterial)
# 	gauge = EmbeddedDocumentListField(StandardsGauge)



# class Part(Document):
# 	partNumber = StringField(required=True, max_length=50)
# 	materialType = StringField(required=True)
# 	material = StringField(required=True)
# 	gauge = StringField()
# 	thickness = DecimalField()
# 	blankHeight = DecimalField()
# 	blankWidth = DecimalField()
# 	processes = EmbeddedDocumentListField(ProcessForPart)

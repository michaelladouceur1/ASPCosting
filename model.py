# from mongoengine import *
import pymongo
from pymongo import MongoClient
from typing import *

class Model():
	Standards: Dict = {
		'materialType': [str],
		'material': [{
			'materialType': str,
			'materialName': str,
			'materialDensity': float
		}],
		'processCategory': [{
			'processCategoryName': str,
			'averageRate': float,
			'averageOverhead': float,
			'averageTP': float,
			'averageSetup': float
		}],
		'workCenter': [{
			'ID': int,
			'processCategory': str,
			'hourlyRate': float,
			'hourlyOverhead': float,
			'estimatedTP': float,
			'estimatedSetup': float
		}]
	}

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

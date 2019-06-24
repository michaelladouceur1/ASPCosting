from mongoengine import *

connect('asp-costing', host='localhost', port=27017)

# EMBEDDED DOCUMENTS

class StandardsMaterial(EmbeddedDocument):
	materialType = StringField(required=True)
	materialName = StringField(required=True)
	materialDensity = DecimalField(required=True)

class StandardsGauge(EmbeddedDocument):
	gauge = StringField(required=True)
	thickness = DecimalField(required=True)

class ProcessForPart(EmbeddedDocument):
	processCategory = StringField(required=True)
	setupTime = DecimalField()
	operationNumber = IntField(required=True)
	timePerOperation = DecimalField(required=True)
	workCenter = IntField()

# DOCUMENTS

class Standards(Document):
	materialType = ListField(StringField())
	material = EmbeddedDocumentListField(StandardsMaterial)
	gauge = EmbeddedDocumentListField(StandardsGauge)

class Part(Document):
	partNumber = StringField(required=True, max_length=50)
	materialType = StringField(required=True)
	material = StringField(required=True)
	gauge = StringField()
	thickness = DecimalField()
	blankHeight = DecimalField()
	blankWidth = DecimalField()
	processes = EmbeddedDocumentListField(ProcessForPart)

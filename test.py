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
	material = ListField(EmbeddedDocumentField(StandardsMaterial))
	gauge = ListField(EmbeddedDocumentField(StandardsGauge))

class Part(Document):
	partNumber = StringField(required=True, max_length=50)
	materialType = StringField(required=True)
	material = StringField(required=True)
	gauge = StringField()
	thickness = DecimalField()
	blankHeight = DecimalField()
	blankWidth = DecimalField()
	processes = ListField(EmbeddedDocumentField(ProcessForPart))

# process = ProcessForPart(
# 	processCategory = 'Press Brake',
# 	operationNumber = 4,
# 	timePerOperation = 0.1
# )
	
# part = Part(
# 	partNumber = 'EE302030.40',
# 	materialType = 'Sheet Metal',
# 	material = 'Carbon Steel',
# 	gauge = '18 GA',
# 	thickness = 0.048,
# 	blankHeight = 40,
# 	blankWidth = 20,
# 	processes = [process]
# )

material = StandardsMaterial(
    materialType = 'sheet metal',
    materialName = 'carbon steel',
    materialDensity = 4000
)

gauge1 = StandardsGauge(
    gauge = '18 GA',
    thickness = 0.048
)

gauge2 = StandardsGauge(
    gauge = '16 GA',
    thickness = 0.06
)

standards = Standards(
    materialType = ['sheet metal', 'bar stock'],
    material = [material],
    gauge = [gauge1, gauge2]
)

standards.save()

print('Database Contacted')
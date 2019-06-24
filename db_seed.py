from mongoengine import *
from model import *

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
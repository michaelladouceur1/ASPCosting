from model import MaterialType, Material
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////home/michael/Documents/Coding/ASP/ASPCosting/test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

materialType = session.query(MaterialType).filter_by(type='SHEET METAL').first()
material = Material()
material.type = materialType
material.name = 'STAINLESS STEEL'
material.density = 3800

session.add(material)
session.commit()






















# standardsSeed = Standards().Model 
# partSeed = Part().Model



# STANDARDS

# standardsSeed['materialType'] = ['sheet metal', 'bar stock']
# standardsSeed['material'] = [{
#     'materialType': 'sheet metal',
#     'materialName': 'carbon steel',
#     'materialDensity': 4000
# },{
#     'materialType': 'sheet metal',
#     'materialName': 'stainless steel',
#     'materialDensity': 3800
# }]
# standardsSeed['gauge'] = [{
#     'gaugeName': '18GA',
#     'gaugeThickness': 0.048
# },{
#     'gaugeName': '16GA',
#     'gaugeThickness': 0.06
# },{
#     'gaugeName': '12GA',
#     'gaugeThickness': 0.105
# }]
# standardsSeed['processCategory'] = [{
#     'processCategoryName': 'Laser',
#     'defaultRate': 40,
#     'defaultOverhead': 120,
#     'defaultTP': 200,
#     'unitsTP': 'inches',
#     'defaultSetup': 0.5 
# }]
# standardsSeed['workCenter'] = [{
#     'workCenterID': 11015,
#     'workCenterName': 'Prima Laser',
#     'processCategory': 'Laser',
#     'hourlyRate': 40.54,
#     'hourlyOverhead': 134.14,
#     'estimatedTP': 1000,
#     'estimatedSetup': 0.083
# }]

# Server().insert('standards', standardsSeed)

# # PART

# partSeed['partNumber'] = 'WAR36HRTB.40'
# partSeed['material'] = 
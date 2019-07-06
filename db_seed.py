from model import   MaterialType, Material, Gauge, ProcessCategory, WorkCenter
from server import connect, insert, query

##### STANDARDS

materialType = [MaterialType('SHEET METAL'), 
                MaterialType('BAR STOCK')]

material = [Material(materialType_id=materialType[0] ,materialType=materialType[0], name='CARBON STEEL', density=3800),
            Material(materialType_id=materialType[1] ,materialType=materialType[1], name='STAINLESS STEEL', density=1200)]

gauge = [Gauge(gauge='18GA', thickness=0.048),
        Gauge(gauge='16GA', thickness=0.06),
        Gauge(gauge='12GA', thickness=0.105),]

processCategory =    [ProcessCategory(name='Laser', rate=40, overhead=110, throughput=200, setup=0.15),
                    ProcessCategory(name='Press Brake', rate=32, overhead=100, throughput=300, setup=0.25)]

workCenter = [WorkCenter(workCenterID=11015, name='Prima Laser', category=processCategory[0], rate=42, overhead=120, throughput=200, setup=0.15)]

# standards = [materialType, material, gauge, processCategory, workCenter]

# insert(*materialType)
insert(*gauge)
insert(*processCategory)
insert(*workCenter)




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
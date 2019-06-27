from model import *
from server import Server

standardsSeed = Standards().Model 

standardsSeed['materialType'] = ['sheet metal', 'bar stock']
standardsSeed['material'] = [{
    'materialType': 'sheet metal',
    'materialName': 'carbon steel',
    'materialDensity': 4000
},{
    'materialType': 'sheet metal',
    'materialName': 'stainless steel',
    'materialDensity': 3800
}]
standardsSeed['gauge'] = [{
    'gaugeName': '18GA',
    'gaugeThickness': 0.048
},{
    'gaugeName': '16GA',
    'gaugeThickness': 0.06
},{
    'gaugeName': '12GA',
    'gaugeThickness': 0.105
}]
standardsSeed['processCategory'] = [{
    'processCategoryName': 'Laser',
    'defaultRate': 40,
    'defaultOverhead': 120,
    'defaultTP': 200,
    'unitsTP': 'inches',
    'defaultSetup': 0.5 
}]
standardsSeed['workCenter'] = [{
    'workCenterID': 11015,
    'workCenterName': 'Prima Laser',
    'processCategory': 'Laser',
    'hourlyRate': 40.54,
    'hourlyOverhead': 134.14,
    'estimatedTP': 1000,
    'estimatedSetup': 0.083
}]

Server('asp-costing').insert('standards', standardsSeed)
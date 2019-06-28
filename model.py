import pymongo
from pymongo import MongoClient
from typing import *
from server import Server 
from type_check import CheckType

class Standards(object):
	def __init__(self):
		self.Model = {
			'materialType': [str],
			'material': [{
				'materialType': str,
				'materialName': str,
				'materialDensity': float
			}],
			'gauge': [{
				'gaugeName': str,
				'gaugeThickness': float
			}],
			'processCategory': [{
				'processCategoryName': str,
				'defaultRate': float,
				'defaultOverhead': float,
				'defaultTP': float,
				'unitsTP': str,
				'defaultSetup': float
				# 'averageRate': float,
				# 'averageOverhead': float,
				# 'averageTP': float,
				# 'averageSetup': float
				}],
			'workCenter': [{
				'workCenterID': int,
				'workCenterName': str,
				'processCategory': str,
				'hourlyRate': float,
				'hourlyOverhead': float,
				'estimatedTP': float,
				'estimatedSetup': float
			}]
		}

class Part(object):
	def __init__(self):
		self.Model = {
			'partNumber': str,
			'materialType': str,
			'material': {
				'materialType': Model().material['materialType'],
				'materialName': Model().material['materialName'],
				'materialDensity': Model().material['materialDensity']
			},
			'gauge': {
				'gaugeName': Model().gauge['gaugeName'],
				'gaugeThickness': Model().gauge['gaugeThickness']
			},
			'blank': {
				'width': float,
				'height': float,
				'laserPath': float,
				'weight': float
			},
			'partProcesses': [{
				'processCategory': str,
				'operationNumber': int,
				'operationName': str,
				'workCenterID': int
				'setup': float,
				'operationTime': float,
				'operationQuantity': int
				
			}]
		}

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
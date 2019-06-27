from server import Server
from utilities import zipToDict
import pprint

items = [{'type': 'print', 'name': 'processes',
            'elements': 'elements'},
            {'type': 'input', 'name': 'processCategoryName',
            'elements': 'PROCESS NAME: '},
            {'type': 'input', 'name': 'defaultRate',
            'elements': 'DEFAULT RATE: '},
            {'type': 'input', 'name': 'defaultOverhead',
            'elements': 'DEFAULT OVERHEAD: '},
            {'type': 'input', 'name': 'defaultTP',
            'elements': 'DEFAULT THROUGH-PUT: '},
            {'type': 'input', 'name': 'unitsTP',
            'elements': 'THROUGH-PUT UNITS: '},
            {'type': 'input', 'name': 'defaultSetup',
            'elements': 'DEFAULT SETUP TIME (h): '}]

answers = ['PRIMA', 40, 120, 200, 'inches', 0.1]

data = zipToDict(items, answers)

print(data)
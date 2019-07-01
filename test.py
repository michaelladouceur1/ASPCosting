from utilities import zipDictAndListToDict

values = ['hello', 'stuff', 'no']
keys = [{'type': 'input', 'name': 'processCategoryName',
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

data = zipDictAndListToDict(keys, values)

print(data)
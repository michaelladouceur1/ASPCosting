from PyInquirer import prompt, Separator
from sys import platform
from os import system
import time

from utilities import zipDictAndListToDict, dfToList
from style import style_1
from server import Server
# from test import HotKeys
from dxf import DXF


spacing = '   '
divider = '   ---------------'

# UTILITIES

def clear():
    if platform == 'win32':
        system('cls')
    else:
        system('clear')

def error_message(error):
    print(f'AN ERROR OCCURRED ACCESSING "{error}". RETURNING TO MAIN MENU')
    time.sleep(4)
    return main_menu()

routeElements = {
    # LEVEL 1
    'mainMenu': 'MAIN MENU',
    # LEVEL 2
    'newCosting': 'NEW COSTING',
    'viewCosting': 'VIEW COSTING',
    'editCosting': 'EDIT COSTING',
    'analytics': 'ANALYTICS',
    'maintenance': 'MAINTENANCE',
    # LEVEL 3
    'costPart': 'COST PART',
    'costProductAssembly': 'COST PRODUCT ASSEMBLY',
    'costProductFamily': 'COST PRODUCT FAMILY',
    'returnMainMenu': 'RETURN TO MAIN MENU',
    'addWorkCenter': 'ADD WORK CENTER',
    'addProcessCategory': 'ADD PROCESS CATEGORY',
    'addMaterialStandards': 'ADD MATERIAL STANDARDS',
    # LEVEL 4
    'addMaterialType': 'ADD MATERIAL TYPE',
    'addMaterial': 'ADD MATERIAL',
    'addGauge': 'ADD GAUGE',
    # RETURN
    'returnToMainMenu': 'RETURN TO MAIN MENU'
}

inputElements = {
    'materialType': ['SHEET METAL', 'BAR STOCK'],
    'material': ['HR STEEL', 'CR STEEL', 'STAINLESS']
}

# VIEWS

class View:
    def __init__(self, title, version, items):
        self.title = title
        self.version = version
        self.items = items
        self.version = version
        self.answer = []
        self.routes = {
            routeElements['mainMenu']: main_menu,
            routeElements['newCosting']: new_costing,
            routeElements['viewCosting']: view_costing,
            routeElements['analytics']: analytics,
            routeElements['maintenance']: maintenance,
            routeElements['costPart']: cost_part,
            routeElements['costProductAssembly']: cost_product_assembly,
            routeElements['costProductFamily']: cost_product_family,
            routeElements['returnMainMenu']: main_menu,
            routeElements['addWorkCenter']: add_work_center,
            routeElements['addProcessCategory']: add_proccess_category,
            routeElements['addMaterialStandards']: add_material_standards,
            routeElements['addMaterialType']: add_material_type,
            routeElements['addMaterial']: add_material,
            routeElements['addGauge']: add_gauge,
            routeElements['returnToMainMenu']: main_menu
        }
        self.render()

    def render(self):
        clear()
        print(f'{spacing}{self.title}')
        print(divider)
        index = 0
        for item in self.items:
            if item['type'] == 'print':
                self.printData(index)
            elif item['type'] == 'list':
                self.answer.append(self.list(index))
            elif item['type'] == 'checkbox':
                self.answer.append(self.checkbox(index))
            elif item['type'] == 'input':
                self.answer.append(self.input(index))
            else:
                print('ERROR')
                continue
            index += 1
        if self.version == 'routing':
            self.router()
        elif self.version == 'input':
            return self.answer
        else:
            return error_message(self.answer)

    def router(self):
        for key in self.routes:
            if self.answer[0] == key:
                return self.routes[key]()
            else:
                continue
        return error_message(self.answer)

    def printData(self, index):
        for data in self.items[index]['elements']:
            print(f'  {data}')

    # TEMPLATE MENU ITEMS

    def list(self, index):
        message = self.items[index]['message']
        params = {
            'type': 'list',
            'name': 'list',
            'message': message,
            'choices': self.items[index]['elements']
        }
        answers = prompt(params, style=style_1)
        return answers['list']

    def checkbox(self, index):
        itemsMod = []
        for choice in self.items[index]['elements']:
            if choice[0] == '-':
                itemsMod.append(Separator(f'--{choice[1:]}--'))
            else:
                itemsMod.append({'name': choice})
        params = {
            'type': 'checkbox',
            'name': 'checkbox',
            'qmark': 'x',
            'message': '',
            'choices': itemsMod
        }
        answers = prompt(params, style=style_1)
        return answers['checkbox']

    def input(self, index):
        params = {
            'type': 'input',
            'name': 'input',
            'message': self.items[index]['elements']
        }
        answers = prompt(params, style=style_1)
        return answers['input']


################################ LEVEL 1 ####################################
def main_menu():

    v = View(title='ASP COSTING MODULE', version='routing', 
            items=[{'type': 'list', 'name': 'mainMenu', 'message': '',
                    'elements': [
                        routeElements['newCosting'], 
                        routeElements['viewCosting'], 
                        routeElements['editCosting'], 
                        routeElements['analytics'],
                        routeElements['maintenance']]}])
    
    print(v)

################################ LEVEL 2 ####################################

def new_costing():

    v = View(title='NEW COSTING MENU', version='routing', 
            items=[{'type': 'list', 'name': 'newCosting', 'message': '',
                    'elements': [
                        routeElements['costPart'], 
                        routeElements['costProductAssembly'], 
                        routeElements['costProductAssembly'], 
                        routeElements['analytics']]}])

def view_costing():

    v = View(title='VIEW COSTING MENU', version='routing', 
            items=[{'type': 'list', 'name': 'viewCosting', 'message': '',
                    'elements': [
                        'COST PART', 
                        'COST PRODUCT ASSEMBLY', 
                        'COST PRODUCT FAMILY', 
                        routeElements['returnToMainMenu']]}])

def edit_costing():

    v = View(title='EDIT COSTING MENU', version='routing', 
            items=[{'type': 'list', 'name': 'editCosting', 'message': '',
                    'elements': [
                        'COST PART', 
                        'COST PRODUCT ASSEMBLY', 
                        'COST PRODUCT FAMILY', 
                        routeElements['returnToMainMenu']]}])

def analytics():

    v = View(title='ANALYTICS MENU', version='routing', 
            items=[{'type': 'list', 'name': 'analytics', 'message': '',
                    'elements': [
                        routeElements['addWorkCenter'], 
                        routeElements['addProcessCategory'], 
                        routeElements['returnToMainMenu']]}])

def maintenance():

    v = View(title='MAINTENANCE MENU', version='routing', 
            items=[{'type': 'list', 'name': 'maintenance', 'message': '',
                    'elements': [
                        routeElements['addWorkCenter'], 
                        routeElements['addProcessCategory'],
                        routeElements['addMaterialStandards'], 
                        routeElements['returnToMainMenu']]}])

################################ LEVEL 3 ####################################

def cost_part():
    materialDF = Server().find('standards')['material'][0]
    gaugeDF = Server().find('standards')['gauge'][0]
    processCategoryDF = Server().find('standards')['processCategory'][0]
    material = dfToList(materialDF, 'materialName')
    gauge = dfToList(gaugeDF, 'gaugeName')
    processCategory = dfToList(processCategoryDF, 'processCategoryName')
    partNoItems = [{'type': 'input', 'name': 'partNumber',
            'elements': 'PART NUMBER: '}]
    partNo = View(title='PART COST MENU', version='input', 
        items=partNoItems)

    matItems = [{'type': 'list', 'name': 'material', 'message': '',
            'elements': material}]

    mat = View(title='PART COST MENU', version='input', 
        items=matItems)

    gaugeItems = [{'type': 'list', 'name': 'gauge', 'message': '',
            'elements': gauge}]

    ga = View(title='PART COST MENU', version='input', 
        items=gaugeItems)

    dxf = DXF(partNo.answer[0])
    blankx, blanky = dxf.blank()
    length = dxf.length() 
    blankInfo = [f'BLANK WIDTH: {blankx}', f'BLANK HEIGHT: {blanky}',f'BLANK LASER PATH: {length}']

    processItems = [{'type': 'print', 'name': 'blank',
            'elements': blankInfo},
            {'type': 'list', 'name': 'processCategoryName', 'message': 'PROCESS CATEGORY: ',
            'elements': processCategory},
            {'type': 'input', 'name': 'operationNumber',
            'elements': 'OPERATION NUMBER: '},
            {'type': 'input', 'name': 'operationName',
            'elements': 'OPERATION NAME: '},
            {'type': 'input', 'name': 'workCenterID',
            'elements': 'WORK CENTER ID: '},
            {'type': 'input', 'name': 'setup',
            'elements': 'SETUP TIME: '},
            {'type': 'input', 'name': 'operationTime',
            'elements': 'TIME PER OPERATION: '},
            {'type': 'input', 'name': 'operationQuantity',
            'elements': 'OPERATION QUANTITY: '},]
    process = View(title='PART COST MENU', version='input', 
        items=processItems)
    print(partNo.answer)
    print(mat.answer)
    print(ga.answer)
    print(process.answer)

def cost_product_assembly():
    print(f'{spacing}PRODUCT ASSEMBLY COST MENU')

def cost_product_family():
    print(f'{spacing}PRODUCT FAMILY COST MENU')

#### MAINTENANCE

def add_work_center():
    processCategory = Server().find('standards')['processCategory'][0]
    elements = []
    for item in processCategory:
        elements.append(item['processCategoryName'])
    items = [{'type': 'input', 'name': 'workCenterID',
            'elements': 'WORK CENTER ID NUMBER: '},
            {'type': 'input', 'name': 'workCenterName',
            'elements': 'WORK CENTER NAME: '},
            {'type': 'list', 'name': 'processCategory', 'message': 'WORK CENTER PROCESS: ',
            'elements': elements},
            {'type': 'input', 'name': 'hourlyRate',
            'elements': 'HOURLY RATE: '},
            {'type': 'input', 'name': 'hourlyOverhead',
            'elements': 'HOURLY OVERHEAD: '},
            {'type': 'input', 'name': 'estimatedTP',
            'elements': 'ESTIMATED THROUGH-PUT: '},
            {'type': 'input', 'name': 'estimatedSetup',
            'elements': 'ESTIMATED SETUP TIME: '}]
    v = View(title='ADD PROCESS MENU', version='input',
        items=items)

    data = zipDictAndListToDict(items, v.answer)

    Server().updateOne('standards', 'push', 'workCenter', data)

    maintenance()

def add_proccess_category():
    data = Server().find('standards')['processCategory'][0]
    print(data)
    elements = []
    for item in data:
        elements.append(item['processCategoryName'])
    items = [{'type': 'print', 'name': 'processes',
            'elements': elements},
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
    v = View(title='ADD PROCESS CATEGORY', version='input',
        items=items)

    data = zipDictAndListToDict(items, v.answer)
    print(type(data))

    Server().updateOne('standards', 'push', 'processCategory', data)

    maintenance()

def add_material_standards():
    v = View(title='MAINTENANCE MENU', version='routing', 
            items=[{'type': 'list', 'name': 'addMaterialStandards', 'message': '',
                    'elements': [
                        routeElements['addMaterialType'], 
                        routeElements['addMaterial'],
                        routeElements['addGauge'], 
                        routeElements['returnToMainMenu']]}])

################################ LEVEL 4 ####################################

def add_material_type():
    elements = Server().find('standards')['materialType'][0]
    items = [{'type': 'print', 'name': 'materialTypes',
            'elements': elements},
            {'type': 'input', 'name': 'materialType',
            'elements': 'MATERIAL TYPE: '}]
    v = View(title='ADD MATERIAL TYPE', version='input',
        items=items)

    Server().updateOne('standards', 'push', 'materialType', v.answer[0])

    add_material_standards()

def add_material():
    data = Server().find('standards')['material'][0]
    materialType = Server().find('standards')['materialType'][0]
    material = []
    for item in data:
        material.append(item['materialName'])
    items = [{'type': 'print', 'name': 'material',
            'elements': material},
            {'type': 'list', 'name': 'materialType', 'message': 'MATERIAL TYPE: ',
            'elements': materialType},
            {'type': 'input', 'name': 'materialName',
            'elements': 'MATERIAL NAME: '},
            {'type': 'input', 'name': 'materialDensity',
            'elements': 'MATERIAL DENSITY: '}]
    v = View(title='ADD MATERIAL', version='input',
        items=items)

    data = zipDictAndListToDict(items, v.answer)

    Server().updateOne('standards', 'push', 'material', data)

    add_material_standards()

def add_gauge():
    data = Server().find('standards')['gauge'][0]
    gauge = []
    for item in data:
        gauge.append(f'{item["gaugeName"]} : {item["gaugeThickness"]}')
    items = [{'type': 'print', 'name': 'material',
            'elements': gauge},
            {'type': 'input', 'name': 'gaugeName',
            'elements': 'ADD GAUGE NAME: '},
            {'type': 'input', 'name': 'gaugeThickness',
            'elements': 'ADD GAUGE THICKNESS: '}]
    v = View(title='ADD MATERIAL', version='input',
        items=items)

    data = zipDictAndListToDict(items, v.answer)

    Server().updateOne('standards', 'push', 'gauge', data)

    add_material_standards()

if __name__ == '__main__':
    # HotKeys(main_menu)
    main_menu()
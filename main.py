from PyInquirer import prompt, Separator
from style import style_1
from os import system
import time

spacing = '   '
divider = '   ---------------'

# UTILITIES

def clear():
    system('cls')
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
    # LEVEL 3
    'costPart': 'COST PART',
    'costProductAssembly': 'COST PRODUCT ASSEMBLY',
    'costProductFamily': 'COST PRODUCT FAMILY',
    'returnMainMenu': 'RETURN TO MAIN MENU',
    'addWorkCenter': 'ADD WORK CENTER',
    'addProcessCategory': 'ADD PROCESS CATEGORY'
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
            routeElements['costPart']: cost_part,
            routeElements['costProductAssembly']: cost_product_assembly,
            routeElements['costProductFamily']: cost_product_family,
            routeElements['returnMainMenu']: main_menu,
            routeElements['addWorkCenter']: add_work_center,
            routeElements['addProcessCategory']: add_proccess_category
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
            print(f'{spacing}{data}')

    # TEMPLATE MENU ITEMS

    def list(self, index):
        params = {
            'type': 'list',
            'name': 'list',
            'message': '',
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


#### LEVEL 1 ####
def main_menu():

    v = View(title='ASP COSTING MODULE', version='routing', 
            items=[{'type': 'list',
                    'elements': [routeElements['newCosting'], routeElements['viewCosting'], routeElements['editCosting'], routeElements['analytics']]}])

#### LEVEL 2 ####

def new_costing():

    v = View(title='NEW COSTING MENU', version='routing', 
            items=[{'type': 'list',
                    'elements': [routeElements['costPart'], routeElements['costProductAssembly'], routeElements['costProductAssembly'], routeElements['analytics']]}])

def view_costing():

    v = View(title='VIEW COSTING MENU', version='routing', 
            items=[{'type': 'list',
                    'elements': ['COST PART', 'COST PRODUCT ASSEMBLY', 'COST PRODUCT FAMILY', 'RETURN TO MAIN MENU']}])

def edit_costing():

    v = View(title='EDIT COSTING MENU', version='routing', 
            items=[{'type': 'list',
                    'elements': ['COST PART', 'COST PRODUCT ASSEMBLY', 'COST PRODUCT FAMILY', 'RETURN TO MAIN MENU']}])

def analytics():

    v = View(title='ANALYTICS MENU', version='routing', 
            items=[{'type': 'list',
                    'elements': [routeElements['addWorkCenter'], routeElements['addProcessCategory'], 'RETURN TO MAIN MENU']}])

#### LEVEL 3 ####

def cost_part():

    v = View(title='PART COST MENU', version='input', 
        items=[{'type': 'list', 'name': 'materialType',
                'elements': inputElements['materialType']},
                {'type': 'list', 'name': 'material',
                'elements': inputElements['material']}])
    print(v.answer)

def cost_product_assembly():
    print(f'{spacing}PRODUCT ASSEMBLY COST MENU')

def cost_product_family():
    print(f'{spacing}PRODUCT FAMILY COST MENU')

def add_work_center():
    v = View(title='ADD PROCESS MENU', version='input',
        items=[{'type': 'input', 'name': 'workCenterID',
                'elements': 'WORK CENTER ID NUMBER: '},
                {'type': 'list', 'name': 'workCenterCategory',
                'elements': 'WORK CENTER ID NUMBER: '}])
    print(v.answer)

def add_proccess_category():
    v = View(title='ADD PROCESS CATEGORY', version='input',
        items=[{'type': 'print', 'name': 'processes',
                'elements': ['Press Brake', 'Laser', 'Stamping']},
                {'type': 'input', 'name': 'newProcess',
                'elements': 'NEW PROCESS: '}])

    print(type(v.answer[0]))


if __name__ == '__main__':
    main_menu()
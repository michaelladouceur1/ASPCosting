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
    'mainMenu': 'MAIN MENU',
    'newCosting': 'NEW COSTING',
    'viewCosting': 'VIEW COSTING',
    'editCosting': 'EDIT COSTING',
    'analytics': 'ANALYTICS',
    'costPart': 'COST PART',
    'costProductAssembly': 'COST PRODUCT ASSEMBLY',
    'costProductFamily': 'COST PRODUCT FAMILY',
    'returnMainMenu': 'RETURN TO MAIN MENU'
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
            routeElements['costPart']: cost_part,
            routeElements['costProductAssembly']: cost_product_assembly,
            routeElements['costProductFamily']: cost_product_family,
            routeElements['returnMainMenu']: main_menu
        }
        self.render()

    def render(self):
        clear()
        print(f'{spacing}{self.title}')
        print(divider)
        index = 0
        print(self.items)
        for item in self.items:
            if item['type'] == 'list':
                self.answer.append(self.list(index))
            elif item['type'] == 'checkbox':
                self.answer.append(self.checkbox(index))
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
                    'elements': ['COST PART', 'COST PRODUCT ASSEMBLY', 'COST PRODUCT FAMILY', 'RETURN TO MAIN MENU']}])

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


if __name__ == '__main__':
    main_menu()
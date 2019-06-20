from PyInquirer import prompt, Separator
from style import style_1
from os import system
import time

spacing = '   '
divider = '   ---------------'

# TEMPLATE MENU ITEMS

# def list(choices):
#     params = {
#         'type': 'list',
#         'name': 'list',
#         'message': '',
#         'choices': choices
#     }
#     answers = prompt(params, style=style_1)
#     return answers['list']

# def checkbox(choices):
#     choicesMod = []
#     for choice in choices:
#         if choice[0] == '-':
#             choicesMod.append(Separator(f'--{choice[1:]}--'))
#         else:
#             choicesMod.append({'name': choice})
#     params = {
#         'type': 'checkbox',
#         'name': 'checkbox',
#         'qmark': 'x',
#         'message': '',
#         'choices': choicesMod
#     }
#     answers = prompt(params, style=style_1)
#     return answers['checkbox']

# UTILITIES

def clear():
    system('cls')

def error_message(error):
    print(f'AN ERROR OCCURRED ACCESSING "{error}". RETURNING TO MAIN MENU')
    time.sleep(4)
    return main_menu()

# VIEWS

class View:
    def __init__(self, title, version, items):
        self.title = title
        self.version = version
        self.items = items
        self.version = version
        self.answer = ''
        self.functions = functions
        self.render()

    def render(self):
        clear()
        print(f'{spacing}{self.title}')
        print(divider)
        if self.version == 'list':
            self.answer = self.list()
        elif self.version == 'checkbox':
            self.answer = self.checkbox()
        renderChange()

    def renderChange(self):
        for item, func in self.items, self.functions:
            if item == self.answer:
                return func
        return error_message()


    def list(self):
        params = {
            'type': 'list',
            'name': 'list',
            'message': '',
            'choices': self.items
        }
        answers = prompt(params, style=style_1)
        return answers['list']

    def checkbox(self):
        itemsMod = []
        for choice in self.items:
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
    # clear()
    # print(f'{spacing}ASP COSTING MODULE')
    # print(divider)
    # answer = list(
    #     ['NEW COSTING', 'VIEW COSTING', 'EDIT COSTING', 'ANALYTICS']
    #     )

    # clear()
    v = View(title='ASP COSTING MODULE', version='list', items=[
        'NEW COSTING', 'VIEW COSTING', 'EDIT COSTING', 'ANALYTICS'
        ], functions=[
        new_costing(), view_costing()
        ])

    # if v.answer == 'NEW COSTING':
    #     return new_costing()
    # elif v.answer == 'VIEW COSTING':
    #     return view_costing()
    # else:
    #     return error_message(answer)

#### LEVEL 2 ####

def new_costing():
    v = View(title='NEW COSTING MENU', version='list', items=[
        'COST PART', 'COST PRODUCT ASSEMBLY', 'COST PRODUCT FAMILY', 'RETURN TO MAIN MENU'
        ], functions=[
        cost_part(), cost_product_assembly(), cost_product_family(), main_menu()
        ])

    # print(f'{spacing}NEW COSTING MENU')
    # print(divider)
    # answer = list(
    #     ['COST PART', 'COST PRODUCT ASSEMBLY', 'COST PRODUCT FAMILY', 'RETURN TO MAIN MENU']
    #     )

    # clear()

    # if answer == 'COST PART':
    #     return cost_part()
    # elif answer == 'COST PRODUCT ASSEMBLY':
    #     return cost_product_assembly()
    # elif answer == 'COST PRODUCT FAMILY':
    #     return cost_product_family()
    # elif answer == 'RETURN TO MAIN MENU':
    #     return main_menu()
    # else:
    #     return error_message()


def view_costing():
    print(f'{spacing}VIEW COSTING MENU')

#### LEVEL 3 ####

def cost_part():
    print(f'{spacing}PART COST MENU')
    print(divider)
    # answer = checkbox(
    #     ['-HELLO', 'STUFF', 'MORE STUFF']
    #     )

def cost_product_assembly():
    print(f'{spacing}PRODUCT ASSEMBLY COST MENU')

def cost_product_family():
    print(f'{spacing}PRODUCT FAMILY COST MENU')


if __name__ == '__main__':
    main_menu()
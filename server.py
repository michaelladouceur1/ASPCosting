from mongoengine import *
from model import *

# def update(document, item, value, mode):
#     collection = document
#     update = collection.objects[0]
#     # eval(document.objects(id=update.id).update_one(mode+'__'+item=value))
#     eval(f'{document}.objects(id={update}.id).update_one({mode}__{item}={str(value)})')

# # update = Standards.objects[0]
# # collection = Standards.objects

# # collection(id=update.id).update_one(add_to_set__materialType='fabric')

# update(Standards, 'material', 'stainless', 'push')

def update(material):
    update = Standards.objects[0]
    Standards.objects.update(material)

update(StandardsMaterial(
    materialName = 'stainless'
))
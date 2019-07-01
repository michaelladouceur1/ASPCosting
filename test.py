from model import *
from server import Server
from bson import DBRef

standards = Server().find('standards')
id = standards._id[0]

partSeed = Part().Model

partSeed['partNumber'] = 'WAR36HRTB.40'
# partSeed['material'] = 

print(partSeed)
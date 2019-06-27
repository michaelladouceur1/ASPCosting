from server import Server
import pprint

server = Server()

data = {}

# response = server.find('standards', data)

server.updateOne('standards', 'push', 'materialType', 'plastic')
class tc():

	def raiseError(mode, input):
		raise Exception(f'The input ({input}) is not equal to a {mode}')

	def verify(mode, input):
		if type(input) == mode:
			pass
		else:
			tc.raiseError(mode, input)

	def check(mode=any, input=[]):
		if type(input) == list:
			if len(input) > 0:
				for i in input:
					tc.verify(mode=mode, input=i)
		else:
			tc.verify(mode=mode, input=input)

class Model():
	def __init__(self):
		self.material = {
			'materialName': str,
			'materialType': str,
			'materialDensity': float
		}

model = Model()
refModel = Model()

# model.material['materialName'] = ['carbon steel']
# model.material['materialType'] = 'sheet metal'
# model.material['materialDensity'] = 4000.0

# if len(model.material) > 0:
# 	for item in model.material:
# 		mode = refModel.material[item]
# 		input = model.material[item]
# 		print(mode)
# 		print(input)
# 		tc.check(mode, input)

def vm(model, refModel, path):
	refModel = f'{refModel}()'
	for i in path:
		refModel += f'.{i}'
		print(refModel)

	result = eval(refModel)
	print(result)
	print(model.path)

vm(model, 'Model', ['material'])
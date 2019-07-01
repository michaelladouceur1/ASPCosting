class CheckType:
	def __init__(self, mode, input):
		self.mode = mode
		self.input = input
		self.check()

	def raiseError(self):
		raise Exception(f'The input ({self.input}) is not equal to a {self.mode}')

	def verify(self, i):
		if type(i) == self.mode:
			pass
		else:
			self.raiseError()

	def check(self):
		if type(self.input) == list and type(self.mode) != list:
			if len(self.input) > 0:
				for i in self.input:
					self.verify(i)
		elif type(self.input) == list and type(self.mode) == list:
			self.mode = self.mode[0]
			if len(self.input) > 0:
				for i in self.input:
					self.verify(i)
		else:
			self.verify(self.input)

def zipDictAndListToDict(keys, values):
	newKeys = []
	for key in keys:
		if key['type'] == 'print':
			continue
		else:
			newKeys.append(key['name'])
	data = dict(zip(newKeys, values))
	return data

def dfToList(df, category):
	arr = []
	for item in df:
		arr.append(item[category])
	return arr
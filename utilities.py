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

def listToUpper(values):
	values = map(lambda x:x.upper(), values)
	return values

def zipDictAndListToDict(keys, values):
	newKeys = []
	values = listToUpper(values)
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

def outputList(data, *args):
	list = []
	for item in data:
		for i in args:
			# print(getattr(item, i))
			list.append(getattr(item, i))
	return list
class Vektor(object):
	"""docstring for Vektor"""
	def __init__(self, *args):
		self.__vars__ = args

	def __add__(self, other):
		if (type(other) is int) or (type(other) is float): 
			self.__vars__ = [i+other for i in self.__vars__]
		if (type(other) is list) or (type(other) is Vektor):
			for i in range(other):
				self.__vars__[i] += other[i]

	def __sub__(self, other):
		if (type(other) is int) or (type(other) is float): 
			self.__vars__ = [i-other for i in self.__vars__]
		if (type(other) is list) or (type(other) is Vektor):
			for i in range(other):
				self.__vars__[i] -= other[i]

	def __mul__(self, other):
		self.__vars__ = [i*other for i in self.__vars__]

	def __truediv__(self, other):
		self.__vars__ = [i/other for i in self.__vars__]

	def __getitem__(self, key):
		return self.__vars__[key]

	def __setitem__(self, key, value):
		self.__vars__[key] = value


		
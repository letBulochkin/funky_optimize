class Vektor(object):
	"""docstring for Vektor"""
	def __init__(self, *args):
		self.__vars__ = []
		for i in args:
			self.__vars__.append(i)
		print(self.__vars__)

	def __repr__(self):
		responce = "Точка ("
		s = ", ".join(str(i) for i in self.__vars__)
		responce = responce + s + ")"
		return responce

	def __add__(self, other):
		if (type(other) is int) or (type(other) is float): 
			self.__vars__ = [i+other for i in self.__vars__]
		if (type(other) is list) or (type(other) is Vektor):
			for i in range(len(other)):
				self.__vars__[i] += other[i]
		return Vektor(*self.__vars__)

	def __sub__(self, other):
		if (type(other) is int) or (type(other) is float): 
			self.__vars__ = [i-other for i in self.__vars__]
		if (type(other) is list) or (type(other) is Vektor):
			for i in range(len(other)):
				self.__vars__[i] -= other[i]
		return Vektor(*self.__vars__)

	def __mul__(self, other):
		self.__vars__ = [i*other for i in self.__vars__]
		return Vektor(*self.__vars__)

	def __truediv__(self, other):
		print(self.__vars__)
		print(type(other))
		self.__vars__ = [i/other for i in self.__vars__]
		return Vektor(*self.__vars__)

	def __getitem__(self, key):
		return self.__vars__[key]

	def __setitem__(self, key, value):
		self.__vars__[key] = value
		return Vektor(*self.__vars__)

	def __len__(self):
		return len(self.__vars__)


		
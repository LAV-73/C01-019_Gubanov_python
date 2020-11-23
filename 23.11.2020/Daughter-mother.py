class People():
	__role = None
	__name = None
	def __init__(self, role, name):
		self.__role = role
		self.__name = name
	def getRole(self):
		return self.__role
	def getName(self):
		return self.__name
	def __str__(self):
		return self.get_str()

class Mother(People):
	def get_str(self):
		return self.getRole() + "'s name: " + self.getName()

class Daughter(People):
	def get_str(self):
		return self.getRole() + "'s name: " + self.getName()

if __name__ == "__main__" :
	mother1 = Mother('Mother', input())
	daughter1 = Daughter('Daughter', input())
	
	print(mother1)
	print(daughter1)

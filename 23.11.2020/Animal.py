class Animal():
	__name = None
	__age = None

	def __init__(self, name_and_age):
		self.__name, self.__age = name_and_age.split()
	
	def getName(self):
		return self.__name
	
	def getAge(self):
		return self.__age

	def __str__(self):
		return self.get_str()

class Zebra(Animal):
	__type = 'Zebra'
	def get_str(self):
		return ('Type of animal: ' + self.__type + '; Name: ' + self.getName() + '; Age: ' + self.getAge())

class Dolphin(Animal):
	__type = 'Dolphin'
	def get_str(self):
		return ('Type of animal: ' + self.__type + '; Name: ' + self.getName() + '; Age: ' + self.getAge())

if __name__ == "__main__" :
	print("Please, write Name and Age of Dolhine in line in this order:")
	dolphin1 = Dolphin(input())
	print("Please, write Name and Age of Zebra in line in this order:")	
	zebra1 = Zebra(input())

	print(dolphin1)
	print(zebra1)

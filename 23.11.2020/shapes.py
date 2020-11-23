class Shape():
	__side_length = None
	__height_legnth = None
	def setParam(self):
		self.__side_length, self.__height_length = list(map(float, input().split()))
	def getSideLength(self):
		return self.__side_length
	def getHeightLength(self):
		return self.__height_length

class Triangle(Shape):
	def area(self):
		return self.getSideLength() * self.getHeightLength() / 2

class Rectangle(Shape):
	def area(self):
		return self.getSideLength() * self.getHeightLength()

if __name__ == '__main__':
	triangle1 = Triangle()
	rectangle1 = Rectangle()

	triangle1.setParam()
	rectangle1.setParam()
	
	print("Площадь треугольника: ", round(triangle1.area(), 2))
	print("Площадь прямоугольника: ", round(rectangle1.area(), 2))

class Shape():
	side_length = None
	height_legnth = None
	def getParam(self):
		self.side_length, self.height_length = list(map(float, input().split()))

class Triangle(Shape):
	def area(self):
		return self.side_length * self.height_length / 2

class Rectangle(Shape):
	def area(self):
		return self.side_length * self.height_length

if __name__ == '__main__':
	triangle1 = Triangle()
	rectangle1 = Rectangle()

	triangle1.getParam()
	rectangle1.getParam()
	
	print("Площадь треугольника: ", round(triangle1.area(), 3))
	print("Площадь прямоугольника: ", round(rectangle1.area(), 3))

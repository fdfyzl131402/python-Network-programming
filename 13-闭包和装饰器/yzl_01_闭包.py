# 面向对象
class Line5(object):
	def __init__(self, k, b):
		self.k = k
		self.b = b

	def __call__(self, x):
		print(self.k * x + self.b)


line_5_1 = Line5(1, 2)
line_5_1(0)
line_5_1(1)
line_5_1(2)
line_5_2 = Line5(11, 22)
line_5_2(0)
line_5_2(1)
line_5_2(2)

# 闭包 
# 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包


def line6(k, b):
	def create_y(x):
		print(k*x+b)
	return create_y


line_6_1 = line6(1, 2)
line_6_1(0)
line_6_1(1)
line_6_1(2)
line_6_2 = line6(11, 22)
line_6_2(0)
line_6_2(1)
line_6_2(2)

# 思考: 函数 匿名函数 闭包 对象当作实参时，有什么区别？
# 1. 匿名函数能够完成基本的简单功能，，，传递是这个函数的引用 只有功能
# 2. 普通函数能够完成较为复杂的功能，，，传递是这个函数的引用 只有功能
# 3. 闭包能够将较为复杂的功能，，，传递是这个闭包中的函数以及数据，因此传递是功能+数据
# 4. 对象能够完成最为负责的功能，，，传递是很多数据+很多功能，因此传递是功能+数据

# 修改外部数据
x = 300


def test1():
	x = 200

	def test2():
		# nonlocal x
		global x
		print("----1----- %s" % x)
		x = 100
		print("----2--- %s" % x)
	return test2


t1 = test1()
t1()

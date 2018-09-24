from math import hypot
'''
此例包含了一个 Vector 类的实现，
上面提到的操作在代码里是用这些特殊方法实现的：__repr__、__abs__、  __add__ 和 __mul__。
'''


class Vector:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	# 把一个对象用字符串的形式表达出来以便辨认
	def __repr__(self):
		return 'Vector(%r, %r)' % (self.x, self.y)

	def __abs__(self):
		return hypot(self.x, self.y)
	
	'''
	def __bool__(self):
		return bool(abs(self))
	'''
	
	# 更高效的bool
	def __bool__(self):
		return bool(self.x or self.y)

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __mul__(self, scalar):
		# 参数验证
		if not isinstance(scalar, (int, float)):
			raise TypeError()
		return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
	a = Vector(5, 12)
	b = Vector(3, 4)
	print('a is %s ' % a)
	print('b is %s ' % b)
	print(abs(a), abs(b))
	print(a+b)
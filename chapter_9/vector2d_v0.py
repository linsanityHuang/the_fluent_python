from array import array
import math

class Vector2d:
	typecode = 'd'
	
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
		
	def __iter__(self):
		return (i for i in (self.x, self.y))
	
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r}, {!r})'.format(class_name, *self)
	
	def __str__(self):
		return str(tuple(self))
	
	def __bytes__(self):
		return (bytes([ord(self.typecode)]) +
				bytes(array(self.typecode, self)))
	
	def __eq__(self, other):
		return tuple(self) == tuple(other)
	
	def __abs__(self):
		return math.hypot(self.x, self.y)
	
	def __bool__(self):
		return bool(abs(self))


if __name__ == '__main__':
	v1 = Vector2d(3, 4)
	# Vector2d 实例的分量可以直接通过属性访问（无需调用读值方法）
	print(v1.x, v1.y)
	'''3.0 4.0'''
	# Vector2d 实例可以拆包成变量元组
	x, y = v1
	print(x, y)
	'''3.0 4.0'''
	# repr 函数调用 Vector2d 实例，得到的结果类似于构建实例的源码。
	v1
	'''Vector2d(3.0, 4.0)'''
	# 这里使用 eval 函数，表明 repr 函数调用 Vector2d 实例得到的是对构造方法的准确表述。
	v1_clone = eval(repr(v1))
	# Vector2d 实例支持使用 == 比较；这样便于测试
	print(v1 == v1_clone)
	'''True'''
	# print 函数会调用 str 函数，对 Vector2d 来说，输出的是一个有序对
	print(v1)
	'''(3.0, 4.0)'''
	# bytes 函数会调用 __bytes__ 方法，生成实例的二进制表示形式
	octets = bytes(v1)
	print(octets)
	'''
	b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
	'''
	# abs 函数会调用 __abs__ 方法，返回 Vector2d 实例的模
	print(abs(v1))
	'''5.0'''
	# bool 函数会调用 __bool__ 方法，如果 Vector2d 实例的模为零，返回 False，否则返回 True
	print(bool(v1), bool(Vector2d(0, 0)))
	'''True False'''

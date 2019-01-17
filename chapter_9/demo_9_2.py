from array import array
import math


class Vector2d:
	# typecode 是类属性，在 Vector2d 实例和字节序列之间转换时使用。
	typecode = 'd'
	
	def __init__(self, x, y):
		# 在 __init__ 方法中把 x 和 y 转换成浮点数，尽早捕获错误，
		# 以防调用 Vector2d 函数时传入不当参数。
		self.x = float(x)
		self.y = float(y)
		
	# 类方法使用 classmethod 装饰器修饰。
	@classmethod
	# 不用传入 self 参数；相反，要通过 cls 传入类本身
	def frombytes(cls, octets):
		# 从第一个字节中读取 typecode。
		typecode = chr(octets[0])
		# 使用传入的 octets 字节序列创建一个 memoryview，然后使用 typecode 转换。
		memv = memoryview(octets[1:]).cast(typecode)
		# 拆包转换后的 memoryview，得到构造方法所需的一对参数
		return cls(*memv)
	
	# 定义 __iter__ 方法，把 Vector2d 实例变成可迭代的对象，这样才能拆包（例如，x, y = my_vector） 。
	# 这个方法的实现方式很简单，直接调用生成器表达式一个接一个产出分量
	def __iter__(self):
		return (i for i in (self.x, self.y))

	def __repr__(self):
		class_name = type(self).__name__
		# __repr__ 方法使用 {!r} 获取各个分量的表示形式，然后插值，构成一个字符串；因为Vector2d 实例是可迭代的对象，
		# 所以 *self 会把 x 和 y 分量提供给 format 函数。
		return '{}({!r}, {!r})'.format(class_name, *self)

	def __str__(self):
		# 从可迭代的 Vector2d 实例中可以轻松地得到一个元组，显示为一个有序对。
		return str(tuple(self))

	def __bytes__(self):
		return (bytes([ord(self.typecode)]) +			#为了生成字节序列，我们把 typecode 转换成字节序列，然后……
				bytes(array(self.typecode, self)))		#……迭代 Vector2d 实例，得到一个数组，再把数组转换成字节序列
	
	def __eq__(self, other):
		# 为了快速比较所有分量，在操作数中构建元组。对 Vector2d 实例来说，可以这样做，不过仍有问题。参见下面的警告
		return tuple(self) == tuple(other)
	
	def __abs__(self):
		# 模是 x 和 y 分量构成的直角三角形的斜边长。
		return math.hypot(self.x, self.y)
	
	def __bool__(self):
		# __bool__ 方法使用 abs(self) 计算模，然后把结果转换成布尔值，因此，0.0 是 False，非零值是 True。
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

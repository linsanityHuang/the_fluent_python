from array import array
import math


class Vector2d:
	# typecode 是类属性，在 Vector2d 实例和字节序列之间转换时使用。
	typecode = 'd'
	
	def __init__(self, x, y):
		# 在 __init__ 方法中把 x 和 y 转换成浮点数，尽早捕获错误，以防调用 Vector2d 函数时传入不当参数。
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

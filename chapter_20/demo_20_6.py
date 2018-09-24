import abc

'''
示例 20-6　model_v5.py：重构后的描述符类
'''


# AutoStorage 类提供了之前 Quantity 描述符的大部分功能
class AutoStorage:
	__counter = 0
	
	def __init__(self):
		cls = self.__class__
		prefix = cls.__name__
		index = cls.__counter
		self.storage_name = '_{}#{}'.format(prefix, index)
		cls.__counter += 1
	
	def __get__(self, instance, owner):
		if instance is None:
			return self
		else:
			return getattr(instance, self.storage_name)
	
	def __set__(self, instance, value):
		setattr(instance, self.storage_name, value)


# Validated 是抽象类，不过也继承自 AutoStorage 类
class Validated(abc.ABC, AutoStorage):
	
	def __set__(self, instance, value):
		# __set__ 方法把验证操作委托给 validate 方法
		value = self.validate(instance, value)
		# 然后把返回的 value 传给超类的 __set__ 方法，存储值
		super().__set__(instance, value)
	
	# 在这个类中，validate 是抽象方法
	@abc.abstractmethod
	def validate(self, instance, value):
		"""return validated value or raise ValueError"""


# Quantity 和 NonBlank 都继承自 Validated 类
class Quantity(Validated):
	"""a number greater than zero"""
	
	def validate(self, instance, value):
		if value <= 0:
			raise ValueError('value must be > 0')
		return value
	

class NonBlank(Validated):
	"""a string with at least one non-space character"""
	
	def validate(self, instance, value):
		value = value.strip()
		if len(value) == 0:
			raise ValueError('value cannot be empty or blank')
		# 要求具体的 validate 方法返回验证后的值，借机可以清理、转换或规范化接收的数据。
		# 这里，我们把 value 首尾的空白去掉，然后将其返回
		return value

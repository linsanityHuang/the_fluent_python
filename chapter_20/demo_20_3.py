'''
此外，为了给用户提供内省和其他元编程技术支持，通过类访问托管属性时，最好让 __get__ 方法返回描述符实例。

示例 20-3 对示例 20-2 做了小幅改动，为 Quantity.__get__ 方法添加了一些逻辑。

通过托管类调用时，__get__ 方法返回描述符的引用
'''


class Quantity:
	__counter = 0
	
	def __init__(self):
		cls = self.__class__
		prefix = cls.__name__
		index = cls.__counter
		self.storage_name = '_{}#{}'.format(prefix, index)
		cls.__counter += 1
	
	def __get__(self, instance, owner):
		if instance is None:
			# 如果不是通过实例调用，返回描述符自身
			return self
		else:
			# 否则，像之前一样，返回托管属性的值
			return getattr(instance, self.storage_name)
	
	def __set__(self, instance, value):
		if value > 0:
			setattr(instance, self.storage_name, value)
		else:
			raise ValueError('value must be > 0')


class LineItem:
	weight = Quantity()
	price = Quantity()
	
	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price
	
	def subtotal(self):
		return self.weight * self.price


if __name__ == '__main__':
	print(LineItem.price)
	'''<__main__.Quantity object at 0x1014e44e0>'''
	br_nuts = LineItem('Brazil nuts', 10, 34.95)
	print(br_nuts.price)
	'''34.95'''

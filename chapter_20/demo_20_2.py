'''
示例 20-2　bulkfood_v4.py：每个 Quantity 描述符都有独一无二的 storage_name

这里可以使用内置的高阶函数 getattr 和 setattr 存取值，无需使用 instance.__dict__，

因为托管属性和储存属性的名称不同，所以把储存属性传给 getattr 函数不会触发描述符，

不会像示例 20-1 那样出现无限递归。
'''


class Quantity:
	
	# __counter 是 Quantity 类的类属性，统计 Quantity 实例的数量
	__counter = 0
	
	def __init__(self):
		# cls 是 Quantity 类的引用
		cls = self.__class__
		prefix = cls.__name__
		index = cls.__counter
		# 每个描述符实例的 storage_name 属性都是独一无二的，因为其值由描述符类的名称和__counter 属性的当前值构成（例如，_Quantity#0）
		self.storage_name = '_{}#{}'.format(prefix, index)
		# 递增 __counter 属性的值
		cls.__counter += 1
	
	# 我们要实现 __get__ 方法，因为托管属性的名称与 storage_name 不同。稍后会说明owner 参数
	def __get__(self, instance, owner):
		# 使用内置的 getattr 函数从 instance 中获取储存属性的值
		return getattr(instance, self.storage_name)
	
	def __set__(self, instance, value):
		if value > 0:
			# 使用内置的 setattr 函数把值存储在 instance 中
			setattr(instance, self.storage_name, value)
		else:
			raise ValueError('value must be > 0')
		
		
class LineItem:
	
	# 现在，不用把托管属性的名称传给 Quantity 构造方法。这是这一版的目标
	weight = Quantity()
	price = Quantity()
	
	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price
	
	def subtotal(self):
		return self.weight * self.price


if __name__ == '__main__':
	coconuts = LineItem('Brazilian coconut', 20, 17.95)
	print(coconuts.weight, coconuts.price)
	print(getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1'))

'''
示例 20-1 是 Quantity 描述符类和新版 LineItem 类，用到两个 Quantity 实例。

示例 20-1　bulkfood_v3.py：使用 Quantity 描述符管理 LineItem 的属性

在示例 20-1 中，各个托管属性的名称与储存属性一样，而且读值方法不需要特殊的逻辑，所以 Quantity 类不需要定义 __get__ 方法。
'''


# 描述符基于协议实现，无需创建子类
class Quantity:
	
	def __init__(self, storage_name):
		# Quantity 实例有个 storage_name 属性，这是托管实例中存储值的属性的名称
		self.storage_name = storage_name
	
	# 尝 试 为 托 管 属 性 赋 值 时， 会 调 用 __set__ 方 法
	# 这 里，self 是 描 述 符 实 例（ 即LineItem.weight 或 LineItem.price） ，
	# instance 是托管实例（LineItem 实例） ，value 是要设定的值。
	def __set__(self, instance, value):
		if value > 0:
			# 这里，必须直接处理托管实例的 __dict__ 属性；如果使用内置的 setattr 函数，会再次触发 __set__ 方法，导致无限递归
			instance.__dict__[self.storage_name] = value
		else:
			raise ValueError('value must be > 0')


class LineItem:
	
	# 第一个描述符实例绑定给 weight 属性。
	weight = Quantity('weight')
	# 第二个描述符实例绑定给 price 属性。
	price = Quantity('price')
	
	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price
	
	def subtotal(self):
		return self.weight * self.price


if __name__ == '__main__':
	truffle = LineItem('White truffle', 100, 0)
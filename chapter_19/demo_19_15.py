'''
假设有个销售散装有机食物的电商应用，客户可以按重量订购坚果、干果或杂粮。

在这个系统中，每个订单中都有一系列商品，而每个商品都可以使用示例 19-15 中的类表示。

示例 19-15　bulkfood_v1：最简单的 LineItem 类
'''


class LineItem:
	def __init__(self, description, weight, price):
		self.description = description
		# 这里已经使用特性的设值方法了，确保所创建实例的 weight 属性不能为负值
		self.weight = weight
		self.price = price
	
	def subtotal(self):
		return self.weight * self.price
	
	# @property 装饰读值方法
	@property
	# 实现特性的方法，其名称都与公开属性的名称一样——weight
	def weight(self):
		# 真正的值存储在私有属性 __weight 中
		return self.__weight
	
	# 被装饰的读值方法有个 .setter 属性，这个属性也是装饰器；这个装饰器把读值方法和设值方法绑定在一起
	@weight.setter
	def weight(self, value):
		# 如果值大于零，设置私有属性 __weight
		if value > 0:
			self.__weight = value
		# 否则，抛出 ValueError 异常
		else:
			raise ValueError('value must be > 0')


if __name__ == '__main__':
	raisins = LineItem('Golden raisins', -10, 6.95)
	print(raisins.subtotal())
	raisins.weight = -20
	print(raisins.subtotal())

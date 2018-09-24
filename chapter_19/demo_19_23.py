'''
我们将定义一个名为 quantity 的特性工厂函数，取这个名字是因为，在这个应用中要管理的属性表示不能为负数或零的量。

示例 19-23 是 LineItem 类的简洁版，用到了 quantity 特性的两个实例：一个用于管理 weight 属性，另一个用于管理 price 属性。
'''


# 示例 19-24 列出 quantity 特性工厂函数的实现。

# storage_name 参数确定各个特性的数据存储在哪儿；对 weight 特性来说，存储的名称是 'weight'
def quantity(storage_name):
	# qty_getter 函数的第一个参数可以命名为 self，但是这么做很奇怪，
	# 因为 qty_getter 函数不在类定义体中；instance 指代要把属性存储其中的 LineItem 实例
	def qty_getter(instance):
		# qty_getter 引用了 storage_name，把它保存在这个函数的闭包里；值直接从 instance.
		# __dict__ 中获取，为的是跳过特性，防止无限递归
		return instance.__dict__[storage_name]
	
	# 定义 qty_setter 函数，第一个参数也是 instance
	def qty_setter(instance, value):
		if value > 0:
			# 值直接存到 instance.__dict__ 中，这也是为了跳过特性
			instance.__dict__[storage_name] = value
		else:
			raise ValueError('value must be > 0')
	# 构建一个自定义的特性对象，然后将其返回
	return property(qty_getter, qty_setter)


# 示例 19-23　bulkfood_v2prop.py：使用特性工厂函数 quantity
class LineItem:
	# 使用工厂函数把第一个自定义的特性 weight 定义为类属性
	weight = quantity('weight')
	# 第二次调用，构建另一个自定义的特性，price
	price = quantity('price')
	
	def __init__(self, description, weight, price):
		self.description = description
		# 这里，特性已经激活，确保不能把 weight 设为负数或零
		self.weight = weight
		self.price = price
	
	def subtotal(self):
		# 这里也用到了特性，使用特性获取实例中存储的值
		return self.weight * self.price


if __name__ == '__main__':
	nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
	# 通过特性读取 weight 和 price，这会遮盖同名实例属性
	print(nutmeg.weight, nutmeg.price)
	# 使用 vars 函数审查 nutmeg 实例，查看真正用于存储值的实例属性。
	print(sorted(vars(nutmeg).items()))
	print(nutmeg.__class__)

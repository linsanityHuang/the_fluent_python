# 示例 6-3　Order 类和使用函数实现的折扣策略
'''
在示例 6-1 中，每个具体策略都是一个类，而且都只定义了一个方法，即 discount。

此外，策略实例没有状态（没有实例属性） 。

你可能会说，它们看起来像是普通的函数——的确如此。

示例 6-3 是对示例 6-1 的重构，把具体策略换成了简单的函数，而且去掉了 Promo 抽象类。
'''

from collections import namedtuple

# 姓名，积分
Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
	def __init__(self, product, quantity, price):
		self.product = product
		self.quantity = quantity
		self.price = price
	
	def total(self):
		return self.price * self.quantity


class Order:
	# cart表示购物车，是由order构成的列表
	def __init__(self, customer, cart, promotion=None):
		self.customer = customer
		self.cart = list(cart)
		self.promotion = promotion
	
	def total(self):
		if not hasattr(self, '__total'):
			# item是order item.total()
			self.__total = sum(item.total() for item in self.cart)
		return self.__total
	
	def due(self):
		if self.promotion is None:
			discount = 0
		else:
			# 计算折扣只需调用self.promotion()函数
			discount = self.promotion(self)
		return self.total() - discount
	
	def __repr__(self):
		fmt = '<Order total: {:.2f} due {:.2f}>'
		return fmt.format(self.total(), self.due())
	

# 各个策略都是函数
def fidelity_promo(order):
	"""为积分为1000或以上的顾客提供5%折扣"""
	return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
	"""单个商品为20个或以上时提供10%折扣"""
	discount = 0
	for item in order.cart:
		if item.quantity >= 20:
			discount += item.total() * .1
		return discount
	

def large_order_promo(order):
	"""订单中的不同商品达到10个或以上时提供7%折扣"""
	distinct_items = {item.product for item in order.cart}
	if len(distinct_items) >= 10:
		return order.total() * .07
	return 0


'''
示例 6-3 中的代码比示例 6-1 少 12 行。不仅如此，新的 Order 类使用起来更简单，如示例6-4 中的 doctest 所示。
示例 6-4　使用函数实现的促销折扣的 Order 类示例
'''
if __name__ == '__main__':
	# 两个顾客：joe的积分是0，ann的积分是1100
	joe = Customer('John Doe', 0)
	ann = Customer('Ann Smith', 1100)
	# 有三个商品的购物车
	cart = [
		LineItem('banana', 4, .5),
		LineItem('apple', 10, 1.5),
		LineItem('watermellon', 5, 5.0),
	]
	# 为了把折扣策略应用到Order实例上，只需把促销函数作为参数传入
	# fidelityPromo没给joe提供折扣
	o = Order(joe, cart, fidelity_promo)
	print(o)
	'''<Order total: 42.00 due: 42.00>'''
	# ann得到了5 % 折扣，因为她的积分超过1000
	o = Order(ann, cart, fidelity_promo)
	print(o)
	'''<Order total: 42.00 due: 39.90>'''
	
	# banana_cart中有30把香蕉和10个苹果
	banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
	
	# BulkItemPromo为joe购买的香蕉优惠了1.50美元
	Order(joe, banana_cart, bulk_item_promo)
	'''<Order total: 30.00 due: 28.50>'''
	
	# long_order中有10个不同的商品，每个商品的价格为1.00美元
	long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
	
	# LargerOrderPromo为joe的整个订单提供了7 % 折扣
	Order(joe, long_order, large_order_promo)
	'''<Order total: 10.00 due: 9.30>'''
	
	Order(joe, cart, large_order_promo)
	'''<Order total: 42.00 due: 42.00>'''
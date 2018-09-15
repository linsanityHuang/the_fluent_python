'''
示例 6-1　实现 Order 类，支持插入式折扣策略
'''
from abc import ABC, abstractmethod
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
	def __init__(self, customer, cart, promotion=None):
		self.customer = customer
		self.cart = list(cart)
		self.promotion = promotion
	
	def total(self):
		if not hasattr(self, '__total'):
			self.__total = sum(item.total() for item in self.cart)
		
		return self.__total
	
	def due(self):
		if self.promotion is None:
			discount = 0
		else:
			discount = self.promotion.discount(self)
		return self.total() - discount
	
	def __repr__(self):
		fmt = '<Order total: {:.2f} due {:.2f}>'
		return fmt.format(self.total(), self.due())


class Promotion(ABC):
	
	@abstractmethod
	def discount(self, order):
		'''返回折扣金额 （正值）'''


# 第一个具体策略
class FidelityPromo(Promotion):
	"""为积分为1000或以上的顾客提供5%折扣"""
	
	def discount(self, order):
		return order.total() * .05 if order.customer.fidelity >= 1000 else 0


# 第二个具体策略
class BulkItemPromo(Promotion):
	"""单个商品为20个或以上时提供10%折扣"""
	
	def discount(self, order):
		discount = 0
		for item in order.cart:
			if item.quantity >= 20:
				discount += item.total() * .1
		return discount


class LargeOrderPromo(Promotion):  # 第三个具体策略
	"""订单中的不同商品达到10个或以上时提供7%折扣"""
	
	def discount(self, order):
		distinct_items = {item.product for item in order.cart}
		if len(distinct_items) >= 10:
			return order.total() * .07
		return 0
	
	
# 示例 6-2　使用不同促销折扣的 Order 类示例

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
	# fidelityPromo没给joe提供折扣
	Order(joe, cart, FidelityPromo())
	'''<Order total: 42.00 due: 42.00>'''
	# ann得到了5 % 折扣，因为她的积分超过1000
	Order(ann, cart, FidelityPromo())
	'''<Order total: 42.00 due: 39.90>'''
	
	# banana_cart中有30把香蕉和10个苹果
	banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
	
	# BulkItemPromo为joe购买的香蕉优惠了1.50美元
	Order(joe, banana_cart, BulkItemPromo())
	'''<Order total: 30.00 due: 28.50>'''
	
	# long_order中有10个不同的商品，每个商品的价格为1.00美元
	long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
	
	# LargerOrderPromo为joe的整个订单提供了7 % 折扣
	Order(joe, long_order, LargeOrderPromo())
	'''<Order total: 10.00 due: 9.30>'''
	
	Order(joe, cart, LargeOrderPromo())
	'''<Order total: 42.00 due: 42.00>'''

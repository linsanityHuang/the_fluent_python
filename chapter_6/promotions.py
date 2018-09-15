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

'''
使用注册装饰器可以改进 6.1 节中的电商促销折扣示例。

回顾一下，示例 6-6 的主要问题是，

定义体中有函数的名称，但是 best_promo 用来判断哪个折扣幅度最大的 promos 列表中也有函数名称。

这种重复是个问题，因为新增策略函数后可能会忘记把它添加到 promos 列表中，

导致 best_promo 忽略新策略，而且不报错，为系统引入了不易察觉的缺陷。

示例 7-3 使用注册装饰器解决了这个问题。

示例 7-3　promos 列表中的值使用 promotion 装饰器填充
'''

promos = []


def promotion(promo_func):
	promos.append(promo_func)
	return promo_func


# 各个策略都是函数
@promotion
def fidelity_promo(order):
	"""为积分为1000或以上的顾客提供5%折扣"""
	return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item_promo(order):
	"""单个商品为20个或以上时提供10%折扣"""
	discount = 0
	for item in order.cart:
		if item.quantity >= 20:
			discount += item.total() * .1
		return discount


@promotion
def large_order_promo(order):
	"""订单中的不同商品达到10个或以上时提供7%折扣"""
	distinct_items = {item.product for item in order.cart}
	if len(distinct_items) >= 10:
		return order.total() * .07
	return 0


def best_promo(order):
	"""选择可用的最佳折扣"""
	return max(promo(order) for promo in promos)

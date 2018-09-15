from chapter_6.demo_6_2 import fidelity_promo, bulk_item_promo, large_order_promo, \
	Order, Customer, LineItem

'''
我们继续使用示例 6-4 中的顾客和购物车，在此基础上添加 3 个测试，如示例 6-5 所示。

示例 6-5　best_promo 函数计算所有折扣，并返回额度最大的
'''

'''
best_promo 函数的实现特别简单，如示例 6-6 所示。

示例 6-6　best_promo 迭代一个函数列表，并找出折扣额度最大的
'''
# promos 列出以函数实现的各个策略
# promos = [fidelity_promo, bulk_item_promo, large_order_promo]


'''
globals() 返回一个字典，表示当前的全局符号表。

这个符号表始终针对当前模块（对函数或方法来说，是指定义它们的模块，而不是调用它们的模块）

示例 6-7 使用 globals 函数帮助 best_promo 自动找到其他可用的 *_promo 函数，过程有点曲折。
# 示例 6-7　内省模块的全局命名空间，构建 promos 列表
'''
promos = [globals()[name] for name in globals()		#迭代 globals() 返回字典中的各个 name
		  if name.endswith('_promo')				#只选择以 _promo 结尾的名称
		  and name != 'best_promo']					#过滤掉 best_promo 自身，防止无限递归


# 与其他几个 *_promo 函数一样，best_promo 函数的参数是一个 Order 实例
def best_promo(order):
	"""选择可用的最佳折扣"""
	# 使用生成器表达式把order传给promos列表中的各个函数，返回计算出的最大折扣额度。
	return max(promo(order) for promo in promos)			# best_promo 内部的代码没有变化
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
	# banana_cart中有30把香蕉和10个苹果
	banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
	# long_order中有10个不同的商品，每个商品的价格为1.00美元
	long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
	
	print(Order(joe, long_order, best_promo))
	print(Order(joe, banana_cart, best_promo))
	print(Order(ann, cart, best_promo))

'''
假如有个名为 avg 的函数，它的作用是计算不断增加的系列值的均值；

例如，整个历史中某个商品的平均收盘价。

每天都会增加新价格，因此平均值要考虑至目前为止所有的价格。

初学者可能会像示例 7-8 那样使用类实现。
'''


# 示例 7-8　average_oo.py：计算移动平均值的类
class Averager():
	
	def __init__(self):
		self.series = []

	def __call__(self, new_value):
		self.series.append(new_value)
		total = sum(self.series)
		return total/len(self.series)


# 示例 7-9 是函数式实现，使用高阶函数 make_averager。
def make_averager():
	serias = []
	
	def averager(new_value):
		serias.append(new_value)
		total = sum(serias)
		return total/len(serias)
	return averager


'''
调用 make_averager 时，返回一个 averager 函数对象。

每次调用 averager 时，它会把参数添加到系列值中，然后计算当前平均值，
'''

if __name__ == '__main__':
	avg = Averager()
	# print(avg(4))
	# print(avg(5))
	# print(avg(5))
	avg = make_averager()
	print(avg(10))
	print(avg(11))
	print(avg(12))

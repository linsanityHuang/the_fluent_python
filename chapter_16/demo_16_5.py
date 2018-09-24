from inspect import getgeneratorstate


'''
如果不预激，那么协程没什么用。

调用 my_coro.send(x) 之前，记住一定要调用 next(my_ coro)。

为了简化协程的用法，有时会使用一个预激装饰器。

示例 16-5 中的 coroutine 装饰器是一例。

示例 16-5　coroutil.py：预激协程的装饰器
'''


from functools import wraps
def coroutine(func):
	"""装饰器： 向前执行到第一个`yield`表达式， 预激`func`"""
	@wraps(func)
	# 把被装饰的生成器函数替换成这里的 primer 函数；
	# 调用 primer 函数时，返回预激后的生成器
	def primer(*args, **kwargs):
		# 调用被装饰的函数，获取生成器对象
		gen = func(*args, **kwargs)
		# 预激生成器
		next(gen)
		# 返回生成器
		return gen
	return primer


@coroutine
def averager():
	total = 0.0
	count = 0
	
	average = None
	while True:
		term = yield average
		total += term
		count += 1
		average = total / count


'''
示例 16-6 展示 @coroutine 装饰器的用法。请与示例 16-3 对比。
示例 16-6　 coroaverager1.py：使用示例 16-5 中定义的 @coroutine 装饰器定义并测试计算移动平均值的协程
'''


if __name__ == '__main__':
	coro_avg = averager()
	print(getgeneratorstate(coro_avg))
	print(coro_avg.send(10))
	print(coro_avg.send(30))
	print(coro_avg.send(5))
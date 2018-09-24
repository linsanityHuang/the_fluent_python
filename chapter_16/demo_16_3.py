'''
第 7 章讨论闭包时，我们分析了如何使用对象计算移动平均值：

示例 7-8 定义的是一个简单的类；

示例 7-14 定义的是一个高阶函数，用于生成一个闭包，在多次调用之间跟踪total 和 count 变量的值。

示例 16-3 展示如何使用协程实现相同的功能。

示例 16-3　coroaverager0.py：定义一个计算移动平均值的协程
'''


def averager():
	total = 0.0
	count = 0
	
	average = None
	# 这个无限循环表明，只要调用方不断把值发给这个协程，它就会一直接收值，然后生成结果。
	# 仅当调用方在协程上调用 .close() 方法，或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止
	while True:
		# 这里的 yield 表达式用于暂停执行协程，把结果发给调用方；
		# 还用于接收调用方后面发给协程的值，恢复无限循环
		term = yield average
		total += term
		count += 1
		average = total/count
		
		
if __name__ == '__main__':
	# 创建协程对象
	coro_avg = averager()
	# 调用 next 函数，预激协程
	next(coro_avg)
	# 计算移动平均值：多次调用 .send(...) 方法，产出当前的平均值
	print(coro_avg.send(10))
	print(coro_avg.send(30))
	print(coro_avg.send(5))

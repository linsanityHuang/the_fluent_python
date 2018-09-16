'''
示例 7-15 定义了一个装饰器，它会在每次调用被装饰的函数时计时，然后把经过的时间、传入的参数和调用的结果打印出来。
示例 7-15　一个简单的装饰器，输出函数的运行时间
'''

import time


def clock(func):
	def clocked(*args):				#定义内部函数 clocked，它接受任意个定位参数
		t0 = time.perf_counter()
		result = func(*args)		#这行代码可用，是因为 clocked 的闭包中包含自由变量 func
		elapsed = time.perf_counter() - t0
		name = func.__name__
		arg_str = ', '.join(repr(arg) for arg in args)
		print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
		return result
	return clocked					# 返回内部函数，取代被装饰的函数


@clock
def snooze(seconds):
	time.sleep(seconds)


@clock
def factorial(n):
	return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
	print('*' * 40, 'Calling snooze(.123)')
	snooze(.123)
	print('*' * 40, 'Calling factorial(6)')
	print('6! =', factorial(6))

'''
示例 7-15 中实现的 clock 装饰器有几个缺点：不支持关键字参数，而且遮盖了被装饰函数的 __name__ 和 __doc__ 属性。

示例 7-17 使用 functools.wraps 装饰器把相关的属性从 func 复制到 clocked 中。

此外，这个新版还能正确处理关键字参数。

示例 7-17　改进后的 clock 装饰器
'''

import time
import functools


def clock(func):
	@functools.wraps(func)
	def clocked(*args, **kwargs):				#定义内部函数 clocked，它接受任意个定位参数
		t0 = time.time()
		result = func(*args, **kwargs)		#这行代码可用，是因为 clocked 的闭包中包含自由变量 func
		elapsed = time.time() - t0
		name = func.__name__
		arg_lst = []
		if args:
			arg_lst.append(', '.join(repr(arg) for arg in args))
		if kwargs:
			pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
			arg_lst.append(', '.join(pairs))
		arg_str = ', '.join(arg_lst)
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
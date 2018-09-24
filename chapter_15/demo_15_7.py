import contextlib
'''
示例 15-5 有一个严重的错误：如果在 with 块中抛出了异常，Python 解释器会将其捕获，然后在 looking_glass 函数的 yield 表达式里再次抛出。

但是，那里没有处理错误的代码，因此 looking_glass 函数会中止，永远无法恢复成原来的 sys.stdout.write 方法，导致系统处于无效状态。

示例 15-7 添加了一些代码，特别用于处理 ZeroDivisionError 异常；这样，在功能上它就与示例 15-3 中基于类的实现等效了。

示例 15-7　 mirror_gen_exc.py：基于生成器的上下文管理器，而且实现了异常处理——从外部看，行为与示例 15-3 一样
'''


@contextlib.contextmanager
def looking_glass():
	import sys
	original_write = sys.stdout.write
	
	def reverse_write(text):
		original_write(text[::-1])
	
	sys.stdout.write = reverse_write
	# 创建一个变量，用于保存可能出现的错误消息；与示例 15-5 相比，这是第一处改动
	msg = ''
	try:
		yield 'JABBERWOCKY'
	# 处理 ZeroDivisionError 异常，设置一个错误消息
	except ZeroDivisionError:
		msg = 'Please DO NOT divide by zero!'
	finally:
		# 撤销对 sys.stdout.write 方法所做的猴子补丁
		sys.stdout.write = original_write
		if msg:
			# 如果设置了错误消息，把它打印出来
			print(msg)


if __name__ == '__main__':
	with looking_glass() as what:
		print('Alice, Kitty and Snowdrop')
		print(what)
	print(what)

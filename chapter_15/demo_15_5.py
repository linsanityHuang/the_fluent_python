import contextlib

'''
@contextmanager 装饰器能减少创建上下文管理器的样板代码量，

因为不用编写一个完整的类，定义 __enter__ 和 __exit__ 方法，而只需实现有一个 yield 语句的生成器，生成想让__enter__ 方法返回的值。

在使用 @contextmanager 装饰的生成器中，yield 语句的作用是把函数的定义体分成两部分：

yield 语句前面的所有代码在 with 块开始时（即解释器调用 __enter__ 方法时）执行，

yield 语句后面的代码在 with 块结束时（即调用 __exit__ 方法时）执行。

下面举个例子。示例 15-5 使用一个生成器函数代替示例 15-3 中定义的 LookingGlass 类。
示例 15-5　mirror_gen.py：使用生成器实现的上下文管理器
'''


# 应用 contextmanager 装饰器
@contextlib.contextmanager
def looking_glass():
	import sys
	# 贮存原来的 sys.stdout.write 方法
	original_write = sys.stdout.write
	
	# 定义自定义的 reverse_write 函数；在闭包中可以访问 original_write
	def reverse_write(text):
		original_write(text[::-1])
	
	# 把 sys.stdout.write 替换成 reverse_write
	sys.stdout.write = reverse_write
	# 产出一个值，这个值会绑定到 with 语句中 as 子句的目标变量上。
	# 执行 with 块中的代码时，这个函数会在这一点暂停
	yield 'JABBERWOCKY'
	# 控制权一旦跳出 with 块，继续执行 yield 语句之后的代码；
	# 这里是恢复成原来的 sys.stdout.write 方法
	sys.stdout.write = original_write


if __name__ == '__main__':
	with looking_glass() as what:
		print('Alice, Kitty and Snowdrop')
		print(what)
	print(what)

'''
示例 15-3　mirror.py：LookingGlass 上下文管理器类的代码
'''


class LookingGlass:
	
	# 除了 self 之外，Python 调用 __enter__ 方法时不传入其他参数
	def __enter__(self):
		import sys
		# 把原来的 sys.stdout.write 方法保存在一个实例属性中，供后面使用
		self.original_write = sys.stdout.write
		# 为 sys.stdout.write 打猴子补丁，替换成自己编写的方法
		sys.stdout.write = self.reverse_write
		# 返回 'JABBERWOCKY' 字符串，这样才有内容存入目标变量 what
		return 'JABBERWOCKY'
	
	# 这是用于取代 sys.stdout.write 的方法，把 text 参数的内容反转，然后调用原来的实现
	def reverse_write(self, text):
		self.original_write(text[::-1])
	
	# 如果一切正常，Python 调用 __exit__ 方法时传入的参数是 None, None, None；如果抛出了异常，这三个参数是异常数据，如下所述
	def __exit__(self, exc_type, exc_value, traceback):
		# 重复导入模块不会消耗很多资源，因为 Python 会缓存导入的模块
		import sys
		# 还原成原来的 sys.stdout.write 方法
		sys.stdout.write = self.original_write
		# 如果有异常，而且是 ZeroDivisionError 类型，打印一个消息
		if exc_type is ZeroDivisionError:
			print('Please DO NOT divide by zero!')
		# ……然后返回 True，告诉解释器，异常已经处理了
		return True
	# 如果 __exit__ 方法返回 None，或者 True 之外的值，with 块中的任何异常都会向上冒泡
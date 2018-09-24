'''
示例 15-2 使用一个精心制作的上下文管理器执行操作，以此强调上下文管理器与 __enter__ 方法返回的对象之间的区别。

示例 15-2　测试 LookingGlass 上下文管理器类
'''

from chapter_15.mirror import LookingGlass

# 上下文管理器是 LookingGlass 类的实例；Python 在上下文管理器上调用 __enter__ 方法，把返回结果绑定到 what 上
with LookingGlass() as what:
	# 打印一个字符串，然后打印 what 变量的值
	print('Alice, Kitty and Snowdrop')
	# 打印出的内容是反向的
	'''pordwonS dna yttiK ,ecilA'''
	print(what)
	'''YKCOWREBBAJ'''

# 现在，with 块已经执行完毕。
# 可以看出，__enter__ 方法返回的值——即存储在 what 变量中的值——是字符串 'JABBERWOCKY'
print(what)
'''JABBERWOCKY'''
# 输出不再是反向的了
print('Back to normal.')

'''
下面是一个简单的 for 循环，迭代一个字符串。

这里，字符串 'ABC' 是可迭代的对象。

背后是有迭代器的，只不过我们看不到
'''

s = 'ABC'
for char in s:
	print(char)
	

'''
如果没有 for 语句，不得不使用 while 循环模拟，要像下面这样写
'''
# 使用可迭代的对象构建迭代器 it
it = iter(s)
while True:
	try:
		# 不断在迭代器上调用 next 函数，获取下一个字符
		print(next(it))
	# 如果没有字符了，迭代器会抛出 StopIteration 异常
	except StopIteration:
		# 释放对 it 的引用，即废弃迭代器对象
		del it
		# 退出循环
		break

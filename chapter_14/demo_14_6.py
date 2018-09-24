'''
示例 14-6 使用 for 循环更清楚地说明了生成器函数定义体的执行过程。
'''


# 定义生成器函数的方式与普通的函数无异，只不过要使用 yield 关键字
def gen_AB():
	print('start')
	# 在 for 循环中第一次隐式调用 next() 函数时，会打印 'start'，然后停在第一个 yield 语句，生成值 'A'。
	yield 'A'
	print('continue')
	# 在 for 循环中第二次隐式调用 next() 函数时，会打印 'continue'，然后停在第二个yield 语句，生成值 'B'
	yield 'B'
	# 第三次调用 next() 函数时，会打印 'end.'，然后到达函数定义体的末尾，导致生成器对象抛出 StopIteration 异常
	print('end.')
	

# 迭代时，for 机制的作用与 g = iter(gen_AB()) 一样，用于获取生成器对象，然后每次迭代时调用 next(g)
for c in gen_AB():
	# 循环块打印 --> 和 next(g) 返回的值。但是，生成器函数中的 print 函数输出结果之后才会看到这个输出
	print('-->', c)

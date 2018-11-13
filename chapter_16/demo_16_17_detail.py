from collections import namedtuple
Result = namedtuple('Result', 'count average')


# 子生成器
def averager():
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield
		if term is None:
			break
		total += term
		count += 1
		average = total/count
	return Result(count, average)


# 委派生成器
def grouper(results, key):
	while True:
		results[key] = yield from averager()


# 客户端代码，即调用方
def main(data):
	results = {}
	# 外层 for 循环每次迭代会新建一个 grouper 实例， 赋值给 group 变量； group 是委派生成器
	for key, values in data.items():
		group = grouper(results, key)
		# 调用 next(group)，预激委派生成器 grouper，此时进入 while True 循环，调用子生成器 averager 后，在 yield from 表达式处暂停
		next(group)
		# 内层 for 循环调用 group.send(value)，直接把值传给子生成器 averager。同时，当前的 grouper 实例（group）在 yield from 表达式处暂停
		# 内层循环结束后，group 实例依旧在 yield from 表达式处暂停，因此，grouper 函数定义体中为 results[key] 赋值的语句还没有执行
		for value in values:
			group.send(value)
		# 如果外层 for 循环的末尾没有 group.send(None)， 那么 averager 子生成器永远不会终止，委派生成器 group 永远不会再次激活，因此永远不会为 results[key] 赋值
		group.send(None)
	# 外层 for 循环重新迭代时会新建一个 grouper 实例，然后绑定到 group 变量上。前一个grouper 实例 （以及它创建的尚未终止的 averager 子生成器实例） 被垃圾回收程序回收。
	report(results)
	

# 输出报告
def report(results):
	for key, result in sorted(results.items()):
		group, unit = key.split(';')
		print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
	'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
	'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
	'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
	'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

'''
示例 16-17 展示了 yield from 结构最简单的用法，只有一个委派生成器和一个子生成器。
因为委派生成器相当于管道，所以可以把任意数量个委派生成器连接在一起：

一个委派生成器使用 yield from 调用一个子生成器，

而那个子生成器本身也是委派生成器，使用yield from 调用另一个子生成器，

以此类推。最终，这个链条要以一个只使用 yield 表达式的简单生成器结束；

不过，也能以任何可迭代的对象结束，如示例 16-16 所示。

任何 yield from 链条都必须由客户驱动，

在最外层委派生成器上调用 next(...) 函数或 .send(...) 方法。

可以隐式调用，例如使用 for 循环。
'''

if __name__ == '__main__':
	main(data)

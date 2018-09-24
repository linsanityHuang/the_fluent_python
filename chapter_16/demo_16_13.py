from collections import namedtuple

'''
示 例 16-13 中 的 averager 协 程 返 回 的 结 果 是 一 个 namedtuple，
两 个 字 段 分 别 是 项 数（count）和平均值（average） 。

我本可以只返回平均值，但是返回一个元组可以获得累积数据的另一个重要信息——项数。

示例 16-13　coroaverager2.py：定义一个求平均值的协程，让它返回一个结果
'''

Result = namedtuple('Result', 'count average')

def averager():
	count = 0
	total = 0.0
	average = None
	while True:
		term = yield
		if term is None:
			# 为了返回值，协程必须正常终止；因此，这一版 averager 中有个条件判断，以便退出累计循环。
			break
		total += term
		count += 1
		average = total/count
	# 返回一个 namedtuple，包含 count 和 average 两个字段。
	# 在 Python 3.3 之前，如果生成器返回值，解释器会报句法错误
	return Result(count, average)


if __name__ == '__main__':
	coro_avg = averager()
	next(coro_avg)
	# 这一版不产出值
	coro_avg.send(10)
	coro_avg.send(30)
	coro_avg.send(6.5)
	# 发送 None 会终止循环，导致协程结束，返回结果。
	# 一如既往，生成器对象会抛出StopIteration 异常。异常对象的 value 属性保存着返回的值。
	# coro_avg.send(None)
	'''
	Traceback (most recent call last):
	  File "/Users/huangjiansheng/Documents/the_fluent_python/chapter_16/demo_16_13.py", line 37, in <module>
		coro_avg.send(None)
	StopIteration: Result(count=3, average=15.5)
	'''
	try:
		coro_avg.send(None)
	except StopIteration as exc:
		result = exc.value
	print(result)
	'''Result(count=3, average=15.5)'''

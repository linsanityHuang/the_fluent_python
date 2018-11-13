import asyncio
import itertools
import sys

'''
示例 18-2　spinner_asyncio.py：通过协程以动画形式显示文本式旋转指针
'''


# 打算交给 asyncio 处理的协程要使用 @asyncio.coroutine 装饰。
# 使用 @asyncio.coroutine 装饰器不是强制要求，但是强烈建议这么做，因为这样能在一众普通的函数中把协程凸显出来，也有助于调试：
# 如果还没从中产出值，协程就被垃圾回收了（意味着有操作未完成，因此有可能是个缺陷） ，那就可以发出警告。这个装饰器不会预激协程。
# 这里不需要示例 18-1 中 spin 函数中用来关闭线程的 signal 参数
@asyncio.coroutine
def spin(msg):
	write, flush = sys.stdout.write, sys.stdout.flush
	for char in itertools.cycle('|/-\\'):
		status = char + ' ' + msg
		write(status)
		flush()
		write('\x08' * len(status))
		try:
			# 使用 yield from asyncio.sleep(.1) 代替 time.sleep(.1)，这样的休眠不会阻塞事件循环
			yield from asyncio.sleep(.1)
		# 如果 spin 函数苏醒后抛出 asyncio.CancelledError 异常，其原因是发出了取消请求，因此退出循环
		except asyncio.CancelledError:
			break
	write(' ' * len(status) + '\x08' * len(status))


# 现在，slow_function 函数是协程，在用休眠假装进行 I/O 操作时，使用 yield from 继续执行事件循环
@asyncio.coroutine
def slow_function():
	# yield from asyncio.sleep(3) 表达式把控制权交给主循环，在休眠结束后恢复这个协程
	yield from asyncio.sleep(3)
	return 42


# 现在，supervisor 函数也是协程，因此可以使用 yield from 驱动 slow_function 函数
@asyncio.coroutine
def supervisor():
	# asyncio.async(...) 函数排定 spin 协程的运行时间，使用一个 Task 对象包装 spin 协程，并立即返回
	spinner = asyncio.async(spin('thinking!'))
	# 显 示 Task 对 象。 输 出 类 似 于 <Task pending coro=<spin() running at spinner_ asyncio.py:12>>
	print('spinner object:', spinner)
	# 驱动 slow_function() 函数。
	# 结束后，获取返回值。
	# 同时，事件循环继续运行，因为slow_function 函数最后使用 yield from asyncio.sleep(3) 表达式把控制权交回给了主循环
	result = yield from slow_function()
	# Task 对象可以取消；取消后会在协程当前暂停的 yield 处抛出 asyncio.CancelledError 异常。
	# 协程可以捕获这个异常，也可以延迟取消，甚至拒绝取消
	spinner.cancel()
	return result


def main():
	# 获取事件循环的引用
	loop = asyncio.get_event_loop()
	# 驱动 supervisor 协程，让它运行完毕；这个协程的返回值是这次调用的返回值
	result = loop.run_until_complete(supervisor())
	loop.close()
	print('Answer:', result)


if __name__ == '__main__':
	main()

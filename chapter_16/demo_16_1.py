from inspect import getgeneratorstate
'''
示例 16-1 展示了协程的行为。
示例 16-1　可能是协程最简单的使用演示
'''


def simple_coroutine():					#协程使用生成器函数定义：定义体中有 yield 关键字
	print('-> coroutine started')
	# yield 在表达式中使用；如果协程只需从客户那里接收数据，
	# 那么产出的值是 None——这个值是隐式指定的，因为 yield 关键字右边没有表达式
	x = yield
	print('-> coroutine received:', x)
	

# 与创建生成器的方式一样，调用函数得到生成器对象
my_coro = simple_coroutine()
print(getgeneratorstate(my_coro))
print(my_coro)
'''<generator object simple_coroutine at 0x1044c1b48>'''
# 首先要调用 next(...) 函数，因为生成器还没启动，没在 yield 语句处暂停，所以一开始无法发送数据
next(my_coro)
print(getgeneratorstate(my_coro))
'''-> coroutine started'''
# 调用这个方法后，协程定义体中的 yield 表达式会计算出 42；现在，协程会恢复，一直运行到下一个 yield 表达式，或者终止
my_coro.send(42)
print(getgeneratorstate(my_coro))
'''-> coroutine received: 42'''
# 这里，控制权流动到协程定义体的末尾，导致生成器像往常一样抛出 StopIteration 异常
print(getgeneratorstate(my_coro))
'''
Traceback (most recent call last):
  File "/Users/huangjiansheng/Documents/the_fluent_python/chapter_16/demo_16_1.py", line 16, in <module>
	my_coro.send(42)
StopIteration
'''

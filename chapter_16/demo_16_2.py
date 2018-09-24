from inspect import getgeneratorstate

'''
下面举个产出多个值的例子，以便更好地理解协程的行为，如示例 16-2 所示。
示例 16-2　产出两个值的协程
'''


def simple_coro2(a):
	print('-> Started: a =', a)
	b = yield a
	print('-> Received: b =', b)
	c = yield a + b
	print('-> Received: c =', c)
	

my_coro2 = simple_coro2(14)
# inspect.getgeneratorstate 函数指明，处于 GEN_CREATED 状态（即协程未启动）
print(getgeneratorstate(my_coro2))
'''GEN_CREATED'''
# 向前执行协程到第一个 yield 表达式，打印 -> Started: a = 14 消息，然后产出 a 的值，并且暂停，等待为 b 赋值
next(my_coro2)
'''-> Started: a = 14'''
# getgeneratorstate 函数指明，处于 GEN_SUSPENDED 状态（即协程在 yield 表达式处暂停）
print(getgeneratorstate(my_coro2))
'''GEN_SUSPENDED'''
# 把数字 28 发给暂停的协程；计算 yield 表达式，得到 28，然后把那个数绑定给 b。
# 打印 -> Received: b = 28 消息，产出 a + b 的值（42） ，然后协程暂停，等待为 c 赋值
my_coro2.send(28)
'''-> Received: b = 28'''
# 把数字 99 发给暂停的协程；计算 yield 表达式，得到 99，然后把那个数绑定给 c。
# 打印-> Received: c = 99 消息，然后协程终止，导致生成器对象抛出 StopIteration 异常
my_coro2.send(99)
'''-> Received: c = 99'''
# getgeneratorstate 函数指明，处于 GEN_CLOSED 状态（即协程执行结束）
print(getgeneratorstate(my_coro2))

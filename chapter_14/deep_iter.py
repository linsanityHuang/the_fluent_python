from random import randint

'''
如前所述，在 Python 中迭代对象 x 时会调用 iter(x)。

可是，iter 函数还有一个鲜为人知的用法：传入两个参数，使用常规的函数或任何可调用的对象创建迭代器。

这样使用时，第一个参数必须是可调用的对象，用于不断调用（没有参数） ，产出各个值；

第二个值是哨符，这是个标记值，当可调用的对象返回这个值时，触发迭代器抛出 StopIteration 异常，而不产出哨符。
'''
# 下述示例展示如何使用 iter 函数掷骰子，直到掷出 1 点为止：


def d6():
	return randint(1, 6)


d6_iter = iter(d6, 1)

print(d6_iter)
'''<callable_iterator object at 0x103cc77b8>'''

# 示例中的 for 循环可能运行特别长的时间，不过肯定不会打印 1，因为 1 是哨符。
for roll in d6_iter:
	print(roll)
'''
3
5
3
4
3
3
5
6
4
6
5
6
3
4
3
5
2
5
5
5
'''

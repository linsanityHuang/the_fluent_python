'''
示例 5-21　使用 reduce 函数和一个匿名函数计算阶乘
'''

from functools import reduce
def fact(n):
	return reduce(lambda a, b: a * b, range(1, n+1))

'''
operator 模块为多个算术运算符提供了对应的函数，
从而避免编写 lambda a, b: a*b 这种平凡的匿名函数。

使用算术运算符函数，可以把示例 5-21 改写成示例 5-22 那样。
示例 5-22　使用 reduce 和 operator.mul 函数计算阶乘
'''

from operator import mul
def fact_(n):
	return reduce(mul, range(1, n+1))

if __name__ == '__main__':
	print(fact_(4))
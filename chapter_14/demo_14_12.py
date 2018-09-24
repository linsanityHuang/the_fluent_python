'''
示例 14-12 中定义了一个名为 aritprog_gen 的生成器函数，作用与 ArithmeticProgression 类一样，只不过代码量更少。

如果把 ArithmeticProgression 类换成 aritprog_gen 函数，示例 14-10 中的测试也都能通过.

示例 14-12　aritprog_gen 生成器函数
'''


def aritprog_gen(begin, step, end=None):
	result = type(begin + step)(begin)
	forever = end is None
	index = 0
	while forever or result < end:
		yield result
		index += 1
		result = begin + step * index


if __name__ == '__main__':
	ap = aritprog_gen(0, 1, 3)
	print(list(ap))
	'''[0, 1, 2]'''
	ap = aritprog_gen(1, .5, 3)
	print(list(ap))
	'''[1.0, 1.5, 2.0, 2.5]'''
	ap = aritprog_gen(0, 1 / 3, 1)
	print(list(ap))
	'''[0.0, 0.3333333333333333, 0.6666666666666666]'''
	from fractions import Fraction
	ap = aritprog_gen(0, Fraction(1, 3), 1)
	print(list(ap))
	'''[Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]'''
	from decimal import Decimal
	ap = aritprog_gen(0, Decimal('.1'), .3)
	print(list(ap))
	'''[Decimal('0'), Decimal('0.1'), Decimal('0.2')]'''

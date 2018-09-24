'''
示例 14-11 列出的是 ArithmeticProgression 类的实现。
示例 14-11　ArithmeticProgression 类
'''


class ArithmeticProgression:
	
	# __init__ 方法需要两个参数：begin 和 step
	# end 是可选的，如果值是 None，那么生成的是无穷数列
	def __init__(self, begin, step, end=None):
		self.begin = begin
		self.step = step
		self.end = end  # None -> 无穷数列
	
	def __iter__(self):
		# 这一行把 self.begin 赋值给 result，不过会先强制转换成前面的加法算式得到的类型
		result = type(self.begin + self.step)(self.begin)
		# 为了提高可读性，我们创建了 forever 变量，如果 self.end 属性的值是 None，那么forever 的值是 True，因此生成的是无穷数列
		forever = self.end is None
		index = 0
		# 这个循环要么一直执行下去，要么当 result 大于或等于 self.end 时结束。如果循环退出了，那么这个函数也随之退出
		while forever or result < self.end:
			# 生成当前的 result 值
			yield result
			index += 1
			# 计算可能存在的下一个结果。这个值可能永远不会产出，因为 while 循环可能会终止
			result = self.begin + self.step * index


if __name__ == '__main__':
	ap = ArithmeticProgression(0, 1, 3)
	print(list(ap))
	'''[0, 1, 2]'''
	ap = ArithmeticProgression(1, .5, 3)
	print(list(ap))
	'''[1.0, 1.5, 2.0, 2.5]'''
	ap = ArithmeticProgression(0, 1 / 3, 1)
	print(list(ap))
	'''[0.0, 0.3333333333333333, 0.6666666666666666]'''
	from fractions import Fraction
	ap = ArithmeticProgression(0, Fraction(1, 3), 1)
	print(list(ap))
	'''[Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]'''
	from decimal import Decimal
	ap = ArithmeticProgression(0, Decimal('.1'), .3)
	print(list(ap))
	'''[Decimal('0'), Decimal('0.1'), Decimal('0.2')]'''

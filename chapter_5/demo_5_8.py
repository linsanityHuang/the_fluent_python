# coding=utf-8
'''
示例 5-8 实现了 BingoCage 类。

这个类的实例使用任何可迭代对象构建，而且会在内部存储一个随机顺序排列的列表。

调用实例会取出一个元素。

示例 5-8　bingocall.py：调用 BingoCage 实例，从打乱的列表中取出一个元素
'''
import random

class BingoCage:
	def __init__(self, items):
		self._items = list(items)				# __init__ 接受任何可迭代对象；在本地构建一个副本，防止列表参数的意外副作用。
		random.shuffle(self._items)				# shuffle 定能完成工作，因为self._items 是列表。

	def pick(self):								# 起主要作用的方法。
		try:
			return self._items.pop()
		except IndexError as e:					# 如果self._items 为空，抛出异常，并设定错误消息。
			raise LookupError('pick from empty BingoCage')

	def __call__(self):							# bingo.pick() 的快捷方式是bingo()。
		return self.pick()


if __name__ == '__main__':
	bingo = BingoCage(range(30))
	print(bingo.pick())
	print(bingo())
	print(callable(bingo))
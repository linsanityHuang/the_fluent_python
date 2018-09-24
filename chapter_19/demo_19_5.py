from collections import abc
import keyword

'''
FrozenJSON 类，比大多数实现都简单，因为只支持读取，即只能访问数据。
不过，这个类能递归，自动处理嵌套的映射和列表。
'''

from chapter_19.demo_19_2 import load


class FrozenJSON:
	def __init__(self, mapping):
		'''
		使用 mapping 参数构建一个字典。
		这么做有两个目的：
		(1) 确保传入的是字典（或者是能转换成字典的对象）；
		(2) 安全起见，创建一个副本。
		'''
		self.__data = {}
		for key, value in mapping.items():
			# 在名称为 Python 关键字的属性后面加上 _
			# keyword.iskeyword(...) 正是我们所需的函数；
			# 为了使用它，必须导入 keyword 模块；
			if keyword.iskeyword(key):
				key += '_'
			self.__data[key] = value

	def __getattr__(self, name):
		try:
			'''
			仅当没有指定名称（name）的属性时才调用 __getattr__ 方法。
			'''
			# 如果 name 是实例属性 __data 的属性，返回那个属性。
			# 调用 keys 等方法就是通过这种方式处理的。
			if hasattr(self.__data, name):
				return getattr(self.__data, name)
			# 否则，从 self.__data 中获取 name 键对应的元素，
			# 返回调用 FrozenJSON.build() 方法得到的结果。
			else:
				return FrozenJSON.build(self.__data[name])
		except KeyError as e:
			raise AttributeError(name)

	# 这是一个备选构造方法，@classmethod 装饰器经常这么用。
	@classmethod
	def build(cls, obj):
		# 如果 obj 是映射，那就构建一个 FrozenJSON 对象。
		if isinstance(obj, abc.Mapping):
			return cls(obj)
		# 如果是 MutableSequence 对象，必然是列表，
		# 因此，我们把 obj 中的每个元素递归地传给 .build() 方法，
		# 构建一个列表。
		elif isinstance(obj, abc.MutableSequence):
			return [cls.build(item) for item in obj]
		# 如果既不是字典也不是列表，那么原封不动地返回元素。
		else:
			return obj



if __name__ == '__main__':
	raw_feed = load()
	# 传入嵌套的字典和列表组成的 raw_feed，创建一个 FrozenJSON 实例
	feed = FrozenJSON(raw_feed)
	print(len(feed.Schedule.speakers))
	print(sorted(feed.Schedule.keys()))
	for key, value in sorted(feed.Schedule.items()):
		print('{:3} {}'.format(len(value), key))

	print(feed.Schedule.speakers[-1].name)
	talk = feed.Schedule.events[40]
	print(type(talk))
	print(talk.name)
	print(talk.speakers)
	print(talk.flavor)

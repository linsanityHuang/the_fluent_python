from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'

def load():
	if not os.path.exists(JSON):
		msg = 'downloading {} to {}'.format(URL, JSON)
		warnings.warn(msg)
		with urlopen(URL) as remote, open(JSON, 'wb+') as local:
			local.write(remote.read())

	with open(JSON) as fp:
		return json.load(fp)


# 把一个 JSON 数据集转换成一个嵌套着 FrozenJSON 对象、列表和简单类型的 FrozenJSON 对象
from collections import abc
import keyword
class FrozenJSON:
	'''
	一个只读接口，使用属性表示法访问JSON类对象
	'''
	def __init__(self, mapping):
		'''
		使用 mapping 参数构建一个字典。
		这么做有两个目的：
		(1) 确保传入的是字典（或者是能转换成字典的对象）；
		(2) 安全起见，创建一个副本。
		'''
		# 在名称为 Python 关键字的属性后面加上 _
		self.__data = {}
		for key, value in mapping.items():
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

# FrozenJSON 类的另一个版本，把之前在类方法 build 中的逻辑移到了 __new__ 方法中。
class FrozenJSON:
	# __new__ 是类方法，第一个参数是类本身，
	# 余下的参数与 __init__ 方法一样，只不过没有 self。
	def __new__(cls, arg):
		if isinstance(arg, abc.Mapping):
			# 默认的行为是委托给超类的 __new__ 方法。
			# 这里调用的是 object 基类的 __new__ 方法，把唯一的参数设为 FrozenJSON。
			return super().__new__(cls)
		# __new__ 方法中余下的代码与原先的 build 方法完全一样
		elif isinstance(arg, abc.MutableSequence):
			return [cls(item) for item in arg]
		else:
			return arg

	def __init__(self, mapping):
		self.__data = {}
		for key, value in mapping.items():
			if iskeyword(key):
				key += '_'
			self.__data[key] = value

	def __getattr__(self, name):
		if hasattr(self.__data, name):
			return getattr(self.__data, name)
		else:
			# 之前，这里调用的是 FrozenJSON.build 方法，现在只需调用 FrozenJSON 构造方法
			return FrozenJSON(self.__data[name])

if __name__ == '__main__':
	# feed 的值是一个字典，里面嵌套着字典和列表，存储着字符串和整数。
	feed = load()
	# 列出 "Schedule" 键中的 4 个记录集合。
	print(sorted(feed['Schedule'].keys()))
	# 显示各个集合中的记录数量。
	for key, value in sorted(feed['Schedule'].items()):
		print('{:3} {}'.format(len(value), key))

	# 深入嵌套的字典和列表，获取最后一个演讲者的名字。
	print(feed['Schedule']['speakers'][-1]['name'])
	# 获取那位演讲者的编号。
	print(feed['Schedule']['speakers'][-1]['serial'])

	print(feed['Schedule']['events'][40]['name'])
	# 每个事件都有一个 'speakers' 字段，列出 0 个或多个演讲者的编号。
	print(feed['Schedule']['events'][40]['speakers'])

	# feed['Schedule']['events'][40]['name'] 这种句法很冗长
	# 在 JavaScript 中，可以使用 feed.Schedule.events[40].name 获取那个值。
	# 在 Python 中，可以实现一个近似字典的类（网上有大量实现），达到同样的效果。
	# 我自己实现了 FrozenJSON 类，比大多数实现都简单，
	# 因为只支持读取，即只能访问数据。不过，这个类能递归，自动处理嵌套的映射和列表。

	feed = FrozenJSON(feed)
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






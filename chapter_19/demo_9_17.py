from collections import abc
from keyword import iskeyword
from chapter_19.demo_19_2 import load

'''
示例 19-7 是 FrozenJSON 类的另一个版本，把之前在类方法 build 中的逻辑移到了 __new__ 方法中。

示例 19-7　 explore2.py：使用 __new__ 方法取代 build 方法，构建可能是也可能不是FrozenJSON 实例的新对象
'''


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
	raw_feed = load()
	# 传入嵌套的字典和列表组成的 raw_feed，创建一个 FrozenJSON 实例
	feed = FrozenJSON(raw_feed)
	print(feed.keys())
	print(feed.Schedule.keys())
	print(feed.Schedule.conferences[0].serial)
	
	# print(type(feed.Schedule.events))
	for item in feed.Schedule.events:
		if item.speakers == [3471, 5199]:
			print(item.items())
	# print(len(feed.Schedule.speakers))
	# print(sorted(feed.Schedule.keys()))
	# for key, value in sorted(feed.Schedule.items()):
	# 	print('{:3} {}'.format(len(value), key))
	#
	# print(feed.Schedule.speakers[-1].name)
	# talk = feed.Schedule.events[40]
	# print(type(talk))
	# print(talk.name)
	# print(talk.speakers)

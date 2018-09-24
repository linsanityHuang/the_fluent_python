from collections import abc
import json
import keyword
from chapter_19.demo_19_2 import load


class FrozenJSON:
	'''FrozenJSON 类有个缺陷：没有对名称为 Python 关键字的属性做特殊处理'''
	def __init__(self, mapping):
		# 使用 mapping 参数构建一个字典。
		# 这么做有两个目的：
		# (1) 确保传入的是字典（或者是能转换成字典的对象） ；
		# (2) 安全起见，创建一个副本
		self.__data = dict(mapping)
		
		'''
		在名称为 Python 关键字的属性后面加上 _
		self.__data = {}
		for key, value in mapping.items():
			if keyword.iskeyword(key):
				key += '_'
				self.__data[key] = value
		'''
		
	# 仅当没有指定名称（name）的属性时才调用 __getattr__ 方法
	def __getattr__(self, name):
		# 如果 name 是实例属性 __data 的属性，返回那个属性。
		# 调用 keys 等方法就是通过这种方式处理的
		if hasattr(self.__data, name):
			return getattr(self.__data, name)
		else:
			# 否则，从 self.__data 中获取 name 键对应的元素，返回调用 FrozenJSON.build() 方法得到的结果
			return FrozenJSON.build(self.__data[name])

	@classmethod
	# 这是一个备选构造方法，@classmethod 装饰器经常这么用
	def build(cls, obj):
		if isinstance(obj, abc.MutableMapping):
			return cls(obj)
		elif isinstance(obj, abc.MutableSequence):
			return [cls.build(item) for item in obj]
		else:
			# 如果既不是字典也不是列表，那么原封不动地返回元素。
			return obj


if __name__ == '__main__':
	# raw_feed = load()
	raw_feed = "{'git_name': 'git@git.houbank.net:huangjiansheng/java_ssm.git', 'git_branch': 'master', 'git_username_val': 'admin', 'git_password_val': '9fvMGfnPGyn3XM+NY8veEw==', 'ci_aim_group': '测试编译组'}"
	# 传入嵌套的字典和列表组成的 raw_feed，创建一个 FrozenJSON 实例
	raw_feed = raw_feed.replace("'", '"')
	# print(raw_feed)
	feed = FrozenJSON(json.loads(raw_feed))
	'''
	print(len(feed.Schedule.speakers))
	print(sorted(feed.Schedule.keys()))
	for key, value in sorted(feed.Schedule.items()):
		print('{:3} {}'.format(len(value), key))
	
	print(feed.Schedule.speakers[-1].name)
	talk = feed.Schedule.events[40]
	print(type(talk))
	print(talk.name)
	print(talk.speakers)
	'''
	print(feed.git_name)
	print(type(feed.data))

from urllib.request import urlopen
import warnings
import os
import json
'''
示例 19-2 没用到元编程，几乎所有代码的作用可以用这一个表达式概括：json.load(fp)。
不过，这样足以处理那个数据集了。osconfeed.load 函数会在后面几个示例中用到。
示例 19-2　osconfeed.py：下载 osconfeed.json（doctest 在示例 19-3 中）
'''

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
	if not os.path.exists(JSON):
		msg = 'downloading {} to {}'.format(URL, JSON)
		# 如果需要下载，就发出提醒
		warnings.warn(msg)
		# 在 with 语句中使用两个上下文管理器（从 Python 2.7 和 Python 3.1 起允许这么做） ，
		# 分别用于读取和保存远程文件
		with urlopen(URL) as remote, open(JSON, 'wb+') as local:
			local.write(remote.read())

	with open(JSON, encoding='utf-8') as fp:
		# json.load 函数解析 JSON 文件，返回 Python 原生对象。
		# 在这个数据源中有这几种数据类型：dict、list、str 和 int
		return json.load(fp)


if __name__ == '__main__':
	# feed 的值是一个字典，里面嵌套着字典和列表，存储着字符串和整数
	feed = load()
	# 列出 "Schedule" 键中的 4 个记录集合
	print(sorted(feed['Schedule'].keys()))
	
	for key, value in sorted(feed['Schedule'].items()):
		# 显示各个集合中的记录数量
		print('{:3} {}'.format(len(value), key))
		'''
		  1 conferences
		494 events
		357 speakers
		 53 venues
		'''
	# 深入嵌套的字典和列表，获取最后一个演讲者的名字
	print(feed['Schedule']['speakers'][-1]['name'])
	
	# 获取那位演讲者的编号
	print(feed['Schedule']['speakers'][-1]['serial'])
	
	print(feed['Schedule']['events'][40]['name'])
	
	# 每个事件都有一个 'speakers' 字段，列出 0 个或多个演讲者的编号
	print(feed['Schedule']['events'][40]['speakers'])






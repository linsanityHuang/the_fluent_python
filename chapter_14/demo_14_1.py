import re
import reprlib
'''
示例 14-1 定义了一个 Sentence 类，通过索引从文本中提取单词。
示例 14-1　sentence.py：把句子划分为单词序列

任何 Python 序列都可迭代的原因是，它们都实现了 __getitem__ 方法。
其实，标准的序列也都实现了 __iter__ 方法，因此你也应该这么做。

此例中Sentence类可以迭代的原因是其实现了 __getitem__ 方法。
'''


RE_WORD = re.compile('\w+')


class Sentence:
	def __init__(self, text):
		self.text = text
		# re.findall 函数返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配
		self.words = RE_WORD.findall(text)

	def __getitem__(self, index):
		# self.words 中保存的是 .findall 函数返回的结果，因此直接返回指定索引位上的单词
		return self.words[index]

	# 为了完善序列协议，我们实现了 __len__ 方法；不过，为了让对象可以迭代，没必要实现这个方法。
	def __len__(self):
		return len(self.words)

	def __repr__(self):
		# reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串表示形式
		# 默认情况下，reprlib.repr 函数生成的字符串最多有 30 个字符。
		return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
	s = Sentence('"The time has come," the Walrus said,')
	print(s)
	'''Sentence('"The time ha... Walrus said,')'''
	# Sentence 实例可以迭代，是因为其实现了__getitem__特殊方法
	for word in s:
		print(word)
	'''
	The
	time
	has
	come
	the
	Walrus
	said
	'''
	# 因为可以迭代，所以 Sentence 对象可以用于构建列表和其他可迭代的类型
	print(list(s))
	'''['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']'''

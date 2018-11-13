import re
import reprlib
'''
示例 14-4　sentence_iter.py：使用迭代器模式实现 Sentence 类

典型的迭代器
Sentence是可迭代对象，对其调用iter函数，返回了SentenceIterator迭代器

迭代器SentenceIterator实现了标准迭代器的两个方法，__next__和__iter__
'''
RE_WORD = re.compile('\w+')


class Sentence:
	
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)
	
	# 与前一版相比，这里只多了一个 __iter__ 方法。
	# 这一版没有 __getitem__ 方法，为的是明确表明这个类可以迭代，因为实现了 __iter__ 方法
	def __iter__(self):
		# 根据可迭代协议，__iter__ 方法实例化并返回一个迭代器
		return SentenceIterator(self.words)


class SentenceIterator:
	
	def __init__(self, words):
		# SentenceIterator 实例引用单词列表
		self.words = words
		# self.index 用于确定下一个要获取的单词
		self.index = 0
	
	def __next__(self):
		try:
			# 获取 self.index 索引位上的单词
			word = self.words[self.index]
		except IndexError:
			# 如果 self.index 索引位上没有单词，那么抛出 StopIteration 异常
			raise StopIteration()
		# 递增 self.index 的值
		self.index += 1
		return word
	
	def __iter__(self):
		return self
		

if __name__ == '__main__':
	s = Sentence('"The time has come," the Walrus said,')
	print(s)
	'''Sentence('"The time ha... Walrus said,')'''
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

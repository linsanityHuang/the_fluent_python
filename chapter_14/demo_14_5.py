'''
实现相同功能，但却符合 Python 习惯的方式是，用生成器函数代替 SentenceIterator 类。

示例 14-5　sentence_gen.py：使用生成器函数实现 Sentence 类
'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
	
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)
	
	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)
	
	def __iter__(self):
		# 迭代 self.words
		for word in self.words:
			# 产出当前的 word
			yield word
		# 这个 return 语句不是必要的；这个函数可以直接“落空” ，自动返回
		# 不管有没有return 语句，生成器函数都不会抛出 StopIteration 异常，而是在生成完全部值之后会直接退出。
		return
	# 不用再单独定义一个迭代器类！


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
	print(list(s))
	'''['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']'''

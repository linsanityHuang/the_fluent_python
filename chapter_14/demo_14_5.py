'''
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


if __name__ == '__main__':
	s = Sentence('"The time has come," the Walrus said,')
	print(s)
	'''Sentence('"The time ha... Walrus said,')'''
	# Sentence 实例可以迭代，稍后说明原因
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

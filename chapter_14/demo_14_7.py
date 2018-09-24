'''
re.finditer 函数是 re.findall 函数的惰性版本，返回的不是列表，而是一个生成器，按需生成 re.MatchObject 实例。

如果有很多匹配，re.finditer 函数能节省大量内存。

我们要使用这个函数让第 4 版 Sentence 类变得懒惰，即只在需要时才生成下一个单词。代码如示例 14-7 所示。

示例 14-7　 sentence_gen2.py： 在 生 成 器 函 数 中 调 用 re.finditer 生 成 器 函 数， 实 现Sentence 类
'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
	
	def __init__(self, text):
		# 不再需要 words 列表
		self.text = text
	
	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)
	
	def __iter__(self):
		# finditer 函数构建一个迭代器，包含 self.text 中匹配 RE_WORD 的单词，产出 MatchObject 实例
		for match in RE_WORD.finditer(self.text):
			# match.group() 方法从 MatchObject 实例中提取匹配正则表达式的具体文本
			yield match.group()


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

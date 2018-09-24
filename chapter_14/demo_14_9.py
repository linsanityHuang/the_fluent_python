'''
生成器表达式会产出生成器，因此可以使用生成器表达式进一步减少 Sentence 类的代码，如示例 14-9 所示。
示例 14-9　sentence_genexp.py：使用生成器表达式实现 Sentence 类


与示例 14-7 唯一的区别是 __iter__ 方法，这里不是生成器函数了（没有 yield） ，而是使用生成器表达式构建生成器，然后将其返回。

不过，最终的效果一样：调用 __iter__ 方法会得到一个生成器对象。
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
		return (match.group() for match in RE_WORD.finditer(self.text))

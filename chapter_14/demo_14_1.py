import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __getitem__(self, index):
		return self.words[index]

	def __len__(self):
		return len(self.words)

	def __repr__(self):
		# reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串表示形式
		# 默认情况下，reprlib.repr 函数生成的字符串最多有 30 个字符。
		return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == '__main__':
	s = Sentence('"The time has come," the Walrus said,')
	print(s)
	for word in s:
		print(word)

	print(list(s))
	print(s[0])
	print(s[1])
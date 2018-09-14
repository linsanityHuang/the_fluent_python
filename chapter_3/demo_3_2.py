# coding=utf-8
# 这段程序从索引中获取单词出现的频率信息，并把它们写进对应的列表里（更好的解决方案在示例 3-4 中）

"""
统计文本中单词出现过的位置
python demo_3_2.py word.txt
"""

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
	# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
	# 同时列出数据和数据下标，一般用在 for 循环当中。
	# start=1,下标从1开始，默认是0
	for line_no, line in enumerate(fp, 1):
		for match in WORD_RE.finditer(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no, column_no)
			# 这其实是一种很不好的实现，这样写只是为了证明论点
			# 提取 word 出现的情况，如果还没有它的记录，返回 []
			occurences = index.get(word, [])
			# 把单词新出现的位置添加到列表的后面
			occurences.append(location)
			# 把新的列表放回字典中，这又牵扯到一次查询操作
			index[word] = occurences

# 以字母顺序打印出结果
# sorted 函数的 key= 参数没有调用 str.upper，而是把这个方法的引用传递给 sorted 函数，这样在排序的时候，单词会被规范成统一格式。
for word in sorted(index, key=str.upper):
	print(word, index[word])
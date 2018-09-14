# coding=utf-8
# 在有序序列中用bisect 查找某个元素的插入位置
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'

def demo(bisect_fn):
	for needle in reversed(NEEDLES):
		position = bisect_fn(HAYSTACK, needle)					# 用特定的bisect 函数来计算元素应该出现的位置。
		offset = position * ' |'								# 利用该位置来算出需要几个分隔符号。
		print(ROW_FMT.format(needle, position, offset))			# 把元素和其应该出现的位置打印出来。

import random
random.seed(1)

print('New  Pos Contents')
print('---  --- --------')
 
l = []
# 执行14次操作
for _ in range(1, 15):
	# 通过查看其ID，发现其为原地插入
	# print(id(l))
	# 先随机生成一个在1-100之间的整数
	r = random.randint(1, 100)
	# 然后使用bisect返回上述整数应该插入的位置，保证插入后，保证序列依旧是升序，当然，序列之前必须是一个有序的序列
	position = bisect.bisect(l, r)
	# 插入并保证元素顺序
	bisect.insort(l, r)
	print('%3d  %3d' % (r, position), l)



# if __name__ == '__main__':
# 	if sys.argv[-1] == 'left':									# 根据命令上最后一个参数来选用bisect 函数。
# 		bisect_fn = bisect.bisect_left
# 	else:
# 		bisect_fn = bisect.bisect
# 	print('DEMO:', bisect_fn.__name__)							# 把选定的函数在抬头打印出来。
# 	print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
# 	demo(bisect_fn)
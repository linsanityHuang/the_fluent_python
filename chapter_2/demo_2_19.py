# coding=utf-8
# insort(seq, item) 把变量 item 插入到序列 seq 中，并能保持 seq 的升序顺序
# bisect.insort(seq, item) 可以保持有序序列的顺序
import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
	new_item = random.randrange(SIZE * 2)
	print('new_item: %20d' % new_item)
	bisect.insort(my_list, new_item)
	print('%8d ->' % new_item, my_list)
import itertools
'''
示例 14-18　演示 itertools.product 生成器函数
'''

# 三个字符的字符串与两个整数的值域得到的笛卡儿积是六个元组（因为 3 * 2 等于 6）
print(list(itertools.product('ABC', range(2))))
'''[('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]'''
suits = 'spades hearts diamonds clubs'.split()
# 两张牌（'AK'）与四种花色得到的笛卡儿积是八个元组
print(list(itertools.product('AK', suits)))
'''
[
	('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'),
	('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')
]
'''
# 如果传入一个可迭代的对象，product 函数产出的是一系列只有一个元素的元组，不是特别有用
print(list(itertools.product('ABC')))
'''[('A',), ('B',), ('C',)]'''
# repeat=N 关键字参数告诉 product 函数重复 N 次处理输入的各个可迭代对象
print(list(itertools.product('ABC', repeat=2)))
'''
[
	('A', 'A'), ('A', 'B'), ('A', 'C'),
	('B', 'A'), ('B', 'B'), ('B', 'C'),
	('C', 'A'), ('C', 'B'), ('C', 'C')
]
'''

print(list(itertools.product(range(2), repeat=3)))
'''
[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
'''

rows = itertools.product('AB', range(2), repeat=2)
for row in rows:
	print(row)
	
'''
('A', 0, 'A', 0)
('A', 0, 'A', 1)
('A', 0, 'B', 0)
('A', 0, 'B', 1)
('A', 1, 'A', 0)
('A', 1, 'A', 1)
('A', 1, 'B', 0)
('A', 1, 'B', 1)
('B', 0, 'A', 0)
('B', 0, 'A', 1)
('B', 0, 'B', 0)
('B', 0, 'B', 1)
('B', 1, 'A', 0)
('B', 1, 'A', 1)
('B', 1, 'B', 0)
('B', 1, 'B', 1)
'''

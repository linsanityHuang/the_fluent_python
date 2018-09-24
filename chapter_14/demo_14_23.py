'''
示例 14-23　把几个序列传给 all 和 any 函数后得到的结果
'''

print(all([1, 2, 3]))

print(all([1, 0, 3]))

print(all([]))

print(any([1, 2, 3]))

print(any([1, 0, 3]))

print(any([0, 0.0]))

print(any([]))

g = (n for n in [0, 0.0, 7, 8])

print(any(g))
print(next(g))

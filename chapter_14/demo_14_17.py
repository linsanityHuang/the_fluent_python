import itertools
'''
示例 14-17　演示用于合并的生成器函数
'''

# 调用 chain 函数时通常传入两个或更多个可迭代对象
print(list(itertools.chain('ABC', range(2))))
'''['A', 'B', 'C', 0, 1]'''
# 如果只传入一个可迭代的对象，那么 chain 函数没什么用
print(list(itertools.chain(enumerate('ABC'))))
'''[(0, 'A'), (1, 'B'), (2, 'C')]'''
# 但是 chain.from_iterable 函数从可迭代的对象中获取每个元素，然后按顺序把元素连接起来，前提是各个元素本身也是可迭代的对象
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
'''[0, 'A', 1, 'B', 2, 'C']'''
# zip 常用于把两个可迭代的对象合并成一系列由两个元素组成的元组
print(list(zip('ABC', range(5))))
'''[('A', 0), ('B', 1), ('C', 2)]'''
# zip 可以并行处理任意数量个可迭代的对象，不过只要有一个可迭代的对象到头了，生成器就停止
print(list(zip('ABC', range(5), [10, 20, 30, 40])))
'''[('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]'''
# itertools.zip_longest 函数的作用与 zip 类似，不过输入的所有可迭代对象都会处理到头，如果需要会填充 None
print(list(itertools.zip_longest('ABC', range(5))))
'''[('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]'''
# fillvalue 关键字参数用于指定填充的值
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))
'''[('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]'''

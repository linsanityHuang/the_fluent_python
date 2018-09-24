import itertools
'''
示例 14-22　itertools.tee 函数产出多个生成器，每个生成器都可以产出输入的各个元素
'''

print(list(itertools.tee('ABC')))
'''[<itertools._tee object at 0x103d0a848>, <itertools._tee object at 0x103d0a888>]'''
g1, g2 = itertools.tee('ABC')

print(next(g1))
'''A'''
print(next(g2))
'''A'''
print(next(g2))
'''B'''
print(list(g1))
'''['B', 'C']'''
print(list(g2))
'''['C']'''
print(list(zip(*itertools.tee('ABC'))))
'''[('A', 'A'), ('B', 'B'), ('C', 'C')]'''

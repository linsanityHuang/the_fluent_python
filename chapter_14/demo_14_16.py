import operator
import itertools
'''
示例 14-16　演示用于映射的生成器函数
'''
# 从 1 开始，为单词中的字母编号
print(list(enumerate('albatroz', 1)))
'''[(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]'''
# 从 0 到 10，计算各个整数的平方
print(list(map(operator.mul, range(11), range(11))))
'''[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''
# 计算两个可迭代对象中对应位置上的两个元素之积，元素最少的那个可迭代对象到头后就停止
print(list(map(operator.mul, range(11), [2, 4, 8])))
'''[0, 4, 16]'''
# 作用等同于内置的 zip 函数
print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))
'''[(0, 2), (1, 4), (2, 8)]'''
# 从 1 开始，根据字母所在的位置，把字母重复相应的次数
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))
'''['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']'''
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
# 计算平均值
print(list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))))
'''[5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.888888888888889, 4.5]'''

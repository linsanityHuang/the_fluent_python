import itertools
import operator
'''
示例 14-15 演示 itertools.accumulate 函数的几个用法。
示例 14-15　演示 itertools.accumulate 生成器函数
'''


sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

# 计算总和
print(list(itertools.accumulate(sample)))
'''[5, 9, 11, 19, 26, 32, 35, 35, 44, 45]'''
# 计算最小值
print(list(itertools.accumulate(sample, min)))
'''[5, 4, 2, 2, 2, 2, 2, 0, 0, 0]'''
# 计算最大值
print(list(itertools.accumulate(sample, max)))
'''[5, 5, 5, 8, 8, 8, 8, 8, 9, 9]'''
# 计算乘积
print(list(itertools.accumulate(sample, operator.mul)))
'''[5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]'''
# 从 1! 到 10!，计算各个数的阶乘
print(list(itertools.accumulate(range(1, 11), operator.mul)))
'''[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]'''

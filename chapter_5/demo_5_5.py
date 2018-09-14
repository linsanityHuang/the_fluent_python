'''
示例 5-5　计算阶乘列表：map 和 filter 与列表推导比较
'''

def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

print(list(map(factorial, range(6))))
print([factorial(n) for n in range(6)])


print(list(map(factorial, filter(lambda x: x % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])


'''
示例 5-6　使用 reduce 和 sum 计算 0~99 之和
'''
from functools import reduce        # 从 Python 3.0 起，reduce 不再是内置函数了
from operator import add            # 导入 add，以免创建一个专求两数之和的函数
print(reduce(add, range(100)))      # 计算 0~99 之和。
print(sum(range(100)))              # 使用 sum 做相同的求和；无需导入或创建求和函数
'''
在参数列表中最适合使用匿名函数。
例如，示例 5-7 使用 lambda 表达式重写了示例 5-4 中排序押韵单词的示例，
这样就省掉了 reverse 函数。
'''

# 示例 5-7　使用 lambda 表达式反转拼写，然后依此给单词列表排序

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))

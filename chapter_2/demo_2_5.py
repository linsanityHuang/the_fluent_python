# 用生成器表达式初始化元组和数组

symbols = '$¢£¥€¤'
# 如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外再用括号把它围起来。
print(tuple(ord(symbol) for symbol in symbols))

import array
# array 的构造方法需要两个参数，因此括号是必需的。array 构造方法的第一个参数指定了数组中数字的存储方式。
print(array.array('I', (ord(symbol) for symbol in symbols)))
# coding=utf-8
# 如果我们需要一个只包含数字的列表，那么 array.array 比 list 更高效。
# 数组支持所有跟可变序列有关的操作，包括 .pop、.insert 和 .extend。
# 另外，数组还提供从文件读取和存入文件的更快的方法，如 .frombytes 和 .tofile。



# 示例2-20 展示了从创建一个有1000 万个随机浮点数的数组开始，到如何把这个数组存放到文件里，再到如何从文件读取这个数组。

# 一个浮点型数组的创建、存入文件和从文件读取的过程
from array import array									# 引入array 类型。
from random import random
floats = array('d', (random() for i in range(10**7)))	# 利用一个可迭代对象来建立一个双精度浮点数组（类型码是'd'），这里我们用的可迭代对象是一个生成器表达式。
print(floats[-1])										# 查看数组的最后一个元素。
with open('floats.bin', 'wb') as f:
    floats.tofile(f)                                    # 把数组存入一个二进制文件里。

floats2 = array('d')									# 新建一个双精度浮点空数组。
with open('floats.bin', 'rb') as f:
    floats2.fromfile(f, 10**7)                          # 把1000 万个浮点数从二进制文件里读取出来。

print(floats2[-1])										# 查看新数组的最后一个元素。
print(floats2 == floats)								# 检查两个数组的内容是不是完全一样。

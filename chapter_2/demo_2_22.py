# coding=utf-8
# 对 numpy.ndarray 的行和列进行基本操作

import numpy as np
a = np.arange(12)
print(a)

print(type(a))

print(a.shape)

a.shape = 3, 4
print(a)

print(a[2])
print(a[2, 1])
print(a[:, 1])

print(a.transpose())

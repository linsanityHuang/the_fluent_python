'''
从 Python 3.3 开始，types 模块中引入了一个封装类名叫 MappingProxyType。
如果给这个类一个映射，它会返回一个只读的映射视图。
虽然是个只读视图，但是它是动态的。
这意味着如果对原映射做出了改动，我们通过这个视图可以观察到，但是无法通过这个视图对原映射做出修改。
示例 3-9 简短地对这个类的用法做了个演示。
'''

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)

# d_proxy[2] = 'X'
# TypeError: 'mappingproxy' object does not support item assignment

d[2] = 'X'
print(d_proxy)
print(d_proxy[2])
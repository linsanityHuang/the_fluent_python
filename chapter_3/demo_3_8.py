
'''
而更倾向于从 UserDict 而不是从 dict 继承的主要原因是，
后者有时会在某些方法的实现上走一些捷径，导致我们不得不在它的子类中重写这些方法，但是 UserDict 就不会带来这些问题。

另外一个值得注意的地方是，UserDict 并不是 dict 的子类，
但是 UserDict 有一个叫作data 的属性，是 dict 的实例，这个属性实际上是 UserDict 最终存储数据的地方。

这样做的好处是，比起示例 3-7，UserDict 的子类就能在实现 __setitem__ 的时候避免不必要的递归，也可以让 __contains__ 里的代码更简洁。

多亏了 UserDict，示例 3-8 里的 StrKeyDict 的代码比示例 3-7 里的 StrKeyDict0 要短一些，功能却更完善：
它不但把所有的键都以字符串的形式存储，还能处理一些创建或者更新实例时包含非字符串类型的键这类意外情况。
'''

# 无论是添加、更新还是查询操作，StrKeyDict 都会把非字符串的键转换为字符串

from collections import UserDict

# StrKeyDict 是对 UserDict 的扩展
class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    # __contains__ 则更简洁些。
    # 这里可以放心假设所有已经存储的键都是字符串。
    # 因此，只要在 self.data 上查询就好了，
    # 并不需要像 StrKeyDict0 那样去麻烦 self.keys()
    def __contains__(self, key):
        return str(key) in self.data

    # __setitem__ 会把所有的键都转换成字符串。
    # 由于把具体的实现委托给了 self.data 属性，这个方法写起来也不难。
    def __setitem__(self, key, item):
        self.data[str(key)] = item


def main():
    d = StrKeyDict([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d[4])
    print(d[1])

def main1():
    d = StrKeyDict([('2', 'two'), ('4', 'four')])
    print(d.get('2'))
    print(d.get(4))
    print(d.get(1, 'N/A'))

if __name__ == '__main__':
    main1()
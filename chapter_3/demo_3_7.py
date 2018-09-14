# StrKeyDict0 在查询的时候把非字符串的键转换为字符串

'''
如 果 要 自 定 义 一 个 映 射 类 型， 更 合 适 的 策 略 其 实 是 继 承 collections.
UserDict 类（示例 3-8 就是如此） 。

这里我们从 dict 继承，只是为了演示 __missing__ 是如何被 dict.__getitem__ 调用的
'''
'''
为什么 isinstance(key, str) 测试在上 __missing__ 中是必需的。
如果没有这个测试，只要 str(k) 返回的是一个存在的键，那么 __missing__ 方法是没问题的，不管是字符串键还是非字符串键，它都能正常运行。
但是如果 str(k) 不是一个存在的键，代码就会陷入无限递归。
这是因为 __missing__ 的最后一行中的 self[str(key)] 会调用 __getitem__，而这个 str(key) 又不存在，于是 __missing__ 又会被调用。

为了保持一致性，__contains__ 方法在这里也是必需的。
这是因为 k in d 这个操作会调用它，但是我们从 dict 继承到的 __contains__ 方法不会在找不到键的时候调用 __missing__ 方法。
__contains__ 里还有个细节，就是我们这里没有用更具 Python 风格的方式——k in my_dict——来检查键是否存在，
因为那也会导致 __contains__ 被递归调用。
为了避免这一情况，这里采取了更显式的方法，直接在这个 self.keys() 里查询
'''
class StrKeyDict0(dict):

    def __missing__(self, key):
        # 如果找不到的键本身就是字符串，那就抛出 KeyError 异常
        if isinstance(key, str):
            raise KeyError(key)
        # 如果找不到的键不是字符串，那么把它转换成字符串再进行查找
        return self[str(key)]

    def get(self, key, default=None):
        try:
            # get 方法把查找工作用 self[key] 的形式委托给 __getitem__，  
            # 这样在宣布查找失败之前，还能通过 __missing__ 再给某个键一个机会
            return self[key]
        except KeyError:
            # 如果抛出 KeyError，那么说明 __missing__ 也失败了，于是返回 default
            return default
    
    def __contains__(self, key):
        # 先按照传入键的原本的值来查找（我们的映射类型中可能含有非字符串的键）
        # 如果没找到，再用 str() 方法把键转换成字符串再查找一次
        return key in self.keys() or str(key) in self.keys()

def main():
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d[4])
    print(d[1])

def main1():
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d.get('2'))
    print(d.get(4))
    print(d.get(1, 'N/A'))

if __name__ == '__main__':
    main1()
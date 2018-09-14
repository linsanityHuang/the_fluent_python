'''
在 Python 3 里面，除了空集，集合的字符串表示形式总是以 {...} 的形式出现
像 {1, 2, 3} 这种字面量句法相比于构造方法（set([1, 2, 3])）要更快且更易读。
后者的速度要慢一些，因为 Python 必须先从 set 这个名字来查询构造方法，然后新建一个列表，最后再把这个列表传入到构造方法里。
但是如果是像 {1, 2, 3} 这样的字面量，Python 会利用一个专门的叫作 BUILD_SET 的字节码来创建集合。
'''

# 用 dis.dis（反汇编函数）来看看两个方法的字节码的不同
from dis import dis
# 检查 {1} 字面量背后的字节码
print(dis('{1}'))
'''
1           0 LOAD_CONST               0 (1)
            2 BUILD_SET                1        特殊的字节码 BUILD_SET 几乎完成了所有的工作
            4 RETURN_VALUE
'''

# set([1]) 的字节码
print(dis('set([1])'))
'''
1           0 LOAD_NAME                0 (set)  3 种不同的操作代替了上面的 BUILD_SET：LOAD_NAME、BUILD_LIST 和 CALL_FUNCTION
            2 LOAD_CONST               0 (1)
            4 BUILD_LIST               1
            6 CALL_FUNCTION            1
            8 RETURN_VALUE
'''

'''
由于 Python 里没有针对 frozenset 的特殊字面量句法，我们只能采用构造方法。
Python 3 里 frozenset 的标准字符串表示形式看起来就像构造方法调用一样。来看这段控制台对话
'''
print(frozenset(range(10)))
'''
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
'''
'''
在 operator 模块余下的函数中，我们最后介绍一下 methodcaller。

它的作用与 attrgetter 和 itemgetter 类似，它会自行创建函数。

methodcaller 创建的函数会在对象上调用参数指定的方法，如示例 5-25 所示。

示例 5-25　methodcaller 使用示例：第二个测试展示绑定额外参数的方式
'''
from operator import methodcaller

s = 'The time has come'

upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))

'''
示例 5-25 中的第一个测试只是为了展示 methodcaller 的用法，

如果想把 str.upper 作为函数使用，只需在 str 类上调用，并传入一个字符串参数，如下所示
'''
print(str.upper(s))

'''
示例 5-25 中的第二个测试表明，methodcaller 还可以冻结某些参数，也就是部分应用（partial application） ，
这与 functools.partial 函数的作用类似。
'''
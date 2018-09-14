'''
示例 5-17　提取函数的签名
'''
'''
inspect.signature 函数返回一个 inspect.Signature 对象，

它有一个 parameters 属性，这是一个有序映射，把参数名和 inspect.Parameter 对象对应起来。

各个 Parameter 属性也有自己的属性，例如 name、default 和 kind。

特殊的 inspect._empty 值表示没有默认值，

考虑到 None 是有效的默认值（也经常这么做） ，而且这么做是合理的
'''
from demo_5_12 import clip
from inspect import signature

sig = signature(clip)
print(sig)
# (text, max_len=80)
'''
kind 属性的值是 _ParameterKind 类中的 5 个值之一，列举如下。

POSITIONAL_OR_KEYWORD           可以通过定位参数和关键字参数传入的形参（多数 Python 函数的参数属于此类）
VAR_POSITIONAL                  定位参数元组
VAR_KEYWORD                     关键字参数字典。
KEYWORD_ONLY                    仅限关键字参数（Python 3 新增） 。
POSITIONAL_ONLY                 仅限定位参数；目前，Python 声明函数的句法不支持，但是有些使用 C 语言实现且不接受关键字参数的函数（如 divmod）支持
'''
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

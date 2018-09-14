'''
Python 对注解所做的唯一的事情是，把它们存储在函数的 __annotations__ 属性里。

仅此而已，Python 不做检查、不做强制、不做验证，什么操作都不做。换句话说，

注解对Python 解释器没有任何意义。注解只是元数据，可以供 IDE、框架和装饰器等工具使用。

写作本书时，标准库中还没有什么会用到这些元数据，

唯有 inspect.signature() 函数知道怎么提取注解，如示例 5-20 所示
'''

# 示例 5-20　从函数签名中提取注解
from chapter_5.demo_5_19 import clip
from inspect import signature

sig = signature(clip)

print(sig.return_annotation)
for param in sig.parameters.values():
	note = repr(param.annotation).ljust(13)
	print(note, ':', param.name, '=', param.default)

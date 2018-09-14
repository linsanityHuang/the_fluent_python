'''
functools 模块提供了一系列高阶函数，其中最为人熟知的或许是 reduce，我们在 5.2.1 节已经介绍过。

余下的函数中，最有用的是 partial 及其变体，partialmethod。

functools.partial 这个高阶函数用于部分应用一个函数。

部分应用是指，基于一个函数创建一个新的可调用对象，把原函数的某些参数固定。

使用这个函数可以把接受一个或多个参数的函数改编成需要回调的 API，这样参数更少。示例 5-26 做了简单的演示
'''
# 示例 5-26　使用 partial 把一个两参数函数改编成需要单参数的可调用对象

from operator import mul
from functools import partial

# 使用 mul 创建 triple 函数，把第一个定位参数定为 3
triple = partial(mul, 3)
# 测试 triple 函数
print(triple(7))
# 在 map 中使用 triple；在这个示例中不能使用 mul
print(list(map(triple, range(1, 10))))

'''
使用 4.6 节介绍的 unicode.normalize 函数再举个例子，这个示例更有实际意义。

如果处理多国语言编写的文本，在比较或排序之前可能会想使用 unicode.normalize('NFC', s) 处理所有字符串 s。

如果经常这么做，可以定义一个 nfc 函数，如示例 5-27 所示。
'''
import unicodedata, functools
nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'

print(s1 == s2)
print(nfc(s1) == nfc(s2))

'''
partial 的第一个参数是一个可调用对象，后面跟着任意个要绑定的定位参数和关键字参数。
示例 5-28 在示例 5-10 中定义的 tag 函数上使用 partial，冻结一个定位参数和一个关键字参数。
示例 5-28　把 partial 应用到示例 5-10 中定义的 tag 函数上
'''
from chapter_5.demo_5_10 import tag
picture = functools.partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))
'''
<img class="pic-frame" src="wumpus.jpeg" />
'''
print(picture)
'''
functools.partial(<function tag at 0x10b9e89d8>, 'img', cls='pic-frame')
'''

print(picture.func)
'''
<function tag at 0x10b9e89d8>
'''
print(picture.args)
'''
('img',)
'''
print(picture.keywords)
'''
{'cls': 'pic-frame'}
'''
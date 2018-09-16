'''
因为 Python 不支持重载方法或函数，所以我们不能使用不同的签名定义 htmlize 的变体，也无法使用不同的方式处理不同的数据类型。

在 Python 中，一种常见的做法是把 htmlize 变成一个分派函数，使用一串 if/elif/elif，调用专门的函数，

如 htmlize_str、htmlize_ int，等等。

这样不便于模块的用户扩展，还显得笨拙：时间一长，分派函数 htmlize 会变得很大，而且它与各个专门函数之间的耦合也很紧密。

Python 3.4 新增的 functools.singledispatch 装饰器可以把整体方案拆分成多个模块，甚至可以为你无法修改的类提供专门的函数。

使用 @singledispatch 装饰的普通函数会变成泛函数（generic function） ：根据第一个参数的类型，以不同方式执行相同操作的一组函数。
'''


# 示例 7-21　 singledispatch 创建一个自定义的 htmlize.register 装饰器，把多个函数绑在一起组成一个泛函数
from functools import singledispatch
from collections import abc
import numbers
import html


# @singledispatch 标记处理 object 类型的基函数。
@singledispatch
def htmlize(obj):
	content = html.escape(repr(obj))
	return '<pre>{}</pre>'.format(content)
	

# 各个专门函数使用 @«base_function».register(«type») 装饰。
@htmlize.register(str)
# 专门函数的名称无关紧要；_ 是个不错的选择，简单明了
def _(text):
	content = html.escape(text).replace('\n', '<br>\n')
	return '<p>{0}</p>'.format(content)


# 为每个需要特殊处理的类型注册一个函数。numbers.Integral 是 int 的虚拟超类。
@htmlize.register(numbers.Integral)
def _(n):
	return '<pre>{0} (0x{0:x})</pre>'.format(n)


# 可以叠放多个 register 装饰器，让同一个函数支持不同类型。
@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
	inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
	return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
	print(htmlize({1, 2, 3}))
	'''<pre>{1, 2, 3}</pre>'''
	print(htmlize(abs))
	'''<pre>&lt;built-in function abs&gt;</pre>'''
	print(htmlize('Heimlich & Co.\n- a game'))
	'''<p>Heimlich &amp; Co.<br>
		- a game</p>'''
	print(htmlize(42))
	'''<pre>42 (0x2a)</pre>'''
	print(htmlize(['alpha', 66, {3, 2, 1}]))
	'''
	<ul>
	<li><p>alpha</p></li>
	<li><pre>66 (0x42)</pre></li>
	<li><pre>{1, 2, 3}</pre></li>
	</ul>
	'''
# coding=utf-8
'''
tag 函数用于生成 HTML 标签；

使用名为 cls 的关键字参数传入“class”属性，这是一种变通方法，因为“class”是 Python 的关键字
'''
def tag(name, *content, cls=None, **attrs):
	'''生成一个或多个HTML标签'''
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
	else:
		attr_str = ''

	if content:
		return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
	# 传入单个定位参数，生成一个指定名称的空标签
	print(tag('br'))									# <br />
	# 第一个参数后面的任意个参数会被 *content 捕获，存入一个元组
	print(tag('p', 'hello'))							# <p>hello</p>
	print(tag('p', 'hello', 'world'))					# <p>hello</p> <p>world</p>
	# tag 函数签名中没有明确指定名称的关键字参数会被 **attrs 捕获，存入一个字典
	print(tag('p', 'hello', id=33))						# <p id="33">hello</p>
	# cls 参数只能作为关键字参数传入
	print(tag('p', 'hello', 'world', cls='sidebar'))	# <p class="sidebar">hello</p>	<p class="sidebar">world</p>
	# 调用 tag 函数时，即便第一个定位参数也能作为关键字参数传入
	print(tag(content='testing', name="img"))			# <img content="testing" />
	my_tag = {'name': 'img', 'title': 'Sunset Boulevard','src': 'sunset.jpg', 'cls': 'framed'}
	# 在 my_tag 前面加上 **，字典中的所有元素作为单个参数传入，同名键会绑定到对应的具名参数上，余下的则被 **attrs 捕获
	print(tag(**my_tag))								# <img class="framed" src="sunset.jpg" title="Sunset Boulevard" />
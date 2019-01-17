'''
函数对象有个 __defaults__ 属性，它的值是一个元组，里面保存着定位参数和关键字参数的默认值。

仅限关键字参数的默认值在 __kwdefaults__ 属性中。

然而，参数的名称在 __code__ 属性中，它的值是一个 code 对象引用，自身也有很多属性。

为了说明这些属性的用途，下面在 clip.py 模块中定义 clip 函数，如示例 5-15 所示，然后再审查它。

示例 5-15　在指定长度附近截断字符串的函数
'''


def clip(text, max_len=80):
	"""在max_len前面或后面的第一个空格处截断文本
	"""
	end = None
	if len(text) > max_len:
		space_before = text.rfind(' ', 0, max_len)
		if space_before >= 0:
			end = space_before
		else:
			space_after = text.rfind(' ', max_len)
			if space_after >= 0:
				end = space_after
	if end is None:		# 没找到空格
		end = len(text)
	return text[:end].rstrip()


if __name__ == '__main__':
	# 提取关于函数参数的信息
	print('clip.__defaults__', clip.__defaults__)
	print('clip.__code__.co_varnames', clip.__code__.co_varnames)
	print('clip.__code__.co_argcount', clip.__code__.co_argcount)

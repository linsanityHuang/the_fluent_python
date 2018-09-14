# coding=utf-8
'''
示例 5-12　Bobo 知道 hello 需要 person 参数，并且从 HTTP 请求中获取它
'''
# import bobo

# @bobo.query('/')
def hello(person):
	return 'Hello %s!' % person

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

# 示例 5-16　提取关于函数参数的信息
if __name__ == '__main__':
	print(clip.__defaults__)			# (80,)
	print(clip.__code__)				# <code object clip at 0x105256db0, file "/Users/huangjiansheng/Documents/the_fluent_python/chapter_5/demo_5_12.py", line 22>
	print(clip.__code__.co_varnames)	# ('text', 'max_len', 'end', 'space_before', 'space_after')
	print(clip.__code__.co_argcount)	# 2
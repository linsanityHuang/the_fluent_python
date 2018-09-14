'''
Python 3 提供了一种句法，用于为函数声明中的参数和返回值附加元数据。

示例 5-19 是示例 5-15 添加注解后的版本，二者唯一的区别在第一行。
'''
# 示例 5-19　有注解的 clip 函数

def clip(text:str, max_len:'int > 0'=80) -> str:
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
# 示例 5-19　有注解的 clip 函数


def clip(text: str, max_len: 'int > 0' = 80) -> str:
# def clip(text, max_len=80):
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
	if end is None:  # 没找到空格
		end = len(text)
	return text[:end].rstrip()


if __name__ == '__main__':
	'''
	{'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}
	'''
	# 注解不会做任何处理，只是存储在函数的 __annotations__ 属性（一个字典）中
	print(clip.__annotations__)

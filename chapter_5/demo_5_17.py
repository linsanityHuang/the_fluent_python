'''
示例 5-17　提取函数的签名
'''
from inspect import signature


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


'''
为了确认被装饰的函数会被替换，请看示例 7-1 中的控制台会话。

示例 7-1　装饰器通常把函数替换成另一个函数
'''

def deco(func):
	def inner():
		print('running inner()')
	return inner					# deco 返回 inner 函数对象

@deco
def target():						#使用 deco 装饰 target
	print('running target()')
	

target()							#调用被装饰的 target 其实会运行 inner
print(target)						#审查对象，发现 target 现在是 inner 的引用
'''
<function deco.<locals>.inner at 0x1076f79d8>
'''
'''
综上，装饰器的一大特性是，能把被装饰的函数替换成其他函数。

第二个特性是，装饰器在加载模块时立即执行。
'''
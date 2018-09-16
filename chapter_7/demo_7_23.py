'''
为了便于启用或禁用 register 执行的函数注册功能，我们为它提供一个可选的 active 参数，设为 False 时，不注册被装饰的函数。

实现方式参见示例 7-23。

从概念上看，这个新的 register 函数不是装饰器，而是装饰器工厂函数。

调用它会返回真正的装饰器，这才是应用到目标函数上的装饰器。

示例 7-23　为了接受参数，新的 register 装饰器必须作为函数调用
'''

# registry 现在是一个 set 对象，这样添加和删除函数的速度更快
registry = set()


# register 接受一个可选的关键字参数
def register(active=True):
	# decorate这个内部函数是真正的装饰器；注意，它的参数是一个函数
	def decorate(func):
		print('running register(active=%s)->decorate(%s)' % (active, func))
		# 只有active参数的值（从闭包中获取）是True时才注册func
		if active:
			registry.add(func)
		# 如果active不为真，而且func在registry中，那么把它删除
		else:
			registry.discard(func)
		# decorate是装饰器，必须返回一个函数
		return func
	
	# register是装饰器工厂函数，因此返回decorate
	return decorate


# @register 工厂函数必须作为函数调用，并且传入所需的参数
@register(active=False)
def f1():
	print('running f1()')


# 即使不传入参数，register 也必须作为函数调用（@register()） ，即要返回真正的装饰器 decorate
@register()
def f2():
	print('running f2()')


def f3():
	print('running f3()')
	

print('running main()')
print('registry ->', registry)
f1()

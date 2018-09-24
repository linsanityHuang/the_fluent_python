'''
本节的主要观点是，obj.attr 这样的表达式不会从 obj 开始寻找 attr，而是从 obj.__ class__ 开始，

而且，仅当类中没有名为 attr 的特性时，Python 才会在 obj 实例中寻找。

这条规则不仅适用于特性，还适用于一整类描述符——覆盖型描述符（overriding descriptor） 。

第 20 章会进一步讨论描述符，那时你会发现，特性其实是覆盖型描述符。
'''

'''
如果实例和所属的类有同名数据属性，那么实例属性会覆盖（或称遮盖）类属性——至少通过那个实例读取属性时是这样。

示例 19-19 阐明了这一点。

示例 19-19　实例属性遮盖类的数据属性
'''


# 定义 Class 类，这个类有两个类属性：data 数据属性和 prop 特性
class Class:
	data = 'the class data attr'
	
	@property
	def prop(self):
		return 'the prop value'


if __name__ == '__main__':
	obj = Class()
	# vars 函数返回 obj 的 __dict__ 属性，表明没有实例属性
	print(vars(obj))
	'''{}'''
	# 读取 obj.data，获取的是 Class.data 的值
	print(obj.data)
	'''the class data attr'''
	# 为 obj.data 赋值，创建一个实例属性
	obj.data = 'bar'
	# 审查实例，查看实例属性
	print(vars(obj))
	'''{'data': 'bar'}'''
	# 现在读取 obj.data，获取的是实例属性的值。从 obj 实例中读取属性时，实例属性data 会遮盖类属性 data
	print(obj.data)
	'''bar'''
	# Class.data 属性的值完好无损
	print(Class.data)
	'''the class data attr'''
	
	# 下面尝试覆盖 obj 实例的 prop 特性。
	# 直接从 Class 中读取 prop 特性，获取的是特性对象本身，不会运行特性的读值方法
	print(Class.prop)
	'''<property object at 0x10ab43a98>'''
	# 读取 obj.prop 会执行特性的读值方法
	print(obj.prop)
	'''the prop value'''
	# 尝试设置 prop 实例属性，结果失败
	# obj.prop = 'foo'
	# 但是可以直接把 'prop' 存入 obj.__dict__
	obj.__dict__['prop'] = 'foo'
	# 可以看到，obj 现在有两个实例属性：data 和 prop
	print(vars(obj))
	'''{'data': 'bar', 'prop': 'foo'}'''
	# 然而，读取 obj.prop 时仍会运行特性的读值方法。特性没被实例属性遮盖
	print(obj.prop)
	'''the prop value'''
	# 覆盖 Class.prop 特性，销毁特性对象
	Class.prop = 'baz'
	# 现在，obj.prop 获取的是实例属性。Class.prop 不是特性了，因此不会再覆盖 obj.prop
	print(obj.prop)
	'''foo'''
	
	# 最后再举一个例子，为 Class 类新添一个特性，覆盖实例属性
	print('最后再举一个例子，为 Class 类新添一个特性，覆盖实例属性')
	# obj.data 获取的是实例属性 data
	print(obj.data)
	'''bar'''
	# Class.data 获取的是类属性 data
	print(Class.data)
	'''the class data attr'''
	# 使用新特性覆盖 Class.data
	Class.data = property(lambda self: 'the "data" prop value')
	# 现在，obj.data 被 Class.data 特性遮盖了
	print(obj.data)
	'''the "data" prop value'''
	# 删除特性
	del Class.data
	# 现在恢复原样，obj.data 获取的是实例属性 data
	print(obj.data)
	'''bar'''


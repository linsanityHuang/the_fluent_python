'''
控制台中的 help() 函数或 IDE 等工具需要显示特性的文档时，会从特性的 __doc__ 属性中提取信息。

如果使用经典调用句法，为 property 对象设置文档字符串的方法是传入 doc 参数：
	weight = property(get_weight, set_weight, doc='weight in kilograms')
	
使用装饰器创建 property 对象时，读值方法（有 @property 装饰器的方法）的文档字符串作为一个整体，变成特性的文档。
'''
class Foo:
	@property
	def bar(self):
		'''The bar attribute'''
		return self.__dict__['bar']
	
	@bar.setter
	def bar(self, value):
		self.__dict__['bar'] = value


if __name__ == '__main__':
	help(Foo.bar)
	'''
	Help on property:

    	The bar attribute
	'''
	help(Foo)
	'''
	Help on class Foo in module __main__:

	class Foo(builtins.object)
	 |  Data descriptors defined here:
	 |
	 |  __dict__
	 |      dictionary for instance variables (if defined)
	 |
	 |  __weakref__
	 |      list of weak references to the object (if defined)
	 |
	 |  bar
	 |      The bar attribute
	'''

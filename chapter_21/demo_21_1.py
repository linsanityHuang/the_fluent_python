def record_factory(cls_name, field_names):
	try:
		# 这里体现了鸭子类型：尝试在逗号或空格处拆分 field_names；如果失败，
		# 那么假定field_names 本就是可迭代的对象，一个元素对应一个属性名
		field_names = field_names.replace(',', ' ').split()
	except AttributeError:
		pass
	# 使用属性名构建元组，这将成为新建类的 __slots__ 属性；
	# 此外，这么做还设定了拆包和字符串表示形式中各字段的顺序。
	field_names = tuple(field_names)
	
	# 这个函数将成为新建类的 __init__ 方法。参数有位置参数和（或）关键字参数。
	def __init__(self, *args, **kwargs):
		attrs = dict(zip(self.__slots__, args))
		attrs.update(kwargs)
		for name, value in attrs.items():
			setattr(self, name, value)
	
	# 实现 __iter__ 函数，把类的实例变成可迭代的对象；
	# 按照 __slots__ 设定的顺序产出字段值。
	def __iter__(self):
		for name in self.__slots__:
			yield getattr(self, name)
	
	# 迭代 __slots__ 和 self，生成友好的字符串表示形式。
	def __repr__(self):
		values = ', '.join('{}={!r}'.format(*i) for i in zip(self.__slots__, self))
		return '{}({})'.format(self.__class__.__name__, values)
	
	# 组建类属性字典
	cls_attrs = dict(
		__slots__=field_names,
		__init__=__init__,
		__iter__=__iter__,
		__repr__=__repr__
	)
	
	# 调用 type 构造方法，构建新类，然后将其返回
	return type(cls_name, (object,), cls_attrs)


if __name__ == '__main__':
	Dog = record_factory('Dog', 'name weight owner')
	rex = Dog('Rex', 30, 'Bob')
	print(rex)

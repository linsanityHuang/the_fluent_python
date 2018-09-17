'''
示例 8-12　一个简单的类，说明可变默认值的危险
'''


class HauntedBus:
	"""备受幽灵乘客折磨的校车"""
	
	# 如果没传入 passengers 参数，使用默认绑定的列表对象，一开始是空列表
	def __init__(self, passengers=[]):
		# 这个赋值语句把 self.passengers 变成 passengers 的别名，而没有传入 passengers 参数时，后者又是默认列表的别名。
		self.passengers = passengers
		
	def pick(self, name):
		# 在 self.passengers 上调用 .remove() 和 .append() 方法时，修改的其实是默认列表，它是函数对象的一个属性
		self.passengers.append(name)
		
	def drop(self, name):
		self.passengers.remove(name)


if __name__ == '__main__':
	bus1 = HauntedBus(['Alice', 'Bill'])
	print(bus1.passengers)
	'''['Alice', 'Bill']'''
	bus1.pick('Charlie')
	bus1.drop('Alice')
	print(bus1.passengers)
	'''['Bill', 'Charlie']'''
	
	bus2 = HauntedBus()
	bus2.pick('Carrie')
	print(bus2.passengers)
	'''['Carrie']'''
	
	bus3 = HauntedBus()
	print(bus3.passengers)
	'''['Carrie']'''
	bus3.pick('Dave')
	print(bus2.passengers)
	'''['Carrie', 'Dave']'''
	
	print(bus2.passengers is bus3.passengers)
	'''True'''
	
	print(bus1.passengers)
	'''['Bill', 'Charlie']'''

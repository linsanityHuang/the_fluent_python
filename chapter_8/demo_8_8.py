import copy

'''
浅复制没什么问题，但有时我们需要的是深复制（即副本不共享内部对象的引用） 。

copy 模块提供的 deepcopy 和 copy 函数能为任意对象做深复制和浅复制。

为了演示 copy() 和 deepcopy() 的用法，示例 8-8 定义了一个简单的类，Bus。

这个类表示运载乘客的校车，在途中乘客会上车或下车。
'''


# 示例 8-8　校车乘客在途中上车和下车
class Bus:
	
	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list(passengers)
	
	def pick(self, name):
		self.passengers.append(name)
		
	def drop(self, name):
		self.passengers.remove(name)


if __name__ == '__main__':
	bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
	bus2 = copy.copy(bus1)
	bus3 = copy.deepcopy(bus1)
	
	# 使用 copy 和 deepcopy，创建 3 个不同的 Bus 实例
	print(id(bus1))
	print(id(bus2))
	print(id(bus3))
	
	bus1.drop('Bill')
	
	# bus1 中的 'Bill' 下车后，bus2 中也没有他了
	print(bus2.passengers)
	
	# 审查 passengers 属性后发现，bus1 和 bus2 共享同一个列表对象，因为 bus2 是 bus1 的浅复制副本
	print(id(bus1.passengers))
	print(id(bus2.passengers))
	print(id(bus3.passengers))
	
	# bus3 是 bus1 的深复制副本，因此它的 passengers 属性指代另一个列表
	print(bus3.passengers)

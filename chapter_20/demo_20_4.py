import chapter_20.model_v4c as model

'''
示例 20-4 是描述符的常规用法
'''


class LineItem:
	weight = model.Quantity()
	price = model.Quantity()
	
	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price
	
	def subtotal(self):
		return self.weight * self.price


if __name__ == '__main__':
	print(LineItem.price)
	'''<__main__.Quantity object at 0x1014e44e0>'''
	br_nuts = LineItem('Brazil nuts', 10, 34.95)
	print(br_nuts.price)
	'''34.95'''

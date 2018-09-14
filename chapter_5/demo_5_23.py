'''
operator 模块中还有一类函数，能替代从序列中取出元素或读取对象属性的 lambda 表达式：

因此，itemgetter 和 attrgetter 其实会自行构建函数。

示例 5-23 展示了 itemgetter 的常见用途：

根据元组的某个字段给元组列表排序。

在这个示例中，按照国家代码（第 2 个字段）的顺序打印各个城市的信息。

其实，itemgetter(1) 的作用与 lambda fields: fields[1] 一样：

创建一个接受集合的函数，返回索引位 1 上的元素。

示例 5-23　演示使用 itemgetter 排序一个元组列表（数据来自示例 2-8）
'''
from operator import itemgetter

metro_data = [
		('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
		('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
		('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
		('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
		('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
	]

for city in sorted(metro_data, key=itemgetter(1)):
	print(city)
'''
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
'''

# 如果把多个参数传给 itemgetter，它构建的函数会返回提取的值构成的元组：

cc_name = itemgetter(1, 0)
for city in metro_data:
	print(cc_name(city))
'''
('JP', 'Tokyo')
('IN', 'Delhi NCR')
('MX', 'Mexico City')
('US', 'New York-Newark')
('BR', 'Sao Paulo')
'''
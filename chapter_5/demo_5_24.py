'''
attrgetter 与 itemgetter 作用类似，它创建的函数根据名称提取对象的属性。

如果把多个属性名传给 attrgetter，它也会返回提取的值构成的元组。

此外，如果参数名中包含 .（点号） ，attrgetter 会深入嵌套对象，获取指定的属性。这些行为如示例 5-24 所示。

这个控制台会话不短，因为我们要构建一个嵌套结构，这样才能展示 attrgetter 如何处理包含点号的属性名。

示例 5-24　 定义一个 namedtuple，名为 metro_data（与示例 5-23 中的列表相同） ，演示使用 attrgetter 处理它
'''
import operator
from collections import namedtuple
from operator import attrgetter

metro_data = [
		('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
		('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
		('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
		('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
		('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
	]

# 使用 namedtuple 定义 LatLong
LatLong = namedtuple('LatLong', 'lat long')
# 再定义 Metropolis
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
# 使用 Metropolis 实例构建 metro_areas 列表；
# 注意，我们使用嵌套的元组拆包提取(lat, long)，然后使用它们构建 LatLong，作为 Metropolis 的 coord 属性
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]

print(metro_areas[0])
'''
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722, long=139.691667))
'''

# 深入 metro_areas[0]，获取它的纬度
print(metro_areas[0].coord.lat)

# 定义一个 attrgetter，获取 name 属性和嵌套的 coord.lat 属性
name_lat = attrgetter('name', 'coord.lat')
# 再次使用 attrgetter，按照纬度排序城市列表
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
	# 使用标号➎中定义的attrgetter，只显示城市名和纬度
	print(name_lat(city))

'''
下面是 operator 模块中定义的部分函数（省略了以 _ 开头的名称，因为它们基本上是实现细节）
'''
names = [name for name in dir(operator) if not name.startswith('_')]
for i, name in enumerate(names, start=1):
	print(name)
	if i % 5 == 0:
		print('\n')
		
'''
这 52 个名称中大部分的作用不言而喻。

以 i 开头、后面是另一个运算符的那些名称（如iadd、iand 等） ，对应的是增量赋值运算符（如 +=、&= 等） 。

如果第一个参数是可变的，那么这些运算符函数会就地修改它；否则，作用与不带 i 的函数一样，直接返回运算结果
'''

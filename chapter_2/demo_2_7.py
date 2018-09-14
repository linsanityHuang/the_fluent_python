# 元组其实是对数据的记录：
# 元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置。
# 正是这个位置信息给数据赋予了意义。

# 如果在任何的表达式里我们在元组内对元素排序，这些元素所携带的信息就会丢失，因为这些信息是跟它们的位置有关的。

# 把元组用作记录

# 洛杉矶国际机场的经纬度
lax_coordinates = (33.9425, -118.408056)
# 东京市的一些信息：市名、年份、人口（单位：百万） 、人口变化（单位：百分比）和面积（单位：平方千米）
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# 一个元组列表，元组的形式为 (country_code, passport_number)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# 在迭代的过程中，passport 变量被绑定到每个元组上
for passport in sorted(traveler_ids):
    # % 格式运算符能被匹配到对应的元组元素上
    print('%s/%s' % passport)

# for 循环可以分别提取元组里的元素，也叫作拆包（unpacking）
# 因为元组中第二个元素对我们没有什么用，所以它赋值给“_”占位符
for coutry, _ in traveler_ids:
    print(coutry)
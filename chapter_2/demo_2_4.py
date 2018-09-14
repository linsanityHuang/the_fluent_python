# 使用列表推导计算笛卡儿积
# 如果你需要一个列表，列表里是 3 种不同尺寸的 T 恤衫，
# 每个尺寸都有 2 个颜色，示例2-4 用列表推导算出了这个列表，列表里有 6 种组合。
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)
# 相当于
tshirts = []
for color in colors:
    for size in sizes:
        tshirts.append((color, size))
print(tshirts)
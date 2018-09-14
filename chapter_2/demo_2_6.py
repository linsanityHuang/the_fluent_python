# 使用生成器表达式计算笛卡儿积

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# 生成器表达式逐个产出元素，从来不会一次性产出一个含有 6 个 T 恤样式的列表
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
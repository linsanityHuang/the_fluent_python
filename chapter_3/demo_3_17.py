# 将同样的数据以不同的顺序添加到 3 个字典里

# 世界人口数量前10位国家的电话区号 
DIAL_CODES = [
                (86, 'China'),
                (91, 'India'),
                (1, 'United States'),
                (62, 'Indonesia'),
                (55, 'Brazil'),
                (92, 'Pakistan'),
                (880, 'Bangladesh'),
                (234, 'Nigeria'),
                (7, 'Russia'),
                (81, 'Japan'),
            ]  

# 创建 d1 的时候，数据元组的顺序是按照国家的人口排名来决定的
d1 = dict(DIAL_CODES)
print('d1:', d1.keys())
# 创建 d2 的时候，数据元组的顺序是按照国家的电话区号来决定的
d2 = dict(sorted(DIAL_CODES))
print('d2:', d2.keys())
# 创建 d3 的时候，数据元组的顺序是按照国家名字的英文拼写来决定的
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3:', d3.keys())
# 这些字典是相等的，因为它们所包含的数据是一样的
assert d1 == d2 and d2 == d3
# 字典推导（dictcomp）可以从任何以键值对作为元素的可迭代对象中构建出字典。
# 示例 3-1 就展示了利用字典推导可以把一个装满元组的列表变成两个不同的字典。

# 一个承载成对数据的列表，它可以直接用在字典的构造方法中。
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

# 这里把配好对的数据左右换了下，国家名是键，区域码是值。
country_code = {country: code for code, country in DIAL_CODES}

print(country_code)

# 跟上面相反，用区域码作为键，国家名称转换为大写，并且过滤掉区域码大于或等于66 的地区。
country_code = {code: country.upper() for country, code in country_code.items() if code < 66}

print(country_code)
# 新建一个 Latin-1 字符集合，该集合里的每个字符的 Unicode 名字里都有“SIGN”这个单词

# 从 unicodedata 模块里导入 name 函数，用以获取字符的名字
from unicodedata import name
# 把编码在 32~255 之间的字符的名字里有“SIGN”单词的挑出来，放到一个集合里
s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(s)
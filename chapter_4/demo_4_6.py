'''
多数非 UTF 编解码器只能处理 Unicode 字符的一小部分子集。

把文本转换成字节序列时，如果目标编码中没有定义某个字符，
那就会抛出 UnicodeEncodeError 异常，除非把 errors 参数传给编码方法或函数，对错误进行特殊处理。

处理错误的方式如示例 4-6 所示
'''

# 编码成字节序列：成功和错误处理
city = 'São Paulo'
print(city.encode('utf_8'))                             # 'utf_?' 编码能处理任何字符串
print(city.encode('utf_16'))    

print(city.encode('iso8859_1'))                         # 'iso8859_1' 编码也能处理字符串 'São Paulo'

# print(city.encode('cp437'))                           # 'cp437' 无法编码 'ã'（带波形符的“a” ） 。默认的错误处理方式 'strict' 抛出 Unicode- EncodeError
print(city.encode('cp437', errors='ignore'))            # error='ignore' 处理方式悄无声息地跳过无法编码的字符；这样做通常很是不妥
print(city.encode('cp437', errors='replace'))           # 编码时指定 error='replace'，把无法编码的字符替换成 '?'；数据损坏了，但是用户知道出了问题。
print(city.encode('cp437', errors='xmlcharrefreplace')) # 'xmlcharrefreplace' 把无法编码的字符替换成 XML 实体
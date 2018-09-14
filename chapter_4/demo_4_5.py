'''
Python 自带了超过 100 种编解码器（codec, encoder/decoder） ，用于在文本和字节之间相互转换。
每个编解码器都有一个名称，如 'utf_8'，而且经常有几个别名，如 'utf8'、'utf- 8' 和 'U8'。
这些名称可以传给 open()、str.encode()、bytes.decode() 等函数的 encoding 参数。

示例 4-5 使用 3 个编解码器把相同的文本编码成不同的字节序列
'''

# 使用 3 个编解码器编码字符串“El Niño” ，得到的字节序列差异很大
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

'''
latin_1 b'El Ni\xf1o'
utf_8   b'El Ni\xc3\xb1o'
utf_16  b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'
'''
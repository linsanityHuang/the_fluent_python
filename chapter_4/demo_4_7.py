'''
不是每一个字节都包含有效的 ASCII 字符，
也不是每一个字符序列都是有效的 UTF-8 或UTF-16。
因此，把二进制序列转换成文本时，如果假设是这两个编码中的一个，
遇到无法转换的字节序列时会抛出 UnicodeDecodeError。

另一方面，很多陈旧的 8 位编码——如 'cp1252'、'iso8859_1' 和 'koi8_r'——能解码任何字节序列流而不抛出错误，例如随机噪声。
因此，如果程序使用错误的 8 位编码，解码过程悄无声息，而得到的是无用输出。
'''
# 示例 4-7 演示了使用错误的编解码器可能出现鬼符或抛出 UnicodeDecodeError

octets = b'Montr\xe9al'             # 这些字节序列是使用 latin1 编码的“Montréal” ；'\xe9' 字节对应“é”

print(octets.decode('cp1252'))      # 可以使用 'cp1252'（Windows 1252）解码，因为它是 latin1 的有效超集

print(octets.decode('iso8859_7'))   # ISO-8859-7 用于编码希腊文，因此无法正确解释 '\xe9' 字节，而且没有抛出错误

print(octets.decode('koi8_r'))      # KOI8-R 用于编码俄文；这里，'\xe9' 表示西里尔字母“И”

# print(octets.decode('utf_8'))       # 'utf_8' 编解码器检测到 octets 不是有效的 UTF-8 字符串，抛出 UnicodeDecodeError

print(octets.decode('utf_8', errors='replace')) # 使用 'replace' 错误处理方式，\xe9 替换成了“�” （码位是 U+FFFD） ，这是官方指定的 REPLACEMENT CHARACTER（替换字符） ，表示未知字符
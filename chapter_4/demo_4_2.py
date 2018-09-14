# 包含 5 个字节的 bytes 和 bytearray 对象

cafe = bytes('café', encoding='utf_8')      # bytes 对象可以从 str 对象使用给定的编码构建
print(cafe)
# b'caf\xc3\xa9'

print(cafe[0])                              # 各个元素是 range(256) 内的整数
# 99
print(cafe[:1])                             # bytes 对象的切片还是 bytes 对象，即使是只有一个字节的切片
# b'c'
cafe_arr = bytearray(cafe)                  # bytearray 对象没有字面量句法，而是以 bytearray() 和字节序列字面量参数的形式显示

print(cafe_arr)
# bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:])                        # bytearray 对象的切片还是 bytearray 对象
# bytearray(b'\xa9')
'''
有几个设置对 Python I/O 的编码默认值有影响，如示例 4-11 中的 default_encodings.py 脚本所示。
'''
# 探索编码默认值
import sys, locale

expressions = """
        locale.getpreferredencoding()       # locale.getpreferredencoding() 是最重要的设置
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

# mac平台输出
'''
 locale.getpreferredencoding() -> 'UTF-8'
                 type(my_file) -> <class '_io.TextIOWrapper'>
              my_file.encoding -> 'UTF-8'
           sys.stdout.isatty() -> True
           sys.stdout.encoding -> 'UTF-8'
            sys.stdin.isatty() -> True
            sys.stdin.encoding -> 'UTF-8'
           sys.stderr.isatty() -> True
           sys.stderr.encoding -> 'UTF-8'
      sys.getdefaultencoding() -> 'utf-8'
   sys.getfilesystemencoding() -> 'utf-8'
'''

# Windows平台输出
'''
 locale.getpreferredencoding() -> 'cp936'                       # locale.getpreferredencoding() 是最重要的设置
                 type(my_file) -> <class '_io.TextIOWrapper'>
              my_file.encoding -> 'cp936'                       # 文本文件默认使用 locale.getpreferredencoding()
           sys.stdout.isatty() -> True
           sys.stdout.encoding -> 'utf-8'
            sys.stdin.isatty() -> True                          # 输出到控制台中，因此 sys.stdout.isatty() 返回 True
            sys.stdin.encoding -> 'utf-8'                       # 因此，sys.stdout.encoding 与控制台的编码相同。
           sys.stderr.isatty() -> True
           sys.stderr.encoding -> 'utf-8'
      sys.getdefaultencoding() -> 'utf-8'
   sys.getfilesystemencoding() -> 'utf-8'
'''
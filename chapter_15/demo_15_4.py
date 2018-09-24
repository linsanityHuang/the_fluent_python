'''
解释器调用 __enter__ 方法时，除了隐式的 self 之外，不会传入任何参数。

传给 __exit__ 方法的三个参数列举如下。
	exc_type 异常类（例如 ZeroDivisionError） 。
	
	exc_value 异常实例。有时会有参数传给异常构造方法，例如错误消息，这些参数可以使用 exc_ value.args 获取。
	
	traceback traceback 对象。
	
上下文管理器的具体工作方式参见示例 15-4。

在这个示例中，我们在 with 块之外使用LookingGlass 类，因此可以手动调用 __enter__ 和 __exit__ 方法。

示例 15-4　在 with 块之外使用 LookingGlass 类
'''

from chapter_15.mirror import LookingGlass

# 实例化并审查 manager 实例
manager = LookingGlass()
print(manager)
'''<chapter_15.mirror.LookingGlass object at 0x107eb9518>'''

# 在上下文管理器上调用 __enter__() 方法，把结果存储在 monster 中
monster = manager.__enter__()
# monster 的值是字符串 'JABBERWOCKY'。打印出的 True 标识符是反向的，因为 stdout 的所有输出都经过 __enter__ 方法中打补丁的 write 方法处理
print(monster == 'JABBERWOCKY')
'''eurT'''

print(monster)
'''YKCOWREBBAJ'''

print(manager)
'''>8159be701x0 ta tcejbo ssalGgnikooL.rorrim.51_retpahc<'''
# 调用 manager.__exit__，还原成之前的 stdout.write
manager.__exit__(None, None, None)
print(monster)
'''JABBERWOCKY'''

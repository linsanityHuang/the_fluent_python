'''
with 语句的目的是简化 try/finally 模式。

这种模式用于保证一段代码运行完毕后执行某项操作，即便那段代码由于异常、return 语句或 sys.exit() 调用而中止，也会执行指定的操作。

finally 子句中的代码通常用于释放重要的资源，或者还原临时变更的状态。

上下文管理器协议包含 __enter__ 和 __exit__ 两个方法。

with 语句开始运行时，会在上下文管理器对象上调用 __enter__ 方法。

with 语句运行结束后，会在上下文管理器对象上调用 __exit__ 方法，以此扮演 finally 子句的角色。

最常见的例子是确保关闭文件对象。使用 with 语句关闭文件的详细说明参见示例 15-1。

示例 15-1　演示把文件对象当成上下文管理器使用
'''

# fp 绑定到打开的文件上，因为文件的 __enter__ 方法返回 self
with open('mirror.py', encoding='utf-8') as fp:
	# 从 fp 中读取一些数据
	src = fp.read(60)
	
print(len(src))
'''60'''
# fp 变量仍然可用
print(fp)
'''<_io.TextIOWrapper name='mirror.py' mode='r' encoding='utf-8'>'''
# 可以读取 fp 对象的属性
print(fp.closed, fp.encoding)
'''True utf-8'''
# 但是不能在 fp 上执行 I/O 操作，因为在 with 块的末尾，调用 TextIOWrapper.__exit__ 方法把文件关闭了
# fp.read(60)

'''
装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。

这通常是在导入时（即 Python 加载模块时） ，

如示例 7-2 中的 demo_7_2.py 模块所示。
'''
# registry 保存被 @register 装饰的函数引用
registry = []


# register 的参数是一个函数
def register(func):
	print('running register(%s)' % func)
	registry.append(func)
	return func


@register
def f1():
	print('running f1()')
	

@register
def f2():
	print('running f2()')
	
	
def f3():
	print('running f3()')


def main():
	print('running main()')
	print('registry ->', registry)
	f1()
	f2()
	f3()


if __name__ == '__main__':
	main()

'''
running register(<function f1 at 0x1081ad268>)
running register(<function f2 at 0x1095c99d8>)
running main()
registry -> [<function f1 at 0x1081ad268>, <function f2 at 0x1095c99d8>]
running f1()
running f2()
running f3()
'''

'''
注意，register 在模块中其他函数之前运行（两次） 。

调用 register 时，传给它的参数是被装饰的函数，例如 <function f1 at 0x100631bf8>。

加载模块后，registry 中有两个被装饰函数的引用：f1 和 f2。

这两个函数，以及 f3，只在 main 明确调用它们时才执行。

如果导入 demo_7_2.py 模块（不作为脚本运行） ，

输出如下：
>>> import registration
running register(<function f1 at 0x10063b1e0>)
running register(<function f2 at 0x10063b268>)

此时查看 registry 的值，得到的输出如下：
>>> registration.registry
[<function f1 at 0x10063b1e0>, <function f2 at 0x10063b268>]

示例 7-2 主要想强调，函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行。

这突出了 Python 程序员所说的导入时和运行时之间的区别
'''
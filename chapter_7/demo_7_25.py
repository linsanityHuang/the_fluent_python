'''
本节再次探讨 clock 装饰器，为它添加一个功能：让用户传入一个格式字符串，控制被装饰函数的输出。

参见示例 7-25。
'''

import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


# clock 是参数化装饰器工厂函数
def clock(fmt=DEFAULT_FMT):
	# decorate是真正的装饰器
	def decorate(func):
		# clocked包装被装饰的函数
		def clocked(*_args):
			t0 = time.time()
			# _result是被装饰的函数返回的真正结果
			_result = func(*_args)
			elapsed = time.time() - t0
			name = func.__name__
			# _args是clocked的参数，args是用于显示的字符串
			args = ', '.join(repr(arg) for arg in _args)
			# result是_result的字符串表示形式，用于显示
			result = repr(_result)
			# 这里使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量
			print(fmt.format(**locals()))
			# clocked 会取代被装饰的函数，因此它应该返回被装饰的函数返回的值。
			return _result
		# decorate 返回 clocked
		return clocked
	# clock 返回 decorate
	return decorate


if __name__ == '__main__':
	
	# 在这个模块中测试，不传入参数调用 clock()，因此应用的装饰器使用默认的格式 str
	@clock()
	def snooze(seconds):
		time.sleep(seconds)
	
	@clock('{name}: {elapsed}s')
	def snooze(seconds):
		time.sleep(seconds)
	
	@clock('{name}({args}) dt={elapsed:0.3f}s')
	def snooze(seconds):
		time.sleep(seconds)

	for i in range(3):
		snooze(.123)

'''
functools.lru_cache 是非常实用的装饰器，它实现了备忘（memoization）功能。

这是一项优化技术，它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。

LRU 三个字母是“Least Recently Used”的缩写，表明缓存不会无限制增长，一段时间不用的缓存条目会被扔掉。

生成第 n 个斐波纳契数这种慢速递归函数适合使用 lru_cache，如示例 7-18 所示。

示例 7-18　生成第 n 个斐波纳契数，递归方式非常耗时
'''

from chapter_7.demo_7_17 import clock


@clock
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)


'''
浪费时间的地方很明显：fibonacci(1) 调用了 8 次，fibonacci(2) 调用了 5 次……

但是，如果增加两行代码，使用 lru_cache，性能会显著改善，如示例 7-19 所示。
'''

# 示例 7-19　使用缓存实现，速度更快
import functools


# 注意，必须像常规函数那样调用 lru_cache。
# 这一行中有一对括号：@functools.lru_ cache()。
# 这么做的原因是，lru_cache 可以接受配置参数，稍后说明
@functools.lru_cache()
# 这里叠放了装饰器：@lru_cache() 应用到 @clock 返回的函数上
@clock
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
	print(fibonacci(6))

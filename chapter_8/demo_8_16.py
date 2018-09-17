'''
示例 8-16　没有指向对象的引用时，监视对象生命结束时的情形
示例 8-16 的目的是明确指出 del 不会删除对象，但是执行 del 操作后可能会导致对象不可获取，从而被删除。
'''

import weakref


s1 = {1, 2, 3}
# s1 和 s2 是别名，指向同一个集合，{1, 2, 3}。
s2 = s1


# 这个函数一定不能是要销毁的对象的绑定方法，否则会有一个指向对象的引用
def bye():
	print('Gone with the wind...')
	

# 在 s1 引用的对象上注册 bye 回调。
ender = weakref.finalize(s1, bye)
# 调用 finalize 对象之前，.alive 属性的值为 True
print(ender.alive)
del s1
# 如前所述，del 不删除对象，而是删除对象的引用
print(ender.alive)
# 重新绑定最后一个引用 s2，让 {1, 2, 3} 无法获取。对象被销毁了，调用了 bye 回调，ender.alive 的值变成了 False。
s2 = 'spam'
print(ender.alive)

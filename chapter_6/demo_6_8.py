from chapter_6 import promotions
import inspect
'''
收集所有可用促销的另一种方法是，在一个单独的模块中保存所有策略函数，把 best_ promo 排除在外。

在示例 6-8 中，最大的变化是内省名为 promotions 的独立模块，构建策略函数列表。

注意，示例 6-8 要导入 promotions 模块，以及提供高阶内省函数的 inspect 模块（简单起见，这里没有给出导入语句，因为导入语句一般放在文件顶部） 。

示例 6-8　内省单独的 promotions 模块，构建 promos 列表
'''

'''
inspect.getmembers 函数用于获取对象（这里是 promotions 模块）的属性，

第二个参数是可选的判断条件（一个布尔值函数） 。

我们使用的是 inspect.isfunction，只获取模块中的函数。
'''
promos = [func for name, func in
		  inspect.getmembers(promotions, inspect.isfunction)]

def best_promo(order):
	"""选择可用的最佳折扣"""
	return max(promo(order) for promo in promos)

if __name__ == '__main__':
	print(promos)
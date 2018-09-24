from concurrent import futures
from chapter_17.demo_17_2 import save_flag, get_flag, show, main

'''
concurrent.futures 模块的主要特色是 ThreadPoolExecutor 和 ProcessPoolExecutor 类，

这两个类实现的接口能分别在不同的线程或进程中执行可调用的对象。

这两个类在内部维护着一个工作线程或进程池，以及要执行的任务队列。

不过，这个接口抽象的层级很高，像下载国旗这种简单的案例，无需关心任何实现细节。

示例 17-3 展示如何使用 ThreadPoolExecutor.map 方法，以最简单的方式实现并发下载。
示例 17-3　flags_threadpool.py：使用 futures.ThreadPoolExecutor 类实现多线程下载的脚本
'''
# 设定 ThreadPoolExecutor 类最多使用几个线程
MAX_WORKERS = 20


# 下载一个图像的函数；这是在各个线程中执行的函数
def download_one(cc):
	image = get_flag(cc)
	show(cc)
	save_flag(image, cc.lower() + '.gif')
	return cc


def download_many(cc_list):
	# 设定工作的线程数量：使用允许的最大值（MAX_WORKERS）与要处理的数量之间较小的那个值，以免创建多余的线程
	workers = min(MAX_WORKERS, len(cc_list))
	# 使 用 工 作 的 线 程 数 实 例 化 ThreadPoolExecutor 类；
	# executor.__exit__ 方 法 会 调 用executor.shutdown(wait=True) 方法，它会在所有线程都执行完毕前阻塞线程
	with futures.ThreadPoolExecutor(workers) as executor:
		# map 方法的作用与内置的 map 函数类似，不过 download_one 函数会在多个线程中并发调用；
		# map 方法返回一个生成器，因此可以迭代，获取各个函数返回的值
		res = executor.map(download_one, sorted(cc_list))
	# 返回获取的结果数量；如果有线程抛出异常，异常会在这里抛出，这与隐式调用 next() 函数从迭代器中获取相应的返回值一样
	return len(list(res))


def download_many(cc_list):
	# 这次演示只使用人口最多的 5 个国家
	cc_list = cc_list[:5]
	# 把 max_workers 硬编码为 3，以便在输出中观察待完成的期物
	with futures.ThreadPoolExecutor(max_workers=3) as executor:
		to_do = []
		# 按照字母表顺序迭代国家代码，明确表明输出的顺序与输入一致
		for cc in sorted(cc_list):
			# executor.submit 方法排定可调用对象的执行时间，然后返回一个期物，表示这个待执行的操作
			future = executor.submit(download_one, cc)
			# 存储各个期物，后面传给 as_completed 函数
			to_do.append(future)
			msg = 'Scheduled for {}: {}'
			# 显示一个消息，包含国家代码和对应的期物
			print(msg.format(cc, future))
		results = []
		# as_completed 函数在期物运行结束后产出期物
		for future in futures.as_completed(to_do):
			# 获取该期物的结果
			res = future.result()
			msg = '{} result: {!r}'
			# 显示期物及其结果
			print(msg.format(future, res))
			results.append(res)
		return len(results)


if __name__ == '__main__':
	main(download_many)

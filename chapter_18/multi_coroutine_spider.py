import time
import requests
from multiprocessing.dummy import Pool as ThreadPool

total = 100
thread = 4


async def request(loop):
	url = 'http://127.0.0.1:5000'
	future = loop.run_in_executor(None, requests.get, url)
	response = await future
	
	
def divide(i):
	import asyncio
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	tasks = [asyncio.ensure_future(request(loop)) for i in range(total//thread)]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
	
	
if __name__ == '__main__':
	time0 = time.time()
	pool = ThreadPool(thread)
	i = [j for j in range(0, thread)]
	pool.map(divide, i)
	pool.close()
	pool.join()
	time1 = time.time()
	print('爬取%d个网页，总花费时间: %.3f' % (total, time1 - time0), end='')
	'''爬取100个网页，总花费时间: 3.302'''

import time
import requests
import asyncio

total = 100


async def request():
	url = 'http://127.0.0.1:5000'
	future = loop.run_in_executor(None, requests.get, url)
	response = await future
	

if __name__ == '__main__':
	time0 = time.time()
	tasks = [asyncio.ensure_future(request()) for i in range(total)]
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
	time1 = time.time()
	print('爬取%d个网页，总花费时间: %.3f' % (total, time1 - time0), end='')
	'''爬取100个网页，总花费时间: 9.110'''

import time
import requests

total = 100
'''
本地的flask应用，在返回网页前等待3秒模拟真实网络爬虫
'''


def request():
	url = 'http://127.0.0.1:5000'
	r = requests.get(url, timeout=10)
	print(r.content)


if __name__ == '__main__':
	time0 = time.time()
	for i in range(0, total):
		request()
	time1 = time.time()
	print('爬取%d个网页，总花费时间: %.3f' % (total, time1-time0), end='')
	'''爬取100个网页，总花费时间: 300.802'''

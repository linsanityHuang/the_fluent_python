import asyncio
import aiohttp


async def run(url):
	print('start spider', url)
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as resp:
			print(resp.url)
			
			
url_list = ["https://www.baidu.com", "https://www.sogo.com", "https://www.bing.com", "https://www.liaoxuefeng.com/"]

tasks = [asyncio.ensure_future(run(url)) for url in url_list]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

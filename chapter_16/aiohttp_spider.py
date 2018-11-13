import aiohttp
import asyncio
import requests
import time

URL = 'https://morvanzhou.github.io/'


def normal():
	for i in range(3):
		r = requests.get(URL)
		url = r.url
		print(url)


t1 = time.time()
normal()
print("Normal total time:", time.time()-t1)


async def job(session):
	response = await session.get(URL)
	return str(response.url)


async def main(loop):
	async with aiohttp.ClientSession() as session:
		tasks = [loop.create_task(job(session)) for _ in range(3)]
		finished, unfinished = await asyncio.wait(tasks)
		all_results = [r.result() for r in finished]
		print(all_results)
		

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Async total time:", time.time() - t1)

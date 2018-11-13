import time
import asyncio


def job(t):
	print('Start job ', t)
	time.sleep(t)
	print('Job ', t, 'takes ', t, ' s')
	
	
async def async_job(t):
	print('Start job ', t)
	await asyncio.sleep(t)
	print('Job ', t, 'takes ', t, ' s')
	
	
async def async_main(loop):
	tasks = [
		loop.create_task(async_job(t)) for t in range(1, 4)
	]
	await asyncio.wait(tasks)


def main():
	[job(t) for t in range(1, 4)]
	

t1 = time.time()
main()
print("NO async total time : ", time.time() - t1)


t2 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(async_main(loop))
loop.close()
print("Async total time : ", time.time() - t2)

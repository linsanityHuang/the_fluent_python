import asyncio

async def test1():
	print(1)
	await test2()
	print(2)
	return 'stop'
	
async def test2():
	print(3)
	print(4)
	
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(test1())
loop.run_until_complete(task)
print(task.result())

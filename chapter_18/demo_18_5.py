import os
import sys
import time
import asyncio
import aiohttp

POP20_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads/'


def save_flag(img, filename):
	path = os.path.join(DEST_DIR, filename)
	with open(path, 'wb') as fp:
		fp.write(img)


def show(text):
	print(text, end=' ')
	sys.stdout.flush()


def main(download_many):
	t0 = time.time()
	count = download_many(POP20_CC)
	elapsed = time.time() - t0
	msg = '\n{} flags downloaded in {:.2f}s'
	print(msg.format(count, elapsed))


async def get_flag(cc):
	url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
	resp = await aiohttp.request('GET', url)
	image = await resp.read()
	return image


async def download_one(cc):
	image = await get_flag(cc)
	show(cc)
	save_flag(image, cc.lower() + '.gif')
	return cc


def download_many(cc_list):
	loop = asyncio.get_event_loop()
	to_do = [download_one(cc) for cc in sorted(cc_list)]
	wait_coro = asyncio.wait(to_do)
	res, _ = loop.run_until_complete(wait_coro)
	loop.close()
	return len(res)


if __name__ == '__main__':
	main(download_many)



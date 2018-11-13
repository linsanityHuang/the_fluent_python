import time
from concurrent.futures import ProcessPoolExecutor, as_completed


NUMBERS = range(25, 38)


def fib(n):
	if n <= 2:
		return 1
	return fib(n-1) + fib(n-2)


start = time.time()

with ProcessPoolExecutor(8) as executor:
	for num, result in zip(NUMBERS, executor.map(fib, NUMBERS)):
		print('fib({}) = {}'.format(num, result))


print('COST: {}'.format(time.time() - start))

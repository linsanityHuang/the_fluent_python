import threading
import itertools
import time
import sys

'''
示例 18-1　spinner_thread.py：通过线程以动画形式显示文本式旋转指针
'''


# 这个类定义一个简单的可变对象；其中有个 go 属性，用于从外部控制线程
class Signal:
	go = True
	

# 这个函数会在单独的线程中运行。signal 参数是前面定义的 Signal 类的实例
def spin(msg, signal):
	write, flush = sys.stdout.write, sys.stdout.flush
	# 这其实是个无限循环，因为 itertools.cycle 函数会从指定的序列中反复不断地生成元素
	for char in itertools.cycle('|/-\\'):
		status = char + ' ' + msg
		write(status)
		flush()
		# 这是显示文本式动画的诀窍所在：使用退格符（\x08）把光标移回来
		write('\x08' * len(status))
		time.sleep(.1)
		# 如果 go 属性的值不是 True 了，那就退出循环
		if not signal.go:
			break
	# 使用空格清除状态消息，把光标移回开头。
	write(' ' * len(status) + '\x08' * len(status))


# 假设这是耗时的计算
def slow_function():
	# 假装等待I/O一段时间
	# 调用 sleep 函数会阻塞主线程，不过一定要这么做，以便释放 GIL，创建从属线程
	time.sleep(10)
	return 42
	

# 这个函数设置从属线程，显示线程对象，运行耗时的计算，最后杀死线程
def supervisor():
	signal = Signal()
	spinner = threading.Thread(target=spin, args=('thinking!', signal))
	# 显示从属线程对象。输出类似于 <Thread(Thread-1, initial)>
	print('spinner object:', spinner)
	# 启动从属线程。
	spinner.start()
	# 运行 slow_function 函数，阻塞主线程。同时，从属线程以动画形式显示旋转指针
	result = slow_function()
	# 改变 signal 的状态；这会终止 spin 函数中的那个 for 循环
	signal.go = False
	# 等待 spinner 线程结束
	spinner.join()
	return result


def main():
	# 运行 supervisor 函数
	result = supervisor()
	print('Answer:', result)


if __name__ == '__main__':
	main()

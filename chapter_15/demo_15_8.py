import csv
import fileinput
'''
除了标准库中举的例子之外，

Martijn Pieters 实现的原地文件重写上下文管理器
http://www.zopatista.com/python/2013/11/26/inplace-file-rewriting/

是 @contextmanager 不 错 的 使用实例。用法如示例 15-8 所示。

示例 15-8　用于原地重写文件的上下文管理器
'''

with inplace(csvfilename, 'r', newline='') as (infh, outfh):
	reader = csv.reader(infh)
	writer = csv.writer(outfh)
	for row in reader:
		row += ['new', 'columns']
		writer.writerow(row)

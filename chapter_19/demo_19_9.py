'''
示例 19-9　schedule1.py：访问保存在 shelve.Shelf 对象里的 OSCON 日程数据
'''
import shelve
import warnings
from chapter_19.demo_19_2 import load

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:
	def __init__(self, **kwargs):
		# 这是使用关键字参数传入的属性构建实例的常用简便方式
		self.__dict__.update(kwargs)


def load_db(db):
	raw_data = load()
	warnings.warn('loading ' + DB_NAME)
	# 迭代集合（例如 'conferences'、'events'，等等）
	for collection, rec_list in raw_data['Schedule'].items():
		# record_type 的值是去掉尾部 's' 后的集合名（即把 'events' 变成 'event'）
		record_type = collection[:-1]
		for record in rec_list:
			# 使用 record_type 和 'serial' 字段构成 key
			key = '{}.{}'.format(record_type, record['serial'])
			# 把 'serial' 字段的值设为完整的键
			record['serial'] = key
			# 构建 Record 实例，存储在数据库中的 key 键名下
			db[key] = Record(**record)
			
			
if __name__ == '__main__':
	# shelve.open 函数打开现有的数据库文件，或者新建一个
	db = shelve.open(DB_NAME)
	# 判断数据库是否填充的简便方法是，检查某个已知的键是否存在；
	# 这里检查的键是conference.115，即 conference 记录（只有一个）的键
	if CONFERENCE not in db:
		# 如果数据库是空的，那就调用 load_db(db)，加载数据
		load_db(db)
	# 获取一条 speaker 记录
	speaker = db['speaker.3471']
	# 它是示例 19-9 中定义的 Record 类的实例
	print(type(speaker))
	# 各个 Record 实例都有一系列自定义的属性，对应于底层 JSON 记录里的字段
	print(speaker.name)
	print(speaker.twitter)
	# 一定要记得关闭 shelve.Shelf 对象。如果可以，使用 with 块确保 Shelf 对象会关闭。
	db.close()

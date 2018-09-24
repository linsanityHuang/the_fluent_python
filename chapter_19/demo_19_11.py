import warnings
# inspect 模块在 load_db 函数中使用
import inspect
import shelve

from chapter_19.demo_19_2 import load

# 因为要存储几个不同类的实例，所以我们要创建并使用不同的数据库文件；
# 这里不用示例 19-9 中的 'schedule1_db'，而是使用 'schedule2_db'
DB_NAME = 'data/schedule2_db'
CONFERENCE = 'conference.115'


class Record:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		
	# __eq__ 方法对测试有重大帮助
	def __eq__(self, other):
		if isinstance(other, Record):
			return self.__dict__ == other.__dict__
		else:
			return NotImplemented
		

# 自定义的异常通常是标志类，没有定义体。写一个文档字符串，说明异常的用途，比只写一个 pass 语句要好
class MissingDatabaseError(RuntimeError):
	"""需要数据库但没有指定数据库时抛出。 """
	

# DbRecord 类扩展 Record 类
class DbRecord(Record):
	# __db 类属性存储一个打开的 shelve.Shelf 数据库引用
	__db = None
	
	# set_db 是静态方法，以此强调不管调用多少次，效果始终一样
	@staticmethod
	def set_db(db):
		# 即使调用 Event.set_db(my_db)，__db 属性仍在 DbRecord 类中设置
		DbRecord.__db = db
		
	# get_db 也是静态方法，因为不管怎样调用，返回值始终是 DbRecord.__db 引用的对象
	@staticmethod
	def get_db():
		return DbRecord.__db
	
	# fetch 是类方法，因此在子类中易于定制它的行为
	@classmethod
	def fetch(cls, ident):
		db = cls.get_db()
		try:
			# 从数据库中获取 ident 键对应的记录
			return db[ident]
		except TypeError:
			# 如果捕获到 TypeError 异常，而且 db 变量的值是 None，抛出自定义的异常，说明必须设置数据库
			if db is None:
				msg = "database not set; call '{}.set_db(my_db)'"
				raise MissingDatabaseError(msg.format(cls.__name__))
			else:
				# 否则，重新抛出 TypeError 异常，因为我们不知道怎么处理
				raise
			
	def __repr__(self):
		# 如果记录有 serial 属性，在字符串表示形式中使用
		if hasattr(self, 'serial'):
			cls_name = self.__class__.__name__
			return '<{} serial={!r}>'.format(cls_name, self.serial)
		else:
			# 否则，调用继承的 __repr__ 方法
			return super().__repr__()


# Event 类扩展 DbRecord 类
class Event(DbRecord):
	@property
	def venue(self):
		key = 'venue.{}'.format(self.venue_serial)
		# 在 venue 特性中使用 venue_serial 属性构建 key，然后传给继承自 DbRecord 类的 fetch 类方法（详情参见下文）
		return self.__class__.fetch(key)
	
	@property
	def speakers(self):
		# speakers 特性检查记录是否有 _speaker_objs 属性
		if not hasattr(self, '_speaker_objs'):
			# 如果没有，直接从 __dict__ 实例属性中获取 'speakers' 属性的值，防止无限递归，因为这个特性的公开名称也是 speakers
			spkr_serials = self.__dict__['speakers']
			# 获取 fetch 类方法的引用（稍后会说明这么做的原因）
			fetch = self.__class__.fetch
			# 使用 fetch 获取 speaker 记录列表，然后赋值给 self._speaker_objs
			self._speaker_objs = [fetch('speaker.{}'.format(key)) for key in spkr_serials]
		# 返回前面获取的列表
		return self._speaker_objs
	
	def __repr__(self):
		# 如果记录有 name 属性，在字符串表示形式中使用
		if hasattr(self, 'name'):
			cls_name = self.__class__.__name__
			return '<{} {!r}>'.format(cls_name, self.name)
		else:
			# 否则，调用继承的 __repr__ 方法
			return super().__repr__()


def load_db(db):
	raw_data = load()
	warnings.warn('loading ' + DB_NAME)
	for collection, rec_list in raw_data['Schedule'].items():
		record_type = collection[:-1]
		# 把 record_type 变量的值首字母变成大写（例如，把 'event' 变成 'Event'） ，获取可能的类名
		cls_name = record_type.capitalize()
		# 从模块的全局作用域中获取那个名称对应的对象；如果找不到对象，使用 DbRecord
		cls = globals().get(cls_name, DbRecord)
		# 如果获取的对象是类，而且是 DbRecord 的子类……
		if inspect.isclass(cls) and issubclass(cls, DbRecord):
			# ……把对象赋值给 factory 变量。因此，factory 的值可能是 DbRecord 的任何一个子类，具体的类取决于 record_type 的值
			factory = cls
		else:
			# 否则，把 DbRecord 赋值给 factory 变量
			factory = DbRecord
		# 这个 for 循环创建 key，然后保存记录，这与之前一样，不过
		for record in rec_list:
			key = '{}.{}'.format(record_type, record['serial'])
			record['serial'] = key
			# ……存储在数据库中的对象由 factory 构建，factory 可能是 DbRecord 类，也可能是根据 record_type 的值确定的某个子类
			db[key] = factory(**record)
			
			
if __name__ == '__main__':
	db = shelve.open(DB_NAME)
	if CONFERENCE not in db:
		load_db(db)
	DbRecord.set_db(db)
	event = DbRecord.fetch('event.33950')
	print(event)
	print(event.venue)
	print(event.venue.name)
	for spkr in event.speakers:
		print('{0.serial}: {0.name}'.format(spkr))

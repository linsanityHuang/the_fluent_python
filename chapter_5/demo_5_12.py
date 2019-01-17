# coding=utf-8
'''
示例 5-12　Bobo 知道 hello 需要 person 参数，并且从 HTTP 请求中获取它
'''
# import bobo


# @bobo.query('/')
def hello(person):
	return 'Hello %s!' % person
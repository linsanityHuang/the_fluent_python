'''
下面重点说明函数专有而用户定义的一般对象没有的属性。

计算两个属性集合的差集便能得到函数专有属性列表（见示例 5-9） 。

示例 5-9　列出常规对象没有而函数有的属性
'''
class C:
    pass
def func():
    pass
def main():
    obj = C()
    attr = set(dir(func)) - set(dir(obj))
    print(sorted(attr))

    '''
    [
        '__annotations__',          dict                    参数和返回值的注解
        '__call__',                 method-wrapper          实现 () 运算符；即可调用对象协议
        '__closure__',              tuple                   函数闭包，即自由变量的绑定（通常是 None）
        '__code__',                 code                    编译成字节码的函数元数据和函数定义体
        '__defaults__',             tuple                   形式参数的默认值
        '__get__',                  method-wrapper          实现只读描述符协议
        '__globals__',              dict                    函数所在模块中的全局变量
        '__kwdefaults__',           dict                    仅限关键字形式参数的默认值
        '__name__',                 str                     函数名称
        '__qualname__']             str                     函数的限定名称， 如Random.choice
    '''

    
if __name__ == '__main__':
    main()
'''
示例 5-1 中的控制台会话表明，Python 函数是对象。
这里我们创建了一个函数，然后调用它，读取它的 __doc__ 属性，

并且确定函数对象本身是 function 类的实例
'''

# 创建并测试一个函数，然后读取它的 __doc__ 属性，再检查它的类型
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

def main():
    print(factorial(42))

    print(factorial.__doc__)

    print(type(factorial))


# 通过别的名称使用函数，再把函数作为参数传递

if __name__ == '__main__':
    fact = factorial
    print(fact)

    print(fact(5))

    print(map(factorial, range(11)))

    print(list(map(factorial, range(11))))
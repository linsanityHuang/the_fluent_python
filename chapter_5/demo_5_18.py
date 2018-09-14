'''
inspect.Signature 对象有个 bind 方法，它可以把任意个参数绑定到签名中的形参上，所用的规则与实参到形参的匹配方式一样。

框架可以使用这个方法在真正调用函数前验证参数，如示例 5-18 所示。
'''
# 示例 5-18　把 tag 函数（见示例 5-10）的签名绑定到一个参数字典上
import sys
sys.path.append('./')
import inspect
from demo_5_10 import tag
# 获取 tag 函数（见示例 5-10）的签名
sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
# 把一个字典参数传给 .bind() 方法
bound_args = sig.bind(**my_tag)
print(bound_args)
# <BoundArguments (name='img', cls='framed', attrs={'title': 'Sunset Boulevard', 'src': 'sunset.jpg'})>
# 得到一个 inspect.BoundArguments 对象

# 迭代 bound_args.arguments（一个 OrderedDict 对象）中的元素，显示参数的名称和值
for name, value in bound_args.arguments.items():
    print(name, '=', value)
'''
name = img
cls = framed
attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
'''
del my_tag['name']
# 把必须指定的参数 name 从 my_tag 中删除

bound_args = sig.bind(**my_tag)
# 调用 sig.bind(**my_tag)，抛出 TypeError，抱怨缺少 name 参数
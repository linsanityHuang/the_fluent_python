'''
例如，若想根据单词的长度排序，只需把 len 函数传给 key 参数，如示例 5-3 所示。
'''

# 示例 5-3 根据单词长度给一个列表排序

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
fruits_sorted = sorted(fruits, key=len)     # 任何单参数函数都能作为 key 参数的值。
print(fruits_sorted)


# 示例 5-4 根据反向拼写给一个单词列表排序
def reverse(word):
    return word[::-1]

fruits_sorted = sorted(fruits, key=reverse)
print(fruits_sorted)
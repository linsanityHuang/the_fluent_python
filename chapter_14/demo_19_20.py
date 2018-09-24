import itertools
'''
示例 14-20　组合学生成器函数会从输入的各个元素中产出多个值
'''
# 'ABC' 中每两个元素（len()==2）的各种组合；在生成的元组中，元素的顺序无关紧要（可以视作集合）
print(list(itertools.combinations('ABC', 2)))
'''[('A', 'B'), ('A', 'C'), ('B', 'C')]'''
# 'ABC' 中每两个元素（len()==2）的各种组合，包括相同元素的组合
print(list(itertools.combinations_with_replacement('ABC', 2)))
'''[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]'''
# 'ABC' 中每两个元素（len()==2）的各种排列；在生成的元组中，元素的顺序有重要意义
print(list(itertools.permutations('ABC', 2)))
'''[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]'''
# 'ABC' 和 'ABC'（repeat=2 的效果）的笛卡儿积
print(list(itertools.product('ABC', repeat=2)))
'''[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]'''

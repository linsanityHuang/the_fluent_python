# coding=utf-8
# bisect 可以用来建立一个用数字作为索引的查询表格， 比如说把分数和成绩8对应起来
# 根据一个分数，找到它所对应的成绩等级
# 成绩分5级，依次是F、D、C、B、A

# 首先给出一个成绩评定的序列，然后通过bisect函数找到要分等级的分数在这个评定序列应该出现的位置，然后返回等级表对应的等级
import bisect
# 首先可以用它的两个可选参数——lo 和 hi——来缩小搜寻的范围。lo 的默认值是 0，hi 的默认值是序列的长度，即 len() 作用于该序列的返回值
# 其次，bisect 函数其实是 bisect_right
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
	i = bisect.bisect(breakpoints, score)							# 用特定的bisect 函数来计算元素应该出现的位置。
	return grades[i]												# 返回成绩的等级

if __name__ == '__main__':
	print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
"""
    1. 一个长度为n-1的递增排序数组中的所有数字都是唯一的，
    并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个
    数字中有且只有一个数字不在该数组中，请找出这个数字。
    1 <= 数组长度 <= 10000

    示例:
    输入: [0,1,2,3,4,5,6,7,9]
    输出: 8
"""

import random

# 随机长度
num = random.randint(1, 10000)
# 生成数组
list_num = []
for i in range(num + 1):
    list_num.append(i)
# 随机删除一个数
num1 = random.randint(1, num)
print(list_num)
print(num1)
list_num.remove(num1)
print(list_num)
# 起始0 当判断到不相等时表示被删除
start = 0
for i in range(len(list_num)):
    if start != i:
        print(i)
        break
    start += 1

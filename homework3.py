"""
1. 给你一个长度为n的数组，其中只有一个数字出现大于n/2次，问如何快速找到这个数字（20分）
"""


list_num = [1, 2, 5, 6, 1, 5, 4, 8, 7, 59, 5, 4, 6, 4, 2, 1, 4, 5, 6, 4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
list_num.sort()
print(list_num)
print(list_num[len(list_num)//2])
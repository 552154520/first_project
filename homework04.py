"""
2、假设给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
最小的 24 小时制时间是 00:00，而最大的是 23:59。
从 00:00 （午夜）开始算起，过得越久，时间越大。
以长度为 5 的字符串返回。(30分)
示例
输入：[1,2,3,4]
输出："23:41"

"""
import random

list_num = [3, 1, 8, 4]
list_num.sort()
list_h = []
list_m = []

x, y = random.sample(list_num, 2)

max = [0, 0]
for h in range(24):
    for m in range(60):
        list_result = []
        list_result.append(h // 10)
        list_result.append(h % 10)
        list_result.append(m // 10)
        list_result.append(m % 10)
        list_result.sort()
        if list_result == list_num:
            max[0] = h
            max[1] = m

print(f"{max[0]}:{max[1]}")

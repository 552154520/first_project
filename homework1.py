"""
    编程题（30分）
        1. 小明家必须要过一座桥。
            小明过桥最快要１秒，
            小明的弟弟最快要３秒，
            小明的爸爸最快要６秒，
            小明的妈妈最快要８秒，
            小明的爷爷最快要１２秒。
        每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。
        过桥时候是黑夜，所以必须有手电筒，
        小明家只有一个手电筒，而且手电筒的电池只剩30秒就将耗尽。
        小明一家该如何过桥，请写出详细过程。

        由小明拿手电筒
        时间为  3 + 1            4
                6 + 1           7
                12(8) + 3       15
                3               3

                29秒
"""
lift_home = {
    "小明": 1,
    "小明弟弟": 3,
    "妈妈": 6,
    "爸爸": 8,
    "爷爷": 12
}
right_home = {}
part = [""]
list_no = [0, 1, 2, 3, 4]
count = 0
# 五次次过桥
# for r in range(len(lift_home) - 1):
#     # 选出第一个第一次过桥的人
#     left = [0, 1, 2, 3, 4]
#     right = []
#     for i in left:
#         left.remove(i)
#         part[count] += str(i)
#         right.append(i)
#         for no1 in left:
#             # 选出第二个第一次过桥的人
#             left.remove(no1)
#             part[count] += (str(i) + "-")
#             right.append(no1)
#             # 选出回来的人
#             if left == []:
#                 count += 1
#                 break
#             for back in right:
#                 right.remove(back)
#                 part[count] += (str(back) + "-")
#                 left.append(back)
#             # 下一趟第一个人
#             for no2 in left:
#                 left.remove(no2)
#                 part[count] += str(no2)
#                 right.append(no2)
# print(part)
















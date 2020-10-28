"""
3、输入一个正数n，输出所有和为n 连续正数序列。（20分）
    例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以输出3 个连续序列1-5、4-6 和7-8。
"""
num  = int(input(">"))
sum = 0
for i in range(1,num):
    sum += i
    for j in range(i+1,num):
        sum +=j
        if sum ==num:
            print(i,"-",j)
            sum =0
            break
        if sum > num:
            sum =0
            break
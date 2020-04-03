"""
输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
"""
import math
b = []
for i in range(2, 101):
    a = int(math.sqrt(i))+1
    for j in range(2, a):
        if (i%j==0):
            break
    else:
        b.append(str(i))

c = ' '.join(b)
print(c)


# print(round(22.2))
# import math
# a = math.sqrt(4)
#
# print(round(a))

# for i in range(1, 1):
#     print(i)

# print(int(1.7))
# print(round(2.9))
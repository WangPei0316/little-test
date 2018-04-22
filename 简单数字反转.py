"""
输入一个整数，求它的反转数，比如输入169结果为961
"""

n = int(input('请输入一个整数：'))
m = n
i = 0
while n != 0:
    i = i*10 + n%10
    n //= 10
print("{:d}反转为{:d}".format(m,i))
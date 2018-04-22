'''
随机生成200个优惠码
'''

import random

list = []
for i in range(65,91):
    list.append(str(chr(i)))
for i in range(97,123):
    list.append(str(chr(i)))
for i in range(10):
    list.append(str(i))

nums = []

def generate(count,length):
    while count > 0:
        s = ''
        for i in range(length):
            a = random.choice(list)
            s = s+a
        nums.append(s)
        count -= 1
    print(nums)


generate(200,10)
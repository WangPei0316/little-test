import redis
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
    return nums


def save(nums):
    r = redis.Redis(host='127.0.0.1',port=6379,password='2012haiaini')
    for i in nums:
        r.rpush("code",i)
save(generate(200, 10))
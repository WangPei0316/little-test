'''
输入一个数字，猜大小
'''
import random

a = random.randint(0, 20)
num = int(input('猜数字：'))
while True:
    if num < a:
        print("太小了")
        num = int(input('重新猜：'))
    elif num > a:
        print("太大了")
        num = int(input('重新猜：'))
    else:
        print("Bingo,%d is the right num."%num)
        break

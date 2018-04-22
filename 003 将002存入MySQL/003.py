import pymysql
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
    connect = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='2012haiaini')
    cur = connect.cursor()
    try:
        __create = 'Create DATABASE if NOT EXISTS ShowMeTheCode'
        cur.execute(__create)
    except:
        print('database create error')
    connect.select_db('ShowMeTheCode')
    try:
        __create_table = 'CREATE TABLE if NOT EXISTS codes(code varchar(64))'
        cur.execute(__create_table)
    except:
        print('table create error')
    cur.executemany('insert into codes VALUES(%s)',nums)
    connect.commit()
    cur.close()
    connect.close()

save(generate(200, 10))

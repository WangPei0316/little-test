def find_num(arr, num):
    tp = set(arr)
    dic = {}
    for i in tp:
        dic[i] = 0
    for i in arr:
        dic[i] += 1
    print(dic[num])


find_num([5, 6, 5, 4, 8, 5, 1, 2], 5)

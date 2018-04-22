score = int(input("Please input your score:"))
while True:
    if score>100 or score<0:
        print('0=<score=<100,Invalid score')
        score = int(input("Please input your score:"))
    else:
        if 90<=score<=100:
            print('A')
        elif 70<=score<=89:
            print('B')
        elif 60<=score<=69:
            print('A')
        else:
            print('D')
        break

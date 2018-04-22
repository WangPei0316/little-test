out = open('test.txt', 'w')

while True:
    txt = input("输入文字或者输入‘q!!!!’退出")
    if txt != ('q!!!!'):
        out.write(txt)
    else:
        out.close()
        break

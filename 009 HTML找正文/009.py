from bs4 import BeautifulSoup

def find_content(path):
    with open(path) as f:
        text = BeautifulSoup(f,'lxml')
        contents = (line.strip() for line in text.get_text())
        for content in contents:
            print(content,end='')


find_content('/home/wangpei/PycharmProjects/littletest/009 HTML找正文/index.html')
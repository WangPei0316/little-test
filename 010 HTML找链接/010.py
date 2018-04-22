from bs4 import BeautifulSoup

def find_content(path):
    with open(path) as f:
        text = BeautifulSoup(f,'lxml')
        urls = text.find_all('a')
        for u in urls:
            print(u['href'])




find_content('/home/wangpei/PycharmProjects/littletest/010 HTML找链接/index.html')
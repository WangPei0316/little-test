import requests,re
from bs4 import BeautifulSoup

def get_img_url():
    url = 'http://tieba.baidu.com/p/2166231880'
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    request = requests.get(url,headers=header).text

    soup = BeautifulSoup(request,'lxml')
    img_list = soup.findAll('img',bdwater=re.compile(r"杉本有美吧"))

    img_src_list = []
    for i in range(len(img_list)):
        img_src_list.append(img_list[i].attrs['src'])
    return img_src_list

def down_img(list):
    for i in range(len(list)):
        file_name = list[i].split('/')[-1]
        image = requests.get(list[i])
        if image.status_code == 200:
            open(file_name,'wb').write(image.content)
        else:
            print("爬取失败")

down_img(get_img_url())
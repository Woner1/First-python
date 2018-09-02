# coding:utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://baike.baidu.com"
his = ["/item/%E7%8C%B4%E5%AD%90/1593453?fr=aladdin"]
for i in range(5):



    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')

    soup = BeautifulSoup(html, features='lxml')
    print(soup.find('h1').get_text()    )
    sub_urls=soup.find_all("a",
                           {
                               "target": "_blank",
                               "href": re.compile("/item/(%.{2})+$")
                           })
    url="https://baike.baidu.com"
    # print(sub_urls)
    if len(sub_urls)!=0:
        his.append(random.sample(sub_urls,1)[0]['href'])
    else:
        his.pop()
    print(his)


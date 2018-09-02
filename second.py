# coding:utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

html = urlopen("http://www.goudaitv.com/").read().decode('utf-8')


soup = BeautifulSoup(html, features='lxml')
print(html)
# img_links = soup.find_all('img')
# for link in img_links:
#     print(link)



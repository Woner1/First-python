# coding:utf-8

from bs4 import BeautifulSoup
from urllib.request import urlopen
import io
import re
html=urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode("utf-8")

soup=BeautifulSoup(html,features='lxml')
month=soup.find_all('ul',{"class":"jan"})
for m in month:
    print(m.get_text())



import requests
import os
from bs4 import BeautifulSoup

URL = "http://www.ngchina.com.cn/animals/"
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_url = soup.find_all('ul', {"class": "img_list"})
print(len(img_url))
os.makedirs('./img/', exist_ok=True)
for ul in img_url:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)

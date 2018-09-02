import os

os.makedirs('./img/',exist_ok=True)
IMAGE_URL="https://www.duba.com/static/images/public/20180831/7dfa3acf084e07a914e397e3f007bcaf.png"
from urllib.request import urlretrieve
urlretrieve(IMAGE_URL,'./img/image3.jpg')
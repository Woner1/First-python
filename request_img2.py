import requests

IMAGE_URL="https://www.duba.com/static/images/public/20180831/7dfa3acf084e07a914e397e3f007bcaf.png"
r = requests.get(IMAGE_URL, stream=True)    # stream loading

with open('./img/image2.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
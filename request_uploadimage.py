import requests
import webbrowser  # 打开游览器观看你是否在百度搜索页面

file={'uploadFile':open('a.jpg','rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
print(r.text)

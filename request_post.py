import requests
import webbrowser  # 打开游览器观看你是否在百度搜索页面

data = {'firstname': 'admin', 'lastname': 123}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)

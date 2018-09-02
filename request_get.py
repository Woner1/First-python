import requests
import webbrowser   #打开游览器观看你是否在百度搜索页面

param={"wd":"莫烦"} #搜索信息
r=requests.get('https://www.baidu.com/s',params=param)
print(r.url)
webbrowser.open(r.url)



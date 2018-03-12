# Python
import requests

#GET
url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'
res = requests.get(url)
print(res.status_code)
print('_'*20)
print(res.content.decode('unicode_escape'))
print("Hello World")

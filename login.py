import requests
from lxml import html
# 创建 session 对象。这个对象会保存所有的登录会话请求。
session_requests = requests.session()
# 提取在登录时所使用的 csrf 标记
login_url = "http://www.chechebijia.com/api/user/login/"
#result = session_requests.get(login_url)
#tree = html.fromstring(result.text)
#authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
payload = {
  "phone": "13811848104",
  "password": "cnt82562288",
  "operateType": 0
}
# 执行登录
result = session_requests.post(
  login_url,
  data = payload,
  headers = dict(referer=login_url)
)
print(result.content.decode('utf-8'))
print('_' * 40)
url = "http://www.chechebijia.com/api/parts"
payload = {
  "token":"",
  "mId": 0,
  "cId": 0,
  "bId": 8,
  "name":"",
  "chId": 0,
  "oIds":"",
  "iG": 0,
  "iO": 0,
  "page": 1,
  "limit": 6,
  "bType": 1,
  "iF": 1
}
# 获取列表
result = session_requests.post(
  url,
  data = payload,
  headers = dict(referer=url)
)
print(result.content.decode('utf-8'))




import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

import requests
url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'
result = requests.get(url)
print(result.status_code)
print('_'*40)
print(result.content.decode('utf-8'))
print(type(result))
print(type(result.content))
<<<<<<< HEAD
print(type(result.content.decode('utf-8')))
'''
fw = open('result.txt', 'w')
fw.write(result._content.decode('utf-8').encode())
fw.close
'''
=======

fw = open('result.txt', 'w')
fw.write(result._content.decode('utf-8'))
fw.close

>>>>>>> 136dfd137bd4b17031efbd2fff7c223f7bbfcff9

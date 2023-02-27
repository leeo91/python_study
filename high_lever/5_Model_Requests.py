# func
import requests
import re

url = 'https://www.ycpai.cn/python/Pu4gniQb.html'
# 反爬虫会带有这个请求头，所以要模拟
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
# 响应的编码格式
response.encoding = 'utf-8'
print(response.text)

value = re.findall('<div class="lesson_title">([\u4e00-\u9fa5]*)</div>', response.text)
print(value)

print('+++++++++++++++++++++++++++++++++++')
url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
# 反爬虫会带有这个请求头，所以要模拟
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers)
with open('logo.jpg', 'wb') as file:
    file.write(resp.content)


input()

#! /usr/bin/python3
# coding= utf-8

from urllib import request
from urllib import parse
from urllib import error
import http.cookiejar
import chardet

chardet.detect()

url = "https://www.baidu.com/"
data = {"name": "tony", "age": 12, "sex": "male"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/76.0.3809.100 Safari/537.36"}
parse.urlencode()
# 普通的get使用
# req= request.Request(url, headers=headers)
# response = request.urlopen(req).read()
# print(response.decode())
# 针对get请求
# try:
#     search = input("输入内容")
#     # https://www.baidu.com/s?ie=UTF-8&wd=wwwww
#     search= request.quote(search)
#     url1 = url + "s?ie=UTF-8&wd=" + search
#     print(url1)
#     req= request.Request(url=url1, headers=headers)
#     response = request.urlopen(req).read()
#     print(response.decode())
# except error.HTTPError:
#     print("error")
# except error.URLError:
#     print("url error")
# post 请求
# parse_data = parse.urlencode(data)
# req = request.Request(url=url, data=parse_data.encode(), headers=headers)
# response = request.urlopen(req)
# print(response.getcode())
# print(response)
# 基本的构建
# handler = request.HTTPHandler()
# opener= request.build_opener(handler)
# req = request.Request(url, headers=headers)
# response = opener.open(req)
# print(response.read())

# 设置代理
# proxy_handler = request.ProxyHandler({"http": "117.87.177.134:9000"})
# opener = request.build_opener(proxy_handler)
# req = request.Request(url, headers=headers)
# response = opener.open(req)
# print(response.read().decode())

# 设置 cookie
#有问题的url（）和data（虚拟的数据）
ck = http.cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(ck)
opener = request.build_opener(handler)
data = parse.urlencode(data).encode()
req = request.Request(url, data=data,headers=headers)
response = opener.open(req).read()
print(response.decode())


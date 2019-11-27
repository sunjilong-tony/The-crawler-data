#! /usr/bin/python3
# coding= utf-8

import requests
"""
get 使用
param
headers
cookie
requests.get(url，param,header,cookie)
r.status_code 获取状态码
r.text获取文件内容
r.head获取headers
r.encoding 获取网页的编码/同样也可以指定编码
r.context已二进制的方式获取内容（特别是图片和视频）
r.cookie获取cookie的信息（cookie信息为字典形式存储）
r.json()已json方式获取内容 
post使用

requests.post(url,data/json,headers,cookie)

put 使用（一般更新数据使用）和post一样
delete使用（无需传递参数）
requests.delete(url)
状态码为204

获取的状态码为304位重新定向请求（在f12对开preserver log 即可）

在requesets中，session对象是一个非常常用的对象，这个对象代表依次用户会话：
从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开
会话能让我们在跨请求时候保持某些参数，比如在同一个session实例发出的所有
请求直接按保持cookie
创建session
session = requests.Session()
得到session对象后，就可以调用该对象中的方法来发送请求

一般请求验证码及让sesson对象记录coolie信息
发送一个get空的请求，
session.get(url)
再次请求数据
session.post(url,data)



"""
# get
url = "http://192.168.112.82:8282/admin/login?redirect=%2Fmeeting%2Flist%2Fparticipant#/login?redirect=%2Fmeeting%2Flist%2Fparticipant"
data = {"mobile": "18000000000", "passWord": "000000"}
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
# r = requests.get(url, params=data, headers=headers)
# print(r.status_code)
# # print(r.text)
# r.json()
# # post
r1= requests.post(url, data=data)
print(r1.status_code)

import requests
import re
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\":"[\d.]*"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
def main():
    goods = '书包'
    depth = 1
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
        printGoodsList(infoList)
if __name__ == '__main__':
    main()
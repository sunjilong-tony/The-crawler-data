#! /usr/bin/python3
# coding= utf-8

from bs4 import BeautifulSoup
"""
使用方式：
可以将一个html文档，转化为指定的对象，然后通过对象的方法或者属性去查找指定的内容
转化本地文件：
soup = BeautifulSoup(open(本地文件)，'lxml')
转化网络文件
soup = BeautifulSoup("字符类型或者字节类型"， “lxml”)
"""

# 根据标签名查找
# soup.a 只能找到第一个符合要求的标签
soup = BeautifulSoup(open("soup.html", encoding="utf-8"), "lxml")
print(soup.a)
# 获取属性
soup.a['href']
soup.a['tille']
#获取内容
soup.a.text
soup.a.string
soup.a.get_text()
# 如果标签还有标签，那么string获取到的结果为None，而其他2个，可以获取到文本内容
# find 找到第一个符合要求的a，同样可以限定
soup.find('a',title/alt/class_/="内容")
 # 找到所有的同样可以限定
soup.find_all()
soup.find_all("a",limit=2)

# 根据选择器选择指定内容
# 常见的选择器：标签选择器/类选择器/id选择器/并集选择器/层级选择器/伪类选择器/属性选器
#select 选择器返回永远是列表，需要通过下标提取指定的对象，然后获取属性和节点，
#该方法也可以通过普通对象调用，找到都是这个对象下面符合要求的所有节点
soup.select("内容")
# coding= utf-8
'''
get:通过url网址传递信息，可以在url网址上添加要传递的信息，不安全
post：可以向服务器提交数据。是一种比较流行和安全的传递方式
put：请求服务器存储一个资源，通常要指定存储的位置
delete：请求一个服务器，删除一个资源
head：请求获取对应的http报头信息，
options：可以获取当前url所支持的请求类型

网页返回的数据为字符串类型，但是是json的，需要转换
https://www.baidu.com:443/path/文件名[:parameters][?query]#fragment
协议，    主机名    端口号   路径        参数       查询    信息片段

第一种是get请求
    方式一：urllib.request.urlopen(url)
    方式二：先创建一个urllib.request.Request对象，然后将对象放入urlopen中。urllib.request.urlopen(Request对象)
第二种是POST:携带数据过去
    比如：登录用户名，密码
    先创建一个urllib.request.Request
    将请求数据放到Request对象中urllib.request.Request(url,data)
    注意：在此之前先将data进行转化：
       data = urllib.parse.urlencode(values)
第三种是：添加请求头
""""
#get 请求
import urllib.request

#get 请求方式1
url = "http://www.baidu.com"
resp = urllib.request.urlopen(url)
if resp.status ==200:
    data = resp.read().decode("utf-8")
    #print(data)

#get请求方式2
url = "http://www.baidu.com"
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
if resp.status ==200:
    data = resp.read().decode("utf-8")
    #print(data)

#post请求
data = {"name":"张三","age":"17"}
url = "http://www.baidu.com"
z_data = urllib.parse.urlencode(data)
req = urllib.request.Request(url,z_data.encode('utf-8'))
resp = urllib.request.urlopen(req)
if resp.status ==200:
    data = resp.read().decode("utf-8")
    #print(data)


#header
import urllib.parse
import urllib.request

url = "http://www.baidu.com"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python'}
headers = {'User-Agent':user_agent}

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data.encode("utf-8"), headers)
response = urllib.request.urlopen(req)
the_page = response.read().decode("utf-8")
print(the_page)
'''''
from collections import deque

# coding= utf-8
import urllib.request
# 向指定的url地址发送请求，并返回服务器想用的数据（文件的对象）

'''
urlopen一般接受三个参数，它的参数如下：
urlopen(url, data, timeout)
第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。

第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。

'''
response = urllib.request.urlopen("http://www.baidu.com")
# 读取文件的全部内容
# data = response.read()
# 将爬取到的文件写入文件
# with open("./file1.html", "wb") as f:
#     f.write(data)
# 第二种
# data = response.readline()
# 第三种，建议
# data = response.readlines()
#response 属性
# 返回当前环境的有关信息
# print(response.info())
# 返回状态码
print(response.getcode())
# if response.getcode() == 200 or response.getcode() == 304:
#     # 500一般是服务器有问题400一般是url错误，300一般是缓冲问题 200执行ok
#     pass
# 返回当前正在爬取的url地址
print(response.geturl())
#搜索为中文url，复制后为字符串，使用下面的方法将其转化成中文（即解码）
# newurl = urllib.request.unquote(url)
# print(newurl)
#编码
# urllib.request.quote()

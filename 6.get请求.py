# coding= utf-8
'''
特点：吧数据拼接到请求路径后面传递给服务器
优点：速度快
缺点：承载少，不安全
'''
import urllib.request

url = "http://www.sunck.wang:8085/sunck"
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)
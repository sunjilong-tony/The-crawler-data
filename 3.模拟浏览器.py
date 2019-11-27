# coding= utf-8
import urllib.request


url = "http://www.baidu.com"
#模拟请求头
headers ={"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 "
                       "Safari/537.36"}
#设置一个请求体
req = urllib.request.Request(url,headers=headers)
#发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)

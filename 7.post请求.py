# coding= utf-8
'''
特点：吧参数进行打包，单独传输
优点：数据量大，安全
缺点：速度慢
'''
import urllib.request
import urllib.parse


url = "http://www.sunck.wang:8085/form"
# 将要发送的数据合成一个字典
# 字典的键去网页里找，一般为input标签的name属性
data ={
    "username":"sunck","passwd":"666"}
# 对要发送的数据进行打包,记住要编码
postdata = urllib.parse.urlencode(data).encode("utf-8")
# 请求体
req = urllib.request.Request(url, data=postdata)
req.add_header("User-Agent","User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 "
                       "Safari/537.36")
#请求
response = urllib.request.urlopen(req)
print(response.data().decode("utf-8"))

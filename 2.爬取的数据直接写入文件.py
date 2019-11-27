# coding= utf-8
import urllib.request
urllib.request.urlretrieve("http://www.baidu.com",filename="./file2.html")
# 此方法在执行过程中会产生一些缓冲，一般要清除缓冲
urllib.request.urlcleanup()

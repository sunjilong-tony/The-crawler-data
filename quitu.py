#! /usr/bin/python3
# coding= utf-8
from urllib import request,error,parse
import re
import time
import http.cookiejar


def get_text(url):
    headers = {
        "User - Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36", }
    cook = http.cookiejar.CookieJar()
    hander = request.HTTPCookieProcessor(cook)
    opener = request.build_opener(hander)
    req = request.Request(url=url, headers=headers)
    data = opener.open(req)
    print(data.getcode())
    print(data.read().decode())


def parse_text():
    pass


def save_text():
    pass


if __name__ == '__main__':
    try:
        url = "https://www.mzitu.com/jiepai/comment-page-43/"
        get_text(url)
    except error.HTTPError:
        print("http error")
    except error.URLError:
        print("url error")


#! /usr/bin/python3
# coding= utf-8

import pymysql


db = pymysql.connect("192.168.159.128", "long", "long", "test")
cursor = db.cursor()
sql = "select name, unix_timestamp() from names;"
cursor.execute(sql)
data = cursor.fetchone()
print(data)




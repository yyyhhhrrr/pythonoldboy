#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='960314',db='app_version')
# 创建游标,类似mysql终端上的游标
cursor = conn.cursor()

# 执行SQL，返回值是受影响行数

effect_row=cursor.execute("select * from sys_log ")

# print(effect_row)

print(cursor.fetchone()) # 取一条
print(cursor.fetchmany(3)) # 取前三条
# print(cursor.fetchall())
#  取所有，如果没有前面那个取一条，就把所有的取了，如果前面取了多少，就从上次取的地方开始取


# 批量提交
# li =[
#      ('alex','usa'),
#      ('sb','usa'),
# ]
# reCount = cur.executemany('insert into UserInfo(Name,Address) values(%s,%s)',li)
#
# conn.commit() 默认已经变成了事务 所以要提交，不然不会修改
# cur.close()

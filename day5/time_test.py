#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import time
print(time.time()) # 时间戳
print(help(time.gmtime()))

x=time.localtime(123411)
print(x)
print(time.strftime("%Y-%m-%d"))
print(x.tm_hour)
print(time.asctime())
print(time.ctime(1231231)) # 时间戳转格式化
#!/usr/bin/env python
# coding:utf-8
# Author:Yang


a="大大"
b=a.encode('GB2312') # 2312
c=a.encode() # utf-8
print(a)

print(b)
print(c.decode('GB2312'))
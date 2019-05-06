#!/usr/bin/env python
# coding:utf-8
# Author:Yang

class YangException(Exception):
    def __init__(self,msg):
        self.message=msg
    # def __str__(self):
    #     return self.message

try:
    raise YangException("我的异常")
except Exception as e:
    print(e)

#!/usr/bin/env python
# coding:utf-8
# Author:Yang


'''消息接收'''
from redishelper import RedisHelper

obj=RedisHelper()
redis_sub=obj.subscribe()

while True:
    msg=redis_sub.parse_response()
    print(msg)
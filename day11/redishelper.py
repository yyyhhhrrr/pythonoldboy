#!/usr/bin/env python
# coding:utf-8
# Author:Yang



'''redis 消息发布订阅 helper'''


import redis

import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='172.16.95.132')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):  # 发布
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self): # 订阅
        pub = self.__conn.pubsub() # 打开收音机
        pub.subscribe(self.chan_sub) # 调频道
        pub.parse_response() # 准备接收
        return pub
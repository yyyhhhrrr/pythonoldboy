#!/usr/bin/env python
# coding:utf-8
# Author:Yang


'''使用连接池 连redis'''
import redis

pool=redis.ConnectionPool(host='172.16.95.132',port='6379')

r=redis.Redis(connection_pool=pool)


r.set('foo','Bar')


print(r.get('foo'))
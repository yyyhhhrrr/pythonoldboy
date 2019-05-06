#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import redis

r=redis.Redis(host='172.16.95.132',port=6379)
r.set('foo','Bar')


print(r.get('foo'))
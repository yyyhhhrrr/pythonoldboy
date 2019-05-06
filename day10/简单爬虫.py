#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import gevent,time
from urllib import request
from gevent import monkey

#简单协程大并发爬网页


monkey.patch_all() # 把当前程序的所有io操作给我单独做上标记

def f(url):
    print('GET:%s'%url)
    resp=request.urlopen(url)
    data=resp.read()
    print('%d bytes received from %s .'%(len(data),url))


urls=['https://www.python.org/',
      'https://www.yahoo.com/',
      'https://github.com/'
]
time_start=time.time()
for url in urls:
    f(url)
print("同步cost:",time.time()-time_start)


async_time_start=time.time()

gevent.joinall([
    gevent.spawn(f,'https://www.python.org/'),
    gevent.spawn(f,'https://www.yahoo.com/'),
    gevent.spawn(f,'https://github.com/'),

])
print("异步cost:",time.time()-async_time_start)

# 时间一样是因为gevent 跟urllib没关系 ，gevent不知道urllib在做io ,
# 所以就没有切换，可以通过加入 monkey补丁
# monkey.patch_all() # 把当前程序的所有io操作给我单独做上标记
#
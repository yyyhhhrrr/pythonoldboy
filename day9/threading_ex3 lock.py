#!/usr/bin/env python
# coding:utf-8
# Author:Yang
import threading
import  time

# 互斥锁
start_time=time.time()
def run(n):
    lock.acquire() # 获取锁
    global num # 声明全局变量了
    num+=1
    lock.release()
lock=threading. Lock # 释放锁

# python 3.x不用加锁了 2.x在ubuntu上要加锁
num =0
t_objs=[]

for i in range(50):

    t =threading.Thread(target=run,args=("t%s"%i,))
    t.start()
    t_objs.append(t)
for t in t_objs:
    t.join()

print("-----all finished---")
print("num:",num)
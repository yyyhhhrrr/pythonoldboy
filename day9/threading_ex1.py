#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import threading
import  time

start_time=time.time()
# 多线程
def run(n):
    print("task",n)
    time.sleep(2)
    print("task done",n)


t_objs=[] # 存线程实例

for i in range(50):

    t =threading.Thread(target=run,args=("t%s"%i,))
    t.start()
    t_objs.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里
for t in t_objs: # 想查看所有线程执行完的时间必须先创建个线程的列表 ，并for循环
    t.join()

print(threading.current_thread(),threading.active_count()) # mainthread、 当前活跃线程
print("cost:",time.time()-start_time)

# 一个进程至少有一个线程，这段程序本身就是一个主线程，最后的cost时间是主线程执行的时间，所以说cost里没有2s，在for循环里只是开辟了子线程的执行
# 默认情况下主线程是不会等子线程执行完毕的
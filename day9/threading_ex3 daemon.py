#!/usr/bin/env python
# coding:utf-8
# Author:Yang
import threading
import  time

start_time=time.time()
# 多线程  守护线程
def run(n):
    print("task",n)
    time.sleep(2)
    print("task done",n)


t_objs=[] # 存线程实例

for i in range(50):

    t =threading.Thread(target=run,args=("t%s"%i,))
    t.setDaemon(True) # 把当前线程设置成守护线程（主线程结束都退出 不关心守护线程是否结束），就不用加join了
    t.start()
    t_objs.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里


print(threading.current_thread(),threading.active_count()) # mainthread、 当前活跃线程
print("cost:",time.time()-start_time)

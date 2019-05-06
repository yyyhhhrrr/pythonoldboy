#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from multiprocessing import Process,Queue

def f(q):
    q.put([42,None,'1'])

if __name__=='__main__':
    q=Queue()
    p=Process(target=f,args=(q,))
    p.start()
    print(q.get())
# 在主进程通过进程QUEUE读到了子进程往q里存的数据

# 解析过程:
# 其实是两个queue,主进程开启queue,把queue作为参数传入子进程中，是复制了另一个queue给子进程（pickle序列化）
# 然后 子进程往queue传数据，再pickle反序列化给主进程的queue
# 只是实现了这个进程的数据传给另一个进程
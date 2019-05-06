#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import threading
import time


# 类的写法来写多线程
# 这样写比较复杂

class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        self.n=n
        self.sleep_time=sleep_time
        super(MyThread,self).__init__() # 因为继承父类 要重构父类的构造方法

    def run(self): # 只能是run
        print("running task",self.n)
        time.sleep(self.sleep_time)
        print("task done..",self.n)
t1=MyThread("t1",2)
t2=MyThread("t2",4)

t1.start()
# t1.join()  # 其实就是有些语言中的wait() 等待线程结束 相当于不等待结果就不会往下走，变成串行的了
t2.start()

t1.join()
t2.join()
print("main thread...")
#!/usr/bin/env python
# coding:utf-8
# Author:Yang

# 事件 线程可以关注另一个线程状态而做出相应的响应
import time
import threading

event=threading.Event()
def lighter():  # 路灯
    count = 0
    event.set() # 先绿灯 默认true为绿灯
    # event.clear() 清空标志位 代表红灯
    # event.wait() 等待标志位
    while True:
        if count >5 and count<10:
            event.clear() # 把标志位清了
            print("\033[41;1mred light is on...\033[0m")
        elif count >10:
            event.set() # 变绿灯
            count =0
        else:
            print("\033[42;1mgreen light is on...\033[0m")
        time.sleep(1)
        count+=1

def car(name):
    while True:
        if event.is_set(): # 代表绿灯
            print("[%s] running..."%name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..."%name)
            event.wait()
            print("\033[34;1m[%s] green light is on ,start going...\033[0m"%name)

light = threading.Thread(target=lighter,)
light.start()

car1=threading.Thread(target=car,args=("Tesla",))
car1.start()

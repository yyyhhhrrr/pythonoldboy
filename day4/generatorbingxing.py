#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import time
# 生产者消费者模型 单线程并行(协程)
def consumer(name):# 消费者
    print("%s 准备吃包子了"%name)
    while True:
        baozi=yield
        print("包子[%s]来了，被[%s]吃了"%(baozi,name))

c=consumer("yhr")
c.__next__()
# b1="韭菜馅"
# c.send(b1) # 调用yield 传值 （唤醒传值）
# c.__next__() # 调用yield  不传值 （只唤醒）


def producer(name): #生产者
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子，分两半")
        c.send(i)
        c2.send(i)


producer("yang")
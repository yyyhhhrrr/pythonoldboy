#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import time

# 装饰器是嵌套和高阶的结合
def timer(func):  # timer(test1)  test1=func  使用到函数的嵌套
    def deco(*args,**kwargs):
        start_time=time.time()
        # return func # return内存地址
        func(*args,**kwargs)  # run test1()
        stop_time=time.time()
        print("runtime %s"%(stop_time-start_time))
    return deco  # 使用到高阶函数
@timer # test1=timer(test1)
def test1():
    time.sleep(3)
    print("1")
@timer
def test2(name,age):
    time.sleep(1)
    print(name,age)


#deco(test1) # 在改函数的调用方式 应该为test1()就不会改函数调用方式


# test1=deco(test1)  # 调用deco是获取test1内存地址 再赋给test1，再test1（）运行，但是结果并没有增加新功能
# test1()
#
# deco(test2)

# test1=timer(test1)
test1() # 此时调用的是deco而不是test1
test2("yang",22)

#!/usr/bin/env python
# coding:utf-8
# Author:Yang
# 第一个特性：函数即“变量”
# def foo():
#     print('in the foo')
#     bar()
#
# foo()
# def bar():
#     print('in the bar')
#
# def foo():
#     print('in the foo')
#     bar()
#
# foo()

# 匿名函数
# calc = lambda x:x*3
# print(calc(3))


# 第二个特性：高阶函数
import time
def bar():
    time.sleep(3)
    print("y")

def test(func): # 高阶函数 调用的形参是一个函数名
    start_time=time.time()
    func()
    stop_time=time.time()
    print(func) # 打印的函数内存地址
    print("run %s"%(stop_time-start_time))


test(bar)

def test2(func):
    print(func)
    return func

# print(test2(bar))
bar=test2(bar)
bar
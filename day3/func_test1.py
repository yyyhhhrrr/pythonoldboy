#!/usr/bin/env python
# coding:utf-8
# Author:Yang


# 函数
def func1():
    print('in the func1')
    return 0
# 过程    相当于没有返回值的函数
def func2():
    print('in the func2')


x=func1()
y=func2()

print('from func1 is %s,from func2 is %s'%(x,y))

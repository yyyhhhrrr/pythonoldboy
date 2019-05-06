#!/usr/bin/env python
# coding:utf-8
# Author:Yang

def test1():
    print('test1')

def test2():
    print('test2')
    return  0

def test3():
    print('test3')
    # return  1,'1',['1','2'],{'3':'4'}
    return test2 # 返回的内存地址
x=test1()
y=test2()
z=test3()
print(x)
print(y)
print(z) # 返回的是（）tuple 元组
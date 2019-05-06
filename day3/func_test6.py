#!/usr/bin/env python
# coding:utf-8
# Author:Yang

def test(*args): # 接收n个位置参数，转换为元组的形式
    print(args)

test(1,2,3,4,6)
test(*[1,2,3,4,5]) # *args=*[1,2,3,4,5]=
                   # 相当于 args = tuple([1,2,3,4,5])

def test1(x,*args):
    print(x)
    print(args)

test1(1,2,3,4,5,6,6,7)


# **kwargs  接收n个关键字参数转换为字典的方式
def test2(**kwargs):
    print(kwargs)
    print(kwargs['name'])
test2(name='yang',age=8,sex='F')
test2(**{'name':'yang','age':'12'})

def test3(name,**kwargs):
    print(name)
    print(kwargs)
test3('yang',age=18,sex='a')

def test4(name,age=18,**kwargs): # 参数组一定要往后放
    print(name)
    print(age)
    print(kwargs)

test4('yang',hobby='tesla')
test4('yang',hobby='tesla',age=4)
test4('yang',3,hobby='tesla')

def test5(name,*args,age=18,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)


test5('yang',3,age=4,hobby='tesla')   # 位置参数必须在关键字参数之前

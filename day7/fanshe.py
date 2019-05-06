#!/usr/bin/env python
# coding:utf-8
# Author:Yang

def bulk(self):
    print("%s is yelling..."%self.name)

class Dog(object):
    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print("%s is eating %s"%(self.name,food))

d = Dog("A")
choice = input(">>:").strip()

# print(hasattr(d,choice))

# print(getattr(d,choice))


if hasattr(d,choice):
    func = getattr(d,choice)
    func("banana")
    # delattr(d,choice)
else:
    setattr(d,choice,bulk) # d.talk=bulk bulk本身在类外 把bulk的内存地址赋给d.talk 使d.talk有bulk的功能

    d.talk(d)


# 反射 就是把字符串映射到函数的内存地址
# hasattr（obj,name_str）,判断一个对象里是否有对应的name_str字符串的方法 返回true or false
# getattr（obj,name_str）,根据字符串去获取obj对象里的对应的方法的内存地址
# setattr（obj,name_str,value）,根据字符串去设置方法
# delattr (obj,name_str),根据字符串删除方法

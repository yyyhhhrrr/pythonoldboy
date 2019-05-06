#!/usr/bin/env python
# coding:utf-8
# Author:Yang

class Dog(object):
    n=123 # 类变量
    def __init__(self,name):
        self.name=name
    @classmethod # 类方法 很少用
    def eat(self):
        print("%s is eating %s "%(self.n,'baozi'))


d=Dog("A")
d.eat()

# 类方法
# 只能访问类方法，不能访问实例变量
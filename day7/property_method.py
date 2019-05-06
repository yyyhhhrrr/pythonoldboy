#!/usr/bin/env python
# coding:utf-8
# Author:Yang

class Dog(object):

    def __init__(self,name):
        self.name=name


    @property  # (有时候用)
    def eat(self):
        print("%s is eating %s "%(self.name,'baozi'))

    @eat.setter # 修改属性
    def eat(self, food):
        print("set to food:", food)

    @eat.deleter  # 删除属性
    def eat(self):
        del self.name
        print("删完了")
d=Dog("A")
d.eat
d.eat="包子"
# 属性方法删不了，必须定义方法删
# del d.eat
# print(d.eat)
del d.eat


# 属性方法
# 把一个方法变成一个静态属性
# 隐藏实现细节
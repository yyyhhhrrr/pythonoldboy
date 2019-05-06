#!/usr/bin/env python
# coding:utf-8
# Author:Yang


class Dog(object):
    def __init__(self,name):
        self.name=name
    @staticmethod  # 静态方法：实际上跟类没什么关系了,相当于是类下的一个函数，与类没有关系（很少用）
    # def eat(self,food):
    #     print("%s is eating %s "%(self.name,food))
    def eat():
        print("is eat")

d=Dog("A")
d.eat()


# 静态方法
# 只是名义上归类管理，实际上在静态方法里访问不了类或实力中的任何属性
#!/usr/bin/env python
# coding:utf-8
# Author:Yang

# class Foo(object): # 创建类的普通方式
#     def __init__(self,name):
#         self.name=name
# f=Foo("A")


def func(self):   # 创建类的特殊方式
    print("hello %s"%self.name)
def __init__(self,name,age):
    self.name=name
    self.age=age

Foo=type('Foo',(object,),{'func':func,'__init__':__init__})

f=Foo("A",22)
f.func()

# 一切皆对象 f,Foo都是对象。f通过Foo类的构造方法创建，那么Foo类也是有某个类的构造方法创建(或者Foo类是type类实例化的)
print(type(f))
print(type(Foo)) # 打印结果为 <class 'type'> Foo类后面的类就是type,Foo类是type类的一个实例

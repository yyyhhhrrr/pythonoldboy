#!/usr/bin/env python
# coding:utf-8
# Author:Yang
from lib import aa
class Foo:
    ''' 类的描述'''

    def func(self):
        pass
    def __call__(self, *args, **kwargs):  #  可以使对象后面加括号，触发执行
        print(1,args,kwargs)
    def __str__(self):    # 可以使打印实例时返回值（没有这个方法时，print(d)是实例的内存地址）
        return "aaaa"
    def __getitem__(self, key):
        print('__getitem___',key)
    def __setitem__(self, key, value):      # 把一个实例变成字典
        print('__setitem__',key,value)
    def __delitem__(self, key):
        print('__delitem__',key)
obj=aa.A()
print(Foo.__doc__) # 打印类前面的注释（就是类是干嘛用的）
print(obj.__module__) # 表示当前对象在哪个模块 输出模块
print(obj.__class__) # 表示当前对象在哪个类  输出类

d=Foo()
d(1,2,k=3)
print(Foo.__dict__) # 查看类中所有方法和成员，以字典形式打印
print(d.__dict__) # 查看实例中的所有变量，以字典形式打印
print(d)

d['name']="A"
print(d['name'])
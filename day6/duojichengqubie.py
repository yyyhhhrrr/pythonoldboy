#!/usr/bin/env python
# coding:utf-8
# Author:Yang
# 多继承区别
# 对于构造函数的查找
# 有两种继承策略：
# 广度优先:横向策略查找优先 D->B->C->A
# 深度优先:纵向策略查找优先 D->B->A->C
# python3 经典类和新式类都是广度优先来继承的
# Python2 经典类是深度优先来继承的，新式类是广度优先来继承的
class A :
    def __init__(self):
        print("A")
class B(A):
    pass
    # def __init__(self):
    #     print("B")
class C(A):
    pass
    # def __init__(self):
    #     print("C")
class D(B,C):
    pass

d1=D()
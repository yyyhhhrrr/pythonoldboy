#!/usr/bin/env python
# coding:utf-8
# Author:Yang
#
# mod = __import__("lib.aa")
#
# a=mod.aa.A()
# print(a)


import importlib
aa=importlib.import_module("lib.aa")
obj=aa.A()


assert type(obj.name) is str  # 断言
print('ddd')


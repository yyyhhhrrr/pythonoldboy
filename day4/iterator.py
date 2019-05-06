#!/usr/bin/env python
# coding:utf-8
# Author:Yang
from collections import Iterable
a=[1,2,3]
print(dir(a))
print(isinstance(a,Iterable))


# 生成器都是iterator对象，list,dict,tuple,str 是Iterbale,却不是iterator
# 凡是可作用与for循环的对象都是iterable对象
# 凡是可作用与next（）函数的兑现个都是iterator对象，表示一个惰性计算的序列
# b=iter(a) 将a转为iterator对象
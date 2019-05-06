#!/usr/bin/env python
# coding:utf-8
# Author:Yang


def fib(max):  # 只要有yield存在 就是生成器 且不是函数了
    n,a,b=0,0,1
    while n <max:
        # print(b)
        yield b  # 保存函数的中断状态
        a,b=b,a+b
        # a,b=b,a+b相当于 t=(b,a+b) t是一个元组
        # a=t[0]
        # b=t[1]
        n=n+1
    return  'done'

f=fib(10)
# #print('---------ddddd')
# print(f.__next__())
# print("----")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

print('start loop')
# #for i in f:
#     print(i)


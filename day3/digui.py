#!/usr/bin/env python
# coding:utf-8
# Author:Yang


#递归函数特性:
# 必须要有约束条件
# 每进入一层，问题规模要减少
# 递归效率不高，递归层次增多后，会导致栈溢出（函数是栈式存储的，每进行一次函数调用，增加一层栈帧，每返回一次值，减少
# 一层栈帧，由于栈不是无限大在内存中，当次数过多时，会导致栈溢出）
def cal(n):

    print(n)
    if int(n/2) > 0:
        return cal(int(n/2))
    print("->",n)

cal(10)
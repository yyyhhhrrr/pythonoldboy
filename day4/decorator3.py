#!/usr/bin/env python
# coding:utf-8
# Author:Yang

# 第三个特性：嵌套函数

def foo():
    print("in the foo")
    def bar():  # 函数即 变量 类似于局部变量
        print("in the bar")
    bar()
foo()
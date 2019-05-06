#!/usr/bin/env python
# coding:utf-8
# Author:Yang

def test(x,y=2): # 默认参数
    print(x)
    print(y)

# test(1,3)
test(1,y=3)


# 默认函数特点：调用函数的时候，默认参数非必须传递
# 用途：1.默认安装值 2.连接数据库端口号
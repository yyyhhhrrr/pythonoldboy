#!/usr/bin/env python
# coding:utf-8
# Author:Yang

def test(x,y): # 形参
    print(x)
    print(y)

# # test(1,2) # 实参   与形参一一对应
# test(y=1,x=2)  # 关键字调用 与形参顺序无关

#test(x=2,3) # 出错 会以为有多个x
test(3,y=2) # 不会出错 ，只是表明y只有一个值
# 关键字参数不能写在位置参数前面
#!/usr/bin/env python
# coding:utf-8
# Author:Yang
product_list=[]
with open("F:/homework/day2/homeworkday2.txt") as f:
    for line in f: # 一行一行读 且内存里只保存一行 最好用这种方式
        product_list.append(list(line.strip('\n').split(',')))



   # print(f.read())# 一次读所有都放进内存
   # for line in f.readlines(): # 一次读一条 放入内存
   #     print(line)
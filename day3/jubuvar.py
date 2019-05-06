#!/usr/bin/env python
# coding:utf-8
# Author:Yang
school="yhr" # 全局变量
names=["y","h","r"]
def chang_name(name):
    global school
    school = "yhr123"
    print('before change',name,school)
    name = 'yang' # 这个函数就是这个变量的作用域
    print('after change',name)
    names[0]="x"
    print("names:",names)

name = 'y' # 全局变量
chang_name(name)
print(name)
print(school)
print(names)  # 只有集合，列表，字典能够改全局变量，字符串、常量是不能改全局变量的（元组本身就不能改）
# 禁止以下写,容易导致逻辑混乱，不好调试，每一次调用都会改全局变量
# def change_name():
#     global name  # 可以变成全局变量，如果之前有就代替以前的全局变量
#     name="y"
#
# change_name()
# print(name)


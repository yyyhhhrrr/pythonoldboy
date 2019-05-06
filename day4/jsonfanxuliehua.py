#!/usr/bin/env python
# coding:utf-8
# Author:Yang

# 读json
import json
f=open('test.txt','r')
data=json.loads(f.read())
print(data['age'])
f.close()
# print(eval(data)['age'])


# # 读pickle
# import pickle
#
# def sayhi():
#     name='yhr'
#     print("hello",name)
#     print("hello2")
# f=open('test2.txt','rb')
# data=pickle.loads(f.read())
# print(data)
# print(data['func']())
f.close
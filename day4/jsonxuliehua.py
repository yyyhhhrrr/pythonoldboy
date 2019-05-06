#!/usr/bin/env python
# coding:utf-8
# Author:Yang
import json
import pickle


def sayhi():
    name='yhr'
    print("hello",name)
info ={
    'name':'yang',
    'age':22

}

f = open("test.txt","w")   # 写json 传简单数据
f.write(json.dumps(info))


# f=open('test2.txt','wb')  # 写pickle 能序列化函数对象 传输内存地址
# f.write(pickle.dumps(info)) # f.write(pickle.dump(info,f)
f.close()

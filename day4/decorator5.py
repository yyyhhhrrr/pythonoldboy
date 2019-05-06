#!/usr/bin/env python
# coding:utf-8
# Author:Yang


# 装饰器高级版

import time
user="yang"
pwd="123"
def auth(auth_type):
   print("auth func:",auth_type)
   def outer_wrapper(func):
       def wrapper(*args, **kwargs):
           print("auth func wrapper:",*args, **kwargs)
           if auth_type =="local":
               username = input("username:").strip()
               password = input("pwd:").strip()

               if user == username and pwd == password:
                   print("\033[32;1m user has passed authentication\033[0m")
                   res = func(*args, **kwargs)  # from home
                   print('---')
                   return res
               else:
                   exit("\033[32;1m error\033[0m")
           elif auth_type=="ldap":
                 print("ladap")
       return wrapper
   return outer_wrapper

def index():
    print("welcome to index.html page")
@auth(auth_type="local")  # 本地认证  这句话相当于
def home(): # 需要登录
    print("welcome to home page")
    return "from home"
@auth(auth_type="ldap")   # 远程认证
def bbs(): # 需要登录
    print("welcome to bbs page")


index()
print(home()) # 调用的wrapper
bbs()
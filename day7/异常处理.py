#!/usr/bin/env python
# coding:utf-8
# Author:Yang

data={}
names=[1,2,3]
try:
    a=1
    print(a)
    # names[3]
    # data['name']
    #open("1.txt") # python 2.x是IOError 3.x是FileNotfounderror

except (KeyError,IndexError) as e:  # 2.7是 except Exception,e
    print("没有Key",e)
except IndexError as e:
    print("列表操作错误",e)
except Exception as e: # 抓住所有错误 一般放到最后   # indentation error 缩进，语法错误抓不到
    print("出错了",e)
else:
    print("一切正常")
finally: # 不管有没有错都执行
    print("不管有没有错都执行")

#!/usr/bin/env python
# coding:utf-8
# Author:Yang
import time

def logger():
    time_format="%Y-%m-%d %X"
    time_current=time.strftime(time_format)
    with open('a.txt','a+') as f :
        f.write('end action\n %s '%time_current)

def test1():
    print('test1 starting actiong..')
    logger()
def test2():
    print('test2 starting actiong..')
    logger()
def test3():
    print('test3 starting actiong..')
    logger()

test1()
test2()
test3()
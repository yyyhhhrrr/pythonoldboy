#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import copy

person=['names',['saving',100]]

#三种浅copy
'''p1=copy.copy(person)
p2=person[:]
p3=list(person)'''

p1=person[:]
p2=person[:]

p1[0]='yang'
p2[0]='gfofyang'

p1[1][1]=50
print(p1,p2)
#!/usr/bin/env python
# coding:utf-8
# Author:Yang
'''count = 0
while True:
    print("count:",count)
    count = count+1 # count +=1
    if count == 1000:
        break
'''
'''
for i in range(0,10):
    if i<3:
        print("count:",i)
    else:
        continue
    print("hehe...")
'''

for i in range(10):

    print('----------',i)
    for j in range(10):
        print(j)
        if j > 5:
            break
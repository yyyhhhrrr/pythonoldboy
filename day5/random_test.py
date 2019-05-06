#!/usr/bin/env python
# coding:utf-8
# Author:Yang
import random
print(random.random()) # (0,1) 随机数
print(random.randint(1,7)) # 1到7 包含7
print(random.randrange(10)) # 取不到10 顾头不顾尾 0到9
print(random.choice('asda')) # 从字符串随机找
print(random.sample('asdac',2)) # 从前二随机取两个
print(random.uniform(1,3)) # 可以定义区间


# random实现简易验证码

checkcode = ''

for i in range(4):
    current = random.randrange(0,4)
    # 字母
    if current == i:
        tmp=chr(random.randint(65,90)) #65->A 90->Z
    else:
    #数字
        tmp=random.randint(0,9)
    checkcode +=str(tmp)

print(checkcode)




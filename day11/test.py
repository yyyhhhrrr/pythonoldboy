#!/usr/bin/env python
# coding:utf-8
# Author:Yang


import random
j = 6
id = []
id = ''.join(str(i) for i in random.sample(range(0,9),j))    # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
print (id)
#!/usr/bin/env python
# coding:utf-8
# Author:Yang

list_1 = [1,4,5,7,3,6,7,9]

list_1=set(list_1) # 变为集合 可以去重
print(list_1,type(list_1))

list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)
# inrwesection 交集
print(list_1 & list_2)
print(list_1.intersection(list_2))
# 并集
print(list_1 | list_2)
print(list_1.union(list_2))
# 差集
print(list_1 - list_2) # 在1不在2
print(list_1.difference(list_2))
# 子集
list_3 = set([1,3,7])
print(list_3.issubset(list_3))
print(list_1.issuperset(list_3)) # 父集

# 对称差集
print(list_1 ^ list_2)
print(list_1.symmetric_difference(list_2)) # 并集-交集 symmetric 对称

list_4 = set([5,6,8])
print(list_3.isdisjoint(list_4)) # 判断没有交集为true

# 没有插入只能添加
list_1.add(999)
print(list_1)
# 添加多项
list_1.update([99,11])
print(list_1)

# 删除
list_1.remove(1)
print(list_1)

# 长度 len(list_1)

# 判断成员

1 in list_1
1 not in list_1
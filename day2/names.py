#!/usr/bin/env python
# coding:utf-8
# Author:Yang

names = ["a","b","c","d"]
names.append("e") # 追加到尾
names.insert(1,"x") # 插入位置 下标为1
names[2]="y" # 修改

# print(names[0],names[1])
print(names[1:3]) # 切片 顾头不顾尾
# print(names[len(names)-1]) # 取最后以为
# print(names[-1]) # 从右边开始数
# print(names[-1:-3])
# print(names[-3:-1]) # 不包含最后一个
# print(names[-2:]) # 包含尾
# print(names[0:3])

#delete
#names.remove("a")
#del names[1]
#names.pop() # 默认删最后一个
#names.pop(1)
print (names)
print(names.index("y"))
names.reverse()
names.sort() # ascll码排序
names2 = [1,2,3]
names.extend(names2)
print(names,names2)
print(names[0:-1:2]) # 2为步长
#!/usr/bin/env python
# coding:utf-8
# Author:Yang

info = {
    'stu1':'y',
    'stu2':'a',
    'stu3':'c',
}

print(info)
#print(info['stu1'])
info['stu1']='z'
print(info)
del info['stu1']
#info.pop('stu1')
#info.popitem() # 随机删除
print(info.get('stu2'))
print('stu1' in info)
'''
c = dict.fromkeys([6,7,8],[1,{"name":"alex"},444])
#print(info.items()) #dict转list

c[7][1]['name']='jack' # 三个共享一个地址'''

for i in info:
    print(i,info[i])

print(info.items()) #dict转list
for k,v in info.items():
    print(k,v )
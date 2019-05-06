#!/usr/bin/env python
# coding:utf-8
# Author:Yang
# 内置函数
print(all([0,-1,3])) # 判断iterable元素 都为真则返回True 非0为真 有假则假

print(any([0,-1,3])) # 有真则真

print(ascii([1,2,"杨"])) #把内存的数据对象变成可打印的字符串对象

print(bin(255)) # 数字十进制转二进制 b 代表二进制开头

print(bool(0),bool(1),bool(-1)) # 判断布尔值 列表为空 字典为空 是假

a=bytes("abcde",encoding="utf-8")
b=bytearray("abcde",encoding="utf-8") #打印a的ascii形式
print(b[1])

def a():
    pass
print(callable(a)) # 判断是否可调用

print(chr(98)) # 把数字对应ascii

print(ord('d')) # 把ascii转对应数字

code="for i in range(10):print(i)"
#print(compile(code,'','exec'))
#c=compile(code,'','exec') # 把字符串编译成可执行文件
exec(code) # exec可直接执行。。。（多行）

list=[]

print(dir(list)) # 可以查方法

print(divmod(5,3)) # 得商，余数

l=[1,2,3]
for i in enumerate(l): # 将iterable可迭代对象组成一个索引序列
    print(i)
a="2*5"
d="[1,2,3]"
print(eval(a)) # 用来执行字符串表达式，并返回表达式的值
print(eval(d)) # 将字符串对象转换为有效的表达式，讲d转换为list

res = filter(lambda n:n>5,range(10)) # 使用了匿名函数做条件，filter作为过滤器，在3.0 filter生成的是迭代器对象，要用for来迭代
for i in res:
    print(i)

import functools
res1=functools.reduce(lambda x,y:x+y,range(10))
print(res1)

f="{} {}".format("hello","world") # 格式化字符串/数字
print(f)

a=frozenset([1,3,444,55,231,3]) # 变成不可变集合

print(globals()) # 返回当前程序所有全局变量的字典

print(hash('yang')) # 生成哈希算法对应哈希值 （找字符串的时候 就是哈希值的二分查找）

print(hex(10)) # 转为16进制 0x

def test():
    local_var='a'
    print(locals()) # 打印当前局部变量
test()

print(oct(10)) # 转八进制 0o
print(oct(8))

print(round(1.3323))
print(round(1.32,2)) #保留两位

a={6:2,-3:1,3:4}
print(sorted(a.items())) # 把key排序变成列表
print(sorted(a.items(),key=lambda x:x[1])) # 把value排序变成列表

a=[1,2,3,4]
b=['a','b','c','d']
for i in zip(a,b): # 拉链 组合
    print(i)

__import__('decorator') # 之后会用
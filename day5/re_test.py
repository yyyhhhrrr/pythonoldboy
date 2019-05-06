#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import re

print(re.match(".+","asde")) # 指定除\n任意字符  match 方法只从字符串开头往后匹配
print(re.search("^a","adade")) # 匹配字符开头
print(re.search("de$","adade")) # 匹配字符结尾
print(re.search("R[a-z]+a","Chen321Ronghua123a"))
print(re.search("ad*","sadea")) # *前字符零次或多次
print(re.findall("ad*","sadea"))
print(re.findall("a*","asdeda"))
print(re.match("a+","sdad"))  # match 从开头匹配
print(re.search("a?","asdwdasdw").group()) # group() 得到结果
print(re.search("aaa?","aaaalex"))  # 符号前 0个或1个
print(re.search("[0-9]{3}","dada1dq2aa4ada4"))  # {}匹配几次
print(re.search("[0-9]{1,3}","dada1dq2aa4ada4"))  # 匹配1到3次 只匹配1
print(re.findall("[0-9]{1,3}","dada1dq2aa4ada4"))  # 匹配1到3次 都要匹配  findall没有group方法
print(re.search("abc|ABC","ABCBabcCD")) # |左或|右
# \A 开头 同^
# \Z 结尾 同$
# \d 数字
# \D 非数字
# \w 匹配[A-Za-z0-9]
# 匹配非[A-Za-z0-9]
# \s 匹配空白字符（\t,\n,\s）


# 分组匹配
print(re.search("(?P<id>[0-9]+)","abcd1234daf034").groupdict())
print(re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","abcd1234daf034").groupdict())

# split
print(re.split("[0-9]+","abc12de3f45GH")) # 分割

# sub
print(re.sub("[0-9]+","|","abc12de3f45GH")) # 替换
print(re.sub("[0-9]+","|","abc12de3f45GH",count=2)) # 替换

# 匹配\
print(re.search("\\\\","abc12de\\3f45GH"))
print(re.search(r"\\","abc12de\\3f45GH")) # 其实结果是一个\
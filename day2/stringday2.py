#!/usr/bin/env python
# coding:utf-8
# Author:Yang

name = "my  name is {name} and i am {year}'s old"
print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-")) # 中心
print(name.endswith("ex"))
#print(name.expandtabs(tabsize=30))
print(name.find("name")) # 返回index
print(name[name.find("name"):])
print(name.format(name='alex',year='22'))
print(name.format_map({'name':'alex','year':'22'})) # 只能加dict
print('ab23'.isalnum()) # 包含阿拉伯数据字或阿拉伯字符
print('ab23'.isalpha()) # 包含字符
print('1.23'.isdecimal())
print('1A'.isdigit())
print('a 1A'.isidentifier()) # 判断是不是一个合法的标识符
print('33.33'.isnumeric())
print('+'.join(['1','2','3']))
print(name.ljust(50,'*')) # 不够用*号表示
print(name.rjust(50,"*"))
print('    alex\n'.strip()) # 去首尾空格  strip('a')去除首字符为a
p = str.maketrans("abcdefli","123$@456")
print("alex li".translate(p))
print('alex li'.replace('l','L'))
# print('alex li'.replace('l','L',1))
# print('alex li'.rfind('l'))
# print('1+2+3+4'.split('+')) # 分割
# print('1+2\n+3+4'.splitlines()) # 分割
# print('Alex LI'.swapcase())
# print('yang hao rna'.title())
# print('alex li'.zfill(50))


#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import sys

print(sys.getdefaultencoding())
s = "你好" # 在这里 以上设置的utf-8只是文件编码，在python里所有都是用的unicode ,所以这里是unicode编码
s_to_gbk=s.encode("gbk")
print(s_to_gbk)  # gbk
print(s.encode()) # utf8

gbk_to_utf8=s_to_gbk.decode("gbk").encode("utf-8")   # 在python3中，encode不但转了编码还转换为byte类型
utf8_to_gbk=s.encode().decode("utf-8").encode("gbk")    # 转码 先decode转为unicode  在这里unicode以byte类型显示 然后再ecode为gbk
print(gbk_to_utf8)
print(utf8_to_gbk)

# 字符串转字节码 encode 编码
# 字节码转字符串 decode  解码
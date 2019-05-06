#!/usr/bin/env python
# coding:utf-8
# Author:Yang

# 客户端
import socket

client=socket.socket() # 默认地址簇为 AF_INET （IPV4）  声明socket类型，同事生成socket连接对象
client.connect(('localhost',9999))
while True:
    msg=input(">>:").strip()
    if len(msg)==0:continue# 不能send None
    client.send(msg.encode("utf-8")) # python2.x 都是字符串 python3.x都是二进制
    data=client.recv(1024)  # recv大小是有限制的
    print("recv:",data)
client.close()

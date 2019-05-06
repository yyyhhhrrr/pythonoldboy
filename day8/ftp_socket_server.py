#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import socket,os,hashlib
server=socket.socket()
server.bind(('localhost',9999))
server.listen()

while True:
    conn,addr=server.accept()
    print("new conn",addr)
    while True:
        print("等待连接")
        data=conn.recv(1024)
        if not data:
            print("客户端已断开...")
            break
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename): # 判断是一个文件而不是目录
            f=open(filename,"rb")
            m =hashlib.md5()
            file_size=os.stat(filename).st_size # 获取文件大小
            conn.send((str(file_size).encode("utf-8"))) # 发送文件大小
            conn.recv(1024) # wait for ack
            for line in f:
                m.update(line)
                print(type(line))
                conn.send(line)
                print(line)
            print("file md5",m.hexdigest())# m转16进制
        f.close()
        conn.send(m.hexdigest().encode()) # 最后send md5。

        print("send done...")

server.close

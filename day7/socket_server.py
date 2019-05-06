#!/usr/bin/env python
# coding:utf-8
# Author:Yang

# 服务器端  实现 简单多连接socket通信，一个挂断，另一个连上

import socket

server=socket.socket()
server.bind(('localhost',6969)) # 绑定要监听的端口
server.listen(5) # 监听(最多可监听5个对话，相当于可以有五个连接排队)

print("i'm waiting for calling..")
while True:
    conn,addr=server.accept() # 等待消息
    print(conn, addr)  # conn连接对象
    # conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print("it's comming")

    while True:
        data=conn.recv(1024)
        print("recv:",data)
        if not data:# 如果data为空
            print("client has lost....")
            break
        conn.send(data.upper())# 变大写
        # send是取决于不同系统的缓冲区大小

server.close()
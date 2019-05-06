#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import select
import socket
import queue

# 单线程下的io 多路复用的selcet实现socket_server


server=socket.socket()
server.bind(('localhost',9000))
server.listen(1000)

# 设置为非阻塞模式

server.setblocking(False) # 不阻塞



inputs=[server]
outputs=[]



while True:
  readable,writeable,exceptional=select.select(inputs,outputs,inputs)

  print(readable,writeable,exceptional)
  for r in readable:
    if r is server: # 如果是server 代表来了一个新连接
      conn,addr=server.accept()
      print("来了个新连接",addr)
      inputs.append(conn)   # 是应为这个新建立的连接还没发数据过来，现在就接受的话程序就要报错
         # 所以要想实现这个客户端发数据来时，server端能知道，就需要让select再监测这个conn
    else:  # 如果是之前的conn 表示发数据了
      data=r.recv(1024)
      print("收到数据",data)
      r.send(data)
      print("send done..")
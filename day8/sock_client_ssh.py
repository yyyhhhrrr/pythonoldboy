#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import  socket

client=socket.socket()
client.connect(("localhost",9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd)==0:
        continue

    client.send(cmd.encode("utf-8"))

    cmd_res_size = client.recv(1024) # 接收命令结果的长度
    print("命令结果大小",cmd_res_size)
    client.send("准备好接受了".encode("utf-8"))
    received_size=0
    received_data=b''
    while received_size < int(cmd_res_size.decode()):
        data=client.recv(1024)
        received_size+=len(data) # 每次收到的有可能小于1024 所以必须用len判断
        received_data+=data
        print(received_size)
        ##print(data.decode())
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())
    # cmd_res=client.recv(1024)
    # print(cmd_res.decode())

client.close
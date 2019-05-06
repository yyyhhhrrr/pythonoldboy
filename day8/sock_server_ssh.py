#!/usr/bin/env python
# coding:utf-8
# Author:Yang
# 减半ssh

import socket,os
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
        print("执行指令",data)
        cmd_res=os.popen(data.decode()).read() # 接收字符串 执行结果也是字符串
        print("before send",len(cmd_res))
        if len(cmd_res)==0:
            cmd_res="cmd has no output..."
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))  # lenth 是整数 不能直接encode 所以要先str 在encode
        # 这是一个坑：注意上面len(cmd_res.encode()) 因为len("中")为1，必须要再encode才能获得字节数 ，一个中文三个字节！！
        # time.sleep(0.5)
        client_ack=conn.recv(1024) # wit client to confirm  这个方法用来防止socket粘包

        conn.send(cmd_res.encode("utf-8"))

server.close

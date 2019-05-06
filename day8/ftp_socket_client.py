#!/usr/bin/env python
# coding:utf-8
# Author:Yang


import socket
import hashlib
client=socket.socket()
client.connect(("localhost",9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd)==0:continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024) # 收到文件大小
        print("server response:",server_response)
        client.send(b"ready to recv file")
        file_total_size=int(server_response.decode())
        received_size=0
        filename = cmd.split()[1]
        f = open(filename+".new","wb")
        m = hashlib.md5()
        while received_size < file_total_size:
            if file_total_size-received_size > 1024: # 要收不止一次
                size = 1024
            else: # 最后一次了，剩多少收多少，如果还是1024 容易把服务器传来的多余数据收了（解决黏包）
                size=file_total_size-received_size
                print("last receive:",size)
            data=client.recv(size)
            print(data)
            received_size+=len(data)
            f.write(data)
            m.update(data)
                # print(file_total_size,received_size)
        else:
            new_file_md5 = m.hexdigest()
            print("file recv done...",received_size,file_total_size)
            f.close()
        server_file_md5=client.recv(1024)
        print("server file md5:",server_file_md5)
        print("new file md5:",new_file_md5)

client.close
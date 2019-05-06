#!/usr/bin/env python
# coding:utf-8
# Author:Yang


import socket
import time

'''引入'''
def handle_requests(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK \r\n\r\n",encoding='utf-8'))
    # client.send(bytes("<h1 style='background-color:red;'>Hello world<h1>",encoding='utf-8'))
    f=open('index.html','rb')
    data = f.read()
    f.close()

    client.send(data)

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)

    while True:
        connection,address=sock.accept()
        handle_requests(connection)
        connection.close()


if __name__== '__main__':
    main()
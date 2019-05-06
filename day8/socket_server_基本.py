#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import socketserver


# 多并发socketserver基本写法
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):# 跟客户端每个请求都在handle 父类里handle（） 为空

        while True:
            try:
                self.data=self.request.recv(1024).strip() # 必须要是self.request
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                # if not self.data: # 客户端断了之后  python2.x 是断开没有异常的 3.x有自带的异常 要抓住
                #     print(self.client_address,"断开了")
                #     break
                self.request.send(self.data.upper())
            except ConnectionError as e:
                print(e)
                break


if __name__=='__main__':
    HOST,PORT="localhost",9999
    # 多并发
    server=socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler) # 多线程处理请求
    # server=socketserver.ForkingTCPServer((HOST,PORT),MyTCPHandler) 多进程处理请求， windows用不了

    # 单个请求
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler) 简化版单个请求

    server.serve_forever()
#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import paramiko

transport = paramiko.Transport(('172.16.95.132',22)) # transport 实例
transport.connect(username='root',password='960314') # 建立连接

sftp=paramiko.SFTPClient.from_transport(transport)
sftp.put('note1.txt','/root/1.txt') # 上传
# sftp.get('/root/1.txt','note2.txt') # 下载

transport.close()


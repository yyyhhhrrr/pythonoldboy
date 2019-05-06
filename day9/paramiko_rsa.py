#!/usr/bin/env python
# coding:utf-8
# Author:Yang


# 基于密钥的登录
import paramiko



#  例如想要在windows上尝试密钥登录 在linux上执行 sz /root/.ssh/id_rsa 就能拷贝到windows本地 ，使用paramiko_rsa.py里登录
# 172.16.95.132的私钥
private_key=paramiko.RSAKey.from_private_key_file('id_rsa.txt')
# 创建ssh对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts 文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# 连接服务器
ssh.connect(hostname='172.16.95.132',port=22,username='root',pkey=private_key)

# 执行命令
stdin,stdout,stderr= ssh.exec_command('ls')
res,err=stdout.read(),stderr.read()
result = res if res else err
# 获取命令结果
# result =stdout.read()
print(result.decode())

# 关闭连接
ssh.close()

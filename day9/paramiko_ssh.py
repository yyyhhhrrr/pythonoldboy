#!/usr/bin/env python
# coding:utf-8
# Author:Yang


# 基于用户名密码登录 不安全
import paramiko
# 创建ssh对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts 文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# 连接服务器
ssh.connect(hostname='172.16.95.132',port=22,username='root',password='960314')

# 执行命令
stdin,stdout,stderr= ssh.exec_command('sh start_tomcat.sh')
res,err=stdout.read(),stderr.read()
result = res if res else err
# 获取命令结果
# result =stdout.read()
print(result.decode())

# 关闭连接
ssh.close()

#!/usr/bin/env python
# coding:utf-8
# Author:Yang


'''有选择接收 direct producer端'''

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                        exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
# argv[1]表示第一个参数，如果没有参数 则默认发送'info':helloworld
# 如果有一个参数以上，第一个参数是发送的类型 例如"error"，第二个参数到后面都是message

message=''.join(sys.argv[2:]) or 'hello world'

channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,
    body=message
)

print("[x] sent %r:%r"%(severity,message))
connection.close()

# producer 发送消息 并带上该消息的类型
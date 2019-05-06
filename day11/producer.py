#!/usr/bin/env python
# coding:utf-8
# Author:Yang

'''send端'''

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel=connection.channel()  # 申明一个管道

# 申明queue
channel.queue_declare(queue='hello',durable=True) # 队列持久化

channel.basic_publish(
    exchange='',
    routing_key='hello',# queue名字
    body='Hello world!',
    properties = pika.BasicProperties(
        delivery_mode=2 , # 消息持久化
    )
)

print("[x] sent 'Hello world!'")
connection.close()
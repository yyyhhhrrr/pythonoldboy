#!/usr/bin/env python
# coding:utf-8
# Author:Yang



'''fanout 订阅广播producer'''
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel=connection.channel()

channel.exchange_declare(exchange='logs', # 声明exchange类型
                         exchange_type='fanout')
# 在producer端不用制定队列名字 因为queue是绑定到exhcange上的，且queue的名字是随机的
message="info:hello world!"

channel.basic_publish(
    exchange='logs',
    routing_key='',# 不用制定queue的名字
    body=message
)

print("[x] Sent %r"%message)
connection.close()
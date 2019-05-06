#!/usr/bin/env python
# coding:utf-8
# Author:Yang


''' rpc server rpc服务的服务端'''
import pika
import time
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost',5672,'/',credentials))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue') # 同样声明 从rpc_queue里收到要server端处理的数据


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body): # 回调函数 收到client端发来的信息进行处理，处理完之后时调用就给client发结果了
    n=body.decode()

    print(" [.] fib(%s)" % n)
    response = n

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,  # 获取client传来的props里定义的返回结果使用的queue (client props属性里reply_to的一个随机queue）
                     properties=pika.BasicProperties(correlation_id= props.correlation_id), # 获取client里传来props里的随机id
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag) # server端处理完消息要给client发一个确认



channel.basic_consume(on_request, queue='rpc_queue')


print(" [x] Awaiting RPC requests")
channel.start_consuming()
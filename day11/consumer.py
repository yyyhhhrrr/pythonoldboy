#!/usr/bin/env python
# coding:utf-8
# Author:Yang


'''receive端'''
'''消息公平分发'''


import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)


channel=connection.channel()

channel.queue_declare(queue='hello',durable=True) # 为什么还要声明？因为不知道消费者和生产者谁先启动，所以要避免出错才声明


def callback(ch,method,properties,body):
    print(ch,method,properties)
    print(method)
    print("[x] Received %r"%body)

    ch.basic_ack(delivery_tag=method.delivery_tag) # 手动确认消息

channel.basic_qos(prefetch_count=1) # 告诉producer 等我处理完这一条 再给我发下一条 实现消息公平分发（可能因为这个配置不高的消费者处理不完那么多消息而堆积）
channel.basic_consume( # 消费消息
                      callback, # 如果收到消息，就调用CALLBACK函数来处理消息 (回调函数)
                      queue='hello'
                      # no_ack=True # no acknowledgement  消息处理完了之后，不给producer 说
                      # 保留no_ack=True 就是不确认  producer 不关心consumer是否处理完消息
                      # 一般默认是要确认，且最好不用 no_ack，因为如果consumer断了，producer好把消息作为新消息给下一个queue处理实现消息轮询
)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming() # 开始收（一直收）
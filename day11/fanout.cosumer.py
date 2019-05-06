#!/usr/bin/env python
# coding:utf-8
# Author:Yang


'''fanout订阅广播consumer'''
import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.exchange_declare(exchange='logs',   # 声明 exchange类型
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True) # exclusive(排他)参数是指不用指定queue的名字，rabbit会随机分配一个名字，在消费者断开后，自动将queue删除

queue_name=result.method.queue  # 拿到queue的名字
print('random queue_name',queue_name)

channel.queue_bind(exchange='logs', # 将queue绑定exchange
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

# 如果consumer没有运行 是收不到producer的消息的，就像广播，没有打开收音机就听不到
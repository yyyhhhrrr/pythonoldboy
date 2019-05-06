#!/usr/bin/env python
# coding:utf-8
# Author:Yang


'''有选择接收 direct consumer端'''
import sys
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                        exchange_type='direct')

result=channel.queue_declare(exclusive=True)  # 随机queue

queue_name=result.method.queue

severities=sys.argv[1:] # 设置的运行参数 去除掉py文件名本身  （发送命令格式例如 python direct_consumer.py waring error）
                                                                         # severities就是[warning,error]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(
        exchange='direct_logs',
        queue=queue_name,
        routing_key=severity
    )

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

# consumer 定义从queue收到消息的类型，然后只收该类型消息，消息类型是一个list
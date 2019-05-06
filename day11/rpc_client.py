#!/usr/bin/env python
# coding:utf-8
# Author:Yang

''' rpc client rpc服务的客户端'''
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', self.credentials))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True) # server端执行完的结果 用一个随机生成的queue接收（就是callback_queue）
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,# 用来收server端执行的结果 on_response 是回调函数，收到消息则执行
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):# 回调函数
        if self.corr_id == props.correlation_id: # 如果client端生成的随机id与server端返回的随机id一致 则将返回的消息赋给body
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())   # uuid模块，调用uuid.uuid4() 可以生成一个唯一的随机id
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',  # 发送数据的时候使用rpc_queue
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,  # props里制定了server端执行完要返回结果通过的queue为上面随机生成的queue
                                       correlation_id=self.corr_id,  # 带上生成的随机id为参数
                                   ),
                                   body=n)
        while self.response is None:
            self.connection.process_data_events()  # 这句是死循环接受server返回的信息，没有结果不用一直等待，是表示使用非阻塞式的connection.start_consuming
            print("no msg..")
        return self.response.decode()


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call('a')
print(" [.] Got %r" % response)
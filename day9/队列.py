#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import queue

# q=queue.Queue(maxsize=2)
# q=queue.LifoQueue()
# q.put("d1")
# q.put("d2")
#
# print(q.qsize())
# print(q.get())
# print(q.get())

q=queue.PriorityQueue()

q.put((-1,"a"))
q.put((10,"yang"))
q.put((3,"b"))
q.put((6,"c"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
#!/usr/bin/env python
# coding:utf-8
# Author:Yang

class Dog:
    def __init__(self,name):
        self.name = name
    def bulk(self):
        print("%s:aa"%self.name)

d1 = Dog("x")
d2 = Dog("y")
d3 = Dog("z")

d1.bulk()
d2.bulk()
d3.bulk()
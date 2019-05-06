#!/usr/bin/env python
# coding:utf-8
# Author:Yang

class Animal:
    def __init__(self,name):
        self.name=name

    def talk(self):
        pass
    @staticmethod
    def animal_talk(obj):  # 一种接口 多种实现
        obj.talk()

class Cat(Animal):
    def talk(self):
        print( "Meow")

class Dog(Animal):
    def talk(self):
        print( "Woof")



d=Dog("yang")
# d.talk()
# animal_talk(d)
c=Cat("hao")
# c.talk()
# animal_talk(c)


# python 没有直接语法支持多态，但是可以间接
Animal.animal_talk(c) # 多态：同一种接口，多种实现
Animal.animal_talk(d)
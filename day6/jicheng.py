#!/usr/bin/env python
# coding:utf-8
# Author:Yang

# class People:经典类
class People(object): # 新式类  多继承方式变了
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("%s is eating.."%self.name)
    def sleep(self):
        print("%s is sleeping.."%self.name)
    def talk(self):
        print("%s is talking.."%self.name)
    def __fuck(self): # 私有方法继承不了
        pass

class Relation(object):
    def make_friends(self,obj): #
        print("%s is making friends with %s"%(self.name,obj.name))
        self.friends.append(obj.name)





class Man(People): # 继承people
    def __init__(self,name,age,money): # 对构造函数进行重构（man多加参数） name,age在父类实现（所有默认参数都要写），money在子类实现
        # People.__init__(self,name,age) 第一种方法
        super(Man, self).__init__(name,age) # 第二种方法 super去继承父类构造函数 优点:当people改变时在字方法里不用写people,多继承时只用写一个super
        self.money=money  # super是新式类的写法 当多继承时 super只写一个是因为只有继承一个构造方法__init__
        print("%s 元"%money)
    def piao(self):
        print("%s is piaoing.."%self.name)
    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Woman(People,Relation): # 多继承people、Realtion 当ralation里没构造方法时去people里找，不管relation在前还是在后,但relation和people都有__init__时只找最左边的那个
    def get_birth(self):
        print("%s is born a baby.."%self.name)
m1 = Man("yang",22,10)
m1.eat()
m1.sleep()
m1.talk()
m1.piao()

w1 = Woman("A",22)
w1.eat()
w1.sleep()
w1.get_birth()
w1.make_friends(m1)


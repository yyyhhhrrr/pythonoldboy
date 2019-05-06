#!/usr/bin/env python
# coding:utf-8
# Author:Yang

class Role(object):

    n=123 # 类变量
    name = "我是类name"
    def __init__(self,name,role,weapon,life_value=100,money=15000): # 将属性存入内存
        # 构造函数
        # 在实例化时做一些类的初始化的工作
        self.name=name  # 实例变量（静态属性），作用域就是实例本身
        self.role=role
        self.weapon=weapon
        self.__life_value=life_value # 私有属性
        self.money=money
    # 类的方法，功能（动态属性）
    def got_shot(self):
        print("i got shot")
    def buy_gun(self,gun_name):
        print("%s just buy %s"%(self.name,gun_name))

        # 析构函数:在实例释放、销毁（程序结束）的时候自动执行的，通常用于做一些收尾工作，如关闭一些数据库连接或关闭打开的临时文件等
    def show_status(self):
         print("name:%s life_value:%s"%(self.name,self.__life_value))
    def __shot(self):# 私有方法
        pass
    def __del__(self):
        print("%s 彻底死了..."%self.name)
r1=Role("yang","police","ak47") # 把一个类变成一个具体对象的过程叫实例化（初始化一个类，造了一个对象）
r1.buy_gun("ak47") # r1又叫做Role的实例
r2=Role("hao","terrorist","awm")
print(Role.name)
print(r2.n,r2.name)
r1.bullet_prove=True # 增加
# del r1.bullet_prove # 删除
print(r1.n,r1.name,r1.bullet_prove) # 先找实例本身，再到类里面找
r1.n="改的类变量"
print(r1.n)
# 所谓的改类变量 相当于是在实例内存里创建一个新n
print(r2.n) # 所以r2内存里没n，就去类的内存里找

print(r1.show_status())# 私有属性只能在类内部访问，不能在外部访问

# 为何有self?:
# 调用函数 -》 执行 -》 返回结果
# 实例化的时候 在一般思维下 应该是这种方式：r1 = Role.__init__(..,...) return x3434(内存地址)
# 实际上是这种方式：
# r1=Role(r1,"alex","police","15000")
# r1.name=...
# 用文字描述就是 先给类传值，类去开辟一块新内存，类往里面存传过来的值，同时r1也传进去了（__init__函数），因为类要让r1把参数记录下，所以
# 就把r1传进去，给r1赋值（实例化）
# 在调用类的方法时 比如r1.buy_gun() 相当于就是Role.buy_gun(r1) 因为要告诉类是谁在调用方法才好把函数的结果传给谁，所以
# 类的每个方法必须至少传入这个实例化的对象，且实例化调用的方法是类内存里的函数。



# 类变量的作用：所有实例共用的属性
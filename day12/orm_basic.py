#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import sqlalchemy


'''ORM框架基本写法'''
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker


engine =create_engine("mysql+pymysql://root:960314@localhost/pytest",
                      encoding='utf-8',echo=True) # echo=True 打印所有信息
# sqlalchemy 底层也是mysqld、pymsql、oracle等的封装

Base = declarative_base() # 生成orm基类

class User(Base):
    __tablename__='user' # 表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>"%(self.id,self.name)



Base.metadata.create_all(engine) # 创建表结构 把base下所有子类都创建了

# 创建数据
Session_class=sessionmaker(bind=engine) # 创建与数据库的会话session class，注意，这里返回给session的是个类，不是一个实例
Session=Session_class() # 生成session 实例

# 插入数据
# user_obj = User(name='yang',password='960314') # 生成你要创建的数据对象
# user_obj2 = User(name='hape',password='123456')
# print(user_obj.name,user_obj.id) # 此时还没创建对象，id还是none
#
# Session.add(user_obj) # 把要创建的数据对象添加到这个session里，一会统一创建
# Session.add(user_obj2)


# 查询数据
#data=Session.query(User).filter_by(name='yang').all() # 所有数据取成一个列表
data=Session.query(User).filter(User.id<10).filter(User.id>3).all() # 多条件查询
# filter_by不好用就用filter

print(data)  # data是一个装对象的列表
print(data[0].name,data[0].password)
Session.commit() # 现在才统一提交，创建数据


# Session.rollback() 回滚
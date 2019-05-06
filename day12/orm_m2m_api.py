#!/usr/bin/env python
# coding:utf-8
# Author:Yang


'''多对多关联api'''
from day12 import orm_m2m
from sqlalchemy.orm import sessionmaker


Session_class=sessionmaker(bind=orm_m2m.engine)
session=Session_class()

# b1=orm_m2m.Book(name="learn python",pub_date="2018-01-10")
# b2=orm_m2m.Book(name="learn linux",pub_date="2018-02-10")
# b3=orm_m2m.Book(name="learn java",pub_date="2018-03-10")
# session.add_all([b1,b2,b3])
# a1=orm_m2m.Author(name="yang")
# a2=orm_m2m.Author(name="zhangsan")
# a3=orm_m2m.Author(name="lisi")
#
# b1.authors=[a1,a3]
# b3.authors=[a1,a2,a3]
# session.add_all([a1,a2,a3])

# 注意如果 session.add_all([b1,b2,b3,a1,a2,a3]) b3有可能比b2先创建 就会打乱b3和b2的顺序

author_obj=session.query(orm_m2m.Author).filter(orm_m2m.Author.name=="yang").first()
print(author_obj.books) # 返回的是一个对象的列表
print(author_obj.books[1].pub_date)

# book_obj=session.query(orm_m2m.Book).filter(orm_m2m.Book.id==6).first()
# print(book_obj.authors)
session.commit()


# 删除数据时 orm会自动删除，不用管中间表

# 要想写中文 在 engine =create_engine("mysql+pymysql://root:960314@localhost/pytest",encoding='utf-8',echo=True) 写了encoding还不管用
# 必须要写成“mysql+pymysql://root:960314@localhost/pytest？charset=utf8”
# 以后就直接写“mysql+pymysql://root:960314@localhost/pytest？charset=utf8” 不用写encoding了
#!/usr/bin/env python
# coding:utf-8
# Author:Yang


'''多对多关联'''
'''一本书可以有多个作者，一个作者又可以出版多本书'''

from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine =create_engine("mysql+pymysql://root:960314@localhost/pytest",
                      encoding='utf-8',echo=True)



Base = declarative_base()

# 创建中间表(使用的是一种很少用的建表方式，不用类的方式创建，是因为用户不用关心这个表)
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)

    authors = relationship('Author',secondary=book_m2m_author,backref='books') # 允许author对象调books
                                                                                    # book对象调authors

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


Base.metadata.create_all(engine)
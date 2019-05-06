#!/usr/bin/env python
# coding:utf-8
# Author:Yang



'''多外键关联'''
from sqlalchemy import create_engine, Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine =create_engine("mysql+pymysql://root:960314@localhost/pytest",
                      encoding='utf-8',echo=True)


Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer, ForeignKey("address.id")) # 账单地址
    shipping_address_id = Column(Integer, ForeignKey("address.id")) # 邮寄地址

    billing_address = relationship("Address",foreign_keys=[billing_address_id])
    shipping_address = relationship("Address",foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))


    def __repr__(self):
        return self.street
Base.metadata.create_all(engine)

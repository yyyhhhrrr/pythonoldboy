#!/usr/bin/env python
# coding:utf-8
# Author:Yang

'''建立外键'''
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship


engine =create_engine("mysql+pymysql://root:960314@localhost/pytest",
                      encoding='utf-8',echo=True)

Base = declarative_base()

class Student(Base):
    __tablename__="student"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    register_date=Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name:%s>" % (self.id,self.name)


class StudyRecord(Base):
    __tablename__="study_record"
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status=Column(String(32),nullable=False)
    stu_id=Column(Integer,ForeignKey("student.id")) # 创建外键


    # 建立关系
    student = relationship("Student",backref="my_study_record") # 这个nb,允许你在student表里通过backref 字段反向查出所有它在student_recprd里的信息,也可以反查
    # ORM将两个对象关联起来，互相调用,在内存里的关联关系而不是数据库
    # 注意！！！relationship的第一个参数是类！！！比如说上面的Student类！！
    # 上面相当于 student=query(Student).filter(Student.id==stu_obj.stu_id.first())
    def __repr__(self):
        return "<%s day:%s status:%s>" % (self.student.name,self.day,self.status)

Base.metadata.create_all(engine)

Session_class=sessionmaker(bind=engine)
session=Session_class()
#
# s1 = Student(name="yang",register_date="2018-12-03")
# s2 = Student(name="lisi",register_date="2016-12-03")
# s3 = Student(name="zhangsan",register_date="2017-12-03")
# s4 = Student(name="wangwu",register_date="2018-09-03")
#
# study_obj1=StudyRecord(day=1,status="yes",stu_id=1)
# study_obj2=StudyRecord(day=2,status="no",stu_id=1)
# study_obj3=StudyRecord(day=3,status="yes",stu_id=1)
# study_obj4=StudyRecord(day=1,status="yes",stu_id=2)
#
# session.add_all([study_obj1,study_obj2,study_obj3,study_obj4])

name_List=[]
stu_obj=session.query(Student.name,Student.id).all() # first()是一个对象 list()是一个对象的列表
for i in range(len(stu_obj)):
    name_List.append(stu_obj[i][0]+",id:"+str(stu_obj[i][1]))
print(stu_obj)
print(name_List) # stu_obj 通过my_study_record 反查 多条上课数据，学生和上课数据是一对多的关系。
# 注意返回值是反查出的student_record对象的返回值
session.commit()
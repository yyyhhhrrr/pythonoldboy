#!/usr/bin/env python
# coding:utf-8
# Author:Yang
class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.students=[]
        self.teachers=[]

    def enroll(self,stu_obj):   # 注册
        print("为学员%s办理注册手续"%stu_obj.name)
        self.students.append(stu_obj)
    def hire(self,stuff_obj): # 雇佣老师
        self.teachers.append(stuff_obj)
        print("为老师%s办理雇佣手续"%stuff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course): # 重构
        super(Teacher,self).__init__(name,age,sex)
        self.salary=salary
        self.course=course
    def tell(self):
        print('''
        --------- info of Teacher------
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching course[%s]"%(self.name,self.course))
class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student, self).__init__(name,age,sex)
        self.stu_id=stu_id
        self.grade=grade
    def tell(self):
        print('''
        ------------ info of Student-------
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        '''%(self.name,self.age,self.sex,self.stu_id,self.grade))
    def pay_tuition(self,amount): # 交学费
        print("%s has paid tution for $%s"% (self.name,amount))

school = School("A大学","春熙路")

t1=Teacher("B老师",40,"M",200000,"Linux")
t2=Teacher("C老师",40,"F",1500,"PythonDevOps")

s1=Student("YangHaoran",22,"M",1001,"PythonDevOps")
s2=Student("Zhangsan",22,"F",1002,"Linux")

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.teachers)

school.teachers[0].teach() # 教课

for stu in school.students:
    print(stu.pay_tuition(5000))
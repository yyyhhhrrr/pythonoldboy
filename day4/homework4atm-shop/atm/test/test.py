#!/usr/bin/env python
# coding:utf-8
# Author:Yang
from db import dbtool

def login(auth_type):
    def outwrapper(func):
        def wrapper(*args,**kwargs):
            user_id = kwargs['id']
            print(user_id)
            user_pwd = kwargs['password']
            if auth_type == "user":
                user_data=dbtool.read_json(user_id)
                print(user_data['id'])
                if user_id == user_data['id']:
                    if user_pwd == user_data['password']:
                        func(*args,**kwargs)
                        return user_data
                    else:
                        print("error password")
                        print(1)

                else:
                    print("the user_id is not exist,please call ATM-manager")
                    print(2)

            else :
                user_data=dbtool.read_manager(user_id)
                if user_id == user_data['id']:
                    if user_pwd == user_data['password']:
                        func(*args,**kwargs)
                        return user_data
                    else:
                        print("error password")
                        print(1)

                else:
                     print("error manager")
                     print(2)

        return  wrapper
    return outwrapper

@login(auth_type="user")
def test(*args,**kwargs):
    user_id = kwargs['id']
    user_password = kwargs['password']
    print('a')

@login(auth_type="manager")
def test2(*args,**kwargs):
    user_id = kwargs['id']
    user_password = kwargs['password']
    print('b')


print(test(id=10000,password="960314"))
test2(id=123456,password="123456")
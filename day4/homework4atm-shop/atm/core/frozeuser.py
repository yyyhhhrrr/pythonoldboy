#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from db import  dbtool
def froze_user():
    user_id = int(input("请输入要管理的用户id:"))
    user_data = dbtool.read_json(user_id)
    if user_data['status']==0:
        print("当前用户状态:正常")
    else:
        print("当前用户状态:冻结")
    user_status = int(input("请输入用户的状态:"))
    if user_data['status'] == 0:
        if user_status =="冻结":
           user_data['status']==1
        else:
            print("当前状态重复")
    else:
        if user_status=="正常":
            user_data['status']==0
        else:
            print("当前状态重复")

    dbtool.write_json(user_data)
    print("修改成功")

#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from db import dbtool
def manage_credit():

    user_id=int(input("请输入要管理的用户id:"))
    user_data=dbtool.read_json(user_id)
    print("%s用户当前总额度为:\033[31;1m%s\033[0m")%(user_id,user_data['s_credit'])
    s_credit=int(input("请输入要更改的额度:"))
    user_data['s_credit']=s_credit
    dbtool.write_json(user_data)
    print("更改成功")

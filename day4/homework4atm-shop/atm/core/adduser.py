#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import datetime
import time
from db import dbtool
def add_user():
    user_id=int(input("请输入添加的用户Id:"))
    user_pwd=input("请输入添加的用户密码:")
    user_s_credit=0
    user_credit=0
    user_balance=0
    time_format="%Y-%m-%d"
    start_date =time.strftime(time_format)
    end_date=datetime.datetime.now()+datetime.timedelta(days=365)
    user_status = 0
    user_data={
        'id':user_id,
        'password':user_pwd,
        's_credit':user_s_credit,
        'credit':user_credit,
        'balance':user_balance,
        'start_date':str(start_date),
        'end_date':str(end_date),
        'status':user_status


    }
    dbtool.write_json(user_data)
    print('添加用户成功')

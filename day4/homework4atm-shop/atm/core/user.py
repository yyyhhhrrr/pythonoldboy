#!/usr/bin/env python
# coding:utf-8
# Author:Yang


def user_information(user_data):
    user_id=user_data['id']
    user_s_credit=user_data['s_credit']
    user_credit=user_data['credit']
    user_balance=user_data['balance']
    start_date=user_data['start_date']
    end_date=user_data['end_date']
    status=user_data['status']

    print("你的id:",user_id)
    print("你的初始额度:",user_s_credit)
    print("你的可用额度:",user_credit)
    print("你的余额:",user_balance)
    print("开户时间:",start_date)
    print("到期时间:",end_date)
    if status == 0:
       print("信用卡状态:正常")
    elif status == 1:
       print("信用卡状态:被冻结")
    else:
       print("信用卡状态:不存在")

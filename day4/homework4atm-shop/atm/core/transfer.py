#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from db import dbtool
from core import bill
def tansfer_accounts(user1_data):
    user1_balance=user1_data['balance']
    print("你的账户余额为\033[31;1m%s\033[0m元"%user1_balance)
    user2_id = int(input("请输入你要转账的账户:"))
    if dbtool.read_json(user2_id) ==2:
        print("账户%s不存在，请重新输入"%user2_id)
        tansfer_accounts(user1_data)
    else:
        if dbtool.read_json(user2_id) ==1:
            print("账户%s已被冻结，请重新输入"%user2_id)
            tansfer_accounts(user1_data)
        else:
            trans_money = int(input("请输入你要转账的金额:"))
            user2_data = dbtool.read_json(user2_id)
            user2_balance = user2_data['balance']
            if trans_money > user1_data['balance']:
                print("你的账户余额不足，不能转账")
            else:
                user1_balance -= trans_money
                user1_data['balance'] = user1_balance
                user2_balance += trans_money
                user2_data['balance'] = user2_balance
                dbtool.write_json(user2_data)
                print("转账\033[31;1m%s\033[0m元成功，账户余额为\033[31;1m%s\033[0m元"%(trans_money,user1_balance))
                bill.bill(user1_data,3,trans_money,user2_id=user2_id)
    return user1_data


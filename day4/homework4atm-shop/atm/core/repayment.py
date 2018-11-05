#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from core import bill

def repay(user_data):
    user_s_credit = user_data['s_credit']
    user_credit = user_data['credit']
    user_balance = user_data['balance']

    if user_s_credit == user_credit:
        print("你的可用额度已是最高，不能继续还款")
    else:
        money = int(input("请输出你要还款的金额:"))
        user_credit+=money
        user_data['credit'] = user_credit
        print("还款成功，还款金额\033[31;1m%s\033[0m元，行用卡可用额度\033[31;1m%s\033[0m"%(money,user_credit))
        bill.bill(user_data,1,money)
    return user_data


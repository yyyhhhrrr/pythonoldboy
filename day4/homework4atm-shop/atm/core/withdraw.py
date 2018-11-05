#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from core import main
from core import bill
def withdarw(user_data):
    user_balance = user_data['balance']
    user_s_credit = user_data['s_credit']
    user_credit = user_data['credit']
    print("你的余额为\033[31;1m%s\033[0m元\n信用卡可用额度为\033[31;1m%s\033[0m元\n信用卡总额度为\033[31;1m%s\033[0m元"%(user_balance,user_credit,user_s_credit))
    print("1.余额取款\n2.信用卡取款\n3.返回主界面")
    choice = int(input("请选择你要取款的方式:"))
    money = int(input("请输入你要取款的金额:"))
    if choice == 1:
        if user_balance >=money:
            user_balance -= money
            user_data['balance'] = user_balance
            print("取款\033[31;1m%s\033[0m元成功，账户余额\033[31;1m%s\033[0m元"%(money,user_balance))
            bill.bill(user_data,2,money,choice=1)
        else:
            print("你的余额已不足取现，请使用信用卡额度取款")
    elif choice == 2:
        if user_credit >=money:
            user_credit -= money
            user_data['credit'] = user_credit
            print("取款\033[31;1m%s\033[0m元成功，行用卡可用额度\033[31;1m%s\033[0m元"%(money,user_credit))
            bill.bill(user_data,2,money,choice=2)
        else:
            print("你的信用卡可用额度已不足，不能取款")
    else:
        main.main_view(user_data)

    return  user_data




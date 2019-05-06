#!/usr/bin/env python
# coding:utf-8
# Author:Yang


from db import dbtool
from core import user
from core import repayment
from core import withdraw
from core import transfer
from core import bill
from core import adduser
from core import manage_credit
from core import frozeuser
from core import logger
import sys

def start_atm():
    print("ATM-Login".center(60,'-'))
    user_id = int(input("please input your ATM-Card ID:"))
    user_pwd = input("please input your password:")
    login_type = input("请选择登录身份:（用户/管理员）")
    return user_id,user_pwd,login_type

# def login(user_id,user_pwd):
#     user_data=dbtool.read_json(user_id)
#     if user_id == user_data['id']:
#         if user_pwd == user_data['password']:
#                 main_view(user_data)
#         else:
#                 print("error password")
#                 start_atm()
#     else:
#             print("the user_id is not exist,please call ATM-manager")
#             start_atm()
#     return user_data

def login(auth_type):
    def outwrapper(func):
        def wrapper(*args,**kwargs):
            user_id = kwargs['id']
            user_pwd = kwargs['password']
            if auth_type == "user":
                user_data=dbtool.read_json(user_id)
                if user_id == user_data['id']:
                    if user_pwd == user_data['password']:
                        func(*args,**kwargs)
                        return user_data
                    else:
                        print("error password")
                        start_atm()
                else:
                    print("the user_id is not exist,please call ATM-manager")
                    start_atm()
            else :
                user_data=dbtool.read_manager(user_id)
                if user_id == user_data['id']:
                    if user_pwd == user_data['password']:
                        func(*args,**kwargs)
                        return user_data
                    else:
                        print("error password")
                        start_atm()
                else:
                     print("error manager")
                     start_atm()
        return  wrapper
    return outwrapper

@login(auth_type="manager")
def admin_view(*args,**kwargs):
    user_id=kwargs['id']
    user_password=kwargs['password']
    user_data=dbtool.read_manager(user_id)
    print('''
    --------login sucess!-----------------
    --------Welcome to the yang's bank----
    --------Welcome admin-----------------
    \033[31;1m 1.添加用户
     2.管理用户额度
     3.冻结账户
     4.退出\033[0m
    ''')
    admin_choice(user_data)




@login(auth_type="user")
def main_view(*args,**kwargs):
    user_id=kwargs['id']
    user_password=kwargs['password']
    user_data=dbtool.read_json(user_id)
    print('''
    --------login sucess!-----------------
    --------Welcome to the yang's bank----
    \033[31;1m  1.账户信息
     2.还款
     3.取款
     4.转账
     5.账单
     6.退出\033[0m
    ''')
    choice(user_data)



def choice(user_data):
    user_choice = int(input("please input your choice:"))
    if user_choice == 1:
        user.user_information(user_data)

    elif user_choice == 2:
        dbtool.write_json(repayment.repay(user_data))

    elif user_choice == 3:
        dbtool.write_json(withdraw.withdarw(user_data))
    elif user_choice == 4:
        dbtool.write_json(transfer.tansfer_accounts(user_data))
    elif user_choice == 5:
        bill.read_bill(user_data['id'])
    elif user_choice == 6:
        print("good bye")
        sys.exit(0)
    else:
        print("请输入正确的操作符")

    user_quit = int(input("请选择操作:1.返回主界面 2.退出ATM :"))
    if user_quit == 1:
        main_view(user_data)
    else:
        print("goodbye")
        sys.exit(0)



def admin_choice(user_data):
    user_choice = int(input("please input your choice:"))
    if user_choice == 1:
        adduser.add_user()
    elif user_choice == 2:
        manage_credit.manage_credit()
    elif user_choice ==3:
        frozeuser.froze_user()
    elif user_choice == 4:
        sys.exit(0)
    else:
        print("chocie error")
    user_quit = int(input("请选择操作:1.返回主界面 2.退出ATM :"))
    if user_quit == 1:
        admin_view(user_data)
    else:
        print("goodbye")
        sys.exit(0)




def run():
    # tuple=start_atm()
    # # login(tuple[0],tuple[1])
    # user_id=tuple[0]
    # user_pwd=tuple[1]
    # login_type=tuple[2]
    user_id,user_pwd,login_type=start_atm()
    if login_type == "用户":
        main_view(id=user_id,password=user_pwd)
    elif login_type =="管理员":
        admin_view(id=user_id,password=user_pwd)
    else:
        print("error login_type")



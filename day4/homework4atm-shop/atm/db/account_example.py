#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from db import dbtool

# acc_dic={
#     'id': 10000,  # 用户id
#     'password': '960314',  # 用户密码
#     's_credit' : 20000,
#     'credit': 20000,  # 用户信用卡可用额度
#     'balance': 7000,  # 用户信用卡余额
#     'start_date': '2018-11-01',  # 用户开户日期
#     'end_date': '2023-11-01',  # 用户信用卡到期日期
#     'status': 0 # 信用卡状态 0 正常 1 被冻结 2 不存在
# }

# acc_dic2={
#     'id': 10001,  # 用户id
#     'password': '960314',  # 用户密码
#     's_credit' : 20000,
#     'credit': 20000,  # 用户信用卡可用额度
#     'balance': 10000,  # 用户信用卡余额
#     'start_date': '2018-11-02',  # 用户开户日期
#     'end_date': '2023-11-02',  # 用户信用卡到期日期
#     'status': 0 # 信用卡状态 0 正常 1 被冻结
# }

acc_dic3={
    'id':123456, # 管理员id
    'password':'123456' # 管理员密码
}


print(dbtool.write_manager(acc_dic3))

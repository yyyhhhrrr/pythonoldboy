#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from bin import atm
import time
def write_bill(user_id,user_operation):
    with open(atm.base_dir+"\\db\\bill\\%s_bill.txt"%user_id,"a+",encoding="utf-8") as f:
        f.write(user_operation)
    f.close()

def bill(user_data,operation,money,**kwargs):
    time_format="%Y-%m-%d %X"
    time_current=time.strftime(time_format)
    if operation == 1: # 还款记录账单
        user_operation=time_current+"\n-----账户:%s"%user_data['id']+"----操作:还款"+"----还款%s元"%money+"----账户余额:%s"%user_data['balance']+"----账户可用额度:%s"%user_data['credit']+"----账户总额度:%s"%user_data['s_credit']
        write_bill(user_data['id'],user_operation)
    elif operation == 2: # 取款记录账单
        choice=kwargs['choice']
        if choice == 1: # 账户余额取款
           user_operation=time_current+"\n-----账户:%s"%user_data['id']+"----操作:账户余额取款"+"----取款%s元"%money+"----账户余额:%s"%user_data['balance']+"----账户可用额度:%s"%user_data['credit']+"----账户总额度:%s"%user_data['s_credit']
           write_bill(user_data['id'],user_operation)
        else :
           user_operation=time_current+"\n-----账户:%s"%user_data['id']+"----操作:信用卡额度取款"+"----取款%s元"%money+"----账户余额:%s"%user_data['balance']+"----账户可用额度:%s"%user_data['credit']+"----账户总额度:%s"%user_data['s_credit']
           write_bill(user_data['id'],user_operation)

    elif operation == 3: # 转账记录账单
        user2_id=kwargs['user2_id']
        user_operation=time_current+"\n-----账户:%s"%user_data['id']+"----操作:转账"+"----目标账户:%s"%user2_id+"----转账%s元"%money+"----账户余额:%s"%user_data['balance']+"----账户可用额度:%s"%user_data['credit']+"----账户总额度:%s"%user_data['s_credit']
        write_bill(user_data['id'],user_operation)
    else:
        pass

def read_bill(user_id):
    with open(atm.base_dir + "\\db\\bill\\%s_bill.txt" % user_id, "r", encoding="utf-8") as f:
        for line in f:
             print(line)
    f.close()
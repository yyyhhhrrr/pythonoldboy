#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import json
from bin import atm

def read_json(user_id):
    try:
        with open(atm.base_dir+"\\db\\account\\%s.txt"%user_id,"r") as f:
            user_data=json.loads(f.read())
            if user_data['status'] == 0:
                return user_data
            else:
                return 1
        f.close()
    except FileNotFoundError as e:
        return 2

def write_json(user_data):
    with open(atm.base_dir+"\\db\\account\\%s.txt"%user_data['id'],"+w") as f:
        f.write(json.dumps(user_data))
    f.close()

def read_manager(user_id):
    try:
        with open(atm.base_dir+"\\db\\manager\\%s.txt"%user_id,"r") as f:
            user_data=json.loads(f.read())
            return user_data
        f.close()
    except FileNotFoundError as e:
        return 2

def write_manager(user_data):
    with open(atm.base_dir+"\\db\\manager\\%s.txt"%user_data['id'],"w+") as f:
        f.write(json.dumps(user_data))
    f.close()

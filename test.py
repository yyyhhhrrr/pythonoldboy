#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import requests
import os
import getpass


def interface_test(ip,port):

    url = "http://%s:%s/card/cardValidate"%(ip,port)
    payload = "{\"cardNum\":\"2787504611\",\"companyId\":\"181\"}"
    headers = {
        'Content-Type': "application/json",
        'token': "2951314e0796466EE5c36ae737566128",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text





#
# ip_list=["39.104.13.49"]
# port_list=["7001","7002"]
#
# interface_test(ip_list[0],port_list[0])
print(getpass.getuser())







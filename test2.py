#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from urllib import parse,request
import json
url="http://39.104.13.49:7002/card/cardValidate"

params={"cardNum":"2787504611","companyId":"181"}
headers = {
    'Content-Type': "application/json",
    'token': "2951314e0796466EE5c36ae737566128",
    'cache-control': "no-cache"
    }



def http_post(url, data_json,headers):
    jdata = json.dumps(data_json).encode()
    req = request.Request(url, jdata,headers)
    response = request.urlopen(req)
    return response.read()


res=http_post(url,params,headers).decode()
print(res)
#!/usr/bin/env python
# coding:utf-8
# Author:Yang
import getpass
_username = 'yang'
_password = 'abc123'
username = input("username:")
password = input("password:")

if _username == username and _password == password :
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password")

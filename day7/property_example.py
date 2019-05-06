#!/usr/bin/env python
# coding:utf-8
# Author:Yang

class Flight(object):
    def __init__(self,name):
        self.flight_name=name

    def checking_status(self):
        print("checking flight %s status "% self.flight_name)
        return 1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("flight got canceled..")
        elif status == 1:
            print("flight is arrived..")
        elif status == 2:
            print("flight has departured already..")
        else:
            print("cannot confirm the flight status...")
    @flight_status.setter
    def flight_status(self,status):
           print("%s has changed to %s"%(self.flight_name,status))

f=Flight("A389")
f.flight_status
f.flight_status="2"

# 隐藏实现细节

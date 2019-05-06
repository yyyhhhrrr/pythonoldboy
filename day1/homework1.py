#!/usr/bin/env python
# coding:utf-8
# Author:Yang

count = 0
list = []

with open("F:/homework1.txt") as f:
   for line in f.readlines():
       list.append(line.strip())

for dict in list:
    dict=eval(dict)
    while count < 4:
        username = input("please input your username:")
        password = input("please input your password:")

        if username in dict:
          if dict[username]==password:
            print("login success..")
            break
          else:
           count +=1
           print("第%d次失败，第三次失败账户将被锁定" % count)
           if count==3:
               print("第%d次失败，第三次失败账户将被锁定"%count)
           elif count==4:
               print("第三次失败，账户已被锁定")
               break

        else:
          count +=1
          if count <3:
            print("第%d次失败，第三次失败账户将被锁定" % count)
          else:
              print("第三次已失败，账户已被锁定")
              with open("F:/homework1error.txt","+w") as f2:
                f2.write("{'%s':'%s'}"%(username,password)+"\n")
                break








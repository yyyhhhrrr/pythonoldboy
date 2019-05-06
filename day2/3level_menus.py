#!/usr/bin/env python
# coding:utf-8
# Author:Yang

data={
    '北京':{
        '朝阳':{
            '北四环':['奥森','北信科']
        }
    }
}


exit_flag = False
while not exit_flag:
    for  i in data:
        print(i)
    choice = input('选择进入1>>:')
    if choice in data :
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input('选择进入2>>:')
            if choice2 in data[choice]:
                while not exit_flag:
                        for i3 in data[choice][choice2]:
                            print("\t",i3)
                        choice3 = input('选择进入3>>:')
                        if choice3 in data[choice][choice2]:
                            for i4 in data[choice][choice2][choice3]:
                                print("\t\t",i4)
                            choice4 = input('按b返回>>:')
                            if choice4 == 'b':
                                pass
                            elif choice4 == 'q':
                                exit_flag = True
                        if choice3 == 'b':
                           break
                        elif choice3 == 'q':
                            exit_flag = True
                if choice2 == 'b':
                    break
                elif choice2 == 'q':
                    exit_flag = True
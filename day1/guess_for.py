#!/usr/bin/env python
# coding:utf-8
# Author:Yang
age_of_oldboy = 56

count = 0
for count in range(3):
    if count == 3:
        break
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger...")
    count +=1
else:
    print("you have tried too many times...")

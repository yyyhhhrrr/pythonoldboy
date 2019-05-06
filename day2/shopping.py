#!/usr/bin/env python
# coding:utf-8
# Author:Yang
product_list=[]
with open("F:/homework/day2/homeworkday2.txt") as f:
    for line in f:
        product_list.append(list(line.strip('\n').split(',')))
shopping_list = []
with open("F:/homework/day2/homeworkday2_spl.txt") as f:
    for line in f:
        shopping_list.append(list(line.strip('\n').strip(',')))
print("用户入口".center(40,"-"))
salary = (input("please input your salary:"))
if salary.isdigit():
    salary=int(salary)
    while True:
        #for item in product_list:
         for index,item in enumerate(product_list):
            #print(product_list.index.html(item),item)
            print(index,item)
         user_choice = input("选择要买吗>>>:")
         if user_choice.isdigit():
             user_choice=int(user_choice)
             if user_choice < len(product_list) and user_choice >=0:
                 p_item = product_list[user_choice]
                 p_item[1]=int(p_item[1])
                 if p_item[1] <= salary: # 买得起
                     shopping_list.append(p_item)
                     salary -=p_item[1]
                     print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item,salary))
                 else:
                     print("\033[41:1m你的余额只剩[%s]\033[0m" % salary)
             else:
                 print("product code [%s] is not exist!",user_choice)

         elif user_choice == 'q':
             with open("F:/homework/day2/homeworkday2_spl.txt","+w") as f:
               print("-------shopping list------")
               for index,item in enumerate(shopping_list):
                print(index,item)
                shopping_list_str="\n".join(str(s) for s in shopping_list)
                wirte_str=((shopping_list_str.replace("[","")).replace("]","")).replace("'","")
                f.write(wirte_str)
             with open("F:/homework/day2/homeworkday2_sly.txt","+a") as f:
               print("Your current balance:",salary)
               f.write("Your current balance:"+str(salary)+'\n')

               exit()
         else:
             print("invalid option")




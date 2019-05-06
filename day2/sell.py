#!/usr/bin/env python
# coding:utf-8
# Author:Yang
#
# product = input("please input a product:")
# price = input("please input the price of product:")
product_list = []
with open("F:/homework/day2/homeworkday2.txt") as f:
    for line in f:
        product_list.append(list(line.strip('\n').split(',')))
#print(product_list)
print("商家入口".center(40,"-"))
print("1.查看商品列表\n2.添加商品\n3.修改商品")
choice = input("pleace choose an operation:")

if choice.isdigit():
    if choice == "1": # 选择1得到商品列表
       for index,item in enumerate(product_list):
         print(index,item)
    elif choice == "2": # 选择2进行新增商品
        product_add = input("please input a product:")
        price_add = input("please input the price of the %s:"%(product_add))
        # add_list=[product_add,price_add]
        # product_list.append(add_list)
        with open('F:/homework/day2/homeworkday2.txt',"a+") as f:
            f.write('\n'+product_add+','+price_add)
    elif choice == "3": # 选择3进行修改商品
        for index, item in enumerate(product_list):
            print(index, item)
        product_index = int(input("please input the index.html of product:")) # 输入要修改的商品编号
        print("1.alter product name\n2.alter product price") # 选择修改商品名或者商品价格
        product_alter = input("please input the choice:")
        if product_alter == "1":
            product_name = (input("please input the new name of product:"))
            product_list[product_index][0]=product_name
        elif product_alter == "2":
            product_price = input("please input the new price of product:")
            product_list[product_index][1]=product_price
        else:
            print("invoid operation")

        product_list_str="\n".join(str(s) for s in product_list) # 商品列表list转str
        write_str=(product_list_str.replace('[','')).replace(']','').replace("'","").replace(" ","") # 分割字符串
        with open("F:/homework/day2/homeworkday2.txt","+w") as f:
            f.write(write_str)
    else:
        print("invoid operation")
else:
        print("invoid operation")
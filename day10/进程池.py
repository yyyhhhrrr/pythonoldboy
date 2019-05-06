#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from multiprocessing import Process,Pool,freeze_support

# 在windows上启动多进程跟linux不一样 ，要import freeze_support或者加if __name__=='__main__'

import time
import os
def Foo(i):
    time.sleep(2)
    print("in process ",os.getpid())
    return  i+100

def Bar(arg):
    print("--->exec done:",arg)

if __name__=='__main__':
    #freeze_support()
    pool=Pool(5) # 和 pool=Pool(process=5)一样  意思为 允许进程池同时放入5个进程，同时运行的进程只有五个

    for i in range(10):# 启动了 但是被放进进程池的进程才会运行
        pool.apply_async(func=Foo,args=(1,),callback=Bar)  # callback=回调  执行完Foo 再执行Bar ，注意:回调是主进程调用的而不是子进程,例如备份数据库时候只用父进程创建连接，子进程去回调父进程的连接 而不用多次创建连接
        # pool.apply(func=Foo,args=(i,)) # 串行
        # pool.apply_async(func=Foo,args=(1,)) # 并行
    print('end')
    pool.close()
    pool.join() # 等所有进程结束 不写join 主进程不会等子进程结束

# 注意python的要求（官方文档都没写），先close再join（死记硬背），如果把join注释了，不等子进程执行完毕程序就关闭了
__author__ = "Alex Li"

from multiprocessing import Process, Manager
import os
# 进程间的共享数据
# 其实也是copy了十个数据 最后汇总，而且内部加了锁 ，不用人为加锁


def f(d, l):
    d[os.getpid()]=os.getpid()
    l.append(1)
    print(l,d)


if __name__ == '__main__':
    with Manager() as manager: # 和 manger=Manager() 一样
        d = manager.dict() # 生成一个可在多个进程之间共享、传递的字典

        l = manager.list(range(5)) # 生成一个可在多个进程之间共享、传递的list

        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list: # 等待结果
            res.join()
        l.append("from parent")
        print(d)
        print(l)
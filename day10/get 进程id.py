__author__ = "Alex Li"

from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name): # 用来子进程启动进程
    info('\033[31;1mcalled from child process function f\033[0m')
    print('hello', name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m') # 主进程启动的进程
    p = Process(target=f, args=('bob',)) # 子进程启动的进程
    p.start()
    # p.join()
__author__ = "Alex Li"

from multiprocessing import Process, Lock

# 进程锁
# 本身进程之间内存不共享，为什么还需要进程锁？
# 原因：主要是保证在屏幕上打印的时候不乱

def f(l, i):
    #l.acquire()
    print('hello world', i)
    #l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()
__author__ = "Alex Li"

import threading, time
# 信号量

def run(n):
    semaphore.acquire() # 信号量锁
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行  实际上是每出来一个就放进去一个
    for i in range(22):
        t = threading.Thread(target=run, args=(i,))
        t.start()
while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    #print(num)
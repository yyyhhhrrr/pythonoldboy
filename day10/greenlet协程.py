__author__ = "Alex Li"

from greenlet import greenlet
# 手动切换  gevent 封装了greenlet
def test1():
    print(12)
    gr2.switch() # 切换gr2
    print(34)
    gr2.switch()
def test2():
    print(56)
    gr1.switch() # 切换gr1
    print(78)

gr1 = greenlet(test1) #启动一个协程
gr2 = greenlet(test2)
gr1.switch()


# greenlet 手动切换
# gevent 自动切换
__author__ = "Alex Li"

import gevent
# 自动IO切换


def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')
def bar():
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')
def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")


gevent.joinall([
    gevent.spawn(foo), # 启动协程
    gevent.spawn(bar),
    gevent.spawn(func3),
])

# 代码中 sleep只是gevent模拟io消耗的时间代指类似于io的消耗的时间
# 运行过程为：foo 先打印第一句 然后遇到io 切换给bar打印第一句 然后遇到io 切换给func3 打印第一句 然后遇到io
# 又给foo 发现foo还在等io,就给bar bar 也在等io ，又给func3 io结束后 打印第二句，返回给foo 还在等io给bar,
# bar 等io结束打印第二句 发给foo,foo等待io结束 打印foo第二句
# 这个单线程的异步执行，只要2s ,但是不使用协程要3s,要2s是指单线程中io等待时间最多的点

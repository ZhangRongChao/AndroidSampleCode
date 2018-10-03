
"""全局解释器锁GIL"""

"""
    如果想要查看CPU的核心数，可以调用标准库模块multiprocessing中的函数cpu_count。
"""
import multiprocessing
print(multiprocessing.cpu_count())  # 8

"""
    先来做几个实验：
    
一、单进程或单线程
def do_sth():
    while True:
        pass

do_sth()
    打开活动监视器（macOS）或任务管理器（Windows），查看CPU占用率：100%。
这说明：单进程或单线程占满了八核CPU中的其中一核。

二、多进程
from multiprocessing import Process

def do_sth():
    while True:
        pass

Process(target=do_sth).start()
Process(target=do_sth).start()

do_sth()
    打开活动监视器（macOS）或任务管理器（Windows），查看CPU占用率：300%。
这说明：三个进程占满了八核CPU中的其中三核，因此，多进程可以实现并行（同时处理多个任务）从而发挥
多核CPU的最大功效。

三、多线程
from threading import Thread

def do_sth():
    while True:
        pass

Thread(target=do_sth).start()
Thread(target=do_sth).start()

do_sth()
    打开活动监视器（macOS）或任务管理器（Windows），查看CPU占用率：100%。
这说明：三个线程并没有占满八核CPU中的其中三核，而只占满了其中一核，因此，多线程并不能实现并行
（同时处理多个任务）而只能实现并发（交替处理多个任务）。
"""

"""
    我们编写的Python代码是通过Python解释器来执行的。通常使用的Python解释器是官方提供的CPython。
CPython中有一个GIL（Global Interpreter Lock，全局解释器锁），其作用相当于Lock，任何线程
在执行前必须先获得GIL，一个线程在获得GIL后其它线程就不能执行，直到该线程释放GIL。因此，GIL保证了
同一时刻只有一个线程可以执行，从而导致Python中的多线程不能实现并行。
    如果将CPython更换为其它的Python解释器，例如：JPython、IronPython、PyPy等，就不会存在
GIL的问题。
"""

"""
    对于IO密集型的任务，例如：网络请求、读写磁盘等，因为IO的速度远远低于CPU和内存的速度，所以，
绝大部分时间都在等待IO操作的完成，CPU的消耗很少。因此，IO密集型的任务在使用多线程时，GIL无法
利用多核的劣势体现得非常微弱。
    一个线程在进行IO操作之前，其获得的GIL总是会被释放，以允许其它线程在该线程等待IO操作的时候
获得GIL。
    对于计算密集型的任务，例如：科学计算、视频处理等，主要消耗的是CPU的资源，全靠CPU的运算能力。
因此，计算密集型的任务在使用多线程时，GIL无法利用多核的劣势体现得非常明显，此外，任务数越多，
花在任务切换的时间就越多，CPU执行任务的效率就越低。
    在没有IO操作时，GIL会在每隔100次操作后被释放（这个次数可以通过sys.setcheckinterval来调整）。
"""

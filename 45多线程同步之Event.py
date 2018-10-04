
"""多线程同步之Event"""

"""
    标准库模块threading中提供了一个类对象Event，也可以实现多线程间的同步。Event实例对象管理着
一个内部标志，通过改变这个内部标志的值，可以让一个线程给其它处于阻塞状态的线程发送一个事件信号，
从而唤醒这些线程让它们转为运行状态。
    Event的方法如下：
（1）set(self)
    将内部标志设置为true。
（2）is_set(self)
    内部标志是否被设置为true。
（3）clear(self)
    将内部标志设置为false。
（4）wait(self, timeout=None)
    当内部标志为false时，调用该方法的线程会被阻塞。
    直到另外一个线程调用了方法set()将内部标志设置为true，或者超过了参数timeout指定的时间，
被阻塞的线程才会转为运行状态。其中，参数timeout必须是一个浮点数，单位是秒。
    如果指定了参数timeout并且超时了，该方法返回False；否则，该方法返回True。
"""
from threading import Thread, Event, current_thread
import time

event = Event()
print(event.is_set())   # False

def do_sth():
    print('%s开始等待' % current_thread().getName())
    event.wait()
    print('%s结束等待' % current_thread().getName())

for i in range(3):
    Thread(target=do_sth).start()

time.sleep(2)

event.set()

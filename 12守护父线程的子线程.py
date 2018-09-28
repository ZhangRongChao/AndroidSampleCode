
"""守护父线程的子线程"""

"""
    在创建线程实例对象时，可以将参数daemon指定为True，从而将创建的线程设置为守护线程。此外，
也可以在调用方法start()之前调用线程实例对象的方法setDaemon(True)或将属性daemon的值设置为True，
从而将该线程设置为守护线程。
    守护线程是为了守护父线程而存在的子线程。当父线程结束时，守护线程就没有存在的意义了，因此，
守护线程会随着父线程的结束而立刻结束。
"""
import threading, time

print('父线程%s启动' % threading.current_thread().getName())

class MyThread(threading.Thread):
    def run(self):
        print('子线程%s启动' % threading.current_thread().getName())
        time.sleep(2)
        print('子线程%s结束' % threading.current_thread().getName())

mt = MyThread()
mt.setDaemon(True)
mt.start()

time.sleep(1)

print('父线程%s结束' % threading.current_thread().getName())

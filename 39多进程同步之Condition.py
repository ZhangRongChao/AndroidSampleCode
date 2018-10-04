
"""多进程同步之Condition"""

"""
    标准库模块multiprocessing中提供了一个类对象Condition，用于表示带触发条件的锁，以帮助我们处理
多进程间复杂的同步问题。Condition允许一个或多个进程等待触发条件，直到收到另外一个进程的通知。
    Condition除了具有Lock和RLock的方法acquire()和release()外，还有以下几个方法：
（1）__init__(self, lock=None)
    参数lock用于指定一个Lock或RLock实例对象作为底层的锁。
    默认值None表示会自动创建一个RLock实例对象作为底层的锁。
    调用Condition实例对象的方法acquire()和release()，其实调用的是底层的锁的相应方法。
（2）wait(self, timeout=None)
    该方法用于等待触发条件，直到收到另外一个进程的通知，或直到超过了参数timeout指定的时间。
其中，参数timeout必须是一个浮点数，单位是秒。
    调用该方法的进程必须已经获得了锁，否则会抛出异常RuntimeError。
    调用该方法后，进程会释放锁并被阻塞，还会被放到条件等待池中。
    如果超过了参数timeout指定的时间还没有收到另外一个进程的通知，该方法返回False；
当收到了另外一个进程的通知时，如果没有指定timeout或在timeout指定的时间内，该方法返回True。
    当收到了另外一个进程的通知，或超过了参数timeout指定的时间后，都会自动调用方法acquire()
试图获得锁，获得锁失败的进程会从条件等待池转移到锁等待池。当另外一个进程调用方法release()释放锁之后，
进程调度程序再从锁等待池中选择一个进程来获得锁。
（3）wait_for(self, predicate, timeout=None)
    该方法比上面的方法多了一个参数predicate，用于指定一个返回值为布尔值的函数，只要该函数的
返回值不为True就一直等待。因此，如果忽略掉timeout，调用该方法就相当于：
while not predicate():
    con.wait()
    调用该方法的进程必须已经获得了锁，否则会抛出异常RuntimeError。
    调用该方法后，进程会释放锁并被阻塞，还会被放到条件等待池中。
    如果超过了参数timeout指定的时间还没有收到另外一个进程的通知并且参数predicate指定的函数的
返回值还不为True，该方法返回False；否则，该方法返回参数predicate指定的函数的最后一次返回值。
    当收到了另外一个进程的通知，或超过了参数timeout指定的时间后，或参数predicate指定的函数的
返回值为True时，都会自动调用方法acquire()试图获得锁，获得锁失败的进程会从条件等待池转移到锁等待池。
当另外一个进程调用方法release()释放锁之后，进程调度程序再从锁等待池中选择一个进程来获得锁。
（4）notify(n=1)
    该方法用于通知条件等待池中等待触发条件的最多n个进程。
    被通知的所有进程都会自动调用方法acquire()试图获得锁，获得锁失败的进程会从条件等待池转移到锁等待池。
当另外一个进程调用方法release()释放锁之后，进程调度程序再从锁等待池中选择一个进程来获得锁。    
    调用该方法的进程必须已经获得了锁，否则会抛出异常RuntimeError。
    进程调用该方法后不会释放锁。
（5）notify_all()
    该方法用于通知条件等待池中等待触发条件的所有进程。
    被通知的所有进程都会自动调用方法acquire()试图获得锁，获得锁失败的进程会从条件等待池转移到锁等待池。
当另外一个进程调用方法release()释放锁之后，进程调度程序再从锁等待池中选择一个进程来获得锁。
    调用该方法的进程必须已经获得了锁，否则会抛出异常RuntimeError。
    进程调用该方法后不会释放锁。
    
    Condition也遵守了上下文管理协议，所以可以使用with语句。
"""
from multiprocessing import Process, Condition
import time

cond = Condition()

class MyProcess1(Process):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        # cond.acquire()

        with cond:
            print('%s说：1' % self.name)
            cond.notify()
            cond.wait()

            # 思考两秒之后再说
            time.sleep(2)
            print('%s说：11' % self.name)
            cond.notify()
            cond.wait()

            time.sleep(2)
            print('%s说：111' % self.name)
            cond.notify()

        # cond.release()

class MyProcess2(Process):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        time.sleep(1)
        # cond.acquire()

        with cond:
            # 思考两秒之后再说
            time.sleep(2)
            print('%s说：2' % self.name)
            cond.notify()
            cond.wait()

            time.sleep(2)
            print('%s说：22' % self.name)
            cond.notify()
            cond.wait()

            time.sleep(2)
            print('%s说：222' % self.name)

        # cond.release()

MyProcess1('Process1').start()
MyProcess2('Process2').start()

"""
Process1说：1
Process2说：2
Process1说：11
Process2说：22
Process1说：111
Process2说：222
"""

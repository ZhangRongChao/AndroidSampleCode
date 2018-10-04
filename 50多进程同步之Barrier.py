
"""多进程同步之Barrier"""

"""
    标准库模块threading中提供了一个类对象Barrier，也可以实现多线程间的同步。Barrier用于表示
阻挡线程的栅栏，如果在线程中调用栅栏的方法wait()，那么该线程就会被栅栏阻挡从而变为阻塞状态。
可以为栅栏指定一个阻挡强度，当被阻挡的线程数达到指定的阻挡强度时，栅栏就会被冲破，所有被栅栏
阻挡的线程都会变为运行状态。当栅栏被冲破之后，会自动恢复，继续阻挡前来的线程。

    Barrier的方法如下：
（1）__init__(self, parties, action=None, timeout=None)
    参数parties用于指定可以阻挡的最大线程数。
    参数action用于指定在栅栏即将被冲破之前被其中一个被阻挡的线程所调用的函数或lambda表达式。
    参数timeout用于指定所有调用方法wait()时的默认值。
（2）wait(self, timeout=None)
    该方法用于将当前线程被栅栏阻挡从而变为阻塞状态。
    参数timeout用于指定被阻塞的最长秒数，如果在指定的秒数后栅栏仍然没有被冲破，则将栅栏的状态
置为broken。
    该方法的返回值是0~(parties-1)之间的一个整数。
（3）reset(self)
    该方法将栅栏重置为初始状态。
    所有调用了方法wait()而被阻塞的线程，都会抛出异常BrokenBarrierError。
（4）abort(self)
    该方法将栅栏的状态置为broken。
    所有调用了方法wait()而被阻塞的线程，以及即将调用方法wait()的线程，都会抛出异常BrokenBarrierError。
    
    Barrier的属性如下：
（1）parties
    可以阻挡的最大线程数
（2）n_waiting
    当前被阻挡的线程数
（3）broken
    Barrier实例对象的状态是否为broken
"""
from multiprocessing import Process, Barrier, current_process
from time import sleep

def do_sth():
    print('%s数量凑够了，即将冲破栅栏！' % current_process().name)

bar = Barrier(3, action=do_sth)

class MyProcess(Process):
    def run(self):
        print('%s启动' % self.name)
        bar.wait()
        print('%s结束' % self.name)

for i in range(8):
    MyProcess().start()
    sleep(2)


"""多进程同步之Semaphore"""

"""
    标准库模块multiprocessing中提供了一个类对象Semaphore，用于表示信号量，它可以帮助我们控制
并发进程的最大数量，从而实现多进程之间的同步。
    以我们日常生活中的停车场为例，假设停车场有100个车位，一开始所有车位都是空的，这是如果同时
来了120辆车，看门人只允许其中100辆车进入，然后放下车拦，剩下的20辆车都必须在入口处等待，
此后来的所有车也都必须在入口处等待。如果有一辆车离开停车场，看门人得知后，打开入口处的车拦，
放入一辆。
    在这个示例中，每个车位都是一个资源，每辆车都好比一个进程，看门人好比是信号量，入口处的等待区
好比是信号量等待池。在信号量的内部维护着一个计数器，其初始值是一个正整数（相当于车位数）。
当有进程（车）想要使用资源（车位）时，先调用方法acquire()试图获得资源（车位），如果此时计数器
大于0（有车位），则信号量（看门人）把计数器减1，然后为该进程（车）分配一个资源（车位）；
如果调用方法acquire()时计数器为0（没有车位），则对应的进程（车）被阻塞，然后被放到信号量等待池
（入口处的等待区）。当有其它进程（车）使用完资源（车位）时，调用方法release()释放资源（车位），
信号量（看门人）把计数器加1，如果此时计数器为1并且信号量等待池（入口处的等待区）有处于等待的进程（车），
则选择一个进程（车），信号量（看门人）把计数器减1，然后为该进程（车）分配一个资源（车位）。
    《图解Python》
    
    Semaphore的方法如下：
（1）__init__(self, value=1)
    参数value用于指定内部计数器的初始值，默认值是1。
（2）acquire(blocking=True, timeout=None)
    参数blocking用于指定获得资源失败时进程是否被阻塞，默认值True表示被阻塞，False表示不阻塞。
    参数timeout用于指定阻塞的最长时间。当参数blocking指定为False时，不能指定参数timeout。
默认值None表示一直阻塞。当指定了参数timeout时，如果超过了指定的时间还没有获得资源成功，
则该方法返回False；如果在指定的时间获得资源成功，则该方法返回True。
    默认情况下（blocking指定为True，timeout指定为None），如果计数器大于0，那就减1，然后
该方法返回True；如果计数器为0，进程被阻塞，然后被放到信号量等待池，直到有另外一个进程调用了
方法release()并且当前进程被进程调度程序从信号量等待池中选中，计数器减1然后返回True。
（3）release()    

    信号量是Dijkstra发明的，最早用的是P()和V()，对应的方法是acquire()和release()。
    
    Semaphore也遵守了上下文管理协议，所以可以使用with语句。                                       
"""
from multiprocessing import Process, Semaphore
import time, random

sem = Semaphore(3)

class MyProcess(Process):
    def run(self):
        # sem.acquire()
        with sem:
            print('%s获得资源' % self.name)
            time.sleep(random.random() * 10)
        # sem.release()

for i in range(10):
    MyProcess().start()

"""
    如果调用release()的次数比调用acquire()的次数多，计数器的当前值就会超过它的初始值。
为了确保能够及时检测到程序中的这种bug，可以使用BoundedSemaphore替代Semaphore，这样，
一旦程序中出现这种bug，就会抛出异常ValueError。
    但是，官方文档中提到：On Mac OS X, this is indistinguishable from Semaphore。

from multiprocessing import BoundedSemaphore

sem = BoundedSemaphore(3)
sem.acquire()
sem.release()
sem.release()  # 在macOS平台上没有抛出异常ValueError
"""

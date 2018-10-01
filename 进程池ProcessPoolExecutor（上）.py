
"""进程池ProcessPoolExecutor（1）"""

"""
    标准库模块concurrent.futures中提供了一个类对象ProcessPoolExecutor，也用于表示进程池。
与Pool相比，ProcessPoolExecutor的功能和性能更加强大。

    ProcessPoolExecutor和ThreadPoolExecutor具有相同的接口方法。
    ProcessPoolExecutor的方法如下：
（1）__init__(self, max_workers=None, mp_context=None,
                 initializer=None, initargs=())
    参数max_workers用于指定进程池中所能容纳的最大进程数。如果不指定或指定为None，则进程池中
所能容纳的最大进程数为CPU的核数。
    参数mp_context用于指定启动进程的上下文，例如：SimpleQueue、Queue或Process。
    参数initializer用于指定在每个进程启动之前被调用的函数或lambda表达式。
    参数initargs用于指定传递给initializer的实参组成的元组。
（2）submit(self, fn, *args, **kwargs)
    该方法用于将需要进程池处理的任务交给进程池，此后会创建并启动由进程池管理的子进程。
    该方法相当于Pool的apply_async()。
    参数fn相当于参数target，用于指定被方法run()调用的函数或lambda表达式。
    参数args用于指定fn接收的个数可变的位置实参。
    参数kwargs用于指定fn接收的个数可变的关键字实参。
    该方法的返回值是一个Future实例对象，表示fn的执行。可以调用Future的方法result()得到fn的
返回值。方法result()是一个同步方法，也就是说，直到fn执行完毕之后方法result()才会返回。
（3）map(self, fn, *iterables, timeout=None, chunksize=1)
    该方法用于将需要线程池处理的全部任务交给线程池，此后会创建并启动由线程池管理的子线程。
    该方法与内置函数map(func, *iterables)的用法类似。
    参数fn相当于参数target，用于指定被方法run()调用的函数或lambda表达式。
    参数iterables用于指定fn接收的所有实参，它是个数可变的可迭代序列。可迭代序列的个数，就是在
每次调用fn时接收的实参的个数。
    该方法的返回值是一个迭代器对象。
（4）shutdown(self, wait=True)
    该方法用于通知executor释放正在使用的所有资源。
    该方法相当于close()和join()。
    参数wait用于指定方法在返回时是否等待。默认值True表示等待所有挂起的进程都执行完毕之后，
并且executor已经释放了所有相关的资源之后，该方法再返回。如果参数wait被指定为False，那么该方法
会立即返回，当所有挂起的进程都执行完毕之后executor会释放所有相关的资源。
    
    类对象ProcessPoolExecutor遵守了上下文管理协议，所以可以使用with语句，这样，在离开运行时
上下文时会自动调用方法shutdown(wait=True)。    
"""
from concurrent.futures import ProcessPoolExecutor
import time, random

print('父进程启动')

def do_sth(i):
    print('子进程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子进程%d结束，耗时%.2f秒' % (i, end - start))

"""
# 将进程池中所能容纳的最大进程数指定为3
ppe = ProcessPoolExecutor(max_workers=3)

# 将需要进程池处理的任务全部交给进程池，此后会创建并启动由进程池管理的子进程
for i in range(1, 11):
    ppe.submit(do_sth, i)

# 父进程被阻塞
# 进程池管理的所有子进程执行完之后，父进程再从被阻塞的地方继续执行
ppe.shutdown(wait=True)
"""

with ProcessPoolExecutor(max_workers=3) as ppe:
    # 将需要进程池处理的任务全部交给进程池，此后会创建并启动由进程池管理的子进程
    """
    for i in range(1, 11):
        ppe.submit(do_sth, i)
    """
    ppe.map(do_sth, range(1, 11))

print('父进程结束')

# 程序运行后会同时创建并启动3个子进程，第4个子进程要等前面3个中的某一个执行结束后才会创建并启动

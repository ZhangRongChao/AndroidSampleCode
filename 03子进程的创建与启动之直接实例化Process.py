
"""子进程的创建与启动之直接实例化Process"""

from multiprocessing import Process, current_process
import time

"""
    标准库模块multiprocessing中提供了一个类对象Process，用于表示进程。
    
    使用类对象Process创建并启动子进程的第1种方式为：
（1）根据类对象Process创建进程实例对象；
（2）调用进程实例对象的方法start()启动进程。
    调用方法start()后，会自动调用方法run()，方法run()会自动调用参数target指定的函数。
    《图解Python》

    Process的特殊方法__init__()的定义如下：  
def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
    调用特殊方法__init__()时必须指定关键字实参，其中：
（1）参数group用于指定进程实例对象所属的进程组，默认不属于任何进程组。
（2）参数target用于指定被方法run()调用的函数，默认没有函数被调用。
（3）参数name用于指定进程实例对象的名称，第n个子进程的默认名称为'Process-n'。此外，可以通过
属性name设置进程实例对象的名称。
（4）参数args用于指定target接收的位置参数，用元组表示，默认不接收位置参数。
（5）参数kwargs用于指定target接收的关键字参数，用字典表示，默认不接收关键字参数。
"""
print('父进程启动（%d--%s）' % (current_process().pid, current_process().name))

def do_sth(arg1, arg2):
    print('子进程启动（%d--%s）' % (current_process().pid, current_process().name))
    time.sleep(2)
    print('arg1 = %d，arg2 = %d' % (arg1, arg2))
    print('子进程结束（%d--%s）' % (current_process().pid, current_process().name))

# process = Process(target=do_sth, name='myprocess', args=(5, 8))
process = Process(target=do_sth, args=(5, 8))
process.start()

print('父进程结束（%d--%s）' % (current_process().pid, current_process().name))

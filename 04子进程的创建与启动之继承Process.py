
"""子进程的创建与启动之继承Process"""

"""
    使用类对象Process创建并启动子进程的第2种方式为：
（1）自定义继承自Process的类对象，重写特殊方法__init__()和方法run()；
（2）根据自定义的类对象创建进程实例对象；
（3）调用进程实例对象的方法start()启动进程。
    调用方法start()后，会自动调用重写后的方法run()。
    
    与第1种方式相比，相当于把参数target指定的函数的函数体转移到了方法run()中。因此，在创建
进程实例对象时无需再指定参数target。
    第1种方式创建进程实例对象时指定的其它参数，在第2种方式中可以传递给重写后的特殊方法__init__()。
    《图解Python》
"""
from multiprocessing import Process
from multiprocessing import current_process
import time

print('父进程启动（%d--%s）' % (current_process().pid, current_process().name))

class MyProcess(Process):
    def __init__(self, name, args):
        super().__init__(name=name)
        self.args = args

    def run(self):
        print('子进程启动（%d--%s）' % (current_process().pid, current_process().name))
        print('arg1 = %d，arg2 = %d' % self.args)
        time.sleep(2)
        print('子进程结束（%d--%s）' % (current_process().pid, current_process().name))

mp = MyProcess(name='myprocess', args=(5, 8))
mp.start()

print('父进程结束（%d--%s）' % (current_process().pid, current_process().name))
